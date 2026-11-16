import { createHash } from 'node:crypto';
import { attributedMorphism, attributedIdentity, inverseAttributed, equalAttributedObjects, canonicalJSON, jsonClone, deepFreeze } from './attributed-diagrams.mjs';
import { importRevisionBundle, revisionEngineDigest, RewriteError } from './revisions.mjs';
import { checkSuppliedJoin, verifyJoinWitness, importRule, planRewrite } from './rules.mjs';

const demand = (condition, code, detail = null) => { if (!condition) throw new RewriteError(code, detail); };
const hash = (domain, body) => createHash('sha256').update(domain + '\n' + canonicalJSON(body)).digest('hex');
const seal = (domain, body) => deepFreeze({ ...body, id: hash(domain, body) });
const checkSeal = (domain, value) => { const { id, ...body } = value; demand(id === hash(domain, body), 'isomorphism-digest-mismatch'); };

function limitsOf(options, allowed = ['maxSearchNodes', 'maxRecords', 'anchors']) {
  demand(options && typeof options === 'object' && !Array.isArray(options)
    && Object.keys(options).every(k => allowed.includes(k)), 'invalid-isomorphism-options');
  const limits = { maxSearchNodes: options.maxSearchNodes === undefined ? 10000 : options.maxSearchNodes,
    maxRecords: options.maxRecords === undefined ? 24 : options.maxRecords };
  demand(Number.isSafeInteger(limits.maxSearchNodes) && limits.maxSearchNodes >= 1 && limits.maxSearchNodes <= 1000000, 'invalid-isomorphism-node-bound');
  demand(Number.isSafeInteger(limits.maxRecords) && limits.maxRecords >= 1 && limits.maxRecords <= 128, 'invalid-isomorphism-record-bound');
  return limits;
}

export function normalizeIsomorphismLimits(options = {}) {
  return deepFreeze(limitsOf(options, ['maxSearchNodes', 'maxRecords']));
}

