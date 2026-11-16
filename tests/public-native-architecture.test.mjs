import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import test from 'node:test'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'

const read = path => readFile(new URL(`../${path}`, import.meta.url), 'utf8')
const theory = await read('docs/theory-page.md')
const publicTheory = await read('website/research/theory/index.md')
const architecture = await read('docs/system-characteristics.md')
const publicArchitecture = await read('website/research/system-characteristics/index.md')
const config = await read('website/.vitepress/config.mts')
const md = await createMarkdownRenderer(fileURLToPath(new URL('../', import.meta.url)))
const headings = {
  continuation: 'Source-relative continuation and higher admission',
  joins: 'Native joins and complete-record comparisons',
  returns: 'Coherent dependent four-return',
  contracts: 'Native continuation and comparison contracts',
}

function section(text, title) {
  const heading = `### ${title}`
  const start = text.indexOf(heading)
  assert(start >= 0, `Missing explanation: ${title}`)
  const suffix = text.slice(start + heading.length)
  const next = /\n#{1,3} /.exec(suffix)
  return text.slice(start, next ? start + heading.length + next.index : undefined).trim()
}

function hasHeading(text, id) {
  const html = md.render(text)
  assert(html.includes(`id="${id}"`), `Missing rendered heading: ${id}`)
}

test('theory explains native continuation without universalizing its admission domain', () => {
  const text = section(theory, headings.continuation)
  for (const term of ['source-relative', 'atomic', 'E-envelope', 'reader', 'not arbitrary native admission', 'not inverse execution']) assert(text.includes(term), term)
  assert(text.includes('/research/results/witness-continuation-admission'))
})

test('join explanation distinguishes original operands, current-value uniqueness and retained histories', () => {
  const text = section(theory, headings.joins)
  for (const term of ['both operand derivations', 'compatibility witness', 'not an equivalence of the original operands', 'Boolean', 'contractible', 'producer histories', 'physical reader']) assert(text.includes(term), term)
  assert(text.includes('/research/results/su32-native-record-comparisons'))
})

test('dependent return is distinct from periodic-state generation and operational complex return', () => {
  const text = section(theory, headings.returns)
  for (const term of ['supplied successor', 'classifying space', 'may be empty', 'shift-four', 'physical time', 'operational complex']) assert(text.includes(term), term)
  assert(text.includes('/research/results/coherent-dependent-four-return'))
  assert(theory.includes('Operational complex/tensor whole-return assembly is still the unresolved goal'))
})

test('architecture contracts name supplied inputs, retained outputs and nonpromotions', () => {
  const text = section(architecture, headings.contracts)
  for (const term of ['Supplied inputs', 'Retained output', 'Not supplied', 'source families', 'selected-value agreement', 'four-record reader', 'producer programs', 'may be empty']) assert(text.includes(term), term)
  for (const slug of ['witness-continuation-admission', 'su32-native-record-comparisons', 'coherent-dependent-four-return']) assert(text.includes(`/research/results/${slug}`), slug)
})

test('new theory/architecture sections reproduce exactly in generated pages', () => {
  for (const key of ['continuation', 'joins', 'returns']) assert.equal(section(publicTheory, headings[key]), section(theory, headings[key]))
  assert.equal(section(publicArchitecture, headings.contracts), section(architecture, headings.contracts))
})

test('new sidebar fragments resolve through the VitePress renderer', () => {
  const targets = [
    ['theory', 'source-relative-continuation-and-higher-admission', theory, publicTheory],
    ['theory', 'native-joins-and-complete-record-comparisons', theory, publicTheory],
    ['theory', 'coherent-dependent-four-return', theory, publicTheory],
    ['system-characteristics', 'native-continuation-and-comparison-contracts', architecture, publicArchitecture],
  ]
  for (const [route, id, source, page] of targets) {
    assert(config.includes(`/research/${route}/#${id}`), id)
    hasHeading(source, id)
    hasHeading(page, id)
  }
  assert.throws(() => hasHeading(theory, 'not-a-native-theorem-heading'), /Missing rendered heading/)
})
