"""Insurance industry template."""

from .base import IndustryTemplate

insurance_template = IndustryTemplate(
    id="insurance",
    name="Insurance",
    
    terminology=[
        "policy", "premium", "deductible", "coverage", "claim",
        "policyholder", "beneficiary", "rider", "endorsement",
        "liability", "comprehensive", "collision", "underwriting",
        "adjuster", "settlement", "subrogation", "exclusion",
        "effective date", "renewal", "lapse", "reinstatement",
        "certificate of insurance", "declarations page", "binder",
    ],
    
    agent_greetings=[
        "Thank you for calling [Insurance Company]. This is {agent_name}. How may I help you with your policy today?",
        "Good [morning/afternoon], [Insurance Company] customer service. I'm {agent_name}. How can I assist you?",
        "Thank you for calling. For quality assurance, this call may be recorded. How may I help you?",
    ],
    
    agent_closings=[
        "Is there anything else I can help you with regarding your coverage today?",
        "Thank you for choosing [Insurance Company]. Drive safely!",
        "We appreciate your business. Is there anything else you need?",
    ],
    
    hold_phrases=[
        "Let me pull up your policy information. One moment please.",
        "I'll need to check with our claims department. May I place you on a brief hold?",
        "Let me review your coverage details. Can you hold for just a moment?",
    ],
    
    compliance_phrases=[
        "For security purposes, can you verify your policy number and date of birth?",
        "I need to confirm I'm speaking with the named insured or an authorized party.",
        "Before discussing claim details, I'll need to verify your identity.",
    ],
    
    scenario_context={
        "claims_filing": "Customer reporting a new claim (accident, damage, loss). Gather incident details, explain claims process, and set expectations.",
        "policy_inquiry": "Customer asking about their current coverage, policy details, or documents. Review policy and explain coverage clearly.",
        "coverage": "Customer asking what is or isn't covered under their policy. Explain coverage limits, exclusions, and options.",
        "premium": "Customer with questions about premium amount, payment options, or billing. Explain factors affecting premium and payment methods.",
        "renewal": "Customer calling about policy renewal, changes, or cancellation. Review renewal terms and process any changes.",
    },
    
    products_services=[
        "Auto insurance", "Home insurance", "Renters insurance",
        "Life insurance", "Umbrella policy", "Roadside assistance",
        "Accident forgiveness", "Multi-policy discount",
        "Safe driver discount", "Paperless discount",
    ],
    
    departments=[
        "Claims", "Policy Services", "Billing", "Underwriting",
        "Sales", "Retention", "Roadside Assistance", "Fraud Investigation",
    ],
)
