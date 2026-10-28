import assert from 'node:assert/strict';
import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {chromium} from '@playwright/test';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const server=http.createServer(async(req,res)=>{
 try{const p=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);if(!p.startsWith(root+path.sep))throw Error('path');
 res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css'})[path.extname(p)]??'text/plain');res.end(await fs.readFile(p));
 }catch{res.statusCode=404;res.end();}
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));
let browser;
try{
 browser=await chromium.launch();
 const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(`http://127.0.0.1:${server.address().port}/research/realization-tower/normal-ray.html`);
 await page.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().draws>0);
 await page.selectOption('#process-select','from-center-cell');
 await page.waitForFunction(()=>normalRayAudit.processId==='from-center-cell');
 assert.equal(await page.locator('#center-interface-audit').isVisible(),true);
 assert.equal(await page.locator('#particle-counts').isVisible(),false);
 assert.equal(await page.locator('#step').isDisabled(),true);
 assert.equal(await page.evaluate(()=>normalRayAudit.presentationBodyCount),0);
 for(let step=1;step<=5;step++){
  await page.click('#next');await page.waitForFunction(s=>normalRayAudit.proceduralStep===s,step);
  assert.equal(await page.evaluate(()=>normalRayAudit.visibleLabels.length),step===1?1:step===5?13:5);
  assert.equal(await page.evaluate(()=>normalRayAudit.presentationAudit.fixedCellSize),true);
 }
 assert.equal(await page.locator('#next').isDisabled(),true);
 assert.match(await page.locator('#procedure').innerText(),/^Step 5/);
 assert.equal(await page.evaluate(()=>normalRayAudit.presentationAudit.arrowCells),8);
 await page.click('#prev');await page.waitForFunction(()=>normalRayAudit.proceduralStep===4);
 await page.click('#prev');await page.waitForFunction(()=>normalRayAudit.proceduralStep===3);
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.processId==='from-center-cell'&&normalRayAudit.proceduralStep===3);
 await page.selectOption('#process-select','retained-construction');await page.waitForFunction(()=>normalRayAudit.processId==='retained-construction');
 await page.selectOption('#process-select','from-center-cell');await page.waitForFunction(()=>normalRayAudit.processId==='from-center-cell'&&normalRayAudit.proceduralStep===3);
 await page.click('#next');await page.waitForFunction(()=>normalRayAudit.proceduralStep===4);
 await page.click('#next');await page.waitForFunction(()=>normalRayAudit.proceduralStep===5);
 await page.locator('#face-opacity').fill('0.4');
 await page.click('#zoom-in');await page.click('#zoom-in');
 await page.waitForTimeout(200);
 const out=path.join(root,'research/strominger/results/center-interface-viewer');await fs.mkdir(out,{recursive:true});
 await page.screenshot({path:path.join(out,'typed-arrow-cells.png')});
 await page.click('#role-label-toggles');await page.waitForFunction(()=>normalRayAudit.visibleLabels.length===0);
 assert.deepEqual(errors,[]);
 console.log('Center-interface viewer: six numbered fixed-size stages, backtracking, persistence, isolated progress, labels and opacity passed. Screenshot: research/strominger/results/center-interface-viewer/typed-arrow-cells.png');
}finally{await browser?.close();await new Promise(r=>server.close(r));}
