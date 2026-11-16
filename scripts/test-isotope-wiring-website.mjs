import assert from 'node:assert/strict';
import { createServer } from 'vitepress';
import { expect } from '@playwright/test';
import { launchBrowser, newBrowserPage, disableNetworking } from './isotope-browser.mjs';
import { prepareEmbeddedCore } from './prepare-isotope-wiring-core.mjs';

await prepareEmbeddedCore({ check: true });

const server = await createServer('website', { host: '127.0.0.1', port: 0 });
await server.listen();
const browser = await launchBrowser();
try {
  const page = await newBrowserPage(browser, { viewport: { width: 1280, height: 900 }, colorScheme: 'light' });
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  const base = `http://127.0.0.1:${server.httpServer.address().port}`;
  await page.goto(`${base}/experiments/isotope-wiring`, { waitUntil: 'domcontentloaded', timeout: 90000 });
  const app = page.frameLocator('iframe.isotope-wiring');
  await app.locator('#title').filter({ hasText: 'Oxygen-16' }).waitFor();
  await expect(app.locator('#core-state')).toHaveText('Passed');
  assert(await app.locator('#canvas svg').count() > 0);
  assert.equal(await app.locator('.appbar').evaluate(e => getComputedStyle(e).backgroundColor), 'rgb(255, 255, 255)');
  await app.locator('#counts-toggle').click();
  assert.equal(await app.locator('#core-results details').count(), 7);
  await app.locator('#changes-base').selectOption('O18');
  assert.match(await app.locator('#changes-summary').innerText(), /Oxygen-18 → Oxygen-16.*2 removed/);
  const removed = app.locator('#changes-list details[data-change="removed"]').first();
  await removed.locator('summary').click();
  const destination = await removed.locator('[data-research-cell]').first().getAttribute('data-research-cell');
  await removed.locator('[data-research-cell]').first().click();
  assert.equal(await app.locator('#cell-title').innerText(), destination);
  assert.match(await app.locator('#core-cell').innerText(), /Structural neighborhood/);
  await app.locator('#changes-overlay').check();
  assert.equal(await app.locator('.difference-mark[data-change="removed"]').count(), 2);
  assert.equal(await app.locator('.difference-mark[data-side="after"]').count(), 0);
  await app.locator('#upper').click();
  assert.equal(await app.locator('.difference-mark[data-change="added"]').count(), 2);
  await expect(app.locator('#core-state')).toHaveText('Failed');
  await app.locator('#counts-toggle').click();
  assert(await app.locator('#core-results [data-status="refuted"] [data-research-cell]').count() > 0);
  await app.locator('#counts-close').click();
  await app.locator('#undo').click();
  await expect(app.locator('#core-state')).toHaveText('Passed');
  assert.equal(await app.locator('.difference-mark[data-change="added"]').count(), 0);
  await app.locator('#inspector-close').click();
  const viewBefore = await app.locator('#canvas svg').getAttribute('viewBox');
  await app.locator('#counts-toggle').click();
  await app.locator('#changes-base').selectOption('V51');
  await app.locator('#counts-close').click();
  assert(await app.locator('.difference-mark[data-record="s4"]').count() > 0);
  assert(Number((await app.locator('#canvas svg').getAttribute('viewBox')).split(' ')[3]) > Number(viewBefore.split(' ')[3]));
  await app.locator('#zoom-in').click();
  await app.locator('#zoom-fit').click();
  await app.locator('#file-menu summary').click();
  const svgDownload = page.waitForEvent('download');
  await app.locator('#export-svg').click();
  const svgChunks = [];
  for await (const chunk of await (await svgDownload).createReadStream()) svgChunks.push(chunk);
  const svgExport = Buffer.concat(svgChunks).toString('utf8');
  assert.match(svgExport, /difference-mark change-removed/);
  assert.match(svgExport, /Removed: dashed pink/);
  await app.locator('#changes-overlay').uncheck();
  assert.equal(await app.locator('.difference-mark').count(), 0);
  for (const id of ['H1','H2','He3','He4','Li6','Li7','Be9','B10','B11','C12','C13','N14','N15','O16','O17','O18','F19','Ne20','Na23','Ti48','V51','V51-conflict']) {
    await app.locator('#catalog-toggle').click();
    await app.locator('#isotopes button[data-id="'+id+'"]').click();await app.locator('#catalog-close').click();
    await expect(app.locator('#core-state')).toHaveText(id === 'V51-conflict' ? 'Failed' : 'Passed');
    if (id === 'V51') assert.match(await app.locator('#core-results').textContent(), /Placement choices remain unresolved/);
  }
  await app.locator('#catalog-toggle').click();
  await app.locator('#isotopes button[data-id="O16"]').click();await app.locator('#catalog-close').click();
  await app.locator('#definition-view').click();
  await app.locator('#source').fill('{"unsaved":"theme must not reload the editor"}');
  await page.locator('.VPSwitchAppearance').first().click();
  await app.locator('html.dark').waitFor();
  assert.equal(await app.locator('#source').inputValue(), '{"unsaved":"theme must not reload the editor"}');
  assert.equal(await app.locator('html').evaluate(e => getComputedStyle(e).getPropertyValue('--vp-c-brand-1').trim()),
    await page.evaluate(() => getComputedStyle(document.documentElement).getPropertyValue('--vp-c-brand-1').trim()));
  page.once('dialog', dialog=>dialog.accept());await app.locator('#reload-source').click();
  await app.locator('#diagram-view').click();
  await app.locator('#catalog-toggle').click();
  await app.locator('#catalog-search').fill('Oxygen-18');
  await app.locator('#isotopes button').filter({ hasText: 'Oxygen-18' }).first().click();
  await app.locator('#title').filter({ hasText: 'Oxygen-18' }).waitFor();
  await app.locator('#counts-toggle').click();
  assert.equal(await app.locator('#counts-panel').isVisible(), true);
  await app.locator('#counts-close').click();
  const assertToolbarFits = async () => {
    const clipped = await app.locator('#toolstrip').evaluate(strip => {
      const bounds = strip.getBoundingClientRect();
      return [...strip.querySelectorAll('button,label')].filter(e => {
        const r = e.getBoundingClientRect();
        return r.left < 0 || r.right > document.documentElement.clientWidth + 1 ||
          r.top < bounds.top || r.bottom > bounds.bottom + 1;
      }).map(e => e.id || e.textContent.trim());
    });
    assert.deepEqual(clipped, [], 'Every toolbar control must fit, even when the document hides overflow');
  };
  const compare = async () => {
    await app.locator('#catalog-toggle').click();
    await app.locator('#compare').click();
    await expect(app.locator('.compare-column')).toHaveCount(3);
    assert(await app.locator('#changes-overlay').isDisabled());
    assert.equal(await app.locator('.difference-mark').count(), 0);
  };
  await compare();
  for (const [grid, labels] of [[true, false], [false, true], [true, true], [false, false]]) {
    await app.locator('#grid').setChecked(grid);
    await app.locator('#labels').setChecked(labels);
    for (const column of await app.locator('.compare-column').all()) {
      assert.equal(await column.locator('.grid-cell').count() > 0, grid);
      assert.equal(await column.locator('.cell-number').count() > 0, labels);
    }
  }
  for (const width of [390, 320, 600]) {
    await page.setViewportSize({ width, height: 844 });
    await app.locator('#diagram-view').click();
    await app.locator('#changes-overlay').check();
    assert(await app.locator('.difference-mark').count() > 0);
    assert(await app.locator('#difference-legend').isVisible());
    await assertToolbarFits();
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
    assert(await app.locator('html').evaluate(e => e.scrollWidth <= e.clientWidth));
    // Exercise actual editing buttons, not just their DOM presence.
    await app.locator('#inspect-toggle').click();
    const upper = await app.locator('#upper').getAttribute('aria-pressed');
    await app.locator('#upper').click();
    await app.locator('#undo').click();
    assert.equal(await app.locator('#upper').getAttribute('aria-pressed'), upper);
    await app.locator('#redo').click();
    assert.notEqual(await app.locator('#upper').getAttribute('aria-pressed'), upper);
    await app.locator('#undo').click();
    await app.locator('#inspector-close').click();
    await compare();
    await assertToolbarFits();
    const cards = await app.locator('.compare-column').evaluateAll(elements => elements.map(e => {
      const r = e.getBoundingClientRect(), svg = e.querySelector('svg').getBoundingClientRect();
      return { top: r.top, bottom: r.bottom, svgHeight: svg.height };
    }));
    assert(cards.every(c => c.svgHeight >= 250), 'Mobile comparison diagrams need a readable minimum height');
    assert(cards[1].top >= cards[0].bottom && cards[2].top >= cards[1].bottom, 'Mobile comparison must stack');
    await app.locator('#diagram-panel').hover();
    await page.mouse.wheel(0, 1500);
    await expect.poll(() => app.locator('#diagram-panel').evaluate(e => e.scrollTop)).toBeGreaterThan(0);
    await app.locator('.compare-column').last().scrollIntoViewIfNeeded();
    assert(await app.locator('#diagram-panel').evaluate(e => e.scrollWidth <= e.clientWidth));
    await app.locator('#diagram-view').click();
    assert.equal(await app.locator('#diagram-panel').evaluate(e => e.scrollTop), 0);
  }
  await page.setViewportSize({ width: 1280, height: 900 });
  await compare();
  const desktopCards = await app.locator('.compare-column').evaluateAll(elements => elements.map(e => {
    const r = e.getBoundingClientRect(); return { top: r.top, left: r.left };
  }));
  assert(desktopCards.every(c => c.top === desktopCards[0].top), 'Desktop comparison stays side by side');
  assert(desktopCards[0].left < desktopCards[1].left && desktopCards[1].left < desktopCards[2].left);
  // Exercise replay through the editor, real downloads, and a fresh browser context.
  await app.locator('#definition-view').click();
  const snapshot = JSON.parse(await app.locator('#source').inputValue());
  const applyJSON = async value => {
    await app.locator('#source').fill(JSON.stringify(value));
    await app.locator('#apply').click();
    assert.equal(await app.locator('#source-status.error').count(), 0, await app.locator('#source-status').innerText());
  };
  const downloadJSON = async selector => {
    await app.locator('#file-menu summary').click();
    const pending = page.waitForEvent('download');
    await app.locator(selector).click();
    const download = await pending, chunks = [];
    for await (const chunk of await download.createReadStream()) chunks.push(chunk);
    return JSON.parse(Buffer.concat(chunks).toString('utf8'));
  };
  await applyJSON({ kind: 'delta', id: snapshot.id, base: snapshot.id, ops: [] });
  assert.deepEqual(JSON.parse(await app.locator('#source').inputValue()), snapshot);
  assert.deepEqual(await downloadJSON('#export-json'), snapshot, 'Same-ID application saves an absolute snapshot, not a cyclic draft');
  const fixture = await app.locator('html').evaluate(() => window.IsotopeWiring.fixtures().O16);
  const metadataBase = { ...fixture, id: 'ReviewBase', name: 'Review base', obsolete: { claim: true } };
  const target = { ...fixture, id: 'ReviewTarget', name: 'Review target', provenance: { reviewed: false } };
  delete target.notes;
  await applyJSON(metadataBase);
  await applyJSON(target);
  await app.locator('#format').selectOption('delta');
  await app.locator('#base-search').fill('ReviewBase');
  await app.locator('#base-results button[data-base="ReviewBase"]').click();
  const exportedDelta = await downloadJSON('#export-json');
  assert(exportedDelta.ops.some(op => op.op === 'remove-metadata' && op.key === 'obsolete'));
  await applyJSON(exportedDelta);
  await app.locator('#format').selectOption('absolute');
  assert.deepEqual(JSON.parse(await app.locator('#source').inputValue()), target);
  // Leave the target so project export retains its authored delta rather than the active compiled view.
  await app.locator('#catalog-toggle').click();
  await app.locator('#catalog-search').fill('O16');
  await app.locator('#isotopes button[data-id="O16"]').click();await app.locator('#catalog-close').click();
  const project = await downloadJSON('#export-project');
  assert.equal(project.definitions.ReviewTarget.kind, 'delta');
  assert(project.definitions.ReviewTarget.ops.some(op => op.op === 'remove-metadata'));
  const fresh = await newBrowserPage(browser);
  fresh.on('pageerror', error => errors.push(error.message));
  await fresh.goto(`${base}/experiments/isotope-wiring`, { waitUntil: 'networkidle' });
  const imported = fresh.frameLocator('iframe.isotope-wiring');
  await imported.locator('#title').filter({ hasText: 'Oxygen-16' }).waitFor();
  await imported.locator('#file-input').setInputFiles({ name: 'project.json', mimeType: 'application/json', buffer: Buffer.from(JSON.stringify(project)) });
  await imported.locator('#toast').filter({ hasText: 'Project imported' }).waitFor();
  await imported.locator('#catalog-toggle').click();
  await imported.locator('#catalog-search').fill('ReviewTarget');
  await imported.locator('#isotopes button[data-id="ReviewTarget"]').click();
  await imported.locator('#definition-view').click();
  assert.deepEqual(JSON.parse(await imported.locator('#source').inputValue()), target);
  await fresh.close();
  // A valid delta before replacement may become cyclic in the proposed registry.
  await applyJSON({ ...fixture, id: 'CycleA', name: 'Cycle A' });
  await applyJSON({ kind: 'delta', id: 'CycleB', name: 'Cycle B', base: 'CycleA', ops: [] });
  await app.locator('#source').fill(JSON.stringify({ kind: 'delta', id: 'CycleA', base: 'CycleB', ops: [] }));
  await app.locator('#apply').click();
  assert.match(await app.locator('#source-status').innerText(), /Cyclic delta/);
  assert.equal(await app.locator('#source-status.error').count(), 1);
  page.once('dialog', dialog=>dialog.accept());await app.locator('#reload-source').click();
  assert.equal(JSON.parse(await app.locator('#source').inputValue()).id, 'CycleB');
  await app.locator('#catalog-toggle').click();
  await app.locator('#catalog-search').fill('CycleA');
  await app.locator('#isotopes button[data-id="CycleA"]').click();
  await applyJSON({ kind: 'delta', id: 'CycleB', base: 'CycleB', ops: [] });
  await app.locator('#diagram-view').click();
  await app.locator('#undo').click();
  assert.equal(await app.locator('#canvas svg').count(), 1, 'Undo of a delta replacement restores a compiled snapshot');
  assert.equal(await app.locator('.render-error').count(), 0);
  await app.locator('#redo').click();
  assert.equal(await app.locator('#canvas svg').count(), 1);
  const offline = await newBrowserPage(browser);
  offline.on('pageerror', error => errors.push(error.message));
  await disableNetworking(offline);
  await offline.goto(new URL('../examples/isotope-wiring/index.html', import.meta.url).href);
  await offline.locator('#counts-toggle').click();
  await expect(offline.locator('#core-state')).toHaveText('Passed');
  assert(await offline.locator('#changes-base').isEnabled());
  assert(await offline.locator('#changes-overlay').isEnabled());
  assert.equal(await offline.locator('#canvas svg').count(), 1);
  await offline.close();
  assert.deepEqual(errors, []);
  console.log('PASS: live core checks on all fixtures and edits, inspectable differences/failures, standalone parity, website theme/layout, editing and export/import regressions.');
} finally {
  await browser.close();
  await server.close();
}
