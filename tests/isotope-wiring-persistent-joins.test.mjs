import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { createDiagram } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { directedGraphSchema as schema } from '../examples/isotope-wiring/core/schemas.mjs';
import { attributeDiagram, attributedMorphism, attributedIdentity, canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { createRevisionStore, importRevisionBundle, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';
import { defineRule, subdiagram, planRewrite, verifyRuleHistory } from '../examples/isotope-wiring/core/rules.mjs';
import { checkSuppliedIsomorphicJoin, verifyIsomorphicJoin } from '../examples/isotope-wiring/core/isomorphic-joins.mjs';
import { searchRuleJoin, verifyJoinSearch } from '../examples/isotope-wiring/core/join-search.mjs';

function graph(vertices, edges = []) {
  const d = createDiagram(schema, { sets: { vertex: vertices, edge: edges.map(e => e[0]) }, maps: {
    source: Object.fromEntries(edges.map(([e, s]) => [e, s])), target: Object.fromEntries(edges.map(([e, , t]) => [e, t])),
  } });
  return attributeDiagram(d, Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(x => [x, {}]))])));
}
const map = (a, b, vertex, edge = {}) => attributedMorphism(a, b, { vertex, edge });
const persistent = { trackingPolicy: 'persistentAfterPeak' };
const searchOptions = { comparison: 'anchoredIsomorphism', ...persistent, maxDepth: 1 };
const code = expected => e => e instanceof RewriteError && e.code === expected;
function peak(asymmetric = false) {
  const host = graph(['a', 'b'], [['u', 'a', 'b'], ['v', 'b', 'a']]), store = createRevisionStore(), seed = store.seed(host);
  const make = (name, keep) => {
    const k = subdiagram(host, { vertex: ['a', 'b'], edge: keep });
    return planRewrite(store, seed.id, defineRule(name, k.inclusion, attributedIdentity(k.object)), attributedIdentity(host));
  };
  const a = make('A', asymmetric ? ['u', 'v'] : ['u']), b = make('B', ['v']);
  const l = graph(['p', 'q'], [['e', 'p', 'q']]), vertices = graph(['p', 'q']), empty = graph([]);
  const erase = defineRule('erase-component', map(empty, l, {}), attributedIdentity(empty));
  const preserve = defineRule('delete-edge-only', map(vertices, l, { p: 'p', q: 'q' }), attributedIdentity(vertices));
  const eraseAll = defineRule('erase-both-edges', map(empty, host, {}), attributedIdentity(empty));
  return { store, seed, a, b, erase, preserve, eraseAll };
}
function retag(domain, input) { const { id, ...body } = input; return { ...body, id: createHash('sha256').update(domain + '\n' + canonicalJSON(body)).digest('hex') }; }

test('equal empty endpoints are a weak join but fail persistent post-peak occurrence preservation', () => {
  const { store, a, b, erase } = peak();
  const left = [{ rule: erase, match: { vertex: { p: 'a', q: 'b' }, edge: { e: 'u' } } }];
  const right = [{ rule: erase, match: { vertex: { p: 'b', q: 'a' }, edge: { e: 'v' } } }];
  const weak = checkSuppliedIsomorphicJoin(store, a, b, left, right);
  assert.equal(weak.witness.status, 'joinedUpToIsomorphism'); assert.equal(weak.witness.routes.status, 'joined');
  const strong = checkSuppliedIsomorphicJoin(store, a, b, left, right, persistent);
  assert.equal(strong.witness.status, 'trackingLost'); assert.equal(strong.witness.comparison, null);
  assert.deepEqual(strong.witness.tracking.lostOnLeft.vertex, ['a', 'b']);
  assert.deepEqual(strong.witness.tracking.lostOnRight.vertex, ['a', 'b']);
  assert.equal(verifyIsomorphicJoin(importRevisionBundle(strong.bundle), strong.witness), true);
});

test('automatic search rejects lost-track candidates and continues to a preserving route', () => {
  const { store, seed, a, b, erase, preserve } = peak(); store.setHead('main', null, seed.id);
  const before = store.exportBundle(), baseline = store.verifyAt(seed.id);
  const weak = searchRuleJoin(store, a, b, [erase, preserve], { comparison: 'anchoredIsomorphism', maxDepth: 1 });
  assert.equal(weak.report.status, 'joinedUpToIsomorphism');
  assert.deepEqual(weak.report.witness.tracking.lostAfterPeak.vertex, ['a', 'b']);
  const result = searchRuleJoin(store, a, b, [erase, preserve], searchOptions);
  assert.equal(result.report.status, 'joinedUpToIsomorphism');
  assert(result.report.endpointComparisons.some(c => c.admission === 'trackingLost'));
  assert.deepEqual(result.report.witness.tracking.lostAfterPeak.vertex, []);
  for (const side of ['left', 'right']) assert.equal(result.report.witness.routes.continuations[side][0].rule.name, 'delete-edge-only');
  assert.equal(verifyJoinSearch(store, JSON.parse(JSON.stringify(result.report))), true);
  assert.equal(verifyRuleHistory(importRevisionBundle(result.bundle)).applications.length, 4);
  assert.deepEqual(store.exportBundle(), before); assert.equal(store.verification(seed.id), baseline);
});

