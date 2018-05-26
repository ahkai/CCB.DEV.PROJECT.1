from flask import Flask

app = Flask(__name__)

app.secret_key = 'yankai'


from db_operation.db_route import db_operation_api
from main_task.main_route import  *
from myutil_route import initmainroute


initmainroute()














