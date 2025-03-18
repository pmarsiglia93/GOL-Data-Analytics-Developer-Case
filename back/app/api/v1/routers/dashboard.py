from typing import Any

from fastapi import APIRouter

from app.data.dashboard import DashboardData

from app.schemas.dashboard import DashboardChartDataGet, DashboardDataGet

from database.models.booking import BookingModel


router = APIRouter()


@router.get(
    '/chart/data/1',
    response_model=DashboardChartDataGet,
    summary='GET | Dashboard Chart Data 1'
)
def get_chart_data_1(
    limit: int = 5000
) -> Any:
    '''
    Retrieves chart data.

    Returns:
    - A dictionary containing the count of records, the limit of records and the data.
    '''

    data   = DashboardData
    model  = BookingModel
    schema = DashboardChartDataGet

    data = data.get_chart_data_1(model.get_dataframe())[:limit]

    count = len(data)

    return schema(
        count=count,
        limit=limit,
        data=data
    )


@router.get(
    '/chart/data/2',
    response_model=DashboardChartDataGet,
    summary='GET | Dashboard Chart Data 2'
)
def get_chart_data_2(
    limit: int = 5000
) -> Any:
    '''
    Retrieves chart data.

    Returns:
    - A dictionary containing the count of records, the limit of records and the data.
    '''

    data   = DashboardData
    model  = BookingModel
    schema = DashboardChartDataGet

    data = data.get_chart_data_2(model.get_dataframe())[:limit]

    count = len(data)

    return schema(
        count=count,
        limit=limit,
        data=data
    )


@router.get(
    '/chart/data/3',
    response_model=DashboardChartDataGet,
    summary='GET | Dashboard Chart Data 3'
)
def get_chart_data_3(
    limit: int = 5000
) -> Any:
    '''
    Retrieves chart data.

    Returns:
    - A dictionary containing the count of records, the limit of records and the data.
    '''

    data   = DashboardData
    model  = BookingModel
    schema = DashboardChartDataGet

    data = data.get_chart_data_3(model.get_dataframe())[:limit]

    count = len(data)

    return schema(
        count=count,
        limit=limit,
        data=data
    )


@router.get(
    '/data',
    response_model=DashboardDataGet,
    summary='GET | Dashboard Data'
)
def get_data(
    limit: int = 5000
) -> Any:
    '''
    Retrieves data.

    Returns:
    - A dictionary containing the count of records, the limit of records and the data.
    '''

    data   = DashboardData
    model  = BookingModel
    schema = DashboardDataGet

    data = data.get_data(model.get_dataframe())[:limit]

    count = len(data)

    return schema(
        count=count,
        limit=limit,
        data=data
    )
