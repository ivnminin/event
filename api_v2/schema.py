from pydantic import BaseModel


class EventBought(BaseModel):
    buyer_address: str
    amount: str
    tx: str

    class Config:
        orm_mode = True
