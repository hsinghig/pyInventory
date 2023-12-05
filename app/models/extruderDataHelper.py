import pandas as pd
from app.extensions import db
from sqlalchemy import text

from app.models import tblextruder


def get_extruder_df():
    columns = ['ID', 'Location', 'Color', 'Width', 'Length', 'Date_created', 'Created_by', 'Modified_date']
    result = get_result(None)
    print(result)   
    df = pd.DataFrame(result, columns=columns)
    return df

def get_extruder_history_df(extruder_id):
    columns = ['ID', 'Location', 'Color', 'Width', 'Length', 'Date_created', 'Created_by', 'Modified_date']
    result = get_result(extruder_id=extruder_id)
    print(result)   
    df = pd.DataFrame(result, columns=columns)
    return df

def get_result(extruder_id):
    if extruder_id:
        stmt = get_select_hist_stmt(extruder_id=extruder_id)
    else:
        stmt = get_select_stmt()

    values = []
    with db.engine.connect() as conn:
        result = conn.execute(stmt)
        for i in result:
            
            data = {
                'ID': i[0], 
                'Location': i[10],
                'Color': i[9],
                'Width': i[14],
                'Length': i[4],
                'Date_created': i[5],
                'Created_by': i[13],
                'Modified_date': i[6]                
            }
            values.append(data)        
        return values
    
    print(values)
    return None


def isUpdateorInsert(color_id, width_id):
    values = []
    stmt = get_extruder_for_color_width(color_id=color_id, width_id=width_id)
    with db.engine.connect() as conn:
        result = conn.execute(stmt)
        if result:
            print('found an entry')
        else:
            print('not found an entry')


def get_select_stmt():
    stmt= '''
SELECT ip.tblextruder.id, ip.tblextruder.location_id, ip.tblextruder.color_id, ip.tblextruder.width_id, ip.tblextruder.length,
ip.tblextruder.CreatedDate, ip.tblextruder.ModifiedDate, ip.tblextruder.CreatedBy_id, ip.tblextruder.ModifiedBy_id, 
ip.tblcolor.name as colorname, ip.tblextruderlocation.name AS locationname, 
             ip.tbluser.firstname, ip.tbluser.lastname, ip.tbluser.email, ip.tblwidth.name AS widthname, ip.tbluser.isactive as useractive
FROM   ip.tblextruder INNER JOIN
             ip.tblcolor ON ip.tblextruder.color_id = ip.tblcolor.id INNER JOIN
             ip.tblextruderlocation ON ip.tblextruder.location_id = ip.tblextruderlocation.id INNER JOIN
             ip.tbluser ON ip.tblextruder.CreatedBy_id = ip.tbluser.id INNER JOIN
             ip.tblwidth ON ip.tblextruder.width_id = ip.tblwidth.id
    '''
    return text(stmt)


def get_select_hist_stmt(extruder_id):
    stmt= text('''
SELECT  hist.extruder_id, hist.location_id, hist.color_id, hist.width_id, hist.length, hist.CreatedDate, 
hist.ModifiedDate, hist.CreatedBy_id, hist.ModifiedBy_id, 
color.name as colorname, location.name as locationname, user1.firstname, user1.lastname, user1.email, width.name as widthname, user1.isactive as useractive
  FROM [ip].[tblextruderHist] hist
  inner join ip.tblcolor color on hist.color_id = color.id
  inner join ip.tblextruderlocation location on hist.location_id = location.id
  inner join ip.tbluser user1 on hist.CreatedBy_id = user1.id
  inner join ip.tblwidth width on hist.width_id = width.id
  where hist.extruder_id = :X
    ''')
    stmt = stmt.bindparams(X=extruder_id)
    return stmt

def get_extruder_for_color_width(color_id, width_id):
    stmt = text('''
            select id from ip.tblextruder where color_id = 1 and width_id = 25
                ''')
   # stmt = stmt.bindparams(X=color_id, Y=width_id)
    return stmt

def insert_extruder_data(locationId, colorId, widthId, length, createdDate, modifiedDate, 
                    createdById, modifiedById, weight):
    stmt = '''
        INSERT INTO ip.tblextruder(location_id, color_id, width_id, length, [CreatedDate],
                 [ModifiedDate], [CreatedBy_id], [ModifiedBy_id], weight) VALUES (
                :locationID, :colorId, :widthId, :length, :createdDate, :modifiedDate, 
                    :createdById, :modifiedById, :weight)
                '''
    values = [{
        'locationID': locationId, 
        'colorId': colorId, 
        'widthId': widthId, 
        'length': length, 
        'createdDate': createdDate, 
        'modifiedDate': modifiedDate, 
        'createdById': createdById, 
        'modifiedById': modifiedById,
        'weight': weight}]
    
    with db.engine.connect() as conn:
        conn.execute(text(stmt), values)
        conn.commit()

def update_extruder_data(id, locationId, length, modifiedDate, 
                    modifiedById, weight):
    stmt = '''
        UPDATE [ip].[tblextruder]
   SET [location_id] = :locationID
      ,[length] = :length      
      ,[ModifiedDate] = :modifiedDate     
      ,[ModifiedBy_id] = :modifiedById
      ,[weight] = :weight
 WHERE  id = :id
        '''


    values = {
        'id': id,
        'locationID': locationId,        
        'length': length,        
        'modifiedDate': modifiedDate,        
        'modifiedById': modifiedById,
        'weight': weight}
    
    with db.engine.connect() as conn:
        conn.execute(text(stmt), values)
        conn.commit()