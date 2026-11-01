import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===1);
 for(let step=2;step<=9;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 const camera=await page.evaluate(()=>normalRayViewAudit.camera);
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===10);
 const audit=await page.evaluate(()=>normalRayAudit.cellulationAudit);assert.equal(audit.cells,15);assert.equal(audit.tetrahedra,8);assert.equal(audit.octahedra,7);assert.equal(audit.interiorFaces,14);assert.equal(audit.animation.completed,5);assert.equal(audit.animation.dotCount,32);assert.equal(audit.animation.phase,'complete');assert.equal(audit.animation.current.animation.current.animation.whiteFaceCount,8);
 assert.equal(await page.locator('#cellulation-next').isDisabled(),false);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),camera);
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.iteration===1&&normalRayAudit.cellulationAudit.animation.completed===0);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.previous.animation.phase),'complete');
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.current.animation.phase==='octahedron',null,{timeout:30000});
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.iteration===2);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.completed),1);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),camera);
 await page.locator('#cellulation-animate').uncheck();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.completed===5);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.dotCount),32);
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.completed===0);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===10);assert.equal(await page.locator('#cellulation-animate').isChecked(),false);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.completed),5);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),camera);
 await page.locator('#cellulation-prev').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===9);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.cells),5);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),camera);
 assert.deepEqual(errors,[]);console.log('PASS: Step 10 repeats five times, retains Step 9, animates sequentially, completes instantly when off, persists without autoplay, and preserves the camera.');
}finally{await browser.close();}
