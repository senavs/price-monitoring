from fastapi import FastAPI

from .database.core import Bootloader
from .modules.error_handler import ErrorHandler
from .modules.middleware import Middleware
from .routes import user, website, prices
from .settings import envs

app = FastAPI(title=envs.FASTAPI_TITLE, description=envs.FASTAPI_DESCRIPTION, version=envs.FASTAPI_VERSION)

# API apps
ErrorHandler(app)
Middleware(app)

# database
Bootloader()

# routes
app.include_router(user.router, prefix='/users', tags=['Users'])
app.include_router(website.router, prefix='/websites', tags=['Websites'])
app.include_router(prices.router, prefix='/prices', tags=['Prices'])
