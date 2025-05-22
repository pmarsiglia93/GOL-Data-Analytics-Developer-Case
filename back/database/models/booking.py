from sqlalchemy import Column, String, DateTime, Integer
from database.base import BaseModel


class BookingModel(BaseModel):
    __tablename__ = 'gdadc_booking'

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birthday = Column(String(50), nullable=False)
    document = Column(String(50), nullable=False)
    departure_date = Column(String(50), nullable=False)
    departure_iata = Column(String(50), nullable=False)
    arrival_iata = Column(String(50), nullable=False)
    arrival_date = Column(String(50), nullable=False)
