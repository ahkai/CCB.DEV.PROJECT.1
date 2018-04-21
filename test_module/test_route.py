from main_task import  app
from flask import  render_template, flash, request, make_response
from test_module.models import User

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

#
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
