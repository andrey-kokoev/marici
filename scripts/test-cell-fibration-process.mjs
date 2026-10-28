import assert from 'node:assert/strict';
import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import {chromium} from '@playwright/test';
const root=process.cwd(),server=http.createServer(async(req,res)=>{
 try{const p=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);if(!p.startsWith(root+path.sep))throw Error('path');res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css'})[path.extname(p)]??'text/plain');res.end(await fs.readFile(p));}catch{res.statusCode=404;res.end();}
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;
try{
 browser=await chromium.launch();const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(`http://127.0.0.1:${server.address().port}/research/realization-tower/normal-ray.html`);
 await page.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().draws>0);
 await page.selectOption('#process-select','fibration-12x12');await page.waitForFunction(()=>normalRayAudit.processId==='fibration-12x12');
 const envelope=await page.evaluate(()=>NormalRayViewer.snapshot().vertices);
 await page.click('#next');await page.waitForFunction(()=>normalRayAudit.proceduralStep===1);
 await page.selectOption('#process-select','cell-fibration');await page.waitForFunction(()=>normalRayAudit.processId==='cell-fibration');
 assert.deepEqual(await page.evaluate(()=>NormalRayViewer.snapshot().vertices),envelope);
 const totals=[[1,2,1,4],[4,8,4,16],[10,20,10,40],[11,22,11,44],[11,34,11,56],[17,46,17,80],[19,48,17,84],[19,90,17,126],[24,98,20,142],[27,101,20,148],[27,105,20,152],[33,111,20,164],[39,111,20,170],[41,113,20,174],[42,113,20,175]];
 for(let step=0;step<15;step++){
  if(step)await page.click('#next');
  await page.waitForFunction(s=>normalRayAudit.proceduralStep===s,step);
  assert.deepEqual(await page.locator('[data-count-row="total"] td').allTextContents(),totals[step].map(String));
  assert.equal(await page.evaluate(()=>normalRayAudit.presentationBodyCount),totals[step][3]);
  assert.equal(await page.locator('#next').isDisabled(),step===14);
 }
 await page.check('#highlight-unassigned');await page.waitForFunction(()=>normalRayAudit.highlightedUnassignedCount===0);
 assert.equal(await page.locator('#cut-empty').isChecked(),true);
 await page.uncheck('#highlight-unassigned');await page.waitForFunction(()=>normalRayAudit.highlightedUnassignedCount===0);
 assert.match(await page.locator('#process-step-index').innerText(),/^Step 14 \/ 14/);
 assert.equal(await page.evaluate(()=>normalRayAudit.cellFibrationAudit.growth.filter(g=>g.kind==='inner-hex-reflection').length),12);
 assert.equal(await page.locator('#hex-conflicts').count(),0);
 assert.equal(await page.locator('#cell-construction-rules li').count(),15);
 await page.click('[data-cut-vertex="all"]');await page.click('[data-cut-layer="2"]');await page.click('[data-cut-start-layer="2"]');await page.check('#cut-enabled');
 await page.waitForFunction(()=>normalRayAudit.presentationBodyCount===40&&normalRayAudit.cutAudit.wireframeCount===0);
 await fs.mkdir('research/strominger/results/cell-fibration-viewer',{recursive:true});
 await page.screenshot({path:'research/strominger/results/cell-fibration-viewer/layer-2-current.png'});
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.proceduralStep===14&&normalRayAudit.presentationBodyCount===40);
 await page.click('[data-cut-vertex="1"]');await page.click('[data-cut-layer="3"]');await page.click('[data-cut-start-layer="3"]');
 await page.waitForFunction(()=>normalRayAudit.presentationBodyCount===19);
 await page.uncheck('#cut-empty');await page.waitForFunction(()=>normalRayAudit.cutAudit.wireframeCount===0);
 await page.click('#clear-cut');await page.waitForFunction(()=>normalRayAudit.presentationBodyCount===175);
 await page.selectOption('#process-select','fibration-12x12');await page.waitForFunction(()=>normalRayAudit.processId==='fibration-12x12');
 assert.equal(await page.evaluate(()=>normalRayAudit.proceduralStep),1);
 await page.selectOption('#process-select','cell-fibration');await page.waitForFunction(()=>normalRayAudit.processId==='cell-fibration'&&normalRayAudit.proceduralStep===14);
 for(const count of [174,170,164,152,148,142,126,84,80,56,44,40,16,4]){await page.click('#prev');await page.waitForFunction(n=>normalRayAudit.presentationBodyCount===n,count);}
 await page.click('#next');await page.waitForFunction(()=>normalRayAudit.presentationBodyCount===16);
 await page.click('#restart-cell-fibration');await page.waitForFunction(()=>normalRayAudit.presentationBodyCount===4);
 // Migrate an old endpoint before the application reads saved progress.
 await page.addInitScript(()=>{const key='marici:isotope-constructor:v1:scene-settings',saved=JSON.parse(localStorage.getItem(key));saved.process.step=99;saved.process.progress['cell-fibration'].step=99;localStorage.setItem(key,JSON.stringify(saved));});
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.proceduralStep===14&&normalRayAudit.presentationBodyCount===175);
 assert.equal(await page.locator('#next').isDisabled(),true);
 assert.deepEqual(errors,[]);console.log('Cell fibration: removed layer-3/4/5 growth, retained lower-layer rules, cuts, progress migration, Previous/Restart and process isolation passed');
}finally{await browser?.close();await new Promise(r=>server.close(r));}
