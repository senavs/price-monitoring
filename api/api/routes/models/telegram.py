from pydantic import BaseModel


class Telegram(BaseModel):
    id_telegram: int
    id_user: int
    chat_id: str


class TelegramResponseList(BaseModel):
    """Response model to /telegram/{username}/list"""

    result: list[Telegram]


class TelegramResponseCreate(BaseModel):
    """Response model to /telegram/{username}/create"""

    result: Telegram


class TelegramRequestCreate(BaseModel):
    """Request model to /websites/{username}/create"""

    chat_id: str
