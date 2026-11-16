import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import { attributeDiagram } from '../examples/isotope-wiring/core/attributed-diagrams.mjs';
import { importLegacyAbsolute } from '../examples/isotope-wiring/core/legacy-adapter.mjs';
import { verifyModel, verifyModelSelectively } from '../examples/isotope-wiring/core/model-predicates.mjs';
import { createRevisionStore, importRevisionBundle, RewriteError } from '../examples/isotope-wiring/core/revisions.mjs';

const context = vm.createContext({});
vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8').match(/<script>([\s\S]*?)<\/script>/)[1], context, { timeout: 5000 });
const fixtures = JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures()));
const clone = x => JSON.parse(JSON.stringify(x));
const modes = report => Object.fromEntries(report.evaluation.predicates.map(p => [p.predicate, p.mode]));
const reused = report => report.evaluation.predicates.filter(p => p.mode === 'reused').map(p => p.predicate).sort();
function setup() {
  const packet = importLegacyAbsolute(fixtures.O16), store = createRevisionStore(), seed = store.seed(packet.object, packet.modelContext);
  const baseline = store.verifyAt(seed.id); return { packet, store, seed, baseline };
}
function agrees(store, revision, selected) {
  const s = store.state(revision), full = verifyModel(s.object, s.context);
  assert.deepEqual(selected.result.checks, full.checks); assert.equal(selected.result.status, full.status);
  assert.equal(selected.result.inputDigest, full.inputDigest);
}

test('metadata-only edits can explicitly transport every predicate without inheriting a report automatically', () => {
  const { store, seed, baseline } = setup();
  const next = store.applyPatch(seed.id, store.preparePatch(seed.id, { metadataAfter: { note: 'new note' } })).revision;
  assert.equal(store.verification(next.id), null);
  const selected = store.verifyAt(next.id, { reuseFrom: seed.id });
  assert.equal(reused(selected.result).length, 7);
  assert.deepEqual(selected.transportFrom, { revisionId: seed.id, verificationId: baseline.id });
  assert.notEqual(selected.stateId, baseline.stateId); assert.notEqual(selected.revisionId, baseline.revisionId);
  agrees(store, next.id, selected);
  store.verifyAt(seed.id, { reuseFrom: seed.id });
  assert.equal(store.verificationById(baseline.id), baseline, 'baseline remains accessible after the latest report changes');
});

test('target changes reuse six structural predicates but recompute the inventory claim', () => {
  const { store, seed } = setup(), c = clone(store.state(seed.id).context); c.targets.Z = 9;
  const next = store.applyPatch(seed.id, store.preparePatch(seed.id, { contextAfter: c })).revision;
  const selected = store.verifyAt(next.id, { reuseFrom: seed.id });
  assert.equal(reused(selected.result).length, 6); assert.equal(modes(selected.result)['inventory-targets'], 'computed');
  assert.equal(selected.result.status, 'refuted'); agrees(store, next.id, selected);
});

test('pair deletion preserves only the unchanged lattice/support/witness reads', () => {
  const { store, seed } = setup();
  const next = store.applyPatch(seed.id, store.preparePatch(seed.id, { remove: [{ sort: 'pair', id: fixtures.O16.graph.pairs[0].id }] })).revision;
  const selected = store.verifyAt(next.id, { reuseFrom: seed.id });
  assert.deepEqual(reused(selected.result), ['lattice-incidence', 'support-incidence', 'witness-grammar']);
  assert.equal(selected.result.status, 'refuted'); agrees(store, next.id, selected);
});

test('dependency-status changes block reuse even when a predicate body sees unchanged incidence', () => {
  const { packet, baseline } = setup(), labels = clone(packet.object.labels);
  const support = packet.object.diagram.sets.support[0]; labels.support[support].endpoints[0].lattice[0]++;
  const changed = attributeDiagram(packet.object.diagram, labels);
  const selected = verifyModelSelectively(changed, packet.modelContext, baseline.result);
  assert.equal(modes(selected)['color-disjointness'], 'computed');
  assert.equal(selected.checks.find(c => c.predicate === 'color-disjointness').status, 'unknown');
  assert.deepEqual(selected.checks, verifyModel(changed, packet.modelContext).checks);
});

test('new witness records invalidate global duplicate/absence checks, not just previously observed IDs', () => {
  const { packet, baseline } = setup(), source = clone(fixtures.O16);
  source.graph.witnesses.push({ ...source.graph.witnesses[0], id: 'fresh-duplicate' });
  const changed = importLegacyAbsolute(source);
  const selected = verifyModelSelectively(changed.object, packet.modelContext, baseline.result);
  assert.equal(modes(selected)['witness-grammar'], 'computed');
  assert(selected.checks.find(c => c.predicate === 'witness-grammar').issues.some(i => i.code === 'duplicate-witness-slot'));
  assert.deepEqual(selected.checks, verifyModel(changed.object, packet.modelContext).checks);
});

test('negative and unknown results may be reused without promotion', () => {
  const packet = importLegacyAbsolute(fixtures['V51-conflict']);
  const bad = verifyModel(packet.object, packet.modelContext);
  const same = verifyModelSelectively(packet.object, packet.modelContext, bad);
  assert.equal(same.status, 'refuted'); assert.equal(reused(same).length, 7);
  const unknown = verifyModel(packet.object, {});
  const stillUnknown = verifyModelSelectively(packet.object, { unrelated: 'annotation' }, unknown);
  assert.equal(stillUnknown.checks.find(c => c.predicate === 'inventory-targets').status, 'unknown');
  assert.equal(modes(stillUnknown)['inventory-targets'], 'reused');
});

test('serialized reports are not trusted baselines and replay stores require fresh checks', () => {
  const { packet, store, seed, baseline } = setup();
  assert.throws(() => verifyModelSelectively(packet.object, packet.modelContext, clone(baseline.result)), /Untrusted verification baseline/);
  const replay = importRevisionBundle(store.exportBundle());
  assert.throws(() => replay.verifyAt(seed.id, { reuseFrom: seed.id }), e => e instanceof RewriteError && e.code === 'missing-verification-baseline');
  replay.verifyAt(seed.id);
  assert.equal(reused(replay.verifyAt(seed.id, { reuseFrom: seed.id }).result).length, 7);
});

test('selective and fresh evaluation agree for all 81 ordered fixture pairs and malformed-label hostiles', () => {
  const packets = Object.values(fixtures).map(importLegacyAbsolute);
  for (const a of packets) {
    const baseline = verifyModel(a.object, a.modelContext);
    for (const b of packets) {
      const selected = verifyModelSelectively(b.object, b.modelContext, baseline), fresh = verifyModel(b.object, b.modelContext);
      assert.deepEqual(selected.checks, fresh.checks); assert.equal(selected.status, fresh.status);
    }
  }
  const a = packets[0], base = verifyModel(a.object, a.modelContext);
  for (const mutate of [
    labels => { labels.shell.s1.size = 'bad'; },
    labels => { labels.port[Object.keys(labels.port)[0]].role = 'unknown'; },
    labels => { labels.cell['s2-01'].col = 0; },
    labels => { labels.lineWitness[Object.keys(labels.lineWitness)[0]].axis = 'V'; },
  ]) {
    const labels = clone(a.object.labels); mutate(labels);
    const changed = attributeDiagram(a.object.diagram, labels);
    assert.deepEqual(verifyModelSelectively(changed, a.modelContext, base).checks, verifyModel(changed, a.modelContext).checks);
  }
});
