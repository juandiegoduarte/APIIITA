from pydantic import BaseModel

class Company (BaseModel):
    name: str
    ticker: str
    price: float
    market_cap: float
    sector: str
    volume: int