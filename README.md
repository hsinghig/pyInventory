# pyInventory
An inventory system developed in flask hosted in microsoft azure cloud

## Setup For deployment
1. Create  a resource group and an app service plan.
2. Make sure you the requirments.txt, or else you miss dependencies
3. In the APP Service plan make sure the configuration - general settings - 
    gunicorn --bind=0.0.0.0 --timeout 600 startup:app  
4. 

## Deployment

## libraries
py -m venv env
 py -m pip install --upgrade pip      
 
(env) PS C:\projects\github\pyInventory> set FLASK_APP=app.py
(env) PS C:\projects\github\pyInventory> set FLASK_ENV=development


(env) PS C:\projects\github\pyInventory> $Env:FLASK_APP="startup:app"
(env) PS C:\projects\github\pyInventory> $Env:FLASK_ENV="development"

## future libraries
1. Pendulum - for datetime
2. pypdf - read / merge /split pdf documents
3. icecream - debugging easier
4. loguru - logging 
5. Xarray - multi dimensional data

https://stackoverflow.com/questions/19314342/python-sqlalchemy-pass-parameters-in-connection-execute