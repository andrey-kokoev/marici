import { readFile } from 'node:fs/promises'

const path = process.argv[2] ?? 'src/data/epistemic-graph.json'
const graph = JSON.parse(await readFile(path, 'utf8'))
const assert = (condition, message) => { if (!condition) throw new Error(message) }

assert(graph.schema === 'marici.public-epistemic-graph.v2', 'Unsupported public graph schema')
assert(/^[0-9a-f]{64}$/.test(graph.ledger_head), 'Invalid ledger head')
assert(graph.entity_count === graph.entities.length, 'Entity count mismatch')
assert(graph.relation_count === graph.relations.length, 'Relation count mismatch')

const entityIds = new Set(graph.entities.map((entity) => entity.entity_id))
const relationIds = new Set(graph.relations.map((relation) => relation.relation_id))
assert(entityIds.size === graph.entities.length, 'Duplicate public entity id')
assert(relationIds.size === graph.relations.length, 'Duplicate public relation id')
assert(!graph.entities.some((entity) => entity.kind === 'narada.epistemic:message_read'), 'Mailbox read receipts leaked into public graph')

for (const entity of graph.entities) {
  assert(typeof entity.kind === 'string' && entity.kind, `Missing kind for ${entity.entity_id}`)
  assert(typeof entity.title === 'string' && entity.title, `Missing title for ${entity.entity_id}`)
  assert(Number.isInteger(entity.temporal?.event_sequence), `Missing temporal sequence for ${entity.entity_id}`)
}
for (const relation of graph.relations) {
  assert(entityIds.has(relation.source_id), `Unknown relation source ${relation.source_id}`)
  assert(entityIds.has(relation.target_id), `Unknown relation target ${relation.target_id}`)
  assert(Number.isInteger(relation.temporal?.event_sequence), `Missing temporal sequence for ${relation.relation_id}`)
}

console.log(`Public epistemic graph OK: ${graph.entity_count} entities, ${graph.relation_count} relations at ${graph.ledger_head}`)
