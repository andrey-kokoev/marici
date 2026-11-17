// Explicit metadata candidate capture only. Normal checks never recapture.
// Uses the preserved path manifests of the already executed thematic commits;
// no Git CLI, scientific checker, source mutation or disposition admission.
import fs from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { observeResearchMarkdown, assessResearchCurrency, baselineFile, dispositionsFile, sourceScope, canonicalJSON, sha256 } from './research-currency.mjs'
const root = fileURLToPath(new URL('../', import.meta.url))
const args = process.argv.slice(2)
if (args.length) {
  if (args.length !== 2 || args[0] !== '--accept-reviewed-candidate' || !/^[a-f0-9]{64}$/.test(args[1])) throw Error('Usage: no arguments to capture an ignored candidate; --accept-reviewed-candidate SHA256 to exclusively create reviewed v1 configs')
  const baseline = JSON.parse(await fs.readFile(path.join(root, '.ai/research-currency-candidate/baseline.json'), 'utf8'))
  const queue = JSON.parse(await fs.readFile(path.join(root, '.ai/research-currency-candidate/dispositions.json'), 'utf8'))
  if (sha256(canonicalJSON({ baseline, queue })) !== args[1]) throw Error('Reviewed candidate digest mismatch')
  const result = assessResearchCurrency(baseline, queue, await observeResearchMarkdown(root))
  if (result.changes.length) throw Error('Source changed since candidate capture; no adoption')
  for (const file of [baselineFile, dispositionsFile]) {
    try { await fs.access(path.join(root, file)) } catch (error) { if (error.code === 'ENOENT') continue; throw error }
    throw Error('Refusing to overwrite reviewed research currency config: ' + file)
  }
  await fs.writeFile(path.join(root, baselineFile), canonicalJSON(baseline), { flag: 'wx' })
  await fs.writeFile(path.join(root, dispositionsFile), canonicalJSON(queue), { flag: 'wx' })
  console.log(JSON.stringify({ adopted_candidate_sha256: args[1], ...result }))
  process.exit(0)
}
const planDir = '.ai/thematic-commit-plan'
const plan = JSON.parse(await fs.readFile(path.join(root, planDir, 'committed.json'), 'utf8'))
const endpoint = '3ace86e3340491c07fdf1c186d99d9ce77140d6b'
if (plan.base !== '518280545d386097ed9bc71588cd084c444fd3dc' || plan.commits.length !== 18 || plan.commits.at(-1).commit !== endpoint) throw Error('Unexpected thematic manifest range')
const observed = await observeResearchMarkdown(root)
const index = new Map(observed.map(item => [item.path, item]))
const changes = new Map(), manifests = []
for (const item of plan.commits) {
  const file = planDir + '/' + item.group + '.commit-paths.z'
  const bytes = await fs.readFile(path.join(root, file))
  const paths = bytes.toString('utf8').split('\0').filter(Boolean)
  if (paths.length !== item.files) throw Error('Thematic manifest count drift: ' + file)
  manifests.push({ group: item.group, commit: item.commit, subject: item.subject, path_manifest_sha256: sha256(bytes), files: paths.length })
  for (const source of paths.filter(file => file.startsWith('research/') && file.endsWith('.md'))) {
    if (!index.has(source)) throw Error('Audited Markdown missing from source observation: ' + source)
    if (!changes.has(source)) changes.set(source, { group: item.group, changed_in: [] })
    changes.get(source).changed_in.push(item.commit)
  }
}
if (changes.size !== 160) throw Error('Audited Markdown inventory differs from 160: ' + changes.size)
const baseline = { schema: 'marici.research-currency-baseline.v1', compare_base: plan.base, baseline_commit: endpoint,
  capture_kind: 'Source text observation only; Git commit identities/path manifests were reviewed separately through the owning Git surface',
  observation_is_scientific_review: false, text_hash_basis: 'SHA-256 of source bytes after CRLF/CR to LF normalization; BOM and legacy non-UTF-8 bytes preserved, no replacement decoding', source_scope: sourceScope, observed_files: observed }
