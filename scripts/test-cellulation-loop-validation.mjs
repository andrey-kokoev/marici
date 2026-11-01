import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let step=2;step<=20;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 const toggle=page.getByLabel('Validate loop',{exact:true});assert.equal(await toggle.isChecked(),false);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.loopValidation),null);
 const camera=await page.evaluate(()=>normalRayViewAudit.camera);await toggle.check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.loopValidation?.issues?.length===2);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),camera);
 assert.equal(await page.locator('[data-loop-join]').count(),4);assert.equal(await page.locator('[data-loop-issue]').count(),2);assert((await page.locator('#loop-validation-report').innerText()).includes('N–N–P–E roles'));
 assert.equal(await page.locator('#loop-validation-overlay').evaluate(el=>getComputedStyle(el).pointerEvents),'none');await page.evaluate(()=>{window.loopReportBefore=normalRayAudit.cellulationAudit.loopValidation;});
 for(const axis of ['x','y','z']){
  await page.locator(`[data-view-axis="${axis}"]`).click();await page.locator('#viewport-recenter').click();await page.waitForTimeout(150);
  assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.loopValidation===window.loopReportBefore),true);
  await page.screenshot({path:`test-results/cellulation-loop-validation-${axis}.png`});
 }
 await toggle.uncheck();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.loopValidation===null);assert.equal(await page.locator('#loop-validation-overlay').count(),0);
 await toggle.check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.loopValidation?.issues?.length===2);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.loopValidation===window.loopReportBefore),true);
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayViewAudit.loopValidation?.status==='pending');await page.waitForFunction(()=>normalRayViewAudit.loopValidation?.issues?.length===2);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.loopValidation?.issues?.length===2);assert.equal(await toggle.isChecked(),true);
 await page.locator('#cellulation-prev').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===19);assert.equal(await page.locator('#loop-validation-overlay').count(),0);
 assert.deepEqual(errors,[]);console.log('PASS: opt-in loop validation reports two route conflicts, four closed joins, valid cells and unresolved roles; caches through camera rotation, pauses during animation, and persists.');
}finally{await browser.close();}
