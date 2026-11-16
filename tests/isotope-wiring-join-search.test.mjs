import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { createDiagram } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { directedGraphSchema as schema } from '../examples/isotope-wiring/core/schemas.mjs';
import { attributeDiagram, attributedMorphism, attributedIdentity, canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { createRevisionStore, importRevisionBundle, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';
import { defineRule, subdiagram, planRewrite, checkSuppliedJoin, verifyJoinWitness, verifyRuleHistory } from '../examples/isotope-wiring/core/rules.mjs';
import { searchRuleJoin, verifyJoinSearch } from '../examples/isotope-wiring/core/join-search.mjs';

function graph(vertices, edges = []) {
  const d = createDiagram(schema, { sets: { vertex: vertices, edge: edges.map(e => e[0]) }, maps: {
    source: Object.fromEntries(edges.map(([e, s]) => [e, s])), target: Object.fromEntries(edges.map(([e, , t]) => [e, t])),
  } });
  return attributeDiagram(d, Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(x => [x, {}]))])));
}
const map = (a, b, vertex, edge = {}) => attributedMorphism(a, b, { vertex, edge });
const code = expected => error => error instanceof RewriteError && error.code === expected;
function peak(size = 1) {
  const names = Array.from({ length: size * 2 }, (_, i) => `e${i}`), host = graph(['a', 'b'], names.map(e => [e, 'a', 'b']));
  const store = createRevisionStore(), seed = store.seed(host); store.setHead('main', null, seed.id);
  const make = (name, keep) => {
    const k = subdiagram(host, { vertex: ['a', 'b'], edge: keep });
    return planRewrite(store, seed.id, defineRule(name, k.inclusion, attributedIdentity(k.object)), attributedIdentity(host));
  };
  const a = make('A', names.slice(size)), b = make('B', names.slice(0, size));
  const l = graph(['p', 'q'], [['e', 'p', 'q']]), k = graph(['p', 'q']);
  const residual = defineRule('delete-edge', map(k, l, { p: 'p', q: 'q' }), attributedIdentity(k));
  return { store, seed, a, b, residual, make };
}
function retag(report) { const { id, ...body } = report; return { ...body, id: createHash('sha256').update('isotope-wiring.join-search.v1\n' + canonicalJSON(body)).digest('hex') }; }

test('automatic one-step residual search produces a replayable join without mutating caller history or verification', () => {
  const { store, seed, a, b, residual } = peak();
  const verification = store.verifyAt(seed.id), before = store.exportBundle();
  const result = searchRuleJoin(store, a, b, [residual], { maxDepth: 1 });
  assert.equal(result.report.status, 'joined'); assert.equal(result.report.coverage, 'stoppedAtJoin');
  assert.equal(result.report.witness.left.applications.length, 2); assert.equal(result.report.witness.right.applications.length, 2);
  assert.equal(verifyJoinWitness(store, result.report.witness), true);
  assert.equal(verifyJoinSearch(store, JSON.parse(JSON.stringify(result.report))), true);
  assert.deepEqual(store.exportBundle(), before); assert.equal(store.verification(seed.id), verification);
});

test('two-step joins require sufficient depth and retain alternative equal-state histories during exploration', () => {
  const { store, a, b, residual } = peak(2);
  const shallow = searchRuleJoin(store, a, b, [residual], { maxDepth: 1 });
  assert.equal(shallow.report.status, 'notFound'); assert.equal(shallow.report.coverage, 'exhaustedDepthBound');
  assert.equal(shallow.report.discoveredNodes, 6); assert.equal(shallow.bundle, null);
  const deep = searchRuleJoin(store, a, b, [residual], { maxDepth: 2 });
  assert.equal(deep.report.status, 'joined'); assert.equal(deep.report.discoveredNodes, 9);
  assert.equal(deep.report.witness.left.applications.length, 3); assert.equal(deep.report.witness.right.applications.length, 3);
  assert.notEqual(deep.report.witness.left.outputRevision, deep.report.witness.right.outputRevision);
  assert.equal(verifyJoinSearch(store, shallow.report), true); assert.equal(verifyJoinSearch(store, deep.report), true);
});

test('one-sided continuations and already equal initial endpoints are admitted', () => {
  const { store, a, residual, make } = peak(), erased = make('erase-both', []);
  const one = searchRuleJoin(store, a, erased, [residual], { maxDepth: 1 });
  assert.equal(one.report.status, 'joined');
  assert.equal(one.report.witness.left.applications.length, 2); assert.equal(one.report.witness.right.applications.length, 1);
  const sameEffect = make('A-variant', ['e1']);
  const zero = searchRuleJoin(store, a, sameEffect, [], { maxDepth: 0, maxNodes: 2 });
  assert.equal(zero.report.status, 'joined'); assert.equal(zero.report.expandedNodes, 0); assert.equal(zero.report.discoveredNodes, 2);
  assert.notEqual(zero.report.witness.left.outputRevision, zero.report.witness.right.outputRevision);
});

test('empty rule pools and depth zero make only bounded negative claims despite equal endpoint counts', () => {
  const { store, a, b, residual } = peak();
  for (const result of [searchRuleJoin(store, a, b, []), searchRuleJoin(store, a, b, [residual], { maxDepth: 0 })]) {
    assert.equal(result.report.status, 'notFound'); assert.equal(result.report.coverage, 'exhaustedDepthBound');
    assert.equal(result.report.witness, null); assert.match(result.report.scope, /does not prove nonjoinability/);
  }
});

