import assert from 'node:assert/strict';
import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {chromium} from '@playwright/test';
import {retainedPbStages} from '../research/realization-tower/retained-pb-process.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const server=http.createServer(async(req,res)=>{
 try{const p=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);if(!p.startsWith(root+path.sep))throw Error('path');
 res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css'})[path.extname(p)]??'text/plain');res.end(await fs.readFile(p));
 }catch{res.statusCode=404;res.end();}
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));
const browser=await chromium.launch();
try{
 const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 // The prior incorrect process must not restore an already assembled scene.
 await page.addInitScript(()=>{if(!sessionStorage.getItem('migration-seeded')){localStorage.setItem('marici:isotope-constructor:v1:scene-settings',JSON.stringify({version:1,process:{id:'retained-pb',k:7,step:6}}));sessionStorage.setItem('migration-seeded','yes');}});
 await page.goto(`http://127.0.0.1:${server.address().port}/research/realization-tower/normal-ray.html`);
 await page.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().draws>0&&normalRayAudit.processId==='retained-construction');
 assert.equal(await page.evaluate(()=>normalRayAudit.retainedAudit.bodyCount),1);
 assert.equal(await page.evaluate(()=>normalRayAudit.surfaceCount),4);
 assert.equal(await page.locator('#step').isDisabled(),true);
 assert.equal(await page.locator('#retained-pb-audit').isVisible(),true);
 assert.equal(await page.locator('#particle-counts').isVisible(),false);
 let prior=1;
 for(let step=1;step<retainedPbStages.length;step++){
  await page.click('#next');await page.waitForFunction(s=>normalRayAudit.proceduralStep===s,step);
  const count=await page.evaluate(()=>normalRayAudit.retainedAudit.bodyCount);assert.ok(count>prior);prior=count;
 }
 const audit=await page.evaluate(()=>normalRayAudit.retainedAudit);
 assert.equal(audit.bodyCount,175);assert.equal(audit.primitiveComponents,343);
 assert.equal(audit.particleRolesAssigned,false);assert.equal(await page.locator('#next').isDisabled(),true);
 await page.click('#prev');await page.waitForFunction(()=>normalRayAudit.retainedAudit.bodyCount<175);
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.processId==='retained-construction'&&normalRayAudit.proceduralStep===7);
 await page.selectOption('#process-select','new-construction');await page.waitForFunction(()=>normalRayAudit.processId==='new-construction');
 await page.selectOption('#process-select','retained-construction');await page.waitForFunction(()=>normalRayAudit.processId==='retained-construction'&&normalRayAudit.proceduralStep===7);
 assert.deepEqual(errors,[]);
 console.log('Process 4: one visible seed, monotone growth, backtracking, gate, migration and isolated saved progress passed');
}finally{await browser.close();await new Promise(r=>server.close(r));}
