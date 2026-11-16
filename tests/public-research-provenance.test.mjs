import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import os from 'node:os'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import test from 'node:test'
import { prepareCurrentResearchProvenance } from '../scripts/prepare-current-research-provenance.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))
const read = relative => fs.readFile(path.join(root, relative), 'utf8')
const manifest = JSON.parse(await read('config/current-research-provenance.v1.json'))
const inventory = JSON.parse(await read('src/data/results-physics.json'))
const guide = await read('website/research/provenance/current-results.md')

test('compact provenance pins immediate sources/tools and historical receipt identities without scientific replay', () => {
  assert.equal(manifest.entries.length, 10)
  assert.equal(manifest.scientific_replay_performed, false)
  assert.equal(manifest.scientific_verdicts_modified, false)
  assert.equal(manifest.receipt_source_compatibility, 'not revalidated')
  assert.equal(manifest.transitive_dependency_closure, 'not claimed')
  assert(Buffer.byteLength(JSON.stringify(manifest)) < 65536)
  let receipts = 0
  for (const entry of manifest.entries) {
    assert.equal(entry.reported_status, inventory.find(item => item.slug === entry.slug).status)
    assert(entry.boundary)
    for (const pin of [...entry.source_packets, ...entry.checker_sources]) assert.match(pin.text_sha256, /^[a-f0-9]{64}$/)
    for (const receipt of entry.historical_receipts) {
      receipts++
      assert.match(receipt.sha256, /^[a-f0-9]{64}$/)
      assert(receipt.bytes > 0)
      assert(!('payload' in receipt) && !('log' in receipt))
    }
  }
  assert.equal(receipts, 16)
})

test('fresh metadata publication succeeds without any ignored historical receipts', async () => {
  const temp = await fs.mkdtemp(path.join(os.tmpdir(), 'marici-provenance-'))
  try {
    await fs.mkdir(path.join(temp, 'config'), { recursive: true })
    await fs.mkdir(path.join(temp, 'src/data'), { recursive: true })
    const config = path.join(temp, 'config/current-research-provenance.v1.json')
    await fs.writeFile(config, JSON.stringify(manifest))
    await fs.writeFile(path.join(temp, 'src/data/results-physics.json'), JSON.stringify(inventory))
    const inputs = new Set(manifest.entries.flatMap(entry => [...entry.source_packets, ...entry.checker_sources].map(pin => pin.path)))
    for (const file of inputs) {
      await fs.mkdir(path.dirname(path.join(temp, file)), { recursive: true })
      await fs.copyFile(path.join(root, file), path.join(temp, file))
    }
    for (const entry of manifest.entries) for (const receipt of entry.historical_receipts) await assert.rejects(fs.access(path.join(temp, receipt.path)), { code: 'ENOENT' })
    const result = await prepareCurrentResearchProvenance(temp)
    assert.equal(result.slugs.length, 10)
    await prepareCurrentResearchProvenance(temp, { check: true })
    const output = path.join(temp, result.target)
    const before = await fs.readFile(output)
    const first = path.join(temp, manifest.entries[0].source_packets[0].path)
    const source = await fs.readFile(first, 'utf8')
    await fs.writeFile(first, source.replace(/\r\n?/g, '\n').replace(/\n/g, '\r\n'))
    await prepareCurrentResearchProvenance(temp, { check: true })
    await fs.appendFile(first, '\n<!-- changed source -->')
    await assert.rejects(prepareCurrentResearchProvenance(temp), /Stale publication provenance source/)
    assert((await fs.readFile(output)).equals(before), 'Source drift silently refreshed pins/output')
    await fs.writeFile(first, source)

    const overstated = structuredClone(manifest)
    overstated.scientific_replay_performed = true
    await fs.writeFile(config, JSON.stringify(overstated))
    await assert.rejects(prepareCurrentResearchProvenance(temp), /overstated/)
    const badReceipt = structuredClone(manifest)
    badReceipt.entries[0].historical_receipts[0].sha256 = 'not-an-identifier'
    await fs.writeFile(config, JSON.stringify(badReceipt))
    await assert.rejects(prepareCurrentResearchProvenance(temp), /Invalid historical receipt/)
    const unsafe = structuredClone(manifest)
    unsafe.entries[0].source_packets[0].path = 'research/../secret.md'
    await fs.writeFile(config, JSON.stringify(unsafe))
    await assert.rejects(prepareCurrentResearchProvenance(temp), /Invalid provenance source pin/)
    await fs.writeFile(config, JSON.stringify(manifest))
    await fs.appendFile(output, 'stale')
    await assert.rejects(prepareCurrentResearchProvenance(temp, { check: true }), /Stale public provenance copy/)
  } finally { await fs.rm(temp, { recursive: true, force: true }) }
})

test('actual generated manifest is current and all selected pages expose the provenance guide', async () => {
  await prepareCurrentResearchProvenance(root, { check: true })
  for (const entry of manifest.entries) {
    const page = await read(`website/research/results/${entry.slug}.md`)
    assert(page.includes('/research/provenance/current-results'), entry.slug)
    assert(page.includes('Metadata validation is not scientific replay'), entry.slug)
  }
  assert((await read('docs/results-page.md')).includes('/research/provenance/current-results'))
})

test('reader guide states hash bases, historical compatibility limits and reproduction policy', () => {
  for (const phrase of ['17 immediate source-packet', '17 checker-source', '16 historical receipt', 'CRLF/CR normalized to LF', 'exact captured receipt bytes', 'not a full transitive dependency closure', 'Receipt/source compatibility is not revalidated', 'not newly inspected or executed binaries', 'successor snapshot']) assert(guide.includes(phrase), phrase)
  assert(guide.includes('/research/provenance/current-results.v1.json'))
  assert(guide.includes('--capture'))
  assert((manifest.reproduction).includes('owning source packet'))
})
