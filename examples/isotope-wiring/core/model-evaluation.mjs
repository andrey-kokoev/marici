import { equalAttributedObjects, canonicalJSON, jsonClone, deepFreeze } from './attributed-diagrams.mjs';
import { isotopeSupportSchema } from './schemas.mjs';

export const modelVersion = 'isotope-wiring.shell-lattice-model.v1';
const checkerVersion = 'isotope-wiring.model-predicates.v2';
const offsets = { T: [0, -1], R: [1, 0], B: [0, 1], L: [-1, 0] };
const own = (o, k) => Object.hasOwn(o, k);
const integer = (x, min = 0) => Number.isSafeInteger(x) && x >= min;
const fields = (x, names) => x && typeof x === 'object' && !Array.isArray(x)
  && canonicalJSON(Object.keys(x).sort()) === canonicalJSON([...names].sort());
const vertexLabel = x => fields(x, ['frame', 'lattice']) && typeof x.frame === 'string' && x.frame.length > 0
  && Array.isArray(x.lattice) && x.lattice.length === 2 && x.lattice.every(Number.isSafeInteger);
const unordered = xs => canonicalJSON(xs.map(canonicalJSON).sort());

// Whole collections include absence of records, not only observed IDs.
export const predicateReadContract = deepFreeze({
  version: 'isotope-wiring.predicate-reads.v1',
  predicates: {
    'attribute-types': { sets: '*', labels: '*', maps: [] },
    'lattice-incidence': { sets: ['shell', 'cell', 'port'], labels: ['shell', 'cell', 'port', 'vertex'], maps: ['cellShell', 'portCell', 'portVertex'] },
    'support-incidence': { sets: ['edge'], labels: ['vertex', 'support'], maps: ['source', 'target', 'edgeSupport'] },
    'pair-grammar': { sets: ['pair'], labels: ['port', 'shell'], maps: ['pairCell', 'cellShell', 'redStart', 'redEnd', 'blueStart', 'blueEnd'] },
    'witness-grammar': { sets: ['lineWitness', 'boundaryWitness'], labels: ['lineWitness', 'port'], maps: ['lineCell', 'lineStart', 'lineEnd', 'boundaryWitnessShell'] },
    'color-disjointness': { sets: ['pair'], labels: [], maps: ['edgeSupport', 'redEdge', 'blueEdge'] },
    'inventory-targets': { sets: ['shell', 'pair', 'lineWitness', 'boundaryWitness'], labels: ['shell'], maps: ['cellShell', 'pairCell'], targets: true },
  },
});
function readProjection(predicate, d, labels, context, dependencyStatuses) {
  const contract = predicateReadContract.predicates[predicate];
  if (!contract) throw Error('Predicate has no declared read projection');
  const pick = (values, keys) => keys === '*' ? values : Object.fromEntries(keys.map(k => [k, values[k] ?? null]));
  return canonicalJSON({ contractVersion: predicateReadContract.version, predicate, schema: d.schema,
    sets: pick(d.sets, contract.sets), labels: pick(labels, contract.labels), maps: pick(d.maps, contract.maps), dependencyStatuses,
    ...(contract.targets ? { targets: own(context, 'targets') ? { present: true, value: context.targets } : { present: false } } : {}),
  });
}