// Compare the incidence/label part while holding context and metadata literally
// fixed. No interpretation or rewriting of embedded identifier strings is made.
export function compareRevisionStates(store, leftRevision, rightRevision, options = {}) {
  const limits = limitsOf(options), left = store.state(leftRevision), right = store.state(rightRevision);
  const x = left.object, y = right.object, schema = x.diagram.schema;
  demand(canonicalJSON(schema) === canonicalJSON(y.diagram.schema), 'isomorphism-schema-mismatch');
  const supplied = jsonClone(options.anchors === undefined ? {} : options.anchors);
  demand(supplied && typeof supplied === 'object' && !Array.isArray(supplied)
    && Object.keys(supplied).every(s => schema.sorts.includes(s)), 'invalid-isomorphism-anchors');
  const anchors = Object.fromEntries(schema.sorts.map(s => [s, Object.hasOwn(supplied, s) ? supplied[s] : {}]));
  for (const s of schema.sorts) {
    demand(anchors[s] && typeof anchors[s] === 'object' && !Array.isArray(anchors[s]), 'invalid-isomorphism-anchors');
    demand(new Set(Object.values(anchors[s])).size === Object.keys(anchors[s]).length, 'isomorphism-anchors-not-injective');
    for (const [a, b] of Object.entries(anchors[s]))
      demand(x.diagram.sets[s].includes(a) && y.diagram.sets[s].includes(b), 'isomorphism-anchor-outside-object');
  }
  let searchNodes = 0;
  function finish(status, reason, forward = null) {
    const inverse = forward ? inverseAttributed(forward) : null;
    return seal('isotope-wiring.state-comparison.v1', {
      format: 'isotope-wiring.state-comparison.v1', engineDigest: revisionEngineDigest,
      leftRevision, rightRevision, leftStateId: left.id, rightStateId: right.id,
      limits, anchors, status, reason, searchNodes,
      forward: forward?.map.components ?? null, inverse: inverse?.map.components ?? null,
      scope: 'Exact labels and schema; context/metadata held literally fixed, not interpreted or retargeted; no equality of revision histories',
    });
  }
  if (canonicalJSON(left.context) !== canonicalJSON(right.context) || canonicalJSON(left.metadata) !== canonicalJSON(right.metadata))
    return finish('notCompared', 'context-or-metadata-mismatch');
  if (schema.sorts.some(s => x.diagram.sets[s].length !== y.diagram.sets[s].length)) return finish('notIsomorphic', 'sort-cardinality-mismatch');
  const identityAnchors = schema.sorts.every(s => Object.entries(anchors[s]).every(([a, b]) => a === b));
  if (identityAnchors && equalAttributedObjects(x, y)) return finish('isomorphic', 'checked-identity', attributedIdentity(x));
  const size = schema.sorts.reduce((n, s) => n + x.diagram.sets[s].length, 0);
  if (size > limits.maxRecords) return finish('unknown', 'maxRecords');
  const tasks = schema.sorts.flatMap(s => x.diagram.sets[s].map(a => ({ s, a,
    images: y.diagram.sets[s].filter(b => (!Object.hasOwn(anchors[s], a) || anchors[s][a] === b)
      && canonicalJSON(x.labels[s][a]) === canonicalJSON(y.labels[s][b])),
  })));
  const components = Object.fromEntries(schema.sorts.map(s => [s, Object.create(null)]));
  const used = Object.fromEntries(schema.sorts.map(s => [s, new Set()]));
  let found = null, exhausted = false;
  function visit(index) {
    if (found || exhausted) return;
    if (searchNodes >= limits.maxSearchNodes) { exhausted = true; return; }
    searchNodes++;
    for (const arrow of schema.arrows) for (const [a, b] of Object.entries(components[arrow.from])) {
      const target = x.diagram.maps[arrow.name][a];
      if (Object.hasOwn(components[arrow.to], target) && components[arrow.to][target] !== y.diagram.maps[arrow.name][b]) return;
    }
    if (index === tasks.length) {
      found = attributedMorphism(x, y, components); inverseAttributed(found); return;
    }
    const { s, a, images } = tasks[index];
    for (const b of images) {
      if (found || exhausted) break;
      if (used[s].has(b)) continue;
      components[s][a] = b; used[s].add(b); visit(index + 1); used[s].delete(b); delete components[s][a];
    }
  }
  visit(0);
  return found ? finish('isomorphic', 'checked-bijection', found)
    : exhausted ? finish('unknown', 'maxSearchNodes') : finish('notIsomorphic', 'exhausted-bijections');
}

export function verifyStateComparison(store, input) {
  const report = jsonClone(input);
  demand(report && typeof report === 'object' && !Array.isArray(report), 'invalid-state-comparison');
  checkSeal('isotope-wiring.state-comparison.v1', report);
  demand(report.engineDigest === revisionEngineDigest, 'isomorphism-engine-mismatch');
  const actual = compareRevisionStates(store, report.leftRevision, report.rightRevision, { ...report.limits, anchors: report.anchors });
  demand(canonicalJSON(actual) === canonicalJSON(report), 'state-comparison-replay-mismatch'); return true;
}

function trackedSource(source, applications) {
  let kept = Object.fromEntries(source.diagram.schema.sorts.map(s => [s, [...source.diagram.sets[s]]]));
  let afterPeak;
  for (const application of applications) {
    const { rule: data, match } = application.spec, rule = importRule(data);
    kept = Object.fromEntries(source.diagram.schema.sorts.map(s => {
      const preserved = new Set(Object.values(rule.left.map.components[s]));
      const deleted = new Set(rule.left.target.diagram.sets[s].filter(x => !preserved.has(x)).map(x => match[s][x]));
      return [s, kept[s].filter(x => !deleted.has(x))];
    }));
    if (!afterPeak) afterPeak = kept;
  }
  return { afterPeak, atEnd: kept };
}

export function normalizeJoinTrackingPolicy(value = 'commonSurvivors') {
  demand(['commonSurvivors', 'persistentAfterPeak'].includes(value), 'invalid-join-tracking-policy');
  return value;
}

