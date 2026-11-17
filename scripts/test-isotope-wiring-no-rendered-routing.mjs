import assert from 'node:assert/strict';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {expect} from '@playwright/test';
import {launchBrowser, newBrowserPage} from './isotope-browser.mjs';

const source=fileURLToPath(new URL('../examples/isotope-wiring/index.html',import.meta.url));
const browser=await launchBrowser();
try {
 for(const width of [1440,390]){
  const page=await newBrowserPage(browser,{viewport:{width,height:900},offline:true});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(pathToFileURL(source).href);
  await expect(page.locator('#title')).toHaveText('Oxygen-16');
  await expect(page.locator('#canvas svg')).toBeVisible();
  assert.equal(await page.evaluate(()=>typeof globalThis.IsotopeWiring.traceAlternatingEdges),'undefined');
  assert.equal(await page.locator('[id^="route-"],[id^="trace-"],[id^="animation-"]').count(),0);
  assert.equal(await page.locator('#canvas .difference-mark').count(),0);
  await page.locator('#inspect-toggle').click();
  const entry=page.locator('#canvas .cell-hit[tabindex="0"]');
  await expect(entry).toHaveCount(1);
  await expect(entry).toBeVisible();
  const id=await entry.getAttribute('data-cell');
  await entry.focus();await page.keyboard.press('Enter');
  await expect(page.locator('#cell-title')).toHaveText(id);
  assert.equal(await page.locator('#canvas .cell-hit[tabindex="0"]').count(),1);
  assert.deepEqual(errors,[]);
  await page.close();
  console.log(`PASS ${width}px: offline authored drawing, no SVG routing/overlays, one visible keyboard entry and inspect activation`);
 }
} finally {await browser.close();}
