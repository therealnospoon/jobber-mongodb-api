import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class JobApplicationEntry(BaseModel):
    # id: str = Field(default_factory=uuid.uuid4, alias='_id')
    company: str = Field(...)
    position: str = Field(...)
    dateApplied: datetime = Field(...)
    status: str = Field(...)
    notes: str = Field(...)
    url: str = Field(...)

    # model_config = ConfigDict(
    #     extra = "forbid", # Disallow extra fields during validation
    #     validate_assignment = True # Enable validation on attribute assignment
    # )
    
    class Config:
        allow_population_by_field_name = True,
        orm_mode = True,
        json_schema_extra = {
            "example": {
                # "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
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

    model_config = ConfigDict(
        extra = "forbid", # Disallow extra fields during validation
        validate_assignment = True # Enable validation on attribute assignment
    )
    
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "company": "Google",
    #             "position": "Software Engineer",
    #             "dateApplied": "2021-07-01T00:00:00",
    #             "status": "Applied",
    #             "notes": "Applied through LinkedIn",
    #             "url": "https://careers.google.com/jobs/results/123456"
    #         }
    #     }