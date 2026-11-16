import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import { createDiagram, identity, equalMorphisms, defineSchema } from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import {
  attributeDiagram, attributedMorphism, attributedIdentity, composeAttributed, inverseAttributed,
  supportComponent, supportIdentity, composeSupport, supportInterfacePolicy,
} from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { importLegacyAbsolute } from '../examples/isotope-wiring/core/legacy-adapter.mjs';
import { verifyModel } from '../examples/isotope-wiring/core/model-predicates.mjs';

const html = readFileSync(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8');
const vmContext = vm.createContext({});
vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], vmContext, { timeout: 5000 });
const fixtures = JSON.parse(JSON.stringify(vmContext.IsotopeWiring.fixtures()));
const clone = x => JSON.parse(JSON.stringify(x));
const check = (report, name) => report.checks.find(c => c.predicate === name);
const oxygen = () => importLegacyAbsolute(fixtures.O16);
function relabel(object, mutate) { const labels = clone(object.labels); mutate(labels); return attributeDiagram(object.diagram, labels); }

function boundaryOf(object) {
  const d = object.diagram;
  const sets = Object.fromEntries(d.schema.sorts.map(s => [s, supportInterfacePolicy.excludedSorts.includes(s) ? [] : [...d.sets[s]]]));
  const maps = Object.fromEntries(d.schema.arrows.map(a => [a.name, Object.fromEntries(sets[a.from].map(x => [x, d.maps[a.name][x]]))]));
  const labels = Object.fromEntries(d.schema.sorts.map(s => [s, Object.fromEntries(sets[s].map(x => [x, object.labels[s][x]]))]));
  return attributeDiagram(createDiagram(d.schema, { sets, maps }), labels);
}
function inclusion(a, b) {
  return attributedMorphism(a, b, Object.fromEntries(a.diagram.schema.sorts.map(s => [s, Object.fromEntries(a.diagram.sets[s].map(x => [x, x]))])));
}
function family() {
  const packets = [0, 1, 2, 3].map(oxygen), boundary = boundaryOf(packets[0].object);
  const components = packets.map(p => supportComponent(inclusion(boundary, p.object), inclusion(boundary, p.object)));
  return { boundary, components, packets };
}
function assemble(tree, components) {
  if (Number.isInteger(tree)) {
    const component = components[tree];
    return { component, legs: [attributedIdentity(component.object)], factor: maps => maps[0] };
  }
  const a = assemble(tree[0], components), b = assemble(tree[1], components);
  const { component, gluing } = composeSupport(b.component, a.component);
  return { component, legs: [...a.legs.map(f => composeAttributed(gluing.left, f)), ...b.legs.map(f => composeAttributed(gluing.right, f))],
    factor: maps => gluing.factor(a.factor(maps.slice(0, a.legs.length)), b.factor(maps.slice(a.legs.length))) };
}
function compare(a, b) {
  const f = a.factor(b.legs), inverse = inverseAttributed(f);
  assert(equalMorphisms(composeAttributed(inverse, f).map, identity(a.component.object.diagram)));
  assert(equalMorphisms(composeAttributed(f, a.component.left).map, b.component.left.map));
  assert(equalMorphisms(composeAttributed(f, a.component.right).map, b.component.right.map));
  return f;
}

test('versioned predicates check all nine fixtures without promoting unresolved placement', () => {
  for (const doc of Object.values(fixtures)) {
    const p = importLegacyAbsolute(doc), result = verifyModel(p.object, p.modelContext);
    assert.equal(result.status, doc.id === 'V51-conflict' ? 'refuted' : 'verified', doc.id);
    assert.equal(result.physicalInterpretation, 'not-checked');
    assert.match(result.scope, /no physical interpretation or placement-resolution/);
    assert.equal(result.checks.length, 7);
  }
});

