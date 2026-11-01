import assert from 'node:assert/strict';
import {mkdir} from 'node:fs/promises';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','beryllium-9');await page.selectOption('#beryllium-9-view','wiring-single-procedure');
 await page.waitForFunction(()=>globalThis.normalRayAudit?.wiringProcedureAudit?.step===0);
 await page.waitForFunction(()=>Math.abs(normalRayViewAudit.camera.offset[0])<1e-8&&Math.abs(normalRayViewAudit.camera.offset[1])<1e-8);
 const start=await page.evaluate(()=>normalRayAudit.wiringProcedureAudit);assert.equal(start.wires,16);assert.equal(start.strands,8);
 await page.click('#be9-wiring-next');await page.waitForFunction(()=>normalRayAudit.wiringProcedureAudit.step===1);
 const twist=await page.evaluate(()=>normalRayAudit.wiringProcedureAudit);assert.deepEqual(twist.wireIds,start.wireIds);assert.equal(twist.maxOutOfPlane,0);assert.equal(twist.straightHalves,true);assert.deepEqual(twist.pinchPoint,[0,0,0]);assert.equal(twist.subbundles,0);
 assert.equal(await page.locator('#be9-wiring-next').isDisabled(),true);
 await mkdir('test-results',{recursive:true});await page.screenshot({path:'test-results/be9-wiring-single-knot.png'});
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.wiringProcedureAudit?.step===1);assert.deepEqual(await page.evaluate(()=>normalRayAudit.wiringProcedureAudit),twist);
 await page.click('#be9-wiring-prev');await page.waitForFunction(()=>normalRayAudit.wiringProcedureAudit.step===0);
 assert.deepEqual(errors,[]);console.log('PASS: flat sixteen-wire bundle, straight single-point knot, no step 2, persistence and return.');
}finally{await browser.close();}
