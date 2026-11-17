import test from 'node:test'
import assert from 'node:assert/strict'
import fs from 'node:fs/promises'
import os from 'node:os'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { assessResearchCurrency, checkResearchCurrency, observeResearchMarkdown, canonicalJSON, sha256, baselineFile, dispositionsFile } from '../scripts/research-currency.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))
const baseline = JSON.parse(await fs.readFile(path.join(root, baselineFile), 'utf8'))
const queue = JSON.parse(await fs.readFile(path.join(root, dispositionsFile), 'utf8'))
const copy = value => structuredClone(value)
const unknown = { path: 'research/fixture/new-source.md', text_sha256: sha256('# New unreviewed source\n') }
const subsequent = (item, change, text_sha256) => ({ path: item.path, change, text_sha256, group: 'finite',
  reviewed_revision: baseline.baseline_commit, disposition: 'pending-source-review', coverage: [],
  rationale: 'Explicit editorial pending-source-review disposition for these exact observed bytes, not a scientific rejection or acceptance.' })

async function temp(t) {
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), 'marici-currency-'))
  t.after(() => fs.rm(dir, { recursive: true, force: true }))
  return dir
}
async function put(dir, file, text) {
  await fs.mkdir(path.dirname(path.join(dir, file)), { recursive: true })
  await fs.writeFile(path.join(dir, file), text)
}
async function configFixture(t, q = queue) {
  const dir = await temp(t)
  await put(dir, baselineFile, canonicalJSON(baseline))
  await put(dir, dispositionsFile, canonicalJSON(q))
  for (const route of new Set(queue.inventory.flatMap(item => item.coverage))) await put(dir, 'website' + route + '.md', '# Coverage fixture\n')
  return dir
}

test('reviewed 160-file inventory has accountable, non-scientific dispositions', () => {
  const result = assessResearchCurrency(baseline, queue, baseline.observed_files)
  assert.equal(result.audited_files, 160)
  assert.equal(queue.thematic_commits.length, 18)
  assert.equal(queue.groups.length, 15)
  assert.deepEqual(result.disposition_counts, { 'public-coverage': 11, 'historical-superseded': 26, 'development-only': 7, duplicate: 6, 'pending-source-review': 110 })
  assert.deepEqual(result.changes, [])
  assert.equal(baseline.observation_is_scientific_review, false)
  assert.equal(queue.scientific_dispositions_modified, false)
})

test('fresh actual research tree still matches observed source checkpoint', async () => {
  const result = await checkResearchCurrency(root)
  assert.equal(result.observed_files, baseline.observed_files.length)
  assert.deepEqual(result.unreviewed, [])
})

test('new uncited research is unreviewed, not automatically covered or scientifically failed', () => {
  const result = assessResearchCurrency(baseline, queue, [...baseline.observed_files, unknown])
  assert.deepEqual(result.unreviewed, [{ ...unknown, change: 'added', disposition: 'unreviewed' }])
  assert.equal('scientific_verdict' in result.unreviewed[0], false)
})

for (const change of ['modified', 'deleted']) test(`detects ${change} legacy research outside the selected 160`, () => {
  const item = baseline.observed_files.find(item => !queue.inventory.some(row => row.path === item.path))
  const observed = baseline.observed_files.filter(row => row.path !== item.path)
  if (change === 'modified') observed.push({ path: item.path, text_sha256: sha256('changed legacy source') })
  const result = assessResearchCurrency(baseline, queue, observed)
  assert.equal(result.unreviewed.length, 1)
  assert.equal(result.unreviewed[0].path, item.path)
  assert.equal(result.unreviewed[0].change, change)
})

test('edited initially covered source also needs new review, despite an existing route', () => {
  const selected = queue.inventory.find(item => item.disposition === 'public-coverage')
  const observed = baseline.observed_files.map(row => row.path === selected.path ? { ...row, text_sha256: sha256('changed selected source') } : row)
  assert.equal(assessResearchCurrency(baseline, queue, observed).unreviewed[0].change, 'modified')
})

for (const change of ['added', 'modified', 'deleted']) test(`explicit ${change} review binds exact current source state`, () => {
  const q = copy(queue), item = change === 'added' ? unknown : baseline.observed_files[0]
  const observed = baseline.observed_files.filter(row => row.path !== item.path)
  const hash = change === 'deleted' ? null : sha256('reviewed source')
  if (hash) observed.push({ path: item.path, text_sha256: hash })
  q.subsequent_dispositions.push(subsequent(item, change, hash))
  const result = assessResearchCurrency(baseline, q, observed)
  assert.equal(result.unreviewed.length, 0)
  assert.equal(result.changes[0].disposition, 'pending-source-review')
})

test('subsequent review cannot remain valid after further source drift', () => {
  const q = copy(queue)
  q.subsequent_dispositions.push(subsequent(unknown, 'added', unknown.text_sha256))
  assert.throws(() => assessResearchCurrency(baseline, q, [...baseline.observed_files, { ...unknown, text_sha256: sha256('later drift') }]), /Stale subsequent/)
})

