from enum import Enum
import sqlalchemy as sa
from sqlalchemy import Enum as sa_Enum 
from sqlalchemy.orm import Mapped, mapped_column
from ..db import Base
from datetime import datetime, timezone

class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PREPARING = "preparing"
    DELIVERING = "delivering"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    


class Orders(Base):
    __tablename__ = "orders"
    user_id : Mapped[int] = mapped_column(sa.ForeignKey("userdb.user_id"))
    order_id : Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    restaurant_id : Mapped[int] = mapped_column(sa.ForeignKey("restaurants.restaurant_id"))
    total_value : Mapped[int] = mapped_column(sa.Integer, nullable=False)
    status : Mapped[OrderStatus] = mapped_column(
        sa_Enum(OrderStatus, name="order_status"), default=OrderStatus.PENDING, nullable=False
    )
    created_at : Mapped[datetime] = mapped_column(server_default=sa.func.now(), nullable= False)


   