import assert from 'node:assert/strict'
import { access, readFile } from 'node:fs/promises'
import test from 'node:test'

const read = path => readFile(new URL(`../${path}`, import.meta.url), 'utf8')
const inventory = JSON.parse(await read('src/data/results-physics.json'))
const index = await read('docs/results-page.md')
const publishedIndex = await read('website/research/results/index.md')
const architecture = await read('docs/system-characteristics.md')
const publicArchitecture = await read('website/research/system-characteristics/index.md')
const programme = await read('website/research/programs/nima-amplitudes.md')
const slugs = ['analytical-native-two-route-pilot', 'conditional-optical-control-integration', 'local-contour-covariance-closure', 'atom-retained-source-transport']
function entry(slug) {
  const matches = inventory.filter(item => item.slug === slug)
  assert.equal(matches.length, 1, `Missing cross-sector curation: ${slug}`)
  return matches[0]
}

test('analytical pilot distinguishes native success, negative analytical residual and absent witness', () => {
  const text = entry(slugs[0]).details
  for (const phrase of ['46 checks', 'strictly negative', 'zero native', 'H=null', 'not an obstruction modulo corrections', 'observation loss']) assert(text.includes(phrase), phrase)
})

test('optical control remains conditional, statistically typed and unapplied at the shared boundary', () => {
  const text = entry(slugs[1]).details
  for (const phrase of ['UNAPPLIED', 'formal outcomes remain null', 'abstain', 'exact nondisturbing', 'MissingIndependentApparatusEvidence', 'operator reopening', 'not elapsed time']) assert(text.includes(phrase), phrase)
})

test('local contour closure preserves unavailable data and absent physical selection', () => {
  const text = entry(slugs[2]).details
  for (const phrase of ['ten local', 'unavailable, not zero', 'physical contour is not', 'full integral cycle', 'global weighted gates remain open']) assert(text.includes(phrase), phrase)
  assert(programme.includes('research cutoff 2026-09-18'))
  assert(programme.includes('## Frontier at the cutoff'))
  assert(programme.includes(`/research/results/${slugs[2]}`))
})

test('atom transport preserves source charts/history and does not identify a physical gauge group', () => {
  const text = entry(slugs[3]).details
  for (const phrase of ['56 certificate routes', '271 route splits', 'S5', 'S4', '137-record T9', 'not a newly compiled Agda', 'not a physical gauge group', 'outside-context']) assert(text.includes(phrase), phrase)
  for (const page of [architecture, publicArchitecture]) {
    assert(page.includes('### Concrete atom-route transport'))
    assert(page.includes(`/research/results/${slugs[3]}`))
  }
})

test('four results are source-linked, reproducible as publication, and discoverable', async () => {
  for (const slug of slugs) {
    const item = entry(slug)
    for (const heading of ['Reported result', 'Controls and exclusions', 'First unresolved obligation', 'Verification and sources']) assert(item.details.includes(`## ${heading}`), `${slug}: ${heading}`)
    assert.match(item.details, /not rerun|not replayed/)
    assert.equal(item.result, null)
    for (const checker of item.checker.split('; ')) await access(new URL(`../${checker}`, import.meta.url))
    const links = [...item.details.matchAll(/https:\/\/github\.com\/andrey-kokoev\/marici\/blob\/main\/(research\/[^)\s]+)/g)]
    assert(links.length)
    for (const [, source] of links) await access(new URL(`../${source}`, import.meta.url))
    const page = await read(`website/research/results/${slug}.md`)
    assert(page.includes(item.details))
    for (const text of [index, publishedIndex]) assert(text.includes(`/research/results/${slug}`), slug)
  }
})

test('an absent cross-sector record cannot satisfy coverage', () => {
  assert.throws(() => entry('not-an-admitted-cross-sector-result'), /Missing cross-sector curation/)
})
