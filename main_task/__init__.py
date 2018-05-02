from flask import Flask
from flask import url_for,request, redirect, abort

app = Flask(__name__)

app.secret_key = 'yankai'


from db_operation.db_route import *
from main_task.main_route import  *












