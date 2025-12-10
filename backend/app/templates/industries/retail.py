"""Retail/E-commerce industry template."""

from .base import IndustryTemplate

retail_template = IndustryTemplate(
    id="retail",
    name="Retail & E-commerce",
    
    terminology=[
        "order number", "tracking number", "shipping", "delivery",
        "return", "refund", "exchange", "store credit", "gift card",
        "promo code", "discount", "coupon", "sale", "clearance",
        "inventory", "out of stock", "backorder", "pre-order",
        "warranty", "product registration", "loyalty points", "rewards",
        "cart", "checkout", "payment method", "billing address",
    ],
    
    agent_greetings=[
        "Thank you for calling [Store Name] customer service. My name is {agent_name}. How can I help you today?",
        "Hi, thanks for calling [Store Name]! I'm {agent_name}. What can I do for you?",
        "Welcome to [Store Name] support. This is {agent_name}. How may I assist you with your order?",
    ],
    
    agent_closings=[
        "Is there anything else I can help you with today?",
        "Thank you for shopping with us! Is there anything else you need?",
        "We appreciate your business. Have a wonderful day!",
    ],
    
    hold_phrases=[
        "Let me look up your order. Can you hold for just a moment?",
        "I'm checking our inventory system now. One moment please.",
        "Let me see what options we have available. Please hold briefly.",
    ],
    
    compliance_phrases=[
        "For your security, can you verify the email address associated with your account?",
        "I'll need the order number or the email used for the purchase.",
    ],
    
    scenario_context={
        "order_status": "Customer checking on order status, shipping updates, or delivery timeline. Look up order and provide tracking information.",
        "returns": "Customer wanting to return or exchange an item. Explain return policy, process return authorization, and provide instructions.",
        "product_inquiry": "Customer asking about product features, availability, or recommendations. Help find the right product for their needs.",
        "complaint": "Customer unhappy with product or service. Listen empathetically, apologize, and find a resolution.",
        "loyalty": "Customer asking about loyalty program, points balance, or rewards. Explain benefits and help redeem rewards.",
    },
    
    products_services=[
        "Standard shipping", "Express shipping", "Same-day delivery",
        "In-store pickup", "Gift wrapping", "Price matching",
        "Extended warranty", "Product protection plan",
        "Loyalty membership", "Gift registry",
    ],
    
    departments=[
        "Order Support", "Returns", "Shipping", "Product Specialists",
        "Loyalty Program", "Gift Cards", "Technical Support", "Escalations",
    ],
)
