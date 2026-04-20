from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
    title : str
    author : str
    rating : Optional[float] = None

class BookResponse(BaseModel):
    id : int
    title : str
    author : str
    rating : Optional[float] = None
    model_config = {"from_attributes": True}

class BookUpdate(BaseModel):
    title : Optional[str] = None
    author : Optional[str] = None
    rating : Optional[float] = None
