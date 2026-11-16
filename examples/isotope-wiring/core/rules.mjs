import { createHash } from 'node:crypto';
import { defineSchema, createDiagram, isMonomorphism, equalMorphisms } from './finite-diagrams.mjs';
import {
  attributeDiagram, attributedMorphism, attributedIdentity, attributedPushout,
  composeAttributed, inverseAttributed, equalAttributedObjects, canonicalJSON, jsonClone, deepFreeze,
} from './attributed-diagrams.mjs';
import { importRevisionBundle, revisionEngineDigest, RewriteError } from './revisions.mjs';

const rules = new WeakSet(), plans = new WeakMap();
const hash = (domain, x) => createHash('sha256').update(domain + '\n' + canonicalJSON(x)).digest('hex');
const seal = (domain, body) => deepFreeze({ ...body, id: hash(domain, body) });
const requireThat = (condition, code, detail = null) => { if (!condition) throw new RewriteError(code, detail); };
const checkSeal = (domain, x) => { const { id, ...body } = x; requireThat(id === hash(domain, body), 'rule-witness-digest-mismatch'); };
const encodeObject = object => ({ diagram: object.diagram, labels: object.labels });
const decodeObject = data => attributeDiagram(createDiagram(defineSchema(data.diagram.schema), data.diagram), data.labels);
const sameKeys = (a, b) => canonicalJSON(Object.keys(a).sort()) === canonicalJSON([...b].sort());

// Explicit closed subdiagram; omission never implicitly deletes incoming data.
export function subdiagram(object, selection) {
  equalAttributedObjects(object, object);
  const d = object.diagram;
  requireThat(Object.keys(selection).every(s => d.schema.sorts.includes(s)), 'unknown-selection-sort');
  const sets = Object.fromEntries(d.schema.sorts.map(s => [s, [...(selection[s] ?? [])]]));
  for (const s of d.schema.sorts) for (const x of sets[s]) requireThat(d.sets[s].includes(x), 'selection-outside-object', { sort: s, id: x });
  const maps = Object.fromEntries(d.schema.arrows.map(a => [a.name, Object.fromEntries(sets[a.from].map(x => [x, d.maps[a.name][x]]))]));
  const labels = Object.fromEntries(d.schema.sorts.map(s => [s, Object.fromEntries(sets[s].map(x => [x, object.labels[s][x]]))]));
  const result = attributeDiagram(createDiagram(d.schema, { sets, maps }), labels);
  const inclusion = attributedMorphism(result, object, Object.fromEntries(d.schema.sorts.map(s => [s, Object.fromEntries(sets[s].map(x => [x, x]))])));
  return Object.freeze({ object: result, inclusion });
}

// Close explicitly selected generators under every outgoing schema incidence.
export function generatedSubdiagram(object, selection) {
  const d = object.diagram;
  requireThat(Object.keys(selection).every(s => d.schema.sorts.includes(s)), 'unknown-selection-sort');
  const selected = Object.fromEntries(d.schema.sorts.map(s => [s, new Set(selection[s] ?? [])]));
  for (const s of d.schema.sorts) for (const x of selected[s]) requireThat(d.sets[s].includes(x), 'selection-outside-object');
  let changed = true;
  while (changed) {
    changed = false;
    for (const a of d.schema.arrows) for (const x of selected[a.from]) {
      const y = d.maps[a.name][x];
      if (!selected[a.to].has(y)) { selected[a.to].add(y); changed = true; }
    }
  }
  return subdiagram(object, Object.fromEntries(d.schema.sorts.map(s => [s, [...selected[s]]])));
}

