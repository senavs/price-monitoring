import uvicorn

from .settings import envs

if __name__ == '__main__':
    uvicorn.run(envs.UVICORN_APP, host=envs.UVICORN_HOST, port=envs.UVICORN_PORT, debug=envs.UVICORN_DEBUG, reload=envs.UVICORN_RELOAD)
