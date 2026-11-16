import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { createDiagram } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { directedGraphSchema as schema } from '../examples/isotope-wiring/core/schemas.mjs';
import { attributeDiagram, attributedMorphism, attributedIdentity, canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { defineRule, checkSuppliedJoin, verifyJoinWitness, proveIndependent, verifyIndependenceWitness } from '../examples/isotope-wiring/core/rules.mjs';
import { enumerateRuleOverlaps, materializeRuleOverlap, verifyOverlapCensus } from '../examples/isotope-wiring/core/overlap-census.mjs';
import { RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';

function graph(vertices, edges = [], label = {}) {
  const d = createDiagram(schema, { sets: { vertex: vertices, edge: edges.map(e => e[0]) }, maps: {
    source: Object.fromEntries(edges.map(([e, s]) => [e, s])), target: Object.fromEntries(edges.map(([e, , t]) => [e, t])),
  } });
  return attributeDiagram(d, Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(d.sets[s].map(x => [x, s === 'vertex' ? label : {}]))])));
}
const map = (a, b, vertex, edge = {}) => attributedMorphism(a, b, { vertex, edge });
const code = expected => error => error instanceof RewriteError && error.code === expected;
function deletion(name = 'delete-edge', label = {}) {
  const k = graph(['a', 'b'], [], label), l = graph(['a', 'b'], [['e', 'a', 'b']], label);
  return defineRule(name, map(k, l, { a: 'a', b: 'b' }), attributedIdentity(k));
}
function retag(census) { const { id, ...body } = census; return { ...body, id: createHash('sha256').update('isotope-wiring.overlap-census.v1\n' + canonicalJSON(body)).digest('hex') }; }

test('complete labelled edge-deletion census has seven independent overlaps and one dependent peak', () => {
  const a = deletion('A'), b = deletion('B'), census = enumerateRuleOverlaps(a, b);
  assert.equal(census.status, 'complete'); assert.equal(census.exhaustedBy, null);
  assert.equal(census.candidates.length, 8);
  assert.deepEqual(census.counts, { independent: 7, dependentPeak: 1, notCoApplicable: 0 });
  assert(census.candidates.every(c => c.analysis.coverage.jointlyCoverIncidence));
  assert.equal(new Set(census.candidates.map(c => c.id)).size, 8);
  assert.equal(verifyOverlapCensus(JSON.parse(JSON.stringify(census))), true);
});

test('node/candidate limits report partial coverage rather than absence of dependent peaks', () => {
  const a = deletion('A'), b = deletion('B');
  const nodes = enumerateRuleOverlaps(a, b, { maxSearchNodes: 1 });
  assert.equal(nodes.status, 'partial'); assert.equal(nodes.exhaustedBy, 'maxSearchNodes'); assert.equal(nodes.candidates.length, 0);
  const prefix = enumerateRuleOverlaps(a, b, { maxCandidates: 1 });
  assert.equal(prefix.status, 'partial'); assert.equal(prefix.exhaustedBy, 'maxCandidates'); assert.equal(prefix.counts.dependentPeak, 0);
  assert.equal(enumerateRuleOverlaps(a, b, { maxCandidates: 8 }).status, 'complete');
  assert.equal(verifyOverlapCensus(prefix), true);
  assert.throws(() => enumerateRuleOverlaps(a, b, { maxPatternRecords: 5 }), code('census-pattern-bound-exceeded'));
});

test('incidence closure, injectivity, and labels constrain candidate identifications', () => {
  const a = deletion('A'), b = deletion('B');
  assert.throws(() => materializeRuleOverlap(a, b, { vertex: {}, edge: { e: 'e' } }), code('overlap-relation-not-closed'));
  assert.throws(() => materializeRuleOverlap(a, b, { vertex: { a: 'a', b: 'a' }, edge: {} }), code('overlap-relation-not-injective'));
  const red = deletion('red', { role: 'red' }), blue = deletion('blue', { role: 'blue' });
  const census = enumerateRuleOverlaps(red, blue);
  assert.equal(census.status, 'complete'); assert.equal(census.candidates.length, 1);
  assert.equal(census.candidates[0].classification, 'independent');
});

