// Publication adapter only. Never executes scientific suppliers or mutates their receipts.
import fs from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { inflateRawSync } from 'node:zlib'
const sha = bytes => createHash('sha256').update(bytes).digest('hex')

// Read only named members from the retained ZIP. No extraction paths or executables.
export function zipMembers(bytes) {
  let end = bytes.length - 22
  while (end >= Math.max(0, bytes.length - 65557) && bytes.readUInt32LE(end) !== 0x06054b50) end--
  if (end < 0 || bytes.readUInt32LE(end) !== 0x06054b50) throw new Error('Missing ZIP directory')
  const result = new Map(); let cursor = bytes.readUInt32LE(end + 16)
  for (let i = 0; i < bytes.readUInt16LE(end + 10); i++) {
    if (bytes.readUInt32LE(cursor) !== 0x02014b50) throw new Error('Invalid ZIP directory')
    const method = bytes.readUInt16LE(cursor + 10), size = bytes.readUInt32LE(cursor + 20), plain = bytes.readUInt32LE(cursor + 24)
    const n = bytes.readUInt16LE(cursor + 28), extra = bytes.readUInt16LE(cursor + 30), comment = bytes.readUInt16LE(cursor + 32), offset = bytes.readUInt32LE(cursor + 42)
    const name = bytes.subarray(cursor + 46, cursor + 46 + n).toString('utf8')
    result.set(name, () => {
      if (bytes.readUInt32LE(offset) !== 0x04034b50) throw new Error('Invalid ZIP member')
      const start = offset + 30 + bytes.readUInt16LE(offset + 26) + bytes.readUInt16LE(offset + 28)
      const packed = bytes.subarray(start, start + size)
      const data = method === 0 ? packed : method === 8 ? inflateRawSync(packed, { maxOutputLength: 30000000 }) : null
      if (!data || data.length !== plain) throw new Error(`Unsupported or corrupt ZIP member: ${name}`)
      return data
    })
    cursor += 46 + n + extra + comment
  }
  return result
}