test('a complete bounded search can reject every candidate by tracking without claiming global nonjoinability', () => {
  const { store, a, b, erase } = peak();
  const result = searchRuleJoin(store, a, b, [erase], searchOptions);
  assert.equal(result.report.status, 'notFound'); assert.equal(result.report.coverage, 'exhaustedDepthBound');
  assert.equal(result.report.endpointComparisons.filter(c => c.admission === 'trackingLost').length, 3);
  assert.deepEqual(result.report.cutoffs, []); assert.match(result.report.scope, /does not prove nonjoinability/);
  assert.equal(verifyJoinSearch(store, result.report), true);
});

test('known tracking failure is a decided rejection even when graph comparison would exceed record limits', () => {
  const { store, a, b, erase, eraseAll } = peak(true);
  const result = searchRuleJoin(store, a, b, [erase, eraseAll], { ...searchOptions, isomorphismOptions: { maxRecords: 1, maxSearchNodes: 1 } });
  assert.equal(result.report.status, 'notFound'); assert.equal(result.report.coverage, 'exhaustedDepthBound');
  assert.equal(result.report.endpointComparisons[0].reason, 'sort-cardinality-mismatch');
  const rejected = result.report.endpointComparisons.filter(c => c.admission === 'trackingLost');
  assert(rejected.length > 0); assert(rejected.every(c => c.comparisonId === null && c.searchNodes === 0 && c.reason === 'persistent-source-loss'));
  assert.deepEqual(result.report.cutoffs, []); assert.equal(verifyJoinSearch(store, result.report), true);
});

test('one-sided deletion and recreation cannot repair source tracking despite exact endpoint equality', () => {
  const host = graph(['x']), empty = graph([]), store = createRevisionStore(), seed = store.seed(host);
  const identity = defineRule('identity', attributedIdentity(host), attributedIdentity(host));
  const a = planRewrite(store, seed.id, identity, attributedIdentity(host));
  const erase = defineRule('erase-x', map(empty, host, {}), attributedIdentity(empty));
  const add = defineRule('add-x', attributedIdentity(empty), map(empty, host, {}));
  const result = checkSuppliedIsomorphicJoin(store, a, a, [
    { rule: erase, match: { vertex: { x: 'x' }, edge: {} } },
    { rule: add, match: { vertex: {}, edge: {} }, allocation: { vertex: { x: 'x' } } },
  ], [], persistent);
  assert.equal(result.witness.routes.status, 'joined'); assert.equal(result.witness.status, 'trackingLost');
  assert.deepEqual(result.witness.tracking.lostOnLeft.vertex, ['x']); assert.deepEqual(result.witness.tracking.lostOnRight.vertex, []);
  assert.equal(verifyIsomorphicJoin(store, result.witness), true);
});

test('initial deletions are excluded from persistence requirements and the empty requirement is well defined', () => {
  const { store, a, b, preserve } = peak();
  const result = searchRuleJoin(store, a, b, [preserve], searchOptions);
  assert.equal(result.report.status, 'joinedUpToIsomorphism');
  assert.deepEqual(result.report.witness.tracking.afterPeak.edge, []);
  const host = graph(['x']), empty = graph([]), other = createRevisionStore(), seed = other.seed(host);
  const rule = defineRule('erase-initial', map(empty, host, {}), attributedIdentity(empty));
  const p = planRewrite(other, seed.id, rule, attributedIdentity(host));
  const vacuous = checkSuppliedIsomorphicJoin(other, p, p, [], [], persistent);
  assert.equal(vacuous.witness.status, 'joinedUpToIsomorphism'); assert.deepEqual(vacuous.witness.tracking.afterPeak.vertex, []);
});

test('policy substitution and false rejection counts fail replay; unsupported policy/mode combinations are refused', () => {
  const { store, a, b, erase } = peak();
  const weak = searchRuleJoin(store, a, b, [erase], { comparison: 'anchoredIsomorphism', maxDepth: 1 }).report;
  const changedWitness = JSON.parse(JSON.stringify(weak.witness)); changedWitness.trackingPolicy = 'persistentAfterPeak';
  assert.throws(() => verifyIsomorphicJoin(store, retag('isotope-wiring.isomorphic-join.v1', changedWitness)), code('isomorphic-join-replay-mismatch'));
  const forged = JSON.parse(JSON.stringify(weak)); forged.limits.trackingPolicy = 'persistentAfterPeak';
  assert.throws(() => verifyJoinSearch(store, retag('isotope-wiring.join-search.v1', forged)), code('join-search-replay-mismatch'));
  const strong = searchRuleJoin(store, a, b, [erase], searchOptions).report;
  const bad = JSON.parse(JSON.stringify(strong)); bad.endpointComparisons.find(c => c.admission === 'trackingLost').lostPersistentCount = 0;
  assert.throws(() => verifyJoinSearch(store, retag('isotope-wiring.join-search.v1', bad)), code('join-search-replay-mismatch'));
  assert.throws(() => searchRuleJoin(store, a, b, [], persistent), code('persistent-tracking-requires-anchored-comparison'));
  assert.throws(() => checkSuppliedIsomorphicJoin(store, a, b, [], [], { trackingPolicy: 'ignore' }), code('invalid-join-tracking-policy'));
});
