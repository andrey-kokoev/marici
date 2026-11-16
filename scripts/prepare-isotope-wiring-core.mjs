import assert from 'node:assert/strict';
import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { resolve } from 'node:path';
import { build } from 'vite';

const root = fileURLToPath(new URL('../', import.meta.url));
const htmlPath = new URL('../examples/isotope-wiring/index.html', import.meta.url);
export const startMarker = '<!-- isotope-research-core:start -->';
export const endMarker = '<!-- isotope-research-core:end -->';

export async function embeddedCore() {
  // Vite defaults NODE_ENV to production during builds. Do not poison a later
  // dev server (notably VitePress) in the same process when checking freshness.
  const nodeEnv = process.env.NODE_ENV;
  let result;
  try { result = await build({
    configFile: false, root, logLevel: 'silent',
    build: {
      write: false, minify: true, target: 'es2022', sourcemap: false,
      lib: { entry: resolve(root, 'examples/isotope-wiring/core/browser-entry.mjs'), name: 'IsotopeResearchCore', formats: ['iife'] },
    },
  }); } finally {
    if (nodeEnv === undefined) delete process.env.NODE_ENV;
    else process.env.NODE_ENV = nodeEnv;
  }
  const outputs = (Array.isArray(result) ? result : [result]).flatMap(r => r.output);
  assert.equal(outputs.length, 1, 'The standalone core must not require sidecar assets');
  const [chunk] = outputs;
  assert.equal(chunk.type, 'chunk');
  assert.deepEqual(chunk.imports, []); assert.deepEqual(chunk.dynamicImports, []);
  const code = chunk.code.trim().replace(/<\/script/gi, '<\\/script');
  return `${startMarker}\n<script id="isotope-research-core">\n// Generated from core/browser-entry.mjs by scripts/prepare-isotope-wiring-core.mjs.\n${code}\n</script>\n${endMarker}`;
}

export function replaceEmbeddedCore(html, section) {
  const start = html.indexOf(startMarker), end = html.indexOf(endMarker);
  assert(start >= 0 && end > start, 'Missing or reversed inline-core markers');
  assert.equal(html.indexOf(startMarker, start + 1), -1, 'Duplicate inline-core start marker');
  assert.equal(html.indexOf(endMarker, end + 1), -1, 'Duplicate inline-core end marker');
  return html.slice(0, start) + section + html.slice(end + endMarker.length);
}

export async function prepareEmbeddedCore({ check = false } = {}) {
  const section = await embeddedCore();
  // Read after compilation so unrelated edits outside the generated region are retained.
  const html = await readFile(htmlPath, 'utf8'), updated = replaceEmbeddedCore(html, section);
  if (check) assert.equal(updated === html, true, 'Embedded core is stale: run node scripts/prepare-isotope-wiring-core.mjs');
  else if (updated !== html) await writeFile(htmlPath, updated);
  return { changed: updated !== html, bytes: Buffer.byteLength(section) };
}

if (process.argv[1] && pathToFileURL(resolve(process.argv[1])).href === import.meta.url) {
  const flags = process.argv.slice(2);
  assert(flags.every(flag => flag === '--check'), 'Only --check is supported');
  const result = await prepareEmbeddedCore({ check: flags.includes('--check') });
  console.log(`${flags.includes('--check') ? 'PASS: embedded core is current' : result.changed ? 'Updated embedded core' : 'Embedded core unchanged'} (${result.bytes} bytes; no external assets).`);
}
