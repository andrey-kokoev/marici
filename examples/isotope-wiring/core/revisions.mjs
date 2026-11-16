import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { defineSchema, createDiagram } from './finite-diagrams.mjs';
import { attributeDiagram, equalAttributedObjects, canonicalJSON, jsonClone, deepFreeze } from './attributed-diagrams.mjs';
import { verifyModel, verifyModelSelectively } from './model-predicates.mjs';

const hash = (domain, data) => createHash('sha256').update(domain + '\n' + canonicalJSON(data)).digest('hex');
export const revisionEngineDigest = hash('isotope-wiring.engine-source.v1', Object.fromEntries([
  'revisions.mjs', 'finite-diagrams.mjs', 'attributed-diagrams.mjs', 'model-predicates.mjs', 'schemas.mjs', 'rules.mjs',
  'overlap-census.mjs', 'verification-bundles.mjs', 'matching.mjs', 'join-search.mjs', 'isomorphic-joins.mjs', 'context-lifting.mjs', 'context-composition.mjs',
].map(name => [name, createHash('sha256').update(readFileSync(new URL(name, import.meta.url))).digest('hex')])));
export class RewriteError extends Error {
  constructor(code, detail) { super(code); this.name = 'RewriteError'; this.code = code; this.detail = detail; }
}
const demand = (condition, code, detail = null) => { if (!condition) throw new RewriteError(code, detail); };
const own = (o, k) => Object.hasOwn(o, k);
function exactKeys(o, keys, code) {
  demand(o && typeof o === 'object' && !Array.isArray(o)
    && canonicalJSON(Object.keys(o).sort()) === canonicalJSON([...keys].sort()), code);
}
const address = r => canonicalJSON([r.sort, r.id]);
const recordOrder = (a, b) => address(a) < address(b) ? -1 : address(a) > address(b) ? 1 : 0;
const tagged = (domain, body) => deepFreeze({ ...body, id: hash(domain, body) });
const validTag = (domain, value) => {
  const { id, ...body } = value;
  demand(id === hash(domain, body), 'content-digest-mismatch', { domain, id }); return body;
};

function snapshot(object, context, metadata) {
  equalAttributedObjects(object, object);
  const c = jsonClone(context), m = jsonClone(metadata);
  demand(c && typeof c === 'object' && !Array.isArray(c), 'context-must-be-object');
  demand(m && typeof m === 'object' && !Array.isArray(m), 'metadata-must-be-object');
  const data = jsonClone({ diagram: object.diagram, labels: object.labels, context: c, metadata: m });
  return deepFreeze({ id: hash('isotope-wiring.state.v1', data), object, context: c, metadata: m, data });
}
function decodeState(data) {
  exactKeys(data, ['diagram', 'labels', 'context', 'metadata'], 'state-fields-mismatch');
  const schema = defineSchema(data.diagram.schema);
  const object = attributeDiagram(createDiagram(schema, data.diagram), data.labels);
  const result = snapshot(object, data.context, data.metadata);
  demand(canonicalJSON(result.data) === canonicalJSON(data), 'noncanonical-state'); return result;
}
function record(state, sort, id) {
  const d = state.object.diagram;
  demand(d.schema.sorts.includes(sort), 'unknown-record-sort', { sort });
  demand(d.sets[sort].includes(id), 'missing-record-match', { sort, id });
  return jsonClone({ label: state.object.labels[sort][id], incidence: Object.fromEntries(d.schema.arrows
    .filter(a => a.from === sort).map(a => [a.name, d.maps[a.name][id]])) });
}
function afterRecord(state, r) {
  exactKeys(r, ['sort', 'id', 'label', 'incidence'], 'record-fields-mismatch');
  demand(state.object.diagram.schema.sorts.includes(r.sort), 'unknown-record-sort', { sort: r.sort });
  exactKeys(r.incidence, state.object.diagram.schema.arrows.filter(a => a.from === r.sort).map(a => a.name), 'record-incidence-domain-mismatch');
  return jsonClone({ label: r.label, incidence: r.incidence });
}

