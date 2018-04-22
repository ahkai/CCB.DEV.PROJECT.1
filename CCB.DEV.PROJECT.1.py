from main_task import app
from flask import url_for,request, redirect, abort


arrServiceRoute = {
                        '10000001': 'getleveldata',
                        '10000002':'getlogicaldata'
                    }


@app.route('/task', methods=['GET','POST'])
def task_main():
    vTaskArg = {}

#    if request.values.getlist():
    if request.values.get('service_id'):

        vTempstr = request.values.get('service_id')
        vTaskArg['service_id'] = vTempstr.encode('ascii')
        #vTaskArg['service_id'] = request.values.get('service_id').decode('ascii')

        if request.values.get('service_args'):
            vTempstr = request.values.get('service_args')
            vTaskArg['service_args'] = vTempstr.encode('ascii')
            #vTaskArg['service_args'] = request.values.get('service_args')
        else:
            vTaskArg['service_args'] = 'none'
    else:
        abort(404)
#    else:
#        abort(404)


    # vValueStr = request.get_json().get('service_id','')

    # if request.args.items():
    #     if request.args.get('service_id'):
    #         vTaskArg['service_id'] = request.args.get('service_id')
    #
    #         if request.args.get('service_args'):
    #             vTaskArg['service_args'] = request.args.get('service_args')
    #         else:
    #             vTaskArg['service_args'] = 'none'
    #     else:
    #         abort(404)
    # else:
    #     abort(404)

    message_info = 'main_task.task_main() get request.arg = [ %s ], ' % vTaskArg

    app.logger.info(message_info)

    # vTaskurl = url_for( 'getlogicaldata', vTaskArg_decode, _method=request.method)
    vTaskurl = url_for( arrServiceRoute[ vTaskArg[ 'service_id' ] ],  _method=request.method)
    vTaskurl = vTaskurl + '?'+ vTaskArg[ 'service_args' ]


    with  app.test_client() as client:
        if request.method == 'GET':
            cli_response = client.get(vTaskurl, follow_redirects=True)
        else:
            if request.method == 'POST':
                cli_response = client.post(vTaskurl, follow_redirects=True)
            else:
                abort(404)
                # raise exception page_not_found(404)

    #vRetData = '%s%s' % ( 'HAHAHHAHAHAH : ', cli_response.data )
    #vRetData = cli_response.data
    vRetData = cli_response

    return vRetData




if __name__ == '__main__':
    app.run(host='0.0.0.0')
