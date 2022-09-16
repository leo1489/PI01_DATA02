from typing import Optional
from pydantic import BaseModel

#creamos un nuevo modelo para definir q tipo de valores el cliente puede enviar al servidor
class UserRequestModel(BaseModel):
    
    username: str
    email: str 

