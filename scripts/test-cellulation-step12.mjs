import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let step=2;step<=11;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);const before=await page.evaluate(()=>normalRayViewAudit.camera);
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===12);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);assert.equal(await page.locator('#cellulation-next').isDisabled(),false);
 const model=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(model.cells,16);assert.equal(model.grid.cells,180);assert.equal(model.arrows.length,2);assert.equal(model.arrows[0].colour,0xffffff);assert.deepEqual(model.latticeFace,[[8,1,7],[8,2,6],[7,2,7]]);assert.equal(model.animation.whiteFaceCount,3);assert.equal(model.animation.newlyClosedFaceCount,2);assert.equal(model.animation.filledDotVisible,true);assert.deepEqual(model.newlyClosedLatticeFaces,[[[8,1,7],[8,2,6],[7,1,6]],[[8,2,6],[7,2,7],[7,1,6]]]);
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='connecting');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount),0);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.previous.animation.candidateVisible),true);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='filling-vertices');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.finish.arrowProgress),1);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.first.whiteFaceCount),1);await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='complete');
 await page.screenshot({path:'test-results/cellulation-step12.png'});
 await page.locator('#edges-only').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount===0);await page.locator('#edges-only').uncheck();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount===3);
 await page.locator('#face-opacity').fill('0.4');await page.waitForFunction(()=>Math.abs(normalRayAudit.cellulationAudit.animation.whiteFaceOpacity-.22)<1e-9);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===12);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);assert.equal(await page.locator('#cellulation-animate').isChecked(),false);
 assert.deepEqual(errors,[]);console.log('PASS: Step 12 retains 927 → 828, adds white 927 → 817, fills 927 then both remaining faces; camera, IDs, opacity controls and reload are preserved.');
}finally{await browser.close();}
