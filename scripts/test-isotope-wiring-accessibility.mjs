import assert from 'node:assert/strict';
import { mkdir } from 'node:fs/promises';
import { expect } from '@playwright/test';
import { launchBrowser, newBrowserPage } from './isotope-browser.mjs';
import { prepareEmbeddedCore } from './prepare-isotope-wiring-core.mjs';

await prepareEmbeddedCore({ check: true });
const engine = process.argv[2] || process.env.ISOTOPE_BROWSER || 'chromium', screenshots = process.argv[3];
assert(['chromium','firefox','webkit'].includes(engine));
if (screenshots) await mkdir(screenshots, { recursive: true });
const browser = await launchBrowser(engine);
const url = new URL('../examples/isotope-wiring/index.html', import.meta.url).href;
const errors = [];
try {
  const page = await newBrowserPage(browser, { offline: true });
  page.on('pageerror', e => errors.push(e.message));
  await page.goto(url); await expect(page.locator('#core-state')).toHaveText('Passed');
  assert.equal(await page.locator('#canvas .cell-hit[tabindex="0"]').count(), 1);
  const current = page.locator('#canvas .cell-hit[tabindex="0"]');
  await current.focus(); await page.keyboard.press('Home');
  await expect(page.locator('#canvas .cell-hit').first()).toBeFocused();
  await page.keyboard.press('ArrowRight');
  await expect(page.locator('#canvas .cell-hit').nth(1)).toBeFocused();
  await page.keyboard.press('End');
  await expect(page.locator('#canvas .cell-hit').last()).toBeFocused();
  await page.keyboard.press('ArrowLeft');
  const selected = await current.getAttribute('data-cell');
  await page.keyboard.press('+'); await expect(current).toBeFocused();
  await page.keyboard.press('0'); await expect(current).toBeFocused();
  await expect(page.locator('#canvas svg')).toHaveAttribute('role', 'group');
  await page.keyboard.press('Enter'); await expect(page.locator('#inspector-close')).toBeFocused();
  await page.keyboard.press('Escape');
  await expect(page.locator(`#canvas .cell-hit[data-cell="${selected}"]`)).toBeFocused();
  await page.keyboard.press('Space'); await expect(page.locator('#inspector-close')).toBeFocused();
  await page.locator('#inspector-close').press('Enter'); await expect(current).toBeFocused();
  await page.keyboard.press('/'); await expect(page.locator('#catalog-search')).toBeFocused();
  await page.keyboard.press('Escape'); await expect(page.locator('#catalog-toggle')).toBeFocused();
  await page.locator('#counts-toggle').press('Enter'); await expect(page.locator('#counts-close')).toBeFocused();
  await page.keyboard.press('Escape'); await expect(page.locator('#counts-toggle')).toBeFocused();
  await page.locator('#file-menu summary').press('Enter'); await page.keyboard.press('Escape');
  await expect(page.locator('#file-menu summary')).toBeFocused();
  await page.locator('#move-tool').click();
  const beforePan = await page.locator('#canvas svg').getAttribute('viewBox');
  const surface = await page.locator('#diagram-panel').boundingBox();
  const x = surface.x + surface.width * .4, y = surface.y + surface.height * .4;
  await page.mouse.move(x, y); await page.mouse.down(); await page.mouse.move(x + 40, y + 30, { steps: 4 }); await page.mouse.up();
  assert.notEqual(await page.locator('#canvas svg').getAttribute('viewBox'), beforePan);
  await expect(page.locator('#diagram-panel')).toHaveAttribute('data-dragging', 'false');
  await page.locator('#move-tool').click(); await page.locator('#zoom-fit').click();
  await page.locator('#canvas .cell-hit[data-cell="s2-00"]').click(); await expect(page.locator('#inspector')).toBeVisible();
  await page.locator('#inspector-close').click();
  await page.locator('#catalog-toggle').click();
  const immediateResults = await page.locator('#catalog-search').evaluate(input => {
    input.value = 'O16'; input.dispatchEvent(new Event('input', { bubbles: true }));
    return [...document.querySelectorAll('#isotopes button[data-id]')].map(b => b.dataset.id);
  });
  assert.deepEqual(immediateResults, ['O16'], 'Local search must not leave a pending redraw that can detach a clicked result');
  await page.locator('#isotopes button[data-id="O16"]').click(); await expect(page.locator('#catalog')).toBeVisible();
  await page.locator('#catalog-close').click();await expect(page.locator('#catalog-toggle')).toBeFocused();
  await page.locator('#catalog-toggle').click(); await page.locator('#compare').click();
  assert.equal(await page.locator('#canvas .cell-hit').count(), 0, 'Read-only comparison has no dead focus targets');
  await page.close();

  // Touch emulation exercises real browser touch/pointer dispatch, not synthetic DOM events.
  const touch = await newBrowserPage(browser, { offline: true, hasTouch: true, isMobile: engine !== 'firefox', viewport: { width: 320, height: 844 } });
  touch.on('pageerror', e => errors.push(e.message));
  await touch.goto(url); await expect(touch.locator('#core-state')).toHaveText('Passed');
  assert(await touch.evaluate(() => matchMedia('(pointer: coarse)').matches));
  for (const selector of ['#zoom-in','#zoom-out','#move-tool','#inspect-toggle','#catalog-toggle','#file-menu summary']) {
    const r = await touch.locator(selector).boundingBox();
    assert(r.width >= 44 && r.height >= 44, `${selector} has a 44px touch target`);
    assert(r.x >= 0 && r.x + r.width <= 321, `${selector} fits narrow viewport`);
  }
  await touch.locator('#canvas .cell-hit[data-cell="s2-00"]').tap();
  await expect(touch.locator('#inspector')).toBeVisible();
  await touch.locator('#upper').tap(); await expect(touch.locator('#core-state')).toHaveText('Failed');
  await touch.locator('#inspector-close').tap(); await touch.locator('#undo').tap();
  await expect(touch.locator('#core-state')).toHaveText('Passed');
  if (engine === 'chromium') {
    await touch.locator('#move-tool').tap();
    const before = await touch.locator('#canvas svg').getAttribute('viewBox');
    const cdp = await touch.context().newCDPSession(touch);
    await cdp.send('Input.synthesizeScrollGesture', { x: 140, y: 400, xDistance: 40, yDistance: 40, gestureSourceType: 'touch', preventFling: true });
    assert.notEqual(await touch.locator('#canvas svg').getAttribute('viewBox'), before);
    await expect(touch.locator('#diagram-panel')).toHaveAttribute('data-dragging', 'false');
    await cdp.detach();
    await touch.locator('#move-tool').tap();
    await expect(touch.locator('#move-tool')).toHaveAttribute('aria-pressed', 'false');
    await touch.locator('#zoom-fit').tap();
    await touch.locator('#canvas .cell-hit[data-cell="s2-00"]').tap();
    await expect(touch.locator('#inspector')).toBeVisible();
    await touch.locator('#inspector-close').tap();
  }
  if (screenshots) await touch.screenshot({ path: `${screenshots}/${engine}-touch-320.png` });
  assert.deepEqual(errors, []);
  console.log(`PASS (${engine}): keyboard cell navigation, inspection focus return, panel dismissal, mouse panning, noninteractive comparison, coarse-pointer targets and touch editing${engine === 'chromium' ? '/panning' : ''}.`);
} finally { await browser.close(); }
