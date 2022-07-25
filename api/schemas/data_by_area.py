from pydantic import BaseModel
from typing import Optional

class data_by_area(BaseModel):
    area: str

    class Config:
        orm_mode = True
