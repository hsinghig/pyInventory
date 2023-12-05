from sqlalchemy import text
from app.extensions import db
from app.models import tblcolor, tblextruder, tblextruderlocation, tbluser, tblwidth

def get_colors_from_database():
    result = db.session.query(tblcolor).all()
    data = []
    for row in result:
        item = (row.id, row.name)       
        data.append(item)       
    return data

def get_width_from_database():
    result = db.session.query(tblwidth).all()
    data = []
    for row in result:
       item = (row.id, row.name) 
       data.append(item)       
    return data

def get_extruder_location_from_database():
    result = db.session.query(tblextruderlocation).all()
    data = []
    for row in result:
        item = (row.id, row.name) 
        data.append(item)       
    return data
 
def get_users_from_database():
    result = db.session.query(tbluser).all()
    data = []
    for row in result:
       item = (row.id, row.email) 
       data.append(item)       
    return data

def get_result_query(color_id, width_id):
    returnValue = 0
    result = db.session.query(tblextruder).filter(tblextruder.color_id == color_id).filter(tblextruder.width_id == width_id).all()
    if len(result) == 0:
        print('Insert')
    else:
        idvalue = result[0].id
        returnValue = idvalue
        print('update')
    return returnValue

def get_select_stmt():
    stmt= '''
SELECT ip.tblextruder.id, ip.tblextruder.location_id, ip.tblextruder.color_id, ip.tblextruder.width_id, ip.tblextruder.length,
ip.tblextruder.CreatedDate, ip.tblextruder.ModifiedDate, ip.tblextruder.CreatedBy_id, ip.tblextruder.ModifiedBy_id, 
ip.tblcolor.name as colorname, ip.tblextruderlocation.name AS locationname, 
             ip.tbluser.firstname, ip.tbluser.lastname, ip.tbluser.email, ip.tblwidth.name AS widthname, ip.tbluser.isactive as useractive
FROM   ip.tblextruder INNER JOIN
             ip.tblcolor ON ip.tblextruder.color_id = ip.tblcolor.id INNER JOIN
             ip.tblextruderlocation ON ip.tblextruder.location_id = ip.tblextruderlocation.id INNER JOIN
             ip.tbluser ON ip.tblextruder.id = ip.tbluser.id INNER JOIN
             ip.tblwidth ON ip.tblextruder.width_id = ip.tblwidth.id
    '''
    return text(stmt)

def get_color_name_for_id(colorID, colorList, widthList):
    colorName = ''
    for color in colorList:
        if str(color[0]) == str(colorID):
            colorName = color[1]
            exit
    return colorName

def get_width_name_for_id(widthID, widthList):
        width = ''
        for w in widthList:
            if str(w[0]) == str(widthID):
                width = width[1]
                exit
        return width