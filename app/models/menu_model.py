from pydantic import BaseModel, Field, ConfigDict
from pydantic.json_schema import SkipJsonSchema

class NewMenuItem(BaseModel):
    name : str
    price : int

class MenuItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)


    item_id :int
    name : str
    price : int
    restaurant_id : int  = Field(exclude=True)



class ListMenuItem(BaseModel):
    items : list[MenuItem]