import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 const saved={offset:[0,0,10],targetOffset:[0,0,0],up:[0,1,0],zoom:.5};
 await page.addInitScript(camera=>{
  const key='marici:isotope-constructor:v1:scene-settings';
  if(!localStorage.getItem(key))localStorage.setItem(key,JSON.stringify({version:1,process:{id:'sulfur-32'},appearance:{sulfurCellulation:true,cellulationStep:1},camera}));
 },saved);
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.translation?.[1]===8);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),saved);assert.deepEqual(await page.evaluate(()=>normalRayAudit.cellulationAudit.translation),[0,8,0]);
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===2);
 assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.cellulationDots.find(d=>d.id==='seed').point),[0,8,0]);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),saved);
 for(let step=3;step<=10;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);assert.deepEqual(await page.evaluate(()=>normalRayAudit.cellulationAudit.translation),[0,8,0]);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),saved);}
 await page.locator('[data-view-axis="x"]').click();await page.waitForTimeout(150);assert.deepEqual(await page.evaluate(()=>normalRayAudit.cellulationAudit.translation),[0,8,0]);
 const rotated=await page.evaluate(()=>normalRayViewAudit.camera);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===10);assert.deepEqual(await page.evaluate(()=>normalRayAudit.cellulationAudit.translation),[0,8,0]);assert.deepEqual(await page.evaluate(()=>normalRayViewAudit.camera),rotated);
 assert.deepEqual(errors,[]);console.log('PASS: one eight-unit screen-up translation, unchanged saved camera, world-space anchors, all steps aligned, no following rotations or repeated translation on reload.');
}finally{await browser.close();}