const publicCoverage = new Map()
for (const [file, legacy] of [['config/current-research-provenance.v1.json', true], ['config/current-research-provenance.v2.json', false]]) {
  const manifest = JSON.parse(await fs.readFile(path.join(root, file), 'utf8'))
  for (const item of manifest.entries) for (const pin of item.source_packets) if (pin.path.endsWith('.md')) {
    if (!publicCoverage.has(pin.path)) publicCoverage.set(pin.path, new Set())
    publicCoverage.get(pin.path).add(legacy ? '/research/results/' + item.slug : item.route)
  }
}
for (const source of ['research/matter/README.md', 'research/matter/ISOTOPE-REFERENCE.md']) publicCoverage.set(source, new Set(['/experiments/isotope-reference']))
const groups = manifests.map(item => ({ id: item.group, title: item.subject, rationale: 'Editorial grouping by the actual thematic commit. Unselected notes remain pending source review, not rejected or semantically absent; scientific ownership and verdicts are unchanged.' }))
const byHash = new Map()
for (const source of [...changes.keys()].sort()) {
  const hash = index.get(source).text_sha256
  if (!byHash.has(hash)) byHash.set(hash, [])
  byHash.get(hash).push(source)
}
const inventory = []
for (const source of [...changes.keys()].sort()) {
  const { group, changed_in } = changes.get(source)
  const text = await fs.readFile(path.join(root, source), 'utf8')
  const title = text.replace(/^\uFEFF/, '').split(/\r?\n/).find(line => /^#\s/.test(line))?.replace(/^#\s+/, '').slice(0, 180) ?? source
  const coverage = [...(publicCoverage.get(source) ?? [])]
  const equals = byHash.get(index.get(source).text_sha256)
  const canonical = equals.find(file => !/\(\d+\)\.md$/.test(file)) ?? equals[0]
  const duplicate = equals.length > 1 && source !== canonical
  inventory.push({ path: source, title, group, changed_in, reviewed_revision: endpoint, text_sha256: index.get(source).text_sha256,
    disposition: duplicate ? 'duplicate' : coverage.length ? 'public-coverage' : 'pending-source-review',
    rationale: duplicate ? 'Exact LF-normalized text duplicate of the named canonical source; no separate scientific validation or claim of originality.' : coverage.length ? 'Selected source/context is explicitly covered by the linked bounded result or explanation; publication coverage is not scientific admission, full semantic exhaustion or public net/app release.' : 'Committed source in this thematic family has not been selected for an additional public claim by this bounded review. Pending source review is explicit; indirect/transitive coverage elsewhere is possible and citation absence is not scientific inadequacy.',
    coverage, ...(duplicate ? { duplicate_of: canonical } : {}) })
}
const queue = { schema: 'marici.research-change-dispositions.v1', review_state: 'candidate-unreviewed', revision: 1, baseline_sha256: sha256(canonicalJSON(baseline)), scientific_dispositions_modified: false,
  reviewed_at_host_utc: new Date().toISOString(), review_actor: 'anonymous',
  review_scope: 'Website editorial dispositions only, not source-owner scientific acceptance. Legacy observation outside the audited 160-file set is a detection baseline, not a claim review.',
  inventory_origin: 'Preserved executed eighteen-commit NUL path manifests; endpoints and thematic commit metadata cross-checked through Site-local Git. The earlier audit reported the same 160-file Markdown count; this is count corroboration, not an independent per-path diff replay. No new Git diff replay is claimed by this capture script.',
  thematic_commits: manifests, groups, inventory, subsequent_dispositions: [] }
await fs.mkdir(path.join(root, '.ai/research-currency-candidate'), { recursive: true })
for (const [name, data] of [['baseline.json', baseline], ['dispositions.json', queue]]) await fs.writeFile(path.join(root, '.ai/research-currency-candidate', name), canonicalJSON(data))
console.log(JSON.stringify({ scope: 'Metadata candidates only; inspect groups/dispositions before adopting', audited: inventory.length, observed: observed.length,
  counts: Object.fromEntries(['public-coverage', 'duplicate', 'pending-source-review'].map(value => [value, inventory.filter(item => item.disposition === value).length])),
  groups: manifests.map(group => ({ ...group, markdown: inventory.filter(item => item.group === group.group).length })) }))
