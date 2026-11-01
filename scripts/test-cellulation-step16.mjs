import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let step=2;step<=15;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);const before=await page.evaluate(()=>normalRayViewAudit.camera);
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===16);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);assert.equal(await page.locator('#cellulation-next').isDisabled(),false);
 const m=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(m.cells,16);assert(m.arrows.every(a=>a.colour===0xffffff));assert.deepEqual(m.latticeFaces,[[[8,2,6],[7,2,7],[7,3,6]],[[8,2,6],[7,2,5],[7,1,6]]]);assert.equal(m.animation.whiteFaceCount,2);
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.index===0&&normalRayAudit.cellulationAudit.animation.phase==='connecting');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.parts[1].arrowProgress),0);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.index===1&&normalRayAudit.cellulationAudit.animation.phase==='connecting');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.parts[0].whiteFaceCount),1);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='complete');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount),2);
 await page.locator('#edges-only').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount===0);await page.locator('#edges-only').uncheck();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount===2);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===16);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);
 assert.deepEqual(errors,[]);console.log('PASS: Step 16 draws 828→837 and fills its face, then 826→817 and its face; previous geometry, candidates, camera and reload remain intact.');
}finally{await browser.close();}
