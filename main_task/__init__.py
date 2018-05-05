from flask import Flask

app = Flask(__name__)

app.secret_key = 'yankai'


from db_operation.db_route import db_operation_api
from main_task.main_route import  *

# cli_response = app.test_client().post("/serviceinfoAAAA", follow_redirects=True)

cli_response = GetmaintaskrouteALL()

MainAPIRouteArray = {}

if cli_response['Code'] == '0':
    print cli_response['Message']
else:
    TempRouteArray = cli_response['RowsArray']

    for TempObj in TempRouteArray:
        TempObj['service_func'] =  TempObj['service_func'].encode('ascii')
        TempObj['service_url'] = TempObj['service_url'].encode('ascii')

    for TempObj in TempRouteArray:
        MainAPIRouteArray[ str(TempObj['service_id']) ] = TempObj












