"""Telecommunications industry template."""

from .base import IndustryTemplate

telecom_template = IndustryTemplate(
    id="telecom",
    name="Telecommunications",
    
    terminology=[
        "service outage", "network", "coverage", "signal strength",
        "data plan", "unlimited", "throttling", "hotspot", "roaming",
        "billing cycle", "prorated", "early termination fee", "contract",
        "upgrade", "trade-in", "device payment", "installment",
        "SIM card", "eSIM", "activation", "porting", "number transfer",
        "voicemail", "call forwarding", "caller ID", "spam blocking",
        "fiber", "broadband", "bandwidth", "speed test", "latency",
    ],
    
    agent_greetings=[
        "Thank you for calling [Carrier Name]. This is {agent_name}. How can I help you today?",
        "Hi, you've reached [Carrier Name] customer care. I'm {agent_name}. What can I do for you?",
        "Thank you for calling. For quality purposes, this call may be recorded. How may I assist you?",
    ],
    
    agent_closings=[
        "Is there anything else I can help you with your service today?",
        "Thank you for being a valued customer. Is there anything else?",
        "Remember, you can also manage your account through our app. Anything else I can help with?",
    ],
    
    hold_phrases=[
        "Let me check the network status in your area. One moment please.",
        "I'm pulling up your account now. Can you hold briefly?",
        "Let me run some diagnostics on your line. This will take just a moment.",
    ],
    
    compliance_phrases=[
        "For account security, can you verify the PIN on your account?",
        "I need to confirm I'm speaking with an authorized user on this account.",
        "Before making changes, I'll need to verify your identity.",
    ],
    
    scenario_context={
        "outage": "Customer reporting service outage or connectivity issues. Check for known outages, troubleshoot, and provide estimated restoration time.",
        "plan_change": "Customer wanting to upgrade, downgrade, or modify their plan. Review current plan, explain options, and process changes.",
        "billing": "Customer with questions about their bill, charges, or payments. Explain charges, apply credits if warranted, set up payment arrangements.",
        "tech_support": "Customer experiencing technical issues with device or service. Troubleshoot step-by-step, escalate to technical team if needed.",
        "activation": "Customer activating new service or device. Guide through activation process, verify service is working.",
    },
    
    products_services=[
        "Unlimited plan", "Family plan", "Prepaid plan",
        "5G service", "Home internet", "TV bundle",
        "Device protection", "International calling",
        "Mobile hotspot", "Cloud storage",
    ],
    
    departments=[
        "Technical Support", "Billing", "Sales", "Retention",
        "Device Support", "Network Operations", "Porting Department",
        "Business Services", "International Services",
    ],
)
