import fs from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('../', import.meta.url))
const manifestPath = 'config/current-research-provenance.v1.json'
const targetPath = 'website/public/research/provenance/current-results.v1.json'
const sha256 = bytes => createHash('sha256').update(bytes).digest('hex')
const lf = text => text.replace(/\r\n?/g, '\n')
const digest = /^[a-f0-9]{64}$/
const safePath = value => typeof value === 'string' && /^(research|scripts|test-results)\/[A-Za-z0-9_./-]+$/.test(value) && !value.split('/').some(part => !part || part === '.' || part === '..')

// Selection is editorial and bounded. These are immediate packets/entry points
// and selected historical receipts, never a claim of full dependency closure.
const selections = [
  ['witness-continuation-admission', ['research/voevodsky/witness-generator-coherence-v1.md'], ['research/voevodsky/results/witness-generator-coherence-v1.json'], 'Source-relative continuation; atomic admission excluded; retained envelope admitted.'],
  ['su32-native-record-comparisons', ['research/strominger/native-shared-reader-join-v1.md', 'research/strominger/su32-record-reader-classification-v1.md', 'research/strominger/su32-release-source-audit-v1.md'], ['research/strominger/results/su32-record-reader-classification-v1/verification.json', 'research/strominger/results/su32-release-source-audit-v1/verification.json'], 'Boolean current-value classification, not original release or physical signal execution.'],
  ['ramsey-history-covariant-readers', ['research/voevodsky/ramsey-covariant-EP-reader-v1.md'], ['research/voevodsky/results/ramsey-covariant-EP-reader-v1.json'], 'Coefficient theorem and finite live repair; complete semantic descent remains open.'],
  ['coherent-dependent-four-return', ['research/strominger/coherent-four-return-v1.md'], ['research/strominger/results/coherent-four-return-v1/agda.json', 'research/strominger/results/coherent-four-return-v1/verification.json'], 'Coherent action on a possibly empty dependent return fibre, not a selected native successor.'],
  ['cellulation-order-and-source-roles', ['research/realization-tower/cellulation-shell-order-audit.md', 'research/realization-tower/cellulation-shell-exhaustive-verification.md', 'research/strominger/cellulation-dot-422-compatibility.md'], ['test-results/cellulation-shell-exhaustive-report.json', 'research/strominger/results/cellulation-dot-422-compatibility.json'], 'Local nonconfluence of the weaker model; global search incomplete; strict role patch blocked.'],
  ['su32-comparison-content-and-operations', ['research/strominger/su32-comparison-license-v1.md', 'research/strominger/su32-static-payload-identification-v1.md', 'research/strominger/su32-boundary-composition-span-v1.md'], ['research/strominger/results/su32-comparison-license-v1/verification.json', 'research/strominger/results/su32-static-payload-identification-v1/verification.json', 'research/strominger/results/su32-boundary-composition-span-v1/verification.json'], 'Transported preparation, rejected static identification and finite operation span remain distinct.'],
  ['analytical-native-two-route-pilot', ['research/aspect/analytical-two-route-pilot.md'], ['research/aspect/results/analytical-two-route-pilot.json'], 'Zero native defect, negative chosen analytical residual, absent intended analytical witness.'],
  ['conditional-optical-control-integration', ['research/sontag/owner-integration-delta-v1.md', 'research/sontag/conditional-statistical-optical-binding-v1.md'], ['research/sontag/results/owner-integration-delta-v1.json', 'research/sontag/results/optical-binding-assembly-v1.json'], 'Conditional statistical model; integration unapplied and empirical apparatus deferred.'],
  ['local-contour-covariance-closure', ['research/benincasa/history6-current-closure-2026-10-13.md'], ['research/benincasa/results/history6_current_closure.json'], 'Local construction closure, not source-selected physical contour or global completion.'],
  ['atom-retained-source-transport', ['research/kitaev/atom-transport-as-a-retained-source-route-v1.md'], ['research/kitaev/results/atom-retained-transport-ancestry-v1.json'], 'Actual chart/history transport; unrestricted coefficient skeleton is not physical gauge selection.'],
]

async function pinText(base, file) {
  if (!safePath(file)) throw Error('Unsafe provenance source path: ' + file)
  return { path: file, text_sha256: sha256(lf(await fs.readFile(path.join(base, file), 'utf8'))) }
}

