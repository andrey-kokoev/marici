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
 await page.addInitScript(()=>{
  const key='marici:isotope-constructor:v1:scene-settings';
  if(!localStorage.getItem(key))localStorage.setItem(key,JSON.stringify({version:1,process:{id:'cell-fibration',k:7,step:3},appearance:{faceOpacity:.37}}));
 });
 await page.goto(`http://127.0.0.1:${server.address().port}/research/realization-tower/normal-ray.html`);
 await page.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().draws>0&&normalRayAudit.presentationBodyCount===44);
 const faces=await page.evaluate(()=>normalRayAudit.surfaceCount),counts=await page.locator('[data-count-row="total"] td').allTextContents();
 assert.ok(faces>0);
 await page.check('#edges-only');await page.waitForFunction(()=>normalRayAudit.edgesOnly&&normalRayAudit.surfaceCount===0&&NormalRayViewer.snapshot().transparency==='edges-only');
 assert.equal(await page.evaluate(()=>normalRayAudit.cellEdgeObjects),44);
 assert.equal(await page.evaluate(()=>normalRayAudit.cellEdgeWidth),3);
 assert.equal(await page.evaluate(()=>NormalRayViewer.snapshot().faceOpacity),.37);
 assert.equal(await page.locator('#face-opacity').isDisabled(),true);
 assert.deepEqual(await page.locator('[data-count-row="total"] td').allTextContents(),counts);
 await fs.mkdir('research/strominger/results/cell-fibration-viewer',{recursive:true});
 await page.screenshot({path:'research/strominger/results/cell-fibration-viewer/edges-only.png'});
 await page.click('[data-cut-vertex="all"]');await page.click('[data-cut-layer="2"]');await page.click('[data-cut-start-layer="2"]');await page.check('#cut-enabled');
 await page.waitForFunction(()=>normalRayAudit.presentationBodyCount===24&&normalRayAudit.cellEdgeObjects===28);
 assert.equal(await page.evaluate(()=>normalRayAudit.surfaceCount),0);
 await page.click('#zoom-in');await page.setViewportSize({width:1100,height:800});
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.edgesOnly&&normalRayAudit.presentationBodyCount===24&&NormalRayViewer.snapshot().draws>0);
 assert.equal(await page.locator('#edges-only').isChecked(),true);
 assert.equal(await page.evaluate(()=>NormalRayViewer.snapshot().faceOpacity),.37);
 await page.uncheck('#bodies');await page.waitForFunction(()=>normalRayAudit.cellEdgeObjects===0);
 assert.equal(await page.evaluate(()=>normalRayAudit.surfaceCount),0);
 await page.check('#bodies');await page.waitForFunction(()=>normalRayAudit.cellEdgeObjects===28);
 await page.uncheck('#edges-only');await page.waitForFunction(()=>!normalRayAudit.edgesOnly&&normalRayAudit.surfaceCount>0);
 assert.equal(await page.locator('#face-opacity').isDisabled(),false);
 assert.equal(await page.locator('#face-opacity').inputValue(),'0.37');
 await page.click('#clear-cut');await page.waitForFunction(()=>normalRayAudit.presentationBodyCount===44);
 assert.equal(await page.evaluate(()=>normalRayAudit.surfaceCount),faces);
 assert.deepEqual(await page.locator('[data-count-row="total"] td').allTextContents(),counts);
 assert.deepEqual(errors,[]);
 console.log('Edges-only: thick outlines, no face batch/compositing, unchanged counts, cuts, resize, body visibility, persistence, and opacity restoration passed');
}finally{await browser?.close();await new Promise(r=>server.close(r));}
