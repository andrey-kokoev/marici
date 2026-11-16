import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import vm from 'node:vm';
import { createDiagram, equalMorphisms, identity } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { directedGraphSchema as schema } from '../examples/isotope-wiring/core/schemas.mjs';
import { attributeDiagram, attributedMorphism, attributedIdentity, inverseAttributed, canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { createRevisionStore, importRevisionBundle, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';
import { importLegacyAbsolute } from '../examples/isotope-wiring/core/legacy-adapter.mjs';
import { defineRule, exportRule, importRule, subdiagram, generatedSubdiagram, planRewrite, applyRewrite,
  transportMatch, proveIndependent, verifyRewriteWitness, verifyIndependenceWitness, verifyRuleHistory } from '../examples/isotope-wiring/core/rules.mjs';

function graph(vertices, edges = []) {
  const d = createDiagram(schema, { sets: { vertex: vertices, edge: edges.map(e => e[0]) },
    maps: { source: Object.fromEntries(edges.map(([e, s]) => [e, s])), target: Object.fromEntries(edges.map(([e, , t]) => [e, t])) } });
  return attributeDiagram(d, Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(x => [x, {}]))])));
}
const map = (a, b, vertex, edge = {}) => attributedMorphism(a, b, { vertex, edge });
const code = expected => e => e instanceof RewriteError && e.code === expected;
const clone = x => JSON.parse(JSON.stringify(x));
function deletion() {
  const l = graph(['a', 'b'], [['e', 'a', 'b']]), k = graph(['a', 'b']);
  return defineRule('delete-directed-edge', map(k, l, { a: 'a', b: 'b' }), attributedIdentity(k));
}
function addition() {
  const k = graph(['a', 'b']), r = graph(['a', 'b'], [['e', 'a', 'b']]);
  return defineRule('add-directed-edge', attributedIdentity(k), map(k, r, { a: 'a', b: 'b' }));
}
function setup(edges = [['first', 'v0', 'v1'], ['second', 'v1', 'v2']]) {
  const store = createRevisionStore(), object = graph(['v0', 'v1', 'v2'], edges), seed = store.seed(object, {}, { origin: 'test' });
  return { store, object, seed };
}
function retag(domain, x) { const { id, ...body } = x; return { ...body, id: createHash('sha256').update(domain + '\n' + canonicalJSON(body)).digest('hex') }; }

test('reusable monic rules serialize exactly and reject nonmonic legs', () => {
  const rule = deletion(); assert.deepEqual(exportRule(importRule(exportRule(rule))), exportRule(rule));
  const k = graph(['a', 'b']), l = graph(['one']);
  assert.throws(() => defineRule('collapse', map(k, l, { a: 'one', b: 'one' }), attributedIdentity(k)), code('rule-legs-must-be-monic'));
  const tampered = exportRule(rule); tampered.name = 'changed';
  assert.throws(() => importRule(tampered), code('rule-witness-digest-mismatch'));
});

test('a reusable rule has explicit matches at two different places', () => {
  const { store, object, seed } = setup(), rule = deletion();
  const m1 = map(rule.left.target, object, { a: 'v0', b: 'v1' }, { e: 'first' });
  const m2 = map(rule.left.target, object, { a: 'v1', b: 'v2' }, { e: 'second' });
  const before = store.exportBundle(), a = planRewrite(store, seed.id, rule, m1), b = planRewrite(store, seed.id, rule, m2);
  assert.deepEqual(store.exportBundle(), before, 'planning is isolated');
  inverseAttributed(a.firstComparison); inverseAttributed(b.firstComparison);
  const result = applyRewrite(store, seed.id, a);
  assert.deepEqual(store.state(result.revision.id).object.diagram.sets.edge, ['second']);
  assert.equal(result.receipt.operation.provenance.rule.id, rule.id);
  assert.throws(() => applyRewrite(store, result.revision.id, b), code('stale-rule-boundary'));
});

test('explicit match transport factors through the preserved context', () => {
  const { store, object, seed } = setup(), rule = deletion();
  const m1 = map(rule.left.target, object, { a: 'v0', b: 'v1' }, { e: 'first' });
  const m2 = map(rule.left.target, object, { a: 'v1', b: 'v2' }, { e: 'second' });
  const a = planRewrite(store, seed.id, rule, m1), transported = transportMatch(a, m2);
  assert.equal(transported.match.map.components.edge.e, 'second');
  assert(transported.factor.target.diagram.sets.edge.includes('second'));
  const result = applyRewrite(store, seed.id, a), b = planRewrite(store, result.revision.id, rule, transported.match);
  const final = applyRewrite(store, result.revision.id, b);
  assert.deepEqual(store.state(final.revision.id).object.diagram.sets.edge, []);
  assert.throws(() => transportMatch(a, m1), code('transport-deleted-match'));
});

