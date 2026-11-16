import assert from 'node:assert/strict';
import { readFile, mkdir } from 'node:fs/promises';
import { expect } from '@playwright/test';
import { launchBrowser, newBrowserPage, disableNetworking } from './isotope-browser.mjs';
import { prepareEmbeddedCore, replaceEmbeddedCore, startMarker, endMarker } from './prepare-isotope-wiring-core.mjs';

await prepareEmbeddedCore({ check: true });
const screenshots = process.argv[2];
if (screenshots) await mkdir(screenshots, { recursive: true });
const browser = await launchBrowser();
try {
  const page = await newBrowserPage(browser, { offline: true, colorScheme: 'light', viewport: { width: 1280, height: 900 } });
  const errors = [], network = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('request', request => { if (/^https?:/.test(request.url())) network.push(request.url()); });
  await page.goto(new URL('../examples/isotope-wiring/index.html', import.meta.url).href);
  await expect(page.locator('#core-state')).toHaveText('Passed');
  const select = async id => {
    await page.locator('#catalog-toggle').click(); await page.locator('#catalog-search').fill(id);
    await page.locator(`#isotopes button[data-id="${id}"]`).click();await page.locator('#catalog-close').click();
  };
  for (const id of ['H1','H2','He3','He4','Li6','Li7','Be9','B10','B11','C12','C13','N14','N15','O16','O17','O18','F19','Ne20','Na23','Ti48','V51','V51-conflict']) {
    await select(id);
    await expect(page.locator('#core-state')).toHaveText(id === 'V51-conflict' ? 'Failed' : 'Passed');
  }
  await select('O16');
  await page.locator('#definition-view').click();
  const original = await page.locator('#source').inputValue();
  await page.locator('#source').fill('{"unsaved":"theme switches must preserve this"}');
  await page.emulateMedia({ colorScheme: 'dark' });
  await expect(page.locator('html')).toHaveClass('dark');
  assert.equal(await page.locator('.appbar').evaluate(e => getComputedStyle(e).backgroundColor), 'rgb(27, 27, 31)');
  assert.equal(await page.locator('#source').inputValue(), '{"unsaved":"theme switches must preserve this"}');
  await page.locator('#file-menu summary').click(); await page.locator('#local-theme').click();
  await expect(page.locator('html')).not.toHaveClass('dark');
  assert.equal(await page.locator('#source').inputValue(), '{"unsaved":"theme switches must preserve this"}');
  page.once('dialog', dialog=>dialog.accept());await page.locator('#reload-source').click();
  assert.equal(await page.locator('#source').inputValue(), original);
  await page.reload();
  await expect(page.locator('#core-state')).toHaveText('Passed');
  assert(await page.evaluate(() => matchMedia('(prefers-color-scheme: dark)').matches));
  await expect(page.locator('html')).not.toHaveClass('dark'); // Manual choice persists despite dark system preference.

  await page.locator('#counts-toggle').click(); await page.locator('#changes-base').selectOption('O18');
  await page.locator('#counts-close').click(); await page.locator('#changes-overlay').check();
  assert.equal(await page.locator('.difference-mark[data-change="removed"]').count(), 2);
  await page.locator('#canvas .cell-hit[data-cell="s2-00"]').focus();
  await page.locator('#canvas .cell-hit[data-cell="s2-00"]').press('Enter');
  await page.locator('#upper').click(); await expect(page.locator('#core-state')).toHaveText('Failed');
  await page.locator('#undo').click(); await expect(page.locator('#core-state')).toHaveText('Passed');
  await page.locator('#redo').click(); await expect(page.locator('#core-state')).toHaveText('Failed');
  await page.locator('#undo').click(); await page.locator('#inspector-close').click();
  await page.locator('#file-menu summary').click();
  const pending = page.waitForEvent('download'); await page.locator('#export-svg').click();
  const chunks = []; for await (const chunk of await (await pending).createReadStream()) chunks.push(chunk);
  assert.match(Buffer.concat(chunks).toString('utf8'), /difference-mark change-removed/);
  await page.locator('#file-menu summary').click(); await page.locator('#local-theme').click();
  await expect(page.locator('html')).toHaveClass('dark');
  if (screenshots) await page.screenshot({ path: `${screenshots}/standalone-dark.png` });
  await page.setViewportSize({ width: 320, height: 844 });
  const clipped = await page.locator('#toolstrip').evaluate(strip => [...strip.querySelectorAll('button,label')].filter(e => {
    const r = e.getBoundingClientRect(); return r.left < 0 || r.right > innerWidth + 1;
  }).map(e => e.id || e.textContent));
  assert.deepEqual(clipped, []);
  if (screenshots) await page.screenshot({ path: `${screenshots}/standalone-mobile.png` });
  assert.deepEqual(network, [], 'No external requests, including failed requests, during file-mode use');

  // Incomplete copies must not silently present structural validation as successful.
  const broken = await newBrowserPage(browser); broken.on('pageerror', e => errors.push(e.message));
  await disableNetworking(broken);
  const html = await readFile(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8');
  await broken.setContent(replaceEmbeddedCore(html, `${startMarker}\n<!-- deliberately omitted -->\n${endMarker}`));
  await expect(broken.locator('#core-state')).toContainText('Structural core unavailable; checks were not run');
  await expect(broken.locator('#changes-overlay')).toBeDisabled();
  await broken.locator('#inspect-toggle').click(); await expect(broken.locator('#trial-open')).toBeDisabled();
  assert.equal(await broken.locator('#canvas svg').count(), 1, 'Legacy rendering remains available without claiming core checks');
  await broken.close();
  assert.deepEqual(errors, []);
  console.log('PASS: file-mode core checks, live edits/undo/redo, differences and SVG export, system/manual theme persistence, mobile width, zero network requests and explicit missing-core failure.');
} finally { await browser.close(); }
