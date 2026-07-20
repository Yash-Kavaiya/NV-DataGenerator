# Six-Sector Landing Page — Design

**Date:** 2026-07-18
**Status:** Approved
**Scope:** Frontend only (no backend, store, or type changes)

## Goal

Add a marketing-style landing page as the app's new first page (`/`) that showcases
six high-value synthetic-data sectors. Each sector card is clickable and drops the
user into the existing generation wizard with that sector's industry pre-selected.

## Key finding

The backend already supports all six sectors — templates, router entries, and
scenarios exist for `healthcare`, `finance`, `automotive`, `retail`,
`manufacturing`, and `government`. Only the **frontend** `industries.ts` is out of
sync (it lists just `healthcare`, `finance`, `retail`, `telecom`, `saas`). So this
work is frontend-only.

## Routing

| Route | Before | After |
|---|---|---|
| `/` | `ConfigWizard` | **`LandingPage`** (new) |
| `/app` | — | `ConfigWizard` (moved) |
| `/transcripts/:jobId` | `TranscriptViewer` | unchanged |

## Sector → industry mapping

| # | Landing card title | industry id | frontend | backend |
|---|---|---|---|---|
| 1 | Healthcare & Life Sciences | `healthcare` | exists | exists |
| 2 | Banking, Financial Services & Insurance (BFSI) | `finance` | exists | exists |
| 3 | Automotive & Autonomous Vehicles | `automotive` | **add** | exists |
| 4 | Retail & E-commerce | `retail` | exists | exists |
| 5 | Manufacturing & Industrial | `manufacturing` | **add** | exists |
| 6 | Government & Defense | `government` | **add** | exists |

## Landing page structure

NVIDIA dark/green theme (`bg-gray-950`, `nvidia-green #76B900`), matching the existing
app. (The referenced hackathon PDF could not be rendered in this environment; the
design stays on-brand with the current dark tech aesthetic.)

1. **Nav** — reuse existing `Header` component + a "Launch Generator" button.
2. **Hero** — headline, subheadline, primary CTA `Launch Generator →` (→ `/app`),
   secondary "Explore sectors" (scrolls to grid), and a small stat strip
   (17 industries · multilingual · NeMo Data Designer).
3. **Six sector cards** — responsive grid (1 / 2 / 3 columns). Each rich card shows:
   icon, title, a tier badge tagline (e.g. "Highest growth potential"), a one-line
   "why top-tier", key use cases (chips/bullets), and a muted "opportunity" note.
   The whole card is clickable.
4. **Footer CTA band** — "Ready to generate?" + Launch button.

## Click behavior

- **Sector card click** → `setIndustry(industryId)` + `setStep(1)` + `navigate('/app')`
  → lands on the Scenarios step with the sector pre-selected.
- **Launch Generator (hero / nav / footer)** → `navigate('/app')` → starts the wizard.

## Files

- **New** `frontend/src/data/sectors.ts` — the six rich landing cards
  (`id, industryId, title, icon, tier, why, useCases[], opportunity`). Keeps
  marketing content separate from the wizard's `industries.ts`.
- **New** `frontend/src/components/LandingPage.tsx` — hero + grid + footer.
- **Edit** `frontend/src/data/industries.ts` — add `automotive`, `manufacturing`,
  `government` with scenarios matching the backend router IDs.
- **Edit** `frontend/src/App.tsx` — `/` → landing, `/app` → wizard.

## Verification

- `npm run build` (tsc + vite) passes with no type errors.
- Landing renders all six sector cards.
- Clicking each card navigates to `/app`, shows the Scenarios step, and the correct
  industry is pre-selected (verified for the three newly added industries).
- "Launch Generator" navigates to `/app`.

## Out of scope

- Backend changes (already supports all sectors).
- Wiring "Automotive & Autonomous Vehicles" / "Government & Defense" beyond the
  existing `automotive` / `government` contact-center scenarios.
- Any change to the wizard steps themselves.
