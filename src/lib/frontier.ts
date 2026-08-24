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

export type ProgressStatus = 'established' | 'partial' | 'open' | 'falsified' | 'not_applicable'
export type PartialReason = 'typed_not_constructed' | 'constructed_not_verified' | 'verified_limited_scope' | 'blocked_missing_source_input'

export interface ProgressBasis {
  authority_type: 'epistemic_entity' | 'ledger_entry'
  ref: string
  event_id?: string
  href?: string
  label: string
}

export interface ProgressCell {
  status: ProgressStatus
  partial_reason: PartialReason | null
  explanation: string
  evidence_summary: string
  status_basis: ProgressBasis[]
  review_owner: string
  changed_in_version: string
  what_remains: string
  selector_maturity?: 'untyped' | 'typed' | 'constructed' | 'constructed_verified'
}

export interface ProgressSnapshot {
  schema: 'marici.frontier-progress-snapshot.v1'
  version: string
  review_status: 'reviewed'
  introduction: string
  selector_note: string
  stages: { id: string; label: string }[]
  sectors: { id: string; name: string; lens_family_object: string; cells: Record<string, ProgressCell> }[]
  review_records: { decision: string; review_owner: string; sector: string; note?: string }[]
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
const snapshotModules = import.meta.glob<{ default: ProgressSnapshot }>(
  '../data/frontier-snapshots/reviewed/[0-9]*.json',
  { eager: true },
)
export const frontierProgressSnapshots = Object.fromEntries(
  Object.values(snapshotModules).map((module) => [module.default.version, module.default]),
) as Record<string, ProgressSnapshot>
const selectedCurrentFrontier = releases.find((release) => release.version === registry.current)

if (!selectedCurrentFrontier) {
  throw new Error(`Current frontier release ${registry.current} is missing`)
}

export const currentFrontier: FrontierRelease = selectedCurrentFrontier
