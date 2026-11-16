import { createHash } from 'node:crypto';
import { isMonomorphism, equalMorphisms } from './finite-diagrams.mjs';
import { attributedMorphism, attributedIdentity, composeAttributed, inverseAttributed, equalAttributedObjects, canonicalJSON, jsonClone, deepFreeze } from './attributed-diagrams.mjs';
import { importRevisionBundle, revisionEngineDigest, RewriteError } from './revisions.mjs';
import { importRule, planRewrite, applyRewrite, transportMatch } from './rules.mjs';
import { verifyIsomorphicJoin } from './isomorphic-joins.mjs';

const demand = (condition, code, detail = null) => { if (!condition) throw new RewriteError(code, detail); };
const hash = body => createHash('sha256').update('isotope-wiring.context-lift.v1\n' + canonicalJSON(body)).digest('hex');

// This helper checks step embeddings, not a whole history or a model claim.
export function extendContextEmbedding(embedding, basePlan, extensionPlan) {
  // Transport the retained inclusions: this also requires kernel-admitted plans.
  const retained = transportMatch(basePlan, basePlan.inclusion).match;
  const extendedRetained = transportMatch(extensionPlan, extensionPlan.inclusion).match;
  demand(basePlan.rule.id === extensionPlan.rule.id && canonicalJSON(basePlan.spec.rule) === canonicalJSON(extensionPlan.spec.rule), 'context-step-rule-mismatch');
  demand(isMonomorphism(embedding.map), 'context-embedding-must-be-monic');
  demand(equalMorphisms(composeAttributed(embedding, basePlan.match).map, extensionPlan.match.map), 'context-step-match-square-failed');
  const schema = basePlan.target.diagram.schema;
  const components = Object.fromEntries(schema.sorts.map(s => {
    const pairs = basePlan.complement.diagram.sets[s].map(x => [x, embedding.map.components[s][x]]);
    for (const [r, x] of Object.entries(basePlan.spec.allocation[s])) pairs.push([x, extensionPlan.spec.allocation[s][r]]);
    return [s, Object.fromEntries(pairs)];
  }));
  const next = attributedMorphism(basePlan.target, extensionPlan.target, components);
  demand(isMonomorphism(next.map), 'context-lift-result-not-monic');
  const complementMap = attributedMorphism(basePlan.complement, extensionPlan.complement,
    Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(basePlan.complement.diagram.sets[s].map(x => [x, embedding.map.components[s][x]]))])));
  demand(equalMorphisms(composeAttributed(next, retained).map,
    composeAttributed(extendedRetained, complementMap).map), 'context-lift-retained-square-failed');
  demand(equalMorphisms(composeAttributed(next, basePlan.comatch).map, extensionPlan.comatch.map), 'context-lift-comatch-square-failed');
  return next;
}

