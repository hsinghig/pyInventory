import pandas as pd
import os
import json


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
   # loadInventoryData()
    getInventory()