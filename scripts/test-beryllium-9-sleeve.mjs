import assert from 'node:assert/strict';
import {mkdir} from 'node:fs/promises';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1680,height:1200}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 await page.selectOption('#process-select','beryllium-9');await page.uncheck('#seed-pairs-by-layer');await page.check('#seed-show-reference');
 await page.waitForFunction(()=>document.querySelectorAll('.assembly-canvas[data-audit]').length===3&&[...document.querySelectorAll('.assembly-canvas')].every(e=>JSON.parse(e.dataset.audit).centralSleeves===1));
 assert.equal(await page.locator('#be9-central-sleeve').isChecked(),true);
 const ids=await page.evaluate(()=>normalRayComparisonAudit.referenceIds);
 assert.equal(await page.locator('.reference-strand').count(),8);assert.equal(await page.locator('#sulfur-reference-top .polarity-arrow').count(),16);
 for(const a of await page.locator('.assembly-canvas').evaluateAll(xs=>xs.map(e=>JSON.parse(e.dataset.audit)))){assert.equal(a.vertices,7);assert.equal(a.edges,16);assert.equal(a.strands,8);assert.equal(a.sleeveStrands,4);assert.equal(a.incomingPairs,2);assert.equal(a.outgoingPairs,2);}
 assert.match(await page.locator('#sulfur-reference-top h3').innerText(),/central sleeve trial/);
 await page.locator('#process-panel').evaluate(e=>e.scrollTop=0);await mkdir('test-results',{recursive:true});await page.screenshot({path:'test-results/beryllium-9-central-sleeve.png'});
 await page.uncheck('#be9-central-sleeve');await page.waitForFunction(()=>[...document.querySelectorAll('.assembly-canvas')].every(e=>JSON.parse(e.dataset.audit).edges===12));
 assert.equal(await page.locator('#sulfur-reference-top .polarity-arrow').count(),12);assert.deepEqual(await page.evaluate(()=>normalRayComparisonAudit.referenceIds),ids);
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayComparisonAudit?.referenceKind==='be9-reference-clone');assert.equal(await page.locator('#be9-central-sleeve').isChecked(),false);
 await page.check('#be9-central-sleeve');await page.waitForFunction(()=>normalRayComparisonAudit.referenceKind==='be9-central-sleeve-candidate');
 await page.selectOption('#process-select','beryllium-8');await page.waitForFunction(()=>normalRayComparisonAudit.processId==='beryllium-8'&&[...document.querySelectorAll('.assembly-canvas')].every(e=>JSON.parse(e.dataset.audit).edges===12));
 assert.equal(await page.locator('#be9-central-sleeve').count(),0);assert.equal(await page.locator('#sulfur-reference-top .polarity-arrow').count(),12);
 assert.deepEqual(errors,[]);console.log('PASS: Be-9 central-sleeve trial, four retained passages, three assemblies, reversible toggle, persistence and unchanged Be-8.');
}finally{await browser.close();}
