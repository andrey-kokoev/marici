import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {chromium} from '@playwright/test';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const registry=JSON.parse(await fs.readFile(path.join(root,'research/strominger/results/neutrino_seed_candidates.json'),'utf8'));
const browser=await chromium.launch({headless:true,args:['--enable-unsafe-swiftshader']});
const errors=[];let samples=0;
try{
 const page=await browser.newPage({viewport:{width:1500,height:1000}});
 page.on('pageerror',e=>errors.push(e.message));
 for(const asset of ['papers/witness-generators/proton-neutron-assembly.html','website/public/experiments/proton-neutron-assembly.html']){
  await page.setViewportSize({width:1500,height:1000});
  console.log('Checking',asset);
  await page.goto(pathToFileURL(path.join(root,asset)).href);
  await page.waitForFunction(()=>window.neutrinoAssemblyAudit||!document.querySelector('#error').hidden);
  assert.equal(await page.locator('#error').isVisible(),false,await page.locator('#error').textContent());
  await page.locator('#focus').selectOption('neutrino');
  assert.equal(await page.locator('#neutrino-seed option').count(),7);
  await page.locator('#construction-controls > summary').click();
  for(const candidate of registry.candidates){
   await page.locator('#neutrino-seed').selectOption(String(candidate.id));
   for(let stage=0;stage<8;stage++){
    await page.locator(`[data-step="${stage}"]`).click();
    await page.waitForTimeout(1100);
    const audit=await page.evaluate(()=>window.neutrinoAssemblyAudit);
    assert.equal(audit.candidate,candidate.id);assert.equal(audit.stage,stage+1);
    assert.deepEqual(audit.counts,candidate.geometry.counts);
    assert.deepEqual(audit.cycles,candidate.seed_cycles);
    assert.equal(audit.spinDecoration,false);assert.equal(audit.chargeAssigned,false);
    assert.equal(audit.physicsDerived,false);
    if(stage<2)assert.equal(audit.filledFaces,0);
    if(stage>=3)assert.equal(audit.shownCells,candidate.geometry.counts.cone_cells);
    const markers=await page.evaluate(()=>window.vertexMarkerAudit);
    assert(Math.abs(markers.maxRadius-markers.standardRadius)<1e-12);
    samples++;
   }
   await page.locator('#seed-arrows').scrollIntoViewIfNeeded();
   await page.locator('#seed-arrows').check();
   const arrows=await page.evaluate(()=>window.seedArrowAudit.neutrino);
   assert.equal(arrows.arrowCount,candidate.seed_cycles.reduce((n,c)=>n+c.length-1,0));
   assert.equal(arrows.visible,true);
   await page.locator('#seed-arrows').uncheck();
  }
  const before=await page.evaluate(()=>window.neutrinoAssemblyAudit.points);
  for(const layer of ['surfaces','edges','vertices','labels']){
   await page.locator('#layer-'+layer).uncheck();
   assert.equal(await page.evaluate(k=>window.displayLayerAudit.counts[k],layer),0);
   await page.locator('#layer-'+layer).check();
  }
  assert.deepEqual(await page.evaluate(()=>window.neutrinoAssemblyAudit.points),before);
  await page.locator('#focus').selectOption('proton');
  assert.equal(await page.locator('#neutrino-candidates').isVisible(),false);
  for(const width of [390,1500]){await page.setViewportSize({width,height:900});await page.waitForTimeout(150);assert.equal(await page.locator('#error').isVisible(),false);}
 }
 assert.deepEqual(errors,[]);
 const result={status:'passed',samples,seven_candidates_all_eight_stages_both_assets:true,seed_counts:true,layer_filters_preserve_geometry:true,no_spin_or_charge_decoration:true,page_errors:errors};
 await fs.writeFile(path.join(root,'research/strominger/results/neutrino_seed_workbench_browser.json'),JSON.stringify(result,null,2)+'\n');
 console.log(JSON.stringify(result,null,2));
}finally{await browser.close();}
