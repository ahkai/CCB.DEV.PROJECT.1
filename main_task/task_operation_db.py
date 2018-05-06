from flask_restful import Resource, reqparse
from sqlalchemy import func, text
from datetime import datetime

from models import *
from myutil import mysession_scope,my_make_response,GetTimeLine

class UpdateTaskInfo(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('task_id', type=str, location='args')
        reg_data.add_argument('service_id', type=str, location='args')
        reg_data.add_argument('task_begin', type=str, location='args')
        reg_data.add_argument('task_end', type=str, location='args')
        reg_data.add_argument('task_message', type=str, location='args')
        reg_data.add_argument('task_status', type=str, location='args')

        args = reg_data.parse_args()

        task_id = args['task_id']
        service_id = args['service_id']
        task_begin = args['task_begin']
        task_end = args['task_end']
        task_message = args['task_message']
        task_status = args['task_status']

        if task_message == '':
            task_message = 'none'
            args['task_message'] = 'none'

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        RetObj = {}

        if task_begin == '' and  task_end == '' :

            task_status = 0
            task_begin = datetime.now()

            args['task_begin'] = task_begin
            args['task_status'] = task_status

            vInsertRow = TaskInfo(  task_id=task_id,
                                    service_id=service_id,
                                    task_begin=task_begin,
                                    # task_end=task_end,
                                    task_message=task_message,
                                    task_status=task_status
                                )

            with mysession_scope(RetObj) as MySession:
                MySession.add(vInsertRow)

                RetObj['Code'] = '1'
                RetObj['TaskArgs'] = args

            if RetObj['Code'] == '0' :
                print "MySession Exception:[" + RetObj['Message'] + "]"
        else:

            task_end = datetime.now()
            args['task_end'] = task_end
            args['task_status'] = 1

            with mysession_scope( RetObj ) as MySession:
                MySession.query(TaskInfo).filter(TaskInfo.task_id == task_id).update(args)

                RetObj['Code'] = '1'
                RetObj['TaskArgs'] = args

            if RetObj['Code'] == '0' :
                print "MySession Exception:[" + RetObj['Message'] + "]"

        return my_make_response( RetObj )

class GetTaskMinData(Resource):

    def post(self):


        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        RetObj = {}
        vresult = ''
        vparam1 = ''

        vsqlstatement1 = "select now();"

        vsqlstatement2 = "select date_sub(now(), interval 1 hour)"

        vsqlstatement3 ="select c.type_id as ServiceType, " \
                                "DATE_FORMAT( concat(date(a.task_begin), ' ', hour(a.task_begin), ':', floor(minute(a.task_begin) / 30) * 30), '%Y-%m-%d %H:%i') as TaskStartTime, " \
                                "count(*) as TotalNum "\
                        "from task_info as a, service_info as b, service_type as c "\
                        "where a.task_begin >= :param1 and " \
                        "a.service_id = b.service_id and " \
                        "b.service_type = c.type_id " \
                        " group by 1, 2"

        arrRows = []
        vTimeLine = []

        with mysession_scope(RetObj) as MySession:
            vresult = MySession.execute( text( vsqlstatement2 ) )

            if vresult.cursor._rowcount > 0 :
                vMyRow = vresult.fetchone()

                vparam1 = str(vMyRow[0])
                vStartTime = vMyRow[0]
                vStartName = ''
                vTimeLine = GetTimeLine(vStartTime)
                vTimeLineObj = {}
                vTTimeLineObj = []
                vDataLine = []

                vresult = MySession.execute(text(vsqlstatement3), {"param1": vparam1})

                if vresult.cursor._rowcount > 0:

                    for index in range( vresult.cursor._rowcount ):
                        vMyRow = vresult.fetchone()
                        newobj = {}

                        for index2 in range( len( vMyRow ) ):
                            newobj[ vMyRow._parent.keys[index2].encode('ascii') ] = vMyRow[index2]

                        arrRows.append(newobj)

                        if vStartName == '':
                            vStartName = newobj['ServiceType']

                        if newobj['ServiceType'] != vStartName or index == (vresult.cursor._rowcount - 1 ):
                            vTimeLineObj['name'] = str(vStartName)
                            vTimeLineObj['type'] = 'line'

                            for index3 in range( len( vTimeLine )):
                                vDataLineData = 0
                                for index4 in range( len( arrRows)):
                                    vtempstr = arrRows[index4]['TaskStartTime'].encode('ascii')

                                    if vTimeLine[index3] == str(arrRows[index4]['TaskStartTime'].encode('ascii')):
                                        vDataLineData = arrRows[index4]['TotalNum']

                                vDataLine.append(vDataLineData)

                            vTimeLineObj['data'] = vDataLine

                            vStartName = newobj['ServiceType']
                            vTTimeLineObj.append(vTimeLineObj)
                            vTimeLineObj = {}

            RetObj['Code'] = '1'
            RetObj['TaskArgs'] = vTTimeLineObj
            RetObj['TimeLine'] = vTimeLine

        if RetObj['Code'] == '0' :
            print "MySession Exception:[" + RetObj['Message'] + "]"


        return my_make_response( RetObj )



def UpdateTaskInfoD(args):

    task_id = args['task_id']
    service_id = args['service_id']
    task_begin = args['task_begin']
    task_end = args['task_end']
    task_message = args['task_message']
    task_status = args['task_status']

    if task_message == '':
        task_message = 'none'
        args['task_message'] = 'none'

    MySQL_engine.execution_options(isolation_level="READ COMMITTED")

    RetObj = {}

    if task_begin == '' and task_end == '':

        task_status = 0
        task_begin = datetime.now()

        args['task_begin'] = task_begin
        args['task_status'] = task_status

        vInsertRow = TaskInfo(task_id=task_id,
                              service_id=service_id,
                              task_begin=task_begin,
                              task_message=task_message,
                              task_status=task_status
                              )

        with mysession_scope( RetObj ) as MySession :
            MySession.add(vInsertRow)

        if RetObj['Code'] == '0':
            print "MySession Exception:[" + RetObj['Message'] + "]"
        else:
            RetObj['Code'] = '1'
            RetObj['TaskArgs'] = args
    else:

        task_end = datetime.now()
        args['task_end'] = task_end
        args['task_status'] = 1

        with mysession_scope(RetObj) as MySession:
            MySession.query(TaskInfo).filter(TaskInfo.task_id == task_id).update(args)

            RetObj['Code'] = '1'
            RetObj['TaskArgs'] = args

        if RetObj['Code'] == '0':
            print "MySession Exception:[" + RetObj['Message'] + "]"

    return RetObj







