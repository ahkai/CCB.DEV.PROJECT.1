from main_task import app
from flask import json, Response
from flask_restful import Api
from service_config_db import Getservicetype,Getservicetype2,Getserviceinfo,\
    Updserviceinfo,Delserviceinfo,Updservicetype,Delservicetype,Getservicetype22,\
    Getmaintaskroute,GetmaintaskrouteALL
from task_operation_db import UpdateTaskInfo,GetTaskMinData,GetTop10Service,GetLevel2Total,GetSYSinfo

main_task_api = Api(app, default_mediatype="application/json")
main_task_api.add_resource(Getservicetype, '/gatewayconf/servicetypea')
main_task_api.add_resource(Getservicetype2, '/gatewayconf/servicetypeb')
main_task_api.add_resource(Getserviceinfo, '/gatewayconf/serviceinfoc')
main_task_api.add_resource(Updserviceinfo, '/gatewayconf/serviceinfod')
main_task_api.add_resource(Delserviceinfo, '/gatewayconf/serviceinfoe')
main_task_api.add_resource(Updservicetype, '/gatewayconf/serviceinfof')
main_task_api.add_resource(Delservicetype, '/gatewayconf/serviceinfog')
main_task_api.add_resource(Getservicetype22, '/gatewayconf/serviceinfoh')
main_task_api.add_resource(Getmaintaskroute, '/gatewayconf/serviceinfoAAAA')
main_task_api.add_resource(UpdateTaskInfo, '/gatewaymanage/taskinfoa')
main_task_api.add_resource(GetTaskMinData, '/gatewaymanage/taskinfob')
main_task_api.add_resource(GetTop10Service, '/gatewaymanage/taskinfoc')
main_task_api.add_resource(GetLevel2Total, '/gatewaymanage/taskinfod')
main_task_api.add_resource(GetSYSinfo, '/gatewaymanage/taskinfoe')

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.errorhandler(403)
def page_not_found(error):
    content = json.dumps({"error_code": "403"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(404)
def page_not_found(error):
    content = json.dumps({"error_code": "404"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(400)
def page_not_found(error):
    content = json.dumps({"error_code": "400"})
    # resp = Response(content)
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    resp = Response_headers(content)
    return resp
    # return "error_code:400"


@app.errorhandler(410)
def page_not_found(error):
    content = json.dumps({"error_code": "410"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(500)
def page_not_found(error):
    content = json.dumps({"error_code": "500"})
    resp = Response_headers(content)
    return resp