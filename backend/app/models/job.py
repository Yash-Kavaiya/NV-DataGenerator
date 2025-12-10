from typing import Literal, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from .transcript import GenerationConfig

JobStatus = Literal["pending", "running", "completed", "failed"]


class GenerationJob(BaseModel):
    id: str
    status: JobStatus = "pending"
    config: GenerationConfig
    progress: float = 0.0
    total_records: int = Field(alias="totalRecords")
    completed_records: int = Field(alias="completedRecords", default=0)
    created_at: str = Field(alias="createdAt")
    completed_at: Optional[str] = Field(alias="completedAt", default=None)
    error: Optional[str] = None

    class Config:
        populate_by_name = True

    @classmethod
    def create(cls, config: GenerationConfig) -> "GenerationJob":
        import uuid
        return cls(
            id=str(uuid.uuid4()),
            config=config,
            total_records=config.num_records,
            created_at=datetime.utcnow().isoformat() + "Z",
        )
