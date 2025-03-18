import io

import logging

from typing import Annotated, Any

import pandas as pd

from fastapi import APIRouter, File, HTTPException

from fastapi.responses import StreamingResponse

from app.data.booking import BookingData

from app.schemas.booking import BookingGet, BookingPost, BookingFilePost

from database.models.booking import BookingModel


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    '',
    response_model=BookingGet,
    summary='GET | Booking'
)
def get_booking(
    limit: int = 5000
) -> Any:
    '''
    Retrieves booking data.

    Returns:
    - A dictionary containing the count of records, the limit of records and the data.
    '''

    model  = BookingModel
    schema = BookingGet

    count = model.count_all()
    data  = model.get_limit(limit)

    return schema(
        count=count,
        limit=limit,
        data=data
    )


@router.get(
    '/file/download',
    summary='GET | Booking File Download'
)
def get_file_download() -> Any:
    '''
    Generates an Excel file with the data and streams it as a download.

    Returns:
    - StreamingResponse: A streaming response containing the Excel file.
    '''

    model  = BookingModel

    df = model.get_dataframe()

    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

    buffer.seek(0)

    return StreamingResponse(
        buffer,
        headers={'Content-Disposition': 'attachment; filename=booking.xlsx'},
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


@router.post(
    '',
    response_model=BookingPost,
    status_code=201,
    summary='POST | Booking'
)
def post_booking(
    data: BookingPost
) -> Any:
    '''
    Saves booking data.

    Parameters:
    - **data**: The booking data to be saved.

    Returns:
    - A dictionary containing a representation of the data saved.
    '''

    data  = data.dict()
    model = BookingModel

    model.save_dictionary(data)

    return data


@router.post(
    '/file/upload',
    response_model=BookingFilePost,
    status_code=201,
    summary='POST | Booking File Upload'
)
def post_file_upload(
    content: Annotated[bytes, File()]
) -> Any:
    '''
    Uploads booking data from a file.

    Parameters:
    - **content**: The content of the file to upload.

    Returns:
    - A dictionary containing the number of rows uploaded.

    Raises:
    - HTTPException: If the data or file format is invalid.
    '''

    data   = BookingData
    model  = BookingModel
    schema = BookingFilePost

    try:
        df = data.read_from_file(content)

    except Exception as exception:
        logger.exception('Invalid data or file format')

        raise HTTPException(
            detail='Invalid data or file format',
            status_code=422
        )

    model.delete_all()
    model.save_dataframe(df)

    rows = len(df)

    return schema(
        rows=rows
    )
