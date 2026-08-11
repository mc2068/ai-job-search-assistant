from pydantic import BaseModel, Field
from typing import Optional, List, Literal

class Job(BaseModel):
    """
    Represents a standardized job listing for AI Job Search Assistant.
    """

    id: str = Field(..., description="Unique identifier for the job")
    title: str = Field(..., description="The name of the role")
    company: str = Field(..., description="The name of the company")
    source_url: str = Field(..., description="the source url of the posted job")
    skills: List[str] = Field(..., description="The needed skills for the job")
    description: str = Field(..., description="the description of the posted job")
    location: Optional[str] = Field(default=None, description="Where the job is located")
    remote_type: Optional[Literal["remote", "hybrid", "onsite", "unknown"]] = Field(default=None, description="the possible values of remote type")
    posted_date: Optional[str] = Field(default=None, description="the day when the job announcement was posted")
    salary_min: Optional[int] = Field(default=None, description="Minimum salary")
    salary_max: Optional[int] = Field(default=None, description="Maximum salary")
    currency: Optional[str] = Field(default="unknown", description="the currency of the salary")