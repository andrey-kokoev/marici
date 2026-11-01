import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000},permissions:['clipboard-read','clipboard-write']}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let step=2;step<=19;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);const before=await page.evaluate(()=>normalRayViewAudit.camera),ids=await page.evaluate(()=>normalRayViewAudit.cellulationDots.map(a=>a.id));
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===20);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);assert.equal(await page.locator('#cellulation-next').isDisabled(),false);
 const m=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(m.cells,42);assert.equal(m.grid.placedCells,42);assert.equal(m.sharedCells,1);assert.deepEqual(m.attachmentLattice,[0,8,8]);assert.deepEqual(m.endLattice,[0,0,0]);assert.equal(m.animation.closed,true);assert(m.arrows.every(a=>a.colour===0xffffff));
 const dots=await page.evaluate(()=>normalRayViewAudit.cellulationDots);for(const id of ids)assert(dots.some(a=>a.id===id));assert.equal(new Set(dots.map(a=>a.latticePoint.join(','))).size,dots.length);
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='turning-closing-white-bar');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.previous.animation.phase),'complete');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.grid.placedCells),36);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.closed);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===20);assert.equal(await page.locator('#cellulation-animate').isChecked(),false);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);await page.screenshot({path:'test-results/cellulation-step20.png'});
 const candidate=await page.evaluate(()=>normalRayViewAudit.cellulationDots.find(a=>a.id.startsWith('closing-white:')&&a.visible));assert(candidate);
 await page.locator(`[data-dot-lock="${candidate.id}"]`).dblclick();await page.waitForFunction(id=>document.querySelector('#cellulation-copy-status')?.textContent===`Copied ID: ${id}`,candidate.id);assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),candidate.id);
 assert.deepEqual(errors,[]);console.log('PASS: Step 20 closes blue 088 to red 000 with only a reflected/rotated white bar, reuses shared cells and IDs, preserves camera, and supports replay/reload/copy.');
}finally{await browser.close();}
