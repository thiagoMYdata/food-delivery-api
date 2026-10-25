from fastapi import FastAPI

from app.routing import restaurants, auth

app = FastAPI(openapi_prefix="/api")
app.include_router(restaurants.router)
app.include_router(auth.router)
