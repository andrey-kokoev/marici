import registry from '../data/frontiers/registry.json'

export type FrontierKind = 'calculus' | 'physical' | 'upstream'

export interface FrontierEvidence {
  label: string
  href: string
}

export interface FrontierSector {
  id: string
  name: string
  kind: FrontierKind
  carrier: string
  coefficient: string
  selection: string
  sharp_result: string
  frontier: string
  next_test: string
  strength: string
  evidence: FrontierEvidence[]
}

export interface FrontierRelease {
  schema: 'marici.frontier-atlas.v1'
  version: string
  label: string
  released_at: string
  status: 'historical' | 'current'
  summary: string
  pins: {
    git_commit: string
    git_commit_role: 'source_baseline'
    epistemic_event: string
    epistemic_head: string
    epistemic_event_count?: number
    evidence_through_event?: number
    ledger_sequence_ceiling: number
  }
  supersedes: string | null
  changes: string[]
  sectors: FrontierSector[]
}

const modules = import.meta.glob<{ default: FrontierRelease }>(
  '../data/frontiers/[0-9]*.json',
  { eager: true },
)

const releases = Object.values(modules)
  .map((module) => module.default)
  .sort((left, right) => left.version.localeCompare(right.version, undefined, { numeric: true }))

if (releases.length !== registry.versions.length) {
  throw new Error('Frontier registry and immutable release count disagree')
}

for (const release of releases) {
  if (release.schema !== 'marici.frontier-atlas.v1') {
    throw new Error(`Unsupported frontier schema in ${release.version}`)
  }
  if (!registry.versions.includes(release.version)) {
    throw new Error(`Unregistered frontier release ${release.version}`)
  }
  const sectorIds = release.sectors.map((sector) => sector.id)
  if (new Set(sectorIds).size !== sectorIds.length) {
    throw new Error(`Duplicate sector id in frontier release ${release.version}`)
  }
}

export const frontierRegistry = registry
export const frontierReleases = releases
const selectedCurrentFrontier = releases.find((release) => release.version === registry.current)

if (!selectedCurrentFrontier) {
  throw new Error(`Current frontier release ${registry.current} is missing`)
}

export const currentFrontier: FrontierRelease = selectedCurrentFrontier
