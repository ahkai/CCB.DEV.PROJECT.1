
from db_operation.db_object import DBObject
from main_task import app



# init database data
my_db = DBObject()
my_db_level = DBObject(arg_database='PT_DEMO')

app.secret_key = 'yankai'