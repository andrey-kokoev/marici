import { createHash } from 'node:crypto';
import { canonicalJSON, jsonClone, deepFreeze } from './attributed-diagrams.mjs';
import { importRevisionBundle, revisionEngineDigest, RewriteError } from './revisions.mjs';

const demand = (condition, code, detail = null) => { if (!condition) throw new RewriteError(code, detail); };
const hash = (domain, body) => createHash('sha256').update(domain + '\n' + canonicalJSON(body)).digest('hex');
const tagged = (body) => deepFreeze({ ...body, id: hash('isotope-wiring.verification-bundle.v1', body) });
const sameKeys = (o, keys) => canonicalJSON(Object.keys(o).sort()) === canonicalJSON([...keys].sort());

// The archive is transported as claims. Replay re-establishes every baseline
// with the checker before any selective result can be reused.
export function exportVerificationBundle(store, verificationIds) {
  demand(Array.isArray(verificationIds) && verificationIds.length > 0 && verificationIds.every(x => typeof x === 'string'), 'verification-roots-required');
  demand(new Set(verificationIds).size === verificationIds.length, 'duplicate-verification-root');
  const roots = [...verificationIds].sort(), reports = [], done = new Set(), active = new Set();
  function visit(id) {
    if (done.has(id)) return;
    demand(!active.has(id), 'cyclic-verification-dependency');
    demand(done.size + active.size < 1024, 'verification-report-bound-exceeded');
    const report = store.verificationById(id); demand(report, 'missing-verification-dependency', { id });
    active.add(id);
    if (report.transportFrom) {
      const baseline = store.verificationById(report.transportFrom.verificationId);
      demand(baseline && baseline.revisionId === report.transportFrom.revisionId, 'verification-baseline-binding-mismatch');
      visit(baseline.id);
    }
    active.delete(id); done.add(id); reports.push(report);
  }
  for (const root of roots) visit(root);
  return tagged({ format: 'isotope-wiring.verification-bundle.v1', engineDigest: revisionEngineDigest,
    revisions: store.exportBundle(), roots, reports,
    scope: 'Replay of checker reports and exact read-projection transport; not authentication, physical evidence, or typed-rule derivation certification',
  });
}

export function replayVerificationBundle(input) {
  const bundle = jsonClone(input);
  demand(bundle && typeof bundle === 'object' && !Array.isArray(bundle)
    && sameKeys(bundle, ['format', 'engineDigest', 'revisions', 'roots', 'reports', 'scope', 'id']), 'verification-bundle-fields-mismatch');
  const { id, ...body } = bundle;
  demand(id === hash('isotope-wiring.verification-bundle.v1', body), 'verification-bundle-digest-mismatch');
  demand(bundle.format === 'isotope-wiring.verification-bundle.v1' && bundle.engineDigest === revisionEngineDigest, 'verification-bundle-engine-mismatch');
  demand(Array.isArray(bundle.reports) && bundle.reports.length > 0 && bundle.reports.length <= 1024, 'verification-report-bound-exceeded');
  demand(Array.isArray(bundle.roots) && bundle.roots.length > 0, 'verification-roots-required');
  const store = importRevisionBundle(bundle.revisions), seen = new Set();
  for (const expected of bundle.reports) {
    demand(expected && typeof expected === 'object' && !Array.isArray(expected), 'invalid-verification-report');
    const { id: reportId, ...reportBody } = expected;
    demand(reportId === hash('isotope-wiring.revision-verification.v1', reportBody), 'verification-report-digest-mismatch');
    demand(!seen.has(reportId), 'duplicate-verification-report');
    demand(expected.engineDigest === revisionEngineDigest, 'verification-report-engine-mismatch');
    demand(store.revision(expected.revisionId).stateId === expected.stateId, 'verification-state-binding-mismatch');
    let options = {};
    if (expected.transportFrom) {
      const ref = expected.transportFrom;
      demand(seen.has(ref.verificationId), 'missing-verification-dependency', ref);
      demand(store.verificationById(ref.verificationId).revisionId === ref.revisionId, 'verification-baseline-binding-mismatch');
      options = { reuseFrom: ref.revisionId, reuseVerificationId: ref.verificationId };
    }
    const actual = store.verifyAt(expected.revisionId, options);
    demand(canonicalJSON(actual) === canonicalJSON(expected), 'verification-report-replay-mismatch', { reportId });
    seen.add(reportId);
  }
  for (const root of bundle.roots) demand(seen.has(root), 'missing-verification-root', { root });
  // Reject unreferenced claims, duplicate roots, and noncanonical dependency order.
  demand(canonicalJSON(exportVerificationBundle(store, bundle.roots)) === canonicalJSON(bundle), 'noncanonical-verification-bundle');
  return Object.freeze({ store, reports: Object.freeze(bundle.roots.map(root => store.verificationById(root))), bundleId: bundle.id });
}
