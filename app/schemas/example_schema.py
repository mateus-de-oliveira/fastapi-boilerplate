from typing import Optional
from pydantic import BaseModel

class ExampleSchema(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
