import assert from 'node:assert/strict'
import { access, readFile } from 'node:fs/promises'
import test from 'node:test'

const read = path => readFile(new URL(`../${path}`, import.meta.url), 'utf8')
const guide = await read('website/experiments/construction-workbench.md')
const gallery = await read('website/experiments/index.md')
const belt = await read('website/experiments/native-belt-guide.md')
const results = await read('docs/results-page.md')
const config = await read('website/.vitepress/config.mts')

test('workbench directory is discoverable and uses supported control selection rather than invented presets', () => {
  for (const text of [gallery, belt, config]) assert(text.includes('/experiments/construction-workbench'))
  for (const label of ['Be-8', 'Be-9', 'Retained expansion', 'Cellulation', 'NNPE composition', 'Hex strands', 'Channels / cutaway']) assert(guide.includes(label), label)
  assert(guide.includes('Construction process'))
  assert(guide.includes('retains settings'))
  const presets = [...guide.matchAll(/preset=([^)\s]+)/g)].map(match => match[1])
  assert.deepEqual(presets, ['native-belt'])
})

test('beryllium guide distinguishes slot return, stable identities, sleeve passages and display lanes', () => {
  for (const phrase of ['eight complete routes', 'Four passes restore every slot', 'slot-routing law', 'endpoint permutation stay unchanged', 'edge–strand incidence', 'drawing offsets', 'binding energy, lifetime or isotope-stability']) assert(guide.includes(phrase), phrase)
})

test('NNPE guide does not identify assigned inventory with changing attachment ports', () => {
  for (const phrase of ['assigned inventory N:1/P:1', '16N/16P', 'occupied ports', 'loop-producing joins', 'fifteen joins and eighteen external ports', 'retained binary history']) assert(guide.includes(phrase), phrase)
})

test('sulfur guide and results preserve one-step calibration and global-wiring limits', () => {
  for (const phrase of ['16/16', '768', 'leave-one-carrier-out', 'not independent experimental validation', 'without using target wiring as a lookup']) assert(guide.includes(phrase), phrase)
  assert(results.includes('/experiments/construction-workbench#sulfur-local-continuation-what-was-predicted'))
  assert(guide.includes('not rerun'))
})

test('gallery separates WebGL, local serving, CDN dependencies and static fallbacks', () => {
  for (const phrase of ['## Runtime requirements', 'local HTTP', 'external Three.js CDN', 'SVG/static fallback', 'pinned JSON', 'same-site']) assert(gallery.includes(phrase), phrase)
  assert(!gallery.includes('The newer workbenches also require network access'))
})

test('workbench provenance links point to existing research sources', async () => {
  const links = [...guide.matchAll(/https:\/\/github\.com\/andrey-kokoev\/marici\/blob\/main\/(research\/[^)\s]+)/g)]
  assert.equal(links.length, 4)
  for (const [, path] of links) await access(new URL(`../${path}`, import.meta.url))
})
