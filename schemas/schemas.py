from pydantic import BaseModel


class Car(BaseModel):
    model:str
    name:str
    year:int
    price:int