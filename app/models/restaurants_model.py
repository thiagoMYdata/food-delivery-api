from pydantic import BaseModel, Field
from .auth_model import UserModel
from datetime import datetime



class RestaurantModel(BaseModel):
    user_id : int
    name : str
    profit : int




class NewRestaurantModel(BaseModel):
    name : str
    profit : int
