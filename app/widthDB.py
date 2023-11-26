import pyodbc
from dbconnect import server, username, pwd, database

class WidthDatabase:
    def __init__(self):
        connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server='+server+';Database='+database+';Uid='+username+';Pwd='+pwd+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        self.conn = pyodbc.connect(connection_string)
        self.cursor = self.conn.cursor()

    def get_widths(self):
        query = "SELECT [id],[name],[isActive],[comment] FROM [ip].[tblwidth] where isActive = 'True'"
        self.cursor.execute(query)
        result = []
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict['id'] = row[0]
            item_dict['name']  = row[1]
            item_dict['isActive'] = row[2]
            item_dict['comment'] = row[3]
            result.append(item_dict)
        
        print(result)        

    def get_width(self, width_id):
        pass 

    def add_width(self, name, isActive):
        pass

if __name__ == '__main__':
    db = WidthDatabase()
    db.get_widths()

        