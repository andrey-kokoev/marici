import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===1);
 for(let step=2;step<=22;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);const camera=await page.evaluate(()=>normalRayViewAudit.camera);let ids=await page.evaluate(()=>normalRayViewAudit.cellulationDots.map(a=>a.id));
 for(let step=23;step<=26;step++){
  await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s&&normalRayAudit.cellulationAudit.animation.phase==='complete',step);
  assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),camera);
  const a=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(a.unitTriangles,64);assert.equal(a.cells,[94,124,149,174][step-23]);assert.equal(a.interiorCellsExcluded,86);assert.deepEqual(a.surfaceColorCounts,step<25?{red:15,blue:0,white:20}:{red:0,blue:15,white:10});
  const dots=await page.evaluate(()=>normalRayViewAudit.cellulationDots);for(const id of ids)assert(dots.some(d=>d.id===id));ids=dots.map(d=>d.id);assert.equal(new Set(dots.map(d=>d.latticePoint.join(','))).size,dots.length);
  await page.screenshot({path:`test-results/cellulation-step${step}.png`});
 }
 assert.equal(await page.locator('#cellulation-next').isDisabled(),true);assert((await page.locator('#shell-order-warning').innerText()).includes('Order dependence detected'));assert((await page.locator('#shell-dot-422-unresolved').innerText()).includes('unresolved'));assert((await page.locator('#shell-role-compatibility').innerText()).includes('unresolved'));
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase!=='complete');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.grid.placedCells),149);
 await page.locator('#cellulation-animate').uncheck();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='complete');
 await page.locator('#shell-witness-start').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.witness.action===0&&normalRayAudit.cellulationAudit.witness.completedFaces===0);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.grid.placedCells),149);
 for(let action=1;action<=14;action++){await page.locator('#shell-action-next').click();await page.waitForFunction(a=>normalRayAudit.cellulationAudit.witness.action===a,action);if(action<9)assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.witness.completedFaces),0);if(action===7)await page.screenshot({path:'test-results/cellulation-shell-witness-before-fill.png'});}
 assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.grid.placedCells),150);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.previous.animation.phase),'complete');
 await page.locator('#shell-witness-start').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.witness.completedCells===0);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.witness.completedFaces),0);
 await page.locator('#shell-witness-complete').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='complete');
 await page.locator('#cellulation-validate-loop').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.loopValidation?.issues?.length===2);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===26);assert.equal(await page.locator('#cellulation-animate').isChecked(),false);
 await page.locator('#cellulation-validate-loop').uncheck();await page.locator('[data-view-axis="z"]').click();await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);await page.screenshot({path:'test-results/cellulation-shell.png'});
 assert.deepEqual(errors,[]);console.log('PASS: four face-fill steps preserve camera and IDs, form a seed-colored red/white and blue/white 174-cell shell, support replay/validation/reload and leave 86 deep interior cells excluded.');
}finally{await browser.close();}
