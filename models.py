import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class JobApplicationEntry(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    createdOn: datetime = Field(default_factory=datetime.now)
    company: str = Field(...)
    position: str = Field(...)
    dateApplied: datetime = Field(...)
    status: str = Field(...)
    notes: str = Field(...)
    url: str = Field(...)
    class Config:
        populate_by_name = True
        from_attributes = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "createdOn": "2021-07-01T00:00:00",
                "company": "Google",
                "position": "Software Engineer",
                "dateApplied": "2021-07-01T00:00:00",
                "status": "Applied",
                "notes": "Applied through LinkedIn",
                "url": "https://careers.google.com/jobs/results/123456"
            }
        }
class JobApplicationEntryUpdate(BaseModel):
    company: Optional[str]
    position: Optional[str]
    dateApplied: Optional[datetime]
    status: Optional[str]
    notes: Optional[str]
    url: Optional[str]
    class Config:
        schema_extra = {
            "example": {
                "company": "Google",
                "position": "Software Engineer",
                "dateApplied": "2021-07-01T00:00:00",
                "status": "Applied",
                "notes": "Applied through LinkedIn",
                "url": "https://careers.google.com/jobs/results/123456"
            }
        }