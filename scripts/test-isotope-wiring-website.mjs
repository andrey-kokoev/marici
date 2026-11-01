import assert from 'node:assert/strict';
import { createServer } from 'vitepress';
import { chromium } from '@playwright/test';

const server = await createServer('website', { host: '127.0.0.1', port: 0 });
await server.listen();
const browser = await chromium.launch();
try {
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 }, colorScheme: 'light' });
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  const base = `http://127.0.0.1:${server.httpServer.address().port}`;
  await page.goto(`${base}/experiments/isotope-wiring`, { waitUntil: 'domcontentloaded', timeout: 90000 });
  const app = page.frameLocator('iframe.isotope-wiring');
  await app.locator('#title').filter({ hasText: 'Oxygen-16' }).waitFor();
  assert(await app.locator('#canvas svg').count() > 0);
  assert.equal(await app.locator('.appbar').evaluate(e => getComputedStyle(e).backgroundColor), 'rgb(255, 255, 255)');
  await app.locator('#definition-view').click();
  await app.locator('#source').fill('{"unsaved":"theme must not reload the editor"}');
  await page.locator('.VPSwitchAppearance').first().click();
  await app.locator('html.dark').waitFor();
  assert.equal(await app.locator('#source').inputValue(), '{"unsaved":"theme must not reload the editor"}');
  assert.equal(await app.locator('html').evaluate(e => getComputedStyle(e).getPropertyValue('--vp-c-brand-1').trim()),
    await page.evaluate(() => getComputedStyle(document.documentElement).getPropertyValue('--vp-c-brand-1').trim()));
  await app.locator('#reload-source').click();
  await app.locator('#diagram-view').click();
  await app.locator('#catalog-toggle').click();
  await app.locator('#catalog-search').fill('Oxygen-18');
  await app.locator('#isotopes button').filter({ hasText: 'Oxygen-18' }).first().click();
  await app.locator('#title').filter({ hasText: 'Oxygen-18' }).waitFor();
  await app.locator('#counts-toggle').click();
  assert.equal(await app.locator('#counts-panel').isVisible(), true);
  await page.setViewportSize({ width: 390, height: 844 });
  assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
  assert(await app.locator('html').evaluate(e => e.scrollWidth <= e.clientWidth));
  assert.deepEqual(errors, []);
  console.log('PASS: website route, rendering, theme synchronization without editor reset, isotope selection, counts and mobile width.');
} finally {
  await browser.close();
  await server.close();
}
