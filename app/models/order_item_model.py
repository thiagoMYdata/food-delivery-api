from pydantic import BaseModel

class Item(BaseModel):
    id : int
    quantity : int

class OrderItemModel(BaseModel):
    order_id : int
    itens : list[Item]
    description : str = ""


