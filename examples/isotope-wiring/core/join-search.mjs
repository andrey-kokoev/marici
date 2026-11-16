import { createHash } from 'node:crypto';
import { attributedMorphism, canonicalJSON, jsonClone, deepFreeze } from './attributed-diagrams.mjs';
import { importRevisionBundle, revisionEngineDigest, RewriteError } from './revisions.mjs';
import { exportRule, importRule, planRewrite, applyRewrite, checkSuppliedJoin } from './rules.mjs';
import { enumerateRuleMatches, materializeRuleMatch, normalizeMatchLimits, matchAllocationPolicy } from './matching.mjs';
import { checkSuppliedIsomorphicJoin, normalizeIsomorphismLimits, normalizeJoinTrackingPolicy } from './isomorphic-joins.mjs';

const demand = (condition, code, detail = null) => { if (!condition) throw new RewriteError(code, detail); };
const hash = body => createHash('sha256').update('isotope-wiring.join-search.v1\n' + canonicalJSON(body)).digest('hex');

// Breadth-first exploration of two finite route trees. Histories are NOT
// deduplicated by state; the state index only finds an endpoint on the other side.
export function searchRuleJoin(store, a, b, continuationRules, options = {}) {
  demand(Array.isArray(continuationRules) && continuationRules.length <= 16, 'join-search-rule-bound');
  const pool = [...continuationRules], rules = pool.map(exportRule);
  demand(new Set(rules.map(r => r.id)).size === rules.length, 'duplicate-join-search-rule');
  demand(options && typeof options === 'object' && !Array.isArray(options)
    && Object.keys(options).every(k => ['maxDepth', 'maxNodes', 'matchOptions', 'comparison', 'maxComparisons', 'isomorphismOptions', 'trackingPolicy'].includes(k)), 'invalid-join-search-options');
  const limits = { maxDepth: options.maxDepth === undefined ? 2 : options.maxDepth,
    maxNodes: options.maxNodes === undefined ? 128 : options.maxNodes,
    matchOptions: normalizeMatchLimits(options.matchOptions === undefined ? {} : options.matchOptions),
    comparison: options.comparison === undefined ? 'exact' : options.comparison,
    trackingPolicy: normalizeJoinTrackingPolicy(options.trackingPolicy),
    maxComparisons: options.maxComparisons === undefined ? 128 : options.maxComparisons,
    isomorphismOptions: normalizeIsomorphismLimits(options.isomorphismOptions === undefined ? {} : options.isomorphismOptions) };
  demand(['exact', 'anchoredIsomorphism'].includes(limits.comparison), 'invalid-join-search-comparison');
  demand(limits.comparison === 'anchoredIsomorphism' || limits.trackingPolicy === 'commonSurvivors', 'persistent-tracking-requires-anchored-comparison');
  demand(Number.isSafeInteger(limits.maxComparisons) && limits.maxComparisons >= 1 && limits.maxComparisons <= 4096, 'invalid-join-search-comparison-bound');
  demand(Number.isSafeInteger(limits.maxDepth) && limits.maxDepth >= 0 && limits.maxDepth <= 8, 'invalid-join-search-depth');
  demand(Number.isSafeInteger(limits.maxNodes) && limits.maxNodes >= 2 && limits.maxNodes <= 1024, 'invalid-join-search-node-bound');
  const initial = checkSuppliedJoin(store, a, b, [], [], { maxStepsPerBranch: limits.maxDepth });
  const scratch = importRevisionBundle(initial.bundle);
  const schema = scratch.state(initial.witness.left.outputRevision).object.diagram.schema;
  for (const rule of pool)
    demand(canonicalJSON(rule.left.target.diagram.schema) === canonicalJSON(schema), 'join-search-rule-schema-mismatch');
  const queue = ['left', 'right'].map(side => ({ side, revision: initial.witness[side].outputRevision, steps: [] }));
  const index = { left: new Map(), right: new Map() };
  const stateKey = revision => canonicalJSON(scratch.state(revision).data);
  for (const root of queue) index[root.side].set(stateKey(root.revision), root);
  const cutoffs = [], matchSearches = [], endpointComparisons = [];
  let expandedNodes = 0, discoveredNodes = 2;
  function finish(join, coverage) {
    const body = {
      format: 'isotope-wiring.join-search.v1', engineDigest: revisionEngineDigest,
      peak: initial.witness.peak, rules, limits, allocationPolicy: matchAllocationPolicy,
      status: join ? join.witness.status : 'notFound', coverage, discoveredNodes, expandedNodes,
      matchSearches, endpointComparisons, cutoffs, witness: join?.witness ?? null,
      scope: `${limits.comparison === 'exact' ? 'Exact full-state' : 'Common-survivor-anchored isomorphic'} joins using this ordered rule list and one deterministic fresh-allocation policy; tracking policy ${limits.trackingPolicy}; bounded route trees only; notFound does not prove nonjoinability or confluence`,
    };
    return Object.freeze({ report: deepFreeze({ ...body, id: hash(body) }), bundle: join?.bundle ?? null });
  }
  function comparePair(left, right) {
    if (endpointComparisons.length >= limits.maxComparisons) {
      cutoffs.push({ kind: 'maxComparisons' }); return { capped: true, join: null };
    }
    const result = checkSuppliedIsomorphicJoin(store, a, b, left.steps, right.steps,
      { ...limits.isomorphismOptions, trackingPolicy: limits.trackingPolicy, maxStepsPerBranch: limits.maxDepth });
    const { witness } = result, comparison = witness.comparison;
    demand(witness.routes.left.outputRevision === left.revision && witness.routes.right.outputRevision === right.revision, 'join-search-comparison-boundary-mismatch');
    endpointComparisons.push({ leftRevision: left.revision, rightRevision: right.revision,
      witnessId: witness.id, comparisonId: comparison?.id ?? null, status: comparison?.status ?? 'notCompared',
      reason: comparison?.reason ?? 'persistent-source-loss', searchNodes: comparison?.searchNodes ?? 0,
      admission: witness.status, lostPersistentCount: Object.values(witness.tracking.lostAfterPeak).reduce((n, xs) => n + xs.length, 0) });
    if (comparison && (comparison.status === 'unknown' || comparison.status === 'notCompared'))
      cutoffs.push({ kind: 'isomorphism', leftRevision: left.revision, rightRevision: right.revision, reason: comparison.reason });
    return { capped: false, join: witness.status === 'joinedUpToIsomorphism' ? result : null };
  }
  if (limits.comparison === 'anchoredIsomorphism') {
    const compared = comparePair(queue[0], queue[1]);
    if (compared.join) return finish(compared.join, 'stoppedAtJoin');
  } else if (initial.witness.status === 'joined') return finish(initial, 'stoppedAtJoin');
  for (let cursor = 0; cursor < queue.length; cursor++) {
    const node = queue[cursor];
    if (node.steps.length >= limits.maxDepth) continue;
    expandedNodes++;
    for (const rule of pool) {
      let census;
      try { census = enumerateRuleMatches(scratch, node.revision, rule, limits.matchOptions); }
      catch (error) {
        if (!(error instanceof RewriteError) || error.code !== 'match-object-bound-exceeded') throw error;
        cutoffs.push({ kind: 'matchObjectBound', side: node.side, revision: node.revision, ruleId: rule.id, detail: error.detail });
        continue;
      }
      matchSearches.push({ side: node.side, revision: node.revision, ruleId: rule.id, censusId: census.id,
        status: census.status, exhaustedBy: census.exhaustedBy, searchNodes: census.searchNodes, counts: census.counts });
      if (census.status === 'partial') cutoffs.push({ kind: 'matching', side: node.side, revision: node.revision,
        ruleId: rule.id, exhaustedBy: census.exhaustedBy });
      for (const entry of census.matches) {
        if (entry.applicability !== 'applicable') continue;
        if (discoveredNodes >= limits.maxNodes) {
          cutoffs.push({ kind: 'maxNodes' }); return finish(null, 'partial');
        }
        const { plan } = materializeRuleMatch(scratch, node.revision, rule, entry.components);
        demand(plan && canonicalJSON(plan.spec) === canonicalJSON(entry.plan), 'join-search-match-replay-mismatch');
        const applied = applyRewrite(scratch, node.revision, plan);
        const next = { side: node.side, revision: applied.revision.id, steps: [...node.steps,
          { rule, match: entry.components, allocation: entry.allocation }] };
        discoveredNodes++;
        if (limits.comparison === 'anchoredIsomorphism') {
          // Compare route nodes, not deduplicated states: identical states may
          // carry different surviving-source tracks.
          for (const other of queue) {
            if (other.side === next.side) continue;
            const compared = comparePair(next.side === 'left' ? next : other, next.side === 'right' ? next : other);
            if (compared.capped) return finish(null, 'partial');
            if (compared.join) return finish(compared.join, 'stoppedAtJoin');
          }
        } else {
          const key = stateKey(next.revision), other = index[node.side === 'left' ? 'right' : 'left'].get(key);
          if (other) {
            const left = node.side === 'left' ? next : other, right = node.side === 'right' ? next : other;
            const join = checkSuppliedJoin(store, a, b, left.steps, right.steps, { maxStepsPerBranch: limits.maxDepth });
            demand(join.witness.status === 'joined', 'join-search-endpoint-mismatch');
            return finish(join, 'stoppedAtJoin');
          }
          if (!index[node.side].has(key)) index[node.side].set(key, next);
        }
        queue.push(next);
      }
    }
  }
  return finish(null, cutoffs.length ? 'partial' : 'exhaustedDepthBound');
}

export function verifyJoinSearch(store, input) {
  const report = jsonClone(input);
  demand(report && typeof report === 'object' && !Array.isArray(report), 'invalid-join-search-report');
  const { id, ...body } = report;
  demand(id === hash(body), 'join-search-digest-mismatch');
  demand(report.engineDigest === revisionEngineDigest && report.peak?.inputs?.length === 2
    && Array.isArray(report.rules), 'join-search-engine-or-input-mismatch');
  const scratch = importRevisionBundle(store.exportBundle());
  const plans = report.peak.inputs.map(spec => {
    const rule = importRule(spec.rule), target = scratch.state(spec.inputRevision).object;
    const match = attributedMorphism(rule.left.target, target, spec.match);
    const plan = planRewrite(scratch, spec.inputRevision, rule, match, spec.allocation);
    demand(canonicalJSON(plan.spec) === canonicalJSON(spec), 'join-search-plan-replay-mismatch'); return plan;
  });
  const actual = searchRuleJoin(scratch, ...plans, report.rules.map(importRule), report.limits).report;
  demand(canonicalJSON(actual) === canonicalJSON(report), 'join-search-replay-mismatch'); return true;
}
