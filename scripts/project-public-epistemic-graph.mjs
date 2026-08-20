import { readdir, readFile, writeFile } from 'node:fs/promises'
import { basename, resolve } from 'node:path'

function argument(name, fallback) {
  const index = process.argv.indexOf(name)
  return index >= 0 ? process.argv[index + 1] : fallback
}

const inputPath = resolve(argument('--input', '.ai/tmp/epistemic-graph-snapshot.json'))
const outputPath = resolve(argument('--output', 'src/data/epistemic-graph.json'))
const ledgerRoot = resolve(argument('--ledger-root', 'src/ledger'))

function slugFromLocator(locator) {
  if (typeof locator !== 'string' || !/^src[\\/]ledger[\\/].+\.md$/i.test(locator)) return null
  const filename = basename(locator).replace(/\.md$/i, '')
  const match = filename.match(/^(\d{8})-(\d+)[ _-](.+)$/)
  if (!match) return null
  return `${match[1]}-${match[2]}-${match[3]}`
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
}

function frontmatterAuthors(markdown, title) {
  const block = markdown.match(/^---\s*\r?\n([\s\S]*?)\r?\n---/)
  const authors = []
  if (block) {
    const single = block[1].match(/^author:\s*(marici\.(?:Nima|Benincasa))\s*$/m)
    if (single) authors.push(single[1])
    const list = block[1].match(/^authors:\s*\r?\n((?:\s+-\s+.+\r?\n?)*)/m)
    if (list) {
      for (const match of list[1].matchAll(/^\s+-\s+(marici\.(?:Nima|Benincasa))\s*$/gm)) authors.push(match[1])
    }
  }
  if (authors.length) return [...new Set(authors)]
  return /\bcosmolog(?:y|ical|ies)\b/i.test(title) ? ['marici.Benincasa'] : ['marici.Nima']
}

