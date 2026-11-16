import { createHash } from 'node:crypto';
import { createDiagram } from './finite-diagrams.mjs';
import { attributeDiagram, attributedMorphism, attributedPushout, canonicalJSON, jsonClone, deepFreeze } from './attributed-diagrams.mjs';
import { exportRule, importRule, planRewrite, analyzeOverlap } from './rules.mjs';
import { createRevisionStore, revisionEngineDigest, RewriteError } from './revisions.mjs';

const demand = (condition, code, detail = null) => { if (!condition) throw new RewriteError(code, detail); };
const hash = (domain, body) => createHash('sha256').update(domain + '\n' + canonicalJSON(body)).digest('hex');
const seal = (domain, body) => deepFreeze({ ...body, id: hash(domain, body) });
const sameKeys = (o, keys) => canonicalJSON(Object.keys(o).sort()) === canonicalJSON([...keys].sort());

function patterns(a, b) {
  exportRule(a); exportRule(b); // Require checked rules.
  const left = a.left.target, right = b.left.target;
  demand(canonicalJSON(left.diagram.schema) === canonicalJSON(right.diagram.schema), 'overlap-schema-mismatch');
  return { left, right, schema: left.diagram.schema };
}
function closedRelation(schema, left, right, relation) {
  return schema.arrows.every(a => Object.entries(relation[a.from]).every(([x, y]) =>
    relation[a.to][left.diagram.maps[a.name][x]] === right.diagram.maps[a.name][y]));
}

// Reconstruct one explicitly labelled overlap. A partial bijection at each sort
// is the pullback of two monic, jointly covering matches, when incidence-closed.
export function materializeRuleOverlap(a, b, identifications) {
  const { left, right, schema } = patterns(a, b), relation = jsonClone(identifications);
  demand(relation && typeof relation === 'object' && !Array.isArray(relation) && sameKeys(relation, schema.sorts), 'overlap-relation-sorts-mismatch');
  for (const s of schema.sorts) {
    demand(relation[s] && typeof relation[s] === 'object' && !Array.isArray(relation[s]), 'invalid-overlap-relation');
    const values = Object.values(relation[s]);
    demand(new Set(values).size === values.length, 'overlap-relation-not-injective');
    for (const [x, y] of Object.entries(relation[s])) {
      demand(left.diagram.sets[s].includes(x) && right.diagram.sets[s].includes(y), 'overlap-relation-outside-pattern');
      demand(canonicalJSON(left.labels[s][x]) === canonicalJSON(right.labels[s][y]), 'overlap-label-mismatch');
    }
  }
  demand(closedRelation(schema, left, right, relation), 'overlap-relation-not-closed');
  const sets = Object.fromEntries(schema.sorts.map(s => [s, Object.keys(relation[s])]));
  const maps = Object.fromEntries(schema.arrows.map(a => [a.name, Object.fromEntries(sets[a.from].map(x => [x, left.diagram.maps[a.name][x]]))]));
  const labels = Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(sets[s].map(x => [x, left.labels[s][x]]))]));
  const k = attributeDiagram(createDiagram(schema, { sets, maps }), labels);
  const l = attributedMorphism(k, left, Object.fromEntries(schema.sorts.map(s => [s, Object.fromEntries(sets[s].map(x => [x, x]))])));
  const r = attributedMorphism(k, right, relation), sum = attributedPushout(l, r);
  const store = createRevisionStore();
  const seed = store.seed(sum.object, {}, { scope: 'labelled-rule-overlap', ruleIds: [a.id, b.id], identifications: relation });
  function allocate(rule, side) {
    return Object.fromEntries(schema.sorts.map(s => {
      const preserved = new Set(Object.values(rule.right.map.components[s]));
      return [s, Object.fromEntries(rule.right.target.diagram.sets[s].filter(x => !preserved.has(x)).map(x => {
        let id = `census-${side}:${JSON.stringify([s, x])}`;
        while (sum.object.diagram.sets[s].includes(id)) id = '_' + id;
        return [x, id];
      }))];
    }));
  }
  const refusals = [], planned = [];
  for (const [index, rule, match, side] of [[0, a, sum.left, 'A'], [1, b, sum.right, 'B']]) {
    try { planned[index] = planRewrite(store, seed.id, rule, match, allocate(rule, side)); }
    catch (error) {
      // Only mathematical applicability refusal belongs in the census.
      // Engine defects must abort instead of masquerading as completed coverage.
      if (!(error instanceof RewriteError) || error.code !== 'rule-dangling-condition') throw error;
      planned[index] = null; refusals.push({ side, code: error.code, detail: error.detail });
    }
  }
  const analysis = refusals.length ? null : analyzeOverlap(store, planned[0], planned[1]);
  const classification = refusals.length ? 'notCoApplicable' : analysis.independenceCriterion === 'conditions-satisfied' ? 'independent' : 'dependentPeak';
  const candidate = seal('isotope-wiring.overlap-candidate.v1', {
    format: 'isotope-wiring.overlap-candidate.v1', ruleIds: [a.id, b.id], identifications: relation,
    host: { diagram: sum.object.diagram, labels: sum.object.labels }, sourceRevision: seed.id,
    classification, refusals, analysis,
  });
  return Object.freeze({ store, seed, host: sum.object, plans: Object.freeze(planned), candidate });
}

