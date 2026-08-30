import { readdir, readFile } from 'node:fs/promises'
import path from 'node:path'

const root = path.resolve('src/data/oddballs')
const registry = JSON.parse(await readFile(path.join(root, 'registry.json'), 'utf8'))
const files = (await readdir(root)).filter((name) => /^\d+\.\d+\.\d+\.json$/.test(name))
  .sort((left, right) => left.localeCompare(right, undefined, { numeric: true }))
const releases = await Promise.all(files.map(async (name) => JSON.parse(await readFile(path.join(root, name), 'utf8'))))
const statuses = new Set(['open', 'explained', 'promoted', 'dissolved', 'superseded'])
const confidences = new Set(['high', 'medium-high', 'medium', 'medium-low', 'low'])
const assert = (condition, message) => { if (!condition) throw new Error(message) }

assert(registry.schema === 'marici.oddball-observatory.registry.v1', 'Unsupported oddball registry schema')
assert(JSON.stringify(files.map((name) => name.slice(0, -5))) === JSON.stringify(registry.versions), 'Oddball registry must exactly match immutable releases')
for (const [index, release] of releases.entries()) {
  assert(release.schema === 'marici.oddball-observatory.v1', `Unsupported schema in ${files[index]}`)
  assert(release.version === files[index].slice(0, -5), `Filename/version mismatch in ${files[index]}`)
  assert(/^[0-9a-f]{40}$/.test(release.pins?.git_commit), `Invalid Git pin in ${release.version}`)
  assert(release.pins?.git_commit_role === 'source_baseline', `Untyped Git pin in ${release.version}`)
  assert(Number.isInteger(release.pins?.ledger_sequence_ceiling), `Invalid ledger ceiling in ${release.version}`)
  assert(release.observations?.length > 0, `Release ${release.version} has no observations`)
  assert(new Set(release.observations.map((item) => item.id)).size === release.observations.length, `Duplicate observation id in ${release.version}`)
  for (const item of release.observations) {
    assert(statuses.has(item.status), `Invalid status in ${release.version}/${item.id}`)
    assert(confidences.has(item.confidence), `Invalid confidence in ${release.version}/${item.id}`)
    assert(Array.isArray(item.sectors) && item.sectors.length > 0, `Missing sectors in ${release.version}/${item.id}`)
    for (const field of ['name', 'first_seen', 'last_updated', 'observation', 'invariant_content', 'caution', 'next_test'])
      assert(typeof item[field] === 'string' && item[field].trim(), `Missing ${field} in ${release.version}/${item.id}`)
    assert(Array.isArray(item.evidence) && item.evidence.length > 0, `Missing evidence in ${release.version}/${item.id}`)
  }
  assert(index === 0 ? release.supersedes === null : release.supersedes === releases[index - 1].version, `Bad supersession in ${release.version}`)
}
const current = releases.filter((release) => release.status === 'current')
assert(current.length === 1 && current[0].version === registry.current, 'Exactly one registered release must be current')
assert(releases.at(-1)?.version === registry.current, 'Current oddball release must be latest')
console.log(`Oddball Observatory OK: ${releases.length} immutable release, ${releases.at(-1).observations.length} observations`)
