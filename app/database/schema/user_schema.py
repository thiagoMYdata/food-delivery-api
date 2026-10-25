import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from ..db import Base


class UserSchema(Base):
    __tablename__ = "userdb"
    user_id: Mapped[int] = mapped_column(
        sa.Integer, primary_key=True, autoincrement=True, nullable=False
    )
    username: Mapped[str] = mapped_column(sa.VARCHAR(), nullable=False)
    hashed_password: Mapped[str] = mapped_column(sa.VARCHAR(), nullable=False)
    email: Mapped[str] = mapped_column(sa.VARCHAR(), nullable=False)
