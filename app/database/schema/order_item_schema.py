import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from ..db import Base



class OrderItem(Base):
    __tablename__ = "order_item"
    id : Mapped[int] = mapped_column(sa.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id : Mapped[int] = mapped_column(sa.ForeignKey("userdb.user_id"))
    order_id : Mapped[int] = mapped_column(sa.ForeignKey("orders.order_id"))
    quantity : Mapped[int] = mapped_column(sa.Integer, nullable=False)
    description: Mapped[int] = mapped_column(sa.VARCHAR, nullable=False)
