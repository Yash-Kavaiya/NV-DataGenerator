"""Industry templates registry."""

from .base import IndustryTemplate
from .healthcare import healthcare_template
from .finance import finance_template
from .telecom import telecom_template
from .retail import retail_template
from .travel import travel_template
from .insurance import insurance_template

# Registry of all industry templates
INDUSTRY_TEMPLATES: dict[str, IndustryTemplate] = {
    "healthcare": healthcare_template,
    "finance": finance_template,
    "telecom": telecom_template,
    "retail": retail_template,
    "travel": travel_template,
    "insurance": insurance_template,
}


def get_template(industry_id: str) -> IndustryTemplate | None:
    """Get industry template by ID."""
    return INDUSTRY_TEMPLATES.get(industry_id)


def get_all_templates() -> list[IndustryTemplate]:
    """Get all available industry templates."""
    return list(INDUSTRY_TEMPLATES.values())


__all__ = [
    "IndustryTemplate",
    "INDUSTRY_TEMPLATES",
    "get_template",
    "get_all_templates",
]
