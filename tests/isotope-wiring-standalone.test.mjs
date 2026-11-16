import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import { prepareEmbeddedCore, replaceEmbeddedCore, startMarker, endMarker } from '../scripts/prepare-isotope-wiring-core.mjs';
import { inspectDefinition, compareDefinitions, trialPairPlacement, trialWitnessPlacement, surveyPlacements } from '../examples/isotope-wiring/core/editor-research.mjs';

const html = readFileSync(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8');
const embedded = html.match(/<script id="isotope-research-core">([\s\S]*?)<\/script>/)?.[1];
const editor = html.match(/<script>([\s\S]*?)<\/script>/)?.[1];
assert(embedded && editor);
const context = vm.createContext({});
vm.runInContext(embedded, context, { timeout: 5000 });
vm.runInContext(editor, context, { timeout: 5000 });
const plain = value => JSON.parse(JSON.stringify(value));
const fixtures = plain(context.IsotopeWiring.fixtures());
const runtime = context.IsotopeWiringResearch;

test('embedded runtime matches current maintained core sources without external assets', async () => {
  const nodeEnv = process.env.NODE_ENV;
  await prepareEmbeddedCore({ check: true });
  assert.equal(process.env.NODE_ENV, nodeEnv, 'Freshness checks must not change the subsequent dev-server mode');
  assert.doesNotMatch(html, /<script[^>]+\bsrc\s*=/i);
  assert.doesNotMatch(html, /<link[^>]+\brel=["']stylesheet/i);
  assert.equal([...html.matchAll(/<script>/g)].length, 1, 'Legacy headless adapter retains its single-script entry');
});

test('embedded checks agree with the source core on every supplied fixture', () => {
  for (const doc of Object.values(fixtures)) assert.deepEqual(plain(runtime.inspect(JSON.stringify(doc))), plain(inspectDefinition(doc)), doc.id);
  const broken = plain(fixtures.O16); broken.graph.pairs[0].cell = 'missing';
  assert.deepEqual(plain(runtime.inspect(JSON.stringify(broken))), plain(inspectDefinition(broken)));
});

test('embedded destination surveys agree with maintained source functions', () => {
  for (const [doc, kind, record] of [[fixtures.O16, 'witnesses', 's2-01-H'], [fixtures.V51, 'pairs', 's3-10-upper']]) {
    assert.deepEqual(plain(runtime.surveyPlacements(JSON.stringify(doc), kind, record, 0)),
      plain(surveyPlacements(doc, kind, record)));
  }
});

test('embedded differences and successful/failed trials agree with source functions', () => {
  for (const cell of ['s3-01', 's3-00']) {
    assert.deepEqual(plain(runtime.trialPlacement(JSON.stringify(fixtures.V51), 's3-10-upper', cell)),
      plain(trialPairPlacement(fixtures.V51, 's3-10-upper', cell)));
  }
  for (const cell of ['s2-00', 's2-10']) {
    assert.deepEqual(plain(runtime.trialWitnessPlacement(JSON.stringify(fixtures.O16), 's2-01-H', cell)),
      plain(trialWitnessPlacement(fixtures.O16, 's2-01-H', cell)));
  }
  assert.deepEqual(plain(runtime.compare(JSON.stringify(fixtures.O18), JSON.stringify(fixtures.O16))),
    plain(compareDefinitions(fixtures.O18, fixtures.O16)));
  assert.throws(() => runtime.trialPlacement(JSON.stringify(fixtures.V51), 's3-10-upper', 's4-00'), /same shell/);
});

test('embedding replacement preserves all handwritten HTML and refuses ambiguous markers', () => {
  const original = `prefix\n${startMarker}\nold\n${endMarker}\nsuffix`;
  const replacement = `${startMarker}\nnew\n${endMarker}`;
  assert.equal(replaceEmbeddedCore(original, replacement), `prefix\n${replacement}\nsuffix`);
  for (const bad of ['', `${endMarker}${startMarker}`, `${original}${startMarker}`, `${original}${endMarker}`]) {
    assert.throws(() => replaceEmbeddedCore(bad, replacement), /marker/i);
  }
});
