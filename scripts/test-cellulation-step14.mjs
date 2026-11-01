import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let step=2;step<=13;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);const before=await page.evaluate(()=>normalRayViewAudit.camera);
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===14);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);assert.equal(await page.locator('#cellulation-next').isDisabled(),false);
 const m=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(m.cells,16);assert.equal(m.arrows.length,2);assert(m.arrows.every(a=>a.colour===0xffffff));assert.deepEqual(m.arrows[0].euler,[180,-45,180]);assert.deepEqual(m.latticeFace,[[8,2,6],[8,3,5],[7,3,6]]);assert.equal(m.animation.whiteFaceCount,1);
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='first-arrow');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.secondArrowProgress),0);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='connecting');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.firstArrowProgress),1);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount),0);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='filling-faces');await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='complete');
 await page.locator('#edges-only').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount===0);await page.locator('#edges-only').uncheck();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount===1);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===14);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);
 assert.deepEqual(errors,[]);console.log('PASS: Step 14 draws white 936→837→927 in sequence, fills the triangle, and preserves previous construction, camera and reload.');
}finally{await browser.close();}
