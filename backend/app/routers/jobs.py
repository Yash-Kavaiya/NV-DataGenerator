import json
import csv
import io
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.services.job_store import job_store

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("")
async def list_jobs():
    """List all generation jobs."""
    jobs = job_store.list_jobs()
    return [job.model_dump(by_alias=True) for job in jobs]


@router.get("/{job_id}")
async def get_job(job_id: str):
    """Get status of a specific job."""
    job = job_store.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job.model_dump(by_alias=True)


@router.delete("/{job_id}")
async def delete_job(job_id: str):
    """Delete a job and its results."""
    if not job_store.delete_job(job_id):
        raise HTTPException(status_code=404, detail="Job not found")
    return {"message": "Job deleted"}


@router.get("/{job_id}/download")
async def download_job(job_id: str, format: str = "json"):
    """Download generated transcripts."""
    transcripts = job_store.get_results(job_id)
    if not transcripts:
        raise HTTPException(status_code=404, detail="Job results not found")

    if format == "json":
        content = json.dumps(transcripts, indent=2)
        return StreamingResponse(
            io.StringIO(content),
            media_type="application/json",
            headers={"Content-Disposition": f"attachment; filename=transcripts_{job_id}.json"},
        )
    elif format == "jsonl":
        lines = [json.dumps(t) for t in transcripts]
        content = "\n".join(lines)
        return StreamingResponse(
            io.StringIO(content),
            media_type="application/x-ndjson",
            headers={"Content-Disposition": f"attachment; filename=transcripts_{job_id}.jsonl"},
        )
    elif format == "csv":
        output = io.StringIO()
        if transcripts:
            # Flatten for CSV
            flat_records = []
            for t in transcripts:
                flat = {
                    "id": t["id"],
                    "industry": t["industry"],
                    "scenario": t["scenario"],
                    "callType": t["callType"],
                    "customerName": t["customer"]["name"],
                    "customerAge": t["customer"]["age"],
                    "customerSentiment": t["customer"]["sentiment"],
                    "agentName": t["agent"]["name"],
                    "agentExperience": t["agent"]["experienceLevel"],
                    "conversationTurns": len(t["conversation"]),
                    "durationSeconds": t["metadata"]["durationSeconds"],
                    "resolutionStatus": t["metadata"]["resolutionStatus"],
                    "csatScore": t["metadata"]["csatScore"],
                    "createdAt": t["createdAt"],
                }
                flat_records.append(flat)

            writer = csv.DictWriter(output, fieldnames=flat_records[0].keys())
            writer.writeheader()
            writer.writerows(flat_records)

        return StreamingResponse(
            io.StringIO(output.getvalue()),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename=transcripts_{job_id}.csv"},
        )
    else:
        raise HTTPException(status_code=400, detail="Unsupported format")
