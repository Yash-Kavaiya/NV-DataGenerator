import type { GenerationConfig, GenerationJob, Transcript } from '@/types'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

async function fetchApi<T>(endpoint: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_URL}${endpoint}`, {
    headers: {
      'Content-Type': 'application/json',
      ...options?.headers,
    },
    ...options,
  })

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Unknown error' }))
    throw new Error(error.detail || `HTTP ${response.status}`)
  }

  return response.json()
}

export const api = {
  // Generate preview (small batch for testing)
  generatePreview: (config: GenerationConfig): Promise<{ transcripts: Transcript[] }> =>
    fetchApi('/generate/preview', {
      method: 'POST',
      body: JSON.stringify(config),
    }),

  // Start batch generation job
  startGeneration: (config: GenerationConfig): Promise<GenerationJob> =>
    fetchApi('/generate/batch', {
      method: 'POST',
      body: JSON.stringify(config),
    }),

  // Get job status
  getJob: (jobId: string): Promise<GenerationJob> =>
    fetchApi(`/jobs/${jobId}`),

  // List all jobs
  listJobs: (): Promise<GenerationJob[]> =>
    fetchApi('/jobs'),

  // Download generated data
  downloadJob: async (jobId: string, format: 'json' | 'csv' | 'jsonl' = 'json'): Promise<Blob> => {
    const response = await fetch(`${API_URL}/jobs/${jobId}/download?format=${format}`)
    if (!response.ok) throw new Error('Download failed')
    return response.blob()
  },

  // Health check
  health: (): Promise<{ status: string }> =>
    fetchApi('/health'),
}
