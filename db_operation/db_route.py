from flask_restful import Api
from main_task import app
from db_route_def import Connectdb,Getleveldata,Getlogicaldata

db_operation_api = Api(app, default_mediatype="application/json")
db_operation_api.add_resource(Connectdb, '/task_connect')
db_operation_api.add_resource(Getleveldata, '/getlevel')
db_operation_api.add_resource(Getlogicaldata, '/getlogical')


