import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import { importLegacyAbsolute } from '../examples/isotope-wiring/core/legacy-adapter.mjs';
import { canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { createRevisionStore, importRevisionBundle, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';

const html = readFileSync(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8');
const context = vm.createContext({});
vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], context, { timeout: 5000 });
const fixture = JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures().O16));
const clone = x => JSON.parse(JSON.stringify(x));
function setup() {
  const packet = importLegacyAbsolute(fixture), store = createRevisionStore();
  const seed = store.seed(packet.object, packet.modelContext, { note: 'initial metadata', source: packet.retainedSource });
  return { store, seed, packet };
}
function recordAt(store, revision, sort, id) {
  const { object } = store.state(revision), d = object.diagram;
  return { sort, id, label: object.labels[sort][id], incidence: Object.fromEntries(d.schema.arrows.filter(a => a.from === sort).map(a => [a.name, d.maps[a.name][id]])) };
}
function removePair(store, revision) {
  const id = fixture.graph.pairs[0].id;
  return store.preparePatch(revision, { remove: [{ sort: 'pair', id }] });
}
const code = expected => error => error instanceof RewriteError && error.code === expected;
function retag(domain, input) {
  const { id, ...body } = input;
  return { ...body, id: createHash('sha256').update(domain + '\n' + canonicalJSON(body)).digest('hex') };
}

test('state/revision identities are deterministic, immutable, and metadata-sensitive', () => {
  const { store, seed, packet } = setup();
  assert.equal(store.seed(packet.object, packet.modelContext, { source: packet.retainedSource, note: 'initial metadata' }).id, seed.id);
  const other = store.seed(packet.object, packet.modelContext, { note: 'different' });
  assert.notEqual(other.stateId, seed.stateId); assert.notEqual(other.id, seed.id);
  assert.throws(() => store.state(seed.id).context.targets.Z++, TypeError);
  assert.equal(store.state(seed.id).context.targets.Z, 8);
});

test('exact record edits retain matches and reject stale revision boundaries, even with equal state', () => {
  const { store, seed } = setup(), op = removePair(store, seed.id);
  assert.equal(op.remove[0].before.label && Object.keys(op.remove[0].before.incidence).length > 0, true);
  const a = store.applyPatch(seed.id, op), noop = store.applyPatch(seed.id, store.preparePatch(seed.id));
  assert.equal(noop.revision.stateId, seed.stateId);
  assert.notEqual(noop.revision.id, seed.id);
  assert.throws(() => store.applyPatch(noop.revision.id, op), code('stale-operation-boundary'));
  assert.throws(() => store.applyPatch(a.revision.id, op), code('stale-operation-boundary'));
  assert.equal(store.applyPatch(seed.id, op).revision.id, a.revision.id, 'exact replay is idempotent');
});

test('forged before-images and overlapping edit requests are refused', () => {
  const { store, seed } = setup();
  const op = clone(removePair(store, seed.id)); op.remove[0].before.label = { invented: true };
  assert.throws(() => store.applyPatch(seed.id, retag('isotope-wiring.operation.v1', op)), code('before-image-or-operation-mismatch'));
  const p = fixture.graph.pairs[0].id;
  assert.throws(() => store.preparePatch(seed.id, { remove: [{ sort: 'pair', id: p }], replace: [recordAt(store, seed.id, 'pair', p)] }), code('overlapping-record-edits'));
  assert.throws(() => store.preparePatch(seed.id, { add: [recordAt(store, seed.id, 'pair', p)] }), code('record-already-exists'));
});

test('dangling deletion is localized and leaves the store and active head unchanged', () => {
  const { store, seed } = setup(); store.setHead('main', null, seed.id);
  const vertex = store.state(seed.id).object.diagram.sets.vertex[0];
  const op = store.preparePatch(seed.id, { remove: [{ sort: 'vertex', id: vertex }] });
  const before = store.exportBundle();
  assert.throws(() => store.applyAtHead('main', op), error => {
    assert(code('dangling-reference')(error));
    assert(error.detail.some(r => r.missingTarget === vertex && ['source', 'target', 'portVertex'].includes(r.arrow))); return true;
  });
  assert.deepEqual(store.exportBundle(), before); assert.equal(store.head('main'), seed.id);
});

test('atomic coordinated deletion succeeds without automatic garbage collection', () => {
  const { store, seed } = setup(), pair = fixture.graph.pairs[0].id;
  const d = store.state(seed.id).object.diagram, edge = d.maps.redEdge[pair];
  const op = store.preparePatch(seed.id, { remove: [{ sort: 'pair', id: pair }, { sort: 'edge', id: edge }] });
  const next = store.applyPatch(seed.id, op).revision, after = store.state(next.id).object.diagram;
  assert.equal(after.sets.pair.length, 7); assert.equal(after.sets.edge.length, d.sets.edge.length - 1);
  assert(after.sets.support.includes(d.maps.edgeSupport[edge]), 'unreferenced support is retained');
});

