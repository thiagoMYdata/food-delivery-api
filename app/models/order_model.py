from pydantic import BaseModel



class OrdersModel(BaseModel):
    user_id : int
    restaurant_id : int
    total_value : int
    status : str