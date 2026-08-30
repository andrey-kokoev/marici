import { readFile } from 'node:fs/promises'

const file = process.argv[2]
if (!file) throw new Error('Usage: node scripts/check-frontier-snapshot.mjs <snapshot.json>')
const snapshot = JSON.parse(await readFile(file, 'utf8'))
const statuses = new Set(['established', 'partial', 'open', 'falsified', 'not_applicable'])
const partialReasons = new Set(['typed_not_constructed', 'constructed_not_verified', 'verified_limited_scope', 'blocked_missing_source_input'])
const stages = ['carrier', 'lens_family', 'source_selector', 'selected_point', 'physical_readout']
const selectorMaturities = new Set(['untyped', 'typed', 'constructed', 'constructed_verified'])
const owners = new Set(['marici.Nima', 'marici.Benincasa', 'marici.Figueiredo', 'marici.Strominger', 'marici.Grothendieck'])
const assert = (condition, message) => { if (!condition) throw new Error(message) }

assert(snapshot.schema === 'marici.frontier-progress-snapshot.v1', 'Unsupported snapshot schema')
assert(snapshot.review_status === 'pending_scientific_review' || snapshot.review_status === 'reviewed' || snapshot.review_status === 'rejected', 'Invalid review status')
assert(JSON.stringify(snapshot.authority_pipeline) === JSON.stringify(['epistemic_graph', 'reviewed_frontier_snapshot', 'versioned_ui']), 'Invalid authority pipeline')
assert(snapshot.prepared_by === 'marketing', 'Snapshot implementation owner must be marketing')
assert(JSON.stringify(snapshot.stages.map((stage) => stage.id)) === JSON.stringify(stages), 'Pipeline stages are not canonical')
for (const sector of snapshot.sectors) {
  assert(owners.has(sector.cells.carrier.review_owner), `Invalid review owner for ${sector.id}`)
  for (const stage of stages) {
    const cell = sector.cells[stage]
    assert(cell && statuses.has(cell.status), `Invalid status at ${sector.id}/${stage}`)
    assert(cell.changed_in_version === snapshot.version, `Invalid changed_in_version at ${sector.id}/${stage}`)
    assert(typeof cell.what_remains === 'string' && cell.what_remains.trim(), `Missing what_remains at ${sector.id}/${stage}`)
    assert(Array.isArray(cell.status_basis), `Missing status_basis at ${sector.id}/${stage}`)
    assert(owners.has(cell.review_owner), `Invalid review_owner at ${sector.id}/${stage}`)
    if (cell.status === 'partial') assert(partialReasons.has(cell.partial_reason), `Missing typed partial_reason at ${sector.id}/${stage}`)
    else assert(cell.partial_reason === null, `partial_reason must be null for non-partial cell ${sector.id}/${stage}`)
    if (stage === 'source_selector') assert(selectorMaturities.has(cell.selector_maturity), `Missing selector maturity at ${sector.id}`)
    for (const basis of cell.status_basis) {
      assert(basis.authority_type === 'epistemic_entity' || basis.authority_type === 'ledger_entry', `Invalid basis type at ${sector.id}/${stage}`)
      assert(typeof basis.ref === 'string' && basis.ref.trim(), `Invalid basis ref at ${sector.id}/${stage}`)
    }
    if (snapshot.review_status === 'reviewed' && cell.status_basis.length === 0) {
      const operatorException = snapshot.review_records.some((record) =>
        record.decision === 'approved' &&
        record.review_owner === 'operator' &&
        record.sector === 'all' &&
        record.authority === 'explicit_operator_instruction'
      )
      assert(operatorException, `Reviewed cell lacks admitted basis at ${sector.id}/${stage}`)
    }
  }
}
if (snapshot.review_status === 'reviewed') {
  const approved = new Set(snapshot.review_records.filter((record) => record.decision === 'approved').map((record) => record.review_owner + ':' + record.sector))
  const operatorApprovedAll = approved.has('operator:all')
  for (const requirement of snapshot.review_requirements) assert(operatorApprovedAll || approved.has(requirement.review_owner + ':' + requirement.sector), `Missing approval from ${requirement.review_owner} for ${requirement.sector}`)
}
console.log(`Frontier snapshot OK: v${snapshot.version} · ${snapshot.review_status} · ${snapshot.sectors.length} sectors`)
