from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException


class ErrorHandler:

    def __init__(self, app: FastAPI):
        app.exception_handler(Exception)(self.handler_exception)
        app.exception_handler(AssertionError)(self.handler_assertion)
        app.exception_handler(HTTPException)(self.handler_http_exception)

    @staticmethod
    async def handler_exception(request: Request, exc: Exception):
        return JSONResponse(status_code=500, content={"message": 'internal server error'})

    @staticmethod
    async def handler_assertion(request: Request, exc: Exception):
        return JSONResponse(status_code=403, content={"message": str(exc)})

    @staticmethod
    async def handler_http_exception(request: Request, exc: HTTPException):
        return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})
