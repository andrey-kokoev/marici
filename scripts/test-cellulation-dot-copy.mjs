import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000},permissions:['clipboard-read','clipboard-write']}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===2);await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);
 const seed=page.locator('[data-dot-lock="seed"]');await seed.dblclick();await page.waitForFunction(()=>document.querySelector('#cellulation-copy-status')?.textContent==='Copied ID: seed');assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),'seed');assert.equal(await page.locator('#cellulation-copy-status').innerText(),'Copied ID: seed');assert.equal(await page.evaluate(()=>normalRayViewAudit.cellulationLock),null);
 await seed.click();await page.waitForFunction(()=>normalRayViewAudit.cellulationLock?.id==='seed');await seed.dblclick();assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),'seed');assert.equal(await page.evaluate(()=>normalRayViewAudit.cellulationLock?.id),'seed');
 await page.waitForFunction(()=>!document.querySelector('#cellulation-copy-status'),null,{timeout:6000});
 await seed.click();await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===3);await page.locator('#viewport-recenter').click();await page.waitForTimeout(100);
 await page.locator('[data-dot-lock="witness"]').dblclick();await page.waitForFunction(()=>document.querySelector('#cellulation-copy-status')?.textContent==='Copied ID: witness');assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),'witness');assert.equal(await page.locator('#cellulation-copy-status').innerText(),'Copied ID: witness');
 await page.evaluate(()=>{
  Object.defineProperty(navigator.clipboard,'write',{configurable:true,value:async()=>{throw new DOMException('Denied','NotAllowedError');}});
  document.execCommand=()=>{throw new DOMException('Fallback denied','NotAllowedError');};
 });
 await seed.dblclick();await page.waitForFunction(()=>document.querySelector('#cellulation-copy-status')?.textContent==='Clipboard unavailable. ID: seed');
 assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),'witness');assert.deepEqual(errors,[]);
 console.log('PASS: VueUse clipboard copies exact dot IDs on double-click, preserves pin state, expires success feedback and reports failure when both clipboard paths are denied.');
}finally{await browser.close();}