test('independence retains a full-state diamond, not equality of revision histories', () => {
  const { store, object, seed } = setup(), rule = deletion();
  const a = planRewrite(store, seed.id, rule, map(rule.left.target, object, { a: 'v0', b: 'v1' }, { e: 'first' }));
  const b = planRewrite(store, seed.id, rule, map(rule.left.target, object, { a: 'v1', b: 'v2' }, { e: 'second' }));
  const before = store.exportBundle(), result = proveIndependent(store, a, b), w = result.witness;
  assert.deepEqual(store.exportBundle(), before, 'proof search does not create branches in the caller');
  assert.notEqual(w.ab.second.outputRevision, w.ba.second.outputRevision);
  const replay = importRevisionBundle(result.bundle);
  assert.equal(replay.revision(w.ab.second.outputRevision).stateId, w.commonStateId);
  assert.equal(replay.revision(w.ba.second.outputRevision).stateId, w.commonStateId);
  assert.deepEqual(replay.state(w.ab.second.outputRevision).object.diagram.sets.edge, []);
  assert.equal(verifyIndependenceWitness(store, JSON.parse(JSON.stringify(w))), true);
  assert.equal(verifyRewriteWitness(replay, w.ab.second), true);
});

test('disjoint write sets are insufficient: delete/read overlap is refused', () => {
  const { store, object, seed } = setup(), remove = deletion(), l = remove.left.target;
  const preserve = defineRule('read-preserve-edge', attributedIdentity(l), attributedIdentity(l));
  const match = map(l, object, { a: 'v0', b: 'v1' }, { e: 'first' });
  const a = planRewrite(store, seed.id, remove, match), b = planRewrite(store, seed.id, preserve, match);
  assert.equal(b.operation.remove.length + b.operation.add.length, 0);
  assert.throws(() => proveIndependent(store, a, b), error => code('delete-read-conflict')(error) && error.detail.some(x => x.id === 'first'));
});

test('external incidence prevents deletion of a matched vertex', () => {
  const { store, object, seed } = setup(), l = graph(['p']), k = graph([]);
  const rule = defineRule('delete-vertex', map(k, l, {}), attributedIdentity(k));
  const before = store.exportBundle();
  assert.throws(() => planRewrite(store, seed.id, rule, map(l, object, { p: 'v0' })), error =>
    code('rule-dangling-condition')(error) && error.detail.some(x => x.arrow === 'source' && x.id === 'first'));
  assert.deepEqual(store.exportBundle(), before);
});

test('noninjective matches cannot silently identify pattern occurrences', () => {
  const { store, object, seed } = setup([]), rule = addition();
  const match = map(rule.left.target, object, { a: 'v0', b: 'v0' });
  assert.throws(() => planRewrite(store, seed.id, rule, match, { edge: { e: 'loop' } }), code('rule-match-must-be-monic'));
});

test('fresh allocations are explicit and shared allocations block independence', () => {
  const { store, object, seed } = setup([]), rule = addition();
  const match = map(rule.left.target, object, { a: 'v0', b: 'v1' });
  assert.throws(() => planRewrite(store, seed.id, rule, match), code('allocation-domain-mismatch'));
  const a = planRewrite(store, seed.id, rule, match, { edge: { e: 'new-a' } });
  const b = planRewrite(store, seed.id, rule, match, { edge: { e: 'new-b' } });
  const result = proveIndependent(store, a, b), replay = importRevisionBundle(result.bundle);
  assert.deepEqual(replay.state(result.witness.ab.second.outputRevision).object.diagram.sets.edge, ['new-a', 'new-b']);
  assert.throws(() => proveIndependent(store, a, a), code('parallel-allocation-conflict'));
  const installed = applyRewrite(store, seed.id, a);
  const nextMatch = map(rule.left.target, store.state(installed.revision.id).object, { a: 'v0', b: 'v1' });
  assert.throws(() => planRewrite(store, installed.revision.id, rule, nextMatch, { edge: { e: 'new-a' } }), code('allocation-not-fresh'));
});

test('interface and rule-side IDs may differ; retained host IDs stay unchanged', () => {
  const { store, object, seed } = setup([]);
  const k = graph(['k0', 'k1']), l = graph(['a', 'b']), r = graph(['r0', 'r1'], [['z', 'r0', 'r1']]);
  const rule = defineRule('renamed-interface-add', map(k, l, { k0: 'a', k1: 'b' }), map(k, r, { k0: 'r0', k1: 'r1' }));
  const plan = planRewrite(store, seed.id, rule, map(l, object, { a: 'v0', b: 'v1' }), { edge: { z: 'added' } });
  const next = applyRewrite(store, seed.id, plan), d = store.state(next.revision.id).object.diagram;
  assert.deepEqual(d.sets.vertex, ['v0', 'v1', 'v2']); assert.equal(d.maps.source.added, 'v0'); assert.equal(d.maps.target.added, 'v1');
});

test('different rule derivations bind different revisions even for an identical ground effect', () => {
  const { store, object, seed } = setup(), r1 = deletion(), r2 = defineRule('another-deletion-derivation', r1.left, r1.right);
  const match = map(r1.left.target, object, { a: 'v0', b: 'v1' }, { e: 'first' });
  const a = applyRewrite(store, seed.id, planRewrite(store, seed.id, r1, match));
  const b = applyRewrite(store, seed.id, planRewrite(store, seed.id, r2, match));
  assert.equal(a.revision.stateId, b.revision.stateId); assert.notEqual(a.revision.id, b.revision.id);
});

