import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

const html = readFileSync(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8');
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
assert.equal(scripts.length, 1, 'Update the headless adapter if the app changes its script layout');
const context = vm.createContext({});
vm.runInContext(scripts[0][1], context, { timeout: 5000 });
const core = context.IsotopeWiring;
const fixtures = core.fixtures();
const plain = value => JSON.parse(JSON.stringify(value));

// Characterization of the legacy engine, not certification of the proposed architecture.
test('all supplied fixtures have their declared bounded grammar status', () => {
  for (const [id, doc] of Object.entries(fixtures)) {
    const result = core.validate(doc);
    assert.equal(result.valid, id !== 'V51-conflict', id);
    assert.equal(result.EP, doc.graph.pairs.length);
    assert.equal(result.N, doc.graph.witnesses.length);
  }
  assert(core.validate(fixtures.V51).issues.some(i => i.code === 'unresolved'));
  assert(core.validate(fixtures['V51-conflict']).issues.some(i => i.code === 'ep-count'));
});

test('all distinct-ID fixture pairs roundtrip at the existing graph projection', () => {
  for (const base of Object.values(fixtures)) for (const target of Object.values(fixtures)) {
    if (base.id === target.id) continue; // Identity is covered separately below.
    const replay = core.compile(core.diff(base, target), { [base.id]: base });
    assert(core.sameGraph(replay, target), `${base.id} -> ${target.id}`);
  }
});

test('compilation refuses missing bases and cyclic delta dependencies', () => {
  assert.throws(() => core.compile({ kind: 'delta', id: 'A', base: 'missing', ops: [] }), /Missing base/);
  const registry = {
    A: { kind: 'delta', id: 'A', base: 'B', ops: [] },
    B: { kind: 'delta', id: 'B', base: 'A', ops: [] },
  };
  assert.throws(() => core.compile(registry.A, registry), /Cyclic delta/);
});

test('graph diff and compilation do not mutate their inputs', () => {
  const a = core.clone(fixtures.O16), b = core.clone(fixtures.O18);
  const before = JSON.stringify([a, b]);
  core.compile(core.diff(a, b), { [a.id]: a });
  assert.equal(JSON.stringify([a, b]), before);
});

test('structurally broken references are distinguished from count errors', () => {
  const broken = core.clone(fixtures.O16);
  broken.graph.pairs[0].cell = 'absent';
  assert.equal(core.validate(broken).geometry, null);
  const wrongCount = core.clone(fixtures.O16);
  wrongCount.Z++;
  assert.equal(core.validate(wrongCount).valid, false);
  assert(core.validate(wrongCount).geometry);
});

test('equal inventories do not establish graph identity', () => {
  const a = core.clone(fixtures.O17), b = core.clone(a);
  b.graph.witnesses.at(-1).axis = 'V';
  assert.equal(core.validate(a).valid, true);
  assert.equal(core.validate(b).valid, true);
  assert.equal(core.validate(a).N, core.validate(b).N);
  assert.equal(core.sameGraph(a, b), false);
});

test('graph replay does not promise graph-array ordering', () => {
  const base = core.clone(fixtures.O16), target = core.clone(fixtures.O17);
  target.graph.cells.reverse();
  const replay = core.compile(core.diff(base, target), { [base.id]: base });
  assert(core.sameGraph(replay, target));
  assert.notDeepEqual(plain(replay.graph.cells), plain(target.graph.cells));
});

test('a mutable delta base can change the compiled target without changing the delta', () => {
  const base = core.clone(fixtures.O16), delta = core.diff(base, fixtures.O17);
  const original = core.compile(delta, { [base.id]: base });
  base.graph.pairs[0].history.push('changed-base');
  const changed = core.compile(delta, { [base.id]: base });
  assert.equal(core.sameGraph(original, changed), false);
});

test('identity delta must replay against the supplied snapshot', () => {
  const base = core.clone(fixtures.O16);
  assert(core.sameGraph(base, core.compile(core.diff(base, base), { [base.id]: base })));
});

test('fixture roundtrip must delete base-only metadata', () => {
  const base = core.clone(fixtures.O16), target = core.clone(fixtures.O17);
  base.baseOnlyClaim = 'must not survive';
  assert.deepEqual(plain(core.compile(core.diff(base, target), { [base.id]: base })), plain(target));
});

test('generated cell IDs must distinguish all coordinates allowed by the validator', () => {
  // Evaluate the actual source leaf function without changing the app API.
  const declaration = scripts[0][1].match(/const cellId=[^;]+;/)?.[0];
  assert(declaration);
  const cellId = vm.runInNewContext(`${declaration}\ncellId`);
  assert.notEqual(cellId(12, 1, 10), cellId(12, 11, 0));
  const seen = new Set();
  for (let n = 1; n <= 20; n++) for (let r = 0; r < n; r++) for (let c = 0; c < n; c++) {
    const id = cellId(n, r, c);
    assert(!seen.has(id), `collision at ${n},${r},${c}`);
    seen.add(id);
    if (r < 10 && c < 10) assert.equal(id, `s${n}-${r}${c}`, 'Retain existing fixture IDs');
  }
});

test('same-ID revisions can resolve through a registry delta without hiding true cycles', () => {
  const delta = core.diff(fixtures.O17, fixtures.O16);
  const registry = { O16: delta, O17: fixtures.O17 };
  const root = { kind: 'delta', id: 'O16', base: 'O16', ops: [] };
  assert.deepEqual(plain(core.compile(root, registry)), plain(fixtures.O16));
  assert.throws(() => core.compile(root, { O16: root }), /Cyclic delta/);
  const a = { kind: 'delta', id: 'A', base: 'B', ops: [] };
  assert.throws(() => core.compile(core.clone(a), { A: a, B: { kind: 'delta', id: 'B', base: 'A', ops: [] } }), /Cyclic delta/);
});

test('metadata deletions survive JSON export/replay, preserve target values and leave inputs unchanged', () => {
  const base = core.clone(fixtures.O16), target = core.clone(fixtures.O17);
  Object.assign(base, { obsolete: { claim: true }, notes: 'old', nullable: 1, '': 'remove empty key' });
  Object.assign(target, { nullable: null, provenance: { evidence: ['fixture'], verified: false }, empty: [] });
  delete target.notes;
  const before = JSON.stringify([base, target]);
  const delta = plain(core.diff(base, target));
  assert(delta.ops.some(op => op.op === 'remove-metadata' && op.key === 'obsolete'));
  assert.deepEqual(plain(core.compile(delta, { [base.id]: base })), plain(target));
  assert.equal(JSON.stringify([base, target]), before);
});

test('legacy deltas still inherit metadata; deletion operations cannot remove structural fields', () => {
  const base = core.clone(fixtures.O16);
  base.provenance = { source: 'fixture' };
  const delta = { kind: 'delta', id: 'copy', base: base.id, ops: [] };
  assert.deepEqual(plain(core.compile(delta, { [base.id]: base }).provenance), { source: 'fixture' });
  for (const key of ['id', 'kind', 'graph', 'absent', 42, null]) {
    assert.throws(() => core.compile({ ...delta, ops: [{ op: 'remove-metadata', key }] }, { [base.id]: base }), /metadata/i);
  }
});
