from main_task import app
from flask import url_for,request, json, Response


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



@app.route('/task', methods=['GET','POST'])
def task_main():

    vTaskArg = request.args.get('task_arg')

    vTaskArg_decode = vTaskArg.decode('utf-8')

    message_info = 'ARG = [ %s ], decode = [ %s ]' % (vTaskArg , vTaskArg_decode)

    app.logger.info(message_info)

    vTaskurl = url_for( 'getlogicaldata', vTaskArg_decode, _method=request.method)

    with  app.test_client() as client:
        cli_response = client.get(vTaskurl, follow_redirects=True)

    vRetData = '%s%s' % ( 'HAHAHHAHAHAH : ', cli_response.data )

    return vRetData


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



if __name__ == '__main__':
    app.run(host='0.0.0.0')
