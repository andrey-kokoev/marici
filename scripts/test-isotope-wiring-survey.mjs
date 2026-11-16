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
  const page = await newBrowserPage(browser, { offline: !hosted, viewport: { width: 1440, height: 1000 } });
  const errors = [], network = [];
  page.on('pageerror', e => errors.push(e.message));
  if (!hosted) page.on('request', r => { if (/^https?:/.test(r.url())) network.push(r.url()); });
  await page.goto(hosted ? `http://127.0.0.1:${server.httpServer.address().port}/experiments/isotope-wiring`
    : new URL('../examples/isotope-wiring/index.html', import.meta.url).href);
  const app = hosted ? page.frameLocator('iframe.isotope-wiring') : page;
  await expect(app.locator('#core-state')).toHaveText('Passed');
  const snapshot = async () => {
    await app.locator('#definition-view').click(); await app.locator('#format').selectOption('absolute');
    const doc = JSON.parse(await app.locator('#source').inputValue()); await app.locator('#diagram-view').click(); return doc;
  };
  const open = async () => {
    if (await app.locator('#inspector').isVisible()) await app.locator('#inspector-close').click();
    await app.locator('#canvas .cell-hit[data-cell="s2-01"]').click(); await app.locator('#trial-open').click();
    await app.locator('#trial-kind').selectOption('witnesses'); await app.locator('#trial-pair').selectOption('s2-01-H');
    await app.locator('#trial-survey summary').click();
  };
  const original = await snapshot(); await open();
  await app.locator('#survey-run').click(); await expect(app.locator('#survey-run')).toBeDisabled();
  assert.equal(await app.locator('[data-survey-cell]').count(), 3);
  assert.match(await app.locator('#survey-status').innerText(), /Checked 3 of 3 other cells; 1 pass/);
  assert.match(await app.locator('#survey-status').innerText(), /do not select a unique placement/);
  assert.equal((await app.locator('#survey-results').innerText()).match(/Inventory: Passed/g).length, 3);
  await app.locator('[data-survey-cell="s2-10"]').click();
  await expect(app.locator('#trial-save')).toBeDisabled(); assert.match(await app.locator('#trial-issues').innerText(), /duplicate-witness-slot/);
  await app.locator('#trial-configure').click();await app.locator('[data-survey-cell="s2-00"]').click(); await expect(app.locator('#trial-save')).toBeEnabled();
  await expect(app.locator('#trial-preview')).toBeFocused(); await expect(app.locator('#trial-save')).toHaveText('Keep s2-00 as alternative');
  await app.locator('#trial-configure').click();await app.locator('#trial-pair').selectOption('s2-01-V');
  assert.equal(await app.locator('[data-survey-cell]').count(), 0); await expect(app.locator('#survey-run')).toBeEnabled();
  await app.locator('#trial-kind').selectOption('pairs'); assert.equal(await app.locator('[data-survey-cell]').count(), 0);
  await app.locator('#trial-kind').selectOption('witnesses'); await app.locator('#trial-pair').selectOption('s2-01-H');
  await app.locator('#survey-run').click(); await app.locator('#horizontal').evaluate(button=>button.click());
  await expect(app.locator('#survey-run')).toBeDisabled(); await expect(app.locator('#trial-save')).toBeDisabled();
  assert.match(await app.locator('#survey-status').innerText(), /stale/);
  for (const button of await app.locator('[data-survey-cell]').all()) await expect(button).toBeDisabled();
  await app.locator('#trial-cancel').click(); await app.locator('#undo').click(); assert.deepEqual(await snapshot(), original);

  // A larger supplied shell exercises real UI pagination without inventing extra inventory.
  const wider = structuredClone(original); wider.id = 'O16-survey'; wider.name = 'Oxygen survey test';
  wider.graph.shells.find(s => s.id === 's2').size = 4;
  for (let row = 0; row < 4; row++) for (let col = 0; col < 4; col++) {
    if (!wider.graph.cells.some(c => c.shell === 's2' && c.row === row && c.col === col))
      wider.graph.cells.push({ id: `survey-${row}-${col}`, shell: 's2', row, col, history: [] });
  }
  await app.locator('#file-input').setInputFiles({ name: 'wider.json', mimeType: 'application/json', buffer: Buffer.from(JSON.stringify(wider)) });
  await expect(app.locator('#title')).toHaveText(wider.name); await expect(app.locator('#core-state')).toHaveText('Passed');
  const widerBefore = await snapshot(); await open(); await app.locator('#survey-run').click();
  assert.equal(await app.locator('[data-survey-cell]').count(), 8);
  assert.match(await app.locator('#survey-status').innerText(), /Checked 8 of 15/);
  assert.match(await app.locator('#survey-status').innerText(), /Partial survey/);
  await expect(app.locator('#survey-run')).toBeEnabled(); await app.locator('#survey-run').click();
  assert.equal(await app.locator('[data-survey-cell]').count(), 15);
  assert.match(await app.locator('#survey-status').innerText(), /Checked 15 of 15 other cells; 13 pass/);
  await expect(app.locator('#survey-run')).toBeDisabled();
  const ids = await app.locator('[data-survey-cell]').evaluateAll(nodes => nodes.map(n => n.dataset.surveyCell));
  assert.equal(new Set(ids).size, 15);
  for (const width of [1440, 320]) {
    await page.setViewportSize({ width, height: 1000 }); await app.locator('#survey-status').scrollIntoViewIfNeeded();
    assert(await app.locator('#trial-panel').evaluate(e => e.scrollWidth <= e.clientWidth));
    if (screenshots) await (hosted ? page.locator('iframe.isotope-wiring') : page).screenshot({ path: `${screenshots}/${hosted ? 'hosted' : 'offline'}-survey-${width}.png` });
  }
  await app.locator('#trial-cancel').click(); assert.deepEqual(await snapshot(), widerBefore, 'Surveying never saves or mutates the working source');
  assert.deepEqual(errors, []); assert.deepEqual(network, []);
  console.log(`PASS (${hosted ? 'hosted' : 'offline'}): bounded placement survey, inventory vs structural discrimination, result previews, reset/stale rejection, pagination and source isolation.`);
} finally { await browser.close(); if (server) await server.close(); }
