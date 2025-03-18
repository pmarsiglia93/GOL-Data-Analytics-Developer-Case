from fastapi import APIRouter, Depends

from app.api.dependencies import get_credentials

from app.api.v1.routers import (
    booking,
    dashboard,
)

from app.config.settings import settings


if settings.ENV == 'DEV':
    v1_router = APIRouter()
else:
    v1_router = APIRouter(dependencies=[Depends(get_credentials)])

v1_router.include_router(booking.router, prefix='/booking', tags=['booking'])
v1_router.include_router(dashboard.router, prefix='/dashboard', tags=['dashboard'])