export function checkSuppliedIsomorphicJoin(store, a, b, leftSteps = [], rightSteps = [], options = {}) {
  const limits = limitsOf(options, ['maxSearchNodes', 'maxRecords', 'maxStepsPerBranch', 'trackingPolicy']);
  const trackingPolicy = normalizeJoinTrackingPolicy(options.trackingPolicy);
  const maxStepsPerBranch = options.maxStepsPerBranch === undefined ? 16 : options.maxStepsPerBranch;
  const routes = checkSuppliedJoin(store, a, b, leftSteps, rightSteps, { maxStepsPerBranch });
  const scratch = importRevisionBundle(routes.bundle), source = scratch.state(a.spec.inputRevision).object;
  const left = trackedSource(source, routes.witness.left.applications), right = trackedSource(source, routes.witness.right.applications);
  const intersect = (p, q) => Object.fromEntries(source.diagram.schema.sorts.map(s => [s, p[s].filter(x => q[s].includes(x))]));
  const afterPeak = intersect(left.afterPeak, right.afterPeak), atEnd = intersect(left.atEnd, right.atEnd);
  const lostAfterPeak = Object.fromEntries(source.diagram.schema.sorts.map(s => [s, afterPeak[s].filter(x => !atEnd[s].includes(x))]));
  const lostOnLeft = Object.fromEntries(source.diagram.schema.sorts.map(s => [s, afterPeak[s].filter(x => !left.atEnd[s].includes(x))]));
  const lostOnRight = Object.fromEntries(source.diagram.schema.sorts.map(s => [s, afterPeak[s].filter(x => !right.atEnd[s].includes(x))]));
  const rejectedTracking = trackingPolicy === 'persistentAfterPeak' && Object.values(lostAfterPeak).some(xs => xs.length > 0);
  const anchors = Object.fromEntries(source.diagram.schema.sorts.map(s => [s, Object.fromEntries(atEnd[s].map(x => [x, x]))]));
  // Known track loss refutes this route under the stronger policy without
  // spending a permutation-search budget or inventing a comparison result.
  const comparison = rejectedTracking ? null : compareRevisionStates(scratch, routes.witness.left.outputRevision, routes.witness.right.outputRevision, { ...limits, anchors });
  const witness = seal('isotope-wiring.isomorphic-join.v1', {
    format: 'isotope-wiring.isomorphic-join.v1', engineDigest: revisionEngineDigest,
    trackingPolicy, comparisonLimits: limits,
    status: rejectedTracking ? 'trackingLost' : comparison.status === 'isomorphic' ? 'joinedUpToIsomorphism' : comparison.status === 'unknown' ? 'unknown' : 'notJoined',
    routes: routes.witness, comparison, tracking: { afterPeak, atEnd, lostAfterPeak, lostOnLeft, lostOnRight },
    scope: 'Only supplied routes under the declared source-tracking policy; persistentAfterPeak requires both continuations to retain and the comparison to fix every common post-peak source occurrence; no context-extension or confluence theorem or equality of histories',
  });
  return Object.freeze({ witness, bundle: routes.bundle });
}

export function verifyIsomorphicJoin(store, input) {
  const witness = jsonClone(input);
  demand(witness && typeof witness === 'object' && !Array.isArray(witness), 'invalid-isomorphic-join');
  checkSeal('isotope-wiring.isomorphic-join.v1', witness);
  demand(witness.engineDigest === revisionEngineDigest, 'isomorphism-engine-mismatch');
  verifyJoinWitness(store, witness.routes);
  const scratch = importRevisionBundle(store.exportBundle());
  const plans = witness.routes.peak.inputs.map(spec => {
    const rule = importRule(spec.rule), match = attributedMorphism(rule.left.target, scratch.state(spec.inputRevision).object, spec.match);
    const plan = planRewrite(scratch, spec.inputRevision, rule, match, spec.allocation);
    demand(canonicalJSON(plan.spec) === canonicalJSON(spec), 'isomorphic-join-plan-mismatch'); return plan;
  });
  const steps = list => list.map(s => ({ rule: importRule(s.rule), match: s.match, allocation: s.allocation }));
  const actual = checkSuppliedIsomorphicJoin(scratch, ...plans,
    steps(witness.routes.continuations.left), steps(witness.routes.continuations.right),
    { ...witness.comparisonLimits, trackingPolicy: witness.trackingPolicy, maxStepsPerBranch: witness.routes.maxStepsPerBranch }).witness;
  demand(canonicalJSON(actual) === canonicalJSON(witness), 'isomorphic-join-replay-mismatch'); return true;
}