async function publicProvenance(payload) {
  const slug = slugFromLocator(payload.locator)
  if (!slug) return payload.version ? { version: String(payload.version) } : undefined
  const ledgerPath = resolve(ledgerRoot, basename(payload.locator))
  let markdown = ''
  try {
    markdown = await readFile(ledgerPath, 'utf8')
  } catch {
    return payload.version ? { version: String(payload.version) } : undefined
  }
  const match = basename(payload.locator).match(/^(\d{8})-(\d+)/)
  const title = markdown.match(/^#\s+(.+)$/m)?.[1]?.trim() || payload.title
  const dateKey = match?.[1]
  return {
    version: payload.version ? String(payload.version) : undefined,
    ledger_entry: match ? Number(match[2]) : undefined,
    href: `/ledger/${slug}/`,
    authors: frontmatterAuthors(markdown, title),
    published_at: dateKey ? `${dateKey.slice(0, 4)}-${dateKey.slice(4, 6)}-${dateKey.slice(6, 8)}` : undefined,
  }
}

const input = JSON.parse(await readFile(inputPath, 'utf8'))
const snapshot = input.structuredContent ?? input
if (snapshot.schema !== 'narada.epistemic.graph_snapshot.v1') {
  throw new Error(`Expected narada.epistemic.graph_snapshot.v1, received ${snapshot.schema ?? 'unknown'}`)
}

const ledgerEntries = (await readdir(ledgerRoot))
  .map((filename) => filename.match(/^(\d{8})-(\d+).+\.md$/i))
  .filter(Boolean)
  .map((match) => ({
    entry: Number(match[2]),
    date: `${match[1].slice(0, 4)}-${match[1].slice(4, 6)}-${match[1].slice(6, 8)}`,
  }))
  .sort((a, b) => a.entry - b.entry)

const entities = []
for (const entity of snapshot.entities ?? []) {
  const payload = entity.payload ?? {}
  const projected = {
    entity_id: String(entity.entity_id),
    kind: String(entity.kind),
    title: String(entity.title),
  }
  if (typeof payload.status === 'string' && payload.status.trim()) projected.status = payload.status.trim()
  if (typeof payload.summary === 'string' && payload.summary.trim()) projected.summary = payload.summary.trim()
  const provenance = await publicProvenance(payload)
  if (provenance) projected.provenance = Object.fromEntries(Object.entries(provenance).filter(([, value]) => value !== undefined))
  entities.push(projected)
}

const knownIds = new Set(entities.map((entity) => entity.entity_id))
const relations = (snapshot.relations ?? [])
  .filter((relation) => knownIds.has(relation.source_id) && knownIds.has(relation.target_id))
  .map(({ relation_id, relation_type, source_id, target_id, event_id }) => ({
    relation_id: String(relation_id),
    relation_type: String(relation_type),
    source_id: String(source_id),
    target_id: String(target_id),
    _event_id: event_id,
  }))

const projectedById = new Map(entities.map((entity) => [entity.entity_id, entity]))
const eventSequence = (eventId) => Number(String(eventId ?? '').match(/^ev-(\d+)/)?.[1])
const eventGroups = new Map()
for (const raw of snapshot.entities ?? []) {
  const sequence = eventSequence(raw.event_id)
  if (!Number.isFinite(sequence)) continue
  const group = eventGroups.get(sequence) ?? { entries: [], dates: [] }
  const projected = projectedById.get(raw.entity_id)
  if (projected?.provenance?.ledger_entry) {
    group.entries.push(projected.provenance.ledger_entry)
    if (projected.provenance.published_at) group.dates.push(projected.provenance.published_at)
  }
  eventGroups.set(sequence, group)
}
for (const raw of snapshot.relations ?? []) {
  const sequence = eventSequence(raw.event_id)
  if (Number.isFinite(sequence) && !eventGroups.has(sequence)) eventGroups.set(sequence, { entries: [], dates: [] })
}
const eventSequences = [...eventGroups.keys()].sort((a, b) => a - b)
const anchoredSequences = eventSequences.filter((sequence) => eventGroups.get(sequence).entries.length)
function temporalForEvent(eventId) {
  const sequence = eventSequence(eventId)
  if (!Number.isFinite(sequence)) throw new Error(`Missing admission event sequence for ${eventId ?? 'unknown event'}`)
  const group = eventGroups.get(sequence) ?? { entries: [], dates: [] }
  const entries = [...new Set(group.entries)].sort((a, b) => a - b)
  if (entries.length) {
    const entryMin = entries[0]
    const entryMax = entries.at(-1)
    return {
      entry: entryMax,
      entry_min: entryMin,
      entry_max: entryMax,
      published_at: [...new Set(group.dates)].sort().at(-1),
      event_sequence: sequence,
      basis: entries.length === 1 ? 'admission_event' : 'admission_event_batch',
    }
  }
  const previous = [...anchoredSequences].reverse().find((candidate) => candidate < sequence)
  const next = anchoredSequences.find((candidate) => candidate > sequence)
  const lower = previous === undefined ? 1 : Math.max(...eventGroups.get(previous).entries) + 1
  const upper = next === undefined ? lower : Math.min(...eventGroups.get(next).entries)
  return {
    entry: upper,
    entry_min: Math.min(lower, upper),
    entry_max: upper,
    event_sequence: sequence,
    basis: 'admission_event_bounded',
  }
}
const rawEntityById = new Map((snapshot.entities ?? []).map((entity) => [entity.entity_id, entity]))
for (const entity of entities) {
  entity.temporal = temporalForEvent(rawEntityById.get(entity.entity_id)?.event_id)
}
for (const relation of relations) {
  relation.temporal = temporalForEvent(relation._event_id)
  delete relation._event_id
}

entities.sort((a, b) => a.kind.localeCompare(b.kind) || a.title.localeCompare(b.title) || a.entity_id.localeCompare(b.entity_id))
relations.sort((a, b) => a.relation_type.localeCompare(b.relation_type) || a.source_id.localeCompare(b.source_id) || a.target_id.localeCompare(b.target_id))

const output = {
  schema: 'marici.public-epistemic-graph.v2',
  ledger_head: String(snapshot.ledger_head),
  entity_count: entities.length,
  relation_count: relations.length,
  ledger_entries: ledgerEntries,
  entities,
  relations,
}

await writeFile(outputPath, JSON.stringify(output) + '\n', 'utf8')
console.log(`Projected ${entities.length} entities and ${relations.length} relations at ${output.ledger_head}`)
