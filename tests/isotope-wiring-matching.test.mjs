import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import { importLegacyAbsolute } from '../examples/isotope-wiring/core/legacy-adapter.mjs';
import { createDiagram } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { directedGraphSchema as schema } from '../examples/isotope-wiring/core/schemas.mjs';
import { attributeDiagram, attributedMorphism, attributedIdentity, canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { createRevisionStore, importRevisionBundle, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';
import { defineRule, subdiagram, generatedSubdiagram, planRewrite, applyRewrite, checkSuppliedJoin, verifyJoinWitness } from '../examples/isotope-wiring/core/rules.mjs';
import { enumerateRuleMatches, materializeRuleMatch, verifyRuleMatchCensus } from '../examples/isotope-wiring/core/matching.mjs';

function graph(vertices, edges = [], labels = {}) {
  const d = createDiagram(schema, { sets: { vertex: vertices, edge: edges.map(e => e[0]) }, maps: {
    source: Object.fromEntries(edges.map(([e, s]) => [e, s])), target: Object.fromEntries(edges.map(([e, , t]) => [e, t])),
  } });
  return attributeDiagram(d, Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(x => [x, labels[s]?.[x] ?? {}]))])));
}
const map = (a, b, vertex, edge = {}) => attributedMorphism(a, b, { vertex, edge });
const code = expected => e => e instanceof RewriteError && e.code === expected;
function seeded(host) { const store = createRevisionStore(), seed = store.seed(host); return { store, seed }; }
function deleteEdge(loop = false) {
  const vertices = loop ? ['p'] : ['p', 'q'], l = graph(vertices, [['e', 'p', loop ? 'p' : 'q']]), k = graph(vertices);
  return defineRule('delete-edge', map(k, l, Object.fromEntries(vertices.map(x => [x, x]))), attributedIdentity(k));
}
function retag(x) { const { id, ...body } = x; return { ...body, id: createHash('sha256').update('isotope-wiring.rule-match-census.v1\n' + canonicalJSON(body)).digest('hex') }; }

test('automatic edge matches retain each occurrence, including parallel edges, without mutating the source', () => {
  const { store, seed } = seeded(graph(['a', 'b', 'c'], [['u', 'a', 'b'], ['v', 'a', 'b'], ['w', 'b', 'c']]));
  store.setHead('main', null, seed.id);
  const before = store.exportBundle(), rule = deleteEdge(), census = enumerateRuleMatches(store, seed.id, rule);
  assert.equal(census.status, 'complete'); assert.deepEqual(census.counts, { applicable: 3, dangling: 0 });
  assert.deepEqual(census.matches.map(m => m.components.edge.e).sort(), ['u', 'v', 'w']);
  assert.equal(verifyRuleMatchCensus(importRevisionBundle(before), JSON.parse(JSON.stringify(census))), true);
  assert.deepEqual(store.exportBundle(), before);
  const chosen = materializeRuleMatch(store, seed.id, rule, census.matches[0].components);
  assert.deepEqual(chosen.entry, census.matches[0]);
  const applied = applyRewrite(store, seed.id, chosen.plan);
  assert.equal(store.state(applied.revision.id).object.diagram.sets.edge.length, 2);
  assert.equal(store.head('main'), seed.id);
});

test('isolated-vertex matches agree with the injection-count oracle through size three', () => {
  for (let n = 0; n <= 3; n++) for (let m = 0; m <= 3; m++) {
    const l = graph(Array.from({ length: n }, (_, i) => `p${i}`)), host = graph(Array.from({ length: m }, (_, i) => `h${i}`));
    const rule = defineRule('identity-pattern', attributedIdentity(l), attributedIdentity(l)), { store, seed } = seeded(host);
    const census = enumerateRuleMatches(store, seed.id, rule);
    const expected = n > m ? 0 : Array.from({ length: n }, (_, i) => m - i).reduce((a, b) => a * b, 1);
    assert.equal(census.status, 'complete'); assert.equal(census.counts.applicable, expected); assert.equal(census.counts.dangling, 0);
  }
});

test('naturality and injectivity agree with an independent oracle on all 16 two-vertex simple directed graphs', () => {
  const possibilities = [['aa', 'a', 'a'], ['ab', 'a', 'b'], ['ba', 'b', 'a'], ['bb', 'b', 'b']];
  for (let bits = 0; bits < 16; bits++) {
    const edges = possibilities.filter((_, i) => bits & (1 << i)), { store, seed } = seeded(graph(['a', 'b'], edges));
    for (const loop of [false, true]) {
      const census = enumerateRuleMatches(store, seed.id, deleteEdge(loop));
      const expected = edges.filter(([, a, b]) => (a === b) === loop).length;
      assert.equal(census.status, 'complete'); assert.equal(census.counts.applicable, expected); assert.equal(census.counts.dangling, 0);
    }
  }
});

