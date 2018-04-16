from flask import Flask, render_template, flash, request, make_response
from models import User
import json
from db_operation import *


app = Flask(__name__)

my_db = db_operation()

my_db_level = db_operation(arg_database='PT_DEMO')

app.secret_key = 'yankai'

@app.route('/database/<operation_id>')
def connect_db(operation_id):

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


@app.route('/getlogical/<app_id>')
def GET_LOGICAL_DATA(app_id):

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


@app.route('/', methods=['GET', 'POST'])
def hello_world():

    content = "Hello World aaa!"

    response = make_response(render_template("homepage.html", content1=content))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Referer,Accept,Origin,User-Agent,x-requested-with,content-type'
    return response,200
    # return render_template("homepage.html", content1=content)

@app.route('/user/<user_id>')
def hello_user(user_id):
    vUser = None

    if int(user_id) == 1:
        vUser = User(12, 'ahkai')
    else:
        vUser = User(11, 'yuanyuan')

    return render_template("hellouser.html",vUser=vUser )

@app.route('/begin')
def first_login():
    return render_template("login.html")


@app.route('/user_login', methods=['POST'])
def user_login():
    vform = request.form

    vUser_name = vform.get('user_name')
    vUser_pw  = vform.get('user_pw')

    if not vUser_name:
        flash("please input user name !")
        return render_template("login.html")
    if not vUser_pw:
        flash("please input passwd !")
        return render_template("login.html")

    flash("Success!")
    return render_template("login.html")

@app.errorhandler(404)
def error_page(e):
    vUser = None
    vError = "error message!"
    return render_template("hellouser.html", vUser=vUser, vError=vError)

if __name__ == '__main__':
    app.run("192.168.232.11")
