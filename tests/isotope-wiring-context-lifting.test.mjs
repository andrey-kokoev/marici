import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { createDiagram } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { directedGraphSchema as schema } from '../examples/isotope-wiring/core/schemas.mjs';
import { attributeDiagram, attributedMorphism, attributedIdentity, canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { createRevisionStore, importRevisionBundle, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';
import { defineRule, subdiagram, planRewrite, verifyRuleHistory } from '../examples/isotope-wiring/core/rules.mjs';
import { checkSuppliedIsomorphicJoin } from '../examples/isotope-wiring/core/isomorphic-joins.mjs';
import { liftPersistentJoin, verifyContextLift } from '../examples/isotope-wiring/core/context-lifting.mjs';

function graph(vertices, edges = []) {
  const d = createDiagram(schema, { sets: { vertex: vertices, edge: edges.map(e => e[0]) }, maps: {
    source: Object.fromEntries(edges.map(([e, s]) => [e, s])), target: Object.fromEntries(edges.map(([e, , t]) => [e, t])),
  } });
  return attributeDiagram(d, Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(x => [x, {}]))])));
}
const map = (a, b, vertex, edge = {}) => attributedMorphism(a, b, { vertex, edge });
const code = expected => e => e instanceof RewriteError && e.code === expected;
const persistent = { trackingPolicy: 'persistentAfterPeak' };
function peak(fresh = false) {
  const host = graph(['a', 'b'], fresh ? [] : [['u', 'a', 'b'], ['v', 'b', 'a']]);
  const store = createRevisionStore(), seed = store.seed(host);
  let a, b, left = [], right = [];
  if (fresh) {
    const r = graph(['a', 'b'], [['e', 'a', 'b']]);
    const rule = defineRule('create', attributedIdentity(host), map(host, r, { a: 'a', b: 'b' }));
    a = planRewrite(store, seed.id, rule, attributedIdentity(host), { edge: { e: 'fresh-A' } });
    b = planRewrite(store, seed.id, rule, attributedIdentity(host), { edge: { e: 'fresh-B' } });
  } else {
    const make = keep => {
      const k = subdiagram(host, { vertex: ['a', 'b'], edge: [keep] });
      return planRewrite(store, seed.id, defineRule(`keep-${keep}`, k.inclusion, attributedIdentity(k.object)), attributedIdentity(host));
    };
    a = make('u'); b = make('v');
    const l = graph(['p', 'q'], [['e', 'p', 'q']]), k = graph(['p', 'q']);
    const rule = defineRule('delete-edge', map(k, l, { p: 'p', q: 'q' }), attributedIdentity(k));
    left = [{ rule, match: { vertex: { p: 'a', q: 'b' }, edge: { e: 'u' } } }];
    right = [{ rule, match: { vertex: { p: 'b', q: 'a' }, edge: { e: 'v' } } }];
  }
  const { witness } = checkSuppliedIsomorphicJoin(store, a, b, left, right, persistent);
  return { host, store, seed, a, b, witness };
}
function extension(base, fresh = false) {
  const host = graph(['A', 'B', 'z'], fresh ? [['fresh-A', 'z', 'A']] : [['U', 'A', 'B'], ['V', 'B', 'A'], ['context', 'z', 'A']]);
  const store = createRevisionStore(), seed = store.seed(host, { interpretation: 'larger-context' }, { note: 'retained' });
  const embedding = map(base.host, host, { a: 'A', b: 'B' }, fresh ? {} : { u: 'U', v: 'V' });
  return { store, seed, embedding };
}
function retag(input) { const { id, ...body } = input; return { ...body, id: createHash('sha256').update('isotope-wiring.context-lift.v1\n' + canonicalJSON(body)).digest('hex') }; }

