import assert from 'node:assert/strict';
import {mkdir} from 'node:fs/promises';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 // Enter from Su-32 Wiring: Be must not depend on the saved sulfur view flag.
 await page.selectOption('#process-select','sulfur-32');await page.selectOption('#sulfur-32-view','wiring');
 await page.waitForFunction(()=>globalThis.normalRayAudit?.incomingBundleAudit?.strands===16);
 await page.selectOption('#process-select','beryllium-8');
 await page.waitForFunction(()=>normalRayAudit.processId==='beryllium-8'&&normalRayAudit.branchingSeedAudit?.layers===8);
 const audit=await page.evaluate(()=>normalRayAudit.branchingSeedAudit);
 assert.equal(audit.depth,4);assert.equal(audit.edgeLayers,8);assert.equal(audit.sidePairs,32);assert.equal(audit.sidePairsPerLayer,4);assert.equal(audit.sidePairHeight,6);assert.equal(audit.sidePairSleevesPerLayer,4);assert.equal(audit.edges,240);assert.equal(audit.nodes,200);
 assert.deepEqual(audit.reflectionCenter,[0,-3.5,-1]);
 assert.match(await page.locator('#seed-show-reference').locator('..').innerText(),/Show Be-8 reference/);
 assert.deepEqual(await page.locator('#beryllium-8-view option').allTextContents(),['White-rooted hex simplex']);
 assert.equal(await page.locator('#sulfur-32-view').count(),0);assert.equal(await page.locator('#sulfur-32-fibrate').count(),0);assert.equal(await page.locator('#sulfur-wire-info').count(),0);
 assert.equal(await page.locator('.process-navigation').count(),0);assert.equal(await page.locator('#step').isVisible(),false);assert.equal(await page.locator('#inventory-panel').isVisible(),false);
 assert.equal(await page.locator('#seed-layer-selector button').count(),8);
 await page.click('#seed-layer-2');await page.waitForFunction(()=>normalRayAudit.branchingSeedAudit.visibleLayers.length===7);
 await page.locator('#seed-layer-gap').fill('3');await page.locator('#seed-layer-gap').dispatchEvent('input');await page.waitForFunction(()=>normalRayAudit.branchingSeedAudit.gap===3);
 await page.click('#seed-face-on');await page.click('#seed-layers-view');
 await page.check('#seed-pairs-combined');await page.check('#seed-show-reference');await page.selectOption('#seed-comparison-rule','same-colour');
 await page.waitForFunction(()=>globalThis.normalRayComparisonAudit?.sourceCopies===56);
 assert.equal(await page.locator('.reference-strand').count(),8);assert.equal(await page.locator('.combined-strand').count(),8);
 assert.match(await page.locator('#sulfur-reference-top h3').innerText(),/Be-8 reference candidate/);
 assert.equal(await page.evaluate(()=>normalRayComparisonAudit.referenceIds.every(id=>id.startsWith('be8:wire:'))),true);
 const alignment=await page.evaluate(()=>[...document.querySelectorAll('.reference-strand')].map((g,i)=>g.querySelector('text').getAttribute('x')===document.querySelectorAll('.combined-strand')[i].querySelector('text').getAttribute('x')));assert(alignment.every(Boolean));
 assert.equal(await page.locator('#sulfur-reference-top .polarity-arrow').count(),12);
 assert.deepEqual(await page.locator('.reference-strand').evaluateAll(xs=>xs.map(x=>Number(x.dataset.polarity))),[0,0,1,1,-1,-1,0,0]);
 for(const id of ['be-reference-fixed-forward','be-reference-fixed-reverse'])assert.equal(await page.locator('#'+id+' .polarity-arrow').count(),12);
 assert.deepEqual(await page.locator('#sulfur-reference-top .polarity-label').allTextContents(),['P/E →','P/E →','P/E ←','P/E ←']);
 const arrowChecks=await page.locator('.reference-strand, .reference-direction-strand').evaluateAll(xs=>xs.every(g=>{
  const arrows=[...g.querySelectorAll('.polarity-arrow')];
  return arrows.length===(Number(g.dataset.polarity)?3:0)&&arrows.every((a,i)=>a.getAttribute('fill')==='#ffffff'&&Number(a.dataset.segment)===i);
 }));assert(arrowChecks);
 const originalIds=await page.locator('.reference-strand').evaluateAll(xs=>xs.map(x=>x.dataset.strand));
 const fixedRows=['be-reference-fixed-forward','be-reference-fixed-reverse'];
 for(const id of fixedRows){
  assert.equal(await page.locator('#'+id+' .reference-direction-strand').count(),8);
  assert.deepEqual(await page.locator('#'+id+' .reference-direction-strand').evaluateAll(xs=>xs.map(x=>x.dataset.strand)),originalIds);
 }
 assert.deepEqual(await page.locator('#be-reference-fixed-forward .direction-component').allTextContents(),['white','white','white','red','red','white','blue','blue']);
 assert.deepEqual(await page.locator('#be-reference-fixed-reverse .direction-component').allTextContents(),['white','white','red','white','white','red','blue','blue']);
 assert.equal(await page.locator('.reference-direction-row polyline[stroke-dasharray]').count(),0);
 assert.equal(await page.locator('#sulfur-reference-top polyline[stroke-dasharray]').count(),4);
 for(const id of fixedRows){
  assert.deepEqual(await page.locator('#'+id+' .direction-output-slot').allTextContents(),['3','6','7','2','1','8','5','4']);
  const samePaths=await page.evaluate(rowId=>[...document.querySelectorAll('#'+rowId+' .reference-direction-strand')].every((g,i)=>g.querySelector('polyline').getAttribute('points')===document.querySelectorAll('.reference-strand')[i].querySelector('polyline').getAttribute('points')),id);assert(samePaths);
 }
 assert.equal(await page.locator('.reference-direction-row [marker-end], [data-read-reversed], .direction-slot-order').count(),0);
 const fixedAlignment=await page.evaluate(()=>[...document.querySelectorAll('.reference-strand')].every((g,i)=>[...document.querySelectorAll('.reference-direction-row')].every(row=>row.querySelectorAll('.reference-direction-strand')[i].querySelector('text').getAttribute('x')===g.querySelector('text').getAttribute('x'))));assert(fixedAlignment);
 const rowPositions=await page.evaluate(()=>['sulfur-reference-top','be-reference-fixed-forward','be-reference-fixed-reverse','sulfur-combined-bottom'].map(id=>document.getElementById(id).getBoundingClientRect().top));assert(rowPositions.every((y,i)=>i===0||y>rowPositions[i-1]));
 await mkdir('test-results',{recursive:true});await page.screenshot({path:'test-results/beryllium-8-reference-comparison.png'});
 await page.locator('#sulfur-reference-panel').evaluate(e=>e.scrollTop=0);await page.screenshot({path:'test-results/beryllium-8-direction-components.png'});
 await page.uncheck('#seed-pairs-combined');await page.uncheck('#seed-show-reference');
 assert.equal(await page.locator('.reference-direction-row').count(),0);
 await page.locator('#process-panel').evaluate(e=>e.scrollTop=0);
 await mkdir('test-results',{recursive:true});await page.screenshot({path:'test-results/beryllium-8-white-rooted.png'});
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.processId==='beryllium-8'&&normalRayAudit.branchingSeedAudit?.gap===3&&normalRayAudit.branchingSeedAudit.depth===4);
 assert.equal(await page.locator('#process-select').inputValue(),'beryllium-8');assert.equal(await page.locator('#beryllium-8-view').inputValue(),'branching-seed');assert.equal(await page.locator('#seed-layer-2').getAttribute('aria-pressed'),'false');
 await page.selectOption('#process-select','sulfur-32');await page.waitForFunction(()=>normalRayAudit.incomingBundleAudit?.strands===16);
 assert.equal(await page.locator('#sulfur-32-view').inputValue(),'wiring');
 await page.selectOption('#process-select','beryllium-8');await page.waitForFunction(()=>normalRayAudit.processId==='beryllium-8'&&normalRayAudit.branchingSeedAudit?.layers===8);
 assert.deepEqual(errors,[]);console.log('PASS: Be-8 depth four, four pairs per layer, independent eight-route reference, two component-selection copies with unchanged paths and slots, persistence, and unchanged Su-32 selection.');
}finally{await browser.close();}
