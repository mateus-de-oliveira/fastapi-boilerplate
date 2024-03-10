#faça um esquema de exemplo utilizando o pydantic
from pydantic import BaseModel
from typing import Optional

class ExampleSchema(BaseModel):
    id: Optional[int] = None
    name: str
    age: int

    class Config:
        orm_mode = True
        