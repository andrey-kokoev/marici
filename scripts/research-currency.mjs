import fs from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('../', import.meta.url))
export const baselineFile = 'config/research-currency-baseline.v1.json'
export const dispositionsFile = 'config/research-change-dispositions.v1.json'
export const excludedDirectories = ['.ai', '.git', '.venv', '__pycache__', 'node_modules', 'results', 'runs', 'scc-freezes', 'target', 'vendor']
export const canonicalJSON = value => JSON.stringify(value, null, 2) + '\n'
export const sha256 = value => createHash('sha256').update(value).digest('hex')
// Byte-preserving newline normalization also handles legacy non-UTF-8 notes.
export const normalizedSourceBytes = bytes => Buffer.from(bytes.toString('latin1').replace(/\r\n?/g, '\n'), 'latin1')
export const reviewedBaselineSha256 = '3b4d1abae2900b378c5a0476b39c00a1c2d020d730553495a6a7f4dc86787b15'
export const reviewedInventorySha256 = 'a978836ef40520f370258a108521c0bc5cf24df80043710e58e367cb188c89bd'
export const reviewedThematicSha256 = 'b4b507584d11fd76bbe9d80573f37d9134d38ebdad1bbcf5decf18d878812bea'
export const inventoryIdentity = inventory => inventory.map(({ path, text_sha256, changed_in }) => ({ path, text_sha256, changed_in })).sort((a, b) => a.path < b.path ? -1 : a.path > b.path ? 1 : 0)
const digest = /^[a-f0-9]{64}$/
const commit = /^[a-f0-9]{40}$/
const dispositions = new Set(['public-coverage', 'historical-superseded', 'development-only', 'duplicate', 'pending-source-review'])
const safe = value => typeof value === 'string' && value.startsWith('research/') && value.endsWith('.md') && !/[\\\r\n\0]/.test(value) && !value.split('/').some(part => !part || part === '.' || part === '..')
export const sourceScope = { root: 'research', extension: '.md', excluded_directories: excludedDirectories, excluded_prefixes: ['.check-tmp-', '.tmp'] }

export async function observeResearchMarkdown(base = root) {
  const records = []
  async function walk(relative) {
    for (const entry of await fs.readdir(path.join(base, relative), { withFileTypes: true })) {
      if (excludedDirectories.includes(entry.name) || sourceScope.excluded_prefixes.some(prefix => entry.name.startsWith(prefix))) continue
      const file = relative + '/' + entry.name
      if (entry.isSymbolicLink()) throw Error('Research source symlink requires explicit inventory policy: ' + file)
      if (entry.isDirectory()) await walk(file)
      else if (entry.isFile() && entry.name.endsWith('.md')) {
        if (!safe(file)) throw Error('Unsafe research source path')
        const bytes = await fs.readFile(path.join(base, file))
        records.push({ path: file, text_sha256: sha256(normalizedSourceBytes(bytes)) })
      }
    }
  }
  await walk('research')
  return records.sort((a, b) => a.path < b.path ? -1 : a.path > b.path ? 1 : 0)
}

