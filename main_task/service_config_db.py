from flask import  make_response, request, json, jsonify
from flask_restful import Resource, reqparse
from contextlib import contextmanager
from sqlalchemy.orm import *
from models import *
from sqlalchemy import *
from datetime import datetime,time

#Session = sessionmaker( bind=MySQL_engine )
#Session.configure(bind=engine)  # once engine is available

@contextmanager
def mysession_scope():
    """Provide a transactional scope around a series of operations."""

    #MySQL_engine.execution_options(isolation_level="READ COMMITTED")
    SessionObject = sessionmaker(bind=MySQL_engine)

    MySession = SessionObject()

    try:
        yield MySession
        MySession.commit()
    except:
        MySession.rollback()
        raise
    finally:
        MySession.close()


def formatdatetime( arrobjs, colname ):

    arrNew = []

    for iCount in range(0, len(arrobjs), 1):
        objNew =  arrobjs[iCount]

        tempstr =  objNew[colname]
        objNew[colname] = str(tempstr)

        # tempstr.replace('datetime.datetime(', '')
        # tempstr.replace(')', '')
        # tempstr = datetime(tempstr)

        arrNew.append(objNew)

    return arrNew

def my_make_response( RetObj ):
    RetjsonStr = json.dumps(RetObj, encoding="UTF-8", ensure_ascii=False)

    myresponse = make_response(RetjsonStr)

    myresponse.headers['Access-Control-Allow-Origin'] = '*'
    myresponse.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    myresponse.headers[
        'Access-Control-Allow-Headers'] = 'Referer,Accept,Origin,User-Agent,x-requested-with,content-type'

    return myresponse

class Getservicetype(Resource):

    def post(self):

        # reg_data = reqparse.RequestParser()
        # reg_data.add_argument('app_id', type=str, location='args')
        # args = reg_data.parse_args()
        #
        # app_id = args['app_id']

        # if (request.method == 'POST'):
        #     app_id = request.form('app_id')

        # MyConnect = MySQL_engine.execution_options(
        #     isolation_level="READ COMMITTED"
        # )
        #
        # connection.execution_options(stream_results=True). \
        #     execute(stmt)

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        with mysession_scope() as MySession:
            vQuery = MySession.query( ServiceType ).filter(ServiceType.type_level==1).order_by( ServiceType.obj_id )

            vtServiceTypes = vQuery.all()

            arrRows = []
            for vtServiceType in vtServiceTypes:
                arrRows.append( vtServiceType.toDict() )

        arrRows = formatdatetime( arrRows, 'type_date')
        #print jsonify( arrRows )
        #print arrRows
        #print json.dumps(arrRows, cls=new_alchemy_encoder(), check_circular=False)

        RetObj = {}
        RetObj['Code'] = '1'
        RetObj['LEVEL_1'] = arrRows

        return my_make_response( RetObj )


