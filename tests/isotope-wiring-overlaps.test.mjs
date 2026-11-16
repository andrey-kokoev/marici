import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { createDiagram } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { directedGraphSchema as schema } from '../examples/isotope-wiring/core/schemas.mjs';
import { attributeDiagram, attributedMorphism, attributedIdentity, canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { createRevisionStore, importRevisionBundle, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';
import { subdiagram, defineRule, planRewrite, proveIndependent, analyzeOverlap, checkSuppliedJoin, verifyJoinWitness, verifyRuleHistory } from '../examples/isotope-wiring/core/rules.mjs';

function graph(vertices, edges = []) {
  const d = createDiagram(schema, { sets: { vertex: vertices, edge: edges.map(e => e[0]) },
    maps: { source: Object.fromEntries(edges.map(([e, s]) => [e, s])), target: Object.fromEntries(edges.map(([e, , t]) => [e, t])) } });
  return attributeDiagram(d, Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(id => [id, {}]))])));
}
const map = (a, b, vertex, edge = {}) => attributedMorphism(a, b, { vertex, edge });
const code = value => e => e instanceof RewriteError && e.code === value;
function peak(outside = false) {
  const l = graph(['a', 'b', 'c'], [['u', 'a', 'b'], ['v', 'b', 'c']]);
  const x = outside ? graph(['a', 'b', 'c', 'outside'], [['u', 'a', 'b'], ['v', 'b', 'c']]) : l;
  const store = createRevisionStore(), seed = store.seed(x);
  const kA = subdiagram(l, { vertex: ['a', 'b', 'c'], edge: ['v'] }), kB = subdiagram(l, { vertex: ['a', 'b', 'c'], edge: ['u'] });
  const ruleA = defineRule('remove-u-retain-v', kA.inclusion, attributedIdentity(kA.object));
  const ruleB = defineRule('remove-v-retain-u', kB.inclusion, attributedIdentity(kB.object));
  const match = map(l, x, { a: 'a', b: 'b', c: 'c' }, { u: 'u', v: 'v' });
  const a = planRewrite(store, seed.id, ruleA, match), b = planRewrite(store, seed.id, ruleB, match);
  const small = graph(['p', 'q'], [['e', 'p', 'q']]), k = graph(['p', 'q']);
  const residual = defineRule('remove-residual-edge', map(k, small, { p: 'p', q: 'q' }), attributedIdentity(k));
  const left = [{ rule: residual, match: { vertex: { p: 'b', q: 'c' }, edge: { e: 'v' } } }];
  const right = [{ rule: residual, match: { vertex: { p: 'a', q: 'b' }, edge: { e: 'u' } } }];
  return { store, seed, a, b, left, right, match };
}
function retag(x) { const { id, ...body } = x; return { ...body, id: createHash('sha256').update('isotope-wiring.supplied-join.v1\n' + canonicalJSON(body)).digest('hex') }; }

test('overlap analysis records conflicting occurrences and joint incidence coverage', () => {
  const { store, a, b } = peak(), analysis = analyzeOverlap(store, a, b);
  assert.equal(analysis.independenceCriterion, 'not-satisfied'); assert.equal(analysis.deleteRead.length, 2);
  assert.equal(analysis.shared.length, 5); assert.equal(analysis.coverage.jointlyCoverIncidence, true);
  assert.throws(() => proveIndependent(store, a, b), code('delete-read-conflict'));
  const larger = peak(true), context = analyzeOverlap(larger.store, larger.a, larger.b);
  assert.equal(context.coverage.jointlyCoverIncidence, false); assert.deepEqual(context.coverage.uncovered.vertex, ['outside']);
});

test('shared preserved records are not reported as deletion conflicts', () => {
  const host = graph(['a', 'b', 'c'], [['u', 'a', 'b'], ['v', 'b', 'c']]);
  const l = graph(['p', 'q'], [['e', 'p', 'q']]), k = graph(['p', 'q']);
  const rule = defineRule('delete-one-edge', map(k, l, { p: 'p', q: 'q' }), attributedIdentity(k));
  const store = createRevisionStore(), seed = store.seed(host);
  const a = planRewrite(store, seed.id, rule, map(l, host, { p: 'a', q: 'b' }, { e: 'u' }));
  const b = planRewrite(store, seed.id, rule, map(l, host, { p: 'b', q: 'c' }, { e: 'v' }));
  const result = analyzeOverlap(store, a, b);
  assert.equal(result.independenceCriterion, 'conditions-satisfied');
  assert.deepEqual(result.shared, [{ sort: 'vertex', id: 'b', aDeletes: false, bDeletes: false }]);
  assert.deepEqual(result.deleteRead, []);
});

