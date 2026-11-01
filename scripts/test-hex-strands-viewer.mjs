import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
import {mkdir} from 'node:fs/promises';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>!document.querySelector('#process-select')?.disabled);
 await page.selectOption('#process-select','sulfur-32');
 await page.selectOption('#sulfur-32-view','hex-strands');
 await page.waitForFunction(()=>globalThis.normalRayAudit?.hexStrandsAudit?.visibleFamilies.length===16);
 await mkdir('test-results',{recursive:true});await page.screenshot({path:'test-results/hex-strands-3d.png'});
 await page.selectOption('#hex-strand-select','SLLLL');
 await page.waitForFunction(()=>normalRayAudit.hexStrandsAudit.visibleFamilies.length===1);
 for(let stage=0;stage<=7;stage++){
  await page.selectOption('#hex-strand-stage',String(stage));
  await page.waitForFunction(stage=>normalRayAudit.hexStrandsAudit.stage===stage&&normalRayAudit.hexStrandsAudit.traceCopies===16*2**stage,stage);
 }
 await page.selectOption('#hex-strand-copy','127');
 await page.waitForFunction(()=>normalRayAudit.hexStrandsAudit.copy===127);
 await page.locator('#hex-strand-spacing').fill('0.5');await page.locator('#hex-strand-spacing').dispatchEvent('input');
 await page.waitForFunction(()=>normalRayAudit.hexStrandsAudit.spacing===.5);
 await page.reload();
 await page.waitForFunction(()=>globalThis.normalRayAudit?.hexStrandsAudit?.copy===127&&normalRayAudit.hexStrandsAudit.spacing===.5);
 assert.equal(await page.locator('#sulfur-32-view').inputValue(),'hex-strands');
 await page.selectOption('#hex-strand-stage','0');await page.waitForFunction(()=>normalRayAudit.hexStrandsAudit.copy===-1);
 await page.selectOption('#sulfur-32-view','wiring');
 await page.waitForFunction(()=>normalRayAudit.incomingBundleAudit?.strands===16);
 await page.selectOption('#sulfur-32-view','geometry');await page.waitForFunction(()=>!normalRayAudit.hexStrandsAudit&&!normalRayAudit.incomingBundleAudit);
 assert.deepEqual(errors,[]);console.log('Hex strands 3D: stages, isolation, copy selection, spacing, persistence and existing views passed.');
}finally{await browser.close();}
