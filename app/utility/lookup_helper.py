
SELECT_TABLE_LOCATIONS= """ SELECT id, name, isExtruderLocation, 
    isCrossPlyLocation from locations """

SELECT_TABLE_WIDTHS = """ SELECT id, width, isActive from widths where isActive = 1"""

SELECT_TABLE_COLORS = """ SELECT id, name, isExtruderColor, isCrossPlyColor
    from colors"""

SELECT_TABLE_USERS = """ SELECT id, firstName, lastName, email, isActive, canDelete 
    from users where isActive = 1 """

INSERT_TABLE_EXTRUDER = """INSERT INTO extruder(locationID, colorID, widthID, length, weight, 
    dateEST, userID, dateUTC, comments) VALUES (?,?,?,?,?,?,?,?,?) """

SELECT_TABLE_EXTRUDER = """ SELECT ext.id, ext.locationID, l.name as location, ext.colorID,  c.name as color, ext.widthID, 
    w.width as width, ext.length, ext.weight, ext.dateEST, ext.userID, u.lastName,  u.FirstName, u.email,
    ext.dateUTC, ext.comments from extruder ext 
    INNER JOIN locations l on l.id = ext.locationID
    INNER JOIN colors c on c.id = ext.colorID
    INNER JOIN widths w on w.id = ext.widthID
    INNER JOIN users u on u.id = ext.userID
"""