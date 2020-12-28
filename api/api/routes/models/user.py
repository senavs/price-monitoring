from pydantic import BaseModel


class User(BaseModel):
    id_user: int
    username: str


class UserResponseList(BaseModel):
    """Response model to /users/list"""

    result: list[User]


class UserRequestCreate(BaseModel):
    """Request model to /users/create"""

    username: str


class UserResponseCreate(BaseModel):
    """Response model to /users/create"""

    result: User
