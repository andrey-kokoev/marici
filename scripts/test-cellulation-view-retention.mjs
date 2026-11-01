import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===1);
 await page.waitForFunction(()=>normalRayViewAudit.camera.up.every(v=>Math.abs(v+1/Math.sqrt(3))<1e-10));
 await page.locator('[data-view-axis="z"]').click();await page.getByRole('button',{name:'Zoom +',exact:true}).click();
 await page.mouse.move(650,400);await page.mouse.down({button:'right'});await page.mouse.move(1050,450,{steps:10});await page.mouse.up({button:'right'});await page.waitForTimeout(200);
 const restart=async()=>{await page.locator('#cellulation-animate').uncheck();await page.locator('#cellulation-animate').check();};
 const read=()=>page.evaluate(()=>({camera:normalRayViewAudit.camera,target:normalRayViewAudit.target,frustum:normalRayViewAudit.frustum}));
 const saved=await read();
 const values=o=>[...o.camera.offset,...o.camera.targetOffset,...o.camera.up,o.camera.zoom,...o.target,...o.frustum];
 async function unchanged(){const actual=values(await read()),expected=values(saved);actual.forEach((x,i)=>assert(Math.abs(x-expected[i])<1e-8,`Camera component ${i}: ${x} != ${expected[i]}`));}
 for(const step of [2,3,4]){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);await unchanged();}
 await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation?.phase==='complete');assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.proposalVisible&&!normalRayAudit.cellulationAudit.animation.whiteDotVisible),true);await unchanged();
 await restart();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation?.phase==='proposition');await unchanged();
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===5);await unchanged();
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===6);await unchanged();
 await restart();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='candidates');await unchanged();
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===7);await unchanged();
 await restart();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.stage===2);await unchanged();
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===8);await unchanged();
 await restart();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='opposite-vertex');await unchanged();
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===9);await unchanged();
 await restart();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='first-tetrahedron');await unchanged();
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===10);await unchanged();
 await restart();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='extending'&&normalRayAudit.cellulationAudit.animation.iteration===1);await unchanged();
 for(const step of [9,8,7,6,5,4,3,2,1]){await page.locator('#cellulation-prev').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);await unchanged();}
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===1);await unchanged();
 await page.selectOption('#sulfur-32-view','cellulation-reference');await page.waitForFunction(()=>normalRayAudit.cellulationAudit.source==='repeating-fcc');await unchanged();
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.source==='repeating-fcc');await unchanged();
 await page.selectOption('#sulfur-32-view','channels');await page.waitForFunction(()=>normalRayAudit.view!=='cellulation');
 await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>normalRayAudit.cellulationAudit?.step===1);await unchanged();
 await page.locator('#reset-view').click();await page.waitForFunction(()=>normalRayViewAudit.zoom===1&&normalRayViewAudit.camera.up.every(v=>Math.abs(v+1/Math.sqrt(3))<1e-10));
 assert.deepEqual(errors,[]);console.log('PASS: steps, Animate toggle, reference view, view return and reload preserve the camera; only explicit Reset restores the default.');
}finally{await browser.close();}
