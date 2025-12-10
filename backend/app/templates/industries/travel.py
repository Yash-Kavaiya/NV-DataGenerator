"""Travel & Hospitality industry template."""

from .base import IndustryTemplate

travel_template = IndustryTemplate(
    id="travel",
    name="Travel & Hospitality",
    
    terminology=[
        "reservation", "booking", "confirmation number", "itinerary",
        "check-in", "check-out", "room type", "upgrade", "amenities",
        "flight", "departure", "arrival", "layover", "connection",
        "boarding pass", "seat assignment", "baggage", "carry-on",
        "cancellation policy", "refund", "credit", "rebooking",
        "loyalty program", "points", "miles", "status", "elite",
    ],
    
    agent_greetings=[
        "Thank you for calling [Travel Company]. This is {agent_name}. How may I assist with your travel plans today?",
        "Welcome to [Hotel/Airline] reservations. I'm {agent_name}. How can I help you?",
        "Thank you for calling. Do you have an existing reservation, or would you like to make a new booking?",
    ],
    
    agent_closings=[
        "Is there anything else I can help you with for your trip?",
        "Thank you for choosing [Travel Company]. Have a wonderful trip!",
        "Safe travels! Is there anything else you need before your departure?",
    ],
    
    hold_phrases=[
        "Let me check availability for those dates. One moment please.",
        "I'm looking up your reservation now. Can you hold briefly?",
        "Let me see what options we have. Please hold for just a moment.",
    ],
    
    compliance_phrases=[
        "Can you provide your confirmation number or the name on the reservation?",
        "For security, I'll need to verify the credit card used for booking.",
        "May I have the email address associated with your account?",
    ],
    
    scenario_context={
        "reservation": "Customer making a new reservation or booking. Help find availability, explain options, and complete booking.",
        "cancellation": "Customer wanting to cancel or modify existing reservation. Explain cancellation policy, process changes, and discuss alternatives.",
        "complaint": "Customer unhappy with their experience. Listen empathetically, apologize, and offer appropriate compensation.",
        "rewards": "Customer asking about loyalty program, points balance, or redemption. Explain program benefits and help with redemptions.",
        "special_request": "Customer with special needs (accessibility, dietary, preferences). Document requests and confirm accommodations.",
    },
    
    products_services=[
        "Standard room", "Suite", "Ocean view", "Club level",
        "Economy class", "Business class", "First class",
        "Travel insurance", "Car rental", "Airport transfer",
        "Spa services", "Room service", "Late checkout",
    ],
    
    departments=[
        "Reservations", "Guest Services", "Concierge", "Loyalty Program",
        "Group Bookings", "Special Services", "Complaints", "Refunds",
    ],
)
