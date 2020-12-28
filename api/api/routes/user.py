from fastapi import APIRouter

from .models.user import UserResponseList, UserResponseCreate, UserRequestCreate
from ..modules.user import list_, create, delete

router = APIRouter()


@router.get('/list', summary='List all users', status_code=200, response_model=UserResponseList)
def router_list():
    return {'result': list_()}


@router.post('/create', summary='Create a new user', status_code=201, response_model=UserResponseCreate)
def router_list(body: UserRequestCreate):
    return {'result': create(**body.dict())}


@router.delete('/{id_user}/remove', summary='Remove a user', status_code=200)
def router_list(id_user: int):
    delete(id_user)
    return {}
