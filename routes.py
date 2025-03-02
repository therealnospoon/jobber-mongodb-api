from fastapi import APIRouter, HTTPException, Body, Request, Response, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import JobApplicationEntry, JobApplicationEntryUpdate

router = APIRouter()

@router.post("/", \
            response_description="Add new job application entry", \
                status_code=status.HTTP_201_CREATED, \
                    response_model=JobApplicationEntry)
def create_job_application_entry(request: Request, jobApplicationEntry: JobApplicationEntry = Body(...)):
    jobApplicationEntry = jsonable_encoder(jobApplicationEntry)
    new_job_application_entry = request.app.database["jobApplicationRecords"].insert_one(jobApplicationEntry)
    created_job_application_entry = request.app.database["jobApplicationsRecords"].find_one({"_id": new_job_application_entry.inserted_id})
    
    return created_job_application_entry

@router.get("/", \
            response_description="List all job application entries", \
                response_model=List[JobApplicationEntry])
def list_job_application_entries(request: Request):
    job_application_entries = list(request.app.database["jobApplicationRecords"].find(limit=100))
    
    return job_application_entries

@router.get("/{id}", \
            response_description="Get a single job application entry", \
                response_model=JobApplicationEntry)
def find_job_application_entry(request: Request, id: str):
    if (job_application_entry := request.app.database["jobApplicationRecords"].find_one({"_id": id})) is not None:
        return job_application_entry
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job entry with ID {id} not found")

@router.put("/{id}", \
            response_description="Update a job application entry", \
                response_model=JobApplicationEntry)
def update_job_application_entry(request: Request, id: str, jobApplicationEntry: JobApplicationEntryUpdate = Body(...)):
    jobApplicationEntry = {k: v for k, v in jobApplicationEntry.model_dump().items() if v is not None}
    if len(jobApplicationEntry) >= 1:
        update_result = request.app.database["jobApplicationRecords"].update_one({"_id": id}, {"$set": jobApplicationEntry})
        
    if update_result.modified_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job entry with ID {id} not found")
    elif update_result.modified_count == 1:
        if (updated_job_application_entry := request.app.database["jobApplicationRecords"].find_one({"_id": id})) is not None:
            return updated_job_application_entry
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job entry with ID {id} not found")
        
@router.delete("/{id}", \
                response_description="Delete a job application entry")
def delete_job_application_entry(request: Request, id: str, response: Response):
    delete_result = request.app.database["jobApplicationRecords"].delete_one({"_id": id})
    
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job entry with ID {id} not found")