from fastapi import APIRouter

from .models.price import PriceResponseList
from ..modules.price import list_
from ..queue_manager.tasks import get_price

router = APIRouter()


@router.get('/{username}/{id_website}/list', summary='List all registered prices from websites', status_code=200, response_model=PriceResponseList)
def router_list(username: str, id_website: int):
    return {'result': list_(username, id_website)}


@router.get('/force', summary='Force run extraction task', status_code=200)
def router_force():
    get_price.delay()
    return {}
