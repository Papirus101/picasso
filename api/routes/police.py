import datetime
import os

from fastapi import APIRouter, HTTPException, Body, Depends, Request
from queries import generate_where_date, get_data
from sql import SELECT_DATA
from models import PoliceResponse

police_router = APIRouter(prefix='/police',
                              tags=['police'])

@police_router.get('/get_incident', response_model=PoliceResponse)
async def get_incident_list(
        date_from: datetime.datetime | None,
        date_to: datetime.datetime | None,
        page: int = 1):
    where_statement = generate_where_date(date_from, date_to)
    sql = SELECT_DATA.format(
            table_name=os.getenv('TABLE_NAME'),
            where_date=where_statement,
            offset=page * 20)
    data = await get_data(sql)
    returned_data = {'data': [dict(a) for a in data]}
    if not data:
        raise HTTPException(400)
    return returned_data
