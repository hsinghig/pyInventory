DATABASE_SERVER = 'dbpyinventory.database.windows.net'
DATABASE_NAME = 'pyInventoryDB'
DATABASE_UID = 'sqladmin'
DATABASE_PWD = 'Harsha77!'
SECRET_KEY = 'IMPACT_GUARD'

ALLOWED_IMAGE_EXTENSIONS = ["jpeg", "jpg", "png"]
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
RECAPTCHA_PUBLIC_KEY= "6Lfty"
RECAPTCHA_PRIVATE_KEY="6LFSDFFDY"

def get_formatted_conn():
     conn = 'mssql+pyodbc://'+DATABASE_UID+':' + DATABASE_PWD + '@'+ DATABASE_SERVER + '/' + DATABASE_NAME + '?driver=ODBC+Driver+17+for+SQL+Server'
     return conn
  