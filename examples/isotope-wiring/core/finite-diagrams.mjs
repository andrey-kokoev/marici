// Finite diagrams over a fixed, equationally presented schema.
// No DOM, coordinates, particle interpretation, or validity-target constraints.
const schemas = new WeakSet(), diagrams = new WeakSet(), morphisms = new WeakSet();
const schemaKeys = new WeakMap(), diagramKeys = new WeakMap();
const fail = message => { throw new Error(message); };
const check = (condition, message) => { if (!condition) fail(message); };
const freeze = value => {
  if (value && typeof value === 'object') { Object.values(value).forEach(freeze); Object.freeze(value); }
  return value;
};
const stable = value => JSON.stringify(value, (_, v) => v && typeof v === 'object' && !Array.isArray(v)
  ? Object.fromEntries(Object.keys(v).sort().map(k => [k, v[k]])) : v);
const id = value => check(typeof value === 'string' && value.length > 0 && !['__proto__', 'prototype', 'constructor'].includes(value), 'Invalid identifier');
const keysExactly = (value, keys, label) => {
  check(value && typeof value === 'object' && !Array.isArray(value), `${label}: expected a record`);
  check(stable(Object.keys(value).sort()) === stable([...keys].sort()), `${label}: keys do not match domain`);
};
const requireDiagram = d => check(diagrams.has(d), 'Expected a checked diagram');
const requireMorphism = f => check(morphisms.has(f), 'Expected a checked morphism');
const sameSchema = (a, b) => schemaKeys.get(a) === schemaKeys.get(b);

export function defineSchema({ id: name, sorts, arrows = [], equations = [] }) {
  id(name); check(Array.isArray(sorts), 'Schema sorts must be an array');
  sorts.forEach(id); check(new Set(sorts).size === sorts.length, 'Duplicate sort');
  const names = new Set();
  const checkedArrows = arrows.map(a => {
    id(a.name); check(!names.has(a.name), 'Duplicate schema arrow'); names.add(a.name);
    check(sorts.includes(a.from) && sorts.includes(a.to), 'Unknown arrow sort');
    return { name: a.name, from: a.from, to: a.to };
  }).sort((a, b) => a.name < b.name ? -1 : a.name > b.name ? 1 : 0);
  const byName = new Map(checkedArrows.map(a => [a.name, a]));
  const end = (at, path) => {
    check(sorts.includes(at) && Array.isArray(path), 'Invalid equation path');
    for (const name of path) {
      const a = byName.get(name); check(a && a.from === at, 'Equation path is not composable'); at = a.to;
    }
    return at;
  };
  const checkedEquations = equations.map(e => {
    check(end(e.at, e.left) === end(e.at, e.right), 'Equation endpoints differ');
    return { at: e.at, left: [...e.left], right: [...e.right] };
  }).sort((a, b) => stable(a) < stable(b) ? -1 : stable(a) > stable(b) ? 1 : 0);
  const result = freeze({ id: name, sorts: [...sorts].sort(), arrows: checkedArrows, equations: checkedEquations });
  schemas.add(result); schemaKeys.set(result, stable(result)); return result;
}

export function createDiagram(schema, { sets, maps }) {
  check(schemas.has(schema), 'Expected a checked schema');
  keysExactly(sets, schema.sorts, 'Sets'); keysExactly(maps, schema.arrows.map(a => a.name), 'Maps');
  const checkedSets = Object.fromEntries(schema.sorts.map(sort => {
    check(Array.isArray(sets[sort]), `Not a finite set: ${sort}`); sets[sort].forEach(id);
    check(new Set(sets[sort]).size === sets[sort].length, `Duplicate record in ${sort}`);
    return [sort, [...sets[sort]].sort()];
  }));
  const checkedMaps = Object.fromEntries(schema.arrows.map(a => {
    keysExactly(maps[a.name], checkedSets[a.from], a.name);
    const entries = checkedSets[a.from].map(x => {
      check(checkedSets[a.to].includes(maps[a.name][x]), `Unbound incidence: ${a.name}(${x})`);
      return [x, maps[a.name][x]];
    });
    return [a.name, Object.fromEntries(entries)];
  }));
  const follow = (x, path) => path.reduce((y, a) => checkedMaps[a][y], x);
  for (const e of schema.equations) for (const x of checkedSets[e.at])
    check(follow(x, e.left) === follow(x, e.right), `Schema equation fails at ${e.at}:${x}`);
  const result = freeze({ schema, sets: checkedSets, maps: checkedMaps });
  diagrams.add(result); diagramKeys.set(result, stable(result)); return result;
}

