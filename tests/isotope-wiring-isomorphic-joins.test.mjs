import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import { importLegacyAbsolute } from '../examples/isotope-wiring/core/legacy-adapter.mjs';
import { createDiagram } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { directedGraphSchema as schema } from '../examples/isotope-wiring/core/schemas.mjs';
import { attributeDiagram, attributedMorphism, attributedIdentity, inverseAttributed, canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { createRevisionStore, importRevisionBundle, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';
import { defineRule, subdiagram, planRewrite } from '../examples/isotope-wiring/core/rules.mjs';
import { compareRevisionStates, verifyStateComparison, checkSuppliedIsomorphicJoin, verifyIsomorphicJoin } from '../examples/isotope-wiring/core/isomorphic-joins.mjs';

function graph(vertices, edges = [], labels = {}) {
  const d = createDiagram(schema, { sets: { vertex: vertices, edge: edges.map(e => e[0]) }, maps: {
    source: Object.fromEntries(edges.map(([e, s]) => [e, s])), target: Object.fromEntries(edges.map(([e, , t]) => [e, t])),
  } });
  return attributeDiagram(d, Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(x => [x, labels[s]?.[x] ?? {}]))])));
}
const map = (a, b, vertex, edge = {}) => attributedMorphism(a, b, { vertex, edge });
const code = expected => e => e instanceof RewriteError && e.code === expected;
const clone = x => JSON.parse(JSON.stringify(x));
function retag(domain, input) { const { id, ...body } = input; return { ...body, id: createHash('sha256').update(domain + '\n' + canonicalJSON(body)).digest('hex') }; }
function freshPeak() {
  const host = graph(['a', 'b']), k = graph(['p', 'q']), r = graph(['p', 'q'], [['e', 'p', 'q']]);
  const store = createRevisionStore(), seed = store.seed(host);
  const ra = defineRule('create-A', attributedIdentity(k), map(k, r, { p: 'p', q: 'q' }));
  const rb = defineRule('create-B', ra.left, ra.right), match = map(k, host, { p: 'a', q: 'b' });
  const a = planRewrite(store, seed.id, ra, match, { edge: { e: 'fresh-A' } });
  const b = planRewrite(store, seed.id, rb, match, { edge: { e: 'fresh-B' } });
  return { store, seed, a, b };
}

test('renamed parallel incidence has a checked bijection and inverse, not merely equal counts', () => {
  const x = graph(['a', 'b'], [['u', 'a', 'b'], ['v', 'a', 'b']]);
  const y = graph(['x', 'y'], [['r', 'x', 'y'], ['s', 'x', 'y']]);
  const store = createRevisionStore(), left = store.seed(x), right = store.seed(y);
  const report = compareRevisionStates(store, left.id, right.id);
  assert.equal(report.status, 'isomorphic'); assert.equal(report.forward.vertex.a, 'x');
  assert.equal(new Set(Object.values(report.forward.edge)).size, 2);
  assert.deepEqual(inverseAttributed(attributedMorphism(x, y, report.forward)).map.components, report.inverse);
  assert.equal(verifyStateComparison(store, clone(report)), true);
});

test('equal sort counts cannot hide changed incidence or changed labels', () => {
  const store = createRevisionStore(), left = store.seed(graph(['a', 'b'], [['u', 'a', 'b']]));
  const loop = store.seed(graph(['x', 'y'], [['v', 'x', 'x']]));
  assert.equal(compareRevisionStates(store, left.id, loop.id).status, 'notIsomorphic');
  const red = store.seed(graph(['r'], [], { vertex: { r: { color: 'red' } } }));
  const blue = store.seed(graph(['b'], [], { vertex: { b: { color: 'blue' } } }));
  assert.equal(compareRevisionStates(store, red.id, blue.id).status, 'notIsomorphic');
});

test('comparison bounds return unknown; checked identity needs no permutation search', () => {
  const store = createRevisionStore(), left = store.seed(graph(['a', 'b'], [['u', 'a', 'b']]));
  const right = store.seed(graph(['x', 'y'], [['v', 'x', 'y']]));
  for (const [options, reason] of [[{ maxSearchNodes: 1 }, 'maxSearchNodes'], [{ maxRecords: 2 }, 'maxRecords']]) {
    const report = compareRevisionStates(store, left.id, right.id, options);
    assert.equal(report.status, 'unknown'); assert.equal(report.reason, reason); assert.equal(verifyStateComparison(store, report), true);
  }
  const identity = compareRevisionStates(store, left.id, left.id, { maxSearchNodes: 1, maxRecords: 1 });
  assert.equal(identity.status, 'isomorphic'); assert.equal(identity.reason, 'checked-identity'); assert.equal(identity.searchNodes, 0);
});