export async function captureCurrentResearchProvenance(base = root) {
  const inventory = JSON.parse(await fs.readFile(path.join(base, 'src/data/results-physics.json'), 'utf8'))
  const entries = []
  for (const [slug, packets, receipts, boundary] of selections) {
    const matches = inventory.filter(item => item.slug === slug)
    if (matches.length !== 1) throw Error('Missing/duplicate selected result: ' + slug)
    const item = matches[0]
    const historical = []
    for (const file of receipts) {
      if (!safePath(file)) throw Error('Unsafe historical receipt path')
      const bytes = await fs.readFile(path.join(base, file))
      const data = JSON.parse(bytes.toString('utf8').replace(/^\uFEFF/, ''))
      const compiler = data.compiler_sha256 ?? data.source_inventory?.compiler
      const recordedCompiler = {}
      if (digest.test(compiler)) recordedCompiler.executable_sha256 = compiler
      if (typeof data.compiler_version === 'string') recordedCompiler.version = data.compiler_version.split(/\r?\n/)[0].slice(0, 160)
      historical.push({ path: file, sha256: sha256(bytes), bytes: bytes.length, ...(Object.keys(recordedCompiler).length ? { recorded_compiler: recordedCompiler } : {}) })
    }
    entries.push({
      slug,
      reported_status: item.status,
      boundary,
      source_packets: await Promise.all(packets.map(file => pinText(base, file))),
      checker_sources: await Promise.all(item.checker.split('; ').map(file => pinText(base, file))),
      historical_receipts: historical,
    })
  }
  return {
    schema: 'marici.public-research-provenance.v1',
    snapshot_id: 'current-results-publication-v1',
    captured_at: new Date().toISOString(),
    capture_clock: 'Host UTC wall clock; not a scientific execution or independently verified calendar date',
    capture_kind: 'File metadata only; no scientific execution',
    scientific_replay_performed: false,
    scientific_verdicts_modified: false,
    receipt_source_compatibility: 'not revalidated',
    transitive_dependency_closure: 'not claimed',
    text_hash_basis: 'SHA-256 of UTF-8 text with CRLF/CR normalized to LF; BOM preserved',
    receipt_hash_basis: 'SHA-256 of exact historical receipt bytes; payloads not published',
    reproduction: 'Follow the owning source packet invocation and declared environment/toolchain. Checker source digests identify scripts, not unrecorded runtime/compiler binaries. Recorded compiler metadata is copied from historical receipts, not rechecked.',
    entries,
  }
}

export async function prepareCurrentResearchProvenance(base = root, { check = false } = {}) {
  const manifest = JSON.parse(await fs.readFile(path.join(base, manifestPath), 'utf8'))
  if (manifest.schema !== 'marici.public-research-provenance.v1' || manifest.snapshot_id !== 'current-results-publication-v1' || manifest.scientific_replay_performed !== false || manifest.scientific_verdicts_modified !== false || manifest.receipt_source_compatibility !== 'not revalidated' || manifest.transitive_dependency_closure !== 'not claimed') throw Error('Unsupported or overstated publication provenance')
  const inventory = JSON.parse(await fs.readFile(path.join(base, 'src/data/results-physics.json'), 'utf8'))
  const slugs = new Set()
  for (const entry of manifest.entries) {
    if (slugs.has(entry.slug)) throw Error('Duplicate provenance result: ' + entry.slug)
    slugs.add(entry.slug)
    const result = inventory.find(item => item.slug === entry.slug)
    if (!result || result.status !== entry.reported_status || !entry.boundary) throw Error('Stale or missing provenance result: ' + entry.slug)
    if (!entry.source_packets.length || !entry.checker_sources.length || !entry.historical_receipts.length) throw Error('Incomplete provenance entry: ' + entry.slug)
    for (const pin of [...entry.source_packets, ...entry.checker_sources]) {
      if (!safePath(pin.path) || !digest.test(pin.text_sha256)) throw Error('Invalid provenance source pin')
      const actual = await pinText(base, pin.path)
      if (actual.text_sha256 !== pin.text_sha256) throw Error('Stale publication provenance source: ' + pin.path + '; review a successor snapshot, not an automatic scientific replay')
    }
    if (entry.checker_sources.map(pin => pin.path).join('; ') !== result.checker) throw Error('Checker selection drift: ' + entry.slug)
    for (const receipt of entry.historical_receipts) {
      if (!safePath(receipt.path) || !digest.test(receipt.sha256) || !Number.isSafeInteger(receipt.bytes) || receipt.bytes <= 0) throw Error('Invalid historical receipt identifier')
      // Do not read or require ignored local receipts during publication. These
      // identifiers freeze historical bytes; they are not fresh evidence claims.
    }
  }
  if (!slugs.size) throw Error('Empty provenance coverage')
  const content = JSON.stringify(manifest, null, 2) + '\n'
  if (Buffer.byteLength(content) > 65536) throw Error('Provenance metadata exceeds compact publication budget')
  const output = path.join(base, targetPath)
  if (check) {
    if (await fs.readFile(output, 'utf8').catch(() => null) !== content) throw Error('Stale public provenance copy')
  } else {
    await fs.mkdir(path.dirname(output), { recursive: true })
    await fs.writeFile(output, content)
  }
  return { snapshot_id: manifest.snapshot_id, slugs: [...slugs], sha256: sha256(content), bytes: Buffer.byteLength(content), target: targetPath }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  if (process.argv.includes('--capture')) {
    const candidate = await captureCurrentResearchProvenance(root)
    const output = path.join(root, '.ai/current-results-provenance-candidate.json')
    await fs.mkdir(path.dirname(output), { recursive: true })
    await fs.writeFile(output, JSON.stringify(candidate, null, 2) + '\n')
    console.log('Metadata-only candidate written to .ai/current-results-provenance-candidate.json; review before creating a versioned config. No source, receipt or verdict was changed.')
  } else {
    console.log(JSON.stringify(await prepareCurrentResearchProvenance(root, { check: process.argv.includes('--check') })))
  }
}
