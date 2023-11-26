import pypyodbc as odbc
import pandas as pd
import pyodbc

server = 'tcp:dbpyinventory.database.windows.net,1433'
database = 'pyInventoryDB'
username = 'sqladmin'
pwd = 'Harsha77!'

def connectDB():
    connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server='+server+';Database='+database+';Uid='+username+';Pwd='+pwd+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
   # conn = odbc.connect(connection_string)
    conn = pyodbc.connect(connection_string)
    sql = '''
        SELECT TOP (1000) [id]
        ,[name]
        ,[isActive]
        ,[comment]
        FROM [ip].[tblwidth]
        '''
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)

if __name__ == '__main__':
    connectDB()