// A linear attributed rule L <- K -> R. There are no implicit model guards,
// negative application conditions or attribute variables. Bounded automatic
// matching is a separate layer in matching.mjs.
export function defineRule(name, left, right) {
  requireThat(typeof name === 'string' && name.length > 0, 'rule-name-required');
  composeAttributed(left, attributedIdentity(left.source)); composeAttributed(right, attributedIdentity(right.source));
  requireThat(equalAttributedObjects(left.source, right.source), 'rule-interface-mismatch');
  requireThat(isMonomorphism(left.map) && isMonomorphism(right.map), 'rule-legs-must-be-monic');
  const data = seal('isotope-wiring.rule.v1', {
    format: 'isotope-wiring.rule.v1', name,
    interface: encodeObject(left.source), left: encodeObject(left.target), right: encodeObject(right.target),
    leftMap: left.map.components, rightMap: right.map.components,
  });
  const rule = Object.freeze({ id: data.id, name, left, right, data }); rules.add(rule); return rule;
}
export function exportRule(rule) { requireThat(rules.has(rule), 'unchecked-rule'); return jsonClone(rule.data); }
export function importRule(input) {
  const data = jsonClone(input); checkSeal('isotope-wiring.rule.v1', data);
  const k = decodeObject(data.interface), l = decodeObject(data.left), r = decodeObject(data.right);
  const rule = defineRule(data.name, attributedMorphism(k, l, data.leftMap), attributedMorphism(k, r, data.rightMap));
  requireThat(canonicalJSON(rule.data) === canonicalJSON(data), 'noncanonical-rule'); return rule;
}

