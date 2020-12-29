from fastapi import APIRouter

from .models.website import WebsiteResponseList, WebsiteResponseCreate, WebsiteRequestCreate
from ..modules.website import list_, create, delete

router = APIRouter()


@router.get('/{username}/list', summary='List all registered websites', status_code=200, response_model=WebsiteResponseList)
def router_list(username: str):
    return {'result': list_(username)}


@router.post('/{username}/create', summary='Create new website registered', status_code=201, response_model=WebsiteResponseCreate)
def router_create(username: str, body: WebsiteRequestCreate):
    return {'result': create(username, **body.dict())}


@router.delete('/{username}/{id_website}/delete', summary='Remove a website', status_code=200)
def router_delete(username: str, id_website: int):
    delete(username, id_website)
    return {}
