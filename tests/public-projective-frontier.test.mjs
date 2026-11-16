import assert from 'node:assert/strict'
import { access, readFile } from 'node:fs/promises'
import test from 'node:test'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'

const read = path => readFile(new URL(`../${path}`, import.meta.url), 'utf8')
const route = '/research/programs/ads-ds-projective-frontier'
const page = await read('website/research/programs/ads-ds-projective-frontier.md').catch(error => {
  if (error.code === 'ENOENT') return ''
  throw error
})
const theory = await read('docs/theory-page.md')
const publicTheory = await read('website/research/theory/index.md')
const results = await read('docs/results-page.md')
const publicResults = await read('website/research/results/index.md')
const config = await read('website/.vitepress/config.mts')
const md = await createMarkdownRenderer(fileURLToPath(new URL('../', import.meta.url)))

test('projective programme card has an explicit cutoff and separates retained input from erased output', () => {
  for (const phrase of ['October 20, 2026', 'eighteen', 'nine rank-one', 'ambient linear-packet', 'retains the original points', 'not native continuation closure', 'not geometric emergence']) assert(page.includes(phrase), phrase)
  assert(page.includes('bare compiler record'))
  assert(page.includes('real ordered endpoint'))
})

test('frontier does not turn a failed metric selector or snapshot recommendation into a theorem', () => {
  for (const phrase of ['C=4', 'C=16', 'dual-shadow-transport-audit', 'snapshot', 'common R', 'one-step', 'two-step', 'visibility', 'forgetfulness', 'not rerun']) assert(page.includes(phrase), phrase)
  assert(page.includes('No unique scale or privileged shadow'))
  assert(page.includes('stop at the audit'))
})

test('source packets and recorded checker paths exist without rerunning suppliers', async () => {
  const sources = [...page.matchAll(/https:\/\/github\.com\/andrey-kokoev\/marici\/blob\/main\/(research\/[^)\s]+)/g)]
  assert(sources.length >= 5)
  for (const [, path] of sources) await access(new URL(`../${path}`, import.meta.url))
  for (const checker of ['check_source_projective_bridge.py', 'check_retained_projective_correspondence.py', 'check_projective_interval_metric_selection.py', 'check_ads_ds_workbench.py']) {
    assert(page.includes(checker), checker)
    await access(new URL(`../research/nima/checkers/${checker}`, import.meta.url))
  }
})

test('canonical and generated synthesis and navigation expose the dated programme', () => {
  for (const text of [theory, publicTheory, results, publicResults, config]) assert(text.includes(route), 'Missing projective programme link')
  const id = 'retained-projective-frontier'
  assert(config.includes(`/research/theory/#${id}`))
  for (const text of [theory, publicTheory]) assert(md.render(text).includes(`id="${id}"`))
  assert(results.includes('240,000 trials'))
  assert(results.includes('does not derive AdS/dS geometry'))
})
