import assert from 'node:assert/strict';
import {mkdir,readFile} from 'node:fs/promises';
import {expect} from '@playwright/test';
import {launchBrowser,newBrowserPage} from './isotope-browser.mjs';
const screenshots=process.argv[2];if(screenshots)await mkdir(screenshots,{recursive:true});
const browser=await launchBrowser();
try{
 const page=await newBrowserPage(browser,{offline:true,viewport:{width:1280,height:900}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(new URL('../examples/isotope-wiring/index.html',import.meta.url).href);await expect(page.locator('#core-state')).toHaveText('Passed');
 const cards=page.locator('.reference-card'),scene=page.locator('#canvas-scene');
 const choose=async id=>{await page.locator('#catalog-toggle').click();await page.locator('#catalog-search').fill(id);await page.locator(`#isotopes button[data-id="${id}"]`).click();};
 const ids=['H1','He4','C12','S36','Ar40','Ca44'];
 for(const [i,id] of ids.entries()){
  await choose(id);const pin=page.locator('#pin-reference');await expect(pin).toHaveAttribute('aria-disabled','false');await pin.click();await expect(pin).toHaveAttribute('aria-pressed','true');await page.locator('#catalog-close').click();await expect(cards).toHaveCount(i+1);
 }
 const titles=await cards.locator('h3').allTextContents();assert.deepEqual(titles,['Calcium-44','Argon-40','Sulfur-36','Carbon-12','Helium-4','Hydrogen-1']);
 await expect(page.locator('#reference-cards .cell-hit')).toHaveCount(0);
 const sameScale=async()=>{const metrics=await page.locator('#canvas-scene svg.diagram').evaluateAll(nodes=>nodes.map(n=>({scale:n.getScreenCTM().a,width:n.getBoundingClientRect().width,view:n.getAttribute('viewBox')})));assert.equal(metrics.length,7);for(const m of metrics){assert(Math.abs(m.scale-metrics[0].scale)<1e-6);assert(Math.abs(m.width-metrics[0].width)<1);assert.equal(m.view,metrics[0].view);}};
 const scrollCheck=async()=>{
  const m=await scene.evaluate(e=>({client:e.clientWidth,scroll:e.scrollWidth,overflow:getComputedStyle(e).overflowX}));assert(m.scroll>m.client);assert.equal(m.overflow,'auto');
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'No document-level horizontal overflow');
  await scene.evaluate(e=>{e.scrollLeft=e.scrollWidth;});assert(await scene.evaluate(e=>e.scrollLeft)>0);
  const last=await cards.last().boundingBox(),panel=await scene.boundingBox();assert(last.x+last.width<=panel.x+panel.width+1,'Last pin is reachable by panel scrolling');
  await scene.evaluate(e=>{e.scrollLeft=0;});
 };
 await sameScale();await scrollCheck();await page.locator('#zoom-in').click();await sameScale();await page.locator('#zoom-fit').click();
 await page.reload();await expect(cards).toHaveCount(6);assert.deepEqual(await cards.locator('h3').allTextContents(),titles);await sameScale();
 await choose('K41');await page.locator('#catalog-close').click();assert.deepEqual(await cards.locator('h3').allTextContents(),titles,'Selection does not replace pins');
 // Export must contain every pin, not just the visible portion of the scroller.
 await page.locator('#file-menu > summary').click();const downloadPromise=page.waitForEvent('download');await page.locator('#export-canvas').click();const download=await downloadPromise;const svg=await readFile(await download.path(),'utf8');for(const name of ['Potassium-41',...titles])assert(svg.includes(name));await page.locator('#file-menu > summary').click();
 if(screenshots)await page.screenshot({path:`${screenshots}/references-desktop.png`});
 await page.setViewportSize({width:320,height:700});await sameScale();await scrollCheck();
 if(screenshots)await page.screenshot({path:`${screenshots}/references-mobile.png`});
 await page.locator('#definition-view').click();await expect(scene).toBeHidden();await page.locator('#diagram-view').click();await expect(scene).toBeVisible();
 // A pin off screen can be reached and removed; removing pins is persisted.
 await cards.last().locator('[data-unpin-reference]').click();await expect(cards).toHaveCount(5);await page.reload();await expect(cards).toHaveCount(5);
 while(await cards.count())await cards.first().locator('[data-unpin-reference]').click();await expect(page.locator('#references')).toBeHidden();await page.reload();await expect(cards).toHaveCount(0);
 assert.deepEqual(errors,[]);console.log('PASS: more than three pins, persistence, order, shared scale, full export, panel-only horizontal scrolling on desktop/mobile and unpinning.');
}finally{await browser.close();}
