from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    usersname: str
    email: EmailStr
    password: str


class UserDB(UserSchema):
    id: int
    pass


class UserPublic(BaseModel):
    id: int
    usersname: str
    email: EmailStr