test('exact model labels filter candidate images rather than being silently transported', () => {
  const l = graph(['p'], [], { vertex: { p: { frame: 'red' } } });
  const rule = defineRule('read-red', attributedIdentity(l), attributedIdentity(l));
  const { store, seed } = seeded(graph(['a', 'b'], [], { vertex: { a: { frame: 'red' }, b: { frame: 'blue' } } }));
  const census = enumerateRuleMatches(store, seed.id, rule);
  assert.equal(census.matches.length, 1); assert.equal(census.matches[0].components.vertex.p, 'a');
});

test('structural vertex matches with dangling deletions are retained as inapplicable matches', () => {
  const l = graph(['p']), k = graph([]), rule = defineRule('remove-vertex', map(k, l, {}), attributedIdentity(k));
  const { store, seed } = seeded(graph(['a', 'b', 'isolated'], [['u', 'a', 'b']]));
  const census = enumerateRuleMatches(store, seed.id, rule);
  assert.equal(census.status, 'complete'); assert.deepEqual(census.counts, { applicable: 1, dangling: 2 });
  assert.equal(census.matches.find(m => m.applicability === 'applicable').components.vertex.p, 'isolated');
  assert(census.matches.filter(m => m.applicability === 'dangling').every(m => m.plan === null && m.refusal.code === 'rule-dangling-condition'));
});

test('bounds distinguish a partial prefix from complete absence and count dangling matches too', () => {
  const l = graph(['p']), rule = defineRule('read', attributedIdentity(l), attributedIdentity(l));
  const { store, seed } = seeded(graph(['a', 'b']));
  const nodes = enumerateRuleMatches(store, seed.id, rule, { maxSearchNodes: 1 });
  assert.equal(nodes.status, 'partial'); assert.equal(nodes.exhaustedBy, 'maxSearchNodes'); assert.equal(nodes.matches.length, 0);
  const prefix = enumerateRuleMatches(store, seed.id, rule, { maxMatches: 1 });
  assert.equal(prefix.status, 'partial'); assert.equal(prefix.exhaustedBy, 'maxMatches'); assert.equal(prefix.matches.length, 1);
  assert.equal(enumerateRuleMatches(store, seed.id, rule, { maxMatches: 2 }).status, 'complete');
  const empty = seeded(graph([]));
  assert.equal(enumerateRuleMatches(empty.store, empty.seed.id, rule, { maxSearchNodes: 1 }).status, 'complete');
  assert.throws(() => enumerateRuleMatches(store, seed.id, rule, { maxHostRecords: 1 }), code('match-object-bound-exceeded'));
  const erase = defineRule('erase', map(graph([]), l, {}), attributedIdentity(graph([])));
  const incident = seeded(graph(['a', 'b'], [['u', 'a', 'b']]));
  const blocked = enumerateRuleMatches(incident.store, incident.seed.id, erase, { maxMatches: 1 });
  assert.equal(blocked.status, 'partial'); assert.equal(blocked.counts.dangling, 1); assert.equal(blocked.counts.applicable, 0);
});

test('empty-pattern creation has one match and deterministic fresh allocations avoid existing names', () => {
  const empty = graph([]), added = graph(['x', 'y']);
  const rule = defineRule('create-two', attributedIdentity(empty), map(empty, added, {}));
  const { store, seed } = seeded(empty), first = enumerateRuleMatches(store, seed.id, rule);
  assert.equal(first.matches.length, 1); assert.equal(new Set(Object.values(first.matches[0].allocation.vertex)).size, 2);
  const concrete = materializeRuleMatch(store, seed.id, rule, first.matches[0].components);
  const next = applyRewrite(store, seed.id, concrete.plan).revision;
  const second = enumerateRuleMatches(store, next.id, rule);
  assert.equal(second.matches.length, 1);
  const old = new Set(Object.values(first.matches[0].allocation.vertex));
  assert(Object.values(second.matches[0].allocation.vertex).every(x => !old.has(x)));
  assert.deepEqual(enumerateRuleMatches(store, next.id, rule), second);
});

test('pattern automorphisms are not quotiented: equal effects retain distinct match provenance', () => {
  const l = graph(['p', 'q']), k = graph([]), rule = defineRule('erase-two', map(k, l, {}), attributedIdentity(k));
  const { store, seed } = seeded(graph(['a', 'b'])), census = enumerateRuleMatches(store, seed.id, rule);
  assert.equal(census.matches.length, 2);
  const outputs = census.matches.map(m => applyRewrite(store, seed.id, materializeRuleMatch(store, seed.id, rule, m.components).plan).revision);
  assert.equal(outputs[0].stateId, outputs[1].stateId); assert.notEqual(outputs[0].id, outputs[1].id);
});

