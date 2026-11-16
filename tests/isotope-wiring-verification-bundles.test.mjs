import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import vm from 'node:vm';
import { execFileSync } from 'node:child_process';
import { importLegacyAbsolute } from '../examples/isotope-wiring/core/legacy-adapter.mjs';
import { canonicalJSON } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { createRevisionStore, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';
import { exportVerificationBundle, replayVerificationBundle } from '../examples/isotope-wiring/core/verification-bundles.mjs';

const ctx = vm.createContext({});
vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8').match(/<script>([\s\S]*?)<\/script>/)[1], ctx, { timeout: 5000 });
const fixture = JSON.parse(JSON.stringify(ctx.IsotopeWiring.fixtures().O16));
const clone = x => JSON.parse(JSON.stringify(x));
const code = value => e => e instanceof RewriteError && e.code === value;
function retag(domain, x) { const { id, ...body } = x; return { ...body, id: createHash('sha256').update(domain + '\n' + canonicalJSON(body)).digest('hex') }; }
const tagBundle = b => retag('isotope-wiring.verification-bundle.v1', b);
function setup() {
  const p = importLegacyAbsolute(fixture), store = createRevisionStore(), seed = store.seed(p.object, p.modelContext);
  const baseline = store.verifyAt(seed.id), context = clone(p.modelContext); context.targets.Z = 9;
  const next = store.applyPatch(seed.id, store.preparePatch(seed.id, { contextAfter: context })).revision;
  const selected = store.verifyAt(next.id, { reuseFrom: seed.id });
  return { store, seed, next, baseline, selected, packet: p };
}

test('a dependency-complete verification bundle recomputes roots and replays selective transport', () => {
  const { store, baseline, selected } = setup(), before = store.exportBundle();
  const bundle = exportVerificationBundle(store, [selected.id]);
  assert.deepEqual(bundle.reports.map(r => r.id), [baseline.id, selected.id]);
  const replay = replayVerificationBundle(JSON.parse(JSON.stringify(bundle)));
  assert.equal(replay.reports[0].id, selected.id); assert.equal(replay.reports[0].result.status, 'refuted');
  assert.equal(replay.reports[0].result.evaluation.predicates.filter(p => p.mode === 'reused').length, 6);
  assert.deepEqual(exportVerificationBundle(replay.store, bundle.roots), bundle);
  assert.deepEqual(store.exportBundle(), before);
});

test('verification chains replay in a fresh Node process without the original trusted cache', () => {
  const { store, selected } = setup(), bundle = exportVerificationBundle(store, [selected.id]);
  const moduleURL = new URL('../examples/isotope-wiring/core/verification-bundles.mjs', import.meta.url).href;
  const script = `import { readFileSync } from 'node:fs';
    const { replayVerificationBundle } = await import(${JSON.stringify(moduleURL)});
    const result = replayVerificationBundle(JSON.parse(readFileSync(0, 'utf8')));
    console.log(JSON.stringify(result.reports.map(r => ({ id: r.id, status: r.result.status }))));`;
  const output = execFileSync(process.execPath, ['--input-type=module', '-e', script], { input: JSON.stringify(bundle), encoding: 'utf8', timeout: 15000 });
  assert.deepEqual(JSON.parse(output), [{ id: selected.id, status: 'refuted' }]);
});

test('exact archived baseline IDs are replayed even when a newer report exists at that revision', () => {
  const { store, seed, next, baseline, selected } = setup();
  const newer = store.verifyAt(seed.id, { reuseVerificationId: baseline.id });
  assert.notEqual(newer.id, baseline.id);
  const fromNew = store.verifyAt(next.id, { reuseFrom: seed.id, reuseVerificationId: newer.id });
  const fromOld = store.verifyAt(next.id, { reuseFrom: seed.id, reuseVerificationId: baseline.id });
  assert.equal(fromOld.id, selected.id); assert.notEqual(fromNew.id, fromOld.id);
  const bundle = exportVerificationBundle(store, [fromNew.id, fromOld.id]);
  const replay = replayVerificationBundle(bundle);
  assert.deepEqual(replay.reports.map(r => r.id), bundle.roots);
  assert.equal(replay.store.verificationById(newer.id).transportFrom.verificationId, baseline.id);
  assert.throws(() => store.verifyAt(next.id, { reuseFrom: next.id, reuseVerificationId: baseline.id }), code('verification-baseline-binding-mismatch'));
});

test('missing and duplicate verification dependencies are refused', () => {
  const { store, selected } = setup(), original = exportVerificationBundle(store, [selected.id]);
  const missing = clone(original); missing.reports.shift();
  assert.throws(() => replayVerificationBundle(tagBundle(missing)), code('missing-verification-dependency'));
  const duplicate = clone(original); duplicate.reports.push(duplicate.reports[0]);
  assert.throws(() => replayVerificationBundle(tagBundle(duplicate)), code('duplicate-verification-report'));
  assert.throws(() => exportVerificationBundle(store, [selected.id, selected.id]), code('duplicate-verification-root'));
  assert.throws(() => exportVerificationBundle(store, ['missing']), code('missing-verification-dependency'));
});

test('false statuses and reuse claims fail semantic replay even after hashes are recomputed', () => {
  const { store, selected } = setup();
  const bad = clone(exportVerificationBundle(store, [selected.id]));
  const target = bad.reports.at(-1); target.result.status = 'verified';
  bad.reports[bad.reports.length - 1] = retag('isotope-wiring.revision-verification.v1', target);
  bad.roots = [bad.reports.at(-1).id];
  assert.throws(() => replayVerificationBundle(tagBundle(bad)), code('verification-report-replay-mismatch'));
  const altered = clone(exportVerificationBundle(store, [selected.id]));
  altered.reports.at(-1).result.evaluation.predicates.find(p => p.predicate === 'inventory-targets').mode = 'reused';
  altered.reports[altered.reports.length - 1] = retag('isotope-wiring.revision-verification.v1', altered.reports.at(-1));
  altered.roots = [altered.reports.at(-1).id];
  assert.throws(() => replayVerificationBundle(tagBundle(altered)), code('verification-report-replay-mismatch'));
});

test('baseline revision binding, engine mismatch and missing construction history are refused', () => {
  const { store, next, selected } = setup(), original = exportVerificationBundle(store, [selected.id]);
  const wrong = clone(original); wrong.reports.at(-1).transportFrom.revisionId = next.id;
  wrong.reports[wrong.reports.length - 1] = retag('isotope-wiring.revision-verification.v1', wrong.reports.at(-1)); wrong.roots = [wrong.reports.at(-1).id];
  assert.throws(() => replayVerificationBundle(tagBundle(wrong)), code('verification-baseline-binding-mismatch'));
  const engine = clone(original); engine.engineDigest = 'other';
  assert.throws(() => replayVerificationBundle(tagBundle(engine)), code('verification-bundle-engine-mismatch'));
  const missing = clone(original); missing.revisions.seeds = [];
  assert.throws(() => replayVerificationBundle(tagBundle(missing)), code('missing-revision'));
});

test('unreferenced valid reports are not silently admitted into the claimed dependency closure', () => {
  const { store, packet, selected } = setup();
  const unrelated = store.seed(packet.object, packet.modelContext, { independent: true }), report = store.verifyAt(unrelated.id);
  const bundle = clone(exportVerificationBundle(store, [selected.id])); bundle.reports.push(clone(report));
  assert.throws(() => replayVerificationBundle(tagBundle(bundle)), code('noncanonical-verification-bundle'));
});
