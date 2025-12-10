"""Healthcare industry template."""

from .base import IndustryTemplate

healthcare_template = IndustryTemplate(
    id="healthcare",
    name="Healthcare",
    
    terminology=[
        "appointment", "referral", "copay", "deductible", "prior authorization",
        "prescription", "refill", "pharmacy", "provider", "specialist",
        "primary care physician", "PCP", "insurance card", "member ID",
        "explanation of benefits", "EOB", "claim", "out-of-pocket",
        "in-network", "out-of-network", "formulary", "generic", "brand name",
        "dosage", "medication", "lab work", "diagnostic", "procedure",
    ],
    
    agent_greetings=[
        "Thank you for calling [Clinic Name]. This is {agent_name} speaking. How may I assist you with your healthcare needs today?",
        "Good [morning/afternoon], you've reached [Healthcare Provider]. My name is {agent_name}. How can I help you?",
        "Thank you for calling. For quality assurance, this call may be recorded. How may I help you today?",
    ],
    
    agent_closings=[
        "Is there anything else I can help you with regarding your healthcare today?",
        "Before we end, do you have any other questions about your appointment or coverage?",
        "Thank you for choosing [Healthcare Provider]. Take care and feel better soon.",
    ],
    
    hold_phrases=[
        "May I place you on a brief hold while I check your records?",
        "Let me verify that information in our system. One moment please.",
        "I'll need to check with our scheduling department. Can you hold for just a moment?",
    ],
    
    compliance_phrases=[
        "For verification purposes, can you please confirm your date of birth?",
        "I need to verify your identity before accessing your medical records.",
        "This call may be recorded for quality assurance and training purposes.",
    ],
    
    scenario_context={
        "appointment": "Patient calling to schedule, reschedule, or cancel a medical appointment. May need to check provider availability, insurance coverage, or referral requirements.",
        "claims": "Patient inquiring about insurance claim status, denied claims, or explanation of benefits. May involve coordination with insurance company.",
        "prescription": "Patient requesting medication refill, checking prescription status, or asking about pharmacy options. May need to verify with provider.",
        "billing": "Patient with questions about medical bills, payment plans, or charges. May involve explaining EOB or insurance processing.",
        "medical_info": "Patient seeking general health information, test results, or provider recommendations. Must be careful about giving medical advice.",
    },
    
    products_services=[
        "Annual wellness visit", "Specialist consultation", "Lab work",
        "Imaging services", "Telehealth appointment", "Urgent care",
        "Preventive screening", "Vaccination", "Physical therapy",
    ],
    
    departments=[
        "Scheduling", "Billing", "Medical Records", "Insurance Verification",
        "Pharmacy", "Nursing", "Patient Services", "Referral Coordination",
    ],
)
