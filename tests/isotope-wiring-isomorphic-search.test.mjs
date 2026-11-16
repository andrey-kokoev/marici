import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { createDiagram } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { directedGraphSchema as schema } from '../examples/isotope-wiring/core/schemas.mjs';
import { attributeDiagram, attributedMorphism, attributedIdentity, canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { createRevisionStore, importRevisionBundle, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';
import { defineRule, subdiagram, planRewrite, verifyRuleHistory } from '../examples/isotope-wiring/core/rules.mjs';
import { searchRuleJoin, verifyJoinSearch } from '../examples/isotope-wiring/core/join-search.mjs';
import { verifyIsomorphicJoin } from '../examples/isotope-wiring/core/isomorphic-joins.mjs';

function graph(vertices, edges = []) {
  const d = createDiagram(schema, { sets: { vertex: vertices, edge: edges.map(e => e[0]) }, maps: {
    source: Object.fromEntries(edges.map(([e, s]) => [e, s])), target: Object.fromEntries(edges.map(([e, , t]) => [e, t])),
  } });
  return attributeDiagram(d, Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(x => [x, {}]))])));
}
const map = (a, b, vertex, edge = {}) => attributedMorphism(a, b, { vertex, edge });
const code = expected => e => e instanceof RewriteError && e.code === expected;
const mode = { comparison: 'anchoredIsomorphism' };
function peak(fresh = false) {
  const host = graph(['a', 'b'], fresh ? [] : [['u', 'a', 'b'], ['v', 'b', 'a']]);
  const store = createRevisionStore(), seed = store.seed(host);
  let a, b;
  if (fresh) {
    const r = graph(['a', 'b'], [['e', 'a', 'b']]);
    const rule = defineRule('create', attributedIdentity(host), map(host, r, { a: 'a', b: 'b' }));
    a = planRewrite(store, seed.id, rule, attributedIdentity(host), { edge: { e: 'fresh-A' } });
    b = planRewrite(store, seed.id, rule, attributedIdentity(host), { edge: { e: 'fresh-B' } });
  } else {
    const plan = keep => {
      const k = subdiagram(host, { vertex: ['a', 'b'], edge: [keep] });
      const rule = defineRule(`keep-${keep}`, k.inclusion, attributedIdentity(k.object));
      return planRewrite(store, seed.id, rule, attributedIdentity(host));
    };
    a = plan('u'); b = plan('v');
  }
  const l = graph(['p', 'q'], [['e', 'p', 'q']]), k = graph(['p', 'q']);
  const residual = defineRule('delete-edge', map(k, l, { p: 'p', q: 'q' }), attributedIdentity(k));
  return { store, seed, a, b, residual };
}
function retag(report) { const { id, ...body } = report; return { ...body, id: createHash('sha256').update('isotope-wiring.join-search.v1\n' + canonicalJSON(body)).digest('hex') }; }

test('opt-in isomorphic search finds fresh-name joins that the default exact mode does not', () => {
  const { store, seed, a, b } = peak(true); store.setHead('main', null, seed.id);
  const baseline = store.verifyAt(seed.id), before = store.exportBundle();
  const exact = searchRuleJoin(store, a, b, [], { maxDepth: 0 });
  assert.equal(exact.report.status, 'notFound'); assert.deepEqual(exact.report.endpointComparisons, []);
  const result = searchRuleJoin(store, a, b, [], { ...mode, maxDepth: 0 });
  assert.equal(result.report.status, 'joinedUpToIsomorphism'); assert.equal(result.report.endpointComparisons.length, 1);
  assert.equal(result.report.witness.routes.status, 'notJoined');
  assert.equal(verifyIsomorphicJoin(store, result.report.witness), true);
  assert.equal(verifyJoinSearch(importRevisionBundle(result.bundle), JSON.parse(JSON.stringify(result.report))), true);
  assert.deepEqual(store.exportBundle(), before); assert.equal(store.verification(seed.id), baseline);
});

test('automatic anchored search refuses the source swap but discovers valid residual continuations', () => {
  const { store, a, b, residual } = peak();
  const immediate = searchRuleJoin(store, a, b, [], { ...mode, maxDepth: 0 });
  assert.equal(immediate.report.status, 'notFound'); assert.equal(immediate.report.coverage, 'exhaustedDepthBound');
  assert.equal(immediate.report.endpointComparisons[0].status, 'notIsomorphic');
  const result = searchRuleJoin(store, a, b, [residual], { ...mode, maxDepth: 1 });
  assert.equal(result.report.status, 'joinedUpToIsomorphism'); assert.equal(result.report.endpointComparisons.length, 4);
  assert.equal(result.report.witness.routes.left.applications.length, 2); assert.equal(result.report.witness.routes.right.applications.length, 2);
  assert.deepEqual(result.report.witness.comparison.anchors.vertex, { a: 'a', b: 'b' });
  assert.deepEqual(result.report.witness.tracking.lostAfterPeak.vertex, []);
  const replay = importRevisionBundle(result.bundle);
  assert.equal(verifyRuleHistory(replay).applications.length, 4); assert.equal(verifyJoinSearch(replay, result.report), true);
});

