import sqlite3
import os
from datetime import datetime, timezone
import pytz

database_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/inventoryDB.db'
conn = sqlite3.connect(database_abs_path)

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS colors")
c.execute("DROP TABLE IF EXISTS widths")
c.execute("DROP TABLE IF EXISTS users")
c.execute("DROP TABLE IF EXISTS locations")
c.execute("DROP TABLE IF EXISTS extruder")
c.execute(""" CREATE TABLE colors(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          isExtruderColor INTEGER,
          isCrossPlyColor INTEGER
)""")

colorList = [
    ("BLACK",1,1), ("BLUE",1,1), ("GREEN",1,1), ("ORANGE",0,1), ("PURPLE",1,1), ("RED",0,1), ("YELLOW",1,1)
    ]
c.executemany("INSERT INTO colors (name, isExtruderColor, isCrossPlyColor) VALUES (?, ?, ?)", colorList)

c.execute(""" CREATE TABLE widths(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          width INTEGER,
          isActive INTEGER
)""")

widthList = [
    (87, 1), (93,1), (99, 1), (102, 1), (105, 1), (111, 1), (117,1)
]
c.executemany("INSERT INTO widths(width, isActive) VALUES (?,?)", widthList)

c.execute(""" CREATE TABLE users(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          firstName TEXT,
          lastName TEXT, 
          email TEXT,
          isActive INTEGER,
          canDelete INTEGER
)
          """)

userList = [
    ("Nathan", "Kyle", "nkyle@impact-guard.com", 1, 1),    
    ("Mike", "Maravola", "mmaravola@impact-guard.com", 1, 1), 
    ("Hemant", "Singh", "hsingh@impact-guard.com", 1, 1), 
    ("Sam", "Osten", "sosten@impact-guard.com", 1, 1),
    ("Scott", "Gainar", "sgainar@impact-guard.com", 1, 0)
]
c.executemany("INSERT INTO users(firstName, lastName, email, isActive, canDelete) VALUES (?, ?, ?, ?, ?)", userList)

c.execute(""" CREATE TABLE locations(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          isExtruderLocation INTEGER,
          isCrossPlyLocation INTEGER
)""")
locationList = [
    ("EXT A", 1, 0), ("EXT B", 1, 0), ("X-Ply A", 0, 1), ("X-Ply B", 0, 1)
]
c.executemany("INSERT INTO locations(name, isExtruderLocation, isCrossPlyLocation) VALUES (?, ? , ?)", locationList)
c.execute(""" CREATE TABLE extruder(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          locationID INTEGER, 
          colorID INTEGER,
          widthID INTEGER,
          length INTEGER,
          weight INTEGER,
          dateEST TEXT,
          userID INTEGER,
          dateUTC TEXT, 
          comments TEXT
)""")
utc_time = datetime.utcnow()

    # Make it aware of the UTC timezone
utc_time = utc_time.replace(tzinfo=pytz.utc)

    # Convert it to EST timezone
est_time = utc_time.astimezone(pytz.timezone("US/Eastern"))

extruderList = [
    (1, 1, 1, 200, 20, est_time, 1, utc_time, "initial db entry")
]
c.executemany("INSERT INTO extruder(locationID, colorID, widthID, length, weight, dateEST, userID, dateUTC, comments) VALUES (?,?,?,?,?,?,?,?,?)", extruderList)


conn.commit()
conn.close()