test('missing targets are unknown; malformed or mismatching targets are refuted', () => {
  const p = oxygen();
  const missing = verifyModel(p.object);
  assert.equal(missing.status, 'unknown');
  assert.equal(check(missing, 'inventory-targets').issues[0].code, 'missing-target-input');
  for (const targets of [null, { Z: -1, N: 8, expectedByShell: [2, 6] }, { Z: 9, N: 8, expectedByShell: [2, 6] }])
    assert.equal(verifyModel(p.object, { targets }).status, 'refuted');
  assert.throws(() => verifyModel(p.object, null), /context must be/);
  const extra = verifyModel(p.object, { targets: { Z: 8, N: 8, expectedByShell: [2, 6, 0] } });
  assert(check(extra, 'inventory-targets').issues.some(i => i.code === 'target-without-shell'));
});

test('unsupported schemas are not applicable rather than silently valid', () => {
  const schema = defineSchema({ id: 'different', sorts: ['point'] });
  const object = attributeDiagram(createDiagram(schema, { sets: { point: [] }, maps: {} }), { point: {} });
  const r = verifyModel(object);
  assert.equal(r.status, 'notApplicable'); assert(r.checks.every(c => c.status === 'notApplicable'));
});

test('attribute failure blocks dependent checks instead of producing spurious verification', () => {
  const p = oxygen(), object = relabel(p.object, labels => { labels.shell.s1.size = 'one'; });
  const r = verifyModel(object, p.modelContext);
  assert.equal(check(r, 'attribute-types').status, 'refuted');
  assert.equal(check(r, 'lattice-incidence').status, 'unknown');
  assert.deepEqual(check(r, 'lattice-incidence').blockedBy, ['attribute-types']);
  assert.equal(check(r, 'inventory-targets').status, 'unknown');
});

test('support labels are checked against actual edge endpoints', () => {
  const p = oxygen(), support = p.object.diagram.sets.support[0];
  const object = relabel(p.object, labels => { labels.support[support].endpoints[0].lattice[0] += 1; });
  const r = verifyModel(object, p.modelContext);
  assert.equal(check(r, 'attribute-types').status, 'verified');
  assert.equal(check(r, 'support-incidence').status, 'refuted');
  assert.equal(check(r, 'color-disjointness').status, 'unknown');
});

test('port geometry and duplicate locations cannot pass on count equality', () => {
  const p = oxygen(), object = relabel(p.object, labels => { labels.cell['s2-01'].row = 0; labels.cell['s2-01'].col = 0; });
  const r = verifyModel(object, p.modelContext);
  assert.equal(check(r, 'inventory-targets').status, 'verified');
  assert.equal(check(r, 'lattice-incidence').status, 'refuted');
  assert(check(r, 'lattice-incidence').issues.some(i => i.code === 'duplicate-cell-position'));
  assert.equal(check(r, 'pair-grammar').status, 'unknown');
});

test('wrong route color and duplicate witness records produce localized residuals', () => {
  const source = clone(fixtures.O16);
  source.graph.pairs[0].red = source.graph.pairs[0].blue;
  source.graph.witnesses.push({ ...source.graph.witnesses[0], id: 'duplicate-witness' });
  const p = importLegacyAbsolute(source), r = verifyModel(p.object, p.modelContext);
  assert(check(r, 'pair-grammar').issues.some(i => i.code === 'route-color-direction'));
  assert(check(r, 'color-disjointness').issues.some(i => i.code === 'color-conflict'));
  assert(check(r, 'witness-grammar').issues.some(i => i.code === 'duplicate-witness-slot'));
});

test('receipt input digest binds all labels, incidence, and supplied context', () => {
  const p = oxygen(), a = verifyModel(p.object, p.modelContext), b = verifyModel(p.object, clone(p.modelContext));
  assert.deepEqual(a, b); assert.match(a.inputDigest, /^[a-f0-9]{64}$/);
  const context = clone(p.modelContext); context.targets.Z++;
  assert.notEqual(a.inputDigest, verifyModel(p.object, context).inputDigest);
  const changed = relabel(p.object, labels => { labels.shell.s1.size = 2; });
  assert.notEqual(a.inputDigest, verifyModel(changed, p.modelContext).inputDigest);
  const source = clone(fixtures.O16); source.graph.pairs[0].id = 'renamed-occurrence';
  const renamed = importLegacyAbsolute(source), result = verifyModel(renamed.object, renamed.modelContext);
  assert.notEqual(a.inputDigest, result.inputDigest);
  assert.deepEqual(a.checks.map(c => c.status), result.checks.map(c => c.status));
  assert.throws(() => a.checks.pop(), TypeError);
});

