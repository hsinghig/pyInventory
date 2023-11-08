import sqlite3
import os

database_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/inventoryDB.db'
table = input("Show table (colors, widths, users, locations, extruder) or blank for all): ")
conn = sqlite3.connect(database_abs_path)

c = conn.cursor()

def show_colors():
    try:
        colorList = c.execute("SELECT * FROM colors")
        print("COLORS")
        print("#"*25)
        for row in colorList:
            print("ID: ", row[0])
            print("Name: ", row[1])
            print("isExtruderColor", row[2])
            print("isCrossPlyColor", row[3])
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to re-initialize the database.")
        conn.close()

def show_width():
    try:
        widthList = c.execute("SELECT * FROM widths")
        print("WIDTH")
        print("#"*25)
        for row in widthList:
            print("ID: ", row[0])
            print("width: ", row[1])
            print("isActive", row[2])
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to re-initialize the database.")
        conn.close()

def show_users():
    try:
        userList = c.execute("SELECT * FROM users")
        print("users")
        print("#"*25)
        for row in userList:
            print("ID: ", row[0])
            print("firstName: ", row[1])
            print("lastName: ", row[2])
            print("email: ", row[3])
            print("isActive: ", row[4])
            print("canDelete: ", row[5])
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to re-initialize the database.")
        conn.close()

def show_locations():
    try:
        locationList = c.execute("SELECT * FROM locations")
        print("locations")
        print("#"*25)
        for row in locationList:
            print("ID: ", row[0])
            print("Name: ", row[1])
            print("isExtruderLocation: ", row[2])
            print("isCrossPlyLocation: ", row[3])
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to re-initialize the database.")
        conn.close()

def show_extruder():
    try:
        userList = c.execute("SELECT * FROM extruder")
        print("extruder")
        print("#"*25)
        for row in userList:
            print("ID: ", row[0])
            print("locationID: ", row[1])
            print("colorID: ", row[2])
            print("widthID: ", row[3])
            print("length: ", row[4])
            print("weight: ", row[5])
            print("dateEST: ", row[6])
            print("userID: ", row[7])
            print("dateUTC: ", row[8])
            print("comments: ", row[9])
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to re-initialize the database.")
        conn.close()


if table == "colors":
    show_colors()
elif table == "width":
    show_width()
elif table== "users":
    show_users()
elif table=="locations":
    show_locations()
elif table=="extruder":
    show_extruder()
else:
    show_colors()
    show_width()
    show_users()
    show_locations()
    show_extruder()

conn.close()