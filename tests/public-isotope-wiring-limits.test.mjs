import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import test from 'node:test'

const read = path => readFile(new URL(`../${path}`, import.meta.url), 'utf8')
const host = await read('website/experiments/isotope-wiring.md')
const limits = await read('website/experiments/isotope-wiring-limitations.md').catch(error => {
  if (error.code === 'ENOENT') return ''
  throw error
})
const wrapper = await read('website/.vitepress/components/IsotopeWiring.vue')
const editor = await read('examples/isotope-wiring/index.html')

test('host surfaces validation/export limitations before the embedded editor', () => {
  const link = host.indexOf('/experiments/isotope-wiring-limitations')
  assert(link >= 0, 'Missing editor limitations link')
  assert(link < host.indexOf('<ClientOnly>'))
  assert(limits.includes('/experiments/isotope-wiring'))
})

test('legacy failures are described as unresolved, not hidden by a passing graph check', () => {
  for (const phrase of ['identity delta', 'base-only metadata', '(1,10)', '(11,0)', 'mutable base', 'graph projection', 'TODO failures are not passes']) assert(limits.includes(phrase), phrase)
  assert(limits.includes('absolute definitions'))
})

test('independent machinery milestones are not advertised as integrated editor functionality', () => {
  for (const phrase of ['not connected to the visualization', 'pending local development', 'finite-incidence', 'attributed adapter', 'model predicates', 'ground rewrites', 'before-image', 'selective evidence transport', 'not a formal proof']) assert(limits.includes(phrase), phrase)
  assert.match(wrapper, /isotope-wiring\/index\.html\?raw/)
  assert.doesNotMatch(editor, /(?:finite-diagrams|legacy-adapter|model-predicates|revisions)\.mjs/)
})

test('software validation is kept distinct from model completion and physical acceptance', () => {
  for (const phrase of ['supplied targets', 'not derived', 'not composition-closed', 'unresolved placement', 'isotope stability', 'not a certified persistence']) assert(limits.includes(phrase), phrase)
})

test('pending machinery paths are not broken published-source hyperlinks', () => {
  assert(!/\]\([^)]*(?:MACHINERY\.md|core\/(?:CLOSURE|ADAPTER|MODEL|REVISIONS)\.md)/.test(limits))
  assert(limits.includes('may be absent from a clean checkout'))
  assert(limits.includes('examples/isotope-wiring/index.html'))
})
