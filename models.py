from pydantic import BaseModel
from typing import List

class Episode(BaseModel):
    episode_number: int
    title: str
    description: str
    air_date: str
    rating: float

class Season(BaseModel):
    season_number: int
    episodes: List[Episode]

