import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import os from 'node:os'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'
import test from 'node:test'
import { preparePublicationResearchProvenance, prepareSuccessorResearchProvenance } from '../scripts/prepare-research-provenance-successor.mjs'
const root = fileURLToPath(new URL('../', import.meta.url))
const read = file => fs.readFile(path.join(root, file), 'utf8')
const load = () => read('config/current-research-provenance.v2.json').then(JSON.parse)
const canonicalHash = value => createHash('sha256').update(JSON.stringify(value, null, 2) + '\n').digest('hex')
const frozen = '2963ef78d9cf0b8137ca0f54bdc7d10b6351c47abdf936ef16315c012496d611'

test('historical ten-family v1 remains frozen rather than repinned or extended', async () => {
  const v1 = JSON.parse(await read('config/current-research-provenance.v1.json'))
  assert.equal(canonicalHash(v1), frozen)
  assert.equal(v1.entries.length, 10)
  assert(!v1.entries.some(entry => entry.slug === 'source-certified-coherent-assembly'))
})

test('v2 binds two result statuses and three guide scopes without claiming replay, compatibility or dependency closure', async () => {
  const v2 = await load()
  assert.equal(v2.predecessor.canonical_sha256, frozen)
  assert.equal(v2.entries.length, 5)
  assert.equal(v2.entries.filter(entry => entry.kind === 'result').length, 2)
  assert.equal(v2.scientific_replay_performed, false)
  assert.equal(v2.scientific_verdicts_modified, false)
  assert.equal(v2.receipt_source_compatibility, 'not revalidated')
  assert.equal(v2.transitive_dependency_closure, 'not claimed')
  assert(Buffer.byteLength(JSON.stringify(v2)) < 65536)
  assert.equal(v2.entries.flatMap(entry => entry.source_packets).length, 36)
  assert.equal(v2.entries.flatMap(entry => entry.checker_sources).length, 27)
  assert.equal(v2.entries.flatMap(entry => entry.historical_receipts).length, 19)
  const programme = v2.entries.find(entry => entry.id === 'ramsey-november-programme')
  for (const name of ['check_pairwise_rigidity_base.py', 'check_circulant_reduction.py', 'verify_neighborhood_stability.py']) assert(programme.unavailable_inputs.some(input => input.reference.endsWith(name)))
  assert(v2.entries.find(entry => entry.id === 'held-pe-publication-explanation').compatibility_limits.join(' ').includes('publication-registration mismatch'))
})

async function fixture() {
  const base = await fs.mkdtemp(path.join(os.tmpdir(), 'provenance-v2-'))
  const v1 = JSON.parse(await read('config/current-research-provenance.v1.json'))
  const v2 = await load()
  const files = new Set(['config/current-research-provenance.v1.json', 'config/current-research-provenance.v2.json', 'config/research-provenance-selection.v2.json', 'src/data/results-physics.json',
    ...v1.entries.flatMap(entry => [...entry.source_packets, ...entry.checker_sources].map(pin => pin.path)),
    ...v2.entries.flatMap(entry => [...entry.source_packets, ...entry.checker_sources].map(pin => pin.path))])
  for (const file of files) { await fs.mkdir(path.dirname(path.join(base, file)), { recursive: true }); await fs.copyFile(path.join(root, file), path.join(base, file)) }
  return { base, v2 }
}

test('successor publishes without any historical receipt payloads; newline normalization does not recapture', async () => {
  const { base, v2 } = await fixture()
  try {
    for (const receipt of v2.entries.flatMap(entry => entry.historical_receipts)) await assert.rejects(fs.access(path.join(base, receipt.path)), { code: 'ENOENT' })
    const result = await preparePublicationResearchProvenance(base)
    assert.equal(result.slugs.length, 12)
    assert.equal(result.routes.length, 5)
    await preparePublicationResearchProvenance(base, { check: true })
    const first = path.join(base, v2.entries[0].source_packets[0].path)
    await fs.writeFile(first, (await fs.readFile(first, 'utf8')).replace(/\r\n?/g, '\n').replace(/\n/g, '\r\n'))
    await prepareSuccessorResearchProvenance(base, { check: true })
  } finally { await fs.rm(base, { recursive: true, force: true }) }
})