class Getservicetype2(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('type_id', type=str, location='args')
        args = reg_data.parse_args()

        type_id = args['type_id']

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        with mysession_scope() as MySession:
            vQuery = MySession.query( ServiceType ).filter(ServiceType.type_level==2).filter(ServiceType.type_uplevel==type_id).order_by( ServiceType.obj_id )

            vtServiceTypes = vQuery.all()

            arrRows = []
            for vtServiceType in vtServiceTypes:
                arrRows.append( vtServiceType.toDict() )

        arrRows = formatdatetime( arrRows, 'type_date')

        RetObj = {}
        RetObj['Code'] = '1'
        RetObj['LEVEL_2'] = arrRows

        return my_make_response( RetObj )

class Getserviceinfo(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('service_type', type=str, location='args')
        args = reg_data.parse_args()

        service_type = args['service_type']

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        with mysession_scope() as MySession:
            vQuery = MySession.query( ServiceInfo ).filter(ServiceInfo.service_type==service_type).order_by( ServiceInfo.service_id )

            vtServiceTypes = vQuery.all()

            arrRows = []
            for vtServiceType in vtServiceTypes:
                arrRows.append( vtServiceType.toDict() )

        arrRows = formatdatetime( arrRows, 'service_date')

        RetObj = {}
        RetObj['Code'] = '1'
        RetObj['RowsArray'] = arrRows

        return my_make_response( RetObj )

class Updserviceinfo(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('service_id', type=str, location='args')
        reg_data.add_argument('service_type', type=str, location='args')
        reg_data.add_argument('service_name', type=str, location='args')
        reg_data.add_argument('service_desc', type=str, location='args')
        reg_data.add_argument('service_url', type=str, location='args')
        reg_data.add_argument('service_func', type=str, location='args')
        reg_data.add_argument('service_owner', type=str, location='args')
        reg_data.add_argument('service_date', type=str, location='args')
        reg_data.add_argument('service_status', type=str, location='args')
        args = reg_data.parse_args()

        service_id = args['service_id']
        service_type = args['service_type']
        service_name = args['service_name']
        service_desc = args['service_desc']
        service_url = args['service_url']
        service_func = args['service_func']
        service_status = args['service_status']
        service_owner = args['service_owner']
        service_date = args['service_date']

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        if service_id == 'AUTO' :

            with mysession_scope() as MySession:
                vQuery = MySession.query( func.max(ServiceInfo.service_id).label('col1') ).all()

                # vtServiceTypes = vQuery.all()

            for tempitem in vQuery:
                MaxService_id = tempitem.col1 + 1

            args['service_id'] = MaxService_id
            args['service_date'] = ''

            # service_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            service_date = datetime.now()
            vInsertRow = ServiceInfo( service_id=MaxService_id,
                                      service_type=service_type,
                                      service_name=service_name,
                                      service_desc=service_desc,
                                      service_func=service_func,
                                      service_url=service_url,
                                      service_date=service_date,
                                      service_status=service_status,
                                      service_owner=service_owner
                                      )

            with mysession_scope() as MySession:
                MySession.add(vInsertRow)

            with mysession_scope() as MySession:
                vtServiceTypes = MySession.query(ServiceInfo).filter(ServiceInfo.service_id == MaxService_id).all()

                arrRows = []
                for vtServiceType in vtServiceTypes:
                    arrRows.append(vtServiceType.toDict())

                arrRows = formatdatetime(arrRows, 'service_date')

            RetObj = {}
            RetObj['Code'] = 'redisplay'
            RetObj['RowsArray'] = arrRows

        else:
            with mysession_scope() as MySession:

                MySession.query(ServiceInfo).filter(ServiceInfo.service_id == service_id).update(args)

            RetObj = {}
            RetObj['Code'] = '1'
            RetObj['RowsArray'] = 'success'


        return my_make_response( RetObj )

class Delserviceinfo(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('service_id', type=str, location='args')
        args = reg_data.parse_args()

        service_id = args['service_id']

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        with mysession_scope() as MySession:
            MySession.query( ServiceInfo ).filter(ServiceInfo.service_id==service_id).delete()

        RetObj = {}
        RetObj['Code'] = '1'
        RetObj['RowsArray'] = 'AAAAA'

        return my_make_response( RetObj )

class Updservicetype(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('obj_id', type=str, location='args')
        reg_data.add_argument('obj_name', type=str, location='args')
        reg_data.add_argument('type_desc', type=str, location='args')
        reg_data.add_argument('type_level', type=str, location='args')
        reg_data.add_argument('type_uplevel', type=str, location='args')
        reg_data.add_argument('type_date', type=str, location='args')
        reg_data.add_argument('type_status', type=str, location='args')

        args = reg_data.parse_args()

        obj_id = args['obj_id']
        obj_name = args['obj_name']
        type_desc = args['type_desc']
        type_level = args['type_level']
        type_uplevel = args['type_uplevel']
        type_date = args['type_date']
        type_status = args['type_status']

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        if obj_id == 'AUTO' :

            with mysession_scope() as MySession:
                vQuery = MySession.query( func.max(ServiceType.obj_id).label('col1') ).all()

                # vtServiceTypes = vQuery.all()

            for tempitem in vQuery:
                MaxService_id = tempitem.col1 + 1

            # args['obj_id'] = MaxService_id
            # args['type_date'] = ''

            # service_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            type_date = datetime.now()
            vInsertRow = ServiceType( obj_id=MaxService_id,
                                      obj_name=obj_name,
                                      type_desc=type_desc,
                                      type_level=type_level,
                                      type_uplevel=type_uplevel,
                                      type_date=type_date,
                                      type_status=type_status
                                      )

            with mysession_scope() as MySession:
                MySession.add(vInsertRow)

            with mysession_scope() as MySession:
                vtServiceTypes = MySession.query(ServiceType).filter(ServiceType.obj_id == MaxService_id).all()

                arrRows = []
                for vtServiceType in vtServiceTypes:
                    arrRows.append(vtServiceType.toDict())

                arrRows = formatdatetime(arrRows, 'type_date')

            RetObj = {}
            RetObj['Code'] = 'redisplay'
            RetObj['RowsArray'] = arrRows

        else:
            with mysession_scope() as MySession:

                MySession.query(ServiceType).filter(ServiceType.obj_id == obj_id).update(args)

            RetObj = {}
            RetObj['Code'] = '1'
            RetObj['RowsArray'] = 'success'


        return my_make_response( RetObj )

class Delservicetype(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('obj_id', type=str, location='args')
        args = reg_data.parse_args()

        obj_id = args['obj_id']

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        with mysession_scope() as MySession:
            MySession.query( ServiceType ).filter(ServiceType.obj_id == obj_id).delete()

        RetObj = {}
        RetObj['Code'] = '1'
        RetObj['RowsArray'] = 'BBBBB'

        return my_make_response( RetObj )