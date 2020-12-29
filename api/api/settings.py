from pydantic import BaseSettings


class PriceMonitoringSettings(BaseSettings):
    FASTAPI_TITLE: str = 'Price Monitoring API'
    FASTAPI_DESCRIPTION: str = 'Price monitoring API from different sites with Telegram notifications'
    FASTAPI_VERSION: str = '1.0.0'

    UVICORN_APP: str = 'api:app'
    UVICORN_HOST: str = '0.0.0.0'
    UVICORN_PORT: int = 8080
    UVICORN_DEBUG: bool = False
    UVICORN_RELOAD: bool = False

    DATABASE_URI: str = 'mysql://root:toor@mysql:3306/PRICE_MONITORING'
    DATABASE_RESET: bool = False

    BROKER_URI: str = 'amqp://root:toor@rabbitmq:5672'

    TASK_GET_PRICE_SECONDS: int = 60

    TELEGRAM_SEND_MESSAGE_URI: str = 'https://api.telegram.org/bot%BOT_TOKEN%/sendMessage?chat_id=%CHAT_ID%&text=%MESSAGE%'
    TELEGRAM_BOT_TOKEN: str


envs = PriceMonitoringSettings()
