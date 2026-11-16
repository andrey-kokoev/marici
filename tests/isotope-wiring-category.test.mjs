import test from 'node:test';
import assert from 'node:assert/strict';
import {
  defineSchema, createDiagram, createMorphism, identity, compose,
  equalDiagrams, equalMorphisms, isMonomorphism, inverse, initial, initialMap,
  pushout, coproduct, pullback, product, terminal, terminalMap, equalizer, coequalizer,
  openComponent, identityComponent, composeOpen,
} from '../examples/isotope-wiring/core/finite-diagrams.mjs';
import { directedGraphSchema as graphSchema, isotopeIncidenceSchema } from '../examples/isotope-wiring/core/schemas.mjs';

const setSchema = defineSchema({ id: 'test.finite-set.v1', sorts: ['item'] });
const finiteSet = n => createDiagram(setSchema, { sets: { item: Array.from({ length: n }, (_, i) => `x${i}`) }, maps: {} });
function functions(domain, codomain) {
  if (!domain.length) return [{}];
  const [head, ...tail] = domain;
  return functions(tail, codomain).flatMap(rest => codomain.map(y => ({ ...rest, [head]: y })));
}
const setMaps = (a, b) => functions(a.sets.item, b.sets.item).map(item => createMorphism(a, b, { item }));
const graph = (vertices, edges) => createDiagram(graphSchema, {
  sets: { vertex: vertices, edge: edges.map(e => e[0]) },
  maps: { source: Object.fromEntries(edges.map(([e, s]) => [e, s])), target: Object.fromEntries(edges.map(([e, , t]) => [e, t])) },
});
const mapGraph = (a, b, vertex, edge = {}) => createMorphism(a, b, { vertex, edge });

test('checked finite diagrams reject dangling incidences and wrong domains', () => {
  assert.throws(() => graph(['a'], [['e', 'a', 'missing']]), /Unbound incidence/);
  assert.throws(() => graph(['a', 'a'], []), /Duplicate record/);
  assert.throws(() => createDiagram(graphSchema, { sets: { vertex: [], edge: [] }, maps: { source: {}, target: { phantom: 'a' } } }), /keys do not match/);
  assert.throws(() => identity({ sets: {}, maps: {} }), /checked diagram/);
  const d = graph(['a'], []);
  assert.throws(() => d.sets.vertex.push('b'), TypeError);
});

test('schema equations and structural naturality are checked, not assumed', () => {
  const involution = defineSchema({ id: 'test.involution', sorts: ['point'], arrows: [{ name: 'flip', from: 'point', to: 'point' }], equations: [{ at: 'point', left: ['flip', 'flip'], right: [] }] });
  assert.throws(() => createDiagram(involution, { sets: { point: ['a', 'b'] }, maps: { flip: { a: 'b', b: 'b' } } }), /equation fails/);
  assert.throws(() => defineSchema({ id: 'bad', sorts: ['point'], equations: [{ at: 'point', left: ['absent'], right: [] }] }), /not composable/);
  const a = graph(['s', 't'], [['e', 's', 't']]);
  assert.throws(() => mapGraph(a, a, { s: 't', t: 's' }, { e: 'e' }), /Naturality fails/);
});

test('identity and associativity hold for all maps on a two-element finite set', () => {
  const d = finiteSet(2), maps = setMaps(d, d);
  for (const f of maps) {
    assert(equalMorphisms(compose(identity(d), f), f));
    assert(equalMorphisms(compose(f, identity(d)), f));
    for (const g of maps) for (const h of maps)
      assert(equalMorphisms(compose(h, compose(g, f)), compose(compose(h, g), f)));
  }
  assert.throws(() => compose(identity(finiteSet(1)), identity(d)), /boundary mismatch/);
});

test('same schema ID does not admit a different presentation; map data has exact domains', () => {
  const alien = defineSchema({ id: graphSchema.id, sorts: ['vertex', 'edge'] });
  const a = graph([], []), b = createDiagram(alien, { sets: { vertex: [], edge: [] }, maps: {} });
  assert.throws(() => createMorphism(a, b, { vertex: {}, edge: {} }), /Schema mismatch/);
  const d = finiteSet(1);
  assert.throws(() => createMorphism(d, d, { item: {} }), /keys do not match/);
});

