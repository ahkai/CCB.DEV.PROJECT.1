from flask import  make_response, request, json
from flask_restful import Resource, reqparse
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from models import *

#Session = sessionmaker( bind=MySQL_engine )
#Session.configure(bind=engine)  # once engine is available

@contextmanager
def mysession_scope():
    """Provide a transactional scope around a series of operations."""

    MySession = sessionmaker(bind=MySQL_engine)
    MySession.connection(execution_options={'isolation_level': '"READ COMMITTED"'})

    try:
        yield MySession
        MySession.commit()
    except:
        MySession.rollback()
        raise
    finally:
        MySession.close()


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

        with mysession_scope() as MySession:
            vtServiceType = MySession.query( ServiceType ).order_by( ServiceType.type_id )

        print vtServiceType

        return 'Success'

        # if 'Successful' in vMsg:
        #     vRetData = my_db_level.query_app_bind_logical(col1=app_id)
        #
        #     RetjsonStr = json.dumps(vRetData, encoding="UTF-8", ensure_ascii=False)
        #
        # if my_db_level.db_connection_handle is not None:
        #     if my_db_level.db_connection_handle.connection_id is not None:
        #         if vRetData['Code'] is '1':
        #             vMsg = my_db_level.my_db_disconnect()
        #
        #             response = make_response(RetjsonStr)
        #             response.headers['Access-Control-Allow-Origin'] = '*'
        #             response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        #             response.headers[
        #                 'Access-Control-Allow-Headers'] = 'Referer,Accept,Origin,User-Agent,x-requested-with,content-type'
        #             return response
        # else:
        #     return 'Error', 400
        #
        # return 'Error', 400

class Getserviceinfo(Resource):

    def post(self):

        reg_data = reqparse.RequestParser()
        reg_data.add_argument('app_id', type=str, location='args')
        args = reg_data.parse_args()

        app_id = args['app_id']

        # if (request.method == 'POST'):
        #     app_id = request.form('app_id')

        vMsg = my_db_level.my_db_connect()

        if 'Successful' in vMsg:
            vRetData = my_db_level.query_app_bind_logical(col1=app_id)

            RetjsonStr = json.dumps(vRetData, encoding="UTF-8", ensure_ascii=False)

        if my_db_level.db_connection_handle is not None:
            if my_db_level.db_connection_handle.connection_id is not None:
                if vRetData['Code'] is '1':
                    vMsg = my_db_level.my_db_disconnect()

                    response = make_response(RetjsonStr)
                    response.headers['Access-Control-Allow-Origin'] = '*'
                    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
                    response.headers[
                        'Access-Control-Allow-Headers'] = 'Referer,Accept,Origin,User-Agent,x-requested-with,content-type'
                    return response
        else:
            return 'Error', 400

        return 'Error', 400
