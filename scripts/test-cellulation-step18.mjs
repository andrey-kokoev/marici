import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let step=2;step<=17;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);const before=await page.evaluate(()=>normalRayViewAudit.camera),ids=await page.evaluate(()=>normalRayViewAudit.cellulationDots.map(a=>a.id));
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===18&&normalRayAudit.cellulationAudit.animation.completed===5);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);assert.equal(await page.locator('#cellulation-next').isDisabled(),false);
 const m=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(m.cells,22);assert.equal(m.grid.placedCells,22);assert.equal(m.animation.reusedStep12,true);
 const dots=await page.evaluate(()=>normalRayViewAudit.cellulationDots);assert.equal(dots.length,ids.length+15);assert.equal(new Set(dots.map(a=>a.id)).size,dots.length);assert(dots.some(a=>a.latticePoint.join(',')==='8,8,0'));
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.completed===0&&normalRayAudit.cellulationAudit.animation.step===13);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.grid.placedCells),17);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.previous.animation.whiteRectangleCount),1);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.step===14);await page.locator('#cellulation-animate').uncheck();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.completed===5);
 assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.current.animation.whiteRectangleCount),1);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===18);assert.equal(await page.locator('#cellulation-animate').isChecked(),false);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.completed),5);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);await page.screenshot({path:'test-results/cellulation-step18.png'});
 assert.deepEqual(errors,[]);console.log('PASS: Step 18 repeats five times in (0,+1,-1), reuses joins, preserves prior work/camera/IDs, animates new stages only and reloads complete.');
}finally{await browser.close();}
