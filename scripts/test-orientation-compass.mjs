import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 const compass=page.locator('#orientation-compass');assert(await compass.isVisible());assert.equal(await compass.locator('[data-compass-direction]').count(),6);assert.equal(await compass.locator('[data-compass-plane]').count(),3);
 const box=await compass.boundingBox(),canvas=await page.locator('canvas').first().boundingBox();assert(Math.abs(box.x-canvas.x-12)<1);assert(Math.abs(canvas.y+canvas.height-box.y-box.height-12)<1);
 assert.equal(await compass.evaluate(el=>getComputedStyle(el).pointerEvents),'none');
 await page.locator('[data-view-axis="z"]').click();await page.waitForTimeout(100);const before=await compass.locator('[data-compass-direction="+X"] line').getAttribute('y2');
 await page.getByRole('button',{name:'Roll left',exact:true}).click();await page.waitForTimeout(100);assert.notEqual(await compass.locator('[data-compass-direction="+X"] line').getAttribute('y2'),before);
 await page.locator('#close-scene').click();assert(await compass.isVisible());await page.waitForTimeout(100);
 await page.screenshot({path:'test-results/orientation-compass.png'});assert.deepEqual(errors,[]);console.log('PASS: bottom-left compass shows signed XYZ directions and XY/XZ/YZ planes, follows camera rotation, and never intercepts pointer input.');
}finally{await browser.close();}
