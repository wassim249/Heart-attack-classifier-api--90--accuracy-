from pydantic import BaseModel, conlist


class Person(BaseModel):  
    data : conlist(float, min_items=13, max_items=13)