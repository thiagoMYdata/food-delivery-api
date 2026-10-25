from datetime import timedelta
from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm


from ..config.app_config import getApp_config
from ..models.auth_model import UserModel, Token, Register
from ..database.db import get_db
from sqlalchemy.orm import Session
from ..database.schema import UserSchema
from fastapi.responses import JSONResponse

from ..helper import (
    authenticate_user,
    create_access_token,
    get_current_user,
    get_password_hash,
)

# -------configs--------------


config = getApp_config()

router = APIRouter(prefix="/auth")


# -------router---------------


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=config.token_expire_time)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/")
async def read_users_me(
    current_user: Annotated[UserModel, Depends(get_current_user)],
) -> UserModel:
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: Annotated[UserModel, Depends(get_current_user)]):
    return [{"item_id": "Foo", "owner": current_user.username}]


@router.post("/register")
def register(data: Register, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.query(UserSchema).filter(UserSchema.email == data.email).first()

    if existing_user:
        return JSONResponse(
            {"message": "User with this email already exists"}, status_code=400
        )
    # Create a new user
    new_user = UserSchema(
        username=data.username,
        email=data.email,
        hashed_password=get_password_hash(data.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully!", "UserSchema": new_user}