// Shared synchronous evaluator. Node supplies SHA-256 for archived reports;
// the live browser view supplies no digest and exposes only checks/statuses.
// Predicate bodies and dependency rules are identical in both environments.
export function createModelChecker(digest = () => null) {
 const checkedReports = new WeakMap();
 function verifyModel(object, context = {}) { return evaluateModel(object, context); }
 function verifyModelSelectively(object, context, previousReport) {
  if (!checkedReports.has(previousReport)) throw Error('Untrusted verification baseline: recompute imported reports first');
  return evaluateModel(object, context, checkedReports.get(previousReport));
 }
 function evaluateModel(object, context, previous = null) {
  equalAttributedObjects(object, object);
  const inputContext = jsonClone(context), d = object.diagram, labels = object.labels;
  if (!inputContext || typeof inputContext !== 'object' || Array.isArray(inputContext)) throw Error('Model context must be a JSON object');
  const inputDigest = digest(canonicalJSON({ diagram: d, labels, context: inputContext }));
  const checks = [], byName = new Map(), reads = new Map(), evaluation = [];
  const supported = canonicalJSON(d.schema) === canonicalJSON(isotopeSupportSchema);
  function run(predicate, dependencies, body) {
    const key = readProjection(predicate, d, labels, inputContext, Object.fromEntries(dependencies.map(name => [name, byName.get(name).status])));
    const readDigest = digest(key), baseline = previous?.reads.get(predicate);
    if (baseline?.key === key) {
      const result = baseline.result;
      checks.push(result); byName.set(predicate, result); reads.set(predicate, { key, result });
      evaluation.push({ predicate, mode: 'reused', readDigest }); return result;
    }
    const issues = [];
    const issue = (code, sort, id, detail) => issues.push({ code, sort, id, detail });
    let status;
    if (!supported) status = 'notApplicable';
    else if (dependencies.some(name => byName.get(name).status !== 'verified')) status = 'unknown';
    else { status = body(issue) ?? (issues.length ? 'refuted' : 'verified'); }
    const result = { predicate, status, dependencies, issues };
    if (status === 'unknown' && dependencies.some(name => byName.get(name).status !== 'verified'))
      result.blockedBy = dependencies.filter(name => byName.get(name).status !== 'verified');
    checks.push(result); byName.set(predicate, result); reads.set(predicate, { key, result });
    evaluation.push({ predicate, mode: 'computed', readDigest }); return result;
  }
  run('attribute-types', [], issue => {
    const validators = {
      shell: x => fields(x, ['order', 'size']) && integer(x.order, 1) && integer(x.size, 1) && x.size <= 20,
      cell: x => fields(x, ['row', 'col']) && integer(x.row) && integer(x.col),
      port: x => fields(x, ['role']) && own(offsets, x.role),
      vertex: vertexLabel,
      edge: x => fields(x, []), pair: x => fields(x, []), boundaryWitness: x => fields(x, []),
      lineWitness: x => fields(x, ['axis']) && ['H', 'V'].includes(x.axis),
      boundary: x => fields(x, ['kind']) && x.kind === 'shell-frame',
      support: x => fields(x, ['kind', 'endpoints']) && x.kind === 'undirected-lattice-support'
        && Array.isArray(x.endpoints) && x.endpoints.length === 2 && x.endpoints.every(vertexLabel),
    };
    for (const s of d.schema.sorts) for (const x of d.sets[s])
      if (!validators[s](labels[s][x])) issue('invalid-label', s, x, 'Label does not satisfy the versioned attribute type');
  });
  run('lattice-incidence', ['attribute-types'], issue => {
    const positions = new Set(), orders = new Set(), frames = new Map();
    for (const s of d.sets.shell) {
      const order = labels.shell[s].order;
      if (orders.has(order)) issue('duplicate-shell-order', 'shell', s, { order }); orders.add(order);
    }
    for (const c of d.sets.cell) {
      const shell = d.maps.cellShell[c], attrs = labels.cell[c], size = labels.shell[shell].size;
      if (attrs.row >= size || attrs.col >= size) issue('cell-outside-shell', 'cell', c, { size });
      const position = canonicalJSON([shell, attrs.row, attrs.col]);
      if (positions.has(position)) issue('duplicate-cell-position', 'cell', c, { shell }); positions.add(position);
      const ports = d.sets.port.filter(p => d.maps.portCell[p] === c), roles = ports.map(p => labels.port[p].role).sort();
      if (canonicalJSON(roles) !== canonicalJSON(['B', 'L', 'R', 'T'])) issue('cell-port-domain', 'cell', c, { roles });
      for (const p of ports) {
        const vertex = labels.vertex[d.maps.portVertex[p]], [dx, dy] = offsets[labels.port[p].role];
        const expected = [attrs.col - attrs.row + dx, attrs.row + attrs.col + 1 + dy];
        if (canonicalJSON(vertex.lattice) !== canonicalJSON(expected)) issue('port-lattice-mismatch', 'port', p, { expected, actual: vertex.lattice });
        if (!frames.has(shell)) frames.set(shell, vertex.frame);
        else if (frames.get(shell) !== vertex.frame) issue('mixed-shell-frames', 'port', p, { shell });
      }
    }
  });
  run('support-incidence', ['attribute-types'], issue => {
    for (const e of d.sets.edge) {
      const source = labels.vertex[d.maps.source[e]], target = labels.vertex[d.maps.target[e]];
      const support = d.maps.edgeSupport[e];
      if (source.frame !== target.frame) issue('cross-frame-edge', 'edge', e, { source: source.frame, target: target.frame });
      if (unordered([source, target]) !== unordered(labels.support[support].endpoints))
        issue('support-endpoints-mismatch', 'edge', e, { support });
    }
  });
  run('pair-grammar', ['attribute-types', 'lattice-incidence'], issue => {
    const occupancy = new Map(), shapes = new Set();
    for (const p of d.sets.pair) {
      const cell = d.maps.pairCell[p], shell = d.maps.cellShell[cell];
      occupancy.set(cell, (occupancy.get(cell) ?? 0) + 1);
      const routes = [];
      for (const color of ['red', 'blue']) {
        const start = labels.port[d.maps[`${color}Start`][p]].role, end = labels.port[d.maps[`${color}End`][p]].role;
        routes.push([start, end].sort());
        const [a, b] = [offsets[start], offsets[end]], dx = b[0] - a[0], dy = b[1] - a[1];
        const expected = (labels.shell[shell].order % 2 ? 1 : -1) * (color === 'red' ? 1 : -1);
        if (Math.abs(dx) !== 1 || Math.abs(dy) !== 1) issue('non-diagonal-route', 'pair', p, { color });
        if (dx * dy !== expected) issue('route-color-direction', 'pair', p, { color, expected });
      }
      const shape = canonicalJSON([cell, routes]);
      if (shapes.has(shape)) issue('duplicate-pair-occupancy', 'pair', p, { cell }); shapes.add(shape);
    }
    for (const [cell, count] of occupancy) if (count > 2) issue('cell-capacity', 'cell', cell, { count, maximum: 2 });
  });
  run('witness-grammar', ['attribute-types'], issue => {
    const slots = new Set();
    for (const w of d.sets.lineWitness) {
      const cell = d.maps.lineCell[w], axis = labels.lineWitness[w].axis, slot = canonicalJSON(['line', cell, axis]);
      if (slots.has(slot)) issue('duplicate-witness-slot', 'lineWitness', w, { cell, axis }); slots.add(slot);
      const roles = [d.maps.lineStart[w], d.maps.lineEnd[w]].map(p => labels.port[p].role);
      const expected = axis === 'H' ? ['L', 'R'] : ['T', 'B'];
      if (canonicalJSON(roles) !== canonicalJSON(expected)) issue('witness-axis-route', 'lineWitness', w, { expected, actual: roles });
    }
    for (const w of d.sets.boundaryWitness) {
      const shell = d.maps.boundaryWitnessShell[w], slot = canonicalJSON(['boundary', shell]);
      if (slots.has(slot)) issue('duplicate-boundary-witness', 'boundaryWitness', w, { shell }); slots.add(slot);
    }
  });
  run('color-disjointness', ['support-incidence'], issue => {
    const colors = new Map();
    for (const p of d.sets.pair) for (const color of ['red', 'blue']) {
      const support = d.maps.edgeSupport[d.maps[`${color}Edge`][p]];
      if (!colors.has(support)) colors.set(support, new Set()); colors.get(support).add(color);
    }
    for (const [support, values] of colors) if (values.size > 1) issue('color-conflict', 'support', support, { colors: [...values].sort() });
  });
  run('inventory-targets', ['attribute-types'], issue => {
    const targets = inputContext.targets;
    if (own(inputContext, 'targets') && (!targets || typeof targets !== 'object' || Array.isArray(targets))) {
      issue('invalid-target-container', 'context', 'targets', 'Expected a target object'); return;
    }
    const missing = ['Z', 'N', 'expectedByShell'].filter(k => !targets || !own(targets, k));
    if (missing.length) { issue('missing-target-input', 'context', 'targets', { missing }); return 'unknown'; }
    if (!integer(targets.Z) || !integer(targets.N) || !Array.isArray(targets.expectedByShell) || !targets.expectedByShell.every(x => integer(x))) {
      issue('invalid-target-types', 'context', 'targets', 'Expected nonnegative integer inventory and shell targets'); return;
    }
    const ep = d.sets.pair.length, n = d.sets.lineWitness.length + d.sets.boundaryWitness.length;
    if (ep !== targets.Z) issue('ep-count', 'context', 'Z', { actual: ep, expected: targets.Z });
    if (n !== targets.N) issue('n-count', 'context', 'N', { actual: n, expected: targets.N });
    for (const shell of d.sets.shell) {
      const order = labels.shell[shell].order;
      const actual = d.sets.pair.filter(p => d.maps.cellShell[d.maps.pairCell[p]] === shell).length;
      const expected = targets.expectedByShell[order - 1];
      if (actual !== expected) issue('shell-count', 'shell', shell, { actual, expected: expected ?? null });
    }
    const orders = new Set(d.sets.shell.map(s => labels.shell[s].order));
    for (let i = 0; i < targets.expectedByShell.length; i++) if (!orders.has(i + 1))
      issue('target-without-shell', 'context', 'expectedByShell', { order: i + 1 });
  });
  const status = !supported ? 'notApplicable' : checks.some(c => c.status === 'refuted') ? 'refuted'
    : checks.some(c => c.status === 'unknown') ? 'unknown' : 'verified';
  const report = deepFreeze({ modelVersion, checkerVersion, inputDigest, status, checks,
    evaluation: { contractVersion: predicateReadContract.version, baselineInputDigest: previous?.inputDigest ?? null, predicates: evaluation },
    scope: 'Declared shell-lattice predicates and agreement with supplied targets only; no physical interpretation or placement-resolution claim',
    physicalInterpretation: 'not-checked' });
  checkedReports.set(report, { inputDigest, reads }); return report;
 }
 return Object.freeze({ verifyModel, verifyModelSelectively });
}
