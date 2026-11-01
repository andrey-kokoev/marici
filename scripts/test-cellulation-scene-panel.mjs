import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===1);
 const panel=page.locator('#scene-panel');
 for(const id of ['grid','cell-hover-enabled','prior','azimuth','elevation','ray-view','axial-rotation','rotation-speed'])assert.equal(await panel.locator('#'+id).count(),0,id);
 for(const id of ['opacity','edges-only','face-opacity','bodies','reset-view','zoom-in','zoom-out','auto-rotate'])assert.equal(await panel.locator('#'+id).count(),1,id);
 assert.match(await panel.innerText(),/Show construction/);assert.equal(await panel.locator('[data-view-axis]').count(),3);
 await page.locator('#edges-only').check();assert.equal(await page.locator('#face-opacity').isDisabled(),true);await page.locator('#edges-only').uncheck();assert.equal(await page.locator('#face-opacity').isEnabled(),true);
 await page.locator('#auto-rotate').check();assert.equal(await panel.locator('#rotation-speed').count(),1);await page.locator('#auto-rotate').uncheck();assert.equal(await panel.locator('#rotation-speed').count(),0);
 await page.screenshot({path:'test-results/cellulation-clean-scene-panel.png'});
 await page.selectOption('#sulfur-32-view','cellulation-reference');await page.waitForFunction(()=>normalRayAudit.cellulationAudit.source==='repeating-fcc');assert.match(await panel.innerText(),/Show faces/);assert.equal(await panel.locator('#prior').count(),0);
 await page.selectOption('#sulfur-32-view','channels');await page.waitForFunction(()=>normalRayAudit.view!=='cellulation');
 for(const id of ['cell-hover-enabled','prior','azimuth','elevation','ray-view','axial-rotation','rotation-speed'])assert.equal(await panel.locator('#'+id).count(),1,id);
 assert.deepEqual(errors,[]);console.log('PASS: cellulation Scene panel contains only relevant controls; other views retain their controls.');
}finally{await browser.close();}
