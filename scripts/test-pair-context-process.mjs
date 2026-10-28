import assert from 'node:assert/strict';
import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import {chromium} from '@playwright/test';
const root=process.cwd();
const server=http.createServer(async(req,res)=>{
 try{const p=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);if(!p.startsWith(root+path.sep))throw Error('path');res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css'})[path.extname(p)]??'text/plain');res.end(await fs.readFile(p));}catch{res.statusCode=404;res.end();}
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;
try{
 browser=await chromium.launch();const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(`http://127.0.0.1:${server.address().port}/research/realization-tower/normal-ray.html`);
 await page.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().draws>0);
 await page.selectOption('#process-select','fibration-12x12');
 await page.waitForFunction(()=>normalRayAudit.processId==='fibration-12x12');
 await page.click('#next');await page.waitForFunction(()=>normalRayAudit.proceduralStep===1);
 await page.selectOption('#process-select','pair-context-7x4');
 await page.waitForFunction(()=>normalRayAudit.processId==='pair-context-7x4');
 assert.equal(await page.locator('#pair-context-audit').isVisible(),true);
 assert.equal(await page.evaluate(()=>normalRayAudit.pairContextAudit.position),1);
 assert.equal(await page.locator('#step').isDisabled(),true);
 await page.click('#reset-view');
 for(let i=1;i<28;i++){await page.click('#next');await page.waitForFunction(n=>normalRayAudit.proceduralStep===n,i);}
 assert.equal(await page.locator('#next').isDisabled(),true);
 assert.equal(await page.evaluate(()=>normalRayAudit.pairContextAudit.actionHistory.length),8);
 assert.deepEqual(await page.evaluate(()=>Object.keys(normalRayAudit.pairContextAudit.bank)),['aa','ab','ba','bb']);
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.processId==='pair-context-7x4'&&normalRayAudit.proceduralStep===27);
 await page.selectOption('#process-select','fibration-12x12');await page.waitForFunction(()=>normalRayAudit.processId==='fibration-12x12'&&normalRayAudit.proceduralStep===1);
 await page.selectOption('#process-select','pair-context-7x4');await page.waitForFunction(()=>normalRayAudit.processId==='pair-context-7x4'&&normalRayAudit.proceduralStep===27);
 await page.click('#prev');await page.waitForFunction(()=>normalRayAudit.proceduralStep===26);
 assert.deepEqual(errors,[]);console.log('Pair context process: 28 positions, bank, controls, persistence and fibration isolation passed');
}finally{await browser?.close();await new Promise(r=>server.close(r));}
