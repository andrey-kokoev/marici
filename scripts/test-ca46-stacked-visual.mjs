import assert from 'node:assert/strict';
import {mkdir} from 'node:fs/promises';
import {expect} from '@playwright/test';
import {launchBrowser,newBrowserPage} from './isotope-browser.mjs';
import {prepareIsotopeWiringPublic} from './prepare-isotope-wiring-public.mjs';
await prepareIsotopeWiringPublic();
const dir=process.argv[2]||'temp/ca46-stacked-visual';await mkdir(dir,{recursive:true});
const browser=await launchBrowser();
try{
 const page=await newBrowserPage(browser,{offline:true,viewport:{width:1280,height:950}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(new URL('../examples/isotope-wiring/ca46-stacked-trial.html',import.meta.url).href);
 await expect(page.locator('#scene g[data-cell]')).toHaveCount(10);await expect(page.locator('#scene line[data-edge]')).toHaveCount(60);await expect(page.locator('#scene polygon')).toHaveCount(40);await expect(page.locator('#embedding option')).toHaveCount(16);await expect(page.locator('#contact-marker')).toHaveCount(1);
 await page.screenshot({path:dir+'/oblique.png',fullPage:true});
 const first=await page.locator('#scene').getAttribute('data-mask');await page.locator('#embedding').selectOption('15');assert.notEqual(await page.locator('#scene').getAttribute('data-mask'),first);await expect(page.locator('#selection-status')).toContainText('Embedding 16 / 16');
 await page.locator('#projection').click();await expect(page.locator('#scene')).toHaveAttribute('data-view','projection');
 const contacts=await page.locator('#scene').evaluate(svg=>{const source=svg.querySelector('[data-cell="s1-00"] [data-edge="TB"]'),target=svg.querySelector('[data-cell="s2-01"] [data-edge="TR"]');return [[source.getAttribute('x2'),source.getAttribute('y2')],[target.getAttribute('x1'),target.getAttribute('y1')]];});assert.deepEqual(contacts[0],contacts[1]);
 await page.screenshot({path:dir+'/projection.png',fullPage:true});
 await page.locator('#faces').uncheck();await expect(page.locator('#scene polygon')).toHaveCount(0);await page.locator('#labels').uncheck();await expect(page.locator('#scene .cell-label')).toHaveCount(0);
 await page.locator('#side').click();await expect(page.locator('#side')).toHaveAttribute('aria-pressed','true');await expect(page.locator('#projection')).toHaveAttribute('aria-pressed','false');
 await page.locator('#faces').check();await page.locator('#labels').check();await page.locator('#yaw').fill('-25');await page.locator('#yaw').dispatchEvent('input');await expect(page.locator('#scene')).toHaveAttribute('data-view','oblique');await page.locator('#yaw').fill('25');await page.locator('#yaw').dispatchEvent('input');await page.setViewportSize({width:390,height:844});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await page.screenshot({path:dir+'/mobile.png',fullPage:true});
 await page.goto(new URL('../examples/isotope-wiring/index.html',import.meta.url).href);await expect(page.locator('#ca46-stacked-visual')).toBeHidden();await page.locator('#catalog-toggle').click();await page.locator('#catalog-search').fill('Ca46');await page.locator('#isotopes button[data-id="Ca46"]').click();await page.locator('#catalog-close').click();await expect(page.locator('#ca46-stacked-visual')).toBeVisible();await expect(page.locator('#core-state')).toHaveText('Passed');
 const popupPromise=page.waitForEvent('popup');await page.locator('#ca46-stacked-visual').click();const popup=await popupPromise;await popup.waitForLoadState();await expect(popup.locator('#scene g[data-cell]')).toHaveCount(10);await popup.close();
 await page.goto(new URL('../website/public/experiments/ca46-stacked-trial.html',import.meta.url).href);await expect(page.locator('a').filter({hasText:'Original drawing / editor'})).toHaveAttribute('href','isotope-wiring-standalone.html');await expect(page.locator('#scene g[data-cell]')).toHaveCount(10);
 assert.deepEqual(errors,[]);console.log('Ca46 stacked visual: desktop/mobile controls, actual vertex contact, baseline link, and screenshots passed');
}finally{await browser.close();}
