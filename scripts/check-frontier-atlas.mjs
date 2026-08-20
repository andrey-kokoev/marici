import { readdir, readFile } from 'node:fs/promises'
import path from 'node:path'

const root = path.resolve('src/data/frontiers')
const registry = JSON.parse(await readFile(path.join(root, 'registry.json'), 'utf8'))
const files = (await readdir(root))
  .filter((name) => /^\d+\.\d+\.\d+\.json$/.test(name))
  .sort((left, right) => left.localeCompare(right, undefined, { numeric: true }))
const releases = await Promise.all(
  files.map(async (name) => JSON.parse(await readFile(path.join(root, name), 'utf8'))),
)

function assert(condition, message) {
  if (!condition) throw new Error(message)
}

assert(registry.schema === 'marici.frontier-atlas.registry.v1', 'Unsupported registry schema')
assert(
  JSON.stringify(files.map((name) => name.slice(0, -5))) === JSON.stringify(registry.versions),
  'Registry versions must exactly match ordered immutable release files',
)

const seen = new Set()
for (const [index, release] of releases.entries()) {
  assert(release.schema === 'marici.frontier-atlas.v1', `Unsupported release schema in ${files[index]}`)
  assert(release.version === files[index].slice(0, -5), `Filename/version mismatch in ${files[index]}`)
  assert(!seen.has(release.version), `Duplicate release ${release.version}`)
  assert(release.pins?.git_commit_role === 'source_baseline', `Untyped Git pin in ${release.version}`)
  assert(/^[0-9a-f]{40}$/.test(release.pins?.git_commit), `Invalid Git pin in ${release.version}`)
  assert(/^ev-\d{12}-[0-9a-f-]{36}$/.test(release.pins?.epistemic_event), `Invalid graph event in ${release.version}`)
  assert(Number.isInteger(release.pins?.ledger_sequence_ceiling), `Invalid ledger ceiling in ${release.version}`)
  assert(release.sectors?.length > 0, `Release ${release.version} has no sectors`)
  assert(new Set(release.sectors.map((sector) => sector.id)).size === release.sectors.length, `Duplicate sector id in ${release.version}`)
  for (const sector of release.sectors) {
    for (const field of ['name', 'kind', 'carrier', 'coefficient', 'selection', 'sharp_result', 'frontier', 'next_test', 'strength']) {
      assert(typeof sector[field] === 'string' && sector[field].trim(), `Missing ${field} in ${release.version}/${sector.id}`)
    }
    assert(Array.isArray(sector.evidence) && sector.evidence.length > 0, `Missing evidence in ${release.version}/${sector.id}`)
  }
  if (index === 0) {
    assert(release.supersedes === null, 'First release must not supersede another release')
  } else {
    assert(release.supersedes === releases[index - 1].version, `Release ${release.version} must supersede its immediate predecessor`)
  }
  seen.add(release.version)
}

const current = releases.filter((release) => release.status === 'current')
assert(current.length === 1, 'Exactly one release must be current')
assert(current[0].version === registry.current, 'Registry current version and release status disagree')
assert(releases.at(-1)?.version === registry.current, 'Current version must be the latest registered release')

console.log(`Frontier Atlas OK: ${releases.length} immutable releases, current v${registry.current}`)
