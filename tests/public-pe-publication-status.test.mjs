import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import test from 'node:test'
import { normalizeNet } from '../src/conjecture-nets/model.js'
import { assertBundledNetFragment } from '../scripts/check-public-research-coverage.mjs'
const read = file => fs.readFile(new URL('../' + file, import.meta.url), 'utf8')
const route = '/experiments/pe-net-publication-status'
const held = 'research/strominger/contracts/persistent-seam-pe-conjecture-net.v1.json'
const guide = () => read('website' + route + '.md')
function requireSelectionBoundary(text) {
  for (const phrase of ['five-net public selection', 'development selection', 'graph admission', 'commit is not publication approval', 'unresolved source wording']) assert(text.includes(phrase), 'Missing P/E publication boundary: ' + phrase)
}

test('P/E status distinguishes committed research, development, graph admission and release', async () => {
  const text = await guide()
  requireSelectionBoundary(text)
  for (const file of ['src/conjecture-nets/catalog.json', 'src/conjecture-nets/development-catalog.json']) assert(text.includes(file), file)
  assert(text.includes('.ai/conjecture-nets/development/'))
  assert(text.includes('not bundled'))
})

test('revision-73 witness-record frontier does not recreate a missing parent cell or scalar-to-cell solution', async () => {
  const source = JSON.parse(await read(held))
  assert.equal(source.revision, 73)
  assert.equal(source.conjectures.length, 131)
  assert.equal(source.frontier.length, 7)
  assert.equal(source.recommended_start, 'f736-boundary-witness-record-graph-lift')
  const text = await guide()
  for (const phrase of ['revision 73', '131 nodes', 'seven', 'f736-boundary-witness-record-graph-lift', 'H234', 'kappa', 'boundary identifications', 'finite representative', 'quotient class alone', 'inverse mate', 'one H736', 'not constructed']) assert(text.includes(phrase), phrase)
  for (const id of ['f736-polarized-kernel-witness-lift-conjecture', 'f736-cutoff-current-transgression-witness-conjecture']) {
    assert.equal(source.conjectures.find(node => node.id === id).status, 'deferred_missing_operation')
    assert(text.includes(id), id)
  }
  assert(text.includes('not mathematically refuted'))
})

test('public source mismatch is explicitly attributed and left for an authorized owner locus', async () => {
  const text = await guide()
  for (const phrase of ['selected explicitly in the public conjecture-net catalog', 'owner-local branch registered for public explorer', 'marici.Strominger', 'not rerun', 'no owner correction', 'not a scientific rejection']) assert(text.includes(phrase), phrase)
  for (const file of ['research/strominger/persistent-seam-pe-conjecture.md', 'research/strominger/persistent-seam-pe-node-typing-review-v28.md', 'research/strominger/checkers/check_persistent_seam_pe_net.mjs']) {
    assert(text.includes(file), file)
    await fs.access(new URL('../' + file, import.meta.url))
  }
})

test('status guide is discoverable and selected as explanation, without advertising a held explorer deep link', async () => {
  for (const file of ['website/experiments/index.md', 'docs/conjecture-net-explorer.md', 'website/.vitepress/config.mts']) assert((await read(file)).includes(route), file)
  const pointer = JSON.parse(await read('config/public-research-coverage.current.json'))
  assert(JSON.parse(await read(pointer.config)).required_pages.includes(route))
  const text = await guide()
  assert(!/\]\([^)]*conjecture-nets\.html#net=marici\.persistent-seam-pe/.test(text))
  assert(text.includes('No scientific supplier or graph transition'))
})

test('actual public catalog and prepared bundle stay at five, held P/E stays development-only and its public fragment is rejected', async () => {
  const publicCatalog = JSON.parse(await read('src/conjecture-nets/catalog.json'))
  const development = JSON.parse(await read('src/conjecture-nets/development-catalog.json'))
  const snapshot = JSON.parse(await read('website/public/experiments/conjecture-nets.json'))
  assert.equal(publicCatalog.nets.length, 5)
  assert(!publicCatalog.nets.some(net => net.path === held))
  assert(development.nets.some(net => net.path === held))
  assert.deepEqual(snapshot.nets.map(net => net.source), publicCatalog.nets.map(net => net.path))
  const nets = snapshot.nets.map(net => normalizeNet(net.contract, net.source, net.title))
  assert.throws(() => assertBundledNetFragment('net=marici.persistent-seam-pe.v1&node=persistent-seam-pe', nets), /not bundled/)
})

test('deleting a publication-state distinction fails rather than silently treating source presence as approval', async () => {
  const text = await guide()
  requireSelectionBoundary(text)
  for (const phrase of ['five-net public selection', 'commit is not publication approval', 'unresolved source wording']) assert.throws(() => requireSelectionBoundary(text.replaceAll(phrase, '')), /Missing P\/E publication boundary/)
})
