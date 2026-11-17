import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import os from 'node:os'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'
import test from 'node:test'
import { loadPublicResearchCoverage, canonicalCoverageJSON } from '../scripts/public-research-coverage-config.mjs'
import { preparePublicResearchFrontier } from '../scripts/prepare-public-research-frontier.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))

const read = file => fs.readFile(new URL('../' + file, import.meta.url), 'utf8')

test('current editor frontier does not reopen the three repaired core regressions', async () => {
  const pointer = JSON.parse(await read('config/public-research-coverage.current.json'))
  const current = JSON.parse(await read(pointer.config))
  const editor = current.frontier.find(entry => entry.id === 'editor-replay-integration')
  assert(editor.reported_completed.includes('14 passing checks'))
  assert(!/three unresolved TODO|Repairs for identity-delta/.test(editor.first_missing + editor.acceptance))
  assert(editor.first_missing.includes('whole-definition'))
  assert(editor.first_missing.includes('revision'))
})

test('maintenance and reader guide separate core repairs, broader regressions and unverified browser status', async () => {
  const workflow = await read('docs/public-research-publication.md')
  const guide = await read('website/experiments/isotope-wiring-limitations.md')
  assert(!workflow.includes("three expected TODO failures remain unresolved"))
  for (const text of [workflow, guide]) {
    assert(text.includes('343/371'))
    assert(text.includes('28 failures'))
    assert(text.includes('3ace86e33'))
    assert(text.includes('371/371'))
  }
  assert(!guide.includes('All 33 runs pass'))
  assert(guide.includes('Historical browser report'))
  assert(guide.includes('c1025e302'))
  assert(guide.includes('30/30 runs passed'))
  assert(guide.includes('zero failures or unrun cases'))
  assert(guide.includes('tested dirty working tree'))
  assert(guide.includes('not retired placement-dialog controls'))
})

test('the selector advances to v2 without changing the historical v1 checkpoint', async () => {
  const { contract, snapshots } = await loadPublicResearchCoverage(root)
  assert.equal(contract.snapshot_id, 'public-research-frontier-v2')
  assert.equal(snapshots[1].snapshot_id, 'public-research-frontier-v1')
  assert.equal(snapshots[1].sha256, '4dd13a11c228cc6a5e4b922cac09ef2252134fa227f8d56bd1ed53d1de2a0565')
  assert(snapshots[1].contract.frontier.find(entry => entry.id === 'editor-replay-integration').acceptance.includes('three unresolved TODO'))
  assert(contract.as_of.includes('other research rows retain'))
})

test('public snapshot pointer and historical bytes match the reviewed selector', async () => {
  await preparePublicResearchFrontier(root, { check: true })
  const pointer = JSON.parse(await read('website/public/research/frontier/current.json'))
  assert.equal(pointer.current.snapshot_id, 'public-research-frontier-v2')
  assert(!JSON.stringify(pointer).includes('config/'))
  const historical = await read('website/public/research/frontier/public-research-frontier-v1.json')
  assert.equal(createHash('sha256').update(historical).digest('hex'), pointer.history[0].sha256)
  assert.equal(historical, canonicalCoverageJSON(JSON.parse(await read('config/public-research-coverage.v1.json'))))
  const page = await read('website/research/frontier/current.md')
  assert(page.includes('14 passing checks'))
  assert(page.includes('historical, not current obligations'))
  assert(!page.includes('three unresolved TODO requirements'))
})

test('coverage selector rejects unsafe references, rollback and changed historical sources', async () => {
  const temp = await fs.mkdtemp(path.join(os.tmpdir(), 'marici-current-coverage-'))
  try {
    await fs.mkdir(path.join(temp, 'config'))
    for (const file of ['public-research-coverage.current.json', 'public-research-coverage.v1.json', 'public-research-coverage.v2.json']) await fs.writeFile(path.join(temp, 'config', file), await read('config/' + file))
    const currentFile = path.join(temp, 'config/public-research-coverage.current.json')
    const original = JSON.parse(await fs.readFile(currentFile, 'utf8'))
    await loadPublicResearchCoverage(temp)
    await fs.writeFile(currentFile, JSON.stringify({ ...original, config: '../outside.json' }))
    await assert.rejects(loadPublicResearchCoverage(temp), /Unsafe/)
    await fs.writeFile(currentFile, JSON.stringify({ ...original, snapshot_id: 'public-research-frontier-v1' }))
    await assert.rejects(loadPublicResearchCoverage(temp), /mismatched/)
    await fs.writeFile(currentFile, JSON.stringify({ ...original, config: 'config/public-research-coverage.v1.json', snapshot_id: 'public-research-frontier-v1' }))
    await assert.rejects(loadPublicResearchCoverage(temp), /duplicate/)
    await fs.writeFile(currentFile, JSON.stringify(original))
    const oldFile = path.join(temp, 'config/public-research-coverage.v1.json')
    const historical = JSON.parse(await fs.readFile(oldFile, 'utf8'))
    historical.frontier[0].first_missing += ' silently rewritten'
    await fs.writeFile(oldFile, JSON.stringify(historical))
    await assert.rejects(loadPublicResearchCoverage(temp), /Historical coverage snapshot changed/)
  } finally { await fs.rm(temp, { recursive: true, force: true }) }
})

test('frontier freshness rejects a stale published archive without needing scientific receipts', async () => {
  const temp = await fs.mkdtemp(path.join(os.tmpdir(), 'marici-frontier-snapshot-'))
  try {
    await fs.mkdir(path.join(temp, 'config'))
    for (const file of ['public-research-coverage.current.json', 'public-research-coverage.v1.json', 'public-research-coverage.v2.json']) await fs.writeFile(path.join(temp, 'config', file), await read('config/' + file))
    await preparePublicResearchFrontier(temp)
    await preparePublicResearchFrontier(temp, { check: true })
    await fs.writeFile(path.join(temp, 'website/public/research/frontier/public-research-frontier-v1.json'), '{}\n')
    await assert.rejects(preparePublicResearchFrontier(temp, { check: true }), /Stale generated research frontier/)
  } finally { await fs.rm(temp, { recursive: true, force: true }) }
})
