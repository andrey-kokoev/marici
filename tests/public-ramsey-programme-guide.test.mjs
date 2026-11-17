import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import test from 'node:test'
const read = path => fs.readFile(new URL('../' + path, import.meta.url), 'utf8')
const route = '/research/programs/ramsey-mathematical-programme-2026-11'
const guidePath = 'website' + route + '.md'
const guide = () => read(guidePath)
const sources = [
  'ramsey_matrix_generator_current_position_2026-11-08.md',
  'reflected_simplex_coherence_consolidated_2026-11-09.md',
  'minimum_dimension_phase_rigidity_2026-11-10.md',
  'heptagon-normal-form-theorem.md',
  'neighborhood_stability_at_twenty_three.md',
]
function requireBoundaries(text) {
  for (const phrase of ['no general Ramsey formula', 'unrestricted n = 4 remains open', 'simultaneous-stability step remains missing', 'not independently verified', 'exactly 22 vertices']) assert(text.includes(phrase), 'Missing programme boundary: ' + phrase)
}

test('dated imported-note guide distinguishes reported results, certificates, counterexamples and open claims', async () => {
  const text = await guide()
  requireBoundaries(text)
  for (const phrase of ['Editorial snapshot: 2026-11-17', 'source-note dates', 'Source-reported written results', 'Conditional finite certificates', 'Counterexamples', 'Open claims', 'not rerun']) assert(text.includes(phrase), phrase)
  assert(!text.includes('\\boxed'))
})

test('all five selected source links resolve and source import is not verification or novelty evidence', async () => {
  const text = await guide()
  for (const source of sources) {
    assert(text.includes('/research/chatgpt/ramsey/' + source), source)
    await fs.access(new URL('../research/chatgpt/ramsey/' + source, import.meta.url))
  }
  for (const phrase of ['commit is not proof', 'no priority or novelty claim', 'not pinned by the historical ten-family v1 snapshot']) assert(text.includes(phrase), phrase)
})

test('matrix transport and reflected-simplex models do not become universal graph constructors or native fillers', async () => {
  const text = await guide()
  for (const phrase of ['lower-bound witnesses', 'K_{2,3}', 'two of twenty', 'a^{-2}', 'a^2=1', 'cycles, not supplied filled faces', 'incidence-to-edge-colouring']) assert(text.includes(phrase), phrase)
})

test('rigidity separates the n=3 proof, n=2 counterexample and translation-invariant theorem from unrestricted n=4', async () => {
  const text = await guide()
  for (const phrase of ['n = 3', '64', 'eight-dimensional', 'n = 2', 'translation-invariant', '1,024', 'positive semidefinite', 'rank sixteen', 'not arbitrary graph signings']) assert(text.includes(phrase), phrase)
})

test('heptagon certificate retains all three hypotheses and the finite trust boundary', async () => {
  const text = await guide()
  for (const phrase of ['no triangle', 'no independent seven-set', 'induced seven-cycle', 'even number of neighbours', '6-regular', 'binary adjacency rank 16', 'eight-qubit', 'two isomorphism classes', 'DRAT', 'not a proof-assistant formalization', 'not the unrestricted Ramsey upper bound']) assert(text.includes(phrase), phrase)
})

test('one-root stability bound is not all-root exclusion; missing reproduction helpers are not linked as files', async () => {
  const text = await guide()
  for (const phrase of ['one three-stable root', 'at most 23', 'independence number seven', 'rank-four', 'rank-one', 'every root', 'not a counterexample to the classical Ramsey value']) assert(text.includes(phrase), phrase)
  for (const name of ['check_pairwise_rigidity_base.py', 'check_circulant_reduction.py', 'verify_neighborhood_stability.py']) {
    assert(text.includes(name))
    assert(!text.includes('blob/main/research/chatgpt/ramsey/' + name))
    await assert.rejects(fs.access(new URL('../research/chatgpt/ramsey/' + name, import.meta.url)), { code: 'ENOENT' })
  }
  assert(text.includes('not found in the reviewed tree'))
})

test('canonical/generated entrypoints and selected coverage expose the guide; deleting qualifications fails', async () => {
  const text = await guide()
  for (const file of ['docs/results-page.md', 'docs/theory-page.md', 'website/research/results/index.md', 'website/research/theory/index.md', 'website/.vitepress/config.mts']) assert((await read(file)).includes(route), file)
  const pointer = JSON.parse(await read('config/public-research-coverage.current.json'))
  const coverage = JSON.parse(await read(pointer.config))
  assert(coverage.required_pages.includes(route))
  requireBoundaries(text)
  for (const phrase of ['no general Ramsey formula', 'unrestricted n = 4 remains open', 'simultaneous-stability step remains missing', 'exactly 22 vertices']) assert.throws(() => requireBoundaries(text.replaceAll(phrase, '')), /Missing programme boundary/)
})
