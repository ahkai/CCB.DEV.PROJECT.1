import mysql.connector

class Dbobject(object):

    vLog_Message = None

    def __init__(self, arg_host="localhost", arg_port="3306", arg_user="root", arg_password="111111", arg_database="mysql", arg_charset="utf8"):
        self.db_host = arg_host
        self.db_port = arg_port
        self.db_user = arg_user
        self.db_password = arg_password
        self.db_database = arg_database
        self.db_charset = arg_charset

        self.connectstr = 'host='+arg_host+',port='+arg_port+', user='+arg_user+',password='+arg_password+', database='+arg_database+', charset='+arg_charset

        self.db_connection_handle = None
        self.db_cursor = None

    def my_db_connect(self):

        vLog_Message = '</br>'

        try:
            #connect to database
            temp_con = None
            temp_con = mysql.connector.connect(host=self.db_host, port=self.db_port, user=self.db_user,password=self.db_password, database=self.db_database, charset=self.db_charset)

            if not temp_con:
                vLog_Message = "Connect Failed </br>"
            else:
                vLog_Message = "Connect Successful  </br>"

                self.db_connection_handle = temp_con
                self.db_cursor = self.db_connection_handle.cursor()

                vLog_Message = '%s%s%s%s' % (vLog_Message, ' ', self.db_connection_handle.connection_id, '</br>')

        except mysql.connector.Error, e:
            vLog_Message = '%s%s%s%s' % (vLog_Message, ' ', e.message, ' </br>')
            self.db_connection_handle = None

        return vLog_Message

    def my_db_disconnect(self):

        vLog_Message = '</br>'

        try:
            # close cursor

            self.db_cursor.close()

            # disconnect from databaes
            self.db_connection_handle.close()

            vLog_Message = "Close Successful  </br>"

        except mysql.connector.Error, e:
            vLog_Message = '%s%s%s%s' % (vLog_Message, ' ', e.message, '</br>')

        self.db_connection_handle = None
        self.db_cursor = None

        return vLog_Message

    def my_db_insert_test1(self, col1=0 , col2='none'):

        vLog_Message = '</br>'
        col1_value=int(col1)
        col2_value=col2
        try:
            insert_test1 = ("insert into test1( col1 ,col2 ) values( %s, %s )")
            data_array = ( col1_value , col2_value )

            #execute
            self.db_cursor.execute(insert_test1, data_array)

            #commit
            self.db_connection_handle.commit()

            vLog_Message = 'Insert Successful  </br>'

        except mysql.connector.custom_error_exception(), e:
        #except mysql.connector.Error, e:
            vLog_Message = '%s%s%s%s' % (vLog_Message, ' ', e.message, '</br>')

        return vLog_Message

    def my_db_query_test1(self, col1=None , col2=None):

        vCol1 = str( col1 )
        vCol2 = '%s%s%s' % ( '%', col2, '%' )

        vLog_Message = '</br>'
        query_str = 'SELECT col1, col2  FROM test1 '
        first_flag = 0
        vResult_set = 'Resule Set are Following: </br>'

        if  col1 is not None :
            query_str = '%s%s' % ( query_str, ' WHERE col1 = %s ' )
            first_flag = 1

        if col2 is not None:
            if first_flag == 0:
                query_str = '%s%s' % ( query_str, ' WHERE col2 LIKE %s ' )
                first_flag = 2
            else:
                query_str = '%s%s' % (query_str, ' AND col2 LIKE %s ')
                first_flag = 3

        try:
            query_test1 = query_str

            #vCol1 = '%s%s%s' % ("'", col1, "'")

            vLog_Message = '%s%s%s%s' % ( vLog_Message, 'Command Str:' , query_str, ' </br>')
            vLog_Message = '%s%s%s%s' % ( vLog_Message, 'First Flag:', str(first_flag), ' </br>')
            vLog_Message = '%s%s%s%s' % ( vLog_Message, 'Col1:', vCol1, ' </br>')
            vLog_Message = '%s%s%s%s' % ( vLog_Message, 'Col2:', vCol2, ' </br>')

            # execute
            if first_flag == 0:
                self.db_cursor.execute(query_test1)
            if first_flag == 1:
                self.db_cursor.execute(query_test1 , (vCol1,) )
            if first_flag == 2:
                self.db_cursor.execute(query_test1,  (vCol2,) )
            if first_flag == 3:
                self.db_cursor.execute(query_test1, ( vCol1, vCol2 ) )

            for ( col1, col2 ) in self.db_cursor:
                vResult_set = '%s%s%s' % ( vResult_set, "{}, {} ".format( col1, col2 ) , '</br>' )



            vLog_Message = '%s%s' % ( vLog_Message, 'Query Successful  </br>' )

        except mysql.connector.custom_error_exception() as e:
        #except mysql.connector.Error as e:
            vLog_Message = '%s%s%s%s' % (vLog_Message, 'custom_error_exception:', e.message, '</br>')
            #vLog_Message = '%s%s%s%s' % (vLog_Message, 'Error Msg1:', e2.message, '</br>')

        return  '%s%s' % ( vLog_Message, vResult_set )

    def query_app_system(self, col1=None , col2=None, col3=None):

        vCol1 = str( col1 )
        vCol2 = '%s%s%s' % ( '%', col2, '%' )

        vLog_Message = '</br>'
        query_str = 'SELECT app_id, app_ename, app_cname  FROM app_system '
        vResult_set = 'Resule Set are Following: </br>'

        result_array = []
        RetData = {}

        try:
            self.db_cursor.execute(query_str)

            for ( res ) in self.db_cursor:
                temp_array = {}

                temp_array['obj_id'] = res[0]
                temp_array['app_ename'] = res[1]
                temp_array['obj_name'] = res[2]

                #cname_str = res[2]
                #cname_str.encode('utf-8')
                #fencoding = chardet.detect(cname_str)
                #print fencoding
                #cname_str.encode('gb2312')
                #cname_str.decode('utf8').encode('gb2312')

                #temp_array['app_cname'] = unicode(cname_str, 'gbk')
                #temp_array['app_cname'] = cname_str.decode('utf-8')

                result_array.append(temp_array)

            RetData['Code'] = '1'
            RetData['LEVEL_1'] = result_array

            #RetjsonStr = json.dumps(RetData)

            vLog_Message = '%s%s' % ( vLog_Message, 'Query Successful  </br>' )

        except mysql.connector.custom_error_exception() as e:
        #except mysql.connector.Error as e:
            #vLog_Message = '%s%s%s%s' % (vLog_Message, 'custom_error_exception:', e.message, '</br>')
            #vLog_Message = '%s%s%s%s' % (vLog_Message, 'Error Msg1:', e2.message, '</br>')

            RetData['Code'] = '0'

        return  RetData

    def query_app_bind_logical(self, col1=None , col2=None, col3=None):

        vCol1 = str(col1)

        query_str = 'select a.logical_id, a.logical_name, a.logical_type, a.cpu_num, a.mem_num, a.os_type_id, d.type_desc, d.type_desc2 \
                     from logical_info a, app_system b, app_bind_logical c , software_model_type d \
                     where a.logical_id = c.logical_id and b.app_id = c.app_id and a.os_type_id = d.type_id and c.app_id = %s '

        result_array = []
        RetData = {}

        try:
            self.db_cursor.execute( query_str , (vCol1,))

            for ( res ) in self.db_cursor:
                temp_array = {}

                temp_array['logical_id'] = res[0]
                temp_array['logical_name'] = res[1]
                temp_array['logical_type'] = res[2]
                temp_array['cpu_num'] = res[3]
                temp_array['mem_num'] = res[4]
                temp_array['os_type_id'] = res[5]
                temp_array['type_desc'] = res[6]
                temp_array['type_desc2'] = res[7]

                result_array.append(temp_array)

            RetData['Code'] = '1'
            RetData['RowsArray'] = result_array

        except mysql.connector.custom_error_exception() as e:
            RetData['Code'] = '0'

        return  RetData

    def query_service_info(self, col1=None , col2=None, col3=None):

        vCol1 = str( col1 )
        vCol2 = '%s%s%s' % ( '%', col2, '%' )

        vLog_Message = '</br>'
        query_str = 'SELECT app_id, app_ename, app_cname  FROM app_system '
        vResult_set = 'Resule Set are Following: </br>'

        result_array = []
        RetData = {}

        try:
            self.db_cursor.execute(query_str)

            for ( res ) in self.db_cursor:
                temp_array = {}

                temp_array['app_id'] = res[0]
                temp_array['app_ename'] = res[1]
                temp_array['app_cname'] = res[2]

                #cname_str = res[2]
                #cname_str.encode('utf-8')
                #fencoding = chardet.detect(cname_str)
                #print fencoding
                #cname_str.encode('gb2312')
                #cname_str.decode('utf8').encode('gb2312')

                #temp_array['app_cname'] = unicode(cname_str, 'gbk')
                #temp_array['app_cname'] = cname_str.decode('utf-8')

                result_array.append(temp_array)

            RetData['Code'] = '1'
            RetData['LEVEL_1'] = result_array

            #RetjsonStr = json.dumps(RetData)

            vLog_Message = '%s%s' % ( vLog_Message, 'Query Successful  </br>' )

        except mysql.connector.custom_error_exception() as e:
        #except mysql.connector.Error as e:
            #vLog_Message = '%s%s%s%s' % (vLog_Message, 'custom_error_exception:', e.message, '</br>')
            #vLog_Message = '%s%s%s%s' % (vLog_Message, 'Error Msg1:', e2.message, '</br>')

            RetData['Code'] = '0'

        return  RetData