from datetime import datetime
from typing import Literal, Optional
from uuid import uuid4
from pydantic import BaseModel, Field

Sentiment = Literal["frustrated", "neutral", "satisfied", "angry", "confused"]
CallType = Literal["inbound", "outbound"]
ResolutionStatus = Literal["resolved", "escalated", "pending", "unresolved"]
ExperienceLevel = Literal["junior", "mid", "senior"]
IssueComplexity = Literal["low", "medium", "high"]


class CustomerProfile(BaseModel):
    name: str
    age: int
    sentiment: Sentiment
    issue_complexity: IssueComplexity = Field(alias="issueComplexity")

    class Config:
        populate_by_name = True


class AgentProfile(BaseModel):
    name: str
    department: str
    experience_level: ExperienceLevel = Field(alias="experienceLevel")

    class Config:
        populate_by_name = True


class ConversationTurn(BaseModel):
    speaker: Literal["agent", "customer"]
    text: str
    timestamp: Optional[str] = None


class TranscriptMetadata(BaseModel):
    duration_seconds: int = Field(alias="durationSeconds")
    resolution_status: ResolutionStatus = Field(alias="resolutionStatus")
    csat_score: Optional[int] = Field(alias="csatScore", default=None)
    call_reason_primary: str = Field(alias="callReasonPrimary")
    call_reason_secondary: Optional[str] = Field(alias="callReasonSecondary", default=None)
    escalated: bool = False

    class Config:
        populate_by_name = True


class Transcript(BaseModel):
    id: str
    industry: str
    scenario: str
    call_type: CallType = Field(alias="callType")
    customer: CustomerProfile
    agent: AgentProfile
    conversation: list[ConversationTurn]
    metadata: TranscriptMetadata
    created_at: str = Field(alias="createdAt")

    class Config:
        populate_by_name = True


class GenerationConfig(BaseModel):
    industry: str
    scenarios: list[str]
    call_types: list[CallType] = Field(alias="callTypes", default=["inbound"])
    sentiments: list[Sentiment] = Field(default=["neutral", "frustrated", "satisfied"])
    num_records: int = Field(alias="numRecords", default=10, ge=1, le=1000)
    min_turns: int = Field(alias="minTurns", default=4, ge=2)
    max_turns: int = Field(alias="maxTurns", default=12, le=30)
    include_metadata: bool = Field(alias="includeMetadata", default=True)

    class Config:
        populate_by_name = True


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
    transcripts: list[Transcript] = Field(default_factory=list)

    class Config:
        populate_by_name = True

    @classmethod
    def create(cls, config: GenerationConfig) -> "GenerationJob":
        """Factory method to create a new job from config."""
        return cls(
            id=str(uuid4()),
            config=config,
            totalRecords=config.num_records,
            createdAt=datetime.utcnow().isoformat() + "Z",
        )


