import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
import * as T from 'three';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','cellulation');await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===1);
 async function upperLeft(){
  const v=await page.evaluate(()=>normalRayViewAudit),c=new T.OrthographicCamera(...v.frustum,.01,200);c.zoom=v.camera.zoom;c.up.fromArray(v.camera.up);c.position.fromArray(v.target).add(new T.Vector3(...v.camera.offset));c.lookAt(new T.Vector3(...v.target));c.updateProjectionMatrix();c.updateMatrixWorld();const translation=await page.evaluate(()=>normalRayAudit.cellulationAudit.translation),p=new T.Vector3(...[1,1,1].map((x,i)=>x/(2*Math.SQRT2)+translation[i])).project(c);
  assert(Math.abs(p.x+.44)<1e-8);assert(Math.abs(p.y-.44)<1e-8);
 }
 await page.waitForFunction(()=>Math.abs(Math.hypot(...normalRayAudit.cellulationAudit.translation)-8)<1e-8);await page.locator('#reset-view').click();await page.waitForTimeout(100);
 await upperLeft();assert.equal(await page.locator('#grid').count(),0);
 for(const s of [2,3]){await page.locator('#cellulation-next').click();await page.waitForFunction(step=>normalRayAudit.cellulationAudit.step===step,s);}
 const before=await page.evaluate(()=>({camera:normalRayViewAudit.camera,arrow:normalRayAudit.cellulationAudit.arrows[0]}));
 await page.locator('#cellulation-cell-size').fill('0.5');await page.waitForFunction(()=>normalRayViewAudit.zoom===.5&&normalRayAudit.cellulationAudit.grid.layers===2);
 const after=await page.evaluate(()=>({camera:normalRayViewAudit.camera,arrow:normalRayAudit.cellulationAudit.arrows[0],model:normalRayAudit.cellulationAudit}));assert.deepEqual(after.arrow,before.arrow);assert.equal(after.model.cellSize,1);assert.equal(after.model.grid.cellSize,1);assert.equal(after.model.grid.cells,27);assert.deepEqual({...after.camera,zoom:undefined},{...before.camera,zoom:undefined});
 await page.locator('#reset-view').click();await page.waitForTimeout(100);await upperLeft();assert.equal(await page.evaluate(()=>normalRayViewAudit.zoom),.5);
 await page.screenshot({path:'test-results/cellulation-full-viewport.png'});
 await page.locator('#cellulation-next').click();await page.locator('#cellulation-animate').check();await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.phase==='proposition');await page.waitForFunction(()=>normalRayAudit.cellulationAudit.animation.first>.25);
 await page.locator('#cellulation-cell-size').fill('1.5');await page.waitForFunction(()=>normalRayViewAudit.zoom===1.5);assert((await page.evaluate(()=>normalRayAudit.cellulationAudit.animation.first))>=.25);
 await page.reload();await page.waitForFunction(()=>window.normalRayAudit?.cellulationAudit?.step===4);assert.equal(await page.evaluate(()=>normalRayViewAudit.zoom),1.5);assert.equal(await page.evaluate(()=>normalRayAudit.cellulationAudit.cellSize),1);assert.equal(await page.locator('#cellulation-animate').isChecked(),false);
 assert.deepEqual(errors,[]);console.log('PASS: fixed unit cells, inverse visible-area scaling, bounded two-layer lattice, upper-left reset at both scales, no animation restart, and scale persistence.');
}finally{await browser.close();}
