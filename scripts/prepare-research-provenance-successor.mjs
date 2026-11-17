import fs from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'
import { prepareCurrentResearchProvenance } from './prepare-current-research-provenance.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))
export const successorConfig = 'config/current-research-provenance.v2.json'
export const successorSelection = 'config/research-provenance-selection.v2.json'
const predecessor = 'config/current-research-provenance.v1.json'
const target = 'website/public/research/provenance/current-results.v2.json'
const candidate = '.ai/current-results-provenance-v2-candidate.json'
const frozenV1 = '2963ef78d9cf0b8137ca0f54bdc7d10b6351c47abdf936ef16315c012496d611'
const expectedIDs = ['source-certified-coherent-assembly', 'ramsey-retained-assembly-coherence', 'ramsey-november-programme', 'typed-editor-morse-explanation', 'held-pe-publication-explanation']
const hash = bytes => createHash('sha256').update(bytes).digest('hex')
const canonical = value => JSON.stringify(value, null, 2) + '\n'
const digest = /^[a-f0-9]{64}$/
const safePath = value => typeof value === 'string' && /^(research|apps|src|scripts)\/[A-Za-z0-9_./-]+$/.test(value) && !value.split('/').some(part => !part || part === '.' || part === '..')
const readJSON = async (base, file) => JSON.parse(await fs.readFile(path.join(base, file), 'utf8'))
const same = (a, b) => JSON.stringify(a) === JSON.stringify(b)
function keys(value, allowed) {
  if (!value || typeof value !== 'object' || Array.isArray(value) || Object.keys(value).some(key => !allowed.includes(key))) throw Error('Unsupported provenance metadata fields')
}
async function pin(base, file) {
  if (!safePath(file)) throw Error('Unsafe successor source path: ' + file)
  const text = (await fs.readFile(path.join(base, file), 'utf8')).replace(/\r\n?/g, '\n')
  return { path: file, text_sha256: hash(text) }
}
async function context(base) {
  const previous = await readJSON(base, predecessor)
  if (hash(canonical(previous)) !== frozenV1) throw Error('Frozen predecessor v1 changed; do not recapture its pins')
  const selection = await readJSON(base, successorSelection)
  if (selection.schema !== 'marici.research-provenance-selection.v2' || !same(selection.entries.map(entry => entry.id), expectedIDs)) throw Error('Missing or unreviewed successor selection')
  const inventory = await readJSON(base, 'src/data/results-physics.json')
  return { selection, inventory }
}

export async function captureSuccessorResearchProvenance(base = root) {
  const { selection, inventory } = await context(base)
  const entries = []
  for (const spec of selection.entries) {
    const result = spec.kind === 'result' ? inventory.find(item => item.slug === spec.id) : null
    if (spec.kind === 'result' && !result) throw Error('Missing selected successor result: ' + spec.id)
    const receipts = []
    for (const file of spec.historical_receipts) {
      if (!safePath(file)) throw Error('Unsafe successor receipt path')
      let bytes
      try { bytes = await fs.readFile(path.join(base, file)) }
      catch (error) {
        if (error.code !== 'ENOENT') throw error
        receipts.push({ path: file, availability: 'unavailable at capture', reason: 'Historical payload not present; no identity or successful replay invented' })
        continue
      }
      const data = JSON.parse(bytes.toString('utf8').replace(/^\uFEFF/, ''))
      const metadata = {}
      for (const key of ['schema', 'status', 'checkerStatus', 'scientificStatus', 'outcome']) if (typeof data[key] === 'string' && data[key].length <= 240) metadata[key] = data[key]
      const recorded = {}
      const executable = data.compiler_sha256 ?? data.agda_executable_sha256 ?? data.source_inventory?.compiler
      if (typeof executable === 'string' && digest.test(executable)) recorded.executable_sha256 = executable
      const version = data.compiler_version ?? data.agda_version
      if (typeof version === 'string') recorded.version = version.split(/\r?\n/)[0].slice(0, 160)
      receipts.push({ path: file, availability: 'historical identifier captured', sha256: hash(bytes), bytes: bytes.length,
        ...(Object.keys(metadata).length ? { recorded_metadata: metadata } : {}), ...(Object.keys(recorded).length ? { recorded_compiler: recorded } : {}) })
    }
    entries.push({ ...spec,
      ...(result ? { reported_status: result.status, inventory_checker: result.checker } : {}),
      source_packets: await Promise.all(spec.source_packets.map(file => pin(base, file))),
      checker_sources: await Promise.all(spec.checker_sources.map(file => pin(base, file))), historical_receipts: receipts })
  }
  return { schema: 'marici.public-research-provenance.v2', snapshot_id: 'current-results-publication-v2',
    predecessor: { path: predecessor, snapshot_id: 'current-results-publication-v1', canonical_sha256: frozenV1 },
    selection: { path: successorSelection, canonical_sha256: hash(canonical(selection)) },
    captured_at: new Date().toISOString(), capture_clock: 'Host UTC wall clock, not a scientific execution or independently verified calendar date',
    capture_kind: 'Reviewed file metadata only; no scientific execution', scientific_replay_performed: false, scientific_verdicts_modified: false,
    receipt_source_compatibility: 'not revalidated', transitive_dependency_closure: 'not claimed',
    text_hash_basis: 'SHA-256 of UTF-8 text with CRLF/CR normalized to LF; BOM preserved',
    receipt_hash_basis: 'SHA-256 of exact historical bytes; receipt payloads not published',
    entries }
}

