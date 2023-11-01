import pandas as pd 

def loadInventoryData():
    inventoryFilePath = 'app//data//inventoryData.xlsx'
    extruderDF = pd.read_excel(inventoryFilePath, sheet_name='Extruder')
    crossPlyDF = pd.read_excel(inventoryFilePath, sheet_name='CrossPly')
    print(extruderDF.head(3))
    print(crossPlyDF.head(3))
    return extruderDF, crossPlyDF