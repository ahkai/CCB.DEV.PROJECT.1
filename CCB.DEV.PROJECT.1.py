from main_task import app
from flask import url_for,request, redirect, abort
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

MainAPIRouteArray = {}

# MainAPIRouteArray = {
#                         '10000001': 'getleveldata',
#                         '10000002': 'getlogicaldata',
#                         '10000003': 'getservicetype',
#                         '10000004': 'getservicetype2',
#                         '10000005': 'getserviceinfo',
#                         '10000006': 'updserviceinfo',
#                         '10000007': 'delserviceinfo',
#                         '10000008': 'updservicetype',
#                         '10000009': 'delservicetype',
#                         '10000010': 'getservicetype22'
#                   }

@app.route('/task', methods=['GET','POST'])
def task_main():
    vTaskArg = {}

#    if request.values.getlist():
    if request.values.get('service_id'):

        vTempstr = request.values.get('service_id')

        vTaskArg['service_id'] = vTempstr
        #vTaskArg['service_id'] = vTempstr.encode('ascii')

        if request.values.get('service_args'):
            vTempstr = request.values.get('service_args')

            vTaskArg['service_args'] = vTempstr
        else:
            vTaskArg['service_args'] = 'none'
    else:
        abort(404)

    # message_info = 'main_task.task_main() get request.arg = [ %s ], ' % vTaskArg
    # app.logger.info(message_info)

    vTaskurl = url_for( MainAPIRouteArray[ vTaskArg[ 'service_id' ] ],  _method=request.method)
    vTaskurl = vTaskurl + '?'+ vTaskArg[ 'service_args' ]

    print 'Taskurl:['+vTaskurl+']'

    with  app.test_client() as client:
        if request.method == 'GET':
            cli_response = client.get(vTaskurl, follow_redirects=True)
        else:
            if request.method == 'POST':
                cli_response = client.post(vTaskurl, follow_redirects=True)
            else:
                abort(404)

    vRetData = cli_response

    return vRetData




if __name__ == '__main__':
    app.run(host='0.0.0.0')

cli_response = {}
cli_response = app.test_client().post("/serviceinfoAAAA", follow_redirects=True)

if cli_response['Code'] == '0':
    print cli_response['Message']
else:
    TempRouteArray = cli_response['RowsArray'] 

    for TempObj in TempRouteArray:
        MainAPIRouteArray[TempObj.service_id] = TempObj.service_func


