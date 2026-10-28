import assert from 'node:assert/strict';
import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import {chromium} from '@playwright/test';
const root=process.cwd(),server=http.createServer(async(req,res)=>{try{const p=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);if(!p.startsWith(root+path.sep))throw Error('path');res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css'})[path.extname(p)]??'text/plain');res.end(await fs.readFile(p));}catch{res.statusCode=404;res.end();}});
await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;
try{
 browser=await chromium.launch();const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(`http://127.0.0.1:${server.address().port}/research/realization-tower/normal-ray.html`);
 await page.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().draws>0);
 await page.selectOption('#process-select','double-esd7');await page.waitForFunction(()=>normalRayAudit.processId==='double-esd7');
 assert.equal(await page.locator('#next').count(),0);assert.equal(await page.locator('#prev').count(),0);assert.equal(await page.locator('#apply-rule-closure').count(),0);
 assert.equal(await page.locator('#step').isVisible(),false);assert.equal(await page.locator('label[for="step"]').isVisible(),false);
 assert.equal(await page.locator('[data-double-rule]').count(),4);
 assert.equal(await page.locator('#rule-preview').getAttribute('open'),null);
 await page.locator('#rule-preview > summary').click();
 await page.uncheck('#rim-assembly');
 await page.waitForFunction(()=>document.querySelectorAll('#vertex-labels button').length===5);
 assert.deepEqual(await page.locator('#vertex-labels button').allTextContents(),['V₁ +N','V₂ +P','V₃ E','V₄ −N','V₅ −P']);
 await page.selectOption('#shape-view','wiring');await page.waitForFunction(()=>normalRayAudit.graphMode&&normalRayAudit.graphNodeCount===350);
 const rules=['P-branch','N-P','E-P','N-nonP'],totals=[18,172,222,350];
 for(let i=0;i<rules.length;i++){
  await page.check(`[data-double-rule="${rules[i]}"]`);
  await page.waitForFunction(n=>normalRayAudit.presentationBodyCount===n,totals[i]);
 }
 assert.equal(await page.locator('#process-view-help').count(),0);assert.equal(await page.locator('#instructions').count(),0);
 assert.equal(await page.locator('#internal-sector-experiment').count(),0);
 assert.equal(await page.locator('#internal-electron-self').count(),0);
 assert.equal(await page.locator('#double-esd7-audit summary').filter({hasText:'Transitions ('}).count(),0);
 assert.equal(await page.evaluate(()=>normalRayAudit.presentationBodyCount),350);
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.presentationBodyCount===350&&normalRayAudit.processId==='double-esd7');
 assert.equal(await page.locator('[data-double-rule]:checked').count(),4);
 await page.locator('#rule-preview > summary').click();
 await page.uncheck('[data-double-rule="E-P"]');await page.waitForFunction(()=>normalRayAudit.presentationBodyCount===172&&normalRayAudit.rulePreviewCount===178);
 assert.equal(await page.locator('[data-double-rule]:checked').count(),3);
 await page.check('#highlight-rule-preview');await page.waitForFunction(()=>normalRayAudit.highlightedRulePreviewCount===178);
 await page.check('[data-double-rule="E-P"]');await page.waitForFunction(()=>normalRayAudit.presentationBodyCount===350);
 await page.uncheck('[data-double-rule="P-branch"]');await page.waitForFunction(()=>normalRayAudit.presentationBodyCount===8);
 assert.equal(await page.locator('[data-double-rule]:checked').count(),3);
 await page.selectOption('#process-select','cell-fibration');await page.waitForFunction(()=>normalRayAudit.processId==='cell-fibration');assert.equal(await page.locator('#next').count(),1);
 await page.selectOption('#process-select','double-esd7');await page.waitForFunction(()=>normalRayAudit.wireframeBodyCount===342&&normalRayAudit.graphMode);
 await page.selectOption('#shape-view','geometry');await page.waitForFunction(()=>!normalRayAudit.graphMode);
 assert.deepEqual(errors,[]);console.log('Double ESD7: rule toggles, prerequisites, removal, persistence, preview and process isolation passed');
}finally{await browser?.close();await new Promise(r=>server.close(r));}