test('census replay refuses forged completeness, incidence and state bindings after rehashing', () => {
  const rule = deleteEdge(), { store, seed } = seeded(graph(['a', 'b'], [['u', 'a', 'b'], ['v', 'a', 'b']]));
  const census = enumerateRuleMatches(store, seed.id, rule, { maxMatches: 1 });
  assert.equal(verifyRuleMatchCensus(store, census), true);
  const falseComplete = JSON.parse(JSON.stringify(census)); falseComplete.status = 'complete'; falseComplete.exhaustedBy = null;
  assert.throws(() => verifyRuleMatchCensus(store, retag(falseComplete)), code('match-census-replay-mismatch'));
  const bad = JSON.parse(JSON.stringify(census)); bad.matches[0].components.vertex.p = 'b';
  assert.throws(() => verifyRuleMatchCensus(store, retag(bad)), code('match-census-replay-mismatch'));
  const wrongState = { ...census, inputStateId: 'wrong' };
  assert.throws(() => verifyRuleMatchCensus(store, retag(wrongState)), code('match-census-replay-mismatch'));
});

test('enumerated plans remain tied to the exact revision even after a metadata-only change', () => {
  const rule = deleteEdge(), { store, seed } = seeded(graph(['a', 'b'], [['u', 'a', 'b']]));
  const census = enumerateRuleMatches(store, seed.id, rule), chosen = materializeRuleMatch(store, seed.id, rule, census.matches[0].components);
  const next = store.applyPatch(seed.id, store.preparePatch(seed.id, { metadataAfter: { note: 'changed' } })).revision;
  assert.throws(() => applyRewrite(store, next.id, chosen.plan), code('stale-rule-boundary'));
  assert.equal(verifyRuleMatchCensus(store, census), true, 'old snapshot remains a valid source');
  const current = enumerateRuleMatches(store, next.id, rule);
  assert.deepEqual(current.matches[0].components, census.matches[0].components); assert.notEqual(current.id, census.id);
});

test('the isotope pair-removal occurrence is discovered without inferring a model-validity guarantee', () => {
  const context = vm.createContext({});
  vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8').match(/<script>([\s\S]*?)<\/script>/)[1], context, { timeout: 5000 });
  const fixture = JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures().O16)), packet = importLegacyAbsolute(fixture);
  const store = createRevisionStore(), seed = store.seed(packet.object, packet.modelContext), pair = fixture.graph.pairs[0].id;
  const l = generatedSubdiagram(packet.object, { pair: [pair] }), k = subdiagram(l.object, { ...l.object.diagram.sets, pair: [] });
  const rule = defineRule('remove-owned-pair', k.inclusion, attributedIdentity(k.object));
  const census = enumerateRuleMatches(store, seed.id, rule, { maxHostRecords: 4096, maxSearchNodes: 100000 });
  assert.equal(census.status, 'complete');
  const found = census.matches.find(m => canonicalJSON(m.components) === canonicalJSON(l.inclusion.map.components));
  assert(found); assert.equal(found.applicability, 'applicable');
  const chosen = materializeRuleMatch(store, seed.id, rule, found.components);
  const next = applyRewrite(store, seed.id, chosen.plan).revision;
  assert.equal(store.state(next.id).object.diagram.sets.pair.length, 7);
  assert.equal(store.verification(next.id), null); assert.equal(store.verifyAt(next.id).result.status, 'refuted');
});

test('automatically found residual matches can discharge an explicitly selected joining route', () => {
  const host = graph(['a', 'b', 'c'], [['u', 'a', 'b'], ['v', 'b', 'c']]), { store, seed } = seeded(host);
  const ka = subdiagram(host, { vertex: ['a', 'b', 'c'], edge: ['v'] }), kb = subdiagram(host, { vertex: ['a', 'b', 'c'], edge: ['u'] });
  const ra = defineRule('remove-u', ka.inclusion, attributedIdentity(ka.object)), rb = defineRule('remove-v', kb.inclusion, attributedIdentity(kb.object));
  const a = planRewrite(store, seed.id, ra, attributedIdentity(host)), b = planRewrite(store, seed.id, rb, attributedIdentity(host));
  const immediate = checkSuppliedJoin(store, a, b), scratch = importRevisionBundle(immediate.bundle), residual = deleteEdge();
  assert.equal(immediate.witness.status, 'notJoined');
  const route = branch => {
    const census = enumerateRuleMatches(scratch, immediate.witness[branch].outputRevision, residual);
    assert.equal(census.status, 'complete'); assert.equal(census.counts.applicable, 1);
    const found = census.matches[0]; return [{ rule: residual, match: found.components, allocation: found.allocation }];
  };
  const joined = checkSuppliedJoin(store, a, b, route('left'), route('right'));
  assert.equal(joined.witness.status, 'joined'); assert.equal(verifyJoinWitness(store, joined.witness), true);
});
