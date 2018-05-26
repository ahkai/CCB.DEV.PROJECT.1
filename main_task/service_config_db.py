from flask_restful import Resource, reqparse
from sqlalchemy import func
from datetime import datetime

from models import *
from myutil import mysession_scope,my_make_response,GetTimeLine,mysession_scope2,row2dict,formatdatetime

class Getservicetype(Resource):

    def post(self):

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        RetObj = {}

        with mysession_scope( RetObj ) as MySession:
            vQuery = MySession.query( ServiceType ).filter(ServiceType.type_level==1).order_by( ServiceType.obj_id )

            vtServiceTypes = vQuery.all()

            arrRows = []
            for vtServiceType in vtServiceTypes:
                arrRows.append( vtServiceType.toDict() )

            arrRows = formatdatetime( arrRows, 'type_date')

            RetObj['Code'] = '1'
            RetObj['LEVEL_1'] = arrRows

        if RetObj['Code'] == '0':
            print "MySession Exception:[" + RetObj['Message'] + "]"

        return my_make_response( RetObj )


class Getservicetype2(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('type_id', type=str, location='args')
        args = reg_data.parse_args()

        type_id = args['type_id']

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        RetObj = {}

        with mysession_scope( RetObj ) as MySession:
            vQuery = MySession.query( ServiceType ).filter(ServiceType.type_level==2).filter(ServiceType.type_uplevel==type_id).order_by( ServiceType.obj_id )

            vtServiceTypes = vQuery.all()

            arrRows = []
            for vtServiceType in vtServiceTypes:
                arrRows.append( vtServiceType.toDict() )

            arrRows = formatdatetime( arrRows, 'type_date')

            RetObj['Code'] = '1'
            RetObj['LEVEL_2'] = arrRows

        if RetObj['Code'] == '0':
            print "MySession Exception:[" + RetObj['Message'] + "]"

        return my_make_response( RetObj )

class Getservicetype22(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('obj_id', type=str, location='args')
        args = reg_data.parse_args()

        obj_id = args['obj_id']

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        RetObj = {}

        with mysession_scope( RetObj ) as MySession:
            vQuery = MySession.query( ServiceType ).filter(ServiceType.type_level==2).filter(ServiceType.type_uplevel==obj_id).order_by( ServiceType.obj_id )

            vtServiceTypes = vQuery.all()

            arrRows = []
            for vtServiceType in vtServiceTypes:
                arrRows.append( vtServiceType.toDict() )

            arrRows = formatdatetime( arrRows, 'type_date')

            RetObj['Code'] = '1'
            RetObj['RowsArray'] = arrRows

        if RetObj['Code'] == '0':
            print "MySession Exception:[" + RetObj['Message'] + "]"

        return my_make_response( RetObj )

class Getserviceinfo(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('service_type', type=str, location='args')
        args = reg_data.parse_args()

        service_type = args['service_type']

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        RetObj = {}

        with mysession_scope( RetObj ) as MySession:
            vQuery = MySession.query( ServiceInfo ).filter(ServiceInfo.service_type==service_type).order_by( ServiceInfo.service_id )

            vtServiceTypes = vQuery.all()

            arrRows = []
            for vtServiceType in vtServiceTypes:
                arrRows.append( vtServiceType.toDict() )

            arrRows = formatdatetime( arrRows, 'service_date')

            RetObj['Code'] = '1'
            RetObj['RowsArray'] = arrRows

        if RetObj['Code'] == '0':
            print "MySession Exception:[" + RetObj['Message'] + "]"

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

        args['service_func'] = args['service_func'].lower()
        service_id = args['service_id']
        service_type = args['service_type']
        service_name = args['service_name']
        service_desc = args['service_desc']
        service_url = args['service_url']
        service_func = args['service_func']
        service_status = args['service_status']
        service_owner = args['service_owner']
        service_date = args['service_date']

        RetObj = {}

        if service_name == '':
            service_name = 'none'
            args['service_name'] = 'none'

        if service_desc == '':
            service_desc = 'none'
            args['service_desc'] = 'none'

        if service_url == '':
            service_url = 'none'
            args['service_url'] = 'none'

        if service_func == '':
            service_func = 'none'
            args['service_func'] = 'none'

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        if service_id == 'AUTO' :

            with mysession_scope2( RetObj ) as MySession:
                vQuerys = MySession.query( func.max(ServiceInfo.service_id).label('col1') ).all()

                # vtServiceTypes = vQuery.all()
                if len(vQuerys) != 0:
                    for tempitem in vQuerys:
                        MaxService_id = tempitem.col1 + 1
                else:
                    MaxService_id = 10000001

                args['service_id'] = MaxService_id
                args['service_date'] = ''

                service_url = service_url.encode('ascii')

                service_url = service_url.replace('//', '/')

                print service_url

                if service_url[0] != '/' and service_url != 'none' :
                    service_url = '/' + service_url

                if service_url[ len(service_url) - 1 ] == '/' and len(service_url) != 1 :
                    service_url = service_url[ 0: (len(service_url) - 1 )]

                service_date = datetime.now()

                vInsertRow = ServiceInfo(service_id=MaxService_id,
                                         service_type=service_type,
                                         service_name=service_name,
                                         service_desc=service_desc,
                                         service_func=service_func,
                                         service_url=service_url,
                                         service_date=service_date,
                                         service_status=service_status,
                                         service_owner=service_owner
                                         )

                MySession.add(vInsertRow)

                vtServiceTypes = MySession.query(ServiceInfo).filter(
                    ServiceInfo.service_id == MaxService_id).all()

                arrRows = []
                for vtServiceType in vtServiceTypes:
                    arrRows.append(vtServiceType.toDict())

                arrRows = formatdatetime(arrRows, 'service_date')

                RetObj['Code'] = 'redisplay'
                RetObj['RowsArray'] = arrRows


            if RetObj['Code'] == '0':
                print "MySession Exception:[" + RetObj['Message'] + "]"
        else:
            service_url = service_url.encode('ascii')

            service_url = service_url.replace('//', '/')

            if service_url[0] != '/' and service_url != 'none' :
                service_url = '/' + service_url

            if service_url[len(service_url) - 1] == '/' and len(service_url) != 1:
                service_url = service_url[ 0: (len(service_url) - 1) ]

            args['service_url'] = service_url

            with mysession_scope( RetObj ) as MySession:
                MySession.query(ServiceInfo).filter(ServiceInfo.service_id == service_id).update(args)

                RetObj['Code'] = '1'
                RetObj['RowsArray'] = 'success'

            if RetObj['Code'] == '0':
                print "MySession Exception:[" + RetObj['Message'] + "]"

        return my_make_response( RetObj )

class Delserviceinfo(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('service_id', type=str, location='args')
        args = reg_data.parse_args()

        service_id = args['service_id']

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        RetObj = {}

        if service_id != 'AUTO':
            with mysession_scope( RetObj ) as MySession:
                MySession.query(ServiceInfo).filter(ServiceInfo.service_id == service_id).delete()

                RetObj['Code'] = '1'
                RetObj['RowsArray'] = 'AAAAA'

            if RetObj['Code'] == '0':
                print "MySession Exception:[" + RetObj['Message'] + "]"
        else:
            RetObj['Code'] = '1'
            RetObj['RowsArray'] = 'BBBBB'

        return my_make_response( RetObj )

class Updservicetype(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('obj_id', type=str, location='args')
        reg_data.add_argument('obj_name', type=str, location='args')
        reg_data.add_argument('type_desc', type=str, location='args')
        reg_data.add_argument('type_baseurl', type=str, location='args')
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
        type_baseurl = args['type_baseurl']

        if obj_name == '':
            obj_name = 'none'
            args['obj_name'] = 'none'

        if type_desc == '':
            type_desc = 'none'
            args['type_desc'] = 'none'

        if type_baseurl == '':
            type_baseurl = 'none'
            args['type_baseurl'] = 'none'

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        RetObj = {}

        if obj_id == 'AUTO' :

            with mysession_scope2( RetObj ) as MySession:
                vQuerys = MySession.query( func.max(ServiceType.obj_id).label('col1') ).all()

                if len(vQuerys) != 0:
                    for tempitem in vQuerys:
                        MaxService_id = tempitem.col1 + 1
                else:
                    MaxService_id = 10000001

                if type_level == '1':
                    type_baseurl = str(MaxService_id)
                else:
                    type_baseurl = type_baseurl.encode('ascii')

                    type_baseurl = type_baseurl.replace('//', '/')

                    if type_baseurl[0] != '/' and type_baseurl != 'none':
                        type_baseurl = '/' + type_baseurl

                    if type_baseurl[len(type_baseurl) - 1] == '/' and len(type_baseurl) != 1:
                        type_baseurl = type_baseurl[0: (len(type_baseurl) - 1)]

                type_date = datetime.now()
                vInsertRow = ServiceType(obj_id=MaxService_id,
                                         obj_name=obj_name,
                                         type_desc=type_desc,
                                         type_baseurl=type_baseurl,
                                         type_level=type_level,
                                         type_uplevel=type_uplevel,
                                         type_date=type_date,
                                         type_status=type_status
                                         )
                MySession.add(vInsertRow)

                vtServiceTypes = MySession.query(ServiceType).filter(ServiceType.obj_id == MaxService_id).all()

                arrRows = []
                for vtServiceType in vtServiceTypes:
                    arrRows.append(vtServiceType.toDict())

                arrRows = formatdatetime(arrRows, 'type_date')

                RetObj['Code'] = 'redisplay'
                RetObj['RowsArray'] = arrRows


            if RetObj['Code'] == '0':
                print "MySession Exception:[" + RetObj['Message'] + "]"

        else:

            type_baseurl = type_baseurl.replace( '//', '/' )

            if type_baseurl[0] != '/' and type_baseurl != 'none' :
                type_baseurl = '/' + type_baseurl

            if type_baseurl[len(type_baseurl) - 1] == '/' and len(type_baseurl) != 1 :
                type_baseurl = type_baseurl[0: (len(type_baseurl) - 1)]

            args['type_baseurl'] = type_baseurl

            with mysession_scope2(RetObj) as MySession:
                MySession.query(ServiceType).filter(ServiceType.obj_id == obj_id).update(args)

                vtServiceTypes = MySession.query(ServiceType).filter(ServiceType.obj_id == obj_id).all()

                arrRows = []
                for vtServiceType in vtServiceTypes:
                    arrRows.append(vtServiceType.toDict())

                arrRows = formatdatetime(arrRows, 'type_date')

                RetObj['Code'] = '1'
                RetObj['RowsArray'] = arrRows


            if RetObj['Code'] == '0':
                print "MySession Exception:[" + RetObj['Message'] + "]"


        return my_make_response( RetObj )

class Delservicetype(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('obj_id', type=str, location='args')
        args = reg_data.parse_args()

        obj_id = args['obj_id']

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        RetObj = {}

        if obj_id != 'AUTO':
            with mysession_scope2(RetObj) as MySession:
                vQuerys = MySession.query(ServiceType).filter( (ServiceType.type_level == 2) & (ServiceType.type_uplevel == obj_id) ).order_by(ServiceType.obj_id).all()

                if len(vQuerys) != 0:
                     RetObj['Code'] = '0'
                     RetObj['Message'] = 'It has secondary level catelog , please delete first!'

                     print "Delservicetype Message :[" + RetObj['Message'] + "]"
                else:
                    #with mysession_scope(RetObj) as MySession:
                    MySession.query( ServiceType ).filter(ServiceType.obj_id == obj_id).delete()

                    RetObj['Code'] = '1'
                    RetObj['RowsArray'] = 'BBBBB'

                    # if RetObj['Code'] == '0':
                    #     print "MySession Exception:[" + RetObj['Message'] + "]"

            if RetObj['Code'] == '0':
                print "MySession Exception:[" + RetObj['Message'] + "]"

        else:
            RetObj['Code'] = '1'
            RetObj['RowsArray'] = 'BBBBB'

        return my_make_response( RetObj )

class Getmaintaskroute(Resource):

    def post(self):

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        RetObj = {}

        with mysession_scope(RetObj) as MySession:
            vQuerys = MySession.query(  ServiceInfo.service_id,
                                        ServiceInfo.service_status,
                                        ServiceInfo.service_url,
                                        ServiceInfo.service_func,
                                        ServiceInfo.service_owner,
                                        ServiceInfo.service_date,
                                        ServiceType.type_baseurl)\
                                .filter(    (ServiceInfo.service_status > 0) &
                                            (ServiceInfo.service_type == ServiceType.obj_id) )\
                                .order_by(  ServiceInfo.service_id).all()

            if len(vQuerys) == 0:
                RetObj['Code'] = '0'
                RetObj['Message'] = 'do not find any API service , registed!'
            else:
                arrRows = []
                for vQuery in vQuerys:
                    arrRows.append(vQuery.toDict())

                arrRows = formatdatetime(arrRows, 'type_date')

                RetObj['Code'] = 'redisplay'
                RetObj['RowsArray'] = arrRows

        if RetObj['Code'] == '0':
            print "MySession Exception:[" + RetObj['Message'] + "]"

        return RetObj

def GetmaintaskrouteALL():

        MySQL_engine.execution_options(isolation_level="READ COMMITTED")

        RetObj = {}

        with mysession_scope2(RetObj) as MySession:
            # vQuerys = MySession.query(ServiceInfo).filter((ServiceInfo.service_type == main_obj_id) &
            #                                               (ServiceInfo.service_status == 1)).order_by(ServiceInfo.service_id).all()
            #vQuerys = MySession.query(ServiceInfo).filter((ServiceInfo.service_status == 2)).order_by(ServiceInfo.service_id).all()
            vQuerys = MySession.query(  ServiceInfo.service_id,
                                        ServiceInfo.service_status,
                                        ServiceInfo.service_url,
                                        ServiceInfo.service_func,
                                        ServiceInfo.service_owner,
                                        ServiceInfo.service_date,
                                        ServiceType.type_baseurl)\
                                .filter(    (ServiceInfo.service_status == 2) &
                                            (ServiceInfo.service_type == ServiceType.obj_id) )\
                                .order_by(  ServiceInfo.service_id).all()

            if len(vQuerys) == 0 :
                RetObj['Code'] = '0'
                RetObj['Message'] = 'do not find any API service , registed!'
            else:
                arrRows = []

                arrRows = row2dict(vQuerys)

                arrRows = formatdatetime(arrRows, 'service_date')


                RetObj['Code'] = 'redisplay'
                RetObj['RowsArray'] = arrRows

        if RetObj['Code'] == '0':
            print "MySession Exception:[" + RetObj['Message'] + "]"

        return RetObj




