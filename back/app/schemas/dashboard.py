from typing import Dict, List

from pydantic import BaseModel


class DashboardChartDataSchema(BaseModel):
    category: str
    value: int


class DashboardChartDataGet(BaseModel):
    count: int
    limit: int
    data: List[DashboardChartDataSchema]


class DashboardDataSchema(BaseModel):
    date: str
    iatapair: str
    departures: int
    arrivals: int


class DashboardDataGet(BaseModel):
    count: int
    limit: int
    data: List[DashboardDataSchema]
