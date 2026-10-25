from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator,
    ValidationInfo,
)

# class UserRegistrationModel(BaseModel):
#     username : str = Field(..., min_length=2, max_length=30)
#     email : EmailStr
#     password : str = Field(..., min_length=8, max_length=50)
#     password_confirm : str

#     @model_validator(mode="after")
#     def check_password(self):
#         if self.password != self.password_confirm:
#             raise ValueError("password do not match")
#         return self

# class LoginUserModel(BaseModel):
#     username : str = Field(..., min_length=2, max_length=30)
#     password : str = Field(..., min_length=8, max_length=50)


class UserModel(BaseModel):
    user_id: int
    username: str
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserInDB(UserModel):
    hashed_password: str


class Register(BaseModel):
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    confirm_password: str = Field(..., min_length=6)

    @field_validator("confirm_password")
    @classmethod
    def password_match(cls, v:str, info: ValidationInfo) -> str:
        if "password" in info.data and v != info.data["password"]:
            raise ValueError("passwords do not match")
        return v