test('matcher traversal and object bounds propagate partial coverage instead of false exhaustion', () => {
  const { store, a, b, residual } = peak();
  for (const matchOptions of [{ maxSearchNodes: 1 }, { maxHostRecords: 1 }, { maxPatternRecords: 1 }]) {
    const result = searchRuleJoin(store, a, b, [residual], { maxDepth: 1, matchOptions });
    assert.equal(result.report.status, 'notFound'); assert.equal(result.report.coverage, 'partial');
    assert(result.report.cutoffs.length > 0); assert.equal(verifyJoinSearch(store, result.report), true);
  }
});

test('positive joins remain valid when other match branches were cut off', () => {
  const { store, a, b, residual } = peak(2);
  const result = searchRuleJoin(store, a, b, [residual], { maxDepth: 2, matchOptions: { maxMatches: 1 } });
  assert.equal(result.report.status, 'joined'); assert.equal(result.report.coverage, 'stoppedAtJoin');
  assert(result.report.cutoffs.some(c => c.kind === 'matching' && c.exhaustedBy === 'maxMatches'));
  assert.equal(verifyJoinWitness(store, result.report.witness), true); assert.equal(verifyJoinSearch(store, result.report), true);
});

test('global node bounds stop cyclic identity-rule routes without merging their histories', () => {
  const { store, a, b, residual } = peak(), empty = graph([]);
  const noop = defineRule('identity-event', attributedIdentity(empty), attributedIdentity(empty));
  const capped = searchRuleJoin(store, a, b, [noop], { maxDepth: 8, maxNodes: 5 });
  assert.equal(capped.report.status, 'notFound'); assert.equal(capped.report.coverage, 'partial');
  assert.equal(capped.report.discoveredNodes, 5); assert(capped.report.cutoffs.some(c => c.kind === 'maxNodes'));
  const none = searchRuleJoin(store, a, b, [residual], { maxNodes: 2 });
  assert.equal(none.report.coverage, 'partial'); assert.equal(none.report.discoveredNodes, 2);
  assert.equal(verifyJoinSearch(store, capped.report), true);
});

test('returned bundles contain the checked chosen routes, not an assertion that discarded search histories are equal', () => {
  const { store, a, b, residual } = peak(2), result = searchRuleJoin(store, a, b, [residual], { maxDepth: 2 });
  const replay = importRevisionBundle(result.bundle);
  assert.equal(verifyRuleHistory(replay).applications.length, 6);
  assert.deepEqual(replay.state(result.report.witness.left.outputRevision).object.diagram.sets.edge, []);
  assert.equal(verifyJoinSearch(replay, result.report), true);
});

test('rehashed false statuses, coverage and exploration counts fail search replay', () => {
  const { store, a, b, residual } = peak(), partial = searchRuleJoin(store, a, b, [residual], { maxNodes: 2 }).report;
  assert.throws(() => verifyJoinSearch(store, retag({ ...partial, coverage: 'exhaustedDepthBound', cutoffs: [] })), code('join-search-replay-mismatch'));
  assert.throws(() => verifyJoinSearch(store, retag({ ...partial, status: 'joined' })), code('join-search-replay-mismatch'));
  const good = searchRuleJoin(store, a, b, [residual]).report;
  assert.throws(() => verifyJoinSearch(store, retag({ ...good, discoveredNodes: good.discoveredNodes + 1 })), code('join-search-replay-mismatch'));
});

test('allocation-policy exhaustion is not nonjoinability: explicit common fresh names can join a missed peak', () => {
  const { store, a, b } = peak();
  const k = graph(['p', 'q']), l = graph(['p', 'q'], [['e', 'p', 'q']]), r = graph(['p', 'q'], [['f', 'p', 'q']]);
  const replace = defineRule('replace-edge', map(k, l, { p: 'p', q: 'q' }), map(k, r, { p: 'p', q: 'q' }));
  const searched = searchRuleJoin(store, a, b, [replace], { maxDepth: 1 });
  assert.equal(searched.report.status, 'notFound'); assert.equal(searched.report.coverage, 'exhaustedDepthBound');
  assert.equal(searched.report.discoveredNodes, 4);
  const step = edge => ({ rule: replace, match: { vertex: { p: 'a', q: 'b' }, edge: { e: edge } }, allocation: { edge: { f: 'common-fresh-edge' } } });
  const supplied = checkSuppliedJoin(store, a, b, [step('e1')], [step('e0')]);
  assert.equal(supplied.witness.status, 'joined'); assert.equal(verifyJoinWitness(store, supplied.witness), true);
  assert.equal(verifyJoinSearch(store, searched.report), true);
});

test('invalid limits, duplicate rules and unavailable source history are refused', () => {
  const { store, a, b, residual } = peak();
  assert.throws(() => searchRuleJoin(store, a, b, [residual], { maxDepth: null }), code('invalid-join-search-depth'));
  assert.throws(() => searchRuleJoin(store, a, b, [residual], { maxDepth: 9 }), code('invalid-join-search-depth'));
  assert.throws(() => searchRuleJoin(store, a, b, [residual], { maxNodes: 1 }), code('invalid-join-search-node-bound'));
  assert.throws(() => searchRuleJoin(store, a, b, [residual, residual]), code('duplicate-join-search-rule'));
  assert.throws(() => searchRuleJoin(store, a, b, [residual], { maxDepth: 0, matchOptions: { maxMatches: 0 } }), code('invalid-match-limit'));
  const report = searchRuleJoin(store, a, b, [residual]).report;
  assert.throws(() => verifyJoinSearch(createRevisionStore(), report), code('missing-revision'));
});