// In-memory immutable store. Export is explicit; no implicit disk durability.
export function createRevisionStore() {
  const states = new Map(), revisions = new Map(), receipts = new Map(), seeds = [], steps = [];
  const heads = new Map(), verifications = new Map(), verificationArchive = new Map(), paths = new WeakSet();
  const revision = id => { demand(revisions.has(id), 'missing-revision', { id }); return revisions.get(id); };
  const state = id => states.get(revision(id).stateId);
  function seed(object, context = {}, metadata = {}) {
    const s = snapshot(object, context, metadata);
    const r = tagged('isotope-wiring.revision.v1', { format: 'isotope-wiring.revision.v1', stateId: s.id, parents: [], event: { kind: 'seed', engineDigest: revisionEngineDigest } });
    if (!revisions.has(r.id)) { states.set(s.id, s); revisions.set(r.id, r); seeds.push({ revisionId: r.id, state: s.data }); }
    return r;
  }
  function preparePatch(inputRevision, request = {}) {
    const s = state(inputRevision), q = jsonClone(request);
    demand(q && typeof q === 'object' && !Array.isArray(q), 'patch-request-must-be-object');
    demand(Object.keys(q).every(k => ['remove', 'add', 'replace', 'contextAfter', 'metadataAfter', 'provenance'].includes(k)), 'unknown-patch-field');
    for (const key of ['remove', 'add', 'replace']) if (own(q, key)) demand(Array.isArray(q[key]), 'patch-records-must-be-arrays', { key });
    const used = new Set();
    function unique(r) { const k = address(r); demand(!used.has(k), 'overlapping-record-edits', r); used.add(k); }
    const remove = (q.remove ?? []).map(r => {
      exactKeys(r, ['sort', 'id'], 'remove-fields-mismatch'); unique(r);
      return { sort: r.sort, id: r.id, before: record(s, r.sort, r.id) };
    }).sort(recordOrder);
    const add = (q.add ?? []).map(r => {
      unique(r); const after = afterRecord(s, r);
      demand(!s.object.diagram.sets[r.sort].includes(r.id), 'record-already-exists', r);
      return { sort: r.sort, id: r.id, after };
    }).sort(recordOrder);
    const replace = (q.replace ?? []).map(r => {
      unique(r); const after = afterRecord(s, r);
      return { sort: r.sort, id: r.id, before: record(s, r.sort, r.id), after };
    }).sort(recordOrder);
    return tagged('isotope-wiring.operation.v1', {
      format: 'isotope-wiring.operation.v1', kind: 'record-patch', engineDigest: revisionEngineDigest,
      inputRevision, inputStateId: s.id, remove, add, replace,
      provenance: own(q, 'provenance') ? q.provenance : null,
      contextChange: own(q, 'contextAfter') ? { before: s.context, after: q.contextAfter } : null,
      metadataChange: own(q, 'metadataAfter') ? { before: s.metadata, after: q.metadataAfter } : null,
    });
  }
  function patched(s, op) {
    exactKeys(op, ['format', 'kind', 'engineDigest', 'inputRevision', 'inputStateId', 'remove', 'add', 'replace', 'contextChange', 'metadataChange', 'provenance', 'id'], 'operation-fields-mismatch');
    for (const key of ['remove', 'add', 'replace']) demand(Array.isArray(op[key]), 'patch-records-must-be-arrays', { key });
    // Regenerate the canonical operation and all before-images from the frozen
    // source. This validates matches, disjointness, domains, and explicit metadata semantics.
    const request = {
      provenance: op.provenance,
      remove: op.remove.map(({ sort, id }) => ({ sort, id })),
      add: op.add.map(({ sort, id, after }) => ({ sort, id, ...after })),
      replace: op.replace.map(({ sort, id, after }) => ({ sort, id, ...after })),
      ...(op.contextChange === null ? {} : { contextAfter: op.contextChange.after }),
      ...(op.metadataChange === null ? {} : { metadataAfter: op.metadataChange.after }),
    };
    demand(canonicalJSON(preparePatch(op.inputRevision, request)) === canonicalJSON(op), 'before-image-or-operation-mismatch');
    const data = jsonClone(s.data), d = data.diagram;
    for (const r of op.remove) {
      d.sets[r.sort] = d.sets[r.sort].filter(id => id !== r.id); delete data.labels[r.sort][r.id];
      for (const a of d.schema.arrows.filter(a => a.from === r.sort)) delete d.maps[a.name][r.id];
    }
    for (const r of [...op.add, ...op.replace]) {
      if (!d.sets[r.sort].includes(r.id)) d.sets[r.sort].push(r.id);
      // defineProperty keeps arbitrary rejected IDs from mutating prototypes
      // before the kernel checks identifier admissibility.
      Object.defineProperty(data.labels[r.sort], r.id, { value: r.after.label, enumerable: true, configurable: true, writable: true });
      for (const [a, target] of Object.entries(r.after.incidence))
        Object.defineProperty(d.maps[a], r.id, { value: target, enumerable: true, configurable: true, writable: true });
    }
    const dangling = [];
    for (const a of d.schema.arrows) for (const id of d.sets[a.from]) if (!d.sets[a.to].includes(d.maps[a.name][id]))
      dangling.push({ arrow: a.name, sort: a.from, id, targetSort: a.to, missingTarget: d.maps[a.name][id] });
    demand(dangling.length === 0, 'dangling-reference', dangling);
    const object = attributeDiagram(createDiagram(s.object.diagram.schema, d), data.labels);
    return snapshot(object, op.contextChange === null ? s.context : op.contextChange.after, op.metadataChange === null ? s.metadata : op.metadataChange.after);
  }
  function applyPatch(currentRevision, input) {
    const op = jsonClone(input), before = state(currentRevision);
    demand(op && typeof op === 'object', 'invalid-operation'); validTag('isotope-wiring.operation.v1', op);
    demand(op.engineDigest === revisionEngineDigest && op.format === 'isotope-wiring.operation.v1', 'operation-engine-mismatch');
    demand(op.inputRevision === currentRevision && op.inputStateId === before.id, 'stale-operation-boundary');
    let after;
    if (op.kind === 'record-patch') after = patched(before, op);
    else if (op.kind === 'restore') {
      exactKeys(op, ['format', 'kind', 'engineDigest', 'inputRevision', 'inputStateId', 'restoringReceipt', 'targetStateId', 'id'], 'operation-fields-mismatch');
      const original = receipts.get(op.restoringReceipt);
      demand(original && original.outputRevision === currentRevision && original.beforeStateId === op.targetStateId, 'invalid-restore-boundary');
      after = states.get(op.targetStateId); demand(after, 'missing-before-image');
    } else throw new RewriteError('unknown-operation-kind', op.kind);
    const next = tagged('isotope-wiring.revision.v1', { format: 'isotope-wiring.revision.v1', stateId: after.id, parents: [currentRevision], event: { kind: op.kind, operationId: op.id, engineDigest: revisionEngineDigest } });
    const receipt = tagged('isotope-wiring.rewrite-receipt.v1', {
      format: 'isotope-wiring.rewrite-receipt.v1', engineDigest: revisionEngineDigest, operation: op,
      inputRevision: currentRevision, outputRevision: next.id, beforeStateId: before.id, afterStateId: after.id,
      verificationInvalidation: { policy: 'all', sourceRevision: currentRevision },
    });
    // Commit only after all checks have succeeded. No rejected input mutates a head or store history.
    states.set(after.id, after); revisions.set(next.id, next);
    if (!receipts.has(receipt.id)) { receipts.set(receipt.id, receipt); steps.push(receipt); }
    return Object.freeze({ revision: next, receipt });
  }
  function undo(currentRevision, receiptId) {
    const original = receipts.get(receiptId), current = state(currentRevision);
    demand(original && original.outputRevision === currentRevision, 'invalid-restore-boundary');
    const operation = tagged('isotope-wiring.operation.v1', {
      format: 'isotope-wiring.operation.v1', kind: 'restore', engineDigest: revisionEngineDigest,
      inputRevision: currentRevision, inputStateId: current.id, restoringReceipt: receiptId, targetStateId: original.beforeStateId,
    });
    return applyPatch(currentRevision, operation);
  }
  function setHead(name, expected, next) {
    demand(typeof name === 'string' && name.length > 0, 'invalid-head-name'); revision(next);
    demand((heads.get(name) ?? null) === expected, 'head-compare-and-swap-failed', { name, expected, actual: heads.get(name) ?? null });
    heads.set(name, next); return next;
  }
  function applyAtHead(name, operation) {
    const current = heads.get(name); demand(current, 'missing-head', { name });
    const result = applyPatch(current, operation); setHead(name, current, result.revision.id); return result;
  }
  function verifyAt(revisionId, { reuseFrom = null, reuseVerificationId = null } = {}) {
    const s = state(revisionId), baseline = reuseVerificationId !== null ? verificationArchive.get(reuseVerificationId)
      : reuseFrom === null ? null : verifications.get(reuseFrom);
    demand((reuseFrom === null && reuseVerificationId === null) || baseline, 'missing-verification-baseline', { reuseFrom, reuseVerificationId });
    demand(!baseline || reuseFrom === null || baseline.revisionId === reuseFrom, 'verification-baseline-binding-mismatch');
    const result = baseline ? verifyModelSelectively(s.object, s.context, baseline.result) : verifyModel(s.object, s.context);
    const bound = tagged('isotope-wiring.revision-verification.v1', {
      format: 'isotope-wiring.revision-verification.v1', revisionId, stateId: s.id, engineDigest: revisionEngineDigest,
      transportFrom: baseline ? { revisionId: baseline.revisionId, verificationId: baseline.id } : null, result,
    });
    verifications.set(revisionId, bound); verificationArchive.set(bound.id, bound); return bound;
  }
  function makePath(source, receiptIds = []) {
    revision(source); demand(Array.isArray(receiptIds), 'path-receipts-must-be-array'); let target = source;
    for (const id of receiptIds) { const r = receipts.get(id); demand(r && r.inputRevision === target, 'path-boundary-mismatch', { id }); target = r.outputRevision; }
    const p = deepFreeze({ source, target, receipts: [...receiptIds] }); paths.add(p); return p;
  }
  function composePaths(after, before) {
    demand(paths.has(after) && paths.has(before), 'unchecked-path');
    demand(before.target === after.source, 'path-boundary-mismatch');
    return makePath(before.source, [...before.receipts, ...after.receipts]);
  }
  function exportBundle() {
    return jsonClone({ format: 'isotope-wiring.revision-bundle.v1', engineDigest: revisionEngineDigest,
      seeds, steps, heads: Object.fromEntries([...heads].sort(([a], [b]) => a < b ? -1 : a > b ? 1 : 0)),
      verificationPolicy: 'reports-not-exported-recompute-after-replay' });
  }
  return Object.freeze({ seed, revision, state, preparePatch, applyPatch, undo, setHead, applyAtHead,
    head: name => heads.get(name) ?? null,
    verifyAt, verification: revisionId => { revision(revisionId); return verifications.get(revisionId) ?? null; },
    verificationById: id => verificationArchive.get(id) ?? null,
    makePath, composePaths, exportBundle,
  });
}

