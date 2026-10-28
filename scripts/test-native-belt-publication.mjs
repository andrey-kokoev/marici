import assert from 'node:assert/strict';import fs from 'node:fs/promises';import path from 'node:path';import http from 'node:http';import {chromium} from '@playwright/test';
const root=path.resolve('website/public'),server=http.createServer(async(req,res)=>{try{const file=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);if(!file.startsWith(root+path.sep))throw Error('path');res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml'})[path.extname(file)]??'application/octet-stream');res.end(await fs.readFile(file));}catch{res.statusCode=404;res.end();}});
await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;
try{
 browser=await chromium.launch();const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[],failed=[];page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.status()>=400)failed.push(r.url());});
 await page.goto(`http://127.0.0.1:${server.address().port}/experiments/native-belt/index.html?preset=native-belt`);
 await page.waitForFunction(()=>globalThis.normalRayAudit?.parentCutAudit?.visibleCutCount===2&&!normalRayAudit.graphMode);
 assert.equal(await page.locator('#particle-counts caption').innerText(),'P / N / E counts');
 assert.equal(await page.locator('#particle-counts tbody tr').count(),3);
 assert.deepEqual(await page.locator('#particle-counts [data-count-row="belt-faces"] td').allTextContents(),['32','14','32','78']);
 assert.deepEqual(await page.locator('#particle-counts [data-count-row="combined"] td').allTextContents(),['250','126','206','582']);
 assert.equal(await page.locator('#particle-counts [data-count-row="tip-electrons"]').count(),0);
 assert.deepEqual(await page.locator('#particle-counts [data-count-row="parents-exposed"] td').allTextContents(),['218','112','174','504']);
 assert.equal(await page.evaluate(()=>normalRayAudit.parentEdgeRays.length),0);
 assert.deepEqual(await page.evaluate(()=>normalRayAudit.parentCellulations.map(p=>p.counts)),[{tetrahedra:119,octahedra:56,exposedFaces:196},{tetrahedra:119,octahedra:56,exposedFaces:196}]);
 assert.deepEqual(await page.evaluate(()=>{const e=normalRayAudit.geometryLayoutAudit.beltExtension;return [e.P,e.E,e.addedBoundaryFaces];}),[32,32,32]);
 assert.equal(await page.locator('#process-select').inputValue(),'double-esd7');assert.equal(await page.locator('#shape-view').inputValue(),'geometry');assert.ok(!page.url().includes('preset='));
 assert.deepEqual(await page.evaluate(()=>NormalRayViewer.snapshot().view.vertexLabels.filter(v=>[1,2,7].includes(v.index)).map(v=>v.visible)),[false,false,false]);
 assert.equal(await page.getByRole('link',{name:'← Gallery'}).getAttribute('href'),'/experiments/');assert.equal(await page.getByRole('link',{name:'Guide and scope'}).getAttribute('href'),'/experiments/native-belt-guide');
 await page.selectOption('#shape-view','wiring');await page.waitForFunction(()=>normalRayAudit.graphMode&&normalRayAudit.wiringLayoutAudit?.kind==='exploded-native-cell-dual');
 assert.deepEqual(await page.evaluate(()=>NormalRayViewer.snapshot().view.vertexLabels.filter(v=>[1,2,7].includes(v.index)).map(v=>v.visible)),[false,false,false]);
 assert.equal(await page.evaluate(()=>normalRayAudit.graphNodeCount),384);assert.equal(await page.evaluate(()=>normalRayAudit.graphLinkCount),794);
 assert.deepEqual(await page.locator('#particle-counts [data-count-row="combined"] td').allTextContents(),['176','126','82','384']);
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.graphMode);assert.equal(await page.locator('#shape-view').inputValue(),'wiring');
 // The viewport inventory is compact by default; all original counts remain available.
 assert.equal(await page.locator('#particle-counts tfoot').isVisible(),false);
 await page.selectOption('#process-select','single-octahedral');
 await page.waitForFunction(()=>globalThis.normalRayAudit?.singleOctahedralAudit);
 const panel=page.locator('#inventory-panel'),summary=panel.locator(':scope > summary');
 const countsBefore=await page.locator('#particle-counts tbody td').allTextContents();
 assert.equal(await page.locator('#particle-counts tbody tr:visible').count(),1);
 assert.equal(await page.locator('#particle-counts caption').innerText(),'Whole cells');
 await page.check('#inventory-details');
 assert((await page.locator('#particle-counts tbody tr:visible').count())>10);
 assert(await page.locator('#particle-counts tfoot').isVisible());
 assert.deepEqual(await page.locator('#particle-counts tbody td').allTextContents(),countsBefore);
 await summary.click();assert.equal(await page.locator('#particle-counts').isVisible(),false);
 assert((await panel.boundingBox()).height<50);
 await summary.focus();await page.keyboard.press('Enter');
 assert(await page.locator('#particle-counts').isVisible());
 assert(await page.locator('#inventory-details').isChecked());
 await page.uncheck('#inventory-details');
 assert.equal(await page.locator('#particle-counts tbody tr:visible').count(),1);
 await page.setViewportSize({width:390,height:844});
 for(const detailed of [false,true]){
  await page.locator('#inventory-details').setChecked(detailed);
  const box=await panel.boundingBox(),scene=await page.locator('#scene').boundingBox();
  assert(box.x>=scene.x&&box.x+box.width<=scene.x+scene.width+1);
  assert(box.y>=scene.y&&box.y+box.height<=scene.y+scene.height+1);
 }
 await summary.click();assert.equal(await page.locator('#particle-counts').isVisible(),false);
 assert.deepEqual(errors,[]);assert.deepEqual(failed,[]);console.log('Published native belt: local assets, launch preset, gallery return, geometry/wiring, persistence and responsive collapsible inventory passed');
}finally{await browser?.close();await new Promise(r=>server.close(r));}
