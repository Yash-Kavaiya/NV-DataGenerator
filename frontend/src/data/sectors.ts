// Landing-page showcase content for the six highest-value synthetic-data sectors.
// Kept separate from `industries.ts` (the wizard's selector data): this file holds
// marketing copy, while `industryId` maps each card to a generator industry that the
// backend already supports.

export interface Sector {
  id: string
  /** Generator industry id this card drops the user into (must exist in industries.ts). */
  industryId: string
  title: string
  icon: string
  /** Short tier badge, e.g. "Highest growth potential". */
  tier: string
  /** One-line "why top-tier" rationale. */
  why: string
  useCases: string[]
  /** Muted opportunity note shown at the foot of the card. */
  opportunity: string
}

export const sectors: Sector[] = [
  {
    id: 'healthcare-life-sciences',
    industryId: 'healthcare',
    title: 'Healthcare & Life Sciences',
    icon: '🏥',
    tier: 'Highest growth potential',
    why: 'Strongest CAGR (often 38%+), with massive HIPAA/GDPR privacy barriers and data scarcity for rare diseases and imaging.',
    useCases: [
      'Diagnostic AI (cancer, radiology)',
      'Medical imaging synthesis',
      'Clinical trial simulation',
      'EHR sharing',
      'Drug discovery & genomics',
    ],
    opportunity:
      'Domain-specific generators (MRI/CT scans, pathology slides, longitudinal patient data). High willingness to pay for compliance-focused tools; hospital, pharma and medtech partnerships.',
  },
  {
    id: 'bfsi',
    industryId: 'finance',
    title: 'Banking, Financial Services & Insurance (BFSI)',
    icon: '🏦',
    tier: 'Largest market share',
    why: 'Biggest revenue share (22–35%), driven by fraud rarity, risk modeling and heavy regulation (Basel III, GDPR, CCPA, Solvency II).',
    useCases: [
      'Fraud detection & AML training',
      'Credit risk / scoring simulation',
      'Transaction data for testing',
      'Actuarial & claims modeling',
      'Stress testing',
    ],
    opportunity:
      'Tabular / time-series generators in huge demand. Realistic rare-event synthesis (fraud) with statistical fidelity and privacy. Banks and insurers pay premium prices for compliant solutions.',
  },
  {
    id: 'automotive-av',
    industryId: 'automotive',
    title: 'Automotive & Autonomous Vehicles',
    icon: '🚗',
    tier: 'Perception & simulation leader',
    why: 'Critical for perception AI and simulation, with heavy investment in self-driving and a strong share of vision/simulation synthetic-data markets.',
    useCases: [
      'ADAS / self-driving vision training',
      'Rare edge cases (accidents, weather)',
      'Sensor data (LiDAR, camera)',
      'Robotics validation',
    ],
    opportunity:
      '3D simulation plus photorealistic image/video generation, with scalable procedural generation for millions of scenarios. OEMs, Tier-1 suppliers and AV startups.',
  },
  {
    id: 'retail-ecommerce',
    industryId: 'retail',
    title: 'Retail & E-commerce',
    icon: '🛒',
    tier: 'Steady, easy entry point',
    why: 'Steady adoption for personalization and testing without exposing real customer data (GDPR/CCPA compliant).',
    useCases: [
      'Customer behavior / journey simulation',
      'Recommendation engine training',
      'Inventory & demand forecasting',
      'Marketing A/B testing',
      'Loyalty program optimization',
    ],
    opportunity:
      'Tabular and behavioral data generators make an easy entry point. Synthetic customer profiles and transactions for ML without privacy risk.',
  },
  {
    id: 'manufacturing-industrial',
    industryId: 'manufacturing',
    title: 'Manufacturing & Industrial',
    icon: '🏭',
    tier: 'Strong vision-AI growth',
    why: 'Rising use of AI for quality control and predictive maintenance; synthetic images excel where real defect data is rare or expensive.',
    useCases: [
      'Defect detection (scratches, cracks)',
      'Quality inspection training',
      'Predictive maintenance simulation',
      'Robotics training',
      'Digital twin data',
    ],
    opportunity:
      'Synthetic image/video generation for computer vision (surface defects, assembly lines) combined with physics-based simulation. Factories, electronics and pharma manufacturing.',
  },
  {
    id: 'government-defense',
    industryId: 'government',
    title: 'Government & Defense',
    icon: '🏛️',
    tier: 'Secure & high-value',
    why: 'Secure data needs, training simulation, and strong regulatory/compliance drivers — mentioned consistently across market reports.',
    useCases: [
      'Secure simulation & training data',
      'Cybersecurity scenario generation',
      'Public statistics modeling',
      'Smart city planning',
      'Defense perception systems',
    ],
    opportunity:
      'High-security, auditable synthetic-data platforms with bias reduction. Stable, high-value government and defense contracts (though longer sales cycles).',
  },
]
