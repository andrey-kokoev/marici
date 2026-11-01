import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let step=2;step<=10;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);const before=await page.evaluate(()=>normalRayViewAudit.camera);
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===11);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);assert.equal(await page.locator('#cellulation-next').isDisabled(),false);
 const model=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(model.cells,15);assert.equal(model.grid.cells,169);assert.equal(model.arrows.length,1);assert.deepEqual(model.arrows[0].fromLattice,[8,1,7]);assert.deepEqual(model.arrows[0].toLattice,[8,2,6]);assert.deepEqual(model.arrows[0].euler,[-45,-45,90]);
 assert(await page.evaluate(()=>normalRayViewAudit.cellulationDots.some(a=>JSON.stringify(a.latticePoint)==='[8,1,7]')));
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='growing-arrow');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.previous.animation.completed),5);await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='complete');
 assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.candidateVisible),true);
 const candidate=await page.evaluate(()=>normalRayViewAudit.cellulationDots.find(a=>a.id==='step11:candidate'));assert.deepEqual(candidate.latticePoint,[8,2,6]);
 assert.match(await page.locator('[data-dot-lock="step11:candidate"]').getAttribute('title'),/ID: step11:candidate/);
 await page.screenshot({path:'test-results/cellulation-step11.png'});
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===11);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);
 await page.locator('#cellulation-prev').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===10);
 assert.deepEqual(errors,[]);console.log('PASS: step 11 draws (9,1,8) → (9,2,7), preserves the assembly and camera, animates only its arrow, and persists across reload.');
}finally{await browser.close();}
