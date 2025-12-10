import { useState } from 'react'
import { useMutation, useQuery } from '@tanstack/react-query'
import { Download, Loader2, CheckCircle, XCircle, Clock, FileJson, FileText, Table, History } from 'lucide-react'
import { clsx } from 'clsx'
import { api } from '@/services/api'
import { useConfigStore } from '@/stores/configStore'
import { JobHistory } from './JobHistory'
import type { GenerationJob } from '@/types'

export function ExportPanel() {
  const { config } = useConfigStore()
  const [activeJobId, setActiveJobId] = useState<string | null>(null)

  const startJobMutation = useMutation({
    mutationFn: () => api.startGeneration(config),
    onSuccess: (job) => {
      setActiveJobId(job.id)
    },
  })

  const { data: job } = useQuery({
    queryKey: ['job', activeJobId],
    queryFn: () => api.getJob(activeJobId!),
    enabled: !!activeJobId,
    refetchInterval: (query) => {
      const data = query.state.data as GenerationJob | undefined
      return data?.status === 'running' || data?.status === 'pending' ? 2000 : false
    },
  })

  const downloadMutation = useMutation({
    mutationFn: ({ jobId, format }: { jobId: string; format: 'json' | 'csv' | 'jsonl' }) =>
      api.downloadJob(jobId, format),
    onSuccess: (blob, { format }) => {
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `transcripts.${format}`
      a.click()
      URL.revokeObjectURL(url)
    },
  })

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-white mb-2">Generate & Export</h2>
        <p className="text-gray-400">
          Start full generation and download your synthetic transcripts
        </p>
      </div>

      {/* Config Summary */}
      <div className="bg-gray-800/50 rounded-lg p-4 space-y-2">
        <h3 className="text-sm font-semibold text-gray-400 uppercase">Generation Summary</h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
          <div>
            <span className="text-gray-500">Industry:</span>
            <span className="text-white ml-2 capitalize">{config.industry}</span>
          </div>
          <div>
            <span className="text-gray-500">Scenarios:</span>
            <span className="text-white ml-2">{config.scenarios.length}</span>
          </div>
          <div>
            <span className="text-gray-500">Records:</span>
            <span className="text-white ml-2">{config.numRecords}</span>
          </div>
          <div>
            <span className="text-gray-500">Turns:</span>
            <span className="text-white ml-2">{config.minTurns}-{config.maxTurns}</span>
          </div>
        </div>
      </div>

      {/* Start Generation */}
      {!activeJobId && (
        <button
          onClick={() => startJobMutation.mutate()}
          disabled={startJobMutation.isPending}
          className="btn-primary w-full py-4 text-lg flex items-center justify-center gap-2"
        >
          {startJobMutation.isPending ? (
            <>
              <Loader2 className="w-5 h-5 animate-spin" />
              Starting...
            </>
          ) : (
            <>
              <Download className="w-5 h-5" />
              Generate {config.numRecords} Transcripts
            </>
          )}
        </button>
      )}

      {/* Job Status */}
      {job && (
        <div className="space-y-4">
          <div className="bg-gray-800/50 rounded-lg p-4">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-3">
                <JobStatusIcon status={job.status} />
                <div>
                  <span className="text-white font-medium capitalize">{job.status}</span>
                  <span className="text-gray-500 text-sm ml-2">Job {job.id.slice(0, 8)}</span>
                </div>
              </div>
              <span className="text-gray-400 text-sm">
                {job.completedRecords} / {job.totalRecords} records
              </span>
            </div>

            {/* Progress Bar */}
            <div className="h-2 bg-gray-700 rounded-full overflow-hidden">
              <div
                className={clsx(
                  'h-full transition-all duration-500',
                  job.status === 'completed' ? 'bg-nvidia-green' :
                  job.status === 'failed' ? 'bg-red-500' : 'bg-nvidia-green/70'
                )}
                style={{ width: `${job.progress}%` }}
              />
            </div>

            {job.error && (
              <p className="text-red-400 text-sm mt-2">{job.error}</p>
            )}
          </div>

          {/* Download Options */}
          {job.status === 'completed' && (
            <div className="space-y-3">
              <h3 className="text-lg font-semibold text-white">Download</h3>
              <div className="grid grid-cols-3 gap-3">
                <DownloadButton
                  format="json"
                  icon={<FileJson className="w-5 h-5" />}
                  label="JSON"
                  onClick={() => downloadMutation.mutate({ jobId: job.id, format: 'json' })}
                  isLoading={downloadMutation.isPending}
                />
                <DownloadButton
                  format="jsonl"
                  icon={<FileText className="w-5 h-5" />}
                  label="JSONL"
                  onClick={() => downloadMutation.mutate({ jobId: job.id, format: 'jsonl' })}
                  isLoading={downloadMutation.isPending}
                />
                <DownloadButton
                  format="csv"
                  icon={<Table className="w-5 h-5" />}
                  label="CSV"
                  onClick={() => downloadMutation.mutate({ jobId: job.id, format: 'csv' })}
                  isLoading={downloadMutation.isPending}
                />
              </div>
            </div>
          )}
        </div>
      )}

      {/* Job History */}
      <div className="border-t border-gray-700 pt-6">
        <JobHistory />
      </div>
    </div>
  )
}


function JobStatusIcon({ status }: { status: string }) {
  switch (status) {
    case 'completed':
      return <CheckCircle className="w-6 h-6 text-nvidia-green" />
    case 'failed':
      return <XCircle className="w-6 h-6 text-red-500" />
    case 'running':
      return <Loader2 className="w-6 h-6 text-nvidia-green animate-spin" />
    default:
      return <Clock className="w-6 h-6 text-gray-400" />
  }
}

interface DownloadButtonProps {
  format: string
  icon: React.ReactNode
  label: string
  onClick: () => void
  isLoading: boolean
}

function DownloadButton({ icon, label, onClick, isLoading }: DownloadButtonProps) {
  return (
    <button
      onClick={onClick}
      disabled={isLoading}
      className="btn-secondary flex flex-col items-center gap-2 py-4"
    >
      {icon}
      <span>{label}</span>
    </button>
  )
}
