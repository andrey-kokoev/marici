import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { createDiagram, equalMorphisms } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { directedGraphSchema as schema } from '../examples/isotope-wiring/core/schemas.mjs';
import { attributeDiagram, attributedMorphism, attributedIdentity, composeAttributed, canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { createRevisionStore, importRevisionBundle, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';
import { defineRule, planRewrite, verifyRuleHistory } from '../examples/isotope-wiring/core/rules.mjs';
import { checkSuppliedIsomorphicJoin } from '../examples/isotope-wiring/core/isomorphic-joins.mjs';
import { extendContextEmbedding } from '../examples/isotope-wiring/core/context-lifting.mjs';
import { checkContextLiftComposition, verifyContextLiftComposition } from '../examples/isotope-wiring/core/context-composition.mjs';

function graph(vertices, edges = []) {
  const d = createDiagram(schema, { sets: { vertex: vertices, edge: edges.map(e => e[0]) }, maps: {
    source: Object.fromEntries(edges.map(([e, s]) => [e, s])), target: Object.fromEntries(edges.map(([e, , t]) => [e, t])),
  } });
  return attributeDiagram(d, Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(x => [x, {}]))])));
}
const map = (a, b, vertex, edge = {}) => attributedMorphism(a, b, { vertex, edge });
const code = expected => e => e instanceof RewriteError && e.code === expected;
function base(remove = false) {
  const host = graph(['a', 'b']), r = graph(['a', 'b'], [['e', 'a', 'b']]);
  const store = createRevisionStore(), seed = store.seed(host);
  const rule = defineRule('create-edge', attributedIdentity(host), map(host, r, { a: 'a', b: 'b' }));
  const a = planRewrite(store, seed.id, rule, attributedIdentity(host), { edge: { e: 'fresh-A' } });
  const b = planRewrite(store, seed.id, rule, attributedIdentity(host), { edge: { e: 'fresh-B' } });
  let left = [], right = [];
  if (remove) {
    const k = graph(['p', 'q']), l = graph(['p', 'q'], [['e', 'p', 'q']]);
    const del = defineRule('delete-fresh', map(k, l, { p: 'p', q: 'q' }), attributedIdentity(k));
    const step = edge => ({ rule: del, match: { vertex: { p: 'a', q: 'b' }, edge: { e: edge } } });
    left = [step('fresh-A')]; right = [step('fresh-B')];
  }
  const witness = checkSuppliedIsomorphicJoin(store, a, b, left, right, { trackingPolicy: 'persistentAfterPeak' }).witness;
  return { store, seed, host, witness, a };
}
function level(prefix, count, collision = false) {
  const vertices = Array.from({ length: count }, (_, i) => `${prefix}${i}`);
  const edges = Array.from({ length: count - 2 }, (_, i) => [`${prefix}c${i + 2}`, `${prefix}${i + 2}`, `${prefix}${i === 0 ? 0 : i + 1}`]);
  if (collision) edges.push(['mid-A', vertices.at(-1), vertices[1]]);
  const host = graph(vertices, edges), store = createRevisionStore(), seed = store.seed(host, { level: prefix }, { level: prefix });
  return { host, store, seed };
}
function intoBase(b, h) { return map(b.host, h.host, { a: h.host.diagram.sets.vertex[0], b: h.host.diagram.sets.vertex[1] }); }
function inclusion(h, k) {
  return map(h.host, k.host,
    Object.fromEntries(h.host.diagram.sets.vertex.map((x, i) => [x, k.host.diagram.sets.vertex[i]])),
    Object.fromEntries(h.host.diagram.sets.edge.map((x, i) => [x, k.host.diagram.sets.edge.filter(e => e !== 'mid-A')[i]])));
}
const allocations = (prefix, remove = false) => Object.fromEntries(['left', 'right'].map((side, i) => [side,
  [{ edge: { e: `${prefix}-${i === 0 ? 'A' : 'B'}` } }, ...(remove ? [null] : [])]]));
