from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, conint


class DonationBase(BaseModel):
    full_amount: conint(gt=0)
    comment: Optional[str] = None

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    pass


class DonationList(DonationBase):
    id: int
    create_date: datetime
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class DonationDB(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True
