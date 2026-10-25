from .database.db import get_db
from fastapi import Depends, status,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from .database.schema.user_schema import UserSchema
from datetime import datetime, timedelta, timezone
from .config.app_config import getApp_config
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import InvalidTokenError
from .models.auth_model import TokenData

config = getApp_config()


db_dependency = Annotated[Session, Depends(get_db)]

password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("fakePassword")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# -------auxiliary-functions---------------
def verify_password(plain_password:str, hashed_password:str):
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password:str):
    return password_hash.hash(password)


def get_user(username: str, db: Annotated[Session, Depends(get_db)]):
    user = db.query(UserSchema).filter(UserSchema.username == username).first()
    return user


def authenticate_user(
    username: str, password: str, db: Annotated[Session, Depends(get_db)]
):
    user = get_user(username, db)
    if user is None:
        verify_password(
            password, DUMMY_HASH
        )  # prevent timing attacks during authentication.
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.secret_key, algorithm=config.algorithm)
    return encoded_jwt


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.secret_key, algorithms=[config.algorithm])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = (
        db.query(UserSchema).filter(UserSchema.username == token_data.username).first()
    )
    if user is None:
        raise credentials_exception
    return user

