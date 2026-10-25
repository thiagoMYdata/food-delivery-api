import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from ..db import Base
from datetime import datetime, timezone

# User, orderItem, restaurant, menu, orders

class Coffee(Base):
    __tablename__ = "coffee_product"
    product_id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(sa.VARCHAR(50), nullable=False)
    price : Mapped[int] = mapped_column(sa.Integer, nullable=False)
    

class Pedidos(Base):
    __tablename__ = "client_orders"
    order_id : Mapped[int] = mapped_column(primary_key=True)
    total_price : Mapped[int] = mapped_column(sa.Integer, nullable=False)
    create_at : Mapped[datetime] = mapped_column(sa.DateTime, nullable=False, default=datetime.now(timezone.utc))


class ItemPedido(Base):
    __tablename__ = "client_item_order"
    id : Mapped[int] = mapped_column(primary_key=True)
    order_id : Mapped[int] = mapped_column(sa.ForeignKey("client_orders.order_id"))
    product_id : Mapped[int] = mapped_column(sa.ForeignKey("coffee_product.product_id"))
    quantity : Mapped[int] = mapped_column(sa.Integer, nullable=False)

