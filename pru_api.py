from fastapi import FastAPI
import pandas as pd
import json
from typing import Optional
from enum import Enum
#Pydantic
from pydantic import BaseModel
from pydantic import Field
from fastapi import Body, Query, Path
from http.client import HTTPException
from urllib.error import HTTPError
from fastapi import FastAPI
from database import User
from database import database as connection
from schemas import UserRequestModel
import requests
import csv

app = FastAPI()

@app.get("/test2/")
def apin():
    with open('circuits.csv', newline='') as csvfile:

        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

@app.get("/test4/")
def apin2():
    constructors_df = pd.read_json('./Datasets/constructors.json',encoding = 'utf-8-sig', lines=True)
    print (constructors_df)

    # with open('constructors.json', newline='') as file:

    #     spamreader = csv.reader(file, delimiter=' ', quotechar='|')
    #     for row in spamreader:
    #         print(', '.join(row))
       
    # with open('constructors.json', 'r',encoding = 'UTF8') as f:
    #     data = json.load(f)
    #     for roww in data:
    #         print(','.join(roww))

@app.get("/test5/")
def aapin():
    with open('drivers.json', encoding = 'utf-8-sig') as fe:
        constructors = json.load(fe)
        # for rrow in constructors:
        #     print(', '.join(rrow))
        return constructors

        # spamre = json.reader(fe, delimiter=' ', quotechar='|')
        # for row in spamre:
        #     print(', '.join(row))
        



    # Output: {'name': 'Bob', 'languages': ['English', 'French']}
    #print(data)

# Output: ['English', 'French']
# print(person_dict['languages'])
# with open('./Datasets/constructors.json', encoding = 'UTF-8') as c:
#         constructors = json.load(c)
#         return constructors




#url = "https://api.estadisticasbcra.com/"
# with open("./circuits.csv") as archivo:
#     datos = csv.load(archivo)

# dict1 = datos
# datos2=json.dumps(dict1)
#data_json = requests.get(url, headers=headers).json()

# def apinuevo(request):
#     data = json.dumps(dict1)
#     return data
#Armamos una tabla con los datos
#dolarblue = pd.DataFrame(datos2)

@app.get("/test1/{para1}")
def test_para_obligatorios(para1: str | int):
    return {"Parametro": para1}

@app.get("/test3/")
def test_para_opcional(para1: str | int = None):
    if para1 == None:
        return {"Respuesta": "Parametro no encontrado"}
    else:
        return {"Parametro": para1}

@app.get('/constructors')
async def constructors():
    with open('./Datasets/constructors.json', encoding = 'UTF-8') as c:
        constructors = json.load(c)
        return constructors



# import pandas as pd
# import json
# from fastapi import FastAPI

# app = FastAPI()

# with open("./constructors.json", encoding="UTF-8") as f:
#     people = json.load(f)

# data_json = requests.get(url, headers=headers).json()  #Llamado

#     Ndf = pd.DataFrame(data_json) #Arma una tabla con los datos

# people = pd.DataFrame.from_dict(people)