export function equalDiagrams(a, b) {
  requireDiagram(a); requireDiagram(b); return diagramKeys.get(a) === diagramKeys.get(b);
}

export function createMorphism(source, target, components) {
  requireDiagram(source); requireDiagram(target);
  check(sameSchema(source.schema, target.schema), 'Schema mismatch');
  keysExactly(components, source.schema.sorts, 'Morphism components');
  const checked = Object.fromEntries(source.schema.sorts.map(sort => {
    keysExactly(components[sort], source.sets[sort], `Component ${sort}`);
    return [sort, Object.fromEntries(source.sets[sort].map(x => {
      check(target.sets[sort].includes(components[sort][x]), `Unbound morphism image: ${sort}:${x}`);
      return [x, components[sort][x]];
    }))];
  }));
  for (const a of source.schema.arrows) for (const x of source.sets[a.from])
    check(checked[a.to][source.maps[a.name][x]] === target.maps[a.name][checked[a.from][x]], `Naturality fails: ${a.name} at ${x}`);
  const result = freeze({ source, target, components: checked }); morphisms.add(result); return result;
}

export function identity(object) {
  requireDiagram(object);
  return createMorphism(object, object, Object.fromEntries(object.schema.sorts.map(s => [s, Object.fromEntries(object.sets[s].map(x => [x, x]))])));
}

// compose(g,f) means g after f. Endpoint equality includes the entire schema.
export function compose(g, f) {
  requireMorphism(f); requireMorphism(g); check(equalDiagrams(f.target, g.source), 'Composition boundary mismatch');
  const components = Object.fromEntries(f.source.schema.sorts.map(s => {
    const entries = f.source.sets[s].map(x => [x, g.components[s][f.components[s][x]]]);
    return [s, Object.fromEntries(entries)];
  }));
  return createMorphism(f.source, g.target, components);
}

export function equalMorphisms(f, g) {
  requireMorphism(f); requireMorphism(g);
  return equalDiagrams(f.source, g.source) && equalDiagrams(f.target, g.target) && stable(f.components) === stable(g.components);
}

export function isMonomorphism(f) {
  requireMorphism(f);
  return f.source.schema.sorts.every(s => new Set(Object.values(f.components[s])).size === f.source.sets[s].length);
}

export function inverse(f) {
  requireMorphism(f);
  check(isMonomorphism(f) && f.source.schema.sorts.every(s => f.source.sets[s].length === f.target.sets[s].length), 'Morphism is not an isomorphism');
  return createMorphism(f.target, f.source, Object.fromEntries(f.source.schema.sorts.map(s =>
    [s, Object.fromEntries(Object.entries(f.components[s]).map(([x, y]) => [y, x]))])));
}

export function initial(schema) {
  return createDiagram(schema, { sets: Object.fromEntries(schema.sorts.map(s => [s, []])), maps: Object.fromEntries(schema.arrows.map(a => [a.name, {}])) });
}

export function initialMap(target) {
  requireDiagram(target);
  return createMorphism(initial(target.schema), target, Object.fromEntries(target.schema.sorts.map(s => [s, {}])));
}

