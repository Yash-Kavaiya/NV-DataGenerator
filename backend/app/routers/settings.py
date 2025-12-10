"""Settings router for API key management."""
import os
import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/settings", tags=["settings"])

# In-memory storage for current session (use Redis/DB in production)
_current_api_key: str | None = None


class ApiKeyRequest(BaseModel):
    api_key: str


class ApiKeyResponse(BaseModel):
    valid: bool
    message: str


@router.post("/api-key")
async def save_api_key(request: ApiKeyRequest):
    """Save API key for the current session."""
    global _current_api_key
    _current_api_key = request.api_key
    
    # Also set as environment variable for NeMo SDK
    os.environ["NVIDIA_API_KEY"] = request.api_key
    
    return {"success": True, "message": "API key saved for this session"}


@router.get("/api-key/status")
async def get_api_key_status():
    """Check if an API key is configured."""
    global _current_api_key
    env_key = os.getenv("NVIDIA_API_KEY", "")
    has_key = bool(_current_api_key or env_key)
    
    return {
        "configured": has_key,
        "source": "session" if _current_api_key else ("env" if env_key else "none")
    }


@router.post("/test-api", response_model=ApiKeyResponse)
async def test_api_key(request: ApiKeyRequest):
    """Test if the provided API key is valid by making a test request to NVIDIA API."""
    if not request.api_key:
        return ApiKeyResponse(valid=False, message="No API key provided")
    
    if not request.api_key.startswith("nvapi-"):
        return ApiKeyResponse(valid=False, message="Invalid API key format. Should start with 'nvapi-'")
    
    try:
        # Test the API key with a simple request to NVIDIA's API
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://integrate.api.nvidia.com/v1/models",
                headers={
                    "Authorization": f"Bearer {request.api_key}",
                    "Content-Type": "application/json"
                },
                timeout=10.0
            )
            
            if response.status_code == 200:
                return ApiKeyResponse(
                    valid=True, 
                    message="API key is valid! Connected to NVIDIA API successfully."
                )
            elif response.status_code == 401:
                return ApiKeyResponse(
                    valid=False, 
                    message="Invalid API key. Please check your key and try again."
                )
            elif response.status_code == 403:
                return ApiKeyResponse(
                    valid=False, 
                    message="API key does not have access. Check your NVIDIA account permissions."
                )
            else:
                return ApiKeyResponse(
                    valid=False, 
                    message=f"API returned status {response.status_code}. Please try again."
                )
                
    except httpx.TimeoutException:
        return ApiKeyResponse(
            valid=False, 
            message="Connection timed out. Please check your internet connection."
        )
    except httpx.ConnectError:
        return ApiKeyResponse(
            valid=False, 
            message="Could not connect to NVIDIA API. Check your internet connection."
        )
    except Exception as e:
        return ApiKeyResponse(
            valid=False, 
            message=f"Error testing API key: {str(e)}"
        )