test('equal counts do not establish a join, and a failed supplied route is not nonjoinability', () => {
  const { store, a, b } = peak(), before = store.exportBundle();
  const result = checkSuppliedJoin(store, a, b);
  assert.equal(result.witness.status, 'notJoined');
  assert.match(result.witness.scope, /do not prove nonjoinability/);
  const replay = importRevisionBundle(result.bundle);
  assert.equal(replay.state(result.witness.left.outputRevision).object.diagram.sets.edge.length, 1);
  assert.equal(replay.state(result.witness.right.outputRevision).object.diagram.sets.edge.length, 1);
  assert.notEqual(result.witness.leftStateId, result.witness.rightStateId);
  assert.deepEqual(store.exportBundle(), before);
});

test('overlapping rules rejected by independence can join through supplied residual rules', () => {
  const { store, a, b, left, right } = peak(), before = store.exportBundle();
  const result = checkSuppliedJoin(store, a, b, left, right), w = result.witness;
  assert.equal(w.status, 'joined'); assert.equal(w.leftStateId, w.rightStateId);
  assert.notEqual(w.left.outputRevision, w.right.outputRevision);
  assert.equal(w.left.applications.length, 2); assert.equal(w.right.applications.length, 2);
  assert.equal(verifyJoinWitness(store, JSON.parse(JSON.stringify(w))), true);
  const replay = importRevisionBundle(result.bundle);
  assert.deepEqual(replay.state(w.left.outputRevision).object.diagram.sets.edge, []);
  assert.equal(verifyRuleHistory(replay).applications.length, 4);
  assert.deepEqual(store.exportBundle(), before);
});

test('a zero-continuation join does not identify distinct derivation histories', () => {
  const { store, seed, a, match } = peak();
  const variant = defineRule('same-effect-different-rule', a.rule.left, a.rule.right);
  const b = planRewrite(store, seed.id, variant, match);
  assert.equal(analyzeOverlap(store, a, b).deleteRead.length, 2);
  const w = checkSuppliedJoin(store, a, b).witness;
  assert.equal(w.status, 'joined'); assert.notEqual(w.left.outputRevision, w.right.outputRevision);
  assert.equal(w.left.applications.length, 1); assert.equal(w.right.applications.length, 1);
});

test('fresh-ID conflict is distinguished from deletion overlap and does not prove an unjoinable peak', () => {
  const k = graph(['p', 'q']), r = graph(['p', 'q'], [['e', 'p', 'q']]);
  const store = createRevisionStore(), seed = store.seed(k);
  const ruleA = defineRule('add-A', attributedIdentity(k), map(k, r, { p: 'p', q: 'q' }));
  const ruleB = defineRule('add-B', ruleA.left, ruleA.right);
  const a = planRewrite(store, seed.id, ruleA, attributedIdentity(k), { edge: { e: 'same-name' } });
  const b = planRewrite(store, seed.id, ruleB, attributedIdentity(k), { edge: { e: 'same-name' } });
  const analysis = analyzeOverlap(store, a, b);
  assert.equal(analysis.deleteRead.length, 0); assert.deepEqual(analysis.allocations, [{ sort: 'edge', id: 'same-name' }]);
  assert.throws(() => proveIndependent(store, a, b), code('parallel-allocation-conflict'));
  assert.equal(checkSuppliedJoin(store, a, b).witness.status, 'joined');
});

test('joining routes obey explicit bounds and invalid matches never mutate the source store', () => {
  const { store, a, b, left, right } = peak(), before = store.exportBundle();
  assert.throws(() => checkSuppliedJoin(store, a, b, left, right, { maxStepsPerBranch: 0 }), code('join-bound-exceeded'));
  assert.throws(() => checkSuppliedJoin(store, a, b, [], [], { maxStepsPerBranch: 65 }), code('invalid-join-bound'));
  const wrong = [{ ...left[0], match: { vertex: { p: 'b', q: 'c' }, edge: { e: 'already-deleted' } } }];
  assert.throws(() => checkSuppliedJoin(store, a, b, wrong, right), /Unbound morphism image/);
  assert.deepEqual(store.exportBundle(), before);
});

test('join witnesses are replayed rather than trusted by status or recomputed digest', () => {
  const { store, a, b, left, right } = peak();
  const bad = JSON.parse(JSON.stringify(checkSuppliedJoin(store, a, b).witness)); bad.status = 'joined';
  assert.throws(() => verifyJoinWitness(store, retag(bad)), code('join-replay-mismatch'));
  const good = checkSuppliedJoin(store, a, b, left, right).witness;
  assert.throws(() => verifyJoinWitness(createRevisionStore(), good), code('missing-revision'));
});