export function planRewrite(store, inputRevision, rule, match, allocation = {}) {
  requireThat(rules.has(rule), 'unchecked-rule');
  composeAttributed(match, attributedIdentity(match.source));
  const state = store.state(inputRevision), x = state.object, schema = x.diagram.schema;
  requireThat(equalAttributedObjects(match.source, rule.left.target) && equalAttributedObjects(match.target, x), 'rule-match-boundary-mismatch');
  requireThat(isMonomorphism(match.map), 'rule-match-must-be-monic');
  const deleted = {}, remaining = {};
  for (const s of schema.sorts) {
    const kept = new Set(Object.values(rule.left.map.components[s]));
    deleted[s] = rule.left.target.diagram.sets[s].filter(id => !kept.has(id)).map(id => match.map.components[s][id]);
    remaining[s] = x.diagram.sets[s].filter(id => !deleted[s].includes(id));
  }
  const dangling = [];
  for (const a of schema.arrows) for (const id of remaining[a.from])
    if (!remaining[a.to].includes(x.diagram.maps[a.name][id])) dangling.push({ arrow: a.name, sort: a.from, id, deletedTarget: x.diagram.maps[a.name][id] });
  requireThat(dangling.length === 0, 'rule-dangling-condition', dangling);
  const complement = subdiagram(x, remaining);
  const kToD = attributedMorphism(rule.left.source, complement.object, Object.fromEntries(schema.sorts.map(s => [s,
    Object.fromEntries(rule.left.source.diagram.sets[s].map(k => [k, match.map.components[s][rule.left.map.components[s][k]]]))])));
  // Verify the first pushout by its canonical comparison to X, not by counts.
  const first = attributedPushout(rule.left, kToD);
  const firstComparison = first.factor(match, complement.inclusion);
  inverseAttributed(firstComparison);
  const second = attributedPushout(kToD, rule.right);

  const supplied = jsonClone(allocation);
  requireThat(supplied && typeof supplied === 'object' && !Array.isArray(supplied)
    && Object.keys(supplied).every(s => schema.sorts.includes(s)), 'allocation-sorts-mismatch');
  const allocated = {}, names = {}, created = {};
  for (const s of schema.sorts) {
    const preserved = new Set(Object.values(rule.right.map.components[s]));
    const added = rule.right.target.diagram.sets[s].filter(r => !preserved.has(r));
    allocated[s] = supplied[s] ?? {};
    requireThat(allocated[s] && typeof allocated[s] === 'object' && !Array.isArray(allocated[s]) && sameKeys(allocated[s], added), 'allocation-domain-mismatch', { sort: s, expected: added });
    created[s] = Object.values(allocated[s]);
    requireThat(new Set(created[s]).size === created[s].length, 'allocation-collision', { sort: s });
    for (const id of created[s]) {
      requireThat(typeof id === 'string' && id.length > 0 && !['__proto__', 'prototype', 'constructor'].includes(id), 'invalid-allocated-id');
      requireThat(!x.diagram.sets[s].includes(id), 'allocation-not-fresh', { sort: s, id });
    }
    names[s] = Object.fromEntries(complement.object.diagram.sets[s].map(id => [second.left.map.components[s][id], id]));
    for (const r of added) names[s][second.right.map.components[s][r]] = allocated[s][r];
    requireThat(sameKeys(names[s], second.object.diagram.sets[s]), 'rewrite-result-not-covered');
  }
  const raw = second.object.diagram;
  const target = attributeDiagram(createDiagram(schema, {
    sets: Object.fromEntries(schema.sorts.map(s => [s, raw.sets[s].map(id => names[s][id])])),
    maps: Object.fromEntries(schema.arrows.map(a => [a.name, Object.fromEntries(raw.sets[a.from].map(id => [names[a.from][id], names[a.to][raw.maps[a.name][id]]]))])),
  }), Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(raw.sets[s].map(id => [names[s][id], second.object.labels[s][id]]))])));
  const renaming = attributedMorphism(second.object, target, names); inverseAttributed(renaming);
  const retained = composeAttributed(renaming, second.left), comatch = composeAttributed(renaming, second.right);
  const request = {
    provenance: { kind: 'declared-typed-rule', rule: exportRule(rule), match: match.map.components, allocation: allocated },
    remove: schema.sorts.flatMap(s => deleted[s].map(id => ({ sort: s, id }))),
    add: schema.sorts.flatMap(s => created[s].map(id => ({ sort: s, id, label: target.labels[s][id],
      incidence: Object.fromEntries(schema.arrows.filter(a => a.from === s).map(a => [a.name, target.diagram.maps[a.name][id]])) }))),
  };
  const operation = store.preparePatch(inputRevision, request);
  // Isolated replay preflight proves the compiled ground edit reaches the
  // attributed DPO result before a caller's store or head is changed.
  const scratch = importRevisionBundle(store.exportBundle()), preview = scratch.applyPatch(inputRevision, operation);
  requireThat(equalAttributedObjects(scratch.state(preview.revision.id).object, target), 'ground-compiler-result-mismatch');
  const spec = seal('isotope-wiring.rule-plan.v1', {
    format: 'isotope-wiring.rule-plan.v1', engineDigest: revisionEngineDigest, inputRevision,
    rule: exportRule(rule), match: match.map.components, allocation: allocated,
    operationId: operation.id, targetDigest: hash('isotope-wiring.attributed-object.v1', encodeObject(target)),
  });
  const plan = Object.freeze({ spec, rule, match, operation, target, deleted: deepFreeze(deleted), created: deepFreeze(created),
    complement: complement.object, inclusion: complement.inclusion, retained, comatch,
    firstComparison, interfaceToComplement: kToD });
  plans.set(plan, store); return plan;
}

export function applyRewrite(store, currentRevision, plan) {
  requireThat(plans.get(plan) === store, 'unchecked-or-foreign-rule-plan');
  requireThat(currentRevision === plan.spec.inputRevision, 'stale-rule-boundary');
  const result = store.applyPatch(currentRevision, plan.operation);
  const witness = seal('isotope-wiring.rule-application.v1', {
    format: 'isotope-wiring.rule-application.v1', spec: plan.spec,
    outputRevision: result.revision.id, afterStateId: result.revision.stateId, receiptId: result.receipt.id,
  });
  return Object.freeze({ ...result, witness });
}

