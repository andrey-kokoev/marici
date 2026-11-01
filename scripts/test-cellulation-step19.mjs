import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000},permissions:['clipboard-read','clipboard-write']}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let step=2;step<=18;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);const before=await page.evaluate(()=>normalRayViewAudit.camera),ids=await page.evaluate(()=>normalRayViewAudit.cellulationDots.map(a=>a.id));
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===19);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);assert.equal(await page.locator('#cellulation-next').isDisabled(),false);
 const m=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(m.cells,36);assert.equal(m.grid.placedCells,36);assert.equal(m.sharedCells,1);assert.equal(m.rotationDegrees,180);assert.equal(m.arrows.length,8);assert(m.arrows.every(a=>a.colour===0x3080ff));assert.deepEqual(m.attachmentLattice,[8,8,0]);assert.deepEqual(m.endLattice,[0,8,8]);assert.deepEqual(m.arrows[0].to.map(x=>Math.round(x*Math.SQRT2)),[7,8,1]);
 const dots=await page.evaluate(()=>normalRayViewAudit.cellulationDots);for(const id of ids)assert(dots.some(a=>a.id===id));assert.equal(new Set(dots.map(a=>a.latticePoint.join(','))).size,dots.length);
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='rolling-blue-clone');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.previous.animation.completed),5);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.grid.placedCells),22);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='complete');assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===19);assert.equal(await page.locator('#cellulation-animate').isChecked(),false);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);await page.screenshot({path:'test-results/cellulation-step19.png'});
 const end=await page.evaluate(()=>normalRayViewAudit.cellulationDots.find(a=>a.id.startsWith('blue:')&&a.latticePoint.join(',')==='0,8,8'));assert(end?.visible);
 await page.locator(`[data-dot-lock="${end.id}"]`).dblclick();await page.waitForFunction(id=>document.querySelector('#cellulation-copy-status')?.textContent===`Copied ID: ${id}`,end.id);assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),end.id);
 assert.deepEqual(errors,[]);console.log('PASS: Step 19 attaches eight blue arrows at 880, starts 880→781 and continues to (0,8,8), preserves prior geometry/camera/IDs, and supports blue-dot copying and reload.');
}finally{await browser.close();}
