import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { preview } from 'vite';
import { expect } from '@playwright/test';
import { launchBrowser, newBrowserPage } from './isotope-browser.mjs';
import { prepareIsotopeWiringPublic } from './prepare-isotope-wiring-public.mjs';

await prepareIsotopeWiringPublic({ check: true });
const source = await readFile(new URL('../examples/isotope-wiring/index.html', import.meta.url));
const built = await readFile(new URL('../website/.vitepress/dist/experiments/isotope-wiring-standalone.html', import.meta.url));
assert.deepEqual(built, source, 'Built downloadable HTML must be byte-identical to the canonical editor');
const server = await preview({
  configFile: false, root: fileURLToPath(new URL('../website', import.meta.url)), appType: 'mpa',
  build: { outDir: '.vitepress/dist' }, preview: { host: '127.0.0.1', port: 0 },
});
let browser;
try {
  browser = await launchBrowser(); const page = await newBrowserPage(browser);
  const errors = []; page.on('pageerror', e => errors.push(e.message));
  const origin = `http://127.0.0.1:${server.httpServer.address().port}`;
  await page.goto(origin + '/experiments/');
  await page.getByRole('link', { name: 'Isotope wiring editor', exact: true }).last().click();
  await expect(page).toHaveURL(/\/experiments\/isotope-wiring$/);
  const app = page.frameLocator('iframe.isotope-wiring');
  await expect(app.locator('#core-state')).toHaveText('Passed');
  await app.locator('#catalog-toggle').click(); await app.locator('#catalog-search').fill('V51');
  await app.locator('#isotopes button[data-id="V51"]').click();
  await expect(app.locator('#canvas .drawing-unavailable')).toHaveCount(1);
  await expect(app.locator('#canvas .ep,#canvas .cell-hit,#trial-open')).toHaveCount(0);
  await app.locator('#catalog-search').fill('Li6');await app.locator('#isotopes button[data-id="Li6"]').click();await app.locator('#catalog-close').click();
  await app.locator('#inspect-toggle').click();const entry=app.locator('#canvas .cell-hit[tabindex="0"]');await expect(entry).toHaveCount(1);await entry.focus();await page.keyboard.press('Enter');
  await app.locator('#definition-view').click();const retained=await app.locator('#source').inputValue();
  await page.locator('.VPSwitchAppearance').first().click();await expect(app.locator('html.dark')).toHaveCount(1);
  assert.equal(await app.locator('#source').inputValue(),retained,'Host theme synchronization must not reload the editor');
  await app.locator('#diagram-view').click();await expect(app.locator('#canvas .difference-mark')).toHaveCount(0);

  const pending = page.waitForEvent('download'); await page.locator('#wiring-download').click();
  const download = await pending; assert.equal(download.suggestedFilename(), 'isotope-wiring.html');
  const chunks = []; for await (const chunk of await download.createReadStream()) chunks.push(chunk);
  assert.deepEqual(Buffer.concat(chunks), source);
  await expect(page).toHaveURL(/\/experiments\/isotope-wiring$/);
  const popupEvent = page.waitForEvent('popup'); await page.locator('#wiring-full-window').click();
  const popup = await popupEvent; popup.on('pageerror', e => errors.push(e.message));
  await expect(popup.locator('#core-state')).toHaveText('Passed');
  await expect(popup).toHaveURL(/\/experiments\/isotope-wiring-standalone.html$/);
  assert.equal(await popup.evaluate(() => typeof IsotopeWiringResearch.surveyPlacements), 'function');
  await popup.close();
  await page.getByRole('link', { name: 'Validation and export limits', exact: true }).click();
  await expect(page.getByRole('heading', { level: 1 })).toHaveText('Isotope wiring: validation and export limits');
  assert.deepEqual(errors, []);
  console.log('PASS: production navigation, current embedded core/readonly controls, keyboard entry, theme retention, full-window editor, exact standalone download and limitations route.');
} finally {
  if (browser) await browser.close();
  await new Promise((resolve, reject) => server.httpServer.close(error => error ? reject(error) : resolve()));
}
