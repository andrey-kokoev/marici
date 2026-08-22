import registry from '../data/oddballs/registry.json'

export type OddballStatus = 'open' | 'explained' | 'promoted' | 'dissolved' | 'superseded'
export type OddballConfidence = 'high' | 'medium-high' | 'medium' | 'medium-low' | 'low'

export interface OddballEvidence { label: string; href: string }

export interface OddballObservation {
  id: string
  name: string
  status: OddballStatus
  confidence: OddballConfidence
  first_seen: string
  last_updated: string
  sectors: string[]
  observation: string
  invariant_content: string
  caution: string
  next_test: string
  evidence: OddballEvidence[]
}

export interface OddballRelease {
  schema: 'marici.oddball-observatory.v1'
  version: string
  label: string
  released_at: string
  status: 'historical' | 'current'
  summary: string
  pins: { git_commit: string; git_commit_role: 'source_baseline'; ledger_sequence_ceiling: number }
  supersedes: string | null
  changes: string[]
  observations: OddballObservation[]
}

const modules = import.meta.glob<{ default: OddballRelease }>('../data/oddballs/[0-9]*.json', { eager: true })
const releases = Object.values(modules).map((module) => module.default)
  .sort((left, right) => left.version.localeCompare(right.version, undefined, { numeric: true }))

if (releases.length !== registry.versions.length) throw new Error('Oddball registry and immutable release count disagree')
for (const release of releases) {
  if (release.schema !== 'marici.oddball-observatory.v1') throw new Error(`Unsupported oddball schema in ${release.version}`)
  if (!registry.versions.includes(release.version)) throw new Error(`Unregistered oddball release ${release.version}`)
  const ids = release.observations.map((observation) => observation.id)
  if (new Set(ids).size !== ids.length) throw new Error(`Duplicate oddball id in ${release.version}`)
}

export const oddballRegistry = registry
export const oddballReleases = releases
const selected = releases.find((release) => release.version === registry.current)
if (!selected) throw new Error(`Current oddball release ${registry.current} is missing`)
export const currentOddballs: OddballRelease = selected
