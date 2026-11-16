import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import { createServer } from 'vitepress';
import { expect } from '@playwright/test';
import { launchBrowser, newBrowserPage, disableNetworking } from './isotope-browser.mjs';
import { prepareEmbeddedCore } from './prepare-isotope-wiring-core.mjs';

await prepareEmbeddedCore({ check: true });
const standalone = process.argv.includes('--standalone');
const screenshots = process.argv.slice(2).find(arg => arg !== '--standalone');
if (screenshots) await mkdir(screenshots, { recursive: true });
const server = standalone ? null : await createServer('website', { host: '127.0.0.1', port: 0 });
if (server) await server.listen();
const browser = await launchBrowser();
try {
  const network = [];
  const newPage = async options => {
    const page = await newBrowserPage(browser, options);
    if (standalone) {
      await disableNetworking(page);
      page.on('request', request => { if (/^https?:/.test(request.url())) network.push(request.url()); });
    }
    return page;
  };
  const page = await newPage({ viewport: { width: 1440, height: 1000 }, colorScheme: 'light' });
  const errors = []; page.on('pageerror', e => errors.push(e.message));
  const url = standalone ? new URL('../examples/isotope-wiring/index.html', import.meta.url).href
    : `http://127.0.0.1:${server.httpServer.address().port}/experiments/isotope-wiring`;
  await page.goto(url, { waitUntil: 'networkidle' });
  const app = standalone ? page : page.frameLocator('iframe.isotope-wiring');
  const select = async (frame, id) => {
    await frame.locator('#catalog-toggle').click(); await frame.locator('#catalog-search').fill(id);
    await frame.locator(`#isotopes button[data-id="${id}"]`).click();await frame.locator('#catalog-close').click();
  };
  const snapshot = async frame => {
    await frame.locator('#definition-view').click(); await frame.locator('#format').selectOption('absolute');
    const value = JSON.parse(await frame.locator('#source').inputValue());
    await frame.locator('#diagram-view').click(); return value;
  };
  const shot = async name => {
    if (!screenshots) return;
    if (standalone) await page.screenshot({ path: `${screenshots}/${name}.png` });
    else {
      const iframe = page.locator('iframe.isotope-wiring');
      await iframe.evaluate(e => window.scrollBy(0, e.getBoundingClientRect().top - 128));
      await iframe.screenshot({ path: `${screenshots}/${name}.png` });
    }
  };
  const openTrial = async () => {
    if (await app.locator('#inspector').isVisible()) await app.locator('#inspector-close').click();
    await app.locator('#canvas .cell-hit[data-cell="s3-10"]').click();
    await app.locator('#trial-open').click();
    await expect(app.locator('#trial-panel')).toBeVisible();
    await expect(app.locator('#toast')).toBeHidden();
    assert.equal(await app.locator('#trial-pair').inputValue(), 's3-10-upper');
  };
  await expect(app.locator('#core-state')).toHaveText('Passed');
  await select(app, 'V51');
  const original = await snapshot(app);
  await expect(app.locator('#placement-banner')).toBeVisible();
  assert.equal(await app.locator('#canvas .placement-question[data-question-cell="s3-10"]').count(), 1);
  await expect(app.locator('#core-state')).toHaveText('Passed');
  await shot('unresolved-original');
  await openTrial();
  await app.locator('#trial-cell').selectOption('s3-00');
  await expect(app.locator('#trial-save')).toBeDisabled();
  assert.match(await app.locator('#trial-issues').innerText(), /cell-capacity/);
  await app.locator('#trial-review').click();await expect(app.locator('#trial-save')).toBeDisabled();
  assert.equal(await app.locator('#trial-preview svg').count(), 2);
  const trialViews = await app.locator('#trial-preview svg').evaluateAll(nodes => nodes.map(n => n.getAttribute('viewBox')));
  assert.equal(trialViews[0], trialViews[1], 'Trial comparison uses a matched shell viewport');
  assert.match(await app.locator('#trial-focus').innerText(), /Showing shell s3/);
  assert.equal(await app.locator('#trial-preview .cell-hit').count(), 0, 'Previews are not dead editing controls');
  await shot('failed-trial');
  await app.locator('#trial-configure').click();await app.locator('#trial-pair').selectOption('s1-00-upper');
  assert.match(await app.locator('#trial-status').innerText(), /No other cell/);
  await expect(app.locator('#trial-save')).toBeDisabled();
  await app.locator('#trial-pair').selectOption('s3-10-upper');
  await app.locator('#trial-cell').selectOption('s3-01');
  await expect(app.locator('#trial-save')).toBeHidden();
  await app.locator('#trial-review').click();
  await expect(app.locator('#trial-save')).toBeEnabled();
  assert.match(await app.locator('#trial-status').innerText(), /placement remains unresolved/);
  assert.equal(await app.locator('#canvas .placement-question[data-question-cell="s3-10"]').count(), 1);
  assert.equal(await app.locator('#trial-preview .placement-question[data-question-cell="s3-01"]').count(), 1);
  await shot('valid-trial-desktop');
  await app.locator('#trial-cancel').click();
  assert.deepEqual(await snapshot(app), original, 'Discard does not mutate the original');

  await openTrial(); await app.locator('#trial-cell').selectOption('s3-01');
  await app.locator('#trial-review').click();await app.locator('#trial-save').click();
  await expect(app.locator('#trial-panel')).toBeHidden();
  const alternative = await snapshot(app);
  assert.equal(alternative.id, 'V51-alt-1');
  assert.equal(alternative.status, 'unresolved');
  assert.equal(alternative.graph.pairs.find(p => p.id === 's3-10-upper').cell, 's3-01');
  assert.equal(alternative.placementAlternative.sourceDefinitionId, 'V51');
  assert.equal(await app.locator('#canvas .placement-question[data-question-cell="s3-01"]').count(), 1);
  assert(await app.locator('#changes-overlay').isChecked());
  await expect(app.locator('#core-state')).toHaveText('Passed');
  await app.locator('#inspector-close').click(); await shot('kept-alternative');
  // Relocation retains the old record ID; adding at its former cell must not reuse it.
  await app.locator('#canvas .cell-hit[data-cell="s3-10"]').click();
  await app.locator('#upper').click();
  const edited = await snapshot(app);
  assert.equal(new Set(edited.graph.pairs.map(p => p.id)).size, edited.graph.pairs.length);
  assert(edited.graph.pairs.some(p => p.cell === 's3-10' && p.id !== 's3-10-upper'));
  assert.equal(edited.graph.pairs.find(p => p.id === 's3-10-upper').cell, 's3-01');
  await app.locator('#undo').click(); assert.deepEqual(await snapshot(app), alternative);
  await select(app, 'V51'); assert.deepEqual(await snapshot(app), original);
  await openTrial(); await app.locator('#trial-cell').selectOption('s3-01');
  await app.locator('#trial-review').click();await app.locator('#trial-save').click();
  assert.equal((await snapshot(app)).id, 'V51-alt-2', 'Never overwrite the existing alternative');

  // Defense in depth: a programmatic source change cannot save a stale modal preview.
  await select(app, 'V51'); await openTrial(); await app.locator('#trial-cell').selectOption('s3-01');
  await app.locator('#upper').evaluate(button=>button.click());
  await expect(app.locator('#trial-save')).toBeDisabled();
  assert.match(await app.locator('#trial-status').innerText(), /working definition changed/);
  await app.locator('#trial-close').click(); await app.locator('#undo').click();
  assert.deepEqual(await snapshot(app), original);

  if (standalone) {
    await app.locator('#file-menu summary').click(); await app.locator('#local-theme').click();
    await expect(app.locator('html')).toHaveClass('dark');
    assert.equal(await app.locator('.appbar').evaluate(e => getComputedStyle(e).backgroundColor), 'rgb(27, 27, 31)');
  } else await page.locator('.VPSwitchAppearance').first().click();
  for (const width of [390, 320]) {
    await page.setViewportSize({ width, height: 844 });
    await openTrial(); await app.locator('#trial-cell').selectOption('s3-01');
    await app.locator('#trial-review').click();
    const cards = await app.locator('#trial-preview>div').evaluateAll(nodes => nodes.map(n => {
      const r = n.getBoundingClientRect(); return { top: r.top, bottom: r.bottom };
    }));
    assert(cards[0].top >= cards[1].bottom, 'Narrow-screen previews stack with the current trial first');
    assert(await app.locator('#trial-panel').evaluate(e => e.scrollWidth <= e.clientWidth));
    await shot(`trial-mobile-${width}-top`);
    await app.locator('#trial-panel').evaluate(panel => { panel.scrollTop = panel.scrollHeight; });
    const previewBottom = await app.locator('#trial-preview>div').last().evaluate(e => e.getBoundingClientRect().bottom);
    const actionsTop = await app.locator('.trial-actions').evaluate(e => e.getBoundingClientRect().top);
    assert(previewBottom <= actionsTop + 1, 'The entire candidate can be viewed above the sticky actions at the end of scrolling');
    await shot(`trial-mobile-${width}-bottom`);
    await app.locator('#trial-close').click();
    assert.deepEqual(await snapshot(app), original);
  }
  await page.setViewportSize({ width: 1440, height: 1000 });
  await openTrial(); await app.locator('#trial-pair').press('Escape');
  await expect(app.locator('#trial-panel')).toBeHidden();
  await expect(app.locator('#trial-open')).toBeFocused();

  await app.locator('#file-menu summary').click();
  const pending = page.waitForEvent('download'); await app.locator('#export-project').click();
  const chunks = []; for await (const chunk of await (await pending).createReadStream()) chunks.push(chunk);
  const project = Buffer.concat(chunks);
  const fresh = await newPage(); fresh.on('pageerror', e => errors.push(e.message));
  await fresh.goto(url, { waitUntil: 'networkidle' }); const imported = standalone ? fresh : fresh.frameLocator('iframe.isotope-wiring');
  await expect(imported.locator('#core-state')).toHaveText('Passed');
  await imported.locator('#file-input').setInputFiles({ name: 'placements.json', mimeType: 'application/json', buffer: project });
  await imported.locator('#toast').filter({ hasText: 'Project imported' }).waitFor();
  await select(imported, 'V51-alt-1'); assert.deepEqual(await snapshot(imported), alternative);
  assert.equal(await imported.locator('#canvas .placement-question[data-question-cell="s3-01"]').count(), 1);
  await select(imported, 'V51'); assert.deepEqual(await snapshot(imported), original);
  await fresh.close();
  const offline = await newPage(); offline.on('pageerror', e => errors.push(e.message));
  await disableNetworking(offline);
  await offline.goto(new URL('../examples/isotope-wiring/index.html', import.meta.url).href);
  await expect(offline.locator('#core-state')).toHaveText('Passed');
  await select(offline, 'V51');
  await expect(offline.locator('#canvas .placement-question[data-question-cell="s3-10"]')).toHaveCount(1);
  await expect(offline.locator('#placement-banner')).toBeVisible();
  await offline.locator('#canvas .cell-hit[data-cell="s3-10"]').focus();
  await offline.locator('#canvas .cell-hit[data-cell="s3-10"]').press('Enter');
  await expect(offline.locator('#core-state')).toHaveText('Passed');
  await expect(offline.locator('#trial-open')).toBeEnabled();
  await offline.close();
  assert.deepEqual(errors, []);
  if (standalone) assert.deepEqual(network, [], 'Standalone workflows must not request network resources');
  console.log(`PASS (${standalone ? 'standalone, network disabled' : 'hosted'}): explicit uncertainty, failed/valid trials, save/discard isolation, unique alternatives, stale-preview rejection, mobile/keyboard behavior and project replay.`);
} finally { await browser.close(); if (server) await server.close(); }
