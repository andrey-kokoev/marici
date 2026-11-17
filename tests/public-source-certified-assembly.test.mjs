import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import test from 'node:test'
const read = file => fs.readFile(new URL('../' + file, import.meta.url), 'utf8')
const inventory = JSON.parse(await read('src/data/results-physics.json'))
const slug = 'source-certified-coherent-assembly'
const route = '/research/results/' + slug
function requireEntry(entries = inventory) {
  const found = entries.filter(item => item.slug === slug)
  assert.equal(found.length, 1, 'Missing or duplicate common-witness assembly curation')
  return found[0]
}

test('WG common-witness completion has its own source-reported result, separate from its predecessor', () => {
  const entry = requireEntry()
  assert(entry.status.includes('Source-reported'))
  assert(entry.status.includes('declared certified-input scope'))
  assert.equal(entry.result, null)
  assert.equal(entry.checker, 'research/strominger/checkers/check_source_certified_coherent_assembly.py')
  assert(inventory.find(item => item.slug === 'witness-continuation-admission').details.includes(route))
})

test('completion is the dedicated actual-target assembly, not a count of predecessors or arbitrary native admission', async () => {
  const text = requireEntry().details
  const source = JSON.parse(await read('research/strominger/contracts/source-certified-coherent-assembly.v1.json'))
  assert.equal(source.objective_closed_at_declared_scope, true)
  assert(Object.values(source.scope_guards).every(value => value === false))
  for (const phrase of ['literal input object', 'recursive Origins', 'raw policy presentations', 'Closed', 'compiled-child', 'chosen-tag', 'not inferred from dependency counts', 'not rerun']) assert(text.includes(phrase), phrase)
  for (const phrase of ['arbitrary native inputs', 'unrestricted Body action', 'physical adequacy']) assert(text.includes(phrase), phrase)
})

test('local completion stops the objective while all three distinct downstream branches stay outside it', async () => {
  const net = JSON.parse(await read('research/strominger/contracts/wg-source-determination-conjecture-net.v1.json'))
  assert.equal(net.revision, 27)
  assert.equal(net.nodes.length, 50)
  assert.deepEqual(net.frontier, [])
  assert.equal(net.recommended_start, null)
  const entry = requireEntry()
  assert(entry.details.includes('Do not reopen this local objective'))
  for (const node of net.nodes.filter(node => node.status === 'open')) assert(entry.details.includes(node.id), node.id)
  for (const phrase of ['35 scoped constructions', '11 rejected candidates', 'three separately blocked', 'newly declared stronger contract']) assert(entry.details.includes(phrase), phrase)
})

test('public source links and checker exist; ignored receipts are not advertised as downloads', async () => {
  const entry = requireEntry()
  await fs.access(new URL('../' + entry.checker, import.meta.url))
  const links = [...entry.details.matchAll(/https:\/\/github\.com\/andrey-kokoev\/marici\/blob\/main\/(research\/[^)\s]+)/g)]
  assert(links.length >= 4)
  for (const [, file] of links) await fs.access(new URL('../' + file, import.meta.url))
  assert(entry.details.includes('2,382'))
  assert(entry.details.includes('historical receipt'))
  assert(!/\]\([^)]*\/results\/source-certified-coherent-assembly\//.test(entry.details))
})

test('canonical synthesis, result index, selected coverage and generated page expose the scoped completion', async () => {
  for (const file of ['docs/landing-page.md', 'docs/results-page.md', 'docs/theory-page.md', 'docs/system-characteristics.md', 'website/research/results/index.md']) assert((await read(file)).includes(route), file)
  const page = await read('website/research/results/' + slug + '.md')
  assert(page.includes(requireEntry().details))
  const pointer = JSON.parse(await read('config/public-research-coverage.current.json'))
  const coverage = JSON.parse(await read(pointer.config))
  assert(coverage.required_pages.includes(route))
  const wg = coverage.frontier.find(item => item.id === 'witness-application')
  assert(wg.reported_completed.includes('revision 27'))
  assert(wg.reported_completed.includes('Stop this local objective'))
  assert(wg.first_missing.includes('newly declared stronger contract'))
})

test('old provenance is not silently stretched to cover the new assembly; missing curation is rejected', async () => {
  const old = JSON.parse(await read('config/current-research-provenance.v1.json'))
  assert(!old.entries.some(entry => entry.slug === slug))
  assert(requireEntry().details.includes('not pinned by the historical ten-family v1 snapshot'))
  assert.throws(() => requireEntry([]), /Missing or duplicate/)
})
