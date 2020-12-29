from fastapi import APIRouter

from .models.telegram import TelegramResponseList, TelegramResponseCreate, TelegramRequestCreate
from ..modules.telegram import list_, create, delete

router = APIRouter()


@router.get('/{username}/list', summary='List all registered telegram chats', status_code=200, response_model=TelegramResponseList)
def router_list(username: str):
    return {'result': list_(username)}


@router.post('/{username}/create', summary='Create new telegram chat registered', status_code=201, response_model=TelegramResponseCreate)
def router_create(username: str, body: TelegramRequestCreate):
    return {'result': create(username, **body.dict())}


@router.delete('/{username}/{id_telegram}/delete', summary='Remove a telegram chat', status_code=200)
def router_delete(username: str, id_telegram: int):
    delete(username, id_telegram)
    return {}
