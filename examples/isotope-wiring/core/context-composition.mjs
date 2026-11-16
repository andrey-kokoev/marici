import { createHash } from 'node:crypto';
import { equalMorphisms, isMonomorphism } from './finite-diagrams.mjs';
import { attributedMorphism, composeAttributed, canonicalJSON, jsonClone, deepFreeze } from './attributed-diagrams.mjs';
import { importRevisionBundle, revisionEngineDigest, RewriteError } from './revisions.mjs';
import { importRule, planRewrite, applyRewrite } from './rules.mjs';
import { liftPersistentJoin, extendContextEmbedding } from './context-lifting.mjs';

const demand = (condition, code, detail = null) => { if (!condition) throw new RewriteError(code, detail); };
const hash = body => createHash('sha256').update('isotope-wiring.context-composition.v1\n' + canonicalJSON(body)).digest('hex');

function replayPlan(store, expected) {
  const spec = expected.spec, rule = importRule(spec.rule);
  const match = attributedMorphism(rule.left.target, store.state(spec.inputRevision).object, spec.match);
  const plan = planRewrite(store, spec.inputRevision, rule, match, spec.allocation);
  demand(canonicalJSON(plan.spec) === canonicalJSON(spec), 'context-composition-plan-mismatch');
  demand(canonicalJSON(applyRewrite(store, spec.inputRevision, plan).witness) === canonicalJSON(expected), 'context-composition-application-mismatch');
  return plan;
}

