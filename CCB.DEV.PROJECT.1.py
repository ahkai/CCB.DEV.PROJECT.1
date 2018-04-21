from main_task import app
from flask import url_for,request
from db_operation.db_route_def import *

@app.route('/task/<path:operation_id>', methods=['GET', 'POST'])
def task_main(operation_id):

    HtmlStr = "TEST Message!"

#    if(request.method = 'POST'):


    if( operation_id == "1" ):
        HtmlStr = url_for( 'GET_LOGICAL_DATA', app_id=10704, _method=request.method )


    return HtmlStr

if __name__ == '__main__':
    app.run(host='0.0.0.0')
