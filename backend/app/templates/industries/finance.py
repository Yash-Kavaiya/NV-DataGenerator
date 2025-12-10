"""Finance/Banking industry template."""

from .base import IndustryTemplate

finance_template = IndustryTemplate(
    id="finance",
    name="Finance & Banking",
    
    terminology=[
        "account balance", "transaction", "statement", "direct deposit",
        "wire transfer", "ACH", "routing number", "account number",
        "overdraft", "insufficient funds", "pending transaction",
        "credit limit", "APR", "interest rate", "minimum payment",
        "fraud alert", "suspicious activity", "dispute", "chargeback",
        "loan application", "pre-approval", "credit score", "collateral",
        "mortgage", "refinance", "escrow", "principal", "amortization",
    ],
    
    agent_greetings=[
        "Thank you for calling [Bank Name]. This is {agent_name}. For security purposes, this call may be monitored or recorded. How may I assist you?",
        "Welcome to [Bank Name] customer service. My name is {agent_name}. How can I help you with your account today?",
        "Thank you for calling. Before we proceed, I'll need to verify your identity. May I have your account number or the last four digits of your Social Security number?",
    ],
    
    agent_closings=[
        "Is there anything else I can help you with regarding your accounts today?",
        "Thank you for banking with us. Have a great day!",
        "Remember, you can also manage your accounts through our mobile app or online banking.",
    ],
    
    hold_phrases=[
        "Let me pull up your account information. Please hold for just a moment.",
        "I'll need to transfer you to our fraud department. May I place you on a brief hold?",
        "Let me check on that transaction for you. One moment please.",
    ],
    
    compliance_phrases=[
        "For your security, I need to verify your identity. Can you please provide your account PIN or answer your security question?",
        "I'm required to inform you that this call is being recorded for quality and training purposes.",
        "Before I can discuss account details, I need to verify that I'm speaking with the account holder.",
        "Please be aware that we will never ask for your full Social Security number or password.",
    ],
    
    scenario_context={
        "account_inquiry": "Customer checking account balance, recent transactions, or statement information. Verify identity before providing details.",
        "fraud_alert": "Customer reporting suspicious activity or responding to fraud alert. High priority - verify identity carefully and document everything.",
        "loan": "Customer inquiring about loan products, application status, or payment options. May need to discuss rates, terms, and eligibility.",
        "card_dispute": "Customer disputing a charge on their credit or debit card. Need to gather transaction details and initiate dispute process.",
        "wire_transfer": "Customer requesting domestic or international wire transfer. Verify identity, confirm details, and explain fees and timing.",
    },
    
    products_services=[
        "Checking account", "Savings account", "Money market",
        "Certificate of deposit", "Credit card", "Personal loan",
        "Auto loan", "Mortgage", "Home equity line of credit",
        "Online banking", "Mobile deposit", "Bill pay",
    ],
    
    departments=[
        "Account Services", "Fraud Department", "Loan Department",
        "Mortgage Services", "Credit Card Services", "Wire Transfer",
        "Collections", "Account Recovery", "Business Banking",
    ],
)
