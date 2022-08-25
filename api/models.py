import datetime
from pydantic import BaseModel

class PoliceRequestModel(BaseModel):
    crime_id: int
    original_crime_type_name: str
    report_date: datetime.datetime
    call_date: datetime.datetime
    offense_date: datetime.datetime
    call_time: datetime.time
    disposition: str
    address: str
    city: str
    state: str
    agency_id: int
    address_type: str
    common_location: str

class PoliceResponse(BaseModel):
    data: list[PoliceRequestModel]
