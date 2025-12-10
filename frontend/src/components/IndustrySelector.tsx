import { clsx } from 'clsx'
import { industries } from '@/data/industries'
import { useConfigStore } from '@/stores/configStore'

export function IndustrySelector() {
  const { config, setIndustry } = useConfigStore()

  return (
    <div className="space-y-4">
      <div>
        <h2 className="text-2xl font-bold text-white mb-2">Select Industry</h2>
        <p className="text-gray-400">Choose the industry for your synthetic contact center transcripts</p>
      </div>

      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        {industries.map((industry) => (
          <button
            key={industry.id}
            onClick={() => setIndustry(industry.id)}
            className={clsx(
              'card text-left transition-all hover:scale-[1.02]',
              config.industry === industry.id
                ? 'border-nvidia-green ring-2 ring-nvidia-green/20'
                : 'hover:border-gray-700'
            )}
          >
            <div className="text-4xl mb-3">{industry.icon}</div>
            <h3 className="text-lg font-semibold text-white">{industry.name}</h3>
            <p className="text-sm text-gray-400 mt-1">{industry.description}</p>
          </button>
        ))}
      </div>
    </div>
  )
}