test('identity rules preserve state, but their applied events are not identity history paths', () => {
  const { store, object, seed } = setup();
  const rule = defineRule('identity', attributedIdentity(object), attributedIdentity(object));
  const p = planRewrite(store, seed.id, rule, attributedIdentity(object)), result = applyRewrite(store, seed.id, p);
  assert.equal(result.revision.stateId, seed.stateId); assert.notEqual(result.revision.id, seed.id);
  assert(equalMorphisms(p.retained.map, identity(object.diagram)));
  assert.equal(verifyRewriteWitness(store, result.witness), true);
});

test('witness replay refuses recomputed false claims and incomplete dependency bundles', () => {
  const { store, object, seed } = setup(), rule = deletion();
  const a = planRewrite(store, seed.id, rule, map(rule.left.target, object, { a: 'v0', b: 'v1' }, { e: 'first' }));
  const b = planRewrite(store, seed.id, rule, map(rule.left.target, object, { a: 'v1', b: 'v2' }, { e: 'second' }));
  const result = proveIndependent(store, a, b);
  const bad = clone(result.witness); bad.commonStateId = seed.stateId;
  assert.throws(() => verifyIndependenceWitness(store, retag('isotope-wiring.independence.v1', bad)), code('independence-replay-mismatch'));
  const falseApplication = clone(result.witness.ab.first); falseApplication.afterStateId = seed.stateId;
  assert.throws(() => verifyRewriteWitness(store, retag('isotope-wiring.rule-application.v1', falseApplication)), code('rule-application-replay-mismatch'));
  assert.throws(() => verifyRewriteWitness(createRevisionStore(), result.witness.ab.first), code('missing-revision'));
});

test('an added edge depends on preserved endpoints even though it writes a fresh ID', () => {
  const { store, object, seed } = setup([]), add = addition();
  const a = planRewrite(store, seed.id, add, map(add.left.target, object, { a: 'v0', b: 'v1' }), { edge: { e: 'fresh' } });
  const l = graph(['p']), k = graph([]), remove = defineRule('remove-isolated-vertex', map(k, l, {}), attributedIdentity(k));
  const b = planRewrite(store, seed.id, remove, map(l, object, { p: 'v0' }));
  assert.throws(() => proveIndependent(store, a, b), error => code('delete-read-conflict')(error) && error.detail.some(x => x.id === 'v0'));
});

test('history audits reconstruct rule witnesses and distinguish declarations from checked derivations', () => {
  const { store, object, seed } = setup(), remove = deletion();
  assert.equal(verifyRuleHistory(store).status, 'notApplicable');
  const plan = planRewrite(store, seed.id, remove, map(remove.left.target, object, { a: 'v0', b: 'v1' }, { e: 'first' }));
  const applied = applyRewrite(store, seed.id, plan);
  const replay = importRevisionBundle(store.exportBundle()), before = replay.exportBundle();
  const audit = verifyRuleHistory(replay);
  assert.equal(audit.status, 'verified'); assert.equal(audit.applications.length, 1);
  assert.equal(audit.applications[0].id, applied.witness.id); assert.deepEqual(replay.exportBundle(), before);
  const add = addition(), wrongClaim = store.preparePatch(seed.id, {
    remove: [{ sort: 'edge', id: 'first' }],
    provenance: { kind: 'declared-typed-rule', rule: exportRule(add), match: { vertex: { a: 'v0', b: 'v1' }, edge: {} }, allocation: { edge: { e: 'claimed-new-edge' } } },
  });
  store.applyPatch(seed.id, wrongClaim); // Valid ground edit, deliberately false rule claim.
  assert.throws(() => verifyRuleHistory(importRevisionBundle(store.exportBundle())), code('declared-rule-operation-mismatch'));
});

test('an isotope pair-removal rule keeps shared support, provenance, and model failures', () => {
  const html = readFileSync(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8'), context = vm.createContext({});
  vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], context, { timeout: 5000 });
  const source = JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures().O16));
  const packet = importLegacyAbsolute(source), store = createRevisionStore(), seed = store.seed(packet.object, packet.modelContext);
  const pair = source.graph.pairs[0].id, l = generatedSubdiagram(packet.object, { pair: [pair] });
  const k = subdiagram(l.object, { ...l.object.diagram.sets, pair: [] });
  const rule = defineRule('remove-owned-EP-pair', k.inclusion, attributedIdentity(k.object));
  const plan = planRewrite(store, seed.id, rule, l.inclusion), result = applyRewrite(store, seed.id, plan);
  assert.equal(store.state(result.revision.id).object.diagram.sets.pair.length, 7);
  assert.deepEqual(store.state(result.revision.id).object.diagram.sets.support, packet.object.diagram.sets.support);
  assert.equal(store.verification(result.revision.id), null); assert.equal(store.verifyAt(result.revision.id).result.status, 'refuted');
  assert.equal(store.undo(result.revision.id, result.receipt.id).revision.stateId, seed.stateId);
  const replay = importRevisionBundle(store.exportBundle()); assert.equal(verifyRewriteWitness(replay, result.witness), true);
});
