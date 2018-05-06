from flask import  make_response, json
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy import false, inspect
import datetime

from main_task.models import MySQL_engine

@contextmanager
def mysession_scope( RetObj ):
    """Provide a transactional scope around a series of operations."""

    #MySQL_engine.execution_options(isolation_level="READ COMMITTED")
    SessionObject = sessionmaker( bind=MySQL_engine , autoflush=false , autocommit=false )

    MySession = SessionObject()

    # global errMessage, errFlag
    # errMessage = ''
    # errFlag = 0

    try:
        MySession.begin()
        yield MySession
        MySession.commit()

    except Exception, e:

        MySession.rollback()
        RetObj['Code'] = '0'
        RetObj['Message'] = str(e)

    finally:
        RetObj['Code'] = '1'
        RetObj['Message'] = 'db operation success'
        MySession.close()

@contextmanager
def mysession_scope2( RetObj ):
    """Provide a transactional scope around a series of operations."""

    #MySQL_engine.execution_options(isolation_level="READ COMMITTED")
    SessionObject = sessionmaker( bind=MySQL_engine , autoflush=false , autocommit=false )

    MySession = SessionObject()

    # global errMessage, errFlag
    # errMessage = ''
    # errFlag = 0

    try:
        MySession.begin()
        yield MySession
        MySession.commit()

    except Exception, e:

        MySession.rollback()
        RetObj['Code'] = '0'
        RetObj['Message'] = str(e)

    finally:
        MySession.close()

def row2dict(vQuerys):

    arrRows = []
    for vQuery in vQuerys:
        newobj = {}
        for index in range(len(vQuery)):
            newobj[vQuery._fields[index]] = vQuery[index]

        arrRows.append(newobj)

    return arrRows


def formatdatetime( arrobjs, colname ):

    arrNew = []

    for iCount in range(0, len(arrobjs), 1):
        objNew =  arrobjs[iCount]

        tempstr =  objNew[colname]
        objNew[colname] = str(tempstr)

        arrNew.append(objNew)

    return arrNew

def my_make_response( RetObj ):
    RetjsonStr = json.dumps(RetObj, encoding="UTF-8", ensure_ascii=False)

    myresponse = make_response(RetjsonStr)

    myresponse.headers['Access-Control-Allow-Origin'] = '*'
    myresponse.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    myresponse.headers[
        'Access-Control-Allow-Headers'] = 'Referer,Accept,Origin,User-Agent,x-requested-with,content-type'

    return myresponse

def GetTimeLine(vDT):

    newTL = []
    newDT = vDT
    newDT.strftime("%Y-%m-%d %H:%M:%S")

    # newTL.append(str(vDT))

    for index in range( 10 ):
        newDT = newDT + datetime.timedelta(minutes=1)
        tempstr = str(newDT.strftime("%Y-%m-%d %H:%M"))
        newTL.append(tempstr)

    return newTL