test('policy composition is structurally closed but is not closed under model validity', () => {
  const { components: [a, b], packets } = family();
  assert.equal(verifyModel(a.object, packets[0].modelContext).status, 'verified');
  const { component } = composeSupport(b, a);
  const context = clone(packets[0].modelContext);
  context.targets = { Z: 16, N: 16, expectedByShell: [4, 12] };
  const r = verifyModel(component.object, context);
  assert.equal(check(r, 'inventory-targets').status, 'verified');
  assert.equal(check(r, 'pair-grammar').status, 'refuted');
  assert.equal(check(r, 'witness-grammar').status, 'refuted');
  assert.equal(component.object.diagram.sets.pair.length, 16, 'Do not repair composition by deleting records');
});

test('policy-restricted associativity pentagon preserves every original leg and all attributes', () => {
  const { components } = family();
  const objects = [[[[0, 1], 2], 3], [[0, 1], [2, 3]], [0, [1, [2, 3]]], [0, [[1, 2], 3]], [[0, [1, 2]], 3]].map(t => assemble(t, components));
  const short = composeAttributed(compare(objects[1], objects[2]), compare(objects[0], objects[1]));
  const long = composeAttributed(compare(objects[3], objects[2]), composeAttributed(compare(objects[4], objects[3]), compare(objects[0], objects[4])));
  assert(equalMorphisms(short.map, long.map));
  for (let i = 0; i < 4; i++) assert(equalMorphisms(composeAttributed(short, objects[0].legs[i]).map, objects[2].legs[i].map));
  assert.equal(objects[0].component.object.diagram.sets.pair.length, 32);
});

test('policy coherence also covers distinct vertex-only input/output interfaces', () => {
  const objects = [0, 1, 2].map(() => oxygen().object), first = objects[0], schema = first.diagram.schema;
  const boundaries = [[0, 0], [1, 1], [0, 2], [-1, 1]].map(lattice => {
    const id = first.diagram.sets.vertex.find(v => first.labels.vertex[v].frame === 's1' && JSON.stringify(first.labels.vertex[v].lattice) === JSON.stringify(lattice));
    assert(id);
    const sets = Object.fromEntries(schema.sorts.map(s => [s, s === 'vertex' ? [id] : []]));
    const maps = Object.fromEntries(schema.arrows.map(a => [a.name, {}]));
    const labels = Object.fromEntries(schema.sorts.map(s => [s, s === 'vertex' ? { [id]: first.labels.vertex[id] } : {}]));
    return attributeDiagram(createDiagram(schema, { sets, maps }), labels);
  });
  const components = objects.map((o, i) => supportComponent(inclusion(boundaries[i], o), inclusion(boundaries[i + 1], o)));
  const left = assemble([[0, 1], 2], components), right = assemble([0, [1, 2]], components);
  compare(left, right);
  assert.equal(left.component.object.diagram.sets.vertex.length, 3 * first.diagram.sets.vertex.length - 2);
  assert.equal(left.component.object.diagram.sets.support.length, 3 * first.diagram.sets.support.length);
});

test('policy units and the associator satisfy a triangle comparison', () => {
  const { boundary, components: [a, b] } = family(), unit = supportIdentity(boundary);
  const left = assemble([[0, 1], 2], [a, unit, b]), right = assemble([0, [1, 2]], [a, unit, b]);
  const ab = composeSupport(b, a), seam = composeAttributed(ab.gluing.left, a.right);
  const legs = [ab.gluing.left, seam, ab.gluing.right];
  const reduceLeft = left.factor(legs), reduceRight = right.factor(legs), alpha = compare(left, right);
  inverseAttributed(reduceLeft); inverseAttributed(reduceRight);
  assert(equalMorphisms(reduceLeft.map, composeAttributed(reduceRight, alpha).map));
  assert.throws(() => supportIdentity(a.object), /Owned occurrences/);
});