const run = (b, h, k, i, j, options = {}) => checkContextLiftComposition(b.store, b.witness, h.store, h.seed.id, i, k.store, k.seed.id, j, options);
function retag(input) { const { id, ...body } = input; return { ...body, id: createHash('sha256').update('isotope-wiring.context-composition.v1\n' + canonicalJSON(body)).digest('hex') }; }

test('two-stage context lifts commute at every creation/deletion step without changing caller stores', () => {
  const b = base(true), h = level('h', 3), k = level('k', 4), i = intoBase(b, h), j = inclusion(h, k);
  const snapshots = [b, h, k].map(x => x.store.exportBundle());
  const result = run(b, h, k, i, j, { middleAllocations: allocations('mid', true), outerAllocations: allocations('outer', true) });
  const c = result.certificate;
  assert.equal(c.status, 'coherentContextLiftComposition');
  assert.equal(c.stages.left.embeddings.length, 2);
  assert.equal(c.stages.left.embeddings[0].edge['mid-A'], 'outer-A');
  assert.deepEqual(Object.keys(c.stages.left.embeddings[1].edge), ['hc2']);
  assert.deepEqual(c.comparisonSquare.viaOuter, c.comparisonSquare.viaMiddle);
  assert.deepEqual(c.stagedOutside, { vertex: ['k3'], edge: ['kc3'] });
  assert.equal(c.persistentImages.vertex.h2, 'k2');
  const bs = importRevisionBundle(result.baseBundle), hs = importRevisionBundle(result.middleBundle), ks = importRevisionBundle(result.outerBundle);
  assert.equal(verifyContextLiftComposition(bs, hs, ks, JSON.parse(JSON.stringify(c))), true);
  assert.equal(verifyRuleHistory(hs).applications.length, 4); assert.equal(verifyRuleHistory(ks).applications.length, 4);
  assert.deepEqual([b, h, k].map(x => x.store.exportBundle()), snapshots);
});

test('outer default allocations inherit middle choices rather than resetting to base spellings', () => {
  const b = base(), h = level('h', 3), k = level('k', 4);
  const c = run(b, h, k, intoBase(b, h), inclusion(h, k), { middleAllocations: allocations('mid') }).certificate;
  assert.equal(c.direct.allocations.left[0].edge.e, 'mid-A');
  assert.equal(c.stages.left.embeddings[0].edge['mid-A'], 'mid-A');
  assert.equal(c.direct.comparison.forward.edge['mid-A'], 'mid-B');
  assert.equal(verifyContextLiftComposition(b.store, h.store, k.store, c), true);
});

test('identity contexts satisfy concrete left and right unit checks at the exact revision boundaries', () => {
  const b = base(), h = level('h', 3), i = intoBase(b, h);
  const left = run(b, b, h, attributedIdentity(b.host), i).certificate;
  assert.deepEqual(left.first.left.applications, b.witness.routes.left.applications);
  for (const component of Object.values(left.first.left.embeddings[0])) assert(Object.entries(component).every(([x, y]) => x === y));
  const right = run(b, h, h, i, attributedIdentity(h.host), { middleAllocations: allocations('mid') }).certificate;
  assert.deepEqual(right.first.left.applications, right.direct.left.applications);
  for (const component of Object.values(right.stages.left.embeddings[0])) assert(Object.entries(component).every(([x, y]) => x === y));
  assert.equal(verifyContextLiftComposition(b.store, h.store, h.store, right), true);
});

