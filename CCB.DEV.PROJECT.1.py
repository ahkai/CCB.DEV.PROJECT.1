from main_task import app
from flask import url_for,request, redirect, abort

@app.route('/task', methods=['GET','POST'])
def task_main():
    vTaskArg = {}

    if request.args.items():
        if request.args.get('service_id'):
            vTaskArg['service_id'] = request.args.get('service_id')

            if request.args.get('service_args'):
                vTaskArg['service_args'] = request.args.get('service_args')
            else:
                vTaskArg['service_args'] = 'none'
        else:
            abort(404)
    else:
        abort(404)

    message_info = 'main_task.task_main() get request.arg = [ %s ], ' % vTaskArg

    app.logger.info(message_info)

    # vTaskurl = url_for( 'getlogicaldata', vTaskArg_decode, _method=request.method)
    vTaskurl = url_for('getlogicaldata',  _method=request.method)
    vTaskurl = vTaskurl + '?'+ vTaskArg['service_args']


    with  app.test_client() as client:
        if request.method == 'GET':
            cli_response = client.get(vTaskurl, follow_redirects=True)
        else:
            if request.method == 'POST':
                cli_response = client.post(vTaskurl, follow_redirects=True)
            else:
                abort(404)
                # raise exception page_not_found(404)

    vRetData = '%s%s' % ( 'HAHAHHAHAHAH : ', cli_response.data )

    return vRetData




if __name__ == '__main__':
    app.run(host='0.0.0.0')
