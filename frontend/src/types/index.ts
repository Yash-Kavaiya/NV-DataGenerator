export interface Industry {
  id: string
  name: string
  description: string
  icon: string
  scenarios: Scenario[]
}

export interface Scenario {
  id: string
  name: string
  description: string
}

export interface CustomerProfile {
  name: string
  age: number
  sentiment: Sentiment
  issueComplexity: 'low' | 'medium' | 'high'
}

export interface AgentProfile {
  name: string
  department: string
  experienceLevel: 'junior' | 'mid' | 'senior'
}

export type Sentiment = 'frustrated' | 'neutral' | 'satisfied' | 'angry' | 'confused'
export type CallType = 'inbound' | 'outbound'

export interface ConversationTurn {
  speaker: 'agent' | 'customer'
  text: string
  timestamp?: string
}

export interface TranscriptMetadata {
  durationSeconds: number
  resolutionStatus: 'resolved' | 'escalated' | 'pending' | 'unresolved'
  csatScore: number | null
  callReasonPrimary: string
  callReasonSecondary?: string
  escalated: boolean
}

export interface Transcript {
  id: string
  industry: string
  scenario: string
  callType: CallType
  customer: CustomerProfile
  agent: AgentProfile
  conversation: ConversationTurn[]
  metadata: TranscriptMetadata
  createdAt: string
}

export interface GenerationConfig {
  industry: string
  scenarios: string[]
  callTypes: CallType[]
  sentiments: Sentiment[]
  numRecords: number
  minTurns: number
  maxTurns: number
  includeMetadata: boolean
}

export interface GenerationJob {
  id: string
  status: 'pending' | 'running' | 'completed' | 'failed'
  config: GenerationConfig
  progress: number
  totalRecords: number
  completedRecords: number
  createdAt: string
  completedAt?: string
  error?: string
}