test('an atomic edge replacement can transport all affected references explicitly', () => {
  const { store, seed } = setup(), pairId = fixture.graph.pairs[0].id;
  const pair = clone(recordAt(store, seed.id, 'pair', pairId)), edgeId = pair.incidence.redEdge;
  const edge = clone(recordAt(store, seed.id, 'edge', edgeId)); edge.id = 'replacement-edge';
  pair.incidence.redEdge = edge.id;
  const op = store.preparePatch(seed.id, { remove: [{ sort: 'edge', id: edgeId }], add: [edge], replace: [pair] });
  const result = store.applyPatch(seed.id, op), d = store.state(result.revision.id).object.diagram;
  assert.equal(d.maps.redEdge[pairId], edge.id); assert(!d.sets.edge.includes(edgeId));
  assert.equal(store.verifyAt(result.revision.id).result.status, 'verified');
  const restored = store.undo(result.revision.id, result.receipt.id);
  assert.equal(restored.revision.stateId, seed.stateId);
});

test('independent edit routes can share state without identifying their revisions or paths', () => {
  const { store, seed } = setup(), [a, b] = fixture.graph.pairs.slice(0, 2).map(p => p.id);
  const remove = (revision, id) => store.applyPatch(revision, store.preparePatch(revision, { remove: [{ sort: 'pair', id }] }));
  const firstA = remove(seed.id, a), thenB = remove(firstA.revision.id, b);
  const firstB = remove(seed.id, b), thenA = remove(firstB.revision.id, a);
  assert.equal(thenB.revision.stateId, thenA.revision.stateId);
  assert.notEqual(thenB.revision.id, thenA.revision.id);
  assert.notDeepEqual(store.makePath(seed.id, [firstA.receipt.id, thenB.receipt.id]), store.makePath(seed.id, [firstB.receipt.id, thenA.receipt.id]));
});

test('schema-invalid replacements are refused without committing partial changes', () => {
  const { store, seed } = setup(), pair = fixture.graph.pairs[0].id;
  const changed = clone(recordAt(store, seed.id, 'pair', pair));
  changed.incidence.redStart = changed.incidence.redEnd;
  const op = store.preparePatch(seed.id, { replace: [changed] }), before = store.exportBundle();
  assert.throws(() => store.applyPatch(seed.id, op), /Schema equation fails/);
  assert.deepEqual(store.exportBundle(), before);
});

test('full context/metadata replacement removes omitted fields rather than inheriting them', () => {
  const { store, seed } = setup();
  const next = store.applyPatch(seed.id, store.preparePatch(seed.id, { contextAfter: {}, metadataAfter: {} })).revision;
  assert.deepEqual(store.state(next.id).context, {}); assert.deepEqual(store.state(next.id).metadata, {});
  assert.equal(store.verifyAt(next.id).result.status, 'unknown');
  assert.equal(store.state(seed.id).metadata.note, 'initial metadata');
});

test('undo restores full state but creates a new revision with retained provenance', () => {
  const { store, seed } = setup();
  const contextAfter = clone(store.state(seed.id).context); contextAfter.targets.Z = 7; contextAfter.targets.expectedByShell = [1, 6];
  const op = store.preparePatch(seed.id, { remove: [{ sort: 'pair', id: fixture.graph.pairs[0].id }], contextAfter, metadataAfter: { note: 'edited' } });
  const edit = store.applyPatch(seed.id, op), restored = store.undo(edit.revision.id, edit.receipt.id);
  assert.equal(restored.revision.stateId, seed.stateId); assert.notEqual(restored.revision.id, seed.id);
  assert.deepEqual(restored.revision.parents, [edit.revision.id]);
  assert.deepEqual(store.state(restored.revision.id).data, store.state(seed.id).data);
  const redo = store.undo(restored.revision.id, restored.receipt.id);
  assert.equal(redo.revision.stateId, edit.revision.stateId);
  assert.throws(() => store.undo(redo.revision.id, edit.receipt.id), code('invalid-restore-boundary'));
});