// Factor a surviving match through D -> X, then follow D -> Y. This is an
// explicit transport map; it is not a search for a convenient new occurrence.
export function transportMatch(plan, match) {
  requireThat(plans.has(plan), 'unchecked-rule-plan');
  composeAttributed(match, attributedIdentity(match.source));
  requireThat(equalAttributedObjects(match.target, plan.match.target), 'transport-source-mismatch');
  const collisions = [];
  for (const s of match.source.diagram.schema.sorts) for (const [pattern, image] of Object.entries(match.map.components[s]))
    if (plan.deleted[s].includes(image)) collisions.push({ sort: s, pattern, image });
  requireThat(collisions.length === 0, 'transport-deleted-match', collisions);
  const factor = attributedMorphism(match.source, plan.complement, match.map.components);
  requireThat(equalMorphisms(composeAttributed(plan.inclusion, factor).map, match.map), 'transport-square-mismatch');
  return Object.freeze({ factor, match: composeAttributed(plan.retained, factor) });
}

function decodePlan(store, spec) {
  checkSeal('isotope-wiring.rule-plan.v1', spec);
  requireThat(spec.engineDigest === revisionEngineDigest, 'rule-engine-mismatch');
  const rule = importRule(spec.rule), target = store.state(spec.inputRevision).object;
  const match = attributedMorphism(rule.left.target, target, spec.match);
  const plan = planRewrite(store, spec.inputRevision, rule, match, spec.allocation);
  requireThat(canonicalJSON(plan.spec) === canonicalJSON(spec), 'rule-plan-replay-mismatch'); return plan;
}
export function verifyRewriteWitness(store, input) {
  const witness = jsonClone(input); checkSeal('isotope-wiring.rule-application.v1', witness);
  const scratch = importRevisionBundle(store.exportBundle()), plan = decodePlan(scratch, witness.spec);
  const actual = applyRewrite(scratch, plan.spec.inputRevision, plan).witness;
  requireThat(canonicalJSON(actual) === canonicalJSON(witness), 'rule-application-replay-mismatch');
  return true;
}

// Audit claims retained in ground-history provenance. Ground replay alone does
// not establish that a declared typed rule was the actual derivation.
export function verifyRuleHistory(store) {
  const bundle = store.exportBundle(), scratch = importRevisionBundle(bundle), applications = [];
  let otherOperations = 0;
  for (const receipt of bundle.steps) {
    const origin = receipt.operation.provenance;
    if (origin?.kind !== 'declared-typed-rule') { otherOperations++; continue; }
    const rule = importRule(origin.rule), object = scratch.state(receipt.inputRevision).object;
    const match = attributedMorphism(rule.left.target, object, origin.match);
    const plan = planRewrite(scratch, receipt.inputRevision, rule, match, origin.allocation);
    requireThat(canonicalJSON(plan.operation) === canonicalJSON(receipt.operation), 'declared-rule-operation-mismatch');
    const actual = applyRewrite(scratch, receipt.inputRevision, plan);
    requireThat(actual.receipt.id === receipt.id, 'declared-rule-receipt-mismatch');
    applications.push(actual.witness);
  }
  return deepFreeze({ status: applications.length ? 'verified' : 'notApplicable', engineDigest: revisionEngineDigest,
    applications, otherOperations, scope: 'Only operations explicitly declaring a typed rule; no model-validity or authentication claim' });
}

