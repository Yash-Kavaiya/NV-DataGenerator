import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from parent directory
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)

from app.routers import generate_router, jobs_router, industries_router, settings_router

app = FastAPI(
    title="Contact Center Transcript Generator",
    description="Generate synthetic contact center transcripts using NeMo Data Designer",
    version="0.1.0",
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(generate_router, prefix="/api/v1")
app.include_router(jobs_router, prefix="/api/v1")
app.include_router(industries_router, prefix="/api/v1")
app.include_router(settings_router, prefix="/api/v1")


@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/")
async def root():
    return {
        "message": "Contact Center Transcript Generator API",
        "docs": "/docs",
        "health": "/api/v1/health",
    }
