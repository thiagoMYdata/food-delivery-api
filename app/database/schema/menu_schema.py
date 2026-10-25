import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from ..db import Base


class Menu(Base):
    __tablename__ = "menu"
    id : Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    restaurant_id : Mapped[int] = mapped_column(sa.ForeignKey("restaurants.restaurant_id"))
    name : Mapped[int] = mapped_column(sa.VARCHAR, nullable=False)
    price : Mapped[int] = mapped_column(sa.Integer, nullable=False)

