import assert from 'node:assert/strict'
import { access, readFile } from 'node:fs/promises'
import test from 'node:test'

const read = path => readFile(new URL(`../${path}`, import.meta.url), 'utf8')
const route = '/research/predictions/pb208-coherence-capacity'
const card = await read('website/research/predictions/pb208-coherence-capacity.md').catch(error => {
  if (error.code === 'ENOENT') return ''
  throw error
})
const landing = await read('docs/landing-page.md')
const home = await read('website/index.md')
const predictions = await read('website/research/predictions/index.md')
const results = await read('docs/results-page.md')
const publicResults = await read('website/research/results/index.md')
const inventory = JSON.parse(await read('src/data/results-physics.json'))

test('dated capacity card is explicitly a stable-only conjecture, not a verified prediction', () => {
  for (const phrase of ['October 25, 2026', 'operator proposal', 'stable nuclei', 'not a derived nuclear stability result', 'heavier unstable nuclei', 'not a physical-time']) assert(card.includes(phrase), phrase)
  assert(card.includes('4332'))
})

test('all missing capacity maps remain explicit rather than following from arithmetic', () => {
  for (const phrase of ['ninth independent contribution', 'independent binary alternatives', 'extraction and reconstruction', 'fixed-point-free involution', 'neutron readout', 'not derive 82 protons', 'not 256 independent', 'three independent positional']) assert(card.includes(phrase), phrase)
})

test('rivals preserve the stable-neighbor discriminator and reject routing-count promotion', () => {
  for (const phrase of ['Bi-209', '126 neutrons', '198', 'not independent evidence', 'decay threshold', 'not rerun']) assert(card.includes(phrase), phrase)
  assert(card.includes('not a checker for the capacity conjecture'))
})

test('comparison targets, homepage and results discover the conjecture without verified-result admission', () => {
  for (const text of [landing, home, predictions, results, publicResults]) assert(text.includes(route), 'Missing conjecture card entrypoint')
  const start = landing.indexOf('## Predictions')
  const end = landing.indexOf('**Construction and formalizations**', start)
  assert(landing.slice(start, end).includes(route), 'Place the card inside the canonical predictions extraction')
  assert(!inventory.some(item => item.slug === 'pb208-coherence-capacity'), 'Do not install the conjecture as a verified result')
})

test('conjecture sources and the separately scoped routing countertest exist', async () => {
  const sources = [...card.matchAll(/https:\/\/github\.com\/andrey-kokoev\/marici\/blob\/main\/([^)\s]+)/g)]
  assert(sources.length >= 2)
  for (const [, path] of sources) await access(new URL(`../${path}`, import.meta.url))
  assert(card.includes('scripts/falsify-n-routing-conjecture.mjs'))
  await access(new URL('../scripts/falsify-n-routing-conjecture.mjs', import.meta.url))
})
