import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
import * as T from 'three';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>Math.abs(Math.hypot(...(window.normalRayAudit?.cellulationAudit?.translation??[]))-8)<1e-8);
 const button=page.locator('#recenter-view');assert.equal(await button.locator('svg').count(),1);
 const reset=await page.locator('#reset-view').boundingBox(),fit=await button.boundingBox();assert(fit.y>=reset.y+reset.height);assert(Math.abs(fit.x-reset.x)<1);
 const viewportButton=page.locator('#viewport-recenter'),viewportReset=await page.locator('#viewport-reset').boundingBox(),viewportFit=await viewportButton.boundingBox();
 assert.equal(await viewportButton.isVisible(),true);assert(viewportFit.y>=viewportReset.y+viewportReset.height);assert(Math.abs(viewportFit.x-viewportReset.x)<1);
 await page.locator('#close-scene').click();assert.equal(await viewportButton.isVisible(),true);await viewportButton.click();await page.locator('#open-scene').click();
 assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.grid.cells),27);
 await page.evaluate(()=>{window.gridBeforeRotation=normalRayAudit.cellulationAudit.grid;});await page.locator('[data-view-axis="x"]').click();await page.waitForTimeout(100);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.grid===window.gridBeforeRotation),true);
 for(let step=2;step<=10;step++){await page.locator('#cellulation-next').click();await page.waitForFunction(s=>normalRayAudit.cellulationAudit.step===s,step);}
 assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.grid.cells),169);
 await page.getByRole('button',{name:'Roll left',exact:true}).click();await page.waitForTimeout(100);
 const before=await page.evaluate(()=>normalRayViewAudit);await button.focus();await page.keyboard.press('Enter');await page.waitForTimeout(100);
 const v=await page.evaluate(()=>normalRayViewAudit),translation=await page.evaluate(()=>normalRayAudit.cellulationAudit.translation);
 before.quaternion.forEach((x,i)=>assert(Math.abs(x-v.quaternion[i])<1e-9));before.camera.up.forEach((x,i)=>assert(Math.abs(x-v.camera.up[i])<1e-9));
 const camera=new T.OrthographicCamera(...v.frustum,.01,200);camera.zoom=v.zoom;camera.up.fromArray(v.camera.up);camera.position.fromArray(v.target).add(new T.Vector3(...v.camera.offset));camera.lookAt(new T.Vector3(...v.target));camera.updateProjectionMatrix();camera.updateMatrixWorld();
 const points=buildCellulationStep(10).cells.flatMap(c=>c.vertices).map(p=>new T.Vector3(...p).add(new T.Vector3(...translation)).project(camera));
 for(const p of points){assert(Math.abs(p.x)<=.850001);assert(Math.abs(p.y)<=.850001);assert(Math.abs(p.z)<=1);}
 for(const axis of ['x','y'])assert(Math.abs(Math.min(...points.map(p=>p[axis]))+Math.max(...points.map(p=>p[axis])))<1e-8);
 await page.screenshot({path:'test-results/cellulation-recenter.png'});
 await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.completed===0);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.grid.placedCells),6);
 assert((await page.evaluate(()=>normalRayAudit.cellulationAudit.grid.cells))<169);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===10);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.grid.cells),169);
 assert.deepEqual(errors,[]);console.log('PASS: two cached adjacency layers follow placed elements, frame-cross buttons are below Reset in both the panel and viewport, Recenter fits the construction with unchanged viewing direction.');
}finally{await browser.close();}
