#Python
from typing import Optional
from enum import Enum
#Pydantic
from pydantic import BaseModel
from pydantic import Field
#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path
#from fastapi import Query

app = FastAPI()

#models

class HairColor(Enum):
    white= "white"
    brown="brown"
    black ="black"
    blonde="blonde"
    red="red"

class Location(BaseModel):
    city: str
    state: str
    country: str

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
     )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        Le=115
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

@app.get('/')#path operration (path operation decoration)@ decorador a una funcion
def home():
    return {"HHHello" : "WWorld"}

#request and response body

@app.post("/person/new")
def create_person(person: Person = Body()):
    return person

# validadciones: Query parameters

@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1,
        max_length=50,
        tittle= "Person Name",
        description = 'This is the person name. It is between 1 and 50 characters'
    ),#age: Optional[str] = Query(...)#es obligatorio este query aunq query es opcional entonces borramos Optional antes de [str]
    age: str = Query(
        ...,
        title= 'Person Age',
        description= 'This is the person age. It is required')
):
    return {name: age}

#validationes: path parametters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0),
        min_length=1,
        max_length=50,
        title= 'Person id',
        description = 'This is the person id'
):
    return {person_id: "It exists"}

#validaciones request body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title='Person_ID',
        description='This is the person ID',
        gt=0),
        person: Person = Body(...),
        location: Location = Body(...)
    ):
        results = person.dict()
        results.update(location.dict())
        #return results
        return results














# from typing import Optional
# from pydantic import BaseModel
# from fastapi import FastAPI
# from fastapi import Body

# app = FastAPI()

# class Person(BaseModel):
# 	first_name: str
# 	last_name: str
# 	age: int
# 	hair_color: Optional[str] = None
# 	is_maried: Optional[bool] = None


# @app.get("/")
# def home():

#     return {"Hhello": "World"}

# @app.post("/person/new")
# def create_person(person: Person = Body(...)):
# 	return person