test('pointwise pushouts satisfy existence and uniqueness over all spans of sets of size at most two', t => {
  let spans = 0, cocones = 0;
  const sets = [0, 1, 2].map(finiteSet);
  for (const k of sets) for (const a of sets) for (const b of sets)
    for (const f of setMaps(k, a)) for (const g of setMaps(k, b)) {
      const p = pushout(f, g); spans++;
      assert(equalMorphisms(compose(p.left, f), compose(p.right, g)));
      if (isMonomorphism(f)) assert(isMonomorphism(p.right));
      if (isMonomorphism(g)) assert(isMonomorphism(p.left));
      for (const z of sets) for (const u of setMaps(a, z)) for (const v of setMaps(b, z)) {
        if (!equalMorphisms(compose(u, f), compose(v, g))) {
          assert.throws(() => p.factor(u, v), /does not commute/); continue;
        }
        const h = p.factor(u, v); cocones++;
        assert(equalMorphisms(compose(h, p.left), u));
        assert(equalMorphisms(compose(h, p.right), v));
        const candidates = setMaps(p.object, z).filter(m => equalMorphisms(compose(m, p.left), u) && equalMorphisms(compose(m, p.right), v));
        assert.equal(candidates.length, 1);
        assert(equalMorphisms(candidates[0], h));
      }
    }
  t.diagnostic(`${spans} spans, ${cocones} compatible cocones; target sets bounded by size two`);
});

test('pointwise pullbacks satisfy existence and uniqueness over cospans of sets of size at most two', t => {
  let cospans = 0, cones = 0;
  const sets = [0, 1, 2].map(finiteSet);
  for (const c of sets) for (const a of sets) for (const b of sets)
    for (const f of setMaps(a, c)) for (const g of setMaps(b, c)) {
      const p = pullback(f, g); cospans++;
      assert(equalMorphisms(compose(f, p.left), compose(g, p.right)));
      if (isMonomorphism(f)) assert(isMonomorphism(p.right));
      if (isMonomorphism(g)) assert(isMonomorphism(p.left));
      for (const z of sets) for (const u of setMaps(z, a)) for (const v of setMaps(z, b)) {
        if (!equalMorphisms(compose(f, u), compose(g, v))) {
          assert.throws(() => p.factor(u, v), /does not commute/); continue;
        }
        const h = p.factor(u, v); cones++;
        assert(equalMorphisms(compose(p.left, h), u));
        assert(equalMorphisms(compose(p.right, h), v));
        const candidates = setMaps(z, p.object).filter(m => equalMorphisms(compose(p.left, m), u) && equalMorphisms(compose(p.right, m), v));
        assert.equal(candidates.length, 1); assert(equalMorphisms(candidates[0], h));
      }
    }
  t.diagnostic(`${cospans} cospans, ${cones} compatible cones; test sources bounded by size two`);
});

test('equalizers and coequalizers have unique factors on bounded finite sets', () => {
  const sets = [0, 1, 2].map(finiteSet);
  for (const a of sets) for (const b of sets) for (const f of setMaps(a, b)) for (const g of setMaps(a, b)) {
    const e = equalizer(f, g), q = coequalizer(f, g);
    assert(equalMorphisms(compose(f, e.inclusion), compose(g, e.inclusion)));
    assert(equalMorphisms(compose(q.quotient, f), compose(q.quotient, g)));
    for (const z of sets) {
      for (const h of setMaps(z, a)) {
        if (!equalMorphisms(compose(f, h), compose(g, h))) { assert.throws(() => e.factor(h), /does not equalize/); continue; }
        const candidates = setMaps(z, e.object).filter(m => equalMorphisms(compose(e.inclusion, m), h));
        assert.equal(candidates.length, 1); assert(equalMorphisms(e.factor(h), candidates[0]));
      }
      for (const h of setMaps(b, z)) {
        if (!equalMorphisms(compose(h, f), compose(h, g))) { assert.throws(() => q.factor(h), /does not coequalize/); continue; }
        const candidates = setMaps(q.object, z).filter(m => equalMorphisms(compose(m, q.quotient), h));
        assert.equal(candidates.length, 1); assert(equalMorphisms(q.factor(h), candidates[0]));
      }
    }
  }
});

test('ambient closure permits loops and parallel incidence, separately from model policy', () => {
  const k = graph(['p'], []), a = graph(['s', 't'], [['e', 's', 't']]);
  const q = coequalizer(mapGraph(k, a, { p: 's' }), mapGraph(k, a, { p: 't' }));
  assert.equal(q.object.sets.vertex.length, 1); assert.equal(q.object.sets.edge.length, 1);
  const e = q.object.sets.edge[0]; assert.equal(q.object.maps.source[e], q.object.maps.target[e]);
  const t = terminal(graphSchema); assert.equal(t.sets.edge.length, 1, 'terminal graph must contain its loop');
  assert(equalMorphisms(terminalMap(a), compose(terminalMap(q.object), q.quotient)));
  const p = product(a, a); assert.equal(p.object.sets.vertex.length, 4); assert.equal(p.object.sets.edge.length, 1);
  assert(equalMorphisms(compose(p.left, p.factor(identity(a), identity(a))), identity(a)));
});

test('gluing uses supplied maps, not repeated names, and retains all occurrences', () => {
  const k = graph(['port'], []), a = graph(['a', 'seam'], [['same-edge-id', 'a', 'seam']]);
  const b = graph(['seam', 'b'], [['same-edge-id', 'seam', 'b']]);
  const p = pushout(mapGraph(k, a, { port: 'seam' }), mapGraph(k, b, { port: 'seam' }));
  assert.equal(p.object.sets.vertex.length, 3);
  assert.equal(p.object.sets.edge.length, 2);
  assert.notEqual(p.left.components.edge['same-edge-id'], p.right.components.edge['same-edge-id']);
  assert.equal(p.left.components.vertex.seam, p.right.components.vertex.seam);
  assert.equal(coproduct(a, b).object.sets.vertex.length, 4, 'equal names alone do not glue');
  assert(equalMorphisms(compose(p.factor(p.left, p.right), p.left), p.left));
});

test('noninjective spans are supported in the ambient category, without pretending they are inclusions', () => {
  const k = finiteSet(2), a = finiteSet(1), b = finiteSet(2);
  const f = setMaps(k, a)[0], g = identity(b), p = pushout(f, g);
  assert.equal(isMonomorphism(f), false);
  assert.equal(p.object.sets.item.length, 1);
  assert.equal(isMonomorphism(p.right), false);
  assert.throws(() => inverse(f), /not an isomorphism/);
});

const boundary = graph(['p'], []);
function segment(prefix) {
  const d = graph([`${prefix}0`, `${prefix}1`], [[`${prefix}e`, `${prefix}0`, `${prefix}1`]]);
  return openComponent(mapGraph(boundary, d, { p: `${prefix}0` }), mapGraph(boundary, d, { p: `${prefix}1` }));
}

// Composite cocone from a parenthesized sequence; factors are built solely from
// the kernel's universal-map witnesses. No comparison by counts or coordinates.
function assembly(tree, components) {
  if (Number.isInteger(tree)) {
    const component = components[tree];
    return { component, legs: [identity(component.object)], factor: maps => maps[0] };
  }
  const a = assembly(tree[0], components), b = assembly(tree[1], components);
  const { component, gluing } = composeOpen(b.component, a.component);
  return {
    component,
    legs: [...a.legs.map(f => compose(gluing.left, f)), ...b.legs.map(f => compose(gluing.right, f))],
    factor: maps => gluing.factor(a.factor(maps.slice(0, a.legs.length)), b.factor(maps.slice(a.legs.length))),
  };
}
function comparison(a, b) {
  const f = a.factor(b.legs), inv = inverse(f);
  assert(equalMorphisms(compose(f, a.component.left), b.component.left));
  assert(equalMorphisms(compose(f, a.component.right), b.component.right));
  assert(equalMorphisms(compose(inv, f), identity(a.component.object)));
  return f;
}

