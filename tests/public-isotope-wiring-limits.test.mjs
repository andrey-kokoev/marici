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

test('repaired legacy cases remain distinct from unresolved whole-definition persistence guarantees', () => {
  for (const phrase of ['identity delta', 'remove-metadata', 'shell sizes 1–20', 'mutable base', 'Graph records replay checked', '14 passing checks with no TODOs']) assert(limits.includes(phrase), phrase)
  assert(limits.includes('absolute definitions'))
})

test('embedded structural checks are not advertised as full revision machinery or physical acceptance', () => {
  for (const phrase of ['same embedded structural adapter', 'pending local development', 'finite-incidence', 'attributed adapter', 'core/model-predicates.mjs', 'ground rewrites', 'before-image', 'selective evidence transport', 'not a formal proof', 'Browser autosave and legacy delta compilation do not use this revision engine']) assert(limits.includes(phrase), phrase)
  assert.match(wrapper, /isotope-wiring\/index\.html\?raw/)
  assert(editor.includes('<!-- isotope-research-core:start -->'))
  assert(editor.includes('IsotopeWiringResearch'))
  assert.doesNotMatch(editor, /(?:import|src=)[^\n]*(?:model-predicates|revisions)\.mjs/)
})

test('software validation is kept distinct from model completion and physical acceptance', () => {
  for (const phrase of ['supplied targets', 'not derived', 'not composition-closed', 'unresolved placement', 'isotope stability', 'not a certified persistence']) assert(limits.includes(phrase), phrase)
})

test('pending machinery paths are not broken published-source hyperlinks', () => {
  assert(!/\]\([^)]*(?:MACHINERY\.md|core\/(?:CLOSURE|ADAPTER|MODEL|REVISIONS)\.md)/.test(limits))
  assert(limits.includes('may be absent from a clean checkout'))
  assert(limits.includes('examples/isotope-wiring/index.html'))
})
