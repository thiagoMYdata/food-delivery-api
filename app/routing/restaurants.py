from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Annotated
from ..database.db import get_db
from ..models.restaurants_model import RestaurantModel, NewRestaurantModel
from ..models.menu_model import NewMenuItem, ListMenuItem, MenuItem
from ..models.auth_model import UserModel

from ..database.schema.restaurant_schema import Restaurant
from ..database.schema.menu_schema import Menu
from ..helper import get_current_user

# ------------CONFIGS------------------

router = APIRouter(prefix="/restaurants")

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[UserModel, Depends(get_current_user)]

# ------------ROUTER------------------


@router.get("/")
def get_all_restaurants(db : db_dependency):
    restaurants = db.query(Restaurant).all()
    return restaurants


@router.get("/{id}")
def get_restaurant(id: int, db: db_dependency):
    restaurant = db.query(Restaurant).filter(Restaurant.restaurant_id==id).first()
    if restaurant is None:
        raise HTTPException(status_code=404, detail=f"No restaurant found with ID {id}.")
    return restaurant


@router.post("/")
def post_restaurant(data: NewRestaurantModel, current_user: user_dependency, db: db_dependency):
    new = Restaurant(user_id=current_user.user_id, name=data.name, profit=data.profit)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new



@router.post("/{id}/menu")
def new_menu_item(id : int, data: NewMenuItem, db:db_dependency):
    new = Menu(restaurant_id = id, **data.model_dump())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


@router.get("/{id}/menu", response_model=list[MenuItem])
def menu_itens(id : int, db:db_dependency):
    all_itens = db.query(Menu).filter(Menu.restaurant_id == id).all()
    
    if all_itens is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This restaurant doesn't have a manu yet.")
    return all_itens