// Pointwise finite-set pushout. Occurrences on opposite sides are disjoint until
// identified by a supplied span. No coordinate or name-based gluing occurs.
export function pushout(f, g) {
  requireMorphism(f); requireMorphism(g); check(equalDiagrams(f.source, g.source), 'Pushout span boundary mismatch');
  const K = f.source, A = f.target, B = g.target, schema = K.schema;
  const sets = {}, classes = {}, leftComponents = {}, rightComponents = {};
  for (const sort of schema.sorts) {
    const occurrences = [...A.sets[sort].map(x => ['left', x]), ...B.sets[sort].map(x => ['right', x])];
    const lookup = new Map(occurrences.map((pair, i) => [stable(pair), i]));
    const parents = occurrences.map((_, i) => i);
    const find = i => { while (parents[i] !== i) { parents[i] = parents[parents[i]]; i = parents[i]; } return i; };
    for (const x of K.sets[sort]) {
      const a = find(lookup.get(stable(['left', f.components[sort][x]])));
      const b = find(lookup.get(stable(['right', g.components[sort][x]])));
      parents[b] = a;
    }
    const groups = new Map();
    occurrences.forEach((pair, i) => { const root = find(i); if (!groups.has(root)) groups.set(root, []); groups.get(root).push(pair); });
    classes[sort] = Object.fromEntries([...groups.values()].map((members, i) => [`pushout:${sort}:${i}`, members]));
    sets[sort] = Object.keys(classes[sort]);
    leftComponents[sort] = {}; rightComponents[sort] = {};
    for (const [q, members] of Object.entries(classes[sort])) for (const [side, x] of members)
      (side === 'left' ? leftComponents : rightComponents)[sort][x] = q;
  }
  const maps = Object.fromEntries(schema.arrows.map(a => [a.name, Object.fromEntries(sets[a.from].map(q => {
    const images = classes[a.from][q].map(([side, x]) => side === 'left'
      ? leftComponents[a.to][A.maps[a.name][x]] : rightComponents[a.to][B.maps[a.name][x]]);
    check(images.every(y => y === images[0]), 'Pushout incidence is not well-defined');
    return [q, images[0]];
  }))]));
  const object = createDiagram(schema, { sets, maps });
  const left = createMorphism(A, object, leftComponents), right = createMorphism(B, object, rightComponents);
  check(equalMorphisms(compose(left, f), compose(right, g)), 'Pushout square does not commute');
  function factor(u, v) {
    requireMorphism(u); requireMorphism(v);
    check(equalDiagrams(u.source, A) && equalDiagrams(v.source, B) && equalDiagrams(u.target, v.target), 'Cocone boundaries mismatch');
    check(equalMorphisms(compose(u, f), compose(v, g)), 'Cocone does not commute');
    return createMorphism(object, u.target, Object.fromEntries(schema.sorts.map(sort => [sort,
      Object.fromEntries(Object.entries(classes[sort]).map(([q, members]) => {
        const images = members.map(([side, x]) => (side === 'left' ? u : v).components[sort][x]);
        check(images.every(y => y === images[0]), 'Cocone factor is not well-defined'); return [q, images[0]];
      }))])));
  }
  return freeze({ object, left, right, classes, factor });
}

export function coproduct(a, b) {
  requireDiagram(a); requireDiagram(b); check(sameSchema(a.schema, b.schema), 'Schema mismatch');
  return pushout(initialMap(a), initialMap(b));
}

export function terminal(schema) {
  const singleton = s => `terminal:${s}`;
  return createDiagram(schema, {
    sets: Object.fromEntries(schema.sorts.map(s => [s, [singleton(s)]])),
    maps: Object.fromEntries(schema.arrows.map(a => [a.name, { [singleton(a.from)]: singleton(a.to) }])),
  });
}

export function terminalMap(source) {
  requireDiagram(source);
  const target = terminal(source.schema);
  return createMorphism(source, target, Object.fromEntries(source.schema.sorts.map(s =>
    [s, Object.fromEntries(source.sets[s].map(x => [x, target.sets[s][0]]))])));
}

