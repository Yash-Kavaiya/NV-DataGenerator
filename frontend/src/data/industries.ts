import type { Industry } from '@/types'

export const industries: Industry[] = [
  {
    id: 'healthcare',
    name: 'Healthcare',
    description: 'Medical facilities, insurance, pharmacies',
    icon: '🏥',
    scenarios: [
      { id: 'appointment', name: 'Appointment Scheduling', description: 'Book, reschedule, or cancel appointments' },
      { id: 'claims', name: 'Insurance Claims', description: 'File or check status of insurance claims' },
      { id: 'prescription', name: 'Prescription Refills', description: 'Request medication refills' },
      { id: 'billing', name: 'Billing Inquiries', description: 'Questions about medical bills' },
      { id: 'medical_info', name: 'Medical Information', description: 'General health questions and guidance' },
    ],
  },
  {
    id: 'finance',
    name: 'Finance & Banking',
    description: 'Banks, credit unions, financial services',
    icon: '🏦',
    scenarios: [
      { id: 'account_inquiry', name: 'Account Inquiry', description: 'Balance checks, transaction history' },
      { id: 'fraud_alert', name: 'Fraud Alert', description: 'Report suspicious activity' },
      { id: 'loan', name: 'Loan Application', description: 'Apply for or inquire about loans' },
      { id: 'card_dispute', name: 'Card Dispute', description: 'Dispute unauthorized charges' },
      { id: 'wire_transfer', name: 'Wire Transfer', description: 'Initiate or track transfers' },
    ],
  },
  {
    id: 'retail',
    name: 'Retail & E-commerce',
    description: 'Online and physical retail stores',
    icon: '🛒',
    scenarios: [
      { id: 'order_status', name: 'Order Status', description: 'Track orders and deliveries' },
      { id: 'returns', name: 'Returns & Refunds', description: 'Process returns and refunds' },
      { id: 'product_inquiry', name: 'Product Inquiry', description: 'Questions about products' },
      { id: 'complaint', name: 'Complaint', description: 'File complaints about service or products' },
      { id: 'loyalty', name: 'Loyalty Program', description: 'Points, rewards, membership' },
    ],
  },
  {
    id: 'telecom',
    name: 'Telecommunications',
    description: 'Phone, internet, cable providers',
    icon: '📱',
    scenarios: [
      { id: 'outage', name: 'Service Outage', description: 'Report or check on outages' },
      { id: 'plan_change', name: 'Plan Changes', description: 'Upgrade, downgrade, or modify plans' },
      { id: 'billing', name: 'Billing Issues', description: 'Questions about bills and charges' },
      { id: 'tech_support', name: 'Technical Support', description: 'Troubleshoot technical issues' },
      { id: 'activation', name: 'New Activation', description: 'Activate new services or devices' },
    ],
  },
  {
    id: 'saas',
    name: 'SaaS & Tech Support',
    description: 'Software companies, cloud platforms, developer tools',
    icon: '💻',
    scenarios: [
      { id: 'technical_bug', name: 'Technical Bug', description: 'Report a bug or unexpected behavior' },
      { id: 'integration', name: 'API Integration', description: 'Help with API, webhooks, or third-party connections' },
      { id: 'billing', name: 'Billing', description: 'Subscription, invoice, or seat count questions' },
      { id: 'onboarding', name: 'Onboarding', description: 'Getting started and configuration help' },
      { id: 'account', name: 'Account Management', description: 'Login, SSO, permissions, or user management' },
    ],
  },
  {
    id: 'automotive',
    name: 'Automotive',
    description: 'Dealerships, OEMs, connected & autonomous vehicles',
    icon: '🚗',
    scenarios: [
      { id: 'service_appointment', name: 'Service Appointment', description: 'Schedule vehicle maintenance or repair' },
      { id: 'recall', name: 'Safety Recall', description: 'Inquire about or schedule recall repair' },
      { id: 'warranty', name: 'Warranty Claim', description: 'Questions about warranty coverage or claims' },
      { id: 'sales', name: 'Vehicle Sales', description: 'Inquire about buying or leasing a vehicle' },
      { id: 'roadside', name: 'Roadside Assistance', description: 'Request towing or roadside help' },
    ],
  },
  {
    id: 'manufacturing',
    name: 'Manufacturing & Industrial',
    description: 'Factories, industrial suppliers, quality & supply chain',
    icon: '🏭',
    scenarios: [
      { id: 'order_status', name: 'Order Status', description: 'Production progress and delivery timeline' },
      { id: 'quality_issue', name: 'Quality Issue', description: 'Product defect or quality concern' },
      { id: 'technical', name: 'Technical Inquiry', description: 'Specifications, tolerances, compatibility' },
      { id: 'pricing', name: 'Pricing & Quotes', description: 'Request quotes or bulk order pricing' },
      { id: 'supply_chain', name: 'Supply Chain', description: 'Material availability and lead times' },
    ],
  },
  {
    id: 'government',
    name: 'Government & Public Sector',
    description: 'Public agencies, benefits, licensing, defense',
    icon: '🏛️',
    scenarios: [
      { id: 'benefits', name: 'Benefits Inquiry', description: 'Government benefits eligibility and status' },
      { id: 'permits', name: 'Permits & Licensing', description: 'Business or construction permits' },
      { id: 'taxes', name: 'Tax Services', description: 'Filing, refunds, or payment plans' },
      { id: 'dmv', name: 'DMV Services', description: 'Driver licenses, vehicle registration' },
      { id: 'complaint', name: 'Complaint / Request', description: 'Public complaint or record request' },
    ],
  },
]

export const sentiments = [
  { id: 'frustrated', name: 'Frustrated', color: 'text-orange-400' },
  { id: 'neutral', name: 'Neutral', color: 'text-gray-400' },
  { id: 'satisfied', name: 'Satisfied', color: 'text-green-400' },
  { id: 'angry', name: 'Angry', color: 'text-red-400' },
  { id: 'confused', name: 'Confused', color: 'text-yellow-400' },
]

export const callTypes = [
  { id: 'inbound', name: 'Inbound', description: 'Customer calls the contact center' },
  { id: 'outbound', name: 'Outbound', description: 'Agent calls the customer' },
]

export const languages = [
  { id: 'english', name: 'English', flag: '🇺🇸' },
  { id: 'spanish', name: 'Spanish', flag: '🇪🇸' },
  { id: 'french', name: 'French', flag: '🇫🇷' },
  { id: 'german', name: 'German', flag: '🇩🇪' },
  { id: 'portuguese', name: 'Portuguese', flag: '🇧🇷' },
  { id: 'italian', name: 'Italian', flag: '🇮🇹' },
  { id: 'japanese', name: 'Japanese', flag: '🇯🇵' },
  { id: 'mandarin', name: 'Mandarin', flag: '🇨🇳' },
  { id: 'hindi', name: 'Hindi', flag: '🇮🇳' },
  { id: 'arabic', name: 'Arabic', flag: '🇸🇦' },
  { id: 'korean', name: 'Korean', flag: '🇰🇷' },
  { id: 'dutch', name: 'Dutch', flag: '🇳🇱' },
  { id: 'russian', name: 'Russian', flag: '🇷🇺' },
]