test('persistent joining routes lift through renamed source IDs with incoming context attached to retained vertices', () => {
  const base = peak(), ext = extension(base);
  ext.store.setHead('main', null, ext.seed.id);
  const baseline = ext.store.verifyAt(ext.seed.id), before = ext.store.exportBundle(), baseBefore = base.store.exportBundle();
  const result = liftPersistentJoin(base.store, base.witness, ext.store, ext.seed.id, ext.embedding);
  const c = result.certificate, replay = importRevisionBundle(result.extensionBundle);
  assert.equal(c.status, 'liftedPersistentJoin'); assert.deepEqual(c.outside, { vertex: ['z'], edge: ['context'] });
  assert.deepEqual(replay.state(c.left.outputRevision).object.diagram.sets.edge, ['context']);
  assert.equal(replay.state(c.left.outputRevision).object.diagram.maps.target.context, 'A');
  assert.equal(c.comparison.forward.vertex.z, 'z'); assert.equal(c.comparison.forward.edge.context, 'context');
  assert(c.persistentAfterPeak.vertex.includes('A')); assert(c.persistentAfterPeak.edge.includes('context'));
  assert.equal(verifyRuleHistory(replay).applications.length, 4);
  assert.equal(verifyContextLift(importRevisionBundle(result.baseBundle), replay, JSON.parse(JSON.stringify(c))), true);
  assert.deepEqual(ext.store.exportBundle(), before); assert.deepEqual(base.store.exportBundle(), baseBefore);
  assert.equal(ext.store.verification(ext.seed.id), baseline);
  assert.equal(replay.verification(c.left.outputRevision), null);
});

test('explicit allocation overrides avoid context collisions and extend the fresh-record comparison', () => {
  const base = peak(true), ext = extension(base, true);
  assert.throws(() => liftPersistentJoin(base.store, base.witness, ext.store, ext.seed.id, ext.embedding), code('allocation-not-fresh'));
  const result = liftPersistentJoin(base.store, base.witness, ext.store, ext.seed.id, ext.embedding,
    { allocations: { left: [{ edge: { e: 'extended-A' } }], right: [{ edge: { e: 'extended-B' } }] } });
  const c = result.certificate;
  assert.equal(c.left.embeddings[0].edge['fresh-A'], 'extended-A');
  assert.equal(c.right.embeddings[0].edge['fresh-B'], 'extended-B');
  assert.equal(c.comparison.forward.edge['extended-A'], 'extended-B');
  assert.equal(c.comparison.forward.edge['fresh-A'], 'fresh-A', 'the unrelated context occurrence is fixed');
  assert.notEqual(c.comparison.leftStateId, c.comparison.rightStateId);
  assert.equal(verifyContextLift(base.store, ext.store, c), true);
});

test('later matches follow updated embeddings after fresh-name allocation overrides', () => {
  const base = peak(true), ext = extension(base, true);
  const l = graph(['p', 'q'], [['e', 'p', 'q']]), k = graph(['p', 'q']);
  const remove = defineRule('remove-fresh-edge', map(k, l, { p: 'p', q: 'q' }), attributedIdentity(k));
  const step = name => ({ rule: remove, match: { vertex: { p: 'a', q: 'b' }, edge: { e: name } } });
  const witness = checkSuppliedIsomorphicJoin(base.store, base.a, base.b, [step('fresh-A')], [step('fresh-B')], persistent).witness;
  const result = liftPersistentJoin(base.store, witness, ext.store, ext.seed.id, ext.embedding,
    { allocations: { left: [{ edge: { e: 'extended-A' } }, null], right: [{ edge: { e: 'extended-B' } }, null] } });
  const c = result.certificate, replay = importRevisionBundle(result.extensionBundle);
  assert.equal(c.left.applications[1].spec.match.edge.e, 'extended-A');
  assert.equal(c.right.applications[1].spec.match.edge.e, 'extended-B');
  assert.deepEqual(replay.state(c.left.outputRevision).object.diagram.sets.edge, ['fresh-A']);
  assert.equal(c.comparison.forward.edge['fresh-A'], 'fresh-A');
  assert.equal(verifyContextLift(base.store, ext.store, c), true);
});

