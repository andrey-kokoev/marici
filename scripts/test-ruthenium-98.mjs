// Legacy script/process ID retained for compatibility; the displayed item is 5-side oct.
import assert from 'node:assert/strict';
import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {chromium} from '@playwright/test';
const root=process.cwd(),server=http.createServer(async(req,res)=>{
 try{const p=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);if(!p.startsWith(root+path.sep))throw Error('path');res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css'})[path.extname(p)]??'text/plain');res.end(await fs.readFile(p));}catch{res.statusCode=404;res.end();}
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;
try{
 browser=await chromium.launch();const page=await browser.newPage(),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(`http://127.0.0.1:${server.address().port}/${process.argv[2]??'website/public/experiments/native-belt/index.html'}`);
 await page.waitForFunction(()=>globalThis.normalRayAudit);
 await page.selectOption('#process-select','ruthenium-98');
 await page.waitForFunction(()=>normalRayAudit.ruthenium98Audit?.template==='five-side-octahedron');
 assert.equal(await page.locator('#process-select option:checked').innerText(),'5-side oct');
 assert.equal(await page.locator('#ruthenium-98-view').inputValue(),'geometry');
 assert.equal(await page.evaluate(()=>normalRayAudit.presentationBodyCount),245);
 assert.equal(await page.evaluate(()=>normalRayAudit.surfaceCount),200);
 const counts=page.locator('#inventory-panel [data-count-row="oct5-cells"]');
 assert.deepEqual(await counts.locator('td').allTextContents(),['80','85','80','245']);
 await page.screenshot({path:path.join(os.tmpdir(),'five-side-oct-geometry.png')});
 await page.selectOption('#ruthenium-98-view','lattice');
 await page.waitForFunction(()=>normalRayAudit.graphMode&&normalRayAudit.graphNodeCount===245&&normalRayAudit.graphLinkCount===560);
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.processId==='ruthenium-98'&&normalRayAudit.graphMode);
 assert.equal(await page.locator('#ruthenium-98-view').inputValue(),'lattice');
 await page.selectOption('#ruthenium-98-view','wiring');
 await page.waitForFunction(()=>normalRayAudit.rutheniumWiringAudit?.status==='coherent-port-routing'&&!normalRayAudit.graphMode&&normalRayAudit.surfaceCount===200);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.inputFibres),80);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.outputFibres),80);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.slotWires),320);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.copiedBranches),0);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.occupiedNativeFaces),760);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.unwiredFillerSlots),0);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.rendered.retainedFibres),80);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.rendered.retainedSlotWires),320);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.geometricNCells),85);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.internalChannels),340);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.coherenceGroups),62);
 assert.equal(await page.evaluate(()=>normalRayAudit.rutheniumWiringAudit.rendered.internalChannels),340);
 await page.locator('#oct-inspect-interior').click();
 await page.waitForFunction(()=>document.querySelector('#face-opacity').value==='0.12');
 await page.screenshot({path:path.join(os.tmpdir(),'five-side-oct-wiring.png')});
 await page.selectOption('#oct-coherence-group','coherence:1');
 await page.waitForFunction(()=>normalRayAudit.rutheniumWiringAudit.selectedGroup==='coherence:1');
 await page.screenshot({path:path.join(os.tmpdir(),'five-side-oct-coherence-group.png')});
 await page.selectOption('#oct-coherence-group','all');
 await page.waitForFunction(()=>!normalRayAudit.rutheniumWiringAudit.selectedGroup);
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.rutheniumWiringAudit?.status==='coherent-port-routing');
 assert.equal(await page.locator('#ruthenium-98-view').inputValue(),'wiring');
 await page.selectOption('#ruthenium-98-view','geometry');await page.waitForFunction(()=>!normalRayAudit.graphMode&&normalRayAudit.surfaceCount===200);
 assert.deepEqual(errors,[]);
 console.log('5-side oct browser checks passed: octahedral geometry, 245 cells, 200 boundary faces, 560 lattice links, 340 internal N channels, 62 inspectable coherence groups, conservation, persistence.');
}finally{await browser?.close();await new Promise(r=>server.close(r));}
