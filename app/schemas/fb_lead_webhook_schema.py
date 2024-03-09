from typing import List
from pydantic import BaseModel

class FbLeadWebhookSchema(BaseModel):
    object: str
    entry: list

class Value(BaseModel):
    leadgen_id: str
    page_id: str
    form_id: str
    adgroup_id: str
    ad_id: str
    created_time: str

class Changes(BaseModel):
    field: str
    value: Value

class Entry(BaseModel):
    id: int
    time: int
    changes: List[Changes]
