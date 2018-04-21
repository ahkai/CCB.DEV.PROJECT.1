from flask import  make_response, request
from db_operation.DBObject import *
import json

from main_task import app
from db_operation import my_db
from db_operation import my_db_level

@app.route('/database/<operation_id>')
def CONNECT_DB(operation_id):

    vMsg = ''
    vMyHtml = None

    vMyHtml = '%s%s%s' % ('Connect Str:', my_db.connectstr, '</br>')

    if operation_id == 'connect':
        vMyHtml = '%s%s' % (vMyHtml, 'Go into db connecton! </br>')
        vMsg = my_db.my_db_connect()
        vMyHtml = '%s%s%s%s' % (vMyHtml, 'Connect Msg:', vMsg, '</br>' )

    if 'Successful' in vMsg:
        vMyHtml = '%s%s' % (vMyHtml, 'Go into db insert! </br>')
        vMsg = my_db.my_db_insert_test1(1, 'yankai')
        vMyHtml = '%s%s%s%s' % (vMyHtml, 'Insert Msg:', vMsg, '</br>')

        vMyHtml = '%s%s' % (vMyHtml, 'Go into db query! </br>')
        vMsg = my_db.my_db_query_test1(  col2='none'  )
        vMyHtml = '%s%s%s%s' % (vMyHtml, ' Msg:', vMsg, '</br>')

    if my_db.db_connection_handle.connection_id is None:
        pass
    else:
        vMyHtml = '%s%s' % (vMyHtml, 'Go into db disconnect! </br>')
        vMsg = my_db.my_db_disconnect()
        vMyHtml = '%s%s%s%s' % ( vMyHtml, 'Disconnect Msg:', vMsg, '</br>')

    return vMyHtml

@app.route('/getlevel/<level_id>')
def GET_LEVEL_DATA(level_id):

    vMsg = ''
    vMyHtml = None

    vMyHtml = '%s%s%s' % ('Connect Str:', my_db_level.connectstr, '</br>')

    vMyHtml = '%s%s' % (vMyHtml, 'Go into db connecton! </br>')
    vMsg = my_db_level.my_db_connect()
    vMyHtml = '%s%s%s%s' % (vMyHtml, 'Connect Msg:', vMsg, '</br>' )

    if 'Successful' in vMsg:
    #     vMyHtml = '%s%s' % (vMyHtml, 'Go into db insert! </br>')
    #     vMsg = my_db_level.my_db_insert_test1(1, 'yankai')
    #     vMyHtml = '%s%s%s%s' % (vMyHtml, 'Insert Msg:', vMsg, '</br>')
    #
    #     vMyHtml = '%s%s' % (vMyHtml, 'Go into db query! </br>')
        vRetData = my_db_level.query_app_system()

        RetjsonStr = json.dumps(vRetData,encoding="UTF-8", ensure_ascii=False)
    #     vMyHtml = '%s%s%s%s' % (vMyHtml, ' Msg:', vMsg, '</br>')

    if my_db_level.db_connection_handle is not None:
        if my_db_level.db_connection_handle.connection_id is not None:
            if vRetData['Code'] is '1' :
                vMyHtml = '%s%s' % (vMyHtml, 'Go into db disconnect! </br>')
                vMsg = my_db_level.my_db_disconnect()
                vMyHtml = '%s%s%s%s' % ( vMyHtml, 'Disconnect Msg:', vMsg, '</br>')

                response = make_response( RetjsonStr )
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
                response.headers['Access-Control-Allow-Headers'] = 'Referer,Accept,Origin,User-Agent,x-requested-with,content-type'
                return response
    else:
         return 'Error',400

    return 'Error',400


@app.route('/getlogical', methods=['GET', 'POST'])
def GET_LOGICAL_DATA():

    app_id = 'none'

    if( request.method == 'POST' ):
        app_id = request.form('app_id')

    vMsg = my_db_level.my_db_connect()

    if 'Successful' in vMsg:
        vRetData = my_db_level.query_app_bind_logical(col1=app_id)

        RetjsonStr = json.dumps(vRetData,encoding="UTF-8", ensure_ascii=False)

    if my_db_level.db_connection_handle is not None:
        if my_db_level.db_connection_handle.connection_id is not None:
            if vRetData['Code'] is '1' :
                vMsg = my_db_level.my_db_disconnect()

                response = make_response( RetjsonStr )
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
                response.headers['Access-Control-Allow-Headers'] = 'Referer,Accept,Origin,User-Agent,x-requested-with,content-type'
                return response
    else:
         return 'Error',400

    return 'Error',400