import dbconfig
import pymysql

class DBHelper:
    '''
    A class to retrieve and insert data into the database
    '''
    def connect(self), database='bankloan',host='localhost'):
        return pymysql.connect(database=database,
          username=dbconfig.db_username,
          password=dbconfig.db_password,
          host=host
  
          )