test('context and metadata are held literally fixed rather than renamed or silently ignored', () => {
  const host = graph(['a']), store = createRevisionStore(), left = store.seed(host, { target: 1 }, { source: 'a' });
  const context = store.seed(host, { target: 2 }, { source: 'a' }), metadata = store.seed(host, { target: 1 }, { source: 'b' });
  for (const right of [context, metadata]) {
    const report = compareRevisionStates(store, left.id, right.id);
    assert.equal(report.status, 'notCompared'); assert.equal(report.forward, null);
    assert.equal(verifyStateComparison(store, report), true);
  }
});

test('fresh-name differences admit an anchored supplied isomorphic join while exact states and histories stay distinct', () => {
  const { store, seed, a, b } = freshPeak(); store.setHead('main', null, seed.id);
  const before = store.exportBundle(), result = checkSuppliedIsomorphicJoin(store, a, b);
  assert.equal(result.witness.status, 'joinedUpToIsomorphism'); assert.equal(result.witness.routes.status, 'notJoined');
  assert.deepEqual(result.witness.comparison.anchors.vertex, { a: 'a', b: 'b' });
  assert.equal(result.witness.comparison.forward.edge['fresh-A'], 'fresh-B');
  assert.notEqual(result.witness.routes.leftStateId, result.witness.routes.rightStateId);
  assert.notEqual(result.witness.routes.left.outputRevision, result.witness.routes.right.outputRevision);
  assert.equal(verifyIsomorphicJoin(importRevisionBundle(result.bundle), clone(result.witness)), true);
  assert.deepEqual(store.exportBundle(), before);
  assert.equal(checkSuppliedIsomorphicJoin(store, a, b, [], [], { maxSearchNodes: 1 }).witness.status, 'unknown');
});

test('an unanchored graph isomorphism cannot swap surviving source occurrences in a supplied join', () => {
  const host = graph(['a', 'b'], [['u', 'a', 'b'], ['v', 'b', 'a']]), store = createRevisionStore(), seed = store.seed(host);
  const make = (name, keep) => {
    const k = subdiagram(host, { vertex: ['a', 'b'], edge: [keep] });
    return planRewrite(store, seed.id, defineRule(name, k.inclusion, attributedIdentity(k.object)), attributedIdentity(host));
  };
  const result = checkSuppliedIsomorphicJoin(store, make('A', 'u'), make('B', 'v'));
  assert.equal(result.witness.status, 'notJoined');
  const replay = importRevisionBundle(result.bundle), routes = result.witness.routes;
  assert.equal(compareRevisionStates(replay, routes.left.outputRevision, routes.right.outputRevision).status, 'isomorphic');
  assert.equal(verifyIsomorphicJoin(store, result.witness), true);
});

test('deleting and recreating the same spelling does not restore source-occurrence tracking', () => {
  const host = graph(['x']), empty = graph([]), store = createRevisionStore(), seed = store.seed(host);
  const ra = defineRule('identity-A', attributedIdentity(host), attributedIdentity(host));
  const rb = defineRule('identity-B', ra.left, ra.right);
  const a = planRewrite(store, seed.id, ra, attributedIdentity(host)), b = planRewrite(store, seed.id, rb, attributedIdentity(host));
  const del = defineRule('delete-x', map(empty, host, {}), attributedIdentity(empty));
  const add = defineRule('recreate-x', attributedIdentity(empty), map(empty, host, {}));
  const result = checkSuppliedIsomorphicJoin(store, a, b, [
    { rule: del, match: { vertex: { x: 'x' }, edge: {} } },
    { rule: add, match: { vertex: {}, edge: {} }, allocation: { vertex: { x: 'x' } } },
  ]);
  assert.equal(result.witness.status, 'joinedUpToIsomorphism'); assert.equal(result.witness.routes.status, 'joined');
  assert.deepEqual(result.witness.tracking.afterPeak.vertex, ['x']);
  assert.deepEqual(result.witness.tracking.atEnd.vertex, []); assert.deepEqual(result.witness.tracking.lostAfterPeak.vertex, ['x']);
  assert.equal(verifyIsomorphicJoin(store, result.witness), true);
  const forged = clone(result.witness); forged.tracking.lostAfterPeak.vertex = [];
  assert.throws(() => verifyIsomorphicJoin(store, retag('isotope-wiring.isomorphic-join.v1', forged)), code('isomorphic-join-replay-mismatch'));
});

