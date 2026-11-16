import { createDiagram } from './finite-diagrams.mjs';
import { isotopeSupportSchema } from './schemas.mjs';
import { attributeDiagram, canonicalJSON, deepFreeze, jsonClone } from './attributed-diagrams.mjs';

const packets = new WeakSet();
const collections = ['shells', 'cells', 'pairs', 'witnesses'];
const offsets = { T: [0, -1], R: [1, 0], B: [0, 1], L: [-1, 0] };
const key = (kind, ...parts) => `${kind}:${JSON.stringify(parts)}`;
const ensure = (condition, message) => { if (!condition) throw Error(message); };
const safeId = x => typeof x === 'string' && x.length > 0 && !['__proto__', 'prototype', 'constructor'].includes(x);

export const legacyLatticePolicy = deepFreeze({
  id: 'isotope-wiring.legacy-shell-lattice.v1',
  vertexIdentity: 'shell ID and exact integer lattice pair',
  directedEdgeIdentity: 'ordered vertex pair',
  supportIdentity: 'unordered vertex pair',
  crossShellIdentification: 'never implicit; requires a separate explicit interface',
  boundaryMeaning: 'named shell frame, not a certified closed geometric cycle',
});

// Input must already be an absolute definition. No mutable registry lookup,
// drawing evaluation, coordinate rounding, or silent inference of delta bases.
export function importLegacyAbsolute(input) {
  const source = jsonClone(input);
  ensure(source && typeof source === 'object' && !Array.isArray(source) && source.kind === 'absolute', 'Adapter requires an absolute definition');
  ensure(safeId(source.id), 'Invalid definition ID');
  ensure(source.graph && typeof source.graph === 'object' && !Array.isArray(source.graph), 'Missing legacy graph');
  for (const collection of collections) {
    const records = source.graph[collection]; ensure(Array.isArray(records), `Missing collection: ${collection}`);
    const ids = new Set();
    for (const record of records) {
      ensure(record && typeof record === 'object' && !Array.isArray(record) && safeId(record.id), `Invalid ${collection} record ID`);
      ensure(!ids.has(record.id), `Duplicate ${collection} ID: ${record.id}`); ids.add(record.id);
    }
  }
  const schema = isotopeSupportSchema;
  const sets = Object.fromEntries(schema.sorts.map(s => [s, []]));
  const maps = Object.fromEntries(schema.arrows.map(a => [a.name, {}]));
  const labels = Object.fromEntries(schema.sorts.map(s => [s, {}]));
  const add = (sort, id, attrs = {}) => {
    if (!Object.hasOwn(labels[sort], id)) { sets[sort].push(id); labels[sort][id] = attrs; }
    else ensure(canonicalJSON(labels[sort][id]) === canonicalJSON(attrs), `Ambiguous attributes: ${sort}:${id}`);
    return id;
  };
  const shellById = new Map(source.graph.shells.map(s => [s.id, s]));
  const cells = new Map(source.graph.cells.map(c => [c.id, c]));
  const shellOrders = new Set(), positions = new Set();
  for (const s of shellById.values()) {
    ensure(Number.isSafeInteger(s.order) && s.order >= 1 && !shellOrders.has(s.order), 'Invalid or duplicate shell order');
    ensure(Number.isSafeInteger(s.size) && s.size >= 1 && s.size <= 20, 'Shell size outside declared legacy domain 1..20');
    shellOrders.add(s.order); add('shell', s.id, { order: s.order, size: s.size });
  }
  for (const c of cells.values()) {
    const s = shellById.get(c.shell), position = key('position', c.shell, c.row, c.col);
    ensure(s && Number.isSafeInteger(c.row) && Number.isSafeInteger(c.col) && c.row >= 0 && c.col >= 0 && c.row < s.size && c.col < s.size, `Invalid cell coordinates/ownership: ${c.id}`);
    ensure(!positions.has(position), `Ambiguous overlapping cells: ${c.id}`); positions.add(position);
    add('cell', c.id, { row: c.row, col: c.col }); maps.cellShell[c.id] = c.shell;
    for (const [role, [dx, dy]] of Object.entries(offsets)) {
      const lattice = [c.col - c.row + dx, c.row + c.col + 1 + dy];
      const vertex = add('vertex', key('vertex', c.shell, ...lattice), { frame: c.shell, lattice });
      const port = add('port', key('port', c.id, role), { role });
      maps.portCell[port] = c.id; maps.portVertex[port] = vertex;
    }
  }
  function route(cellId, ports) {
    ensure(cells.has(cellId) && Array.isArray(ports) && ports.length === 2 && ports.every(p => Object.hasOwn(offsets, p)), `Invalid route in ${cellId}`);
    const [start, end] = ports.map(p => key('port', cellId, p));
    const [s, t] = [start, end].map(p => maps.portVertex[p]);
    const endpoints = [s, t].sort();
    const support = add('support', key('support', ...endpoints), {
      kind: 'undirected-lattice-support', endpoints: endpoints.map(v => labels.vertex[v]),
    });
    const edge = add('edge', key('edge', s, t));
    maps.source[edge] = s; maps.target[edge] = t; maps.edgeSupport[edge] = support;
    return { start, end, edge };
  }
  for (const p of source.graph.pairs) {
    ensure(cells.has(p.cell) && cells.get(p.cell).shell === p.shell, `Pair ownership mismatch: ${p.id}`);
    add('pair', p.id); maps.pairCell[p.id] = p.cell;
    for (const color of ['red', 'blue']) {
      const r = route(p.cell, p[color]);
      maps[`${color}Edge`][p.id] = r.edge; maps[`${color}Start`][p.id] = r.start; maps[`${color}End`][p.id] = r.end;
    }
  }
  for (const w of source.graph.witnesses) {
    ensure(shellById.has(w.shell), `Witness has no shell: ${w.id}`);
    if (w.kind === 'line') {
      ensure(cells.has(w.cell) && cells.get(w.cell).shell === w.shell && ['H', 'V'].includes(w.axis), `Invalid line witness: ${w.id}`);
      add('lineWitness', w.id, { axis: w.axis }); maps.lineCell[w.id] = w.cell;
      const r = route(w.cell, w.axis === 'H' ? ['L', 'R'] : ['T', 'B']);
      maps.lineEdge[w.id] = r.edge; maps.lineStart[w.id] = r.start; maps.lineEnd[w.id] = r.end;
    } else {
      ensure(w.kind === 'boundary', `Unknown witness kind: ${w.kind}`);
      const boundary = add('boundary', key('boundary', w.shell), { kind: 'shell-frame' });
      maps.boundaryShell[boundary] = w.shell;
      add('boundaryWitness', w.id); maps.witnessBoundary[w.id] = boundary; maps.boundaryWitnessShell[w.id] = w.shell;
    }
  }
  const object = attributeDiagram(createDiagram(schema, { sets, maps }), labels);
  const occurrenceMap = {
    shells: source.graph.shells.map(r => ({ legacyId: r.id, sort: 'shell', id: r.id })),
    cells: source.graph.cells.map(r => ({ legacyId: r.id, sort: 'cell', id: r.id })),
    pairs: source.graph.pairs.map(r => ({ legacyId: r.id, sort: 'pair', id: r.id })),
    witnesses: source.graph.witnesses.map(r => ({ legacyId: r.id, sort: r.kind === 'line' ? 'lineWitness' : 'boundaryWitness', id: r.id })),
  };
  const result = deepFreeze({
    format: 'isotope-wiring.legacy-adapter-packet.v1', object, policy: legacyLatticePolicy,
    // Retaining the complete source makes every extra field and order recoverable.
    // This is provenance, NOT a claim that bare incidence determines the source.
    retainedSource: source, occurrenceMap,
    modelContext: {
      sourceDefinitionId: source.id,
      targets: Object.fromEntries(['Z', 'N', 'expectedByShell'].filter(k => Object.hasOwn(source, k)).map(k => [k, source[k]])),
      status: 'supplied-not-derived',
    },
    report: {
      status: 'structurally-imported', omittedSourceFields: [], modelValidity: 'not-checked',
      retainedOnly: ['definition metadata and targets', 'per-record history and extra fields', 'collection order', 'extra graph fields'],
      interpretationChanges: ['Shared support is shell-local exact lattice incidence; cross-shell screen coincidence is not an identification.', 'Directed route edges and undirected support are distinct objects.', 'A boundary witness has named support, not a computed boundary-cycle certificate.'],
    },
  });
  packets.add(result); return result;
}

// Exact retained-source recovery, not inversion of the lossy incidence projection.
// Re-import an exported packet after persistence; forged/mutated envelopes are not accepted.
export function recoverLegacySource(packet) {
  ensure(packets.has(packet), 'Expected checked adapter packet');
  return jsonClone(packet.retainedSource);
}
