from flask_restful import Resource, reqparse
from sqlalchemy import func
from datetime import datetime

from models import *
from myutil import mysession_scope,my_make_response

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





