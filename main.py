from fastapi import FastAPI,HTTPException, status
from typing import List
from models import Episode, Season
import json
# instatiate app
app = FastAPI()

# read in json data
with open('data/outlander.json') as f:
    show_data: dict = json.load(f)

# homepage endpoint
@app.get("/",include_in_schema=False)
async def get_homepage():
    return {"message": "Hello World"}

# endpoint for all seasons
@app.get("/seasons", response_model=List[Season])
async def get_seasons():
    return show_data["seasons"]

# endpoint for a single season
@app.get("/seasons/{season_number}", response_model=Season)
async def get_season(season_number: int):
    for season in show_data["seasons"]:
        if season["season_number"] == season_number:
            return season
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "Season not found.")