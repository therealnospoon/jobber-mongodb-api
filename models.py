import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class JobApplicationEntry(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias='_id')
    company: str = Field(...)
    position: str = Field(...)
    dateApplied: datetime = Field(...)
    status: str = Field(...)
    notes: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "company": "Google",
                "position": "Software Engineer",
                "dateApplied": "2021-07-01T00:00:00",
                "status": "Applied",
                "notes": "Applied through LinkedIn"
            }
        }
class JobApplicationEntryUpdate(BaseModel):
    company: Optional[str]
    position: Optional[str]
    dateApplied: Optional[datetime]
    status: Optional[str]
    notes: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "company": "Google",
                "position": "Software Engineer",
                "dateApplied": "2021-07-01T00:00:00",
                "status": "Applied",
                "notes": "Applied through LinkedIn"
            }
        }