from sqlalchemy import Column, Date, String

from database.base import BaseModel
from database.config.settings import settings


class BookingModel(BaseModel):
    __tablename__ = settings.DATABASE_TABLENAME_BASE + 'booking'

    first_name     = Column(String(50), nullable=False)
    last_name      = Column(String(50), nullable=False)
    birthday       = Column(String(50), nullable=False)
    document       = Column(String(50), nullable=False)
    departure_date = Column(String(50), nullable=False)
    departure_iata = Column(String(50), nullable=False)
    arrival_iata   = Column(String(50), nullable=False)
    arrival_date   = Column(String(50), nullable=False)
