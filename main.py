from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values

from routes import router as job_app_entries_router

config=dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config['ATLAS_URI'])
    app.database = app.mongodb_client['DB_NAME']
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(job_app_entries_router, tags=["Job Application Entries"], prefix="/job_application_entries")