// Sufficient parallel-independence conditions for this monic, unguarded rule
// fragment. Rejection is NOT a proof that all alternative sequential routes fail.
export function proveIndependent(store, a, b) {
  requireThat(plans.get(a) === store && plans.get(b) === store, 'unchecked-or-foreign-rule-plan');
  requireThat(a.spec.inputRevision === b.spec.inputRevision, 'independence-source-mismatch');
  const conflicts = [];
  for (const [first, second, direction] of [[a, b, 'A-deletes-B-match'], [b, a, 'B-deletes-A-match']])
    for (const s of first.target.diagram.schema.sorts) for (const image of Object.values(second.match.map.components[s]))
      if (first.deleted[s].includes(image)) conflicts.push({ direction, sort: s, id: image });
  requireThat(conflicts.length === 0, 'delete-read-conflict', conflicts);
  for (const s of a.target.diagram.schema.sorts) requireThat(!a.created[s].some(id => b.created[s].includes(id)), 'parallel-allocation-conflict', { sort: s });
  const scratch = importRevisionBundle(store.exportBundle()), inputRevision = a.spec.inputRevision;
  function route(first, second) {
    const p = decodePlan(scratch, first.spec), one = applyRewrite(scratch, inputRevision, p);
    const transported = transportMatch(p, second.match);
    const q = planRewrite(scratch, one.revision.id, second.rule, transported.match, second.spec.allocation);
    const two = applyRewrite(scratch, one.revision.id, q);
    return { first: one.witness, second: two.witness };
  }
  const ab = route(a, b), ba = route(b, a);
  const left = scratch.state(ab.second.outputRevision), right = scratch.state(ba.second.outputRevision);
  requireThat(left.id === right.id && canonicalJSON(left.data) === canonicalJSON(right.data), 'independence-state-square-failed');
  const witness = seal('isotope-wiring.independence.v1', {
    format: 'isotope-wiring.independence.v1', engineDigest: revisionEngineDigest,
    inputRevision, inputs: [a.spec, b.spec], ab, ba, commonStateId: left.id,
    scope: 'commuting full-state square; revision paths remain distinct; no model-validity preservation claim',
  });
  return Object.freeze({ witness, bundle: deepFreeze(scratch.exportBundle()) });
}
// Classify this supplied peak only. Joint coverage is recorded separately;
// overlaps are not an enumeration of critical pairs up to isomorphism.
export function analyzeOverlap(store, a, b) {
  requireThat(plans.get(a) === store && plans.get(b) === store, 'unchecked-or-foreign-rule-plan');
  requireThat(a.spec.inputRevision === b.spec.inputRevision, 'overlap-source-mismatch');
  const d = store.state(a.spec.inputRevision).object.diagram;
  const shared = [], deleteRead = [], allocations = [], uncovered = {};
  for (const s of d.schema.sorts) {
    const ai = new Set(Object.values(a.match.map.components[s])), bi = new Set(Object.values(b.match.map.components[s]));
    for (const id of d.sets[s]) if (ai.has(id) && bi.has(id)) {
      const aDeletes = a.deleted[s].includes(id), bDeletes = b.deleted[s].includes(id);
      shared.push({ sort: s, id, aDeletes, bDeletes });
      if (aDeletes) deleteRead.push({ direction: 'A-deletes-B-match', sort: s, id });
      if (bDeletes) deleteRead.push({ direction: 'B-deletes-A-match', sort: s, id });
    }
    for (const id of a.created[s]) if (b.created[s].includes(id)) allocations.push({ sort: s, id });
    uncovered[s] = d.sets[s].filter(id => !ai.has(id) && !bi.has(id));
  }
  return seal('isotope-wiring.overlap.v1', {
    format: 'isotope-wiring.overlap.v1', engineDigest: revisionEngineDigest, inputRevision: a.spec.inputRevision,
    inputs: [a.spec, b.spec], shared, deleteRead, allocations,
    independenceCriterion: deleteRead.length || allocations.length ? 'not-satisfied' : 'conditions-satisfied',
    coverage: { jointlyCoverIncidence: Object.values(uncovered).every(ids => ids.length === 0), uncovered },
    scope: 'Classification of supplied matches; no exhaustive critical-pair or nonjoinability claim',
  });
}

