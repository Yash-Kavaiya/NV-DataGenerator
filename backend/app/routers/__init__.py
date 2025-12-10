from .generate import router as generate_router
from .jobs import router as jobs_router
from .industries import router as industries_router
from .settings import router as settings_router

__all__ = ["generate_router", "jobs_router", "industries_router", "settings_router"]

