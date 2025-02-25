from pydantic import BaseModel
from datetime import datetime

class CO2Reading(BaseModel):
    ppm: int
    timestamp: datetime
