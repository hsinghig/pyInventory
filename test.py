import pandas as pd
import os
import json
from pytz import datetime
import pytz
from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo

# tzdata

def get_convert_datetime(datePassed, orig_timezone, convert_timezone):
    dt = datetime.strptime(datePassed, '%Y-%m-%d %H:%M:%S')
    if orig_timezone == 'EST':
        dt = dt.astimezone(pytz.timezone('US/Eastern'))
        dt = dt.astimezone(pytz.UTC)
    
    if convert_timezone == 'EST':
        dt = (dt.replace(tzinfo=ZoneInfo('UTC')).astimezone(ZoneInfo('America/New_York')))
    
    if convert_timezone == 'UTC':
        dt = dt.astimezone(pytz.UTC)

    return dt

def get_date(numberOfDays: int):
    newDate = date.today()
    newDate =  newDate + timedelta(days = -1 * numberOfDays)   
    return newDate

def loadInventoryData():
    inventoryFilePath = 'app//data//inventoryData.xlsx'
    extruderDF = pd.read_excel(inventoryFilePath, sheet_name='Extruder')
    crossPlyDF = pd.read_excel(inventoryFilePath, sheet_name='CrossPly')
    print(extruderDF.head(3))
    print(crossPlyDF.head(3))
    return extruderDF, crossPlyDF

def getInventory():
    columns = [
        'Date', 'Location', 'Roll', 'Type', 'Color', 'Width', 'Length', 'Weight', 'Part No.'
    ]
    result = []
    extruderDF, crossPlyDF = loadInventoryData()
    rollsInExtruder = extruderDF['Roll'].unique()
    for rolls in rollsInExtruder:
        if rollInCrossPly(rolls, crossPlyDF=crossPlyDF):
            print(f'Roll {rolls} is in crossply sheet'.format(rolls))
            
        else:
            items = extruderDF['Roll'] == rolls
            filteredDF = extruderDF.loc[items]           
            item = filteredDF.iloc[-1]
            value = getDictObject(item)
            result.append(value)
          
        
    df = pd.DataFrame.from_records(result, columns=columns)
    print(df.head())
    df.to_excel("output.xlsx")

def getDictObject(item):
    data = {
        'Date': item['Date'], 
            'Location': item['Location'],
             'Roll': item['Roll'],
              'Type': item['Type'], 
              'Color': item['Color'], 
              'Width': item['Width'], 
              'Length': item['Length'],
               'Weight': item['Weight'], 
               'Part No.': item['Part No.']
    }
    return data

def rollInCrossPly(rollNumber, crossPlyDF):
    rollCrossPlyColor0 = crossPlyDF['Color 0 Roll'].unique()
    rollCrossPlyColor90 = crossPlyDF['Color 90 Roll'].unique()
    if rollNumber in rollCrossPlyColor0 or rollNumber in rollCrossPlyColor90:
        return True
    else:
        return False


def givenRollLatestData(rollNumber, usageDateCompare, color, length):
    pass

def test():
    print('Test working!!')

if __name__ == '__main__':
    test()
    print(get_date(7))
    print(get_date(31))
   # loadInventoryData()
    #getInventory()
    date_format = '%Y-%m-%d %H:%M:%S'
    dateListEST = [ '2023-07-01 10:35:02', '2023-09-01 13:35:02', '2023-10-01 21:35:02', '2023-08-01 07:35:02', '2023-11-07 10:35:02']
    print('--------------')
    for item in dateListEST:
        utcDate = get_convert_datetime(item, 'EST', 'UTC')
        convertBackString = utcDate.strftime(date_format)
        estNewDate = get_convert_datetime(convertBackString, 'UTC', 'EST')
        estNewDateString = estNewDate.strftime(date_format)
        convertBack = get_convert_datetime(estNewDateString, 'EST', 'UTC')
        print(f' EST : {item}, UTC : {convertBackString}, EST (Back) : {estNewDateString}, UTC again: {convertBack.strftime(date_format)}')