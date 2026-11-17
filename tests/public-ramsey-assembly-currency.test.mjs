import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import test from 'node:test'
const read = path => fs.readFile(new URL('../' + path, import.meta.url), 'utf8')
const inventory = JSON.parse(await read('src/data/results-physics.json'))
const net = JSON.parse(await read('research/voevodsky/contracts/ramsey-tetrahedral-octahedral-conjecture-net.v1.json'))
const slug = 'ramsey-retained-assembly-coherence'
const route = '/research/results/' + slug
function entry(entries = inventory) {
  const found = entries.filter(item => item.slug === slug)
  assert.equal(found.length, 1, 'Missing or duplicate revision-32 Ramsey curation')
  return found[0]
}

test('Ramsey successor is distinct from the 24-case repair and distinguishes local revision from graph admission', () => {
  const result = entry()
  assert.equal(net.revision, 32)
  assert.equal(net.local_update.latest_admitted_revision, 19)
  assert.equal(net.local_update.new_graph_event, null)
  for (const phrase of ['local revision 32', 'graph admission remains revision 19', '24-case reader repair']) assert(result.details.includes(phrase), phrase)
  assert(inventory.find(item => item.slug === 'ramsey-history-covariant-readers').details.includes(route))
  assert.equal(result.result, null)
})

test('native four-facet and higher overlaps retain their explicit input and derivation-comparison boundaries', () => {
  const text = entry().details
  for (const phrase of ['validated full-port input policy', '12 directed edge selections', '24 vertex triple compositions', '72 different-edge restriction cells', '24 full middle', 'common-edge triples', 'different-edge', 'NativeComparison', 'unselected prerequisites', 'not native proof equality']) assert(text.includes(phrase), phrase)
})

test('written arbitrary-assembly proof retains its source-to-global argument and is not mislabeled kernel certification', () => {
  const result = entry()
  const claim = net.nodes.find(node => node.id === 'theorem-candidate-arbitrary-assembly-coherence')
  assert.equal(claim.scope_guards.unbounded_source_graph_coherence, true)
  for (const key of ['formal_kernel_certificate', 'independent_source_selection', 'unchanged_forward_native_admission', 'parent_resolved']) assert.equal(claim.scope_guards[key], false, key)
  for (const phrase of ['exact-integer', '96-state', '160-transition', 'translation naturality', 'anchor displacement', '(0,1,1,0)', 'all 44', 'written mathematical proof', 'not a new Agda/Rzk/Lean kernel certificate', 'not merely the 14- or 66-packet samples']) assert(result.details.includes(phrase), phrase)
})

test('corrected selector and whole-boundary reversal preserve distinct policy, carrier and finiteness limits', () => {
  const text = entry().details
  for (const phrase of ['M1,C1,C2', '2,1,3', 'M0,M2', 'unchanged-N-selector', 'finite complete entry/exit certificate', 'common reflection center K', 'infinite', 'overflowing JavaScript Number', 'not a new forward E operation', '36-coordinate P', '8-coordinate E']) assert(text.includes(phrase), phrase)
})

test('current source-selection and negative-direction gates are named without recreating completed candidate coherence', () => {
  const text = entry().details
  for (const id of ['joint44-native-source-selection', 'negative-direction-policy-native-descent']) {
    assert.equal(net.nodes.find(node => node.id === id).status, 'open_candidate')
    assert(text.includes(id), id)
  }
  for (const phrase of ['Do not repeat bounded cocycle searches', 'independent geometric-face', 'native forcing', 'physical dynamics', 'not rerun for publication']) assert(text.includes(phrase), phrase)
})

test('canonical and generated discovery, source/checker paths and current selected coverage include the successor', async () => {
  const result = entry()
  for (const file of ['docs/landing-page.md', 'docs/results-page.md', 'docs/theory-page.md', 'docs/system-characteristics.md', 'website/research/results/index.md']) assert((await read(file)).includes(route), file)
  assert((await read('website/research/results/' + slug + '.md')).includes(result.details))
  for (const checker of result.checker.split('; ')) await fs.access(new URL('../' + checker, import.meta.url))
  const links = [...result.details.matchAll(/https:\/\/github\.com\/andrey-kokoev\/marici\/blob\/main\/(research\/[^)\s]+)/g)]
  assert(links.length >= 5)
  for (const [, source] of links) await fs.access(new URL('../' + source, import.meta.url))
  const pointer = JSON.parse(await read('config/public-research-coverage.current.json'))
  const config = JSON.parse(await read(pointer.config))
  assert(config.required_pages.includes(route))
  const frontier = config.frontier.find(item => item.id === 'ramsey-descent')
  assert(frontier.reported_completed.includes(route))
  assert(frontier.reported_completed.includes('written'))
  for (const id of ['joint44-native-source-selection', 'negative-direction-policy-native-descent']) assert(frontier.first_missing.includes(id), id)
})

test('historical v1 provenance is not stretched and absent successor curation fails', async () => {
  const old = JSON.parse(await read('config/current-research-provenance.v1.json'))
  assert(!old.entries.some(item => item.slug === slug))
  assert(entry().details.includes('not pinned by the historical ten-family v1 snapshot'))
  assert(!/\]\([^)]*\/results\/ramsey-/.test(entry().details))
  assert.throws(() => entry([]), /Missing or duplicate/)
})