export function assessResearchCurrency(baseline, queue, observed) {
  if (baseline.schema !== 'marici.research-currency-baseline.v1' || queue.schema !== 'marici.research-change-dispositions.v1' || queue.scientific_dispositions_modified !== false || queue.review_state !== 'reviewed-editorial-dispositions' || !Number.isInteger(queue.revision) || queue.revision < 1 || baseline.observation_is_scientific_review !== false || JSON.stringify(baseline.source_scope) !== JSON.stringify(sourceScope)) throw Error('Invalid or overstated research currency policy')
  if (!commit.test(baseline.baseline_commit) || !commit.test(baseline.compare_base) || queue.baseline_sha256 !== reviewedBaselineSha256 || sha256(canonicalJSON(baseline)) !== reviewedBaselineSha256) throw Error('Research currency baseline drift; review a successor, not an automatic recapture')
  const index = new Map()
  for (const item of baseline.observed_files) {
    if (!safe(item.path) || !digest.test(item.text_sha256) || index.has(item.path)) throw Error('Invalid/duplicate baseline source')
    index.set(item.path, item.text_sha256)
  }
  const current = new Map()
  for (const item of observed) {
    if (!safe(item.path) || !digest.test(item.text_sha256) || current.has(item.path)) throw Error('Invalid/duplicate observed source')
    current.set(item.path, item.text_sha256)
  }
  if (sha256(canonicalJSON(queue.thematic_commits)) !== reviewedThematicSha256) throw Error('Thematic commit evidence drift')
  const groups = new Map(queue.groups.map(group => [group.id, group]))
  if (groups.size !== queue.groups.length || queue.thematic_commits.length !== 18 || queue.inventory.length !== 160) throw Error('Incomplete audited eighteen-commit/160-file inventory')
  if (sha256(canonicalJSON(inventoryIdentity(queue.inventory))) !== reviewedInventorySha256) throw Error('Audited research inventory drift')
  for (const group of groups.values()) if (typeof group.id !== 'string' || typeof group.rationale !== 'string' || group.rationale.length < 20) throw Error('Incomplete editorial review group')
  function validateDisposition(item) {
    if (!safe(item.path) || !dispositions.has(item.disposition) || !groups.has(item.group) || typeof item.rationale !== 'string' || item.rationale.length < 20 || !commit.test(item.reviewed_revision)) throw Error('Incomplete research disposition: ' + item.path)
    if (!Array.isArray(item.coverage) || item.coverage.some(route => typeof route !== 'string' || !/^\/(research|experiments)\/[a-z0-9/.-]+$/.test(route) || route.split('/').slice(1).some(part => !part || part === '.' || part === '..'))) throw Error('Unsafe disposition coverage route')
    if (item.disposition === 'public-coverage' && !item.coverage.length) throw Error('Public disposition has no coverage: ' + item.path)
    if (item.disposition === 'duplicate' && (!safe(item.duplicate_of) || item.duplicate_of === item.path)) throw Error('Missing duplicate source: ' + item.path)
    if (item.disposition === 'historical-superseded' && (!safe(item.superseded_by) || !index.has(item.superseded_by))) throw Error('Missing historical successor: ' + item.path)
  }
  const inventory = new Set()
  const commits = new Set(queue.thematic_commits.map(item => item.commit))
  if (commits.size !== 18 || [...commits].some(value => !commit.test(value))) throw Error('Invalid thematic commit identities')
  for (const item of queue.inventory) {
    validateDisposition(item)
    if (inventory.has(item.path) || !index.has(item.path) || index.get(item.path) !== item.text_sha256 || !Array.isArray(item.changed_in) || !item.changed_in.length || item.changed_in.some(value => !commits.has(value))) throw Error('Invalid audited research entry: ' + item.path)
    if (item.disposition === 'duplicate' && index.get(item.duplicate_of) !== item.text_sha256) throw Error('Unverified duplicate content: ' + item.path)
    inventory.add(item.path)
  }
  const reviews = new Map()
  for (const item of queue.subsequent_dispositions) {
    validateDisposition(item)
    if (reviews.has(item.path) || !['added', 'modified', 'deleted'].includes(item.change) || (item.change === 'deleted' ? item.text_sha256 !== null : !digest.test(item.text_sha256))) throw Error('Invalid subsequent review')
    if (item.disposition === 'duplicate' && (item.change === 'deleted' || current.get(item.duplicate_of) !== item.text_sha256)) throw Error('Unverified subsequent duplicate: ' + item.path)
    reviews.set(item.path, item)
  }
  const changes = []
  for (const file of new Set([...index.keys(), ...current.keys()])) {
    if (index.get(file) === current.get(file)) continue
    const change = !index.has(file) ? 'added' : !current.has(file) ? 'deleted' : 'modified'
    const review = reviews.get(file)
    changes.push({ path: file, change, text_sha256: current.get(file) ?? null,
      disposition: review && review.change === change && review.text_sha256 === (current.get(file) ?? null) ? review.disposition : 'unreviewed' })
  }
  for (const review of reviews.values()) if (!changes.some(item => item.path === review.path && item.disposition !== 'unreviewed')) throw Error('Stale subsequent research disposition: ' + review.path)
  return { schema: 'marici.research-currency-observation.v1', scope: 'Editorial source-change accountability only; not semantic coverage or scientific acceptance',
    baseline_commit: baseline.baseline_commit, compared_from: baseline.compare_base, audited_files: inventory.size, observed_files: current.size,
    changes, unreviewed: changes.filter(item => item.disposition === 'unreviewed'),
    disposition_counts: Object.fromEntries([...dispositions].map(value => [value, queue.inventory.filter(item => item.disposition === value).length])),
    git_scope: 'Content comparison detects Markdown changes from later commits and dirty worktrees; no Git process/head polling or every-commit history claim' }
}

export const effectiveDispositions = queue => [...new Map([...queue.inventory, ...queue.subsequent_dispositions].map(item => [item.path, item])).values()]

export async function checkResearchCurrency(base = root, { observed, observeOnly = false } = {}) {
  const baseline = JSON.parse(await fs.readFile(path.join(base, baselineFile), 'utf8'))
  const queue = JSON.parse(await fs.readFile(path.join(base, dispositionsFile), 'utf8'))
  const result = assessResearchCurrency(baseline, queue, observed ?? await observeResearchMarkdown(base))
  for (const route of new Set(effectiveDispositions(queue).flatMap(item => item.coverage))) {
    try { await fs.access(path.join(base, 'website', route.slice(1) + '.md')) }
    catch (error) { throw Error('Research disposition coverage guide missing: ' + route, { cause: error }) }
  }
  if (!observeOnly && result.unreviewed.length) throw Error('Unreviewed research Markdown: ' + result.unreviewed.slice(0, 20).map(item => item.change + ' ' + item.path).join('; ') + ` (${result.unreviewed.length} total; use --observe for the full list). Record a reviewed disposition; do not auto-refresh the baseline.`)
  return result
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  if (process.argv.slice(2).some(arg => arg !== '--observe')) throw Error('Only --observe is supported')
  const result = await checkResearchCurrency(root, { observeOnly: process.argv.includes('--observe') })
  if (process.argv.includes('--observe')) {
    await fs.mkdir(path.join(root, '.ai'), { recursive: true })
    await fs.writeFile(path.join(root, '.ai/research-currency-observation.json'), canonicalJSON(result))
  }
  console.log(JSON.stringify(result))
}
