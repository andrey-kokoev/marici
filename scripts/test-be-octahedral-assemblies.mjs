import assert from 'node:assert/strict';
import {mkdir} from 'node:fs/promises';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1200}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','beryllium-8');await page.uncheck('#seed-pairs-by-layer');await page.check('#seed-show-reference');
 await page.waitForFunction(()=>document.querySelectorAll('.assembly-canvas canvas').length===3&&[...document.querySelectorAll('.assembly-canvas')].every(e=>e.dataset.audit));
 assert.equal(await page.locator('.route-arrow').count(),36);
 for(const slot of [3,6,4,5])assert.equal(await page.locator('#sulfur-reference-top [data-strand]').filter({has:page.locator('text').filter({hasText:new RegExp('^'+slot+'$')})}).locator('.route-arrow').count(),3);
 const audits=await page.locator('.assembly-canvas').evaluateAll(xs=>xs.map(x=>JSON.parse(x.dataset.audit)));
 for(const a of audits){assert.equal(a.strands,8);assert.equal(a.edges,12);assert.equal(a.vertices,6);assert.equal(a.polarityArrows,12);assert.equal(a.routeArrows,12);assert.equal(new Set(a.ids).size,8);}
 assert(audits[0].colours.filter(c=>c.length===2).length===4);assert(audits[1].colours.every(c=>c.length===1));assert(audits[2].colours.every(c=>c.length===1));
 const panel=await page.locator('#sulfur-reference-panel').boundingBox(),processBox=await page.locator('#process-panel').boundingBox(),scene=await page.locator('#scene-panel').boundingBox();
 assert(panel.width>620);assert(panel.x>=processBox.x+processBox.width);assert(panel.x+panel.width<=scene.x);
 for(const id of ['sulfur-reference-top','be-reference-fixed-forward','be-reference-fixed-reverse']){
  const chart=await page.locator('#'+id+' .reference-assembly-row > svg').boundingBox(),assembly=await page.locator('#'+id+' .octahedral-assembly').boundingBox();assert(assembly.x>=chart.x+chart.width);assert(Math.abs(assembly.y-chart.y)<2);
 }
 const strand=await page.locator('.reference-strand').nth(2).getAttribute('data-strand');await page.locator('.reference-strand').nth(2).locator('.strand-hit').hover();
 await page.waitForFunction(id=>[...document.querySelectorAll('.assembly-canvas')].every(e=>e.dataset.highlight===id),strand);
 const canvas=page.locator('.assembly-canvas canvas').first(),host=page.locator('.assembly-canvas').first(),initialCamera=await host.getAttribute('data-camera');
 await canvas.focus();await page.keyboard.press('ArrowRight');await page.waitForFunction(before=>document.querySelector('.assembly-canvas').dataset.camera!==before,initialCamera);
 await page.keyboard.press('Home');await page.waitForFunction(before=>document.querySelector('.assembly-canvas').dataset.camera===before,initialCamera);
 await page.locator('#sulfur-reference-top h3').hover();await page.waitForFunction(()=>[...document.querySelectorAll('.assembly-canvas')].every(e=>e.dataset.highlight===''));
 await mkdir('test-results',{recursive:true});await page.locator('#sulfur-reference-panel').evaluate(e=>e.scrollTop=0);await page.screenshot({path:'test-results/beryllium-8-octahedral-assemblies.png'});
 await page.uncheck('#seed-show-reference');assert.equal(await page.locator('.assembly-canvas canvas').count(),0);
 await page.check('#seed-show-reference');await page.waitForFunction(()=>document.querySelectorAll('.assembly-canvas canvas').length===3);
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','branching-seed');assert.equal(await page.locator('.assembly-canvas canvas').count(),0);
 assert.deepEqual(errors,[]);console.log('PASS: three real eight-strand octahedral assemblies, wider side-by-side layout, linked highlighting, keyboard rotation/reset, teardown and unchanged Su-32.');
}finally{await browser.close();}
