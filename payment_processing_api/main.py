from fastapi import FastAPI

from routes import app

api = FastAPI(title="Payment Processing API")

api.include_router(app, prefix="/api")