test('every edit invalidates prior verification; candidates failing model checks remain representable', () => {
  const { store, seed } = setup(), old = store.verifyAt(seed.id);
  assert.equal(old.result.status, 'verified');
  const pair = clone(recordAt(store, seed.id, 'pair', fixture.graph.pairs[0].id)); pair.id = 'new-owned-occurrence';
  const edit = store.applyPatch(seed.id, store.preparePatch(seed.id, { add: [pair] }));
  assert.equal(store.verification(edit.revision.id), null);
  assert.equal(edit.receipt.verificationInvalidation.policy, 'all');
  assert.equal(store.verifyAt(edit.revision.id).result.status, 'refuted');
  const restored = store.undo(edit.revision.id, edit.receipt.id);
  assert.equal(restored.revision.stateId, seed.stateId); assert.equal(store.verification(restored.revision.id), null);
  assert.equal(store.verification(seed.id).id, old.id, 'historical evidence is retained, not relabelled as current');
});

test('branch heads use compare-and-swap and old snapshots remain explicit branch sources', () => {
  const { store, seed } = setup(); store.setHead('main', null, seed.id);
  const op = removePair(store, seed.id), result = store.applyAtHead('main', op);
  assert.equal(store.head('main'), result.revision.id);
  assert.throws(() => store.applyAtHead('main', op), code('stale-operation-boundary'));
  assert.throws(() => store.setHead('main', seed.id, seed.id), code('head-compare-and-swap-failed'));
  const fork = store.applyPatch(seed.id, store.preparePatch(seed.id, { metadataAfter: { branch: true } }));
  store.setHead('fork', null, fork.revision.id);
  assert.equal(store.head('main'), result.revision.id); assert.deepEqual(fork.revision.parents, [seed.id]);
});

test('revision paths have identities and associative composition without identifying undo histories', () => {
  const { store, seed } = setup();
  const a = store.applyPatch(seed.id, removePair(store, seed.id));
  const b = store.undo(a.revision.id, a.receipt.id);
  const c = store.applyPatch(b.revision.id, store.preparePatch(b.revision.id));
  const pa = store.makePath(seed.id, [a.receipt.id]), pb = store.makePath(a.revision.id, [b.receipt.id]), pc = store.makePath(b.revision.id, [c.receipt.id]);
  assert.deepEqual(store.composePaths(store.makePath(pa.target), pa), pa);
  assert.deepEqual(store.composePaths(pa, store.makePath(pa.source)), pa);
  assert.deepEqual(store.composePaths(pc, store.composePaths(pb, pa)), store.composePaths(store.composePaths(pc, pb), pa));
  assert.notEqual(store.composePaths(pb, pa).target, seed.id, 'state restoration does not erase path provenance');
  assert.throws(() => store.composePaths(pa, pb), code('path-boundary-mismatch'));
});

test('dependency-complete bundles replay edits, branches and undo into identical history', () => {
  const { store, seed } = setup(), a = store.applyPatch(seed.id, removePair(store, seed.id));
  const b = store.undo(a.revision.id, a.receipt.id);
  store.setHead('main', null, b.revision.id); store.setHead('alternative', null, a.revision.id);
  store.verifyAt(seed.id); store.verifyAt(b.revision.id);
  const bundle = JSON.parse(JSON.stringify(store.exportBundle())), replay = importRevisionBundle(bundle);
  assert.deepEqual(replay.exportBundle(), bundle);
  assert.deepEqual(replay.state(b.revision.id).data, store.state(seed.id).data);
  assert.equal(replay.verification(b.revision.id), null);
  assert.equal(replay.verifyAt(b.revision.id).id, store.verification(b.revision.id).id);
});

test('bundle corruption, missing dependencies, wrong engines and duplicate history are refused', () => {
  const { store, seed } = setup(), a = store.applyPatch(seed.id, removePair(store, seed.id));
  store.setHead('main', null, a.revision.id);
  const good = store.exportBundle();
  const corrupt = clone(good); corrupt.seeds[0].state.metadata.note = 'tampered';
  assert.throws(() => importRevisionBundle(corrupt), code('seed-replay-mismatch'));
  const missing = clone(good); missing.seeds = [];
  assert.throws(() => importRevisionBundle(missing), code('missing-revision'));
  const wrong = clone(good); wrong.engineDigest = 'different-engine';
  assert.throws(() => importRevisionBundle(wrong), code('bundle-engine-mismatch'));
  const duplicate = clone(good); duplicate.steps.push(duplicate.steps[0]);
  assert.throws(() => importRevisionBundle(duplicate), code('noncanonical-bundle'));
  const forged = clone(good); forged.steps[0].afterStateId = seed.stateId;
  forged.steps[0] = retag('isotope-wiring.rewrite-receipt.v1', forged.steps[0]);
  assert.throws(() => importRevisionBundle(forged), code('receipt-replay-mismatch'));
  assert.deepEqual(store.exportBundle(), good, 'import refusals do not mutate existing stores');
});