async function validate(base, manifest) {
  keys(manifest, ['schema', 'snapshot_id', 'predecessor', 'selection', 'captured_at', 'capture_clock', 'capture_kind', 'scientific_replay_performed', 'scientific_verdicts_modified', 'receipt_source_compatibility', 'transitive_dependency_closure', 'text_hash_basis', 'receipt_hash_basis', 'entries'])
  if (manifest.schema !== 'marici.public-research-provenance.v2' || manifest.snapshot_id !== 'current-results-publication-v2' || manifest.scientific_replay_performed !== false || manifest.scientific_verdicts_modified !== false || manifest.receipt_source_compatibility !== 'not revalidated' || manifest.transitive_dependency_closure !== 'not claimed') throw Error('Unsupported or overstated successor provenance')
  if (manifest.capture_kind !== 'Reviewed file metadata only; no scientific execution' || manifest.capture_clock !== 'Host UTC wall clock, not a scientific execution or independently verified calendar date' || typeof manifest.captured_at !== 'string' || !/^\d{4}-\d\d-\d\dT/.test(manifest.captured_at) || manifest.text_hash_basis !== 'SHA-256 of UTF-8 text with CRLF/CR normalized to LF; BOM preserved' || manifest.receipt_hash_basis !== 'SHA-256 of exact historical bytes; receipt payloads not published') throw Error('Unsupported or overstated successor capture/hash policy')
  const { selection, inventory } = await context(base)
  if (!same(manifest.predecessor, { path: predecessor, snapshot_id: 'current-results-publication-v1', canonical_sha256: frozenV1 })) throw Error('Invalid predecessor binding')
  if (!same(manifest.selection, { path: successorSelection, canonical_sha256: hash(canonical(selection)) })) throw Error('Unreviewed successor selection drift')
  if (!Array.isArray(manifest.entries) || !same(manifest.entries.map(entry => entry.id), expectedIDs)) throw Error('Missing or duplicate successor coverage')
  const slugs = [], routes = []
  for (const [i, entry] of manifest.entries.entries()) {
    const spec = selection.entries[i]
    keys(entry, ['id', 'kind', 'route', 'source_packets', 'checker_sources', 'historical_receipts', 'unavailable_inputs', 'boundary', 'reproduction', 'compatibility_limits', 'reported_status', 'inventory_checker'])
    for (const key of ['id', 'kind', 'route', 'boundary', 'reproduction', 'unavailable_inputs', 'compatibility_limits']) if (!same(entry[key], spec[key])) throw Error('Successor selection binding drift: ' + entry.id + '/' + key)
    if (!/^\/(research|experiments)\/[a-z0-9/-]+$/.test(entry.route) || !entry.boundary || !entry.reproduction || !entry.compatibility_limits.length || !['guide', 'result'].includes(entry.kind)) throw Error('Invalid successor scope/route')
    routes.push(entry.route)
    if (entry.kind === 'result') {
      const result = inventory.find(item => item.slug === entry.id)
      if (!result || entry.reported_status !== result.status || entry.inventory_checker !== result.checker || entry.route !== '/research/results/' + entry.id) throw Error('Stale successor result/status/checker: ' + entry.id)
      if (!result.checker.split('; ').every(file => spec.checker_sources.includes(file))) throw Error('Unpinned advertised checker: ' + entry.id)
      slugs.push(entry.id)
    } else if ('reported_status' in entry || 'inventory_checker' in entry) throw Error('Guide cannot invent a result status')
    for (const key of ['source_packets', 'checker_sources']) {
      if (!Array.isArray(entry[key]) || !entry[key].length || !same(entry[key].map(item => item.path), spec[key])) throw Error('Missing successor source/checker selection')
      for (const item of entry[key]) {
        keys(item, ['path', 'text_sha256'])
        if (!safePath(item.path) || !digest.test(item.text_sha256)) throw Error('Invalid successor source pin')
        if ((await pin(base, item.path)).text_sha256 !== item.text_sha256) throw Error('Stale successor source: ' + item.path + '; review, do not auto-recapture')
      }
    }
    if (!Array.isArray(entry.historical_receipts) || !same(entry.historical_receipts.map(item => item.path), spec.historical_receipts)) throw Error('Missing successor historical receipt coverage')
    for (const receipt of entry.historical_receipts) {
      keys(receipt, ['path', 'availability', 'reason', 'sha256', 'bytes', 'recorded_metadata', 'recorded_compiler'])
      if (!safePath(receipt.path)) throw Error('Invalid successor receipt path')
      if (receipt.availability === 'historical identifier captured') {
        if (!digest.test(receipt.sha256) || !Number.isSafeInteger(receipt.bytes) || receipt.bytes <= 0 || 'reason' in receipt) throw Error('Invalid successor historical receipt identity')
        if (receipt.recorded_metadata) {
          keys(receipt.recorded_metadata, ['schema', 'status', 'checkerStatus', 'scientificStatus', 'outcome'])
          if (Object.values(receipt.recorded_metadata).some(value => typeof value !== 'string' || value.length > 240)) throw Error('Unsafe receipt metadata')
        }
        if (receipt.recorded_compiler) {
          keys(receipt.recorded_compiler, ['executable_sha256', 'version'])
          if (receipt.recorded_compiler.executable_sha256 !== undefined && !digest.test(receipt.recorded_compiler.executable_sha256)) throw Error('Invalid recorded compiler identity')
          if (receipt.recorded_compiler.version !== undefined && (typeof receipt.recorded_compiler.version !== 'string' || receipt.recorded_compiler.version.length > 160 || /[\r\n]/.test(receipt.recorded_compiler.version))) throw Error('Invalid recorded compiler version')
        }
      } else if (receipt.availability !== 'unavailable at capture' || typeof receipt.reason !== 'string' || !receipt.reason || ['sha256', 'bytes', 'recorded_metadata', 'recorded_compiler'].some(key => key in receipt)) throw Error('Invalid unavailable-receipt boundary')
      // Deliberately do not read ignored receipts or replay scientific suppliers.
    }
  }
  const content = canonical(manifest)
  if (Buffer.byteLength(content) > 65536) throw Error('Successor metadata exceeds compact budget')
  return { content, slugs, routes }
}

