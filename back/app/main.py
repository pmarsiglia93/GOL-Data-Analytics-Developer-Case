from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.routing import APIRoute

from starlette.middleware.cors import CORSMiddleware

from app.api.v1.router import v1_router
from app.config.settings import settings


def custom_generate_unique_id(route: APIRoute):
    return f'{route.tags[0]}-{route.name}'


app = FastAPI(
    title=settings.PROJECT_NAME,
    generate_unique_id_function=custom_generate_unique_id,
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
    swagger_ui_parameters={
        'operationsSorter': 'method',
    },
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(v1_router, prefix=settings.API_V1_STR)
