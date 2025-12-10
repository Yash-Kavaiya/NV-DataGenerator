from fastapi import APIRouter

router = APIRouter(prefix="/industries", tags=["industries"])

INDUSTRIES = [
    {
        "id": "healthcare",
        "name": "Healthcare",
        "description": "Medical facilities, insurance, pharmacies",
        "icon": "🏥",
        "scenarios": [
            {"id": "appointment", "name": "Appointment Scheduling", "description": "Book, reschedule, or cancel appointments"},
            {"id": "claims", "name": "Insurance Claims", "description": "File or check status of insurance claims"},
            {"id": "prescription", "name": "Prescription Refills", "description": "Request medication refills"},
            {"id": "billing", "name": "Billing Inquiries", "description": "Questions about medical bills"},
            {"id": "medical_info", "name": "Medical Information", "description": "General health questions and guidance"},
        ],
    },
    {
        "id": "finance",
        "name": "Finance & Banking",
        "description": "Banks, credit unions, financial services",
        "icon": "🏦",
        "scenarios": [
            {"id": "account_inquiry", "name": "Account Inquiry", "description": "Balance checks, transaction history"},
            {"id": "fraud_alert", "name": "Fraud Alert", "description": "Report suspicious activity"},
            {"id": "loan", "name": "Loan Application", "description": "Apply for or inquire about loans"},
            {"id": "card_dispute", "name": "Card Dispute", "description": "Dispute unauthorized charges"},
            {"id": "wire_transfer", "name": "Wire Transfer", "description": "Initiate or track transfers"},
        ],
    },
    {
        "id": "retail",
        "name": "Retail & E-commerce",
        "description": "Online and physical retail stores",
        "icon": "🛒",
        "scenarios": [
            {"id": "order_status", "name": "Order Status", "description": "Track orders and deliveries"},
            {"id": "returns", "name": "Returns & Refunds", "description": "Process returns and refunds"},
            {"id": "product_inquiry", "name": "Product Inquiry", "description": "Questions about products"},
            {"id": "complaint", "name": "Complaint", "description": "File complaints about service or products"},
            {"id": "loyalty", "name": "Loyalty Program", "description": "Points, rewards, membership"},
        ],
    },
    {
        "id": "telecom",
        "name": "Telecommunications",
        "description": "Phone, internet, cable providers",
        "icon": "📱",
        "scenarios": [
            {"id": "outage", "name": "Service Outage", "description": "Report or check on outages"},
            {"id": "plan_change", "name": "Plan Changes", "description": "Upgrade, downgrade, or modify plans"},
            {"id": "billing", "name": "Billing Issues", "description": "Questions about bills and charges"},
            {"id": "tech_support", "name": "Technical Support", "description": "Troubleshoot technical issues"},
            {"id": "activation", "name": "New Activation", "description": "Activate new services or devices"},
        ],
    },
    {
        "id": "insurance",
        "name": "Insurance",
        "description": "Auto, home, life, and other insurance",
        "icon": "🛡️",
        "scenarios": [
            {"id": "claims_filing", "name": "Claims Filing", "description": "File new insurance claims"},
            {"id": "policy_inquiry", "name": "Policy Inquiry", "description": "Questions about coverage"},
            {"id": "coverage", "name": "Coverage Questions", "description": "What is and isn't covered"},
            {"id": "premium", "name": "Premium Payments", "description": "Pay or inquire about premiums"},
            {"id": "renewal", "name": "Policy Renewal", "description": "Renew or update policies"},
        ],
    },
    {
        "id": "travel",
        "name": "Travel & Hospitality",
        "description": "Airlines, hotels, travel agencies",
        "icon": "✈️",
        "scenarios": [
            {"id": "reservation", "name": "Reservations", "description": "Book flights, hotels, rentals"},
            {"id": "cancellation", "name": "Cancellations", "description": "Cancel or modify bookings"},
            {"id": "complaint", "name": "Complaints", "description": "Issues with service or accommodations"},
            {"id": "rewards", "name": "Loyalty Rewards", "description": "Points, miles, status inquiries"},
            {"id": "special_request", "name": "Special Requests", "description": "Accessibility, dietary, preferences"},
        ],
    },
]


@router.get("")
async def list_industries():
    """List all available industries."""
    return INDUSTRIES


@router.get("/{industry_id}/scenarios")
async def get_industry_scenarios(industry_id: str):
    """Get scenarios for a specific industry."""
    for industry in INDUSTRIES:
        if industry["id"] == industry_id:
            return industry["scenarios"]
    return {"error": "Industry not found"}
