from fastapi import FastAPI, Query
from services.something_service.service import get_something

app = FastAPI()
@app.get("/something")
def get_something_endpoint(
    something: str = Query(..., description="Query topic for something"),
    number: str = Query(..., description="Location for something"),
):
    return get_something(something,number)