from flask_restful import Api
from main_task import app
from db_route_def import *

api = Api(app, default_mediatype="application/json")
api.add_resource(Connectdb, '/task_connect')
api.add_resource(Getleveldata, '/get_level')
api.add_resource(Getlogicaldata, '/get_logical')



