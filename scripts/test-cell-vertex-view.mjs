import assert from 'node:assert/strict';
import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import {Vector3,Quaternion} from 'three';
import {chromium} from '@playwright/test';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
const root=process.cwd(),server=http.createServer(async(req,res)=>{
 try{const p=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);if(!p.startsWith(root+path.sep))throw Error('path');res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css'})[path.extname(p)]??'text/plain');res.end(await fs.readFile(p));}catch{res.statusCode=404;res.end();}
});
const near=(a,b)=>assert.ok(Math.abs(a-b)<1e-6,`${a} != ${b}`);
const sameCamera=(a,b)=>{for(const key of ['offset','targetOffset','up'])a[key].forEach((x,i)=>near(x,b[key][i]));near(a.zoom,b.zoom);};
const viewNormal=(snapshot,vertex)=>{
 const vertices=snapshot.vertices.map(v=>new Vector3(...worldPoint(v.address))),centre=vertices.reduce((s,v)=>s.add(v),new Vector3()).divideScalar(vertices.length);
 return vertices[vertex-1].clone().sub(centre).normalize().applyQuaternion(new Quaternion().fromArray(snapshot.view.quaternion).invert()).toArray();
};
await new Promise(r=>server.listen(0,'127.0.0.1',r));let browser;
try{
 browser=await chromium.launch();const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.addInitScript(()=>{const key='marici:isotope-constructor:v1:scene-settings';if(!localStorage.getItem(key))localStorage.setItem(key,JSON.stringify({version:1,process:{id:'cell-fibration',k:7,step:8},cut:{enabled:true,vertex:1,startLayer:0,layer:3},camera:{offset:[3,4,8],targetOffset:[.2,-.3,.1],up:[.2,1,.15],zoom:1.15}}));});
 await page.goto(`http://127.0.0.1:${server.address().port}/research/realization-tower/normal-ray.html`);
 await page.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().draws>0);
 assert.equal(await page.locator('select#cut-vertex').count(),0);
 assert.deepEqual(await page.locator('#cut-vertex button').allTextContents(),['All','P','N1','N2','E']);
 assert.deepEqual(await page.locator('#cut-vertex button').evaluateAll(bs=>bs.slice(1).map(b=>getComputedStyle(b).backgroundColor)),['rgb(18, 101, 168)','rgb(229, 234, 240)','rgb(229, 234, 240)','rgb(168, 38, 100)']);
 const snapshot=()=>page.evaluate(()=>NormalRayViewer.snapshot());
 const baseline=await snapshot();assert.ok(Math.abs(viewNormal(baseline,1)[2])<.99);
 let selected=1;
 async function change(to,keyboard=false){
  const before=await snapshot(),from=selected;
  const button=page.locator(`[data-cut-vertex="${to}"]`);
  if(keyboard){await button.focus();await page.keyboard.press('Enter');}else await button.click();
  await page.waitForFunction(n=>NormalRayViewer.snapshot().draws>n,before.draws);
  assert.equal(await button.getAttribute('aria-pressed'),'true');
  assert.equal(await page.locator('#cut-vertex button[aria-pressed="true"]').count(),1);
  const after=await snapshot();
  const cycle=[2,1,4,3],pair=(from===1&&to===4)||(from===4&&to===1)||(from===2&&to===3)||(from===3&&to===2),next=v=>pair?({1:4,4:1,2:3,3:2}[v]):cycle[(cycle.indexOf(v)+1)%cycle.length];
  const a=before.view.vertexLabels[from-1],b=after.view.vertexLabels[to-1];
  near(a.anchorX,b.anchorX);near(a.anchorY,b.anchorY);
  const oldNext=before.view.vertexLabels[next(from)-1],newNext=after.view.vertexLabels[next(to)-1];
  if(!((from===2&&to===1)||(from===1&&to===2))){near(oldNext.anchorX,newNext.anchorX);near(oldNext.anchorY,newNext.anchorY);}
  if(!((from===2&&to===1)||(from===1&&to===2)))viewNormal(before,from).forEach((x,i)=>near(x,viewNormal(after,to)[i]));
  near(before.view.zoom,after.view.zoom);
  near(Math.hypot(...before.view.camera.offset),Math.hypot(...after.view.camera.offset));
  near(Math.hypot(...before.view.camera.targetOffset),Math.hypot(...after.view.camera.targetOffset));
  assert.equal(after.process.proceduralStep,8);assert.equal(after.process.cellFibrationAudit.bodyCount,142);
  selected=to;return after;
 }
 await change(2);await change(1);sameCamera(baseline.view.camera,(await snapshot()).view.camera);
 for(const v of [3,4,2,1])await change(v);
 const beforeAll=await snapshot();await page.click('[data-cut-vertex="all"]');await page.waitForFunction(n=>NormalRayViewer.snapshot().draws>n,beforeAll.draws);
 sameCamera(beforeAll.view.camera,(await snapshot()).view.camera);
 await change(3);
 // Explicit vertex selection works even when drag rotation has an anchor.
 await page.locator('[data-lock-vertex="1"]').evaluate(el=>el.click());
 await page.waitForFunction(()=>NormalRayViewer.snapshot().view.vertexLocks.v1);
 await change(2);assert.equal((await snapshot()).view.vertexLocks.v1,true);
 const saved=(await snapshot()).view.camera;
 await page.reload();await page.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().draws>0);
 sameCamera(saved,(await snapshot()).view.camera);
 await change(4,true);
 await page.setViewportSize({width:390,height:844});
 assert.ok(await page.locator('#cut-vertex').evaluate(el=>el.scrollWidth<=el.clientWidth));
 assert.equal(await page.locator('#cut-vertex button:visible').count(),5);
 assert.equal(await page.locator('#cell-cut-controls input[type="number"]').count(),0);
 for(const group of ['#cut-start-layer','#cut-layer']){
  assert.deepEqual(await page.locator(group+' button').allTextContents(),['1','2','3','4','5','6','7']);
  assert.ok(await page.locator(group).evaluate(el=>el.scrollWidth<=el.clientWidth));
 }
 // The mobile scene pauses rendering while scrolled offscreen.
 await page.setViewportSize({width:1440,height:1000});await page.evaluate(()=>window.scrollTo(0,0));
 for(let n=0;n<7;n++){
  await page.click(`[data-cut-layer="${n}"]`);await page.click(`[data-cut-start-layer="${n}"]`);
  await page.waitForFunction(n=>normalRayAudit.cutAudit.startLayer===n&&normalRayAudit.cutAudit.layer===n,n);
  assert.equal(await page.locator('#cut-start-layer button[aria-pressed="true"]').innerText(),String(n+1));
  assert.equal(await page.locator('#cut-layer button[aria-pressed="true"]').innerText(),String(n+1));
 }
 await page.click('[data-cut-layer="2"]');await page.waitForFunction(()=>normalRayAudit.cutAudit.startLayer===2&&normalRayAudit.cutAudit.layer===2);
 await page.locator('[data-cut-start-layer="5"]').focus();await page.keyboard.press('Enter');
 await page.waitForFunction(()=>normalRayAudit.cutAudit.startLayer===5&&normalRayAudit.cutAudit.layer===5);
 await page.reload();await page.waitForFunction(()=>globalThis.normalRayAudit?.cutAudit?.startLayer===5&&normalRayAudit.cutAudit.layer===5);
 assert.equal(await page.locator('#cut-start-layer button[aria-pressed="true"]').innerText(),'6');
 assert.equal(await page.locator('#cut-layer button[aria-pressed="true"]').innerText(),'6');
 assert.deepEqual(errors,[]);
 console.log('Vertex selection preserves screen position, layer-normal angle, zoom and pan; All, locks and reload passed');
}finally{await browser?.close();await new Promise(r=>server.close(r));}