export function enumerateRuleOverlaps(a, b, options = {}) {
  const { left, right, schema } = patterns(a, b);
  demand(options && typeof options === 'object' && !Array.isArray(options), 'invalid-census-options');
  const limits = { maxSearchNodes: 10000, maxCandidates: 256, maxPatternRecords: 24, ...jsonClone(options) };
  demand(sameKeys(limits, ['maxSearchNodes', 'maxCandidates', 'maxPatternRecords']), 'unknown-census-option');
  for (const [name, value] of Object.entries(limits)) demand(Number.isSafeInteger(value) && value >= 1, 'invalid-census-limit', { name });
  // Explicit safety bounds, not completeness claims outside these limits.
  demand(limits.maxSearchNodes <= 1000000 && limits.maxCandidates <= 4096 && limits.maxPatternRecords <= 128, 'census-limit-too-large');
  const size = schema.sorts.reduce((n, s) => n + left.diagram.sets[s].length + right.diagram.sets[s].length, 0);
  demand(size <= limits.maxPatternRecords, 'census-pattern-bound-exceeded', { actual: size, maximum: limits.maxPatternRecords });
  const tasks = schema.sorts.flatMap(s => left.diagram.sets[s].map(x => [s, x]));
  const relation = Object.fromEntries(schema.sorts.map(s => [s, Object.create(null)]));
  const used = Object.fromEntries(schema.sorts.map(s => [s, new Set()]));
  const candidates = []; let searchNodes = 0, closedRelations = 0, exhaustedBy = null;
  function visit(index) {
    if (exhaustedBy) return;
    if (searchNodes >= limits.maxSearchNodes) { exhaustedBy = 'maxSearchNodes'; return; }
    searchNodes++;
    if (index === tasks.length) {
      if (!closedRelation(schema, left, right, relation)) return;
      closedRelations++;
      if (candidates.length >= limits.maxCandidates) { exhaustedBy = 'maxCandidates'; return; }
      candidates.push(materializeRuleOverlap(a, b, relation).candidate); return;
    }
    const [s, x] = tasks[index];
    visit(index + 1); // x is outside the intersection.
    for (const y of right.diagram.sets[s]) {
      if (exhaustedBy) break;
      if (used[s].has(y) || canonicalJSON(left.labels[s][x]) !== canonicalJSON(right.labels[s][y])) continue;
      relation[s][x] = y; used[s].add(y); visit(index + 1); used[s].delete(y); delete relation[s][x];
    }
  }
  visit(0);
  const counts = { independent: 0, dependentPeak: 0, notCoApplicable: 0 };
  for (const c of candidates) counts[c.classification]++;
  return seal('isotope-wiring.overlap-census.v1', {
    format: 'isotope-wiring.overlap-census.v1', engineDigest: revisionEngineDigest,
    rules: [exportRule(a), exportRule(b)], limits, status: exhaustedBy ? 'partial' : 'complete', exhaustedBy,
    searchNodes, closedRelationsVisited: closedRelations, counts, candidates,
    equivalence: 'Fixed labelled rule patterns; host isomorphisms must commute with both matches; no rule-automorphism quotient',
    scope: 'All incidence-closed label-preserving partial bijections explored only when complete; applicability is structural, not model validity; no confluence claim',
  });
}

export function verifyOverlapCensus(input) {
  const census = jsonClone(input);
  demand(census && typeof census === 'object' && !Array.isArray(census), 'invalid-census');
  const { id, ...body } = census;
  demand(id === hash('isotope-wiring.overlap-census.v1', body), 'census-digest-mismatch');
  demand(census.engineDigest === revisionEngineDigest && census.rules?.length === 2, 'census-engine-or-rule-mismatch');
  const [a, b] = census.rules.map(importRule), actual = enumerateRuleOverlaps(a, b, census.limits);
  demand(canonicalJSON(actual) === canonicalJSON(census), 'census-replay-mismatch'); return true;
}