test('unknown isomorphism checks propagate incomplete coverage at depth zero', () => {
  const { store, a, b } = peak(true);
  for (const isomorphismOptions of [{ maxSearchNodes: 1 }, { maxRecords: 1 }]) {
    const result = searchRuleJoin(store, a, b, [], { ...mode, maxDepth: 0, isomorphismOptions });
    assert.equal(result.report.status, 'notFound'); assert.equal(result.report.coverage, 'partial');
    assert.equal(result.report.endpointComparisons[0].status, 'unknown');
    assert(result.report.cutoffs.some(c => c.kind === 'isomorphism'));
    assert.equal(verifyJoinSearch(store, result.report), true);
  }
});

test('a global endpoint-comparison cap prevents a false bounded-exhaustion claim', () => {
  const { store, a, b, residual } = peak();
  const result = searchRuleJoin(store, a, b, [residual], { ...mode, maxDepth: 1, maxComparisons: 1 });
  assert.equal(result.report.status, 'notFound'); assert.equal(result.report.coverage, 'partial');
  assert.equal(result.report.endpointComparisons.length, 1); assert(result.report.cutoffs.some(c => c.kind === 'maxComparisons'));
  assert.equal(result.report.discoveredNodes, 3); assert.equal(verifyJoinSearch(store, result.report), true);
  const justRoots = searchRuleJoin(store, a, b, [], { ...mode, maxDepth: 0, maxComparisons: 1 });
  assert.equal(justRoots.report.coverage, 'exhaustedDepthBound');
});

test('later checked joins remain valid after earlier endpoint comparisons were unresolved', () => {
  const { store, a, b, residual } = peak();
  const result = searchRuleJoin(store, a, b, [residual], { ...mode, maxDepth: 1, isomorphismOptions: { maxSearchNodes: 1 } });
  assert.equal(result.report.status, 'joinedUpToIsomorphism'); assert.equal(result.report.coverage, 'stoppedAtJoin');
  assert.equal(result.report.endpointComparisons[0].status, 'unknown');
  assert(result.report.cutoffs.some(c => c.kind === 'isomorphism'));
  assert.equal(result.report.witness.comparison.reason, 'checked-identity');
  assert.equal(verifyIsomorphicJoin(store, result.report.witness), true); assert.equal(verifyJoinSearch(store, result.report), true);
});

test('forged modes, comparison outcomes and erased cutoff claims fail replay after rehashing', () => {
  const { store, a, b } = peak(true);
  const joined = searchRuleJoin(store, a, b, [], { ...mode, maxDepth: 0 }).report;
  const wrongMode = JSON.parse(JSON.stringify(joined)); wrongMode.limits.comparison = 'exact';
  assert.throws(() => verifyJoinSearch(store, retag(wrongMode)), code('join-search-replay-mismatch'));
  const bad = JSON.parse(JSON.stringify(joined)); bad.endpointComparisons[0].status = 'notIsomorphic';
  assert.throws(() => verifyJoinSearch(store, retag(bad)), code('join-search-replay-mismatch'));
  const limited = searchRuleJoin(store, a, b, [], { ...mode, maxDepth: 0, isomorphismOptions: { maxRecords: 1 } }).report;
  assert.throws(() => verifyJoinSearch(store, retag({ ...limited, coverage: 'exhaustedDepthBound', cutoffs: [] })), code('join-search-replay-mismatch'));
});

test('comparison options are validated before traversal and cannot override survivor anchors', () => {
  const { store, a, b } = peak(true);
  assert.throws(() => searchRuleJoin(store, a, b, [], { comparison: 'unanchored' }), code('invalid-join-search-comparison'));
  assert.throws(() => searchRuleJoin(store, a, b, [], { ...mode, maxComparisons: 0 }), code('invalid-join-search-comparison-bound'));
  assert.throws(() => searchRuleJoin(store, a, b, [], { ...mode, maxDepth: 0, isomorphismOptions: { anchors: {} } }), code('invalid-isomorphism-options'));
  assert.throws(() => searchRuleJoin(store, a, b, [], { ...mode, maxDepth: 0, isomorphismOptions: { maxRecords: 0 } }), code('invalid-isomorphism-record-bound'));
});
