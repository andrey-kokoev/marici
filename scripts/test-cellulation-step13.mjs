import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let step=2;step<=12;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);const before=await page.evaluate(()=>normalRayViewAudit.camera);
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===13);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);assert.equal(await page.locator('#cellulation-next').isDisabled(),false);
 const m=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(m.cells,16);assert.equal(m.grid.cells,180);assert.equal(m.arrows[0].colour,0xffffff);assert.deepEqual(m.arrows[0].fromLattice,[8,2,6]);assert.deepEqual(m.arrows[0].toLattice,[8,3,5]);assert.deepEqual(m.arrows[0].euler,[-45,45,90]);
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='growing-arrow');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.previous.animation.whiteFaceCount),3);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.previous.animation.filledDotVisible),true);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='complete');assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.cellulationDots.find(a=>a.id==='step13:candidate').latticePoint),[8,3,5]);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===13);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);
 assert.deepEqual(errors,[]);console.log('PASS: Step 13 draws the requested white 927→936 arrow and hollow candidate, preserving completed Step 12, camera and saved step.');
}finally{await browser.close();}