test('removed/reverted changes cannot leave a falsely current review', () => {
  const q = copy(queue)
  q.subsequent_dispositions.push(subsequent(unknown, 'added', unknown.text_sha256))
  assert.throws(() => assessResearchCurrency(baseline, q, baseline.observed_files), /Stale subsequent/)
})

test('baseline cannot be recaptured and re-digested to disguise source additions', () => {
  const b = copy(baseline), q = copy(queue)
  b.observed_files.push(unknown)
  q.baseline_sha256 = sha256(canonicalJSON(b))
  assert.throws(() => assessResearchCurrency(b, q, b.observed_files), /baseline drift/)
})

test('160 rows cannot be preserved by swapping an audited source for an unrelated old one', () => {
  const q = copy(queue)
  q.inventory[0] = { ...q.inventory[0], ...baseline.observed_files.find(row => !queue.inventory.some(item => item.path === row.path)) }
  assert.throws(() => assessResearchCurrency(baseline, q, baseline.observed_files), /inventory drift/)
})

for (const [name, mutate, expected] of [
  ['omission', q => q.inventory.pop(), /160-file/],
  ['missing disposition', q => delete q.inventory[0].disposition, /Incomplete research disposition/],
  ['missing rationale', q => q.inventory[0].rationale = '', /Incomplete research disposition/],
  ['missing revision', q => q.inventory[0].reviewed_revision = '', /Incomplete research disposition/],
  ['invented scientific acceptance', q => q.inventory[0].disposition = 'scientifically-verified', /Incomplete research disposition/],
  ['false verdict modification', q => q.scientific_dispositions_modified = true, /overstated/],
  ['unreviewed capture candidate', q => q.review_state = 'candidate-unreviewed', /overstated/],
  ['thematic commit identity drift', q => q.thematic_commits[0].commit = '0'.repeat(40), /Thematic commit/],
  ['public row without coverage', q => q.inventory.find(x => x.disposition === 'public-coverage').coverage = [], /no coverage/],
  ['coverage traversal', q => q.inventory[0].coverage = ['/research/../../secret'], /Unsafe/],
  ['false duplicate', q => q.inventory.find(x => x.disposition === 'duplicate').duplicate_of = baseline.observed_files[0].path, /Unverified duplicate/],
  ['history without successor', q => delete q.inventory.find(x => x.disposition === 'historical-superseded').superseded_by, /historical successor/]
]) test(`rejects ${name}`, () => {
  const q = copy(queue); mutate(q)
  assert.throws(() => assessResearchCurrency(baseline, q, baseline.observed_files), expected)
})

test('standalone enforcement rejects undispositioned addition without touching owner sources', async t => {
  const dir = await configFixture(t)
  await assert.rejects(checkResearchCurrency(dir, { observed: [...baseline.observed_files, unknown] }), /Unreviewed research Markdown: added research\/fixture\/new-source.md/)
  const result = await checkResearchCurrency(dir, { observed: [...baseline.observed_files, unknown], observeOnly: true })
  assert.equal(result.unreviewed.length, 1)
  await assert.rejects(fs.access(path.join(dir, '.ai')))
})

test('normal check works without ignored capture plans or receipts', async t => {
  const dir = await configFixture(t)
  assert.deepEqual((await checkResearchCurrency(dir, { observed: baseline.observed_files })).changes, [])
})

test('rejects missing public coverage guide', async t => {
  const dir = await configFixture(t)
  await fs.rm(path.join(dir, 'website' + queue.inventory.find(item => item.disposition === 'public-coverage').coverage[0] + '.md'))
  await assert.rejects(checkResearchCurrency(dir, { observed: baseline.observed_files }), /coverage guide missing/)
})

test('observer hashes UTF-8 LF-normalized text, preserves BOM and excludes declared generated/runtime directories', async t => {
  const dir = await temp(t)
  await put(dir, 'research/a.md', '# A\r\nx\ry\n')
  await put(dir, 'research/b.md', '\uFEFF# B\n')
  for (const folder of ['results', 'node_modules', '.check-tmp-fixture', '.tmp-fixture']) await put(dir, 'research/' + folder + '/ignored.md', '# Runtime\n')
  await put(dir, 'research/data.json', '{}')
  assert.deepEqual(await observeResearchMarkdown(dir), [
    { path: 'research/a.md', text_sha256: sha256('# A\nx\ny\n') },
    { path: 'research/b.md', text_sha256: sha256('\uFEFF# B\n') }
  ])
})

test('legacy non-UTF-8 bytes are preserved without replacement-decoding hash collisions', async t => {
  const dir = await temp(t)
  await put(dir, 'research/legacy.md', Buffer.from([0xff]))
  const first = await observeResearchMarkdown(dir)
  await put(dir, 'research/legacy.md', Buffer.from([0xfe]))
  const second = await observeResearchMarkdown(dir)
  assert.equal(first[0].text_sha256, sha256(Buffer.from([0xff])))
  assert.notEqual(first[0].text_sha256, second[0].text_sha256)
})
