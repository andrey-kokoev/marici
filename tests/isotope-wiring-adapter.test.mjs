import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import { createDiagram, identity, equalMorphisms, compose } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { attributeDiagram, attributedMorphism, attributedIdentity, composeAttributed, attributedPushout, glueSupport, supportInterfacePolicy } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { isotopeSupportSchema } from '../examples/isotope-wiring/core/schemas.mjs';
import { importLegacyAbsolute, recoverLegacySource } from '../examples/isotope-wiring/core/legacy-adapter.mjs';

const html = readFileSync(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8');
const context = vm.createContext({});
vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], context, { timeout: 5000 });
const fixtures = JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures()));
const copy = x => JSON.parse(JSON.stringify(x));
const allIdentity = object => identity(object.diagram).components;
function supportInterface(object, { omitEdges = false } = {}) {
  const d = object.diagram;
  const sets = Object.fromEntries(d.schema.sorts.map(s => [s,
    supportInterfacePolicy.excludedSorts.includes(s) || (omitEdges && s === 'edge') ? [] : [...d.sets[s]] ]));
  const maps = Object.fromEntries(d.schema.arrows.map(a => [a.name, Object.fromEntries(sets[a.from].map(x => [x, d.maps[a.name][x]]))]));
  const labels = Object.fromEntries(d.schema.sorts.map(s => [s, Object.fromEntries(sets[s].map(x => [x, object.labels[s][x]]))]));
  return attributeDiagram(createDiagram(d.schema, { sets, maps }), labels);
}
function include(source, target) {
  return attributedMorphism(source, target, Object.fromEntries(source.diagram.schema.sorts.map(s => [s, Object.fromEntries(source.diagram.sets[s].map(x => [x, x]))])));
}

test('all legacy fixtures import structurally and retain their complete sources', () => {
  for (const source of Object.values(fixtures)) {
    const packet = importLegacyAbsolute(source), d = packet.object.diagram;
    assert.deepEqual(recoverLegacySource(packet), source);
    assert.equal(d.sets.pair.length, source.graph.pairs.length);
    assert.equal(d.sets.lineWitness.length + d.sets.boundaryWitness.length, source.graph.witnesses.length);
    assert.equal(packet.report.modelValidity, 'not-checked');
    assert.deepEqual(packet.report.omittedSourceFields, []);
    for (const entries of Object.values(packet.occurrenceMap)) for (const entry of entries) assert(d.sets[entry.sort].includes(entry.id));
  }
  assert.equal(importLegacyAbsolute(fixtures['V51-conflict']).report.status, 'structurally-imported', 'count failure must not be silently repaired or called model-valid');
});

test('extra metadata, history, graph fields, and input order survive retained-source recovery', () => {
  const source = copy(fixtures.O16);
  source.extra = { nested: ['unproved', 7] }; source.graph.extra = { note: 'not incidence' };
  source.graph.pairs[0].annotations = { arbitrary: null }; source.graph.pairs.reverse();
  const before = copy(source), packet = importLegacyAbsolute(source);
  source.extra.nested.push('later mutation');
  assert.deepEqual(recoverLegacySource(packet), before);
  const recovered = recoverLegacySource(packet); recovered.graph.pairs.pop();
  assert.deepEqual(recoverLegacySource(packet), before);
  assert.throws(() => packet.retainedSource.graph.cells.pop(), TypeError);
  assert.throws(() => recoverLegacySource({ ...packet }), /checked adapter/);
});

test('opposite directed routes share undirected support without merging owned pairs', () => {
  const source = {
    kind: 'absolute', id: 'two-routes', graph: {
      shells: [{ id: 's', order: 2, size: 2 }],
      cells: [{ id: 'a', shell: 's', row: 0, col: 0 }, { id: 'b', shell: 's', row: 1, col: 0 }],
      pairs: [
        { id: 'p', shell: 's', cell: 'a', red: ['L', 'B'], blue: ['R', 'B'] },
        { id: 'q', shell: 's', cell: 'b', red: ['R', 'T'], blue: ['T', 'L'] },
      ], witnesses: [],
    },
  };
  const d = importLegacyAbsolute(source).object.diagram;
  assert.equal(d.sets.pair.length, 2);
  const [p, q] = ['p', 'q'].map(id => d.maps.redEdge[id]);
  assert.notEqual(p, q); assert.equal(d.maps.edgeSupport[p], d.maps.edgeSupport[q]);
  assert.equal(d.maps.source[p], d.maps.target[q]); assert.equal(d.maps.target[p], d.maps.source[q]);
});