test('open-component units restore the original apex by explicit isomorphisms', () => {
  const c = segment('a');
  const right = composeOpen(identityComponent(c.output), c);
  const r = right.gluing.factor(identity(c.object), c.right);
  inverse(r);
  assert(equalMorphisms(compose(r, right.component.left), c.left));
  assert(equalMorphisms(compose(r, right.component.right), c.right));
  const left = composeOpen(c, identityComponent(c.input));
  const l = left.gluing.factor(c.left, identity(c.object));
  inverse(l);
  assert(equalMorphisms(compose(l, left.component.left), c.left));
  assert(equalMorphisms(compose(l, left.component.right), c.right));
});

test('associator and pentagon compare all retained incidences, not just apex sizes', () => {
  const components = ['a', 'b', 'c', 'd'].map(segment);
  const trees = [
    [[[0, 1], 2], 3], [[0, 1], [2, 3]], [0, [1, [2, 3]]],
    [0, [[1, 2], 3]], [[0, [1, 2]], 3],
  ].map(tree => assembly(tree, components));
  const short = compose(comparison(trees[1], trees[2]), comparison(trees[0], trees[1]));
  const long = compose(comparison(trees[3], trees[2]), compose(comparison(trees[4], trees[3]), comparison(trees[0], trees[4])));
  assert(equalMorphisms(short, long));
  assert.equal(trees[0].component.object.sets.edge.length, 4);
  assert.equal(trees[0].component.object.sets.vertex.length, 5);
  for (let i = 0; i < 4; i++) assert(equalMorphisms(compose(short, trees[0].legs[i]), trees[2].legs[i]));
});

test('renaming the gluing inputs yields a commuting isomorphic composite', () => {
  const k = graph(['p'], []), a = segment('a').object, b = segment('b').object;
  const f = mapGraph(k, a, { p: 'a1' }), g = mapGraph(k, b, { p: 'b0' }), p = pushout(f, g);
  const renamed = graph(['new0', 'new1'], [['newEdge', 'new0', 'new1']]);
  const rho = mapGraph(a, renamed, { a0: 'new0', a1: 'new1' }, { ae: 'newEdge' });
  const q = pushout(compose(rho, f), g);
  const transport = p.factor(compose(q.left, rho), q.right);
  inverse(transport);
  assert(equalMorphisms(compose(transport, p.left), compose(q.left, rho)));
  assert(equalMorphisms(compose(transport, p.right), q.right));
});

test('proposed isotope schema enforces route ownership and endpoint equations', () => {
  const sets = Object.fromEntries(isotopeIncidenceSchema.sorts.map(s => [s, []]));
  Object.assign(sets, { shell: ['s'], cell: ['c'], port: ['p', 'q'], vertex: ['v', 'w'], edge: ['e'], pair: ['pair'] });
  const maps = Object.fromEntries(isotopeIncidenceSchema.arrows.map(a => [a.name, {}]));
  Object.assign(maps, {
    cellShell: { c: 's' }, portCell: { p: 'c', q: 'c' }, portVertex: { p: 'v', q: 'w' },
    source: { e: 'v' }, target: { e: 'w' }, pairCell: { pair: 'c' },
    redEdge: { pair: 'e' }, blueEdge: { pair: 'e' }, redStart: { pair: 'p' }, redEnd: { pair: 'q' }, blueStart: { pair: 'p' }, blueEnd: { pair: 'q' },
  });
  const d = createDiagram(isotopeIncidenceSchema, { sets, maps });
  // Same red/blue support is structurally typed; a separate model may forbid it.
  const p = pushout(identity(d), identity(d));
  assert(equalMorphisms(compose(p.factor(identity(d), identity(d)), p.left), identity(d)));
  const broken = structuredClone(maps); broken.blueEnd.pair = 'p';
  assert.throws(() => createDiagram(isotopeIncidenceSchema, { sets, maps: broken }), /equation fails/);
  assert(equalMorphisms(initialMap(d), createMorphism(initial(isotopeIncidenceSchema), d, Object.fromEntries(isotopeIncidenceSchema.sorts.map(s => [s, {}])))));
});
