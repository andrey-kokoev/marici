import { createHash } from 'node:crypto';
import { isMonomorphism } from './finite-diagrams.mjs';
import { attributedMorphism, canonicalJSON, jsonClone, deepFreeze } from './attributed-diagrams.mjs';
import { exportRule, importRule, planRewrite } from './rules.mjs';
import { revisionEngineDigest, RewriteError } from './revisions.mjs';

const demand = (condition, code, detail = null) => { if (!condition) throw new RewriteError(code, detail); };
const hash = (domain, value) => createHash('sha256').update(domain + '\n' + canonicalJSON(value)).digest('hex');
const seal = (domain, body) => deepFreeze({ ...body, id: hash(domain, body) });
const sameKeys = (o, keys) => canonicalJSON(Object.keys(o).sort()) === canonicalJSON([...keys].sort());

function boundary(store, revisionId, rule) {
  exportRule(rule); // Refuse unchecked rule-shaped data.
  const state = store.state(revisionId), pattern = rule.left.target, host = state.object;
  demand(canonicalJSON(pattern.diagram.schema) === canonicalJSON(host.diagram.schema), 'match-schema-mismatch');
  return { state, pattern, host, schema: host.diagram.schema };
}

// One deterministic fresh allocation, NOT an enumeration of possible names.
// Include previously deleted names in the exclusion set, as planRewrite requires.
function allocate(rule, host, components) {
  return Object.fromEntries(host.diagram.schema.sorts.map(s => {
    const preserved = new Set(Object.values(rule.right.map.components[s])), used = new Set(host.diagram.sets[s]);
    return [s, Object.fromEntries(rule.right.target.diagram.sets[s].filter(x => !preserved.has(x)).map(x => {
      let id = 'match-' + hash('isotope-wiring.match-allocation.v1', { ruleId: rule.id, components, sort: s, record: x });
      while (used.has(id)) id = '_' + id;
      used.add(id); return [x, id];
    }))];
  }));
}

export function materializeRuleMatch(store, revisionId, rule, components) {
  const { pattern, host } = boundary(store, revisionId, rule);
  const match = attributedMorphism(pattern, host, components);
  demand(isMonomorphism(match.map), 'rule-match-must-be-monic');
  const allocation = allocate(rule, host, match.map.components);
  let plan = null, refusal = null;
  try { plan = planRewrite(store, revisionId, rule, match, allocation); }
  catch (error) {
    if (!(error instanceof RewriteError) || error.code !== 'rule-dangling-condition') throw error;
    refusal = { code: error.code, detail: error.detail };
  }
  const entry = deepFreeze({ components: match.map.components, applicability: plan ? 'applicable' : 'dangling',
    allocation, plan: plan?.spec ?? null, refusal });
  return Object.freeze({ match, plan, entry });
}

export const matchAllocationPolicy = 'match-local-fresh.v1';

export function normalizeMatchLimits(options = {}) {
  demand(options && typeof options === 'object' && !Array.isArray(options), 'invalid-match-options');
  const limits = { maxSearchNodes: 10000, maxMatches: 256, maxPatternRecords: 24, maxHostRecords: 128, ...jsonClone(options) };
  const maxima = { maxSearchNodes: 1000000, maxMatches: 4096, maxPatternRecords: 128, maxHostRecords: 4096 };
  demand(sameKeys(limits, Object.keys(maxima)), 'unknown-match-option');
  for (const [name, value] of Object.entries(limits))
    demand(Number.isSafeInteger(value) && value >= 1 && value <= maxima[name], 'invalid-match-limit', { name });
  return deepFreeze(limits);
}

export function enumerateRuleMatches(store, revisionId, rule, options = {}) {
  const { state, pattern, host, schema } = boundary(store, revisionId, rule);
  const limits = normalizeMatchLimits(options);
  for (const [object, name] of [[pattern, 'maxPatternRecords'], [host, 'maxHostRecords']]) {
    const size = schema.sorts.reduce((n, s) => n + object.diagram.sets[s].length, 0);
    demand(size <= limits[name], 'match-object-bound-exceeded', { name, actual: size, maximum: limits[name] });
  }
  // Fixed schema/record order makes replay independent of heuristic tie breaking.
  const tasks = schema.sorts.flatMap(s => pattern.diagram.sets[s].map(x => ({ s, x,
    images: host.diagram.sets[s].filter(y => canonicalJSON(pattern.labels[s][x]) === canonicalJSON(host.labels[s][y])),
  })));
  const components = Object.fromEntries(schema.sorts.map(s => [s, Object.create(null)]));
  const used = Object.fromEntries(schema.sorts.map(s => [s, new Set()]));
  function naturalSoFar() {
    for (const a of schema.arrows) for (const [x, y] of Object.entries(components[a.from])) {
      const z = pattern.diagram.maps[a.name][x];
      if (Object.hasOwn(components[a.to], z) && components[a.to][z] !== host.diagram.maps[a.name][y]) return false;
    }
    return true;
  }
  const matches = []; let searchNodes = 0, exhaustedBy = null;
  function visit(index) {
    if (exhaustedBy) return;
    if (searchNodes >= limits.maxSearchNodes) { exhaustedBy = 'maxSearchNodes'; return; }
    searchNodes++;
    if (!naturalSoFar()) return;
    if (index === tasks.length) {
      if (matches.length >= limits.maxMatches) { exhaustedBy = 'maxMatches'; return; }
      matches.push(materializeRuleMatch(store, revisionId, rule, components).entry); return;
    }
    const { s, x, images } = tasks[index];
    for (const y of images) {
      if (exhaustedBy) break;
      if (used[s].has(y)) continue;
      components[s][x] = y; used[s].add(y); visit(index + 1); used[s].delete(y); delete components[s][x];
    }
  }
  visit(0);
  const counts = { applicable: 0, dangling: 0 };
  for (const entry of matches) counts[entry.applicability]++;
  return seal('isotope-wiring.rule-match-census.v1', {
    format: 'isotope-wiring.rule-match-census.v1', engineDigest: revisionEngineDigest,
    inputRevision: revisionId, inputStateId: state.id, rule: exportRule(rule), limits,
    allocationPolicy: matchAllocationPolicy, status: exhaustedBy ? 'partial' : 'complete', exhaustedBy,
    searchNodes, counts, matches,
    scope: 'Injective exact-label natural transformations from this fixed pattern into this fixed host; no automorphism quotient, guards, frame transport, model-validity or confluence claim',
  });
}

export function verifyRuleMatchCensus(store, input) {
  const census = jsonClone(input);
  demand(census && typeof census === 'object' && !Array.isArray(census), 'invalid-match-census');
  const { id, ...body } = census;
  demand(id === hash('isotope-wiring.rule-match-census.v1', body), 'match-census-digest-mismatch');
  demand(census.engineDigest === revisionEngineDigest, 'match-census-engine-mismatch');
  const actual = enumerateRuleMatches(store, census.inputRevision, importRule(census.rule), census.limits);
  demand(canonicalJSON(actual) === canonicalJSON(census), 'match-census-replay-mismatch'); return true;
}
