import pandas as pd 

def loadInventoryData():
    inventoryFilePath = 'app//data//inventoryData.xlsx'
    extruderDF = pd.read_excel(inventoryFilePath, sheet_name='Extruder')
    crossPlyDF = pd.read_excel(inventoryFilePath, sheet_name='CrossPly')
    print(extruderDF.head(3))
    print(crossPlyDF.head(3))
    extruderDF.to_csv('extruderData.csv')
    crossPlyDF.to_csv('crossplyData.csv')
    return extruderDF, crossPlyDF

def get_table_DUMMY_DATA():
    headings = ("Name", "Role", "Salary", "Department")
    data = (
    ("Hemant", "Software Engineer", "$23332", "Engg"),
    ("Hemant1", "Software Engineer 2", "$53332", "Soft Engg"),
    ("Hemant2", "Software Engineer 3", "$332", "Soft Engineering")
    )
    return headings, data