// A certificate for ONE supplied monic extension, not a universal context lemma.
export function liftPersistentJoin(baseStore, inputWitness, extensionStore, extensionRevision, embedding, options = {}) {
  const witness = jsonClone(inputWitness);
  verifyIsomorphicJoin(baseStore, witness);
  demand(witness.status === 'joinedUpToIsomorphism' && witness.trackingPolicy === 'persistentAfterPeak', 'context-lift-requires-persistent-join');
  const baseRevision = witness.routes.peak.inputRevision;
  const baseSource = baseStore.state(baseRevision).object, extensionSource = extensionStore.state(extensionRevision).object;
  composeAttributed(embedding, attributedIdentity(baseSource));
  demand(equalAttributedObjects(embedding.target, extensionSource), 'context-embedding-target-mismatch');
  demand(isMonomorphism(embedding.map), 'context-embedding-must-be-monic');
  demand(options && typeof options === 'object' && !Array.isArray(options)
    && Object.keys(options).every(k => k === 'allocations'), 'invalid-context-lift-options');
  const supplied = jsonClone(options.allocations === undefined ? {} : options.allocations);
  demand(supplied && typeof supplied === 'object' && !Array.isArray(supplied)
    && Object.keys(supplied).every(k => ['left', 'right'].includes(k)), 'invalid-context-lift-allocations');
  for (const side of ['left', 'right']) if (Object.hasOwn(supplied, side))
    demand(Array.isArray(supplied[side]) && supplied[side].length === witness.routes[side].applications.length
      && supplied[side].every(x => x === null || (x && typeof x === 'object' && !Array.isArray(x))), 'context-lift-allocation-length-or-type');
  const small = importRevisionBundle(baseStore.exportBundle()), large = importRevisionBundle(extensionStore.exportBundle());
  const schema = extensionSource.diagram.schema;
  const outside = Object.fromEntries(schema.sorts.map(s => {
    const image = new Set(Object.values(embedding.map.components[s]));
    return [s, extensionSource.diagram.sets[s].filter(x => !image.has(x))];
  }));
  function liftRoute(side) {
    let inclusion = embedding, current = extensionRevision;
    let tracked = Object.fromEntries(schema.sorts.map(s => [s, [...extensionSource.diagram.sets[s]]]));
    let afterPeak = null;
    const applications = [], embeddings = [], allocations = [];
    for (const [index, expected] of witness.routes[side].applications.entries()) {
      const spec = expected.spec, rule = importRule(spec.rule), source = small.state(spec.inputRevision).object;
      const match = attributedMorphism(rule.left.target, source, spec.match);
      const basePlan = planRewrite(small, spec.inputRevision, rule, match, spec.allocation);
      demand(canonicalJSON(basePlan.spec) === canonicalJSON(spec), 'context-lift-base-plan-mismatch');
      const liftedMatch = composeAttributed(inclusion, match);
      const allocation = supplied[side]?.[index] ?? spec.allocation;
      // A context can make an initial deletion dangling; allocation collisions
      // are also real refusals, never silently repaired or classified as joins.
      const plan = planRewrite(large, current, rule, liftedMatch, allocation);
      const baseResult = applyRewrite(small, spec.inputRevision, basePlan);
      demand(canonicalJSON(baseResult.witness) === canonicalJSON(expected), 'context-lift-base-application-mismatch');
      const result = applyRewrite(large, current, plan);
      const next = extendContextEmbedding(inclusion, basePlan, plan);
      tracked = Object.fromEntries(schema.sorts.map(s => [s, tracked[s].filter(x => !plan.deleted[s].includes(x))]));
      if (afterPeak === null) afterPeak = tracked;
      applications.push(result.witness); embeddings.push(next.map.components); allocations.push(plan.spec.allocation);
      inclusion = next; current = result.revision.id;
    }
    return { data: { outputRevision: current, applications, embeddings }, inclusion, tracked, afterPeak, allocations };
  }
  const left = liftRoute('left'), right = liftRoute('right');
  const baseIso = attributedMorphism(left.inclusion.source, right.inclusion.source, witness.comparison.forward);
  inverseAttributed(baseIso);
  const components = Object.fromEntries(schema.sorts.map(s => {
    const pairs = outside[s].map(x => [x, x]);
    for (const x of left.inclusion.source.diagram.sets[s]) {
      const image = left.inclusion.map.components[s][x];
      demand(!outside[s].includes(image), 'context-lift-images-overlap');
      pairs.push([image, right.inclusion.map.components[s][baseIso.map.components[s][x]]]);
    }
    return [s, Object.fromEntries(pairs)];
  }));
  const comparison = attributedMorphism(left.inclusion.target, right.inclusion.target, components), inverse = inverseAttributed(comparison);
  demand(equalMorphisms(composeAttributed(comparison, left.inclusion).map,
    composeAttributed(right.inclusion, baseIso).map), 'context-lift-comparison-square-failed');
  const persistent = Object.fromEntries(schema.sorts.map(s => [s, left.afterPeak[s].filter(x => right.afterPeak[s].includes(x))]));
  for (const s of schema.sorts) for (const x of persistent[s])
    demand(left.tracked[s].includes(x) && right.tracked[s].includes(x) && comparison.map.components[s][x] === x, 'context-lift-persistence-failed');
  for (const s of schema.sorts) for (const x of outside[s])
    demand(left.tracked[s].includes(x) && right.tracked[s].includes(x), 'context-lift-outside-record-lost');
  const l = large.state(left.data.outputRevision), r = large.state(right.data.outputRevision);
  demand(canonicalJSON(l.context) === canonicalJSON(r.context) && canonicalJSON(l.metadata) === canonicalJSON(r.metadata), 'context-lift-state-boundary-mismatch');
  const body = {
    format: 'isotope-wiring.context-lift.v1', engineDigest: revisionEngineDigest, status: 'liftedPersistentJoin',
    baseWitness: witness, extensionRevision, extensionStateId: extensionStore.state(extensionRevision).id,
    embedding: embedding.map.components, outside, persistentAfterPeak: persistent,
    allocations: { left: left.allocations, right: right.allocations }, left: left.data, right: right.data,
    comparison: { forward: comparison.map.components, inverse: inverse.map.components, leftStateId: l.id, rightStateId: r.id },
    scope: 'Checked lift into one supplied monic context; retained/comatch/comparison squares commute; added context fixed; no universal context-extension, model-preservation, or confluence theorem',
  };
  return Object.freeze({ certificate: deepFreeze({ ...body, id: hash(body) }),
    baseBundle: deepFreeze(small.exportBundle()), extensionBundle: deepFreeze(large.exportBundle()) });
}

export function verifyContextLift(baseStore, extensionStore, input) {
  const certificate = jsonClone(input);
  demand(certificate && typeof certificate === 'object' && !Array.isArray(certificate), 'invalid-context-lift');
  const { id, ...body } = certificate;
  demand(id === hash(body), 'context-lift-digest-mismatch');
  demand(certificate.engineDigest === revisionEngineDigest, 'context-lift-engine-mismatch');
  const source = baseStore.state(certificate.baseWitness.routes.peak.inputRevision).object;
  const target = extensionStore.state(certificate.extensionRevision).object;
  const embedding = attributedMorphism(source, target, certificate.embedding);
  const actual = liftPersistentJoin(baseStore, certificate.baseWitness, extensionStore, certificate.extensionRevision,
    embedding, { allocations: certificate.allocations }).certificate;
  demand(canonicalJSON(actual) === canonicalJSON(certificate), 'context-lift-replay-mismatch'); return true;
}
