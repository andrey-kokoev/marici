import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.NORMAL_RAY_URL??'http://127.0.0.1:8777/research/realization-tower/normal-ray.html');
 await page.waitForFunction(()=>document.querySelector('#process-select')&&!document.querySelector('#process-select').disabled);
 for(const processId of ['beryllium-8','sulfur-32']){
  await page.selectOption('#process-select',processId);
  if(processId==='sulfur-32')await page.selectOption('#sulfur-32-view','branching-seed');
  await page.waitForFunction(id=>globalThis.normalRayAudit?.processId===id&&!!normalRayAudit.branchingSeedAudit,processId);
  await page.check('#seed-pairs-by-layer');
  const before=await page.evaluate(()=>({layers:[...normalRayAudit.branchingSeedAudit.visibleLayers],gap:normalRayAudit.branchingSeedAudit.gap}));
  for(const byLayer of [false,true])for(const combined of [false,true])for(const reference of [false,true]){
   await page.locator('#seed-pairs-by-layer').setChecked(byLayer);
   await page.locator('#seed-pairs-combined').setChecked(combined);
   await page.locator('#seed-show-reference').setChecked(reference);
   await page.waitForFunction(({byLayer,combined})=>
    !!document.getElementById('seed-layer-selector')===(byLayer||combined)&&
    !!document.getElementById('seed-spatial-controls')===byLayer&&
    !!document.getElementById('seed-layer-geometry-notes')===byLayer,{byLayer,combined});
   for(const id of ['seed-layer-gap','seed-layers-view','seed-face-on'])assert.equal(await page.locator('#'+id).count(),byLayer?1:0);
   assert.equal(await page.locator('#seed-layer-selector button').count(),byLayer||combined?8:0);
   assert.equal(await page.locator('#sulfur-reference-top').count(),reference?1:0);
   assert.equal(await page.locator('#sulfur-combined-bottom').count(),combined?1:0);
   if(combined&&!byLayer)assert.equal(await page.locator('#seed-layer-selector').getAttribute('aria-label'),'Combined source layers');
   assert.deepEqual(await page.evaluate(()=>({layers:[...normalRayAudit.branchingSeedAudit.visibleLayers],gap:normalRayAudit.branchingSeedAudit.gap})),before);
  }
  // Combined-only selectors remain functional; hidden controls retain settings.
  await page.uncheck('#seed-pairs-by-layer');await page.check('#seed-pairs-combined');
  await page.click('#seed-layer-2');await page.waitForFunction(()=>!normalRayComparisonAudit.sourceLayers.includes(2));
  await page.uncheck('#seed-pairs-combined');assert.equal(await page.locator('#seed-layer-selector').count(),0);
  await page.check('#seed-pairs-combined');assert.equal(await page.locator('#seed-layer-2').getAttribute('aria-pressed'),'false');
  await page.click('#seed-layer-2');await page.check('#seed-pairs-by-layer');
 }
 assert.deepEqual(errors,[]);
 console.log('PASS: all eight view-toggle combinations on Be-8 and Su-32; irrelevant controls hidden, Combined input selectors functional, settings retained.');
}finally{await browser.close();}