export async function prepareResearchLab(root, out) {
  const target = path.join(out, 'research-lab'); await fs.mkdir(target, { recursive: true })
  const manifest = { scope: 'Publication snapshot, not new scientific verification or physical acceptance.', files: {}, dependencies: {} }
  async function pin(file, expected) {
    const bytes = await fs.readFile(path.join(root, file)), digest = sha(bytes)
    if (expected && digest !== expected) throw new Error(`Research lab: stale evidence ${file}; refresh the owning receipt, not its hash`)
    manifest.dependencies[file] = digest; return bytes
  }
  async function record(key, file, aliases = {}, inputBase = 'research/') {
    const bytes = await pin(file), data = JSON.parse(bytes)
    if (!(data.status === 'passed' || data.verification_status === 'pass' || data.passed === true)) throw new Error(`Research lab: failed receipt ${file}`)
    if (data.verification_passed === false || (data.passed !== true && data.verification_passed !== true && (!data.checks || !Object.values(data.checks).length || !Object.values(data.checks).every(Boolean)))) throw new Error(`Research lab: failed/empty checks ${file}`)
    for (const [dependency, expected] of Object.entries(data.source_hashes || {})) {
      if (dependency === 'archived_phase_receipt') continue // Verified below inside its retained archive.
      await pin(aliases[dependency] || dependency, expected)
    }
    for (const [dependency, expected] of Object.entries(data.inputs_sha256 || {})) await pin(inputBase + dependency, expected)
    await fs.writeFile(path.join(target, `${key}.json`), bytes)
    manifest.files[key] = { source: file, sha256: sha(bytes), checks: data.checks ? Object.values(data.checks).length : null }
    return data
  }
  const symmetry = await record('symmetry', 'research/strominger/results/arrow-symmetry-viewer.json')
  let viewer = (await pin('research/strominger/arrow-symmetry-viewer.html')).toString('utf8')
  viewer = viewer.replace('<aside>', '<aside><p><a href="/experiments/" style="color:#8de7ff">← Construction gallery</a> · <a href="/experiments/research-lab/symmetry.json" style="color:#8de7ff">Source receipt</a></p>')
  await fs.writeFile(path.join(out, 'arrow-symmetry-viewer.html'), '<!-- Generated publication copy; edit research/strominger/arrow-symmetry-viewer.html. -->\n' + viewer)
  await record('arrow', 'research/strominger/results/arrow-anchored-response.json')
  await record('link', 'research/voevodsky/results/proton-electron-single-link-potential-v1.json')
  await record('proton-tasks', 'research/voevodsky/results/proton-native-task-catalogue-v1.json')
  await record('tasks', 'research/voevodsky/results/neutron-native-relationship-tasks-v1.json')
  await record('reference', 'research/strominger/results/retained-reference-protocol.json')
  await record('branches', 'research/nima/results/branch-response-summary.json', {}, 'research/nima/checkers/')
  const t9 = await record('t9', 'research/nima/results/pinned-T9-software-contract.json', {}, 'research/nima/checkers/')
  await pin('research/nima/contracts/T9-exact-domain-software.v1.json', t9.contract_sha256)
  await pin('research/nima/checkers/check_rung_transport_diagram.py')
  for (const [name, digest] of Object.entries(t9.formal_receipts_sha256)) {
    const receipt = JSON.parse(await pin(`research/nima/results/agda-${name}.json`, digest))
    if (!receipt.passed || !receipt.ignore_interfaces || !receipt.inputs_stable_during_check) throw new Error(`Research lab: invalid formal receipt ${name}`)
    await pin(`research/nima/agda/${name}.agda`, receipt.owner_source_inventory_sha256[`${name}.agda`])
  }
  await record('binding', 'research/strominger/results/reference-port-binding.json')
  const clock = await record('clock', 'research/strominger/results/assembly-generated-clock.json', {
    checker: 'research/strominger/checkers/check_assembly_generated_clock.py',
    matrix_helpers: 'research/strominger/checkers/check_native_relational_clock.py',
  })
  const contact = zipMembers(await pin('research/scattering/high-energy/pentachoron_connected_phase_energy_bundle.zip'))
  const archived = 'pentachoron_connected_phase_energy_results.json'
  if (!archived || sha(contact.get(archived)()) !== clock.source_hashes.archived_phase_receipt) throw new Error('Research lab: archived clock receipt mismatch')
  await record('physical-neutron', 'research/strominger/results/physical-neutron-rest-energy.json')
  await record('neutron-rest', 'research/strominger/results/neutron-rest-energy-completion.json')
  await record('binding-law', 'research/voevodsky/results/source-gauss-to-coulomb-binding-v1.json')
  const archive = 'research/scattering/high-energy/pentachoron_matched_spatial_refinement_bundle.zip'
  const members = zipMembers(await pin(archive)), hashes = JSON.parse(members.get('MANIFEST.sha256.json')())
  const summaryBytes = members.get('matched_spatial_summary.json')()
  // The archive uses a path -> digest manifest; fail closed if its format changes.
  if (sha(summaryBytes) !== hashes['matched_spatial_summary.json']) throw new Error('Research lab: spatial summary hash mismatch')
  for (const [name, digest] of Object.entries(hashes)) {
    if (!members.has(name) || sha(members.get(name)()) !== digest) throw new Error(`Research lab: spatial archive member mismatch ${name}`)
  }
  const spatial = JSON.parse(summaryBytes)
  if (spatial.rows.length !== 4 || !spatial.checks.every(v => v.all_raw_checks_pass && v.independent_direct_iterative.passed)) throw new Error('Research lab: failed spatial audits')
  await fs.writeFile(path.join(target, 'spatial.json'), summaryBytes)
  manifest.files.spatial = { source: archive + '#matched_spatial_summary.json', sha256: sha(summaryBytes), archive_sha256: manifest.dependencies[archive] }
  // Explicit selections reduce initial download; full receipts stay available separately.
  const data = {}
  for (const key of ['arrow', 'link', 'tasks', 'proton-tasks', 'reference', 'branches', 't9', 'binding', 'clock', 'spatial']) data[key] = JSON.parse(await fs.readFile(path.join(target, `${key}.json`), 'utf8'))
  data.clock = { ...data.clock, phase_clock_operator: undefined, existing_contact_operator: undefined, actual_initial_density: data.clock.actual_initial_density.map((row, i) => row[i].real), cases: data.clock.cases.map(({ full_density, ...rest }) => rest) }
  data.tasks = { stage_supports: data.tasks.stage_supports, projector_ranks: data.tasks.projector_ranks, diagnostic_dimensions: data.tasks.diagnostic_dimensions, proton_comparison: data.tasks.proton_comparison, minimum_addresses: data.tasks.observation_theorem.minimum_addresses, rim_probe: { full_input_rank: data.tasks.rim_probe.full_input_rank, locally_admitted_rank: data.tasks.rim_probe.locally_admitted_rank }, observation_formula: data.tasks.observation_theorem.formula }
  data['proton-tasks'] = { rank_formula: data['proton-tasks'].all_mask_theorem.rank_formula, minimum_addresses: data['proton-tasks'].all_mask_theorem.minimum_addresses }
  data.link = data.link.link
  const payload = Buffer.from(JSON.stringify(data))
  await fs.writeFile(path.join(target, 'data.json'), payload)
  manifest.files.data = { sha256: sha(payload), scope: 'Selected fields of the pinned receipts; no scientific values invented.' }
  await fs.copyFile(path.join(root, 'papers/witness-generators/research-lab.html'), path.join(out, 'research-lab.html'))
  await fs.copyFile(path.join(root, 'papers/witness-generators/research-lab.mjs'), path.join(out, 'research-lab.mjs'))
  // Detect concurrent changes before publishing the snapshot manifest.
  for (const [file, digest] of Object.entries(manifest.dependencies)) if (sha(await fs.readFile(path.join(root, file))) !== digest) throw new Error(`Research lab: source changed during publication ${file}`)
  await fs.writeFile(path.join(target, 'manifest.json'), JSON.stringify(manifest, null, 2) + '\n')
}
