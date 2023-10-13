from fastapi import FastAPI
import json
# instatiate app
app = FastAPI()

# read in json data
with open('data/outlander.json') as f:
    show_data = json.load(f)

# homepage endpoint
@app.get("/",include_in_schema=False)
async def get_homepage():
    return {"message": "Hello World"}

# endpoint for all shows
@app.get("/seasons")
async def get_seasons():
    return show_data