import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from ..db import Base


class Menu(Base): 
    __tablename__ = "menu"
    restaurant_id : Mapped[int] = mapped_column(sa.ForeignKey("restaurants.restaurant_id"), primary_key=True)
    item_id : Mapped[int] = mapped_column(sa.Integer, primary_key=True )    
    name : Mapped[str] = mapped_column(sa.VARCHAR, nullable=False)
    price : Mapped[int] = mapped_column(sa.Integer, nullable=False)


