import io
import logging
from typing import Any
import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from app.data.booking import BookingData
from app.schemas.booking import BookingGet, BookingPost, BookingFilePost
from database.models.booking import BookingModel

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get('', response_model=BookingGet, summary='GET | Booking')
def get_booking(limit: int = 5000) -> Any:
    model = BookingModel
    schema = BookingGet
    count = model.count_all()
    data = model.get_limit(limit)
    return schema(count=count, limit=limit, data=data)

@router.get('/file/download', summary='GET | Booking File Download')
def get_file_download() -> Any:
    model = BookingModel
    df = model.get_dataframe()
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Reservas')
    buffer.seek(0)
    return StreamingResponse(
        buffer,
        headers={'Content-Disposition': 'attachment; filename=booking.xlsx'},
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

@router.post('', response_model=BookingPost, status_code=201, summary='POST | Booking')
def post_booking(data: BookingPost) -> Any:
    data = data.dict()
    model = BookingModel
    model.save_dictionary(data)
    return data

@router.post('/file/upload', response_model=BookingFilePost, status_code=201, summary='POST | Booking File Upload')
def post_file_upload(file: UploadFile = File(...)) -> Any:
    data = BookingData
    model = BookingModel
    schema = BookingFilePost

    try:
        content = file.file.read()
        df = data.read_from_file(content)
        df = data.validate_dataframe(df)
    except Exception as exception:
        logger.exception('Invalid data or file format')
        raise HTTPException(detail='Invalid data or file format', status_code=422)

    # ✅ Aqui, ao invés de deletar tudo
    # model.delete_all()

    # ✅ Usamos upsert_dataframe passando as chaves únicas
    model.upsert_dataframe(df, keys=['first_name', 'last_name', 'document'])

    rows = len(df)
    return schema(rows=rows)