test('a larger incoming incidence can obstruct an initial deletion without mutating either caller', () => {
  const small = graph(['x']), empty = graph([]), base = createRevisionStore(), seed = base.seed(small);
  const rule = defineRule('delete-vertex', map(empty, small, {}), attributedIdentity(empty));
  const plan = planRewrite(base, seed.id, rule, attributedIdentity(small));
  const witness = checkSuppliedIsomorphicJoin(base, plan, plan, [], [], persistent).witness;
  const large = graph(['X', 'z'], [['incoming', 'z', 'X']]), ext = createRevisionStore(), target = ext.seed(large);
  const before = ext.exportBundle(), baseBefore = base.exportBundle();
  assert.throws(() => liftPersistentJoin(base, witness, ext, target.id, map(small, large, { x: 'X' })), code('rule-dangling-condition'));
  assert.deepEqual(ext.exportBundle(), before); assert.deepEqual(base.exportBundle(), baseBefore);
});

test('nonmonic embeddings and witnesses without the explicitly certified persistence policy are refused', () => {
  const base = peak(true), target = graph(['X']), ext = createRevisionStore(), seed = ext.seed(target);
  assert.throws(() => liftPersistentJoin(base.store, base.witness, ext, seed.id, map(base.host, target, { a: 'X', b: 'X' })), code('context-embedding-must-be-monic'));
  const full = extension(base, true), weak = checkSuppliedIsomorphicJoin(base.store, base.a, base.b).witness;
  assert.throws(() => liftPersistentJoin(base.store, weak, full.store, full.seed.id, full.embedding), code('context-lift-requires-persistent-join'));
});

test('rehashed false stage embeddings, context coverage and comparison maps fail context replay', () => {
  const base = peak(), ext = extension(base), c = liftPersistentJoin(base.store, base.witness, ext.store, ext.seed.id, ext.embedding).certificate;
  for (const mutate of [
    x => { x.left.embeddings[0].vertex.a = 'absent'; },
    x => { x.outside.edge = []; },
    x => { x.comparison.forward.vertex.z = 'A'; },
  ]) {
    const bad = JSON.parse(JSON.stringify(c)); mutate(bad);
    assert.throws(() => verifyContextLift(base.store, ext.store, retag(bad)), code('context-lift-replay-mismatch'));
  }
});

test('source dependencies and engine bindings are required for context certificates', () => {
  const base = peak(), ext = extension(base), c = liftPersistentJoin(base.store, base.witness, ext.store, ext.seed.id, ext.embedding).certificate;
  assert.throws(() => verifyContextLift(createRevisionStore(), ext.store, c), code('missing-revision'));
  assert.throws(() => verifyContextLift(base.store, createRevisionStore(), c), code('missing-revision'));
  assert.throws(() => verifyContextLift(base.store, ext.store, retag({ ...c, engineDigest: 'other' })), code('context-lift-engine-mismatch'));
});

test('allocation programs have exact route lengths and refusals do not publish partial results', () => {
  const base = peak(true), ext = extension(base, true), before = ext.store.exportBundle();
  assert.throws(() => liftPersistentJoin(base.store, base.witness, ext.store, ext.seed.id, ext.embedding,
    { allocations: { left: [] } }), code('context-lift-allocation-length-or-type'));
  assert.throws(() => liftPersistentJoin(base.store, base.witness, ext.store, ext.seed.id, ext.embedding,
    { allocations: { left: [{ edge: { e: 'fresh-A' } }], right: [null] } }), code('allocation-not-fresh'));
  assert.throws(() => liftPersistentJoin(base.store, base.witness, ext.store, ext.seed.id, ext.embedding,
    { allocations: { left: [{ edge: { e: 'valid-left' } }], right: [{ edge: { e: 'fresh-A' } }] } }), code('allocation-not-fresh'));
  assert.deepEqual(ext.store.exportBundle(), before);
});
