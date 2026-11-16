import { createMorphism, isMonomorphism, pushout, equalDiagrams, identity, compose, inverse } from './finite-diagrams.mjs';

const objects = new WeakSet(), maps = new WeakSet();
export function jsonClone(value) {
  const visit = x => {
    if (x === null || typeof x === 'string' || typeof x === 'boolean') return x;
    if (typeof x === 'number' && Number.isFinite(x)) return x;
    if (Array.isArray(x)) return x.map(visit);
    if (x && typeof x === 'object' && [Object.prototype, null].includes(Object.getPrototypeOf(x)))
      return Object.fromEntries(Object.entries(x).map(([k, v]) => [k, visit(v)]));
    throw Error('Expected finite JSON data');
  };
  return visit(value);
}
export function deepFreeze(x) {
  if (x && typeof x === 'object') { Object.values(x).forEach(deepFreeze); Object.freeze(x); }
  return x;
}
export const canonicalJSON = x => JSON.stringify(x, (_, v) => v && typeof v === 'object' && !Array.isArray(v)
  ? Object.fromEntries(Object.keys(v).sort().map(k => [k, v[k]])) : v);
const requireObject = x => { if (!objects.has(x)) throw Error('Expected checked attributed diagram'); };
const requireMap = f => { if (!maps.has(f)) throw Error('Expected checked attributed morphism'); };

// Model labels participate in map compatibility. Provenance is NOT a model label.
export function attributeDiagram(diagram, labels) {
  equalDiagrams(diagram, diagram); // Require a kernel-checked object.
  const copy = jsonClone(labels);
  if (canonicalJSON(Object.keys(copy).sort()) !== canonicalJSON([...diagram.schema.sorts].sort())) throw Error('Attribute sorts mismatch');
  for (const s of diagram.schema.sorts) {
    if (!copy[s] || Array.isArray(copy[s]) || typeof copy[s] !== 'object'
      || canonicalJSON(Object.keys(copy[s]).sort()) !== canonicalJSON([...diagram.sets[s]].sort())) throw Error(`Attribute domain mismatch: ${s}`);
  }
  const result = deepFreeze({ diagram, labels: copy }); objects.add(result); return result;
}

export function attributedMorphism(source, target, components) {
  requireObject(source); requireObject(target);
  const map = createMorphism(source.diagram, target.diagram, components);
  for (const s of source.diagram.schema.sorts) for (const x of source.diagram.sets[s])
    if (canonicalJSON(source.labels[s][x]) !== canonicalJSON(target.labels[s][map.components[s][x]]))
      throw Error(`Model attribute mismatch: ${s}:${x}`);
  const result = Object.freeze({ source, target, map }); maps.add(result); return result;
}

export function equalAttributedObjects(a, b) {
  requireObject(a); requireObject(b);
  return equalDiagrams(a.diagram, b.diagram) && canonicalJSON(a.labels) === canonicalJSON(b.labels);
}
export function attributedIdentity(object) {
  requireObject(object); return attributedMorphism(object, object, identity(object.diagram).components);
}
export function composeAttributed(g, f) {
  requireMap(f); requireMap(g);
  if (!equalAttributedObjects(f.target, g.source)) throw Error('Attributed composition boundary mismatch');
  return attributedMorphism(f.source, g.target, compose(g.map, f.map).components);
}

export function attributedPushout(f, g) {
  requireMap(f); requireMap(g);
  if (!equalDiagrams(f.source.diagram, g.source.diagram)
    || canonicalJSON(f.source.labels) !== canonicalJSON(g.source.labels)) throw Error('Attributed span source mismatch');
  const raw = pushout(f.map, g.map), labels = {};
  for (const s of raw.object.schema.sorts) {
    labels[s] = {};
    for (const [q, members] of Object.entries(raw.classes[s])) {
      const values = members.map(([side, x]) => (side === 'left' ? f.target : g.target).labels[s][x]);
      if (values.some(v => canonicalJSON(v) !== canonicalJSON(values[0]))) throw Error('Incompatible quotient attributes');
      labels[s][q] = values[0];
    }
  }
  const object = attributeDiagram(raw.object, labels);
  const left = attributedMorphism(f.target, object, raw.left.components);
  const right = attributedMorphism(g.target, object, raw.right.components);
  function factor(u, v) {
    requireMap(u); requireMap(v);
    if (!equalAttributedObjects(u.source, f.target) || !equalAttributedObjects(v.source, g.target) || !equalAttributedObjects(u.target, v.target)) throw Error('Attributed cocone boundaries mismatch');
    const h = raw.factor(u.map, v.map);
    return attributedMorphism(object, u.target, h.components);
  }
  return Object.freeze({ object, left, right, raw, factor });
}

// First assembly policy: share support/ownership context, never owned EP or
// neutron occurrences. This is not a capacity or physical-validity predicate.
export const supportInterfacePolicy = Object.freeze({
  id: 'isotope-wiring.support-interface.v1',
  excludedSorts: Object.freeze(['pair', 'lineWitness', 'boundaryWitness']),
});
export function checkSupportLeg(leg) {
  requireMap(leg);
  if (!isMonomorphism(leg.map)) throw Error('Support interface must be injective');
  for (const s of supportInterfacePolicy.excludedSorts)
    if (leg.source.diagram.sets[s]?.length) throw Error(`Owned occurrences cannot be interface records: ${s}`);
  const target = leg.target.diagram;
  if (target.maps.edgeSupport) {
    const sharedSupports = new Set(Object.values(leg.map.components.support));
    const includedEdges = new Set(Object.values(leg.map.components.edge));
    for (const e of target.sets.edge)
      if (sharedSupports.has(target.maps.edgeSupport[e]) && !includedEdges.has(e))
        throw Error('Shared support interface must include every incident directed edge');
  }
  return leg;
}
export function glueSupport(f, g) {
  checkSupportLeg(f); checkSupportLeg(g);
  return Object.freeze({ ...attributedPushout(f, g), policy: supportInterfacePolicy.id });
}

export function inverseAttributed(f) {
  requireMap(f);
  return attributedMorphism(f.target, f.source, inverse(f.map).components);
}

export function supportComponent(left, right) {
  checkSupportLeg(left); checkSupportLeg(right);
  if (!equalAttributedObjects(left.target, right.target)) throw Error('Support cospan apex mismatch');
  return Object.freeze({ input: left.source, output: right.source, object: left.target, left, right, policy: supportInterfacePolicy.id });
}
export function supportIdentity(boundary) {
  return supportComponent(attributedIdentity(boundary), attributedIdentity(boundary));
}
export function composeSupport(g, f) {
  const a = supportComponent(f.left, f.right), b = supportComponent(g.left, g.right);
  if (!equalAttributedObjects(a.output, b.input)) throw Error('Support component interface mismatch');
  const gluing = glueSupport(a.right, b.left);
  // Recheck the external legs: a successful internal pushout alone is not a
  // certificate that the selected boundary policy survived composition.
  const component = supportComponent(composeAttributed(gluing.left, a.left), composeAttributed(gluing.right, b.right));
  return Object.freeze({ component, gluing });
}
