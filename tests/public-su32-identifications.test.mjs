import assert from 'node:assert/strict'
import { access, readFile } from 'node:fs/promises'
import test from 'node:test'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'

const read = path => readFile(new URL(`../${path}`, import.meta.url), 'utf8')
const inventory = JSON.parse(await read('src/data/results-physics.json'))
const results = await read('docs/results-page.md')
const publicResults = await read('website/research/results/index.md')
const theory = await read('docs/theory-page.md')
const publicTheory = await read('website/research/theory/index.md')
const config = await read('website/.vitepress/config.mts')
const slug = 'su32-comparison-content-and-operations'
const route = `/research/results/${slug}`
const md = await createMarkdownRenderer(fileURLToPath(new URL('../', import.meta.url)))

function entry() {
  const matches = inventory.filter(item => item.slug === slug)
  assert.equal(matches.length, 1, 'Missing unified SU32 identification result')
  return matches[0]
}

function explanation(text) {
  const title = '### Comparison actions and operation-valued boundaries'
  const start = text.indexOf(title)
  assert(start >= 0, 'Missing theory distinction between action, content and operation')
  const suffix = text.slice(start + title.length)
  const next = /\n#{1,3} /.exec(suffix)
  return text.slice(start, next ? start + title.length + next.index : undefined).trim()
}

test('SU32 symmetry explicitly transports preparations and outgoing edges, not only endpoints', () => {
  const text = entry().details
  for (const phrase of ['24 coordinate permutations', '104 oriented interfaces', 'same-preparation reconciliation', 'P+ and P-', 'two of four', 'outgoing edge', 'nativeSu32ComparisonCompiled: false']) assert(text.includes(phrase), phrase)
})

test('static-content exclusion states the conjunction, finite-rank obstruction and surviving control', () => {
  const text = entry().details
  for (const phrase of ['80 named fibres', 'finite JSON', 'paired P/E', 'reference reader', 'literal fibre content', '48 of 136', 'strict subtree', '544', 'not every content-bearing fibration']) assert(text.includes(phrase), phrase)
  assert(results.includes('Static fibre content equals its full comparison packet'))
})

test('operation-valued successor retains finite scope and its missing native interpretation', () => {
  const text = entry().details
  for (const phrase of ['448 motifs', 'two internal shared-face', 'five external ports', 'adding retained edges', 'contraction', 'eight local cyclic orientations', 'native boundary-corolla', 'not a full', 'five-step physical period']) assert(text.includes(phrase), phrase)
})

test('publication sources, bounded checkers and generated result are present without ignored downloads', async () => {
  const item = entry()
  assert.equal(item.result, null)
  assert.match(item.details, /not rerun/)
  for (const checker of item.checker.split('; ')) await access(new URL(`../${checker}`, import.meta.url))
  const sources = [...item.details.matchAll(/https:\/\/github\.com\/andrey-kokoev\/marici\/blob\/main\/(research\/[^)\s]+)/g)]
  assert.equal(sources.length, 3)
  for (const [, source] of sources) await access(new URL(`../${source}`, import.meta.url))
  const generated = await read(`website/research/results/${slug}.md`)
  assert(generated.includes(item.details))
  assert(generated.includes(`**${item.status}**`))
})

test('result index, theory explanation and sidebar expose the distinctions', () => {
  for (const text of [results, publicResults]) assert(text.includes(route))
  const source = explanation(theory)
  assert(source.includes(route))
  assert.equal(explanation(publicTheory), source)
  const id = 'comparison-actions-and-operation-valued-boundaries'
  assert(config.includes(`/research/theory/#${id}`))
  for (const text of [theory, publicTheory]) assert(md.render(text).includes(`id="${id}"`))
})
