import assert from 'node:assert/strict';
import {mkdir} from 'node:fs/promises';
import {chromium} from '@playwright/test';
import {Vector3,Quaternion} from 'three';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');
 await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 // Explicitly reframe the translated construction for the click-interaction tests.
 await page.locator('#reset-view').click();
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===2);
 const view=()=>page.evaluate(()=>normalRayViewAudit);
 const cameraNormal=v=>new Vector3(...v.cellulationLock.normal).applyQuaternion(new Quaternion(...v.quaternion).invert()).toArray();
 const near=(a,b,tolerance=1e-7)=>a.forEach((x,i)=>assert(Math.abs(x-b[i])<tolerance,`${a} != ${b}`));
 function invariant(before,after){const id=before.cellulationLock.id,a=before.cellulationDots.find(d=>d.id===id),b=after.cellulationDots.find(d=>d.id===id);near([a.x,a.y],[b.x,b.y],1e-5);near(cameraNormal(before),cameraNormal(after));}
 async function drag(button='left'){await page.mouse.move(700,430);await page.mouse.down({button});await page.mouse.move(1120,490,{steps:15});await page.mouse.up({button});await page.waitForTimeout(150);}
 await page.locator('[data-dot-lock="seed"]').click();await page.waitForFunction(()=>normalRayViewAudit.cellulationLock?.id==='seed');
 const pinStyle=await page.locator('[data-dot-lock="seed"]').evaluate(el=>({shadow:getComputedStyle(el).boxShadow,barWidth:getComputedStyle(el,'::after').width,barHeight:getComputedStyle(el,'::after').height,barTop:getComputedStyle(el,'::after').top}));
 assert.deepEqual(pinStyle,{shadow:'none',barWidth:'12px',barHeight:'2px',barTop:'2px'});
 let before=await view();await drag();let after=await view();invariant(before,after);assert(after.quaternion.some((x,i)=>Math.abs(x-before.quaternion[i])>1e-5));
 before=after;await drag('right');after=await view();invariant(before,after);near(before.camera.targetOffset,after.camera.targetOffset);
 await page.getByRole('button',{name:'Zoom +',exact:true}).click();await page.waitForFunction(z=>normalRayViewAudit.zoom>z,before.zoom);after=await view();invariant(before,after);
 await page.locator('[data-view-axis="x"]').click();await page.waitForTimeout(100);invariant(before,await view());
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===3);assert.equal((await view()).cellulationLock.id,'seed');
 await page.locator('#cellulation-next').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===4);assert.equal((await view()).cellulationLock.id,'seed');
 await page.locator('[data-dot-lock="witness"]').click();await page.waitForFunction(()=>normalRayViewAudit.cellulationLock?.id==='witness');
 before=await view();await drag();after=await view();invariant(before,after);assert(after.quaternion.some((x,i)=>Math.abs(x-before.quaternion[i])>1e-5));
 await mkdir('test-results',{recursive:true});await page.screenshot({path:'test-results/cellulation-dot-lock.png'});
 await page.locator('[data-dot-lock="witness"]').focus();await page.keyboard.press('Enter');await page.waitForFunction(()=>normalRayViewAudit.cellulationLock===null);
 await page.locator('[data-dot-lock="seed"]').click();await page.waitForFunction(()=>normalRayViewAudit.cellulationLock?.id==='seed');
 await page.locator('#reset-view').click();await page.waitForFunction(()=>normalRayViewAudit.cellulationLock===null);
 await page.locator('[data-dot-lock="witness"]').click();await page.waitForFunction(()=>normalRayViewAudit.cellulationLock?.id==='witness');
 await page.locator('#cellulation-prev').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===3);assert.equal((await view()).cellulationLock.id,'witness');
 await page.locator('#cellulation-prev').click();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.step===2&&normalRayViewAudit.cellulationLock===null);
 assert.deepEqual(errors,[]);console.log('PASS: click/keyboard dot locks, normal-constrained drag/presets, fixed screen position through zoom, no pan, replacement/release/reset and step retention.');
}finally{await browser.close();}
