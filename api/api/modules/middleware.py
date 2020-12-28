from time import perf_counter

from fastapi import FastAPI, Request


class Middleware:

    def __init__(self, app: FastAPI):
        app.middleware('http')(self.middleware_metrics)

    @classmethod
    async def middleware_metrics(cls, request: Request, callnext):
        start_time = perf_counter()
        response = await callnext(request)
        process_time = f'{perf_counter() - start_time:.4f}'
        response.headers["X-Process-Time"] = process_time

        return response