test('three concrete contexts agree under reassociation with fixed allocation programs', () => {
  const b = base(), h = level('h', 3), k = level('k', 4), l = level('l', 5);
  const i = intoBase(b, h), j = inclusion(h, k), t = inclusion(k, l);
  const first = run(b, h, k, i, j, { middleAllocations: allocations('mid'), outerAllocations: allocations('outer') });
  const left = run(b, k, l, composeAttributed(j, i), t, { middleAllocations: allocations('outer'), outerAllocations: allocations('last') });
  const right = run(b, h, l, i, composeAttributed(t, j), { middleAllocations: allocations('mid'), outerAllocations: allocations('last') });
  assert.equal(left.certificate.direct.id, right.certificate.direct.id);
  const hs = importRevisionBundle(first.middleBundle), ks = importRevisionBundle(first.outerBundle), ls = importRevisionBundle(left.outerBundle);
  for (const side of ['left', 'right']) {
    const H = hs.state(first.certificate.first[side].outputRevision).object;
    const K = ks.state(first.certificate.direct[side].outputRevision).object;
    const L = ls.state(left.certificate.direct[side].outputRevision).object;
    const jk = attributedMorphism(H, K, first.certificate.stages[side].embeddings[0]);
    const kl = attributedMorphism(K, L, left.certificate.stages[side].embeddings[0]);
    const jl = attributedMorphism(H, L, right.certificate.stages[side].embeddings[0]);
    assert(equalMorphisms(composeAttributed(kl, jk).map, jl.map));
  }
});

test('a nonmonic second embedding is refused even when its composite on the base is monic', () => {
  const b = base(), h = level('h', 3), i = intoBase(b, h);
  const host = graph(['x', 'y'], [['loop', 'x', 'x']]), store = createRevisionStore(), seed = store.seed(host);
  const j = map(h.host, host, { h0: 'x', h1: 'y', h2: 'x' }, { hc2: 'loop' });
  assert.throws(() => run(b, h, { host, store, seed }, i, j), code('context-composition-second-must-be-monic'));
  assert.throws(() => extendContextEmbedding(attributedIdentity(b.host), { ...b.a }, b.a), code('unchecked-rule-plan'));
});

test('outer allocation collisions refuse staged defaults without mutating earlier contexts', () => {
  const b = base(), h = level('h', 3), k = level('k', 4, true), snapshots = [b, h, k].map(x => x.store.exportBundle());
  assert.throws(() => run(b, h, k, intoBase(b, h), inclusion(h, k), { middleAllocations: allocations('mid') }), code('allocation-not-fresh'));
  assert.deepEqual([b, h, k].map(x => x.store.exportBundle()), snapshots);
  const result = run(b, h, k, intoBase(b, h), inclusion(h, k), { middleAllocations: allocations('mid'), outerAllocations: allocations('outer') });
  assert.equal(result.certificate.direct.comparison.forward.edge['mid-A'], 'mid-A');
});

test('false stage maps and comparison-square claims fail replay even with recomputed hashes', () => {
  const b = base(), h = level('h', 3), k = level('k', 4), c = run(b, h, k, intoBase(b, h), inclusion(h, k)).certificate;
  for (const mutate of [
    x => { x.stages.left.embeddings[0].vertex.h0 = 'absent'; },
    x => { x.comparisonSquare.viaMiddle.edge.hc2 = 'absent'; },
    x => { x.direct.outside.edge = []; },
    x => { x.stagedOutside.edge = []; },
    x => { x.persistentImages.vertex.h2 = 'k0'; },
  ]) {
    const bad = JSON.parse(JSON.stringify(c)); mutate(bad);
    assert.throws(() => verifyContextLiftComposition(b.store, h.store, k.store, retag(bad)), code('context-composition-replay-mismatch'));
  }
});

test('composition certificates require all source dependencies, current engines and exact allocation lengths', () => {
  const b = base(), h = level('h', 3), k = level('k', 4), i = intoBase(b, h), j = inclusion(h, k), c = run(b, h, k, i, j).certificate;
  assert.throws(() => verifyContextLiftComposition(b.store, createRevisionStore(), k.store, c), code('missing-revision'));
  assert.throws(() => verifyContextLiftComposition(b.store, h.store, k.store, retag({ ...c, engineDigest: 'other' })), code('context-composition-engine-mismatch'));
  assert.throws(() => run(b, h, k, i, j, { outerAllocations: { left: [] } }), code('context-composition-allocation-shape'));
});
