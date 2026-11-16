import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import { expect } from '@playwright/test';
import { launchBrowser, newBrowserPage } from './isotope-browser.mjs';
import { createServer } from 'vitepress';
import { prepareEmbeddedCore } from './prepare-isotope-wiring-core.mjs';

await prepareEmbeddedCore({ check: true });
const hosted = process.argv.includes('--hosted');
const screenshots = process.argv.slice(2).find(arg => arg !== '--hosted');
if (screenshots) await mkdir(screenshots, { recursive: true });
const server = hosted ? await createServer('website', { host: '127.0.0.1', port: 0 }) : null;
if (server) await server.listen();
const browser = await launchBrowser();
try {
  const errors = [], network = [];
  const newPage = async () => {
    const page = await newBrowserPage(browser, { offline: !hosted, viewport: { width: 1440, height: 1000 } });
    page.on('pageerror', e => errors.push(e.message));
    if (!hosted) page.on('request', r => { if (/^https?:/.test(r.url())) network.push(r.url()); });
    return page;
  };
  const url = hosted ? `http://127.0.0.1:${server.httpServer.address().port}/experiments/isotope-wiring`
    : new URL('../examples/isotope-wiring/index.html', import.meta.url).href;
  const frame = page => hosted ? page.frameLocator('iframe.isotope-wiring') : page;
  const page = await newPage(); await page.goto(url); const app = frame(page);
  await expect(app.locator('#core-state')).toHaveText('Passed');
  const select = async (app, id) => {
    await app.locator('#catalog-toggle').click(); await app.locator('#catalog-search').fill(id);
    await app.locator(`#isotopes button[data-id="${id}"]`).click();await app.locator('#catalog-close').click();
  };
  const snapshot = async app => {
    await app.locator('#definition-view').click(); await app.locator('#format').selectOption('absolute');
    const value = JSON.parse(await app.locator('#source').inputValue());
    await app.locator('#diagram-view').click(); return value;
  };
  const open = async () => {
    if (await app.locator('#inspector').isVisible()) await app.locator('#inspector-close').click();
    await app.locator('#canvas .cell-hit[data-cell="s2-01"]').click();
    await app.locator('#trial-open').click(); await app.locator('#trial-kind').selectOption('witnesses');
    await app.locator('#trial-pair').selectOption('s2-01-H');
  };
  await select(app, 'Ti48'); await open();
  assert.equal(await app.locator('#trial-pair option').evaluateAll(options => options.some(o => o.value.includes('boundary'))), false);
  await app.locator('#trial-cancel').click(); await select(app, 'O16');
  const original = await snapshot(app); await open();
  await app.locator('#trial-cell').selectOption('s2-10');
  await expect(app.locator('#trial-save')).toBeDisabled();
  assert.match(await app.locator('#trial-issues').innerText(), /duplicate-witness-slot/);
  await app.locator('#trial-cell').selectOption('s2-00'); await app.locator('#trial-review').click();await expect(app.locator('#trial-save')).toBeEnabled();
  assert.equal(await app.locator('#trial-preview .placement-question[data-question-cell="s2-00"]').count(), 1);
  assert(await app.locator('#trial-preview .difference-mark[data-collection="witnesses"]').count() >= 2);
  for (const width of [1440, 320]) {
    await page.setViewportSize({ width, height: 1000 });
    assert(await app.locator('#trial-panel').evaluate(e => e.scrollWidth <= e.clientWidth));
    await app.locator('#trial-panel').evaluate(e => { e.scrollTop = e.scrollHeight; });
    if (screenshots) await (hosted ? page.locator('iframe.isotope-wiring') : page).screenshot({ path: `${screenshots}/${hosted ? 'hosted' : 'offline'}-witness-${width}.png` });
  }
  await page.setViewportSize({ width: 1440, height: 1000 });
  await app.locator('#trial-cancel').click(); assert.deepEqual(await snapshot(app), original);
  await open(); await app.locator('#trial-cell').selectOption('s2-00'); await app.locator('#trial-review').click();await app.locator('#trial-save').click();
  const alternative = await snapshot(app);
  assert.equal(alternative.id, 'O16-alt-1'); assert.equal(alternative.status, 'unresolved');
  assert.equal(alternative.placementAlternative.witnessId, 's2-01-H');
  assert.equal(alternative.graph.witnesses.find(w => w.id === 's2-01-H').cell, 's2-00');
  await expect(app.locator('#core-state')).toHaveText('Passed');
  await app.locator('#inspector-close').click(); await app.locator('#canvas .cell-hit[data-cell="s2-01"]').click();
  await app.locator('#horizontal').click();
  const edited = await snapshot(app);
  assert.equal(new Set(edited.graph.witnesses.map(w => w.id)).size, edited.graph.witnesses.length);
  assert(edited.graph.witnesses.some(w => w.cell === 's2-01' && w.axis === 'H' && w.id !== 's2-01-H'));
  await app.locator('#undo').click(); assert.deepEqual(await snapshot(app), alternative);
  await select(app, 'O16'); assert.deepEqual(await snapshot(app), original);
  await open(); await app.locator('#trial-cell').selectOption('s2-00'); await app.locator('#horizontal').evaluate(button=>button.click());
  await expect(app.locator('#trial-save')).toBeDisabled();
  assert.match(await app.locator('#trial-status').innerText(), /working definition changed/);
  await app.locator('#trial-cancel').click(); await app.locator('#undo').click();
  assert.deepEqual(await snapshot(app), original);
  await app.locator('#file-menu summary').click(); const download = page.waitForEvent('download');
  await app.locator('#export-project').click(); const chunks = [];
  for await (const chunk of await (await download).createReadStream()) chunks.push(chunk);
  const fresh = await newPage(); await fresh.goto(url); const imported = frame(fresh);
  await expect(imported.locator('#core-state')).toHaveText('Passed');
  await imported.locator('#file-input').setInputFiles({ name: 'witness-trials.json', mimeType: 'application/json', buffer: Buffer.concat(chunks) });
  await imported.locator('#toast').filter({ hasText: 'Project imported' }).waitFor();
  await select(imported, 'O16-alt-1'); assert.deepEqual(await snapshot(imported), alternative);
  assert.equal(await imported.locator('#canvas .placement-question[data-question-cell="s2-00"]').count(), 1);
  await select(imported, 'O16'); assert.deepEqual(await snapshot(imported), original);
  assert.deepEqual(errors, []); assert.deepEqual(network, []);
  console.log(`PASS (${hosted ? 'hosted' : 'offline'}): witness placement checks, shell-owned exclusion, source isolation, uncertainty, stale rejection, unique edit IDs and fresh-context replay.`);
} finally { await browser.close(); if (server) await server.close(); }
