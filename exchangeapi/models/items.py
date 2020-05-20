from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    rating: Optional[str]
    cuisine: str
