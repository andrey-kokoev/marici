import assert from 'node:assert/strict';
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { resolve } from 'node:path';
import { prepareEmbeddedCore } from './prepare-isotope-wiring-core.mjs';
import { prepareEmbeddedReference } from './prepare-isotope-wiring-reference.mjs';
import { prepareEmbeddedTurtle } from './prepare-isotope-wiring-turtle.mjs';
import { prepareCa46StackedVisual } from './build-ca46-stacked-visual.mjs';

const source = new URL('../examples/isotope-wiring/index.html', import.meta.url);
const destination = new URL('../website/public/experiments/isotope-wiring-standalone.html', import.meta.url);

export async function prepareIsotopeWiringPublic({ check = false } = {}) {
  // Never publish a stale embedded core or maintain a second handwritten editor.
  await prepareEmbeddedCore({ check: true });
  await prepareEmbeddedReference({ check: true });
  await prepareEmbeddedTurtle({ check: true });
  const html = await readFile(source, 'utf8');
  const current = await readFile(destination, 'utf8').catch(error => {
    if (error.code === 'ENOENT') return null;
    throw error;
  });
  if (check) assert.equal(current === html, true, 'Public standalone editor is stale or missing');
  else if (current !== html) {
    await mkdir(new URL('./', destination), { recursive: true });
    await writeFile(destination, html);
  }
  // Regenerate the exclusively generated source before copying it. A clean
  // checkout must not depend on an untracked HTML file from a prior session.
  const preparedVisual = prepareCa46StackedVisual({ check });
  const visualDestination = new URL('../website/public/experiments/ca46-stacked-trial.html', import.meta.url);
  const visual = preparedVisual.html;
  const currentVisual = await readFile(visualDestination, 'utf8').catch(error => {
    if (error.code === 'ENOENT') return null;
    throw error;
  });
  if (check) assert.equal(currentVisual === visual, true, 'Public Ca46 stacked visual is stale or missing');
  else if (currentVisual !== visual) {
    await mkdir(new URL('./', visualDestination), { recursive: true });
    await writeFile(visualDestination, visual);
  }
  return { path: fileURLToPath(destination), bytes: Buffer.byteLength(html), changed: current !== html };
}

if (process.argv[1] && pathToFileURL(resolve(process.argv[1])).href === import.meta.url) {
  assert(process.argv.slice(2).every(arg => arg === '--check'), 'Only --check is supported');
  console.log(await prepareIsotopeWiringPublic({ check: process.argv.includes('--check') }));
}
