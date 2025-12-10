import { clsx } from 'clsx'
import { Check } from 'lucide-react'
import { industries } from '@/data/industries'
import { useConfigStore } from '@/stores/configStore'

export function ScenarioSelector() {
  const { config, toggleScenario } = useConfigStore()
  const industry = industries.find((i) => i.id === config.industry)

  if (!industry) return null

  return (
    <div className="space-y-4">
      <div>
        <h2 className="text-2xl font-bold text-white mb-2">Select Scenarios</h2>
        <p className="text-gray-400">
          Choose call scenarios for {industry.name}. Select multiple for variety.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {industry.scenarios.map((scenario) => {
          const isSelected = config.scenarios.includes(scenario.id)
          return (
            <button
              key={scenario.id}
              onClick={() => toggleScenario(scenario.id)}
              className={clsx(
                'card text-left transition-all flex items-start gap-3',
                isSelected
                  ? 'border-nvidia-green bg-nvidia-green/5'
                  : 'hover:border-gray-700'
              )}
            >
              <div
                className={clsx(
                  'w-5 h-5 rounded border-2 flex items-center justify-center flex-shrink-0 mt-0.5',
                  isSelected ? 'bg-nvidia-green border-nvidia-green' : 'border-gray-600'
                )}
              >
                {isSelected && <Check className="w-3 h-3 text-black" />}
              </div>
              <div>
                <h3 className="font-semibold text-white">{scenario.name}</h3>
                <p className="text-sm text-gray-400">{scenario.description}</p>
              </div>
            </button>
          )
        })}
      </div>

      {config.scenarios.length > 0 && (
        <p className="text-sm text-nvidia-green">
          {config.scenarios.length} scenario{config.scenarios.length > 1 ? 's' : ''} selected
        </p>
      )}
    </div>
  )
}
