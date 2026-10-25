import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from ..db import Base
from datetime import datetime



class Restaurant(Base):
    __tablename__ = "restaurants"
    restaurant_id : Mapped[int] = mapped_column(nullable=False,primary_key=True,autoincrement=True)
    user_id : Mapped[int]= mapped_column(sa.ForeignKey("userdb.user_id"))
    name : Mapped[int] = mapped_column(sa.VARCHAR(50), nullable=False)
    profit : Mapped[int] = mapped_column(sa.Integer, nullable=False, server_default=sa.text("0"))
    created_at : Mapped[datetime] = mapped_column(server_default=sa.func.now(), nullable= False)