// Execute only the supplied joining routes. A failing endpoint comparison does
// not say that other matches, rules, or longer continuations cannot join.
export function checkSuppliedJoin(store, a, b, leftSteps = [], rightSteps = [], { maxStepsPerBranch = 16 } = {}) {
  const peak = analyzeOverlap(store, a, b);
  requireThat(Number.isSafeInteger(maxStepsPerBranch) && maxStepsPerBranch >= 0 && maxStepsPerBranch <= 64, 'invalid-join-bound');
  function normalize(steps) {
    requireThat(Array.isArray(steps) && steps.length <= maxStepsPerBranch, 'join-bound-exceeded');
    return steps.map(step => {
      requireThat(step && Object.keys(step).every(k => ['rule', 'match', 'allocation'].includes(k)), 'join-step-fields-mismatch');
      return { rule: exportRule(step.rule), match: jsonClone(step.match), allocation: jsonClone(step.allocation ?? {}) };
    });
  }
  const continuations = { left: normalize(leftSteps), right: normalize(rightSteps) };
  const scratch = importRevisionBundle(store.exportBundle());
  function execute(spec, steps) {
    const initial = decodePlan(scratch, spec), first = applyRewrite(scratch, spec.inputRevision, initial);
    let revision = first.revision.id; const applications = [first.witness];
    for (const step of steps) {
      const rule = importRule(step.rule), target = scratch.state(revision).object;
      const match = attributedMorphism(rule.left.target, target, step.match);
      const plan = planRewrite(scratch, revision, rule, match, step.allocation);
      const next = applyRewrite(scratch, revision, plan); applications.push(next.witness); revision = next.revision.id;
    }
    return { outputRevision: revision, applications };
  }
  const left = execute(a.spec, continuations.left), right = execute(b.spec, continuations.right);
  const x = scratch.state(left.outputRevision), y = scratch.state(right.outputRevision);
  const joined = x.id === y.id && canonicalJSON(x.data) === canonicalJSON(y.data);
  const witness = seal('isotope-wiring.supplied-join.v1', {
    format: 'isotope-wiring.supplied-join.v1', engineDigest: revisionEngineDigest, peak, continuations, maxStepsPerBranch,
    status: joined ? 'joined' : 'notJoined', left, right, leftStateId: x.id, rightStateId: y.id,
    scope: 'Only the supplied finite continuations; unequal endpoints do not prove nonjoinability; revision histories remain distinct',
  });
  return Object.freeze({ witness, bundle: deepFreeze(scratch.exportBundle()) });
}
export function verifyJoinWitness(store, input) {
  const witness = jsonClone(input); checkSeal('isotope-wiring.supplied-join.v1', witness);
  requireThat(witness.engineDigest === revisionEngineDigest && witness.peak?.inputs?.length === 2, 'invalid-join-witness');
  const scratch = importRevisionBundle(store.exportBundle());
  const [a, b] = witness.peak.inputs.map(spec => decodePlan(scratch, spec));
  const steps = list => list.map(s => ({ rule: importRule(s.rule), match: s.match, allocation: s.allocation }));
  const actual = checkSuppliedJoin(scratch, a, b, steps(witness.continuations.left), steps(witness.continuations.right), { maxStepsPerBranch: witness.maxStepsPerBranch }).witness;
  requireThat(canonicalJSON(actual) === canonicalJSON(witness), 'join-replay-mismatch'); return true;
}

export function verifyIndependenceWitness(store, input) {
  const witness = jsonClone(input); checkSeal('isotope-wiring.independence.v1', witness);
  requireThat(witness.engineDigest === revisionEngineDigest && Array.isArray(witness.inputs) && witness.inputs.length === 2, 'invalid-independence-witness');
  const scratch = importRevisionBundle(store.exportBundle());
  const [a, b] = witness.inputs.map(spec => decodePlan(scratch, spec));
  const actual = proveIndependent(scratch, a, b).witness;
  requireThat(canonicalJSON(actual) === canonicalJSON(witness), 'independence-replay-mismatch'); return true;
}
