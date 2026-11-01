import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1200}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 for(const processId of ['beryllium-8','beryllium-9']){
  await page.selectOption('#process-select',processId);await page.uncheck('#seed-pairs-by-layer');await page.check('#seed-show-reference');
  await page.waitForFunction(()=>document.querySelectorAll('.assembly-canvas[data-audit]').length===3);
  const hosts=page.locator('.assembly-canvas');
  await page.locator('#sulfur-reference-top h3').hover();
  const full=await hosts.first().screenshot();
  for(const row of ['#sulfur-reference-top','#be-reference-fixed-forward','#be-reference-fixed-reverse']){
   const strand=page.locator(row+' [data-strand]').nth(2),id=await strand.getAttribute('data-strand');
   // Whole column, including the label area, must hit without aiming at a thin line.
   await strand.locator('.strand-hit').hover({position:{x:15,y:10}});
   await page.waitForFunction(id=>[...document.querySelectorAll('.assembly-canvas')].every(e=>JSON.parse(e.dataset.visibleStrands).length===8&&Object.entries(JSON.parse(e.dataset.strandOpacities)).every(([strand,opacity])=>opacity===(strand===id?1:.2))),id);
   assert(!full.equals(await hosts.first().screenshot()),'Rendered image must change, not just the hover attribute');
   await page.locator('#sulfur-reference-top h3').hover();
   await page.waitForFunction(()=>[...document.querySelectorAll('.assembly-canvas')].every(e=>JSON.parse(e.dataset.visibleStrands).length===8&&Object.values(JSON.parse(e.dataset.strandOpacities)).every(opacity=>opacity===1)));
  }
  for(let i=0;i<3;i++){
   const host=hosts.nth(i),canvas=host.locator('canvas');await canvas.scrollIntoViewIfNeeded();
   const initial=await host.getAttribute('data-camera'),target=await host.getAttribute('data-target');
   await canvas.hover();const scroll=await page.locator('#sulfur-reference-panel').evaluate(e=>e.scrollTop);
   await page.mouse.wheel(0,-400);await page.waitForFunction(({i,initial})=>document.querySelectorAll('.assembly-canvas')[i].dataset.camera!==initial,{i,initial});
   const zoomed=JSON.parse(await host.getAttribute('data-camera'));assert(Math.hypot(...zoomed)<Math.hypot(...JSON.parse(initial)));
   assert.equal(await page.locator('#sulfur-reference-panel').evaluate(e=>e.scrollTop),scroll,'Wheel zoom must not scroll the panel');
   const box=await canvas.boundingBox();await page.mouse.move(box.x+box.width/2,box.y+box.height/2);await page.mouse.down({button:'right'});await page.mouse.move(box.x+box.width/2+35,box.y+box.height/2+20,{steps:5});await page.mouse.up({button:'right'});
   assert.notEqual(await host.getAttribute('data-target'),target);
   const beforeRotate=await host.getAttribute('data-camera');await page.mouse.down();await page.mouse.move(box.x+box.width/2-25,box.y+box.height/2-20,{steps:5});await page.mouse.up();assert.notEqual(await host.getAttribute('data-camera'),beforeRotate);
   await host.locator('..').getByRole('button').click();assert.equal(await host.getAttribute('data-camera'),initial);assert.equal(await host.getAttribute('data-target'),target);
  }
 }
 assert.deepEqual(errors,[]);console.log('PASS: Be-8/Be-9 hover highlighting with all other strands dimmed but visible from all three rows, rendered-image changes, restoration, wheel zoom without panel scrolling, right-drag pan, left-drag rotation and Reset on every canvas.');
}finally{await browser.close();}