// Dual universal construction: retain precisely the pairs with equal images.
export function pullback(f, g) {
  requireMorphism(f); requireMorphism(g); check(equalDiagrams(f.target, g.target), 'Pullback cospan boundary mismatch');
  const A = f.source, B = g.source, schema = A.schema, pairs = {}, indices = {};
  const sets = {}, leftComponents = {}, rightComponents = {};
  for (const s of schema.sorts) {
    const matches = A.sets[s].flatMap(a => B.sets[s].filter(b => f.components[s][a] === g.components[s][b]).map(b => [a, b]));
    pairs[s] = Object.fromEntries(matches.map((pair, i) => [`pullback:${s}:${i}`, pair]));
    indices[s] = new Map(Object.entries(pairs[s]).map(([q, pair]) => [stable(pair), q]));
    sets[s] = Object.keys(pairs[s]);
    leftComponents[s] = Object.fromEntries(Object.entries(pairs[s]).map(([q, pair]) => [q, pair[0]]));
    rightComponents[s] = Object.fromEntries(Object.entries(pairs[s]).map(([q, pair]) => [q, pair[1]]));
  }
  const maps = Object.fromEntries(schema.arrows.map(a => [a.name, Object.fromEntries(Object.entries(pairs[a.from]).map(([q, [x, y]]) =>
    [q, indices[a.to].get(stable([A.maps[a.name][x], B.maps[a.name][y]]))]))]));
  const object = createDiagram(schema, { sets, maps });
  const left = createMorphism(object, A, leftComponents), right = createMorphism(object, B, rightComponents);
  check(equalMorphisms(compose(f, left), compose(g, right)), 'Pullback square does not commute');
  function factor(u, v) {
    requireMorphism(u); requireMorphism(v);
    check(equalDiagrams(u.target, A) && equalDiagrams(v.target, B) && equalDiagrams(u.source, v.source), 'Cone boundaries mismatch');
    check(equalMorphisms(compose(f, u), compose(g, v)), 'Cone does not commute');
    return createMorphism(u.source, object, Object.fromEntries(schema.sorts.map(s => [s,
      Object.fromEntries(u.source.sets[s].map(x => [x, indices[s].get(stable([u.components[s][x], v.components[s][x]]))]))])));
  }
  return freeze({ object, left, right, pairs, factor });
}

export function product(a, b) {
  requireDiagram(a); requireDiagram(b); check(sameSchema(a.schema, b.schema), 'Schema mismatch');
  return pullback(terminalMap(a), terminalMap(b));
}

function parallel(f, g) {
  requireMorphism(f); requireMorphism(g);
  check(equalDiagrams(f.source, g.source) && equalDiagrams(f.target, g.target), 'Expected parallel morphisms');
}

export function equalizer(f, g) {
  parallel(f, g);
  const square = product(f.target, f.target);
  const p = pullback(square.factor(f, g), square.factor(identity(f.target), identity(f.target)));
  function factor(h) {
    requireMorphism(h); check(equalDiagrams(h.target, f.source), 'Equalizer factor boundary mismatch');
    check(equalMorphisms(compose(f, h), compose(g, h)), 'Map does not equalize');
    return p.factor(h, compose(f, h));
  }
  return freeze({ object: p.object, inclusion: p.left, factor });
}

export function coequalizer(f, g) {
  parallel(f, g);
  const sum = coproduct(f.source, f.source);
  const p = pushout(sum.factor(f, g), sum.factor(identity(f.source), identity(f.source)));
  function factor(h) {
    requireMorphism(h); check(equalDiagrams(h.source, f.target), 'Coequalizer factor boundary mismatch');
    check(equalMorphisms(compose(h, f), compose(h, g)), 'Map does not coequalize');
    return p.factor(h, compose(h, f));
  }
  return freeze({ object: p.object, quotient: p.left, factor });
}

export function openComponent(left, right) {
  requireMorphism(left); requireMorphism(right); check(equalDiagrams(left.target, right.target), 'Cospan apex mismatch');
  return freeze({ input: left.source, output: right.source, object: left.target, left, right });
}

export function identityComponent(object) { return openComponent(identity(object), identity(object)); }

export function composeOpen(g, f) {
  // Recheck legs rather than trusting a caller-constructed component envelope.
  const a = openComponent(f.left, f.right), b = openComponent(g.left, g.right);
  check(equalDiagrams(a.output, b.input), 'Interface mismatch: provide an explicit adapter');
  const gluing = pushout(a.right, b.left);
  return freeze({ component: openComponent(compose(gluing.left, a.left), compose(gluing.right, b.right)), gluing });
}
