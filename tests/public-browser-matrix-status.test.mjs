import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import test from 'node:test'
import { selectBrowserMatrix, browserMatrixResult } from '../scripts/isotope-browser-matrix-contract.mjs'
import { validateBrowserEvidence } from '../scripts/check-isotope-wiring-browser-evidence.mjs'
const manifest = JSON.parse(await fs.readFile(new URL('../config/isotope-wiring-browser-matrix.v1.json', import.meta.url), 'utf8'))
const runsFor = selection => selection.engines.flatMap(engine => selection.cases.map(c => ({ engine, case: c.id, status: 'passed' })))

test('current browser matrix has ten distinct scoped cases and all three engines', () => {
  const selection = selectBrowserMatrix(manifest)
  assert.equal(selection.cases.length, 10)
  assert.equal(runsFor(selection).length, 30)
  assert(manifest.supersession.reason.includes('removed EP controls'))
  assert.equal(browserMatrixResult(manifest, selection, runsFor(selection), true), 'passed')
})

test('selection rejects unknown engines/cases, unsafe paths and empty or duplicated matrices', () => {
  assert.throws(() => selectBrowserMatrix(manifest, ['unknown']), /Unknown browser engine/)
  assert.throws(() => selectBrowserMatrix(manifest, ['--case=missing']), /Unknown browser case/)
  assert.throws(() => selectBrowserMatrix({ ...manifest, cases: [] }), /Empty browser matrix/)
  const unsafe = structuredClone(manifest)
  unsafe.cases[0].script = '../outside.mjs'
  assert.throws(() => selectBrowserMatrix(unsafe), /Unsafe/)
  assert.throws(() => selectBrowserMatrix({ ...manifest, cases: [...manifest.cases, manifest.cases[0]] }), /Duplicate/)
})

test('partial, failed, unrun, duplicate, missing and drifted results cannot be reported as a full pass', () => {
  const full = selectBrowserMatrix(manifest)
  const partial = selectBrowserMatrix(manifest, ['chromium', '--case=network-isolation'])
  assert.equal(browserMatrixResult(manifest, partial, runsFor(partial), true), 'partial_pass')
  const runs = runsFor(full)
  for (const status of ['failed', 'not_run']) assert.equal(browserMatrixResult(manifest, full, [{ ...runs[0], status }, ...runs.slice(1)], true), 'failed')
  assert.equal(browserMatrixResult(manifest, full, runs.slice(1), true), 'failed')
  assert.equal(browserMatrixResult(manifest, full, [...runs, runs[0]], true), 'failed')
  assert.equal(browserMatrixResult(manifest, full, runs, false), 'invalidated')
})

test('recorded evidence covers every engine/case with versions and source identities, not an inflated or partial pass', async () => {
  const evidence = JSON.parse(await fs.readFile(new URL('../config/isotope-wiring-browser-evidence.v1.json', import.meta.url), 'utf8'))
  assert.equal(validateBrowserEvidence(evidence, manifest), 30)
  const missing = structuredClone(evidence)
  missing.runs.pop()
  assert.throws(() => validateBrowserEvidence(missing, manifest))
  const version = structuredClone(evidence)
  version.runs[0].engine_version = 'not-the-tested-engine'
  assert.throws(() => validateBrowserEvidence(version, manifest))
  const identity = structuredClone(evidence)
  delete identity.source_sha256['examples/isotope-wiring/index.html']
  assert.throws(() => validateBrowserEvidence(identity, manifest), /Missing tested source/)
})
