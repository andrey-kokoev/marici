import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 for(let step=2;step<=16;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);const before=await page.evaluate(()=>normalRayViewAudit.camera),ids=await page.evaluate(()=>normalRayViewAudit.cellulationDots.map(a=>a.id));
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===17);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);assert.equal(await page.locator('#cellulation-next').isDisabled(),false);
 const m=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(m.cells,17);assert.equal(m.arrows[0].colour,0xffffff);assert.deepEqual(m.latticeFaces,[[[7,3,6],[7,2,5],[8,3,5]],[[7,3,6],[7,2,5],[8,2,6]]]);assert.equal(m.animation.whiteFaceCount,4);assert.equal(m.animation.whiteRectangleCount,1);assert.deepEqual(m.latticeRectangle,[[7,1,6],[7,2,7],[7,3,6],[7,2,5]]);assert.equal(m.animation.filledDotCount,3);
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='connecting');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.filledDotCount),0);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.previous.animation.whiteFaceCount),2);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='filling-vertices');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount),0);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='filling-faces');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.vertexFillProgress),1);
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='complete');assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.cellulationDots.map(a=>a.id)),ids);
 await page.locator('#edges-only').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount===0);await page.locator('#edges-only').uncheck();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.whiteFaceCount===4);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===17);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),before);
 assert.deepEqual(errors,[]);console.log('PASS: Step 17 draws 837→826, fills three existing dots then both requested triangles and rectangle 817–828–837–826; camera and IDs persist.');
}finally{await browser.close();}
