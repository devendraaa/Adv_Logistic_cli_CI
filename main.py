from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from mylib.logistic import (
    distance_between_two_points,
    cities_list,
    get_coordinates,
    travel_time,
)
# from mylib.wiki import get_wiki_keywords

app = FastAPI()

class City(BaseModel):
    name: str

@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello Logistics INC"}


@app.get("/cities")
async def cities():
    """List cities with GET HTTP Method

    Returns back a list of cities that are available to get further information about
    """

    return {"cities": cities_list()}

if __name__=="__main__":
    uvicorn.run(app, port=8080,host="0.0.0.0")