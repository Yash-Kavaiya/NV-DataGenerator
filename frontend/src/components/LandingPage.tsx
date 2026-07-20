import { useNavigate } from 'react-router-dom'
import { ArrowRight, Sparkles, Database, Languages, ShieldCheck } from 'lucide-react'
import { Header } from './Header'
import { sectors } from '@/data/sectors'
import { useConfigStore } from '@/stores/configStore'

export function LandingPage() {
  const navigate = useNavigate()
  const { setIndustry, setStep } = useConfigStore()

  // Generic entry: start the wizard from the top.
  const launch = () => {
    setStep(0)
    navigate('/app')
  }

  // Sector card: pre-select the industry and jump straight to the Scenarios step.
  const openSector = (industryId: string) => {
    setIndustry(industryId)
    setStep(1)
    navigate('/app')
  }

  return (
    <div className="min-h-screen bg-gray-950">
      <Header />

      {/* Hero */}
      <section className="relative overflow-hidden border-b border-gray-800">
        {/* ambient green glow */}
        <div
          aria-hidden
          className="pointer-events-none absolute -top-40 left-1/2 -translate-x-1/2 w-[900px] h-[900px] rounded-full opacity-20 blur-3xl"
          style={{ background: 'radial-gradient(circle, #76B900 0%, transparent 60%)' }}
        />
        <div className="relative max-w-5xl mx-auto px-4 py-20 md:py-28 text-center">
          <div className="inline-flex items-center gap-2 px-3 py-1.5 mb-6 rounded-full border border-nvidia-green/40 bg-nvidia-green/10 text-nvidia-green text-sm font-medium">
            <Sparkles className="w-4 h-4" />
            Powered by NVIDIA NeMo Data Designer
          </div>

          <h1 className="text-4xl md:text-6xl font-bold text-white tracking-tight">
            Synthetic data for every{' '}
            <span className="text-nvidia-green">regulated industry</span>
          </h1>

          <p className="mt-6 text-lg md:text-xl text-gray-400 max-w-2xl mx-auto">
            Generate privacy-safe, statistically faithful datasets for the six highest-value
            sectors — where real data is scarce, sensitive, or expensive to label.
          </p>

          <div className="mt-9 flex flex-col sm:flex-row items-center justify-center gap-3">
            <button onClick={launch} className="btn-primary flex items-center gap-2 px-6 py-3 text-base">
              Launch Generator
              <ArrowRight className="w-5 h-5" />
            </button>
            <a href="#sectors" className="btn-secondary px-6 py-3 text-base">
              Explore sectors
            </a>
          </div>

          {/* stat strip */}
          <div className="mt-12 flex flex-wrap items-center justify-center gap-x-8 gap-y-3 text-sm text-gray-400">
            <span className="flex items-center gap-2">
              <Database className="w-4 h-4 text-nvidia-green" /> 17 industries
            </span>
            <span className="flex items-center gap-2">
              <Languages className="w-4 h-4 text-nvidia-green" /> 13 languages
            </span>
            <span className="flex items-center gap-2">
              <ShieldCheck className="w-4 h-4 text-nvidia-green" /> Privacy-safe by design
            </span>
          </div>
        </div>
      </section>

      {/* Sectors */}
      <section id="sectors" className="max-w-7xl mx-auto px-4 py-16 md:py-20">
        <div className="text-center max-w-2xl mx-auto mb-12">
          <h2 className="text-3xl md:text-4xl font-bold text-white">Six high-value sectors</h2>
          <p className="mt-3 text-gray-400">
            Each sector maps to a ready-to-run generator. Pick one to jump straight into
            configuring your synthetic dataset.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {sectors.map((sector) => (
            <button
              key={sector.id}
              onClick={() => openSector(sector.industryId)}
              className="card text-left flex flex-col h-full transition-all hover:scale-[1.02] hover:border-nvidia-green/60 group"
            >
              <div className="flex items-start justify-between gap-3">
                <div className="text-4xl">{sector.icon}</div>
                <span className="text-xs font-semibold text-nvidia-green bg-nvidia-green/10 border border-nvidia-green/30 px-2.5 py-1 rounded-full">
                  {sector.tier}
                </span>
              </div>

              <h3 className="mt-4 text-lg font-semibold text-white">{sector.title}</h3>
              <p className="mt-2 text-sm text-gray-400 leading-relaxed">{sector.why}</p>

              <div className="mt-4">
                <p className="text-xs font-semibold uppercase tracking-wide text-gray-500 mb-2">
                  Key use cases
                </p>
                <div className="flex flex-wrap gap-1.5">
                  {sector.useCases.map((useCase) => (
                    <span
                      key={useCase}
                      className="text-xs text-gray-300 bg-gray-800 border border-gray-700 px-2 py-1 rounded-md"
                    >
                      {useCase}
                    </span>
                  ))}
                </div>
              </div>

              <p className="mt-4 text-xs text-gray-500 leading-relaxed">{sector.opportunity}</p>

              <div className="mt-5 pt-4 border-t border-gray-800 flex items-center gap-2 text-sm font-medium text-nvidia-green">
                Generate data
                <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
              </div>
            </button>
          ))}
        </div>
      </section>

      {/* Footer CTA */}
      <section className="border-t border-gray-800 bg-gray-900/40">
        <div className="max-w-4xl mx-auto px-4 py-16 text-center">
          <h2 className="text-2xl md:text-3xl font-bold text-white">Ready to generate?</h2>
          <p className="mt-3 text-gray-400">
            Configure industry, scenarios, sentiment and volume — then export in your format of choice.
          </p>
          <button
            onClick={launch}
            className="btn-primary inline-flex items-center gap-2 mt-8 px-6 py-3 text-base"
          >
            Launch Generator
            <ArrowRight className="w-5 h-5" />
          </button>
        </div>
      </section>
    </div>
  )
}
