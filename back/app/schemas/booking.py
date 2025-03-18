from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class BookingSchema(BaseModel):
    id: Optional[int]

    first_name: str
    last_name: str
    birthday: str
    document: str
    departure_date: str
    departure_iata: str
    arrival_iata: str
    arrival_date: str

    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class BookingGet(BaseModel):
    count: int
    limit: int
    data: List[BookingSchema]


class BookingPost(BaseModel):
    first_name: str
    last_name: str
    birthday: str
    document: str
    departure_date: str
    departure_iata: str
    arrival_iata: str
    arrival_date: str


class BookingFilePost(BaseModel):
    rows: int