// Replay into a fresh store; a failure never mutates a caller's existing store.
export function importRevisionBundle(input) {
  const bundle = jsonClone(input);
  exactKeys(bundle, ['format', 'engineDigest', 'seeds', 'steps', 'heads', 'verificationPolicy'], 'bundle-fields-mismatch');
  demand(bundle.format === 'isotope-wiring.revision-bundle.v1' && bundle.engineDigest === revisionEngineDigest, 'bundle-engine-mismatch');
  demand(bundle.verificationPolicy === 'reports-not-exported-recompute-after-replay', 'bundle-verification-policy-mismatch');
  demand(Array.isArray(bundle.seeds) && Array.isArray(bundle.steps), 'bundle-history-must-be-arrays');
  const store = createRevisionStore();
  for (const seed of bundle.seeds) {
    exactKeys(seed, ['revisionId', 'state'], 'seed-fields-mismatch');
    const s = decodeState(seed.state), r = store.seed(s.object, s.context, s.metadata);
    demand(r.id === seed.revisionId, 'seed-replay-mismatch');
  }
  for (const expected of bundle.steps) {
    validTag('isotope-wiring.rewrite-receipt.v1', expected);
    const result = store.applyPatch(expected.inputRevision, expected.operation);
    demand(canonicalJSON(result.receipt) === canonicalJSON(expected), 'receipt-replay-mismatch');
  }
  demand(bundle.heads && typeof bundle.heads === 'object' && !Array.isArray(bundle.heads), 'bundle-heads-must-be-object');
  for (const [name, id] of Object.entries(bundle.heads)) store.setHead(name, null, id);
  demand(canonicalJSON(store.exportBundle()) === canonicalJSON(bundle), 'noncanonical-bundle');
  return store;
}