test('changed source, checker, result status or public copy fails without silently refreshing pins', async () => {
  const { base, v2 } = await fixture()
  try {
    const result = await preparePublicationResearchProvenance(base)
    const config = path.join(base, 'config/current-research-provenance.v2.json')
    const output = path.join(base, result.target)
    const before = await fs.readFile(output)
    for (const pin of [v2.entries[0].source_packets[0], v2.entries[0].checker_sources[0]]) {
      const file = path.join(base, pin.path), old = await fs.readFile(file)
      await fs.appendFile(file, '\nchanged')
      await assert.rejects(prepareSuccessorResearchProvenance(base), /Stale successor source/)
      assert((await fs.readFile(output)).equals(before))
      await fs.writeFile(file, old)
    }
    const inventoryFile = path.join(base, 'src/data/results-physics.json')
    const inventory = JSON.parse(await fs.readFile(inventoryFile, 'utf8'))
    inventory.find(entry => entry.slug === v2.entries[0].id).status = 'promoted without review'
    await fs.writeFile(inventoryFile, JSON.stringify(inventory))
    await assert.rejects(prepareSuccessorResearchProvenance(base), /Stale successor result/)
    assert.equal(JSON.parse(await fs.readFile(config, 'utf8')).entries[0].reported_status, v2.entries[0].reported_status)
    await fs.copyFile(path.join(root, 'src/data/results-physics.json'), inventoryFile)
    await fs.appendFile(output, 'stale')
    await assert.rejects(prepareSuccessorResearchProvenance(base, { check: true }), /Stale successor public/)
  } finally { await fs.rm(base, { recursive: true, force: true }) }
})

test('false replay, unsafe metadata, erased missing-input boundary and missing family are rejected', async () => {
  const { base, v2 } = await fixture()
  try {
    const config = path.join(base, 'config/current-research-provenance.v2.json')
    for (const mutate of [
      value => { value.scientific_replay_performed = true },
      value => { value.entries[0].historical_receipts[0].sha256 = 'invalid' },
      value => { value.entries[0].historical_receipts[0].payload = { matrices: [] } },
      value => { value.entries[0].source_packets[0].path = 'research/../secret' },
      value => { value.entries[2].unavailable_inputs = [] },
      value => { value.entries.pop() },
      value => { value.capture_kind = 'Scientific replay passed' },
    ]) {
      const changed = structuredClone(v2); mutate(changed)
      await fs.writeFile(config, JSON.stringify(changed))
      await assert.rejects(prepareSuccessorResearchProvenance(base), /overstated|Invalid|Unsupported|selection|Missing/)
    }
  } finally { await fs.rm(base, { recursive: true, force: true }) }
})

test('predecessor and editorial selection drift are rejected before metadata can be refreshed', async () => {
  const { base } = await fixture()
  try {
    const result = await preparePublicationResearchProvenance(base)
    const before = await fs.readFile(path.join(base, result.predecessor.target))
    const previous = path.join(base, 'config/current-research-provenance.v1.json')
    const old = JSON.parse(await fs.readFile(previous, 'utf8')); old.captured_at = 'changed'
    await fs.writeFile(previous, JSON.stringify(old))
    await assert.rejects(preparePublicationResearchProvenance(base), /Frozen predecessor/)
    assert((await fs.readFile(path.join(base, result.predecessor.target))).equals(before))
    await fs.copyFile(path.join(root, 'config/current-research-provenance.v1.json'), previous)
    const file = path.join(base, 'config/research-provenance-selection.v2.json')
    const spec = JSON.parse(await fs.readFile(file, 'utf8')); spec.entries[0].boundary += ' changed'
    await fs.writeFile(file, JSON.stringify(spec))
    await assert.rejects(prepareSuccessorResearchProvenance(base), /selection drift/)
  } finally { await fs.rm(base, { recursive: true, force: true }) }
})

test('all newly curated routes expose successor provenance while v1 remains downloadable', async () => {
  const v2 = await load()
  const guide = await read('website/research/provenance/current-results.md')
  assert(guide.includes('/research/provenance/current-results.v2.json'))
  assert(guide.includes('/research/provenance/current-results.v1.json'))
  for (const entry of v2.entries) {
    const file = 'website' + entry.route + '.md'
    assert((await read(file)).includes('/research/provenance/current-results'), entry.id)
    assert(guide.includes(entry.route), entry.id)
  }
  await preparePublicationResearchProvenance(root, { check: true })
})
