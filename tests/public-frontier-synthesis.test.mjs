import assert from 'node:assert/strict'
import { access, readFile } from 'node:fs/promises'
import test from 'node:test'

const read = path => readFile(new URL(`../${path}`, import.meta.url), 'utf8')
const canonical = await read('docs/landing-page.md')
const published = await read('website/index.md')
const heading = '## Current research frontier: October 2026'
const sources = [
  'research/nima/ADS-DS-WORKBENCH.md',
  'research/voevodsky/witness-generator-coherence-v1.md',
  'research/grothendieck/retained-pair-fails-complete-comparison-at-carrier-equivalence.md',
  'research/strominger/su32-record-reader-classification-v1.md',
  'research/strominger/su32-release-source-audit-v1.md',
  'research/voevodsky/ramsey-covariant-EP-reader-v1.md',
  'research/strominger/coherent-four-return-v1.md',
  'research/realization-tower/cellulation-shell-exhaustive-verification.md',
  'research/strominger/cellulation-dot-422-compatibility.md',
]

function frontier(text) {
  const start = text.indexOf(heading)
  assert(start >= 0, 'Missing dated current frontier')
  const end = text.indexOf('\n## ', start + heading.length)
  return text.slice(start, end < 0 ? undefined : end).trim()
}

function checkCoverage(section) {
  for (const source of sources) assert(section.includes(source), `Missing frontier source: ${source}`)
}

test('homepage leads dated research coverage with source-linked results and counterexamples', async () => {
  const section = frontier(canonical)
  checkCoverage(section)
  assert(canonical.indexOf(heading) < canonical.indexOf('## October 18:'))
  assert.equal((section.match(/^\| (?!Track|---)/gm) || []).length, 7)
  for (const source of sources) await access(new URL(`../${source}`, import.meta.url))
})

test('frontier coverage check rejects an omitted research source', () => {
  assert.throws(() => checkCoverage(''), /Missing frontier source/)
})

test('frontier retains the tested models and the unresolved physical/source boundaries', () => {
  const section = frontier(canonical)
  assert.match(section, /source reports.*not a fresh verification/s)
  assert.match(section, /not arbitrary native admission/)
  assert.match(section, /original release.*unbound/)
  assert.match(section, /compressed.*history/)
  assert.match(section, /may be empty/)
  assert.match(section, /weaker model/)
  assert.match(section, /0 of 30/)
  assert.match(section, /blocked, not repaired/)
})

test('public homepage reproduces the canonical current frontier', () => {
  assert.equal(frontier(published), frontier(canonical), 'Regenerate website/index.md from docs/landing-page.md')
})
