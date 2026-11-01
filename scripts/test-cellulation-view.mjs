import assert from 'node:assert/strict';
import {mkdir} from 'node:fs/promises';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1440,height:960}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 const url=process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html';
 await page.goto(url);await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);await page.selectOption('#process-select','fibration-12x12');await page.locator('#cellulation-view').click();
 await page.waitForFunction(()=>window.cellulationAudit?.visibleCells===175&&window.cellulationAudit.camera);
 assert.equal(await page.locator('#error').innerText(),'');assert.equal(await page.locator('canvas').count(),1);
 assert.equal(await page.evaluate(()=>cellulationAudit.labels+cellulationAudit.overlays+cellulationAudit.internalOctahedralDiagonals),0);
 const original=await page.evaluate(()=>cellulationAudit.camera);
 const box=await page.locator('canvas').boundingBox();await page.mouse.move(box.x+box.width*.5,box.y+box.height*.5);await page.mouse.down();await page.mouse.move(box.x+box.width*.65,box.y+box.height*.6,{steps:12});await page.mouse.up();
 await page.waitForFunction(before=>JSON.stringify(cellulationAudit.camera)!==JSON.stringify(before),original);
 await page.locator('canvas').focus();await page.keyboard.press('+');await page.waitForFunction(()=>cellulationAudit.zoom>1);
 await page.locator('#reset').click();await page.waitForFunction(()=>cellulationAudit.zoom===1);
 await page.locator('#tetrahedra').uncheck();await page.waitForFunction(()=>cellulationAudit.visibleCells===56);
 await page.locator('#octahedra').uncheck();await page.waitForFunction(()=>cellulationAudit.visibleCells===0&&cellulationAudit.uniqueFaces===0);
 await page.locator('#tetrahedra').check();await page.waitForFunction(()=>cellulationAudit.visibleCells===119);
 await page.locator('#octahedra').check();await page.locator('#edges').uncheck();await page.waitForFunction(()=>!cellulationAudit.edgesVisible);await page.locator('#edges').check();
 await page.locator('#opacity').fill('0.3');await page.waitForFunction(()=>cellulationAudit.opacity===.3);await page.locator('#opacity').fill('0.12');
 await mkdir('test-results',{recursive:true});await page.screenshot({path:'test-results/cellulation-view.png'});
 await page.setViewportSize({width:390,height:844});await page.waitForTimeout(200);assert(await page.locator('canvas').evaluate(c=>c.clientHeight>400&&c.clientWidth<=390));
 await page.screenshot({path:'test-results/cellulation-view-mobile.png'});
 await page.getByRole('link',{name:'← Views'}).click();await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 assert.deepEqual(errors,[]);console.log('PASS: 175 whole cells, no labels/overlays, type filters, opacity/edges, camera drag/zoom/reset, mobile sizing and round-trip navigation.');
}finally{await browser.close();}