test('dangling-rule overlaps are distinguished from co-applicable dependent peaks', () => {
  const edge = deletion(), empty = graph([]), vertex = graph(['v']);
  const removeVertex = defineRule('delete-vertex', map(empty, vertex, {}), attributedIdentity(empty));
  const census = enumerateRuleOverlaps(edge, removeVertex);
  assert.equal(census.status, 'complete'); assert.equal(census.candidates.length, 3);
  assert.deepEqual(census.counts, { independent: 1, dependentPeak: 0, notCoApplicable: 2 });
  assert(census.candidates.filter(c => c.classification === 'notCoApplicable').every(c => c.refusals.some(r => r.side === 'B' && r.code === 'rule-dangling-condition')));
});

test('a dependent census candidate can be materialized and checked for a supplied join', () => {
  const a = deletion('A'), b = deletion('B'), census = enumerateRuleOverlaps(a, b);
  const candidate = census.candidates.find(c => c.classification === 'dependentPeak');
  const concrete = materializeRuleOverlap(a, b, candidate.identifications);
  assert.equal(concrete.candidate.id, candidate.id);
  const joined = checkSuppliedJoin(concrete.store, ...concrete.plans);
  assert.equal(joined.witness.status, 'joined'); assert.equal(verifyJoinWitness(concrete.store, joined.witness), true);
});

test('all independent edge-census candidates produce replayable commuting squares', () => {
  const a = deletion('A'), b = deletion('B');
  for (const c of enumerateRuleOverlaps(a, b).candidates.filter(c => c.classification === 'independent')) {
    const concrete = materializeRuleOverlap(a, b, c.identifications);
    const proof = proveIndependent(concrete.store, ...concrete.plans);
    assert.equal(verifyIndependenceWitness(concrete.store, proof.witness), true);
  }
});

test('isolated-vertex censuses match the partial-bijection counting oracle through size two', () => {
  const counts = [[1, 1, 1], [1, 2, 3], [1, 3, 7]], empty = graph([]);
  for (let n = 0; n <= 2; n++) for (let m = 0; m <= 2; m++) {
    const l = graph(Array.from({ length: n }, (_, i) => `a${i}`));
    const r = graph(Array.from({ length: m }, (_, i) => `b${i}`));
    const a = defineRule('erase-left', map(empty, l, {}), attributedIdentity(empty));
    const b = defineRule('erase-right', map(empty, r, {}), attributedIdentity(empty));
    const census = enumerateRuleOverlaps(a, b);
    assert.equal(census.status, 'complete'); assert.equal(census.candidates.length, counts[n][m]);
    assert.equal(census.counts.independent, 1); assert.equal(census.counts.notCoApplicable, 0);
  }
});

test('empty-pattern creation rules use distinct fresh names rather than artificial allocation conflicts', () => {
  const empty = graph([]), added = graph(['new']);
  const a = defineRule('create-A', attributedIdentity(empty), map(empty, added, {}));
  const b = defineRule('create-B', a.left, a.right);
  const census = enumerateRuleOverlaps(a, b);
  assert.equal(census.status, 'complete'); assert.equal(census.candidates.length, 1);
  assert.equal(census.candidates[0].classification, 'independent');
  const concrete = materializeRuleOverlap(a, b, census.candidates[0].identifications);
  const proof = proveIndependent(concrete.store, ...concrete.plans);
  assert.equal(verifyIndependenceWitness(concrete.store, proof.witness), true);
});

test('census replay refuses forged completeness/count claims even with new hashes', () => {
  const a = deletion('A'), b = deletion('B');
  const partial = JSON.parse(JSON.stringify(enumerateRuleOverlaps(a, b, { maxCandidates: 1 })));
  partial.status = 'complete'; partial.exhaustedBy = null;
  assert.throws(() => verifyOverlapCensus(retag(partial)), code('census-replay-mismatch'));
  const bad = JSON.parse(JSON.stringify(enumerateRuleOverlaps(a, b))); bad.counts.dependentPeak = 0;
  assert.throws(() => verifyOverlapCensus(retag(bad)), code('census-replay-mismatch'));
});
