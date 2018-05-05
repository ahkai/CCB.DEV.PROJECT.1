from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR
from sqlalchemy import create_engine, Column, inspect, ForeignKey



MySQL_engine = create_engine( 'mysql+mysqlconnector://root:111111@localhost:3306/PT_DEMO', echo=True)
MySQL_Base = declarative_base()


class ServiceType( MySQL_Base ):
    __tablename__ = 'service_type'

    # type_id      = Column( BIGINT(8), primary_key=True , autoincrement=False )
    # type_name    = Column( VARCHAR(100) )
    obj_id       = Column( 'type_id', BIGINT(8), primary_key=True , autoincrement=False )
    obj_name     = Column( 'type_name', VARCHAR(100) )
    type_desc    = Column( VARCHAR(300) )
    type_baseurl = Column( VARCHAR(300) )
    type_level   = Column( TINYINT(1) )
    type_uplevel = Column( BIGINT(8) )
    type_date    = Column( DATETIME )
    type_status  = Column( TINYINT(1) )

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
        #return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        # obj = {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
        # return json.dumps(obj)


class ServiceInfo( MySQL_Base ):
    __tablename__ = 'service_info'

    service_id      = Column( BIGINT(8) , primary_key=True , autoincrement=False )
    service_type    = Column( BIGINT(8) , ForeignKey('service_type.type_id') )
    service_name    = Column( VARCHAR(100) )
    service_desc    = Column( VARCHAR(300) )
    service_url     = Column( VARCHAR(100) )
    service_func    = Column( VARCHAR(100) )
    service_owner   = Column( VARCHAR(50) )
    service_date    = Column( DATETIME )
    service_status  = Column( TINYINT(1) )

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

class TaskInfo( MySQL_Base ):
    __tablename__ = 'task_info'

    task_id         = Column( VARCHAR(100) , primary_key=True , autoincrement=False )
    service_id      = Column( BIGINT(8) , ForeignKey('service_info.service_id') )
    task_begin      = Column( DATETIME )
    task_end        = Column( DATETIME )
    task_message    = Column( VARCHAR(300) )
    task_status     = Column( TINYINT(1) )

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}