export async function prepareSuccessorResearchProvenance(base = root, { check = false } = {}) {
  const manifest = await readJSON(base, successorConfig)
  const { content, slugs, routes } = await validate(base, manifest)
  const output = path.join(base, target)
  if (check) {
    if (await fs.readFile(output, 'utf8').catch(() => null) !== content) throw Error('Stale successor public provenance copy')
  } else {
    await fs.mkdir(path.dirname(output), { recursive: true })
    await fs.writeFile(output, content)
  }
  return { snapshot_id: manifest.snapshot_id, slugs, routes, sha256: hash(content), bytes: Buffer.byteLength(content), target }
}

export async function preparePublicationResearchProvenance(base = root, options = {}) {
  await context(base) // Freeze predecessor before any output write.
  const previous = await prepareCurrentResearchProvenance(base, options)
  const current = await prepareSuccessorResearchProvenance(base, options)
  return { ...current, slugs: [...previous.slugs, ...current.slugs], predecessor: previous }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const args = process.argv.slice(2)
  if (same(args, ['--capture'])) {
    const content = canonical(await captureSuccessorResearchProvenance(root))
    await fs.mkdir(path.join(root, '.ai'), { recursive: true })
    await fs.writeFile(path.join(root, candidate), content)
    console.log(JSON.stringify({ scope: 'Metadata candidate only; inspect before acceptance; no scientific execution', candidate, sha256: hash(content), bytes: Buffer.byteLength(content) }))
  } else if (args[0] === '--accept-reviewed-candidate' && args.length === 2 && digest.test(args[1])) {
    const content = await fs.readFile(path.join(root, candidate), 'utf8')
    if (hash(content) !== args[1]) throw Error('Candidate differs from reviewed digest')
    await validate(root, JSON.parse(content))
    await fs.writeFile(path.join(root, successorConfig), content, { flag: 'wx' })
    console.log('Created new v2 config from the exact reviewed metadata candidate; v1 and scientific verdicts unchanged')
  } else if (!args.length || same(args, ['--check'])) {
    console.log(JSON.stringify(await preparePublicationResearchProvenance(root, { check: args.includes('--check') })))
  } else throw Error('Use --capture, --accept-reviewed-candidate SHA256, or --check')
}
