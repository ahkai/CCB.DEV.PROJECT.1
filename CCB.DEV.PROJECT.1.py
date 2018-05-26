from main_task import app
from main_task.mysnowflake import gen_id
from main_task.task_operation_db import UpdateTaskInfoD
from main_task.service_config_db import makeroutearray ,MainAPIRouteArray

from flask import url_for,request, redirect, abort
import sys, uuid


from main_task.myutil_route import MainAPIRouteArray

# from threading import current_thread
# mythread = current_thread()
# print mythread.getName()

reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

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

def geturl( vvTaskArg ):

    if MainAPIRouteArray.has_key( vvTaskArg['service_id'] ) is False:
        makeroutearray()

    if MainAPIRouteArray.has_key( vvTaskArg['service_id'] ):

        tempobj = MainAPIRouteArray[vvTaskArg['service_id']]

        tempfunc = tempobj['service_func']
        tempurl = tempobj['service_url']
        tempbaseurl = tempobj['type_baseurl']

        if tempfunc != 'none':
            return url_for(tempfunc)
        else:
            if tempurl == 'none':
                return tempbaseurl
            else:
                if len(tempbaseurl) == 1:
                    return tempurl
                else:
                    return tempbaseurl + tempurl
    else:
        return ''



@app.route('/task', methods=['GET','POST'])
def task_main():

    myTaskID = 0
    myLoopCount = 0

    TaskDetail = {}

    TaskDetail['task_id'] = ''
    TaskDetail['service_id'] = ''
    TaskDetail['task_begin'] = ''
    TaskDetail['task_end'] = ''
    TaskDetail['task_message'] = ''
    TaskDetail['task_status'] = ''

    # mythread = current_thread()
    # print 'AAA:'+str(mythread.ident)
    # print 'AAA:'+mythread.getName()

    vTaskArg = {}

#    if request.values.getlist():
    if request.values.get('service_id'):

        vTempstr = request.values.get('service_id')

        vTaskArg['service_id'] =  vTempstr.encode('ascii')
        #vTaskArg['service_id'] = vTempstr

        if request.values.get('service_args'):
            vTempstr = request.values.get('service_args')

            vTaskArg['service_args'] = vTempstr
        else:
            vTaskArg['service_args'] = 'none'
    else:
        abort(404)



    while myTaskID == 0:
        myTaskID = gen_id()
        myLoopCount = myLoopCount + 1

        if myLoopCount == 10:
            print 'Failed to initial the task id !'
            abort(404)

    TaskDetail['task_id'] = str(myTaskID)
    TaskDetail['service_id'] = vTaskArg['service_id']

    TaskDetail = UpdateTaskInfoD(TaskDetail)

    if TaskDetail['Code'] == '0':
        print 'Task:[' + TaskDetail['TaskArgs']['task_id'] + ']: Failed to insert the begin time!'
        abort(404)
    else:
        print 'Task:[' + TaskDetail['TaskArgs']['task_id'] + ']: Begin! ' + str(TaskDetail['TaskArgs']['task_begin'])

# Get the url address

    vTaskurl = geturl(TaskDetail['TaskArgs'])

    if vTaskurl == '':
        print 'No url was found! return error'
        abort(404)

    vTaskurl = vTaskurl + '?'+ vTaskArg[ 'service_args' ]

    print 'Taskurl:['+vTaskurl+']'

# send this web request to service address

    with  app.test_client() as client:
        if request.method == 'GET':
            cli_response = client.get(vTaskurl, follow_redirects=True)
        else:
            if request.method == 'POST':
                cli_response = client.post(vTaskurl, follow_redirects=True)
            else:
                abort(404)

    tempobj = TaskDetail['TaskArgs']
    TaskDetail = UpdateTaskInfoD(tempobj)

    if TaskDetail['Code'] == '0':
        print 'Task:[' + TaskDetail['TaskArgs']['task_id'] + ']: Failed to update the finish time!'
    else:
        print 'Task:[' + TaskDetail['TaskArgs']['task_id'] + ']: Successful finished! ' + str(TaskDetail['TaskArgs']['task_end'])

    vRetData = cli_response

    return vRetData


if __name__ == '__main__' and len(MainAPIRouteArray) :
    app.run(host='0.0.0.0', debug=True,threaded=True )