test('duplicate/ambiguous input is refused and coordinate-concatenation collisions are not introduced', () => {
  const source = { kind: 'absolute', id: 'large', graph: {
    shells: [{ id: 's12', order: 12, size: 12 }],
    cells: [{ id: 'a', shell: 's12', row: 1, col: 10 }, { id: 'b', shell: 's12', row: 11, col: 0 }], pairs: [], witnesses: [],
  } };
  const d = importLegacyAbsolute(source).object.diagram;
  assert.equal(d.sets.cell.length, 2); assert.equal(d.sets.port.length, 8);
  const duplicate = copy(source); duplicate.graph.cells[1].id = 'a';
  assert.throws(() => importLegacyAbsolute(duplicate), /Duplicate cells/);
  const overlap = copy(source); Object.assign(overlap.graph.cells[1], { row: 1, col: 10 });
  assert.throws(() => importLegacyAbsolute(overlap), /Ambiguous overlapping/);
  assert.throws(() => importLegacyAbsolute({ kind: 'delta', id: 'D', base: 'A', ops: [] }), /absolute definition/);
});

test('equal local lattice coordinates in different shells are not silently identified', () => {
  const source = { kind: 'absolute', id: 'frames', graph: {
    shells: [{ id: 's1', order: 1, size: 1 }, { id: 's2', order: 2, size: 2 }],
    cells: [{ id: 'a', shell: 's1', row: 0, col: 0 }, { id: 'b', shell: 's2', row: 0, col: 0 }], pairs: [], witnesses: [],
  } };
  const packet = importLegacyAbsolute(source);
  assert.equal(packet.object.diagram.sets.vertex.length, 8);
  assert(packet.report.interpretationChanges.some(x => x.includes('cross-shell')));
});

test('model labels must match along every attributed map', () => {
  const a = importLegacyAbsolute(fixtures.O16).object;
  const labels = copy(a.labels); labels.shell.s2.size = 3;
  const b = attributeDiagram(a.diagram, labels);
  assert.throws(() => attributedMorphism(a, b, allIdentity(a)), /Model attribute mismatch/);
  const invalid = copy(a.labels); delete invalid.cell;
  assert.throws(() => attributeDiagram(a.diagram, invalid), /sorts mismatch/);
});

test('attributed identities and composition retain model labels; provenance is not an attribute', () => {
  const a = importLegacyAbsolute(fixtures.O16).object;
  const source = copy(fixtures.O16); source.graph.pairs[0].history.push('new provenance');
  const b = importLegacyAbsolute(source).object;
  const f = attributedMorphism(a, b, allIdentity(a));
  assert(equalMorphisms(composeAttributed(attributedIdentity(b), f).map, f.map));
  assert(equalMorphisms(composeAttributed(f, attributedIdentity(a)).map, f.map));
  const p = attributedPushout(attributedIdentity(a), f);
  const h = p.factor(f, attributedIdentity(b));
  assert(equalMorphisms(compose(h.map, p.left.map), f.map));
  assert(equalMorphisms(compose(h.map, p.right.map), identity(b.diagram)));
});

test('support gluing identifies shared support but retains every owned occurrence', () => {
  const a = importLegacyAbsolute(fixtures.O16).object, b = importLegacyAbsolute(fixtures.O16).object;
  const boundary = supportInterface(a), f = include(boundary, a), g = include(boundary, b);
  const p = glueSupport(f, g);
  assert.equal(p.object.diagram.sets.support.length, a.diagram.sets.support.length);
  assert.equal(p.object.diagram.sets.pair.length, 2 * a.diagram.sets.pair.length);
  assert.equal(p.object.diagram.sets.lineWitness.length, 2 * a.diagram.sets.lineWitness.length);
  const factor = p.factor(p.left, p.right);
  assert(equalMorphisms(factor.map, identity(p.object.diagram)));
  assert(equalMorphisms(compose(p.left.map, f.map), compose(p.right.map, g.map)));
  assert.notEqual(p.left.map.components.pair[a.diagram.sets.pair[0]], p.right.map.components.pair[b.diagram.sets.pair[0]]);
});

test('support policy refuses noninjective interface maps even when all labels match', () => {
  function shells(ids) {
    const schema = isotopeSupportSchema;
    const sets = Object.fromEntries(schema.sorts.map(s => [s, s === 'shell' ? ids : []]));
    const maps = Object.fromEntries(schema.arrows.map(a => [a.name, {}]));
    const labels = Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(sets[s].map(id => [id, { order: 1, size: 1 }]))]));
    return attributeDiagram(createDiagram(schema, { sets, maps }), labels);
  }
  const a = shells(['a', 'b']), b = shells(['target']);
  const components = Object.fromEntries(isotopeSupportSchema.sorts.map(s => [s, s === 'shell' ? { a: 'target', b: 'target' } : {}]));
  const f = attributedMorphism(a, b, components);
  assert.throws(() => glueSupport(f, f), /must be injective/);
});

test('interface policy refuses owned occurrences and incomplete shared supports', () => {
  const a = importLegacyAbsolute(fixtures.O16).object;
  const id = attributedMorphism(a, a, allIdentity(a));
  assert.throws(() => glueSupport(id, id), /Owned occurrences/);
  const boundary = supportInterface(a, { omitEdges: true }), f = include(boundary, a);
  assert.throws(() => glueSupport(f, f), /every incident directed edge/);
  // The underlying attributed category remains broader than this policy.
  const p = attributedPushout(id, id);
  assert.equal(p.object.diagram.sets.pair.length, a.diagram.sets.pair.length);
});