test('all 256 ordered pairs of two-vertex simple directed graphs agree with an independent swap oracle', () => {
  const store = createRevisionStore(), pairs = [[0, 0], [0, 1], [1, 0], [1, 1]];
  const make = (prefix, bits) => {
    const names = [`${prefix}0`, `${prefix}1`];
    return store.seed(graph(names, pairs.flatMap(([a, b], i) => bits & (1 << i) ? [[`${prefix}e${i}`, names[a], names[b]]] : [])));
  };
  const left = Array.from({ length: 16 }, (_, i) => make('l', i)), right = Array.from({ length: 16 }, (_, i) => make('r', i));
  const swap = bits => ((bits & 1) << 3) | ((bits & 2) << 1) | ((bits & 4) >> 1) | ((bits & 8) >> 3);
  for (let i = 0; i < 16; i++) for (let j = 0; j < 16; j++) {
    const report = compareRevisionStates(store, left[i].id, right[j].id);
    assert.equal(report.status, i === j || swap(i) === j ? 'isomorphic' : 'notIsomorphic');
  }
});

test('rehashed false maps and unknown-to-negative promotions fail comparison replay', () => {
  const store = createRevisionStore(), left = store.seed(graph(['a', 'b'])), right = store.seed(graph(['x', 'y']));
  const report = compareRevisionStates(store, left.id, right.id), bad = clone(report); bad.forward.vertex.b = bad.forward.vertex.a;
  assert.throws(() => verifyStateComparison(store, retag('isotope-wiring.state-comparison.v1', bad)), code('state-comparison-replay-mismatch'));
  const inverse = clone(report); inverse.inverse.vertex.x = 'absent';
  assert.throws(() => verifyStateComparison(store, retag('isotope-wiring.state-comparison.v1', inverse)), code('state-comparison-replay-mismatch'));
  const limited = compareRevisionStates(store, left.id, right.id, { maxSearchNodes: 1 });
  assert.throws(() => verifyStateComparison(store, retag('isotope-wiring.state-comparison.v1', { ...limited, status: 'notIsomorphic' })), code('state-comparison-replay-mismatch'));
});

test('an isotope occurrence renaming preserves checked incidence but does not inherit a model report', () => {
  const context = vm.createContext({});
  vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8').match(/<script>([\s\S]*?)<\/script>/)[1], context, { timeout: 5000 });
  const packet = importLegacyAbsolute(JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures().O16)));
  const x = packet.object, d = x.diagram, old = d.sets.pair[0];
  const names = Object.fromEntries(d.schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(id => [id, s === 'pair' && id === old ? 'renamed-pair' : id]))]));
  const y = attributeDiagram(createDiagram(d.schema, {
    sets: Object.fromEntries(d.schema.sorts.map(s => [s, d.sets[s].map(id => names[s][id])])),
    maps: Object.fromEntries(d.schema.arrows.map(a => [a.name, Object.fromEntries(d.sets[a.from].map(id => [names[a.from][id], names[a.to][d.maps[a.name][id]]]))])),
  }), Object.fromEntries(d.schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(id => [names[s][id], x.labels[s][id]]))])));
  const store = createRevisionStore(), left = store.seed(x, packet.modelContext), right = store.seed(y, packet.modelContext);
  const before = store.verifyAt(left.id);
  const report = compareRevisionStates(store, left.id, right.id, { anchors: names, maxRecords: 128 });
  assert.equal(report.status, 'isomorphic'); assert.deepEqual(report.forward, names);
  assert.equal(store.verification(right.id), null);
  const fresh = store.verifyAt(right.id);
  assert.equal(fresh.result.status, 'verified'); assert.notEqual(fresh.result.inputDigest, before.result.inputDigest);
});

test('invalid anchors, limits and missing source histories are refused', () => {
  const store = createRevisionStore(), left = store.seed(graph(['a', 'b'])), right = store.seed(graph(['x', 'y']));
  assert.throws(() => compareRevisionStates(store, left.id, right.id, { anchors: { vertex: { a: 'x', b: 'x' } } }), code('isomorphism-anchors-not-injective'));
  assert.throws(() => compareRevisionStates(store, left.id, right.id, { anchors: { vertex: { a: 'absent' } } }), code('isomorphism-anchor-outside-object'));
  assert.throws(() => compareRevisionStates(store, left.id, right.id, { maxSearchNodes: 0 }), code('invalid-isomorphism-node-bound'));
  const report = compareRevisionStates(store, left.id, right.id);
  assert.throws(() => verifyStateComparison(createRevisionStore(), report), code('missing-revision'));
});
