import { readdir, readFile, writeFile } from 'node:fs/promises'
import { resolve } from 'node:path'

const ledgerRoot = resolve(process.argv[2] ?? '.narada/epistemic/ledger')
const outputPath = resolve(process.argv[3] ?? '.ai/tmp/epistemic-graph-snapshot.json')
const names = (await readdir(ledgerRoot)).filter((name) => /^ev-\d{12}-[0-9a-f-]+\.json$/.test(name)).sort()
const entities = new Map()
const relations = new Map()
let ledgerHead = null

for (const name of names) {
  const event = JSON.parse(await readFile(resolve(ledgerRoot, name), 'utf8'))
  for (const operation of event.operations ?? []) {
    if (operation.op === 'entity.declare') {
      // Read receipts are operational mailbox state, not public epistemic entities.
      if (operation.kind === 'narada.epistemic:message_read') continue
      const entityId = String(operation.entity_id)
      entities.set(entityId, {
        entity_id: entityId,
        kind: String(operation.kind),
        title: String(operation.title ?? entityId),
        payload: { ...operation },
        event_id: String(event.event_id),
      })
    } else if (operation.op === 'entity.kind_canonicalize') {
      const entity = entities.get(String(operation.entity_id))
      if (entity) {
        entity.kind = String(operation.canonical_kind)
        entity.payload.kind = String(operation.canonical_kind)
      }
    } else if (operation.op === 'relation.declare') {
      const relationId = String(operation.relation_id)
      relations.set(relationId, {
        relation_id: relationId,
        relation_type: String(operation.relation_type),
        source_id: String(operation.source_id),
        target_id: String(operation.target_id),
        payload: { ...operation },
        event_id: String(event.event_id),
      })
    }
  }
  ledgerHead = event.event_hash
}

const snapshot = {
  schema: 'narada.epistemic.graph_snapshot.v1',
  status: 'ok',
  ledger_head: ledgerHead,
  entity_count: entities.size,
  relation_count: relations.size,
  entities: [...entities.values()],
  relations: [...relations.values()],
  entity_offset: 0,
  relation_offset: 0,
  next_entity_offset: null,
  next_relation_offset: null,
  limit: Math.max(entities.size, relations.size),
  bounded: false,
}
await writeFile(outputPath, JSON.stringify(snapshot) + '\n')
console.log(JSON.stringify({ output: outputPath, ledger_head: ledgerHead, entity_count: entities.size, relation_count: relations.size }))