// Compare a direct G -> K lift with stagewise transport through G -> H -> K.
// Both routes and all intermediate embeddings are retained, not quotiented.
export function checkContextLiftComposition(baseStore, witness, middleStore, middleRevision, firstEmbedding,
  outerStore, outerRevision, secondEmbedding, options = {}) {
  demand(options && typeof options === 'object' && !Array.isArray(options)
    && Object.keys(options).every(k => ['middleAllocations', 'outerAllocations'].includes(k)), 'invalid-context-composition-options');
  const composite = composeAttributed(secondEmbedding, firstEmbedding);
  demand(isMonomorphism(secondEmbedding.map), 'context-composition-second-must-be-monic');
  const first = liftPersistentJoin(baseStore, witness, middleStore, middleRevision, firstEmbedding,
    { allocations: options.middleAllocations === undefined ? {} : options.middleAllocations });
  const requested = jsonClone(options.outerAllocations === undefined ? {} : options.outerAllocations);
  demand(requested && typeof requested === 'object' && !Array.isArray(requested)
    && Object.keys(requested).every(k => ['left', 'right'].includes(k)), 'context-composition-allocation-shape');
  const allocations = Object.fromEntries(['left', 'right'].map(side => {
    if (Object.hasOwn(requested, side)) demand(Array.isArray(requested[side])
      && requested[side].length === first.certificate.allocations[side].length, 'context-composition-allocation-shape');
    return [side, first.certificate.allocations[side].map((allocation, i) => requested[side]?.[i] ?? allocation)];
  }));
  // Default outer names follow the middle lift, as a staged lift would. They
  // are not silently reset to the original base names or repaired on collision.
  const direct = liftPersistentJoin(baseStore, witness, outerStore, outerRevision, composite, { allocations });
  const base = importRevisionBundle(first.baseBundle), middle = importRevisionBundle(first.extensionBundle), outer = importRevisionBundle(direct.extensionBundle);
  const stages = {}, endpoints = {};
  for (const side of ['left', 'right']) {
    let current = secondEmbedding;
    const embeddings = [];
    const middleApps = first.certificate[side].applications, outerApps = direct.certificate[side].applications;
    demand(middleApps.length === outerApps.length, 'context-composition-route-length-mismatch');
    for (let i = 0; i < middleApps.length; i++) {
      const middlePlan = replayPlan(middle, middleApps[i]), outerPlan = replayPlan(outer, outerApps[i]);
      current = extendContextEmbedding(current, middlePlan, outerPlan);
      const baseTarget = base.state(first.certificate.baseWitness.routes[side].applications[i].outputRevision).object;
      const throughMiddle = attributedMorphism(baseTarget, middlePlan.target, first.certificate[side].embeddings[i]);
      const directEmbedding = attributedMorphism(baseTarget, outerPlan.target, direct.certificate[side].embeddings[i]);
      demand(equalMorphisms(composeAttributed(current, throughMiddle).map, directEmbedding.map), 'context-composition-triangle-failed');
      embeddings.push(current.map.components);
    }
    stages[side] = { embeddings, middleOutputRevision: first.certificate[side].outputRevision,
      outerOutputRevision: direct.certificate[side].outputRevision };
    endpoints[side] = current;
  }
  const middleIso = attributedMorphism(endpoints.left.source, endpoints.right.source, first.certificate.comparison.forward);
  const outerIso = attributedMorphism(endpoints.left.target, endpoints.right.target, direct.certificate.comparison.forward);
  const viaOuter = composeAttributed(outerIso, endpoints.left), viaMiddle = composeAttributed(endpoints.right, middleIso);
  demand(equalMorphisms(viaOuter.map, viaMiddle.map), 'context-composition-comparison-square-failed');
  const schema = secondEmbedding.target.diagram.schema;
  const stagedOutside = Object.fromEntries(schema.sorts.map(s => {
    const image = new Set(Object.values(secondEmbedding.map.components[s]));
    return [s, secondEmbedding.target.diagram.sets[s].filter(x => !image.has(x))];
  }));
  const persistentImages = Object.fromEntries(schema.sorts.map(s => [s,
    Object.fromEntries(first.certificate.persistentAfterPeak[s].map(x => [x, secondEmbedding.map.components[s][x]]))]));
  for (const s of schema.sorts) {
    for (const [x, image] of Object.entries(persistentImages[s]))
      demand(direct.certificate.persistentAfterPeak[s].includes(image)
        && endpoints.left.map.components[s][x] === image && endpoints.right.map.components[s][x] === image
        && outerIso.map.components[s][image] === image, 'context-composition-persistence-failed');
    for (const x of stagedOutside[s])
      demand(outerIso.map.components[s][x] === x, 'context-composition-outside-not-fixed');
    for (const side of ['left', 'right']) {
      const covered = new Set([...stagedOutside[s], ...Object.values(endpoints[side].map.components[s])]);
      demand(covered.size === endpoints[side].target.diagram.sets[s].length
        && endpoints[side].target.diagram.sets[s].every(x => covered.has(x)), 'context-composition-coverage-failed');
    }
  }
  const body = {
    format: 'isotope-wiring.context-composition.v1', engineDigest: revisionEngineDigest,
    status: 'coherentContextLiftComposition', first: first.certificate, direct: direct.certificate,
    secondEmbedding: secondEmbedding.map.components, stages, stagedOutside, persistentImages,
    comparisonSquare: { viaOuter: viaOuter.map.components, viaMiddle: viaMiddle.map.components },
    scope: 'One concrete composable pair of monic contexts with fixed allocation programs; every step triangle and endpoint comparison square checked; histories retained; no universal coherence or confluence theorem',
  };
  return Object.freeze({ certificate: deepFreeze({ ...body, id: hash(body) }), baseBundle: first.baseBundle,
    middleBundle: first.extensionBundle, outerBundle: direct.extensionBundle });
}

export function verifyContextLiftComposition(baseStore, middleStore, outerStore, input) {
  const certificate = jsonClone(input);
  demand(certificate && typeof certificate === 'object' && !Array.isArray(certificate), 'invalid-context-composition');
  const { id, ...body } = certificate;
  demand(id === hash(body), 'context-composition-digest-mismatch');
  demand(certificate.engineDigest === revisionEngineDigest, 'context-composition-engine-mismatch');
  const first = certificate.first, direct = certificate.direct;
  const source = baseStore.state(first.baseWitness.routes.peak.inputRevision).object;
  const mid = middleStore.state(first.extensionRevision).object, target = outerStore.state(direct.extensionRevision).object;
  const i = attributedMorphism(source, mid, first.embedding), j = attributedMorphism(mid, target, certificate.secondEmbedding);
  const actual = checkContextLiftComposition(baseStore, first.baseWitness, middleStore, first.extensionRevision, i,
    outerStore, direct.extensionRevision, j, { middleAllocations: first.allocations, outerAllocations: direct.allocations }).certificate;
  demand(canonicalJSON(actual) === canonicalJSON(certificate), 'context-composition-replay-mismatch'); return true;
}
