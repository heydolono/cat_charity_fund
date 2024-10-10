from datetime import datetime
from pydantic import BaseModel, Extra, Field


class DonationBase(BaseModel):
    full_amount: int = Field(..., gt=0)
    comment: str

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
    close_date: datetime

    class Config:
        orm_mode = True

class DonationDB(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True
