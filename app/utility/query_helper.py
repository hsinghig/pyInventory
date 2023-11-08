from app.utility.db_helper import get_db
from app.utility.lookup_helper import INSERT_TABLE_EXTRUDER, SELECT_TABLE_EXTRUDER, SELECT_TABLE_LOCATIONS, SELECT_TABLE_USERS, SELECT_TABLE_WIDTHS, SELECT_TABLE_COLORS

def get_locations():
    conn = get_db()
    cursor = conn.cursor()
    items_from_database_extruder = cursor.execute(SELECT_TABLE_LOCATIONS)
    data = []    
    for row in items_from_database_extruder:
        item = {
            "id": row[0], "name": row[1], "isExtruderLocation": row[2], "isCrossPlyLocation": row[3]
        }
        data.append(item)

    itemsExtruder = []
    itemsCrossply = []
    for item in data:
        elem = (item['id'],item['name'])
        if (item['isExtruderLocation'] == 1):           
            itemsExtruder.append(elem)
        else:
            itemsCrossply.append(elem)
           
    return itemsExtruder, itemsCrossply

def get_colors():
    conn = get_db()
    cursor = conn.cursor()
    items = cursor.execute(SELECT_TABLE_COLORS)
    dataColors = []
    for row in items:
        item = {
            "id": row[0], "name": row[1], "isExtruderColor": row[2], "isCrossPlyColor": row[3]
        }
        dataColors.append(item)
    colorExtruder = []
    colorCrossPly = []
    for item in dataColors:
        elem = (item['id'], item['name'])
        if (item["isExtruderColor"] == 1):
            colorExtruder.append(elem)
        else:
            colorCrossPly.append(elem)

    return colorExtruder, colorCrossPly

def get_widths():
    conn = get_db()
    cursor = conn.cursor()
    items = cursor.execute(SELECT_TABLE_WIDTHS)
    dataWidths = []
    for row in items:
        elem = (row[0], row[1])
        if (row[2] == 1):
            item = {
            "id": row[0], "width": row[1], "isActive": row[2]
            }
            dataWidths.append(elem)
    return dataWidths

def get_users():
    conn = get_db()
    cursor = conn.cursor()
    items_from_db = cursor.execute(SELECT_TABLE_USERS)
    data = []
    for row in items_from_db:
        displayName = row[2] + ', ' + row[1] + ' (' + row[3] + ')'
        elem = (row[0], displayName)
        data.append(elem)
    return data

def insert_extruder(extruderData):
    conn = get_db()
    cursor = conn.cursor()
    cursor.executemany(INSERT_TABLE_EXTRUDER, extruderData)
    conn.commit()

def get_extruder_data():
    conn = get_db()
    cursor = conn.cursor()
    items_from_db = cursor.execute(SELECT_TABLE_EXTRUDER)
    data = []
    for row in items_from_db:
        data.append(row)
    return data