import assert from 'node:assert/strict';
import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from '@playwright/test';
import { prepareNormalRay } from './prepare-normal-ray.mjs';
import { testFaceCompositor } from './test-normal-ray-transparency.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
await prepareNormalRay(root);
const server=http.createServer(async(req,res)=>{
 try{
  const p=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));
  if(!p.startsWith(root+path.sep))throw Error('path');
  const data=await fs.readFile(p);res.setHeader('Content-Type',({'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json'})[path.extname(p)]||'application/octet-stream');res.end(data);
 }catch{res.statusCode=404;res.end('Not found');}
});
await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
const url=`http://127.0.0.1:${server.address().port}/research/realization-tower/normal-ray.html`;
const browser=await chromium.launch();
const near=(a,b)=>assert(Math.abs(a-b)<1e-7);
async function page(options={}){
 const p=await browser.newPage(options);p.errors=[];p.on('pageerror',e=>p.errors.push(e.message));
 await p.route('**/*',r=>new URL(r.request().url()).hostname==='127.0.0.1'?r.continue():r.abort());return p;
}
async function ready(p){await p.goto(url);await p.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().draws>0);}
async function castAt(p,k,stage){
 await p.locator('#step').fill(String(k));
 await p.waitForFunction(k=>normalRayAudit.k===k,k);
 const shape=await p.evaluate(()=>NormalRayViewer.snapshot());
 assert.deepEqual(shape.vertices[0].address,[-5,2,2,2]);
 for(let i=1;i<4;i++)assert.deepEqual(shape.vertices[i].address,[-5,2,2,2].map((x,j)=>x+(j===0?k:j===i?-k:0)));
 let current=await p.evaluate(()=>normalRayAudit.proceduralStep);
 while(current!==stage){const next=current+(current<stage?1:-1);await p.locator(current<stage?'#next':'#prev').click();await p.waitForFunction(n=>normalRayAudit.proceduralStep===n,next);current=next;}
}
try{
 const p=await page({viewport:{width:1400,height:950}});await ready(p);await p.waitForTimeout(200);
 assert(await p.evaluate(()=>{
  const s=NormalRayViewer.snapshot(),k=s.process.k;
  return s.vertices.every((v,i)=>v.address.every((x,j)=>x===([-5,2,2,2][j]+(i===0?0:j===0?k:j===i?-k:0))));
 }));
 assert.equal(await p.locator('#role-label-toggles').isVisible(),true);
 let snap=await p.evaluate(()=>NormalRayViewer.snapshot());assert.equal(snap.view.projection,'OrthographicCamera');near(snap.view.azimuth,67);near(snap.view.elevation,-68);near(snap.view.frustum[2]/(snap.view.frustum[2]-snap.view.frustum[3]),.625);
 await p.waitForTimeout(250);assert.equal((await p.evaluate(()=>NormalRayViewer.snapshot())).draws,snap.draws);
 await p.locator('#step').fill('3');await p.waitForFunction(()=>JSON.parse(localStorage.getItem('marici:isotope-constructor:v1:scene-settings')).k===3);
 await p.waitForFunction(()=>normalRayAudit.proceduralStep===0);assert.equal(await p.evaluate(()=>normalRayAudit.firstRay),null);
 await p.reload();await p.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().draws>0);
 assert.equal(await p.evaluate(()=>normalRayAudit.firstRay),null);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.shownCells),[await p.evaluate(()=>normalRayAudit.seed)]);
 assert.equal(await p.locator('#step').inputValue(),'3');assert.equal(await p.evaluate(()=>normalRayAudit.k),3);
 assert.equal(await p.locator('#process-select').inputValue(),'new-construction');assert(await p.locator('#next').isEnabled());
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments.map(a=>a.role)),['electron']);
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.proceduralStep===1);
 assert.equal(await p.evaluate(()=>normalRayAudit.firstRay.id),'ray13');
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments.map(a=>a.role)),['electron','proton']);
 assert(await p.evaluate(()=>normalRayAudit.filledCells.includes(normalRayAudit.endingCell)));
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.proceduralStep===2);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.rays.map(r=>r.id)),['ray32']);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments.map(a=>a.role)),['electron','proton','neutron']);
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.proceduralStep===3);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.rays.map(r=>r.id)),['ray32','ray21']);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments.map(a=>a.role)),['electron','proton','neutron']);
 await castAt(p,4,4);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.edgeMeeting.cells),[331,332,333,334]);
 assert(await p.evaluate(()=>normalRayAudit.edgeMeeting.cells.every(id=>normalRayAudit.filledCells.includes(id)&&normalRayAudit.assignments.some(a=>a.cell===id&&a.role==='neutron'))));
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.edgeFronts.map(r=>r.id)),['ray13','ray31']);
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.proceduralStep===5);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments.slice(-2).map(a=>[a.cell,a.role])),[[341,'proton'],[311,'electron']]);
 assert(await p.evaluate(()=>normalRayAudit.faceNeighbors.every(n=>normalRayAudit.filledCells.includes(n.cell)&&n.exteriorFaces.length>0)));
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.proceduralStep===6);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments.slice(-4).map(a=>a.cell)),[340,342,312,314]);
 assert(await p.evaluate(()=>!normalRayAudit.assignments.some(a=>[339,313].includes(a.cell))));
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.proceduralStep===7);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments.slice(-4).map(a=>a.cell)),[131,133,118,121]);
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.proceduralStep===8);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments.slice(-2).map(a=>[a.cell,a.role])),[[313,'neutron'],[339,'neutron']]);
 assert(await p.evaluate(()=>[339,313].every(id=>normalRayAudit.filledCells.includes(id))));
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.proceduralStep===9);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments.slice(-2).map(a=>a.cell)),[58,60]);
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.surfacePropagationVisible);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.surfaceRays.map(r=>r.id)),['meeting-to-V2','meeting-to-V4']);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.dottedRayIds),['meeting-to-V2','meeting-to-V4']);
 assert(await p.evaluate(()=>normalRayAudit.surfaceRays.every(r=>r.surfaceCells.every(c=>normalRayAudit.filledCells.includes(c.cell)&&normalRayAudit.assignments.some(a=>a.cell===c.cell&&a.role==='neutron')))));
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.baseEdgeVisible);
 assert.equal(await p.evaluate(()=>normalRayAudit.proceduralStep),11);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.baseEdgeRays.map(r=>r.id)),['ray24','ray42']);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.dottedRayIds),['meeting-to-V2','meeting-to-V4','ray24','ray42']);
 assert(await p.evaluate(()=>[116,120,122,124].every(id=>normalRayAudit.filledCells.includes(id)&&normalRayAudit.assignments.some(a=>a.cell===id&&a.role==='neutron'))));
 const beforeRay34=await p.evaluate(()=>normalRayAudit.assignments);
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.ray34Visible);
 assert.equal(await p.evaluate(()=>normalRayAudit.proceduralStep),12);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.ray34.contacts.map(c=>normalRayAudit.assignments.find(a=>a.cell===c.cell).role)),['proton','neutron','electron','neutron']);
 assert.deepEqual((await p.evaluate(()=>normalRayAudit.assignments)).slice(0,beforeRay34.length),beforeRay34);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.edge34Predecessors.map(c=>[c.cell,c.electron])),[[308,117]]);
 assert.equal(await p.evaluate(()=>normalRayAudit.ray14),null);
 assert(await p.locator('#next').isEnabled());
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.ray14Visible);
 assert.equal(await p.evaluate(()=>normalRayAudit.proceduralStep),13);
 assert.equal(await p.evaluate(()=>normalRayAudit.ray14.id),'ray14');
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.edge14Assignments.map(a=>a.role)),['electron','neutron','proton','neutron']);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.edge14Predecessors.map(c=>[c.cell,c.proton])),[[328,125]]);
 assert(await p.evaluate(()=>[328,125].every(id=>normalRayAudit.filledCells.includes(id))));
 assert(await p.evaluate(()=>normalRayAudit.filledCells.includes(308)&&normalRayAudit.assignments.some(a=>a.cell===308&&a.role==='proton')));
 assert(await p.evaluate(()=>!normalRayAudit.rays.some(r=>r.id==='ray12')));
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.ray12Visible);
 assert.equal(await p.evaluate(()=>normalRayAudit.proceduralStep),14);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.edge12Assignments.map(a=>a.role)),['electron','neutron','proton','neutron']);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.edge12Predecessors.map(c=>[c.cell,c.proton])),[[338,130]]);
 assert(await p.evaluate(()=>[338,130].every(id=>normalRayAudit.filledCells.includes(id))));
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.ray32PatternVisible);
 assert.equal(await p.evaluate(()=>normalRayAudit.proceduralStep),15);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.edge32Assignments.map(a=>a.role)),['proton','neutron','electron','neutron']);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.edge32Predecessors.map(c=>[c.cell,c.electron])),[[322,123]]);
 assert(await p.evaluate(()=>[322,123].every(id=>normalRayAudit.filledCells.includes(id))));
 assert.equal(await p.evaluate(()=>normalRayAudit.rays.filter(r=>r.id==='ray32').length),1);
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.proceduralStep===16);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.patternClosureRounds[0].map(c=>c.cell)),[309,321,327,335]);
 assert(await p.evaluate(()=>[309,321,327,335].every(id=>normalRayAudit.filledCells.includes(id)&&normalRayAudit.assignments.some(a=>a.cell===id&&a.role==='neutron'))));
 assert.equal(await p.evaluate(()=>normalRayAudit.nextPatternClosure.length),6);
 for(const step of [17,18,19]){await p.locator('#next').click();await p.waitForFunction(step=>normalRayAudit.proceduralStep===step,step);}
 assert(await p.evaluate(()=>normalRayAudit.baseNeutronPassVisible));
 assert(await p.evaluate(()=>normalRayAudit.baseNeutronPass.contacts.every(c=>normalRayAudit.filledCells.includes(c.cell)&&normalRayAudit.assignments.some(a=>a.cell===c.cell&&a.role==='neutron'))));
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.edgeVertexFillVisible);
 assert.equal(await p.evaluate(()=>normalRayAudit.proceduralStep),20);
 assert.equal(await p.evaluate(()=>normalRayAudit.edgeVertexNeutrons.length),4);
 assert(await p.evaluate(()=>normalRayAudit.edgeVertexNeutrons.every(c=>normalRayAudit.filledCells.includes(c.cell)&&normalRayAudit.assignments.some(a=>a.cell===c.cell&&a.role==='neutron'))));
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.median3To24Visible);
 assert.equal(await p.evaluate(()=>normalRayAudit.proceduralStep),21);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.faceMedianRays.map(r=>r.id)),['ray3-24']);
 assert(await p.evaluate(()=>normalRayAudit.assignments.some(a=>a.cell===26&&a.role==='proton')));
 await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.median1To24Visible);
 assert.equal(await p.evaluate(()=>normalRayAudit.proceduralStep),22);
 assert.deepEqual(await p.evaluate(()=>normalRayAudit.faceMedianRays.map(r=>r.id)),['ray3-24','ray1-24']);
 assert(await p.evaluate(()=>normalRayAudit.assignments.some(a=>a.cell===128&&a.role==='electron')));
 const newProcessAssignments=await p.evaluate(()=>normalRayAudit.assignments);
 assert(await p.locator('#next').isDisabled());
 await p.locator('#process-select').selectOption('edge-ray');await p.waitForFunction(()=>normalRayAudit.processId==='edge-ray');
 await p.locator('#next').click();
 for(let k=1;k<=7;k++){await castAt(p,k,2);await p.waitForFunction(k=>normalRayAudit.k===k&&normalRayAudit.proceduralStep===2,k);assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments.map(a=>a.role)),k>=2?['electron','proton']:[]);}
 await p.locator('#next').click();
 assert.equal(await p.locator('input[name="second-edge"]').count(),0);
 for(const branch of [1]){
  for(let k=1;k<=7;k++){
   await castAt(p,k,3);
   await p.waitForFunction(({k,branch})=>normalRayAudit.k===k&&normalRayAudit.secondRay?.branch===branch,{k,branch});
   const audit=await p.evaluate(()=>normalRayAudit),ray=audit.secondRay;
   assert.deepEqual(ray.start,audit.rayEndpoint);assert.equal(ray.length,k);
   assert.deepEqual(ray.end,ray.start.map((x,i)=>x+k*ray.direction[i]));
   assert.deepEqual(audit.assignments.filter(a=>a.role==='neutron').map(a=>a.cell),[ray.cell]);
   if(k>=2)assert(audit.emptySecondCells.length>0);
   assert.deepEqual([...audit.filledCells].sort((a,b)=>a-b),[...new Set([audit.seed,audit.endingCell,ray.cell])].sort((a,b)=>a-b));
  }
 }
 for(let stage=4;stage<=9;stage++){
  await p.locator('#next').click();
  for(let k=1;k<=7;k++){
   await castAt(p,k,stage);await p.waitForFunction(({k,stage})=>normalRayAudit.k===k&&normalRayAudit.proceduralStep===stage,{k,stage});
   const audit=await p.evaluate(()=>normalRayAudit),ray=audit.rays.at(-1);
   assert.equal(audit.rays.length,Math.min(stage,6)-2);
   assert.equal(audit.faceNeighbors.length,stage>=7&&k>=2?2:0);
   assert.equal(audit.partners.length,stage>=7&&k>=2?4:0);
   for(const n of audit.faceNeighbors){assert(audit.shownCells.includes(n.cell));assert(audit.filledCells.includes(n.cell));assert.equal(audit.assignments.find(a=>a.cell===n.cell).role,n.role==='electron'?'proton':'electron');}assert.equal(ray.length,k);
   assert.deepEqual(audit.assignments.filter(a=>a.role==='neutron').map(a=>a.cell),k===1?[audit.secondRay.cell,audit.thirdRay.cell]:[...new Set([audit.secondRay.cell,audit.thirdRay.cell,...audit.neutronNeighbors.map(n=>n.cell),...audit.surfaceNeutronNeighbors.map(n=>n.cell)])]);
   assert.equal(audit.neutronNeighbors.length,stage>=8&&k>=2?4:0);
   for(const n of audit.neutronNeighbors)assert(audit.filledCells.includes(n.cell));
   assert.equal(audit.surfaceNeutronNeighbors.length,stage===9&&k>=2?4:0);
   for(const n of audit.surfaceNeutronNeighbors)assert(audit.filledCells.includes(n.cell));
   assert.deepEqual(ray.end,ray.start.map((x,i)=>x+k*ray.direction[i]));
  }
 }
 await p.locator('#next').click();
 for(let k=1;k<=7;k++){
  await castAt(p,k,10);
  const audit=await p.evaluate(()=>normalRayAudit);
  for(const round of audit.closureRounds)for(const c of round){assert(audit.filledCells.includes(c.cell));assert.equal(audit.assignments.find(a=>a.cell===c.cell).role,'neutron');}
  assert.equal(await p.locator('#next').isDisabled(),false);
  if(k===3){await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.proceduralStep===11);}
  const prior=await p.evaluate(()=>normalRayAudit.assignments);
  await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.comparisonVisible);
  assert.equal(await p.locator('#next').isDisabled(),!(await p.evaluate(()=>normalRayAudit.mediationAvailable)));
  assert.deepEqual((await p.evaluate(()=>normalRayAudit.assignments)).slice(0,prior.length),prior);
  assert.equal(await p.evaluate(()=>normalRayAudit.faceVertexComparisons.length),k===1?0:2);
  if(k===4){
   assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments.filter(a=>a.boundary==='face-vertex').map(a=>[a.cell,a.role])),[[132,'electron'],[127,'proton']]);
   assert(await p.evaluate(()=>[132,127].every(id=>normalRayAudit.filledCells.includes(id)&&normalRayAudit.visibleLabels.some(a=>a.cell===id))));
  }
  if(k>=4){
   await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.mediationVisible);
   const a=await p.evaluate(()=>normalRayAudit);
   assert((await p.evaluate(()=>NormalRayViewer.snapshot().calls))<100,'Ray lines, cell outlines and translucent faces must stay batched');
   assert(a.signalConnections.length>0);assert.deepEqual(a.mediation.reversePaths,a.mediation.paths.map(path=>[...path].reverse()));
   assert(a.mediation.fillerCells.every(id=>a.filledCells.includes(id)&&a.assignments.some(x=>x.cell===id&&x.role==='neutron')));
   assert.equal(await p.locator('#next').isDisabled(),a.nextClosure.length===0);
   if(k===4){
    await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.proceduralStep===13);
    assert.deepEqual(await p.evaluate(()=>normalRayAudit.postMediationRounds[0].map(c=>c.cell)),[58,60]);
    assert(await p.evaluate(()=>[58,60].every(id=>normalRayAudit.filledCells.includes(id)&&normalRayAudit.assignments.some(x=>x.cell===id&&x.role==='neutron'))));
    assert(await p.locator('#next').isEnabled());
    await p.locator('#next').click();await p.waitForFunction(()=>normalRayAudit.surfaceContinuationVisible);
    assert.deepEqual(await p.evaluate(()=>normalRayAudit.surfaceContinuations.map(c=>[c.cell,c.role])),[[329,'electron'],[337,'electron'],[307,'proton'],[319,'proton']]);
    assert(await p.evaluate(()=>[329,337,307,319].every(id=>normalRayAudit.filledCells.includes(id))));
    assert(await p.evaluate(()=>!normalRayAudit.assignments.some(a=>[128,26].includes(a.cell))));
    assert(await p.locator('#next').isDisabled());
    const saved=await p.evaluate(()=>normalRayAudit.assignments);
    await p.locator('#process-select').selectOption('new-construction');await p.waitForFunction(()=>normalRayAudit.processId==='new-construction');
    assert.equal(await p.evaluate(()=>normalRayAudit.proceduralStep),22);
    assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments),newProcessAssignments);assert(await p.locator('#next').isDisabled());
    await p.locator('#process-select').selectOption('edge-ray');await p.waitForFunction(()=>normalRayAudit.processId==='edge-ray'&&normalRayAudit.proceduralStep===14);
    assert.deepEqual(await p.evaluate(()=>normalRayAudit.assignments),saved);
   }
  }
  await castAt(p,k,10);
 }
 const labelGeometry=await p.evaluate(()=>({shown:normalRayAudit.shownCells,filled:normalRayAudit.filledCells,assignments:normalRayAudit.assignments}));
 const toggle=p.locator('#role-label-toggles');await toggle.click();
 await p.waitForFunction(()=>normalRayAudit.visibleLabels.length===0);
 assert.equal(await toggle.getAttribute('aria-pressed'),'false');
 assert(await toggle.isVisible()); // It must remain available to restore hidden labels.
 assert.equal(await p.locator('[data-label-role]').count(),0);
 assert.deepEqual(await p.evaluate(()=>({shown:normalRayAudit.shownCells,filled:normalRayAudit.filledCells,assignments:normalRayAudit.assignments})),labelGeometry);
 await toggle.click();await p.waitForFunction(()=>['proton','neutron','electron'].every(role=>normalRayAudit.visibleLabels.some(a=>a.role===role)));
 const resetBox=await p.locator('#viewport-reset').boundingBox(),sceneBox=await p.locator('#scene').boundingBox(),togglesBox=await p.locator('#role-label-toggles').boundingBox();
 assert(resetBox.x>sceneBox.x+sceneBox.width/2);assert(togglesBox.y>=resetBox.y+resetBox.height);
 await p.locator('#step').fill('3');await p.waitForFunction(()=>normalRayAudit.k===3&&normalRayAudit.proceduralStep===10);
 const direct=await p.evaluate(()=>({shown:normalRayAudit.shownCells,filled:[...normalRayAudit.filledCells].sort((a,b)=>a-b)}));
 for(let stage=9;stage>=1;stage--){await p.locator('#prev').click();await p.waitForFunction(stage=>normalRayAudit.proceduralStep===stage,stage);}
 for(let stage=2;stage<=10;stage++){await p.locator('#next').click();await p.waitForFunction(stage=>normalRayAudit.proceduralStep===stage,stage);}
 assert.deepEqual(await p.evaluate(()=>({shown:normalRayAudit.shownCells,filled:[...normalRayAudit.filledCells].sort((a,b)=>a-b)})),direct);
 for(let stage=9;stage>=2;stage--){await p.locator('#prev').click();await p.waitForFunction(stage=>normalRayAudit.proceduralStep===stage,stage);}
 assert.equal(await p.evaluate(()=>normalRayAudit.secondRay),null);
 const geometry=await p.evaluate(()=>NormalRayViewer.snapshot().rebuilds);await p.locator('#opacity').focus();await p.keyboard.press('ArrowRight');await p.waitForTimeout(100);assert.equal(await p.evaluate(()=>NormalRayViewer.snapshot().rebuilds),geometry);
 const faceState=await p.evaluate(()=>({assignments:normalRayAudit.assignments,labels:normalRayAudit.visibleLabels,rebuilds:NormalRayViewer.snapshot().rebuilds}));
 for(const value of [0,.35,1,.78]){
  await p.locator('#face-opacity').fill(String(value));await p.waitForFunction(value=>NormalRayViewer.snapshot().faceOpacity===value,value);await p.waitForTimeout(80);
  assert.deepEqual(await p.evaluate(()=>({assignments:normalRayAudit.assignments,labels:normalRayAudit.visibleLabels,rebuilds:NormalRayViewer.snapshot().rebuilds})),faceState);
 }
 const q=await p.evaluate(()=>normalRayViewAudit.quaternion);
 for(const a of [1,2])await p.locator(`[data-lock-vertex="${a}"]`).click();await p.waitForTimeout(100);
 (await p.evaluate(()=>normalRayViewAudit.quaternion)).forEach((v,i)=>near(v,q[i]));
 const anchors=await p.evaluate(()=>normalRayViewAudit.vertexLabels.slice(0,2));
 await p.getByRole('button',{name:'Rotate up',exact:true}).click();await p.waitForTimeout(100);
 assert.notDeepEqual(await p.evaluate(()=>normalRayViewAudit.quaternion),q);
 (await p.evaluate(()=>normalRayViewAudit.vertexLabels.slice(0,2))).forEach((v,i)=>{near(v.anchorX,anchors[i].anchorX);near(v.anchorY,anchors[i].anchorY);});
 await p.locator('[data-lock-vertex="3"]').click();await p.waitForTimeout(100);
 const frozen=await p.evaluate(()=>normalRayViewAudit.quaternion);
 await p.getByRole('button',{name:'Rotate left',exact:true}).click();await p.waitForTimeout(100);
 (await p.evaluate(()=>normalRayViewAudit.quaternion)).forEach((v,i)=>near(v,frozen[i]));
 await p.locator('#reset-view').click();await p.waitForTimeout(100);assert.deepEqual(await p.evaluate(()=>normalRayViewAudit.vertexLocks),{v1:false,v2:false,v3:false,v4:false});
 const before=await p.evaluate(()=>normalRayViewAudit.quaternion);await p.getByRole('button',{name:'Roll left',exact:true}).focus();await p.keyboard.press('Enter');await p.waitForTimeout(100);assert.notDeepEqual(await p.evaluate(()=>normalRayViewAudit.quaternion),before);
 await p.locator('#zoom-in').click();await p.waitForTimeout(100);assert((await p.evaluate(()=>normalRayViewAudit.zoom))>1);
 await p.locator('#close-process').click();await p.locator('#close-scene').click();assert.equal(await p.locator('#scene').evaluate(e=>e.clientWidth),1400);await p.locator('#open-process').click();await p.locator('#open-scene').click();
 await p.locator('#auto-rotate').check();await p.waitForTimeout(200);await p.emulateMedia({reducedMotion:'reduce'});await p.waitForFunction(()=>normalRayViewAudit.autoRotate===false);
 await p.locator('#auto-rotate').check();await p.waitForTimeout(100);await p.locator('#scene').evaluate(e=>e.style.transform='translateX(-5000px)');await p.waitForTimeout(200);const stopped=await p.evaluate(()=>NormalRayViewer.snapshot().draws);await p.waitForTimeout(200);assert.equal(await p.evaluate(()=>NormalRayViewer.snapshot().draws),stopped);await p.locator('#scene').evaluate(e=>e.style.transform='');await p.waitForFunction(n=>NormalRayViewer.snapshot().draws>n,stopped);
 await p.locator('#auto-rotate').uncheck();await p.waitForTimeout(100);await p.evaluate(()=>NormalRayViewer.unmount());assert(await p.locator('#fallback').isVisible());assert.equal(await p.locator('.webgl-canvas').count(),0);assert.deepEqual(p.errors,[]);await p.close();
 const mobile=await page({viewport:{width:390,height:844}});await ready(mobile);assert(await mobile.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));assert((await mobile.locator('.webgl-canvas').boundingBox()).width>0);assert.deepEqual(mobile.errors,[]);await mobile.close();
 const persistedLabels=await page();await ready(persistedLabels);
 assert.equal(await persistedLabels.locator('#face-opacity').inputValue(),'1');
 for(const value of [0,.42,1]){
  await persistedLabels.locator('#face-opacity').fill(String(value));await persistedLabels.waitForFunction(value=>JSON.parse(localStorage.getItem('marici:isotope-constructor:v1:scene-settings')).appearance.faceOpacity===value,value);
  await ready(persistedLabels);assert.equal(await persistedLabels.locator('#face-opacity').inputValue(),String(value));assert.equal(await persistedLabels.evaluate(()=>NormalRayViewer.snapshot().faceOpacity),value);
 }
 await persistedLabels.locator('#role-label-toggles').click();await persistedLabels.waitForFunction(()=>JSON.parse(localStorage.getItem('marici:isotope-constructor:v1:scene-settings')).appearance.labels===false&&normalRayAudit.visibleLabels.length===0);
 await ready(persistedLabels);assert.equal(await persistedLabels.locator('#role-label-toggles').getAttribute('aria-pressed'),'false');assert.deepEqual(await persistedLabels.evaluate(()=>normalRayAudit.visibleLabels),[]);
 await persistedLabels.locator('#role-label-toggles').click();await persistedLabels.waitForFunction(()=>JSON.parse(localStorage.getItem('marici:isotope-constructor:v1:scene-settings')).appearance.labels===true&&normalRayAudit.visibleLabels.length>0);
 await ready(persistedLabels);assert.equal(await persistedLabels.locator('#role-label-toggles').getAttribute('aria-pressed'),'true');assert((await persistedLabels.evaluate(()=>normalRayAudit.visibleLabels.length))>0);assert.deepEqual(persistedLabels.errors,[]);await persistedLabels.close();
 const savedScene=await page({viewport:{width:1400,height:950}});await ready(savedScene);
 await savedScene.locator('#grid').uncheck();await savedScene.locator('#opacity').fill('0.24');await savedScene.locator('#face-opacity').fill('0.6');await savedScene.locator('#prior').check();await savedScene.locator('#bodies').uncheck();
 await savedScene.locator('#azimuth').fill('41');await savedScene.locator('#elevation').fill('22');await savedScene.getByRole('button',{name:'Roll right',exact:true}).click();await savedScene.locator('#zoom-in').click();
 const canvasBox=await savedScene.locator('.webgl-canvas').boundingBox();await savedScene.mouse.move(canvasBox.x+canvasBox.width/2,canvasBox.y+canvasBox.height/2);await savedScene.mouse.down({button:'right'});await savedScene.mouse.move(canvasBox.x+canvasBox.width/2+35,canvasBox.y+canvasBox.height/2+15,{steps:5});await savedScene.mouse.up({button:'right'});
 // The pan/roll can move V2 off-screen; persistence must use a visible anchor.
 const savedVertex=await savedScene.locator('[data-lock-vertex]:visible').first().getAttribute('data-lock-vertex');
 await savedScene.locator(`[data-lock-vertex="${savedVertex}"]`).click();await savedScene.locator('#rotation-speed').fill('0');await savedScene.locator('#auto-rotate').check();
 for(const name of ['Appearance','View direction & rotation','Motion'])await savedScene.locator('summary').filter({hasText:name}).click();
 await savedScene.locator('#close-process').click();await savedScene.locator('#close-scene').click();await savedScene.waitForTimeout(400);
 const savedCamera=await savedScene.evaluate(()=>normalRayViewAudit.camera);assert(savedCamera.targetOffset.some(x=>Math.abs(x)>1e-6));
 await ready(savedScene);
 assert(await savedScene.locator('#open-scene').isVisible());assert(await savedScene.locator('#open-process').isVisible());
 const restoredCamera=await savedScene.evaluate(()=>normalRayViewAudit.camera);for(const key of ['offset','targetOffset','up'])restoredCamera[key].forEach((x,i)=>near(x,savedCamera[key][i]));near(restoredCamera.zoom,savedCamera.zoom);
 await savedScene.locator('#open-scene').click();assert.equal(await savedScene.locator('details[open]').count(),0);
 for(const name of ['Appearance','View direction & rotation','Motion'])await savedScene.locator('summary').filter({hasText:name}).click();
 assert(!(await savedScene.locator('#grid').isChecked()));assert.equal(await savedScene.locator('#opacity').inputValue(),'0.24');assert.equal(await savedScene.locator('#face-opacity').inputValue(),'0.6');assert(await savedScene.locator('#prior').isChecked());assert(!(await savedScene.locator('#bodies').isChecked()));assert(await savedScene.locator('#auto-rotate').isChecked());assert.equal(await savedScene.locator('#rotation-speed').inputValue(),'0');assert.equal(await savedScene.locator(`[data-lock-vertex="${savedVertex}"]`).getAttribute('aria-pressed'),'true');
 assert.deepEqual(savedScene.errors,[]);await savedScene.close();
 const edgeClosure=await page();await ready(edgeClosure);await castAt(edgeClosure,7,16);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.nextEdgeClosure.length),14);
 assert.deepEqual(await edgeClosure.evaluate(()=>[normalRayAudit.ray34,normalRayAudit.ray14,normalRayAudit.ray12,normalRayAudit.ray32Pattern].map(r=>[r.diamonds.length,r.blockedDiamonds.length])),[[2,0],[2,0],[2,0],[2,0]]);
 assert.deepEqual(await edgeClosure.evaluate(()=>[63,104,115,85,140,220,266,214].map(id=>normalRayAudit.assignments.find(a=>a.cell===id)?.role)),['electron','proton','proton','electron','neutron','neutron','neutron','neutron']);
 for(const [step,count] of [[17,14],[18,8],[19,4]]){
  const previous=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
  await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(step=>normalRayAudit.proceduralStep===step,step);
  assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.edgeClosureRounds.at(-1).length),count);
  assert.deepEqual((await edgeClosure.evaluate(()=>normalRayAudit.assignments)).slice(0,previous.length),previous);
  assert(await edgeClosure.evaluate(()=>normalRayAudit.edgeClosureRounds.at(-1).every(c=>normalRayAudit.filledCells.includes(c.cell))));
 }
 assert(await edgeClosure.locator('#next').isEnabled());assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.nextEdgeClosure),[]);
 for(const step of [20,21]){await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(step=>normalRayAudit.proceduralStep===step,step);}
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.faceMedianRays.map(r=>r.id)),['ray3-24','ray1-24']);
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.diamondGapVisible);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.proceduralStep),22);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.diamondGapPlan.cells.map(c=>c.cell)),[71,77,120,122,167,187,285,293]);
 assert(await edgeClosure.evaluate(()=>normalRayAudit.diamondGapPlan.cells.every(c=>normalRayAudit.filledCells.includes(c.cell)&&normalRayAudit.assignments.some(a=>a.cell===c.cell&&a.role==='neutron'))));
 const beforeBoundary=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.neutronBoundaryVisible);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.proceduralStep),23);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.neutronBoundaryPlan.cells.map(c=>c.cell)),[75,80,97,99]);
 assert.deepEqual((await edgeClosure.evaluate(()=>normalRayAudit.assignments)).slice(0,beforeBoundary.length),beforeBoundary);
 assert(await edgeClosure.evaluate(()=>[75,80,97,99].every(id=>normalRayAudit.filledCells.includes(id)&&normalRayAudit.assignments.some(a=>a.cell===id&&a.role==='neutron'))));
 const beforeIdentified=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.identifiedSurfaceVisible);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.proceduralStep),24);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.identifiedSurfacePlan.map(c=>c.cell)),[91,93,96,100,105,114,126,129]);
 const afterIdentified=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
 assert.deepEqual(afterIdentified.slice(0,beforeIdentified.length),beforeIdentified);
 assert(afterIdentified.slice(beforeIdentified.length).every(a=>a.role==='neutron'));
 assert(await edgeClosure.locator('#next').isEnabled());
 await edgeClosure.reload();await edgeClosure.waitForFunction(()=>globalThis.normalRayAudit?.identifiedSurfaceVisible);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.proceduralStep),24);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),afterIdentified);
 await edgeClosure.locator('#process-select').selectOption('edge-ray');await castAt(edgeClosure,4,3);
 await edgeClosure.reload();await edgeClosure.waitForFunction(()=>globalThis.normalRayAudit?.processId==='edge-ray'&&normalRayAudit.proceduralStep===3);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.k),4);
 await edgeClosure.locator('#process-select').selectOption('new-construction');
 await edgeClosure.waitForFunction(()=>normalRayAudit.processId==='new-construction'&&normalRayAudit.proceduralStep===24);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.k),7);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),afterIdentified);
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.f134DiamondVisible);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.proceduralStep),25);
 const afterDiamonds=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
 assert.deepEqual(afterDiamonds.slice(0,afterIdentified.length),afterIdentified);
 assert.deepEqual(afterDiamonds.slice(afterIdentified.length).map(a=>[a.cell,a.role]),[[232,'proton'],[92,'electron'],[308,'electron'],[117,'proton']]);
 assert(await edgeClosure.locator('#next').isEnabled());
 await edgeClosure.reload();await edgeClosure.waitForFunction(()=>globalThis.normalRayAudit?.f134DiamondVisible);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),afterDiamonds);
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.f123DiamondVisible);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.proceduralStep),26);
 const afterF123=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
 assert.deepEqual(afterF123.slice(0,afterDiamonds.length),afterDiamonds);
 assert.deepEqual(afterF123.slice(afterDiamonds.length).map(a=>[a.cell,a.role]),[[246,'proton'],[98,'electron'],[322,'electron'],[123,'proton']]);
 assert(await edgeClosure.locator('#next').isEnabled());
 await edgeClosure.locator('#prev').click();await edgeClosure.waitForFunction(()=>normalRayAudit.proceduralStep===25);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),afterDiamonds);
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.f123DiamondVisible);
 await edgeClosure.reload();await edgeClosure.waitForFunction(()=>globalThis.normalRayAudit?.f123DiamondVisible);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),afterF123);
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.surfaceRemainderVisible);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.proceduralStep),27);
 const completedFaces=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
 assert.deepEqual(completedFaces.slice(0,afterF123.length),afterF123);
 assert.deepEqual(completedFaces.slice(afterF123.length).map(a=>[a.cell,a.role]),[107,110,118,121,228,254,272,298].map(id=>[id,'neutron']));
 assert(await edgeClosure.locator('#next').isEnabled());
 await edgeClosure.reload();await edgeClosure.waitForFunction(()=>globalThis.normalRayAudit?.surfaceRemainderVisible);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),completedFaces);
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.remainingFaceVisible);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.proceduralStep),28);
 const allFaces=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
 assert.deepEqual(allFaces.slice(0,completedFaces.length),completedFaces);
 assert.deepEqual(allFaces.slice(completedFaces.length).map(a=>[a.cell,a.role]),[[70,'proton'],[163,'electron'],[81,'proton'],[199,'electron'],[109,'electron'],[241,'proton'],[113,'electron'],[257,'proton'],...[69,84,95,101].map(id=>[id,'neutron'])]);
 assert(await edgeClosure.locator('#next').isDisabled());
 assert(await edgeClosure.locator('#particle-counts').isVisible());
 assert.deepEqual(await edgeClosure.locator('#particle-counts tbody tr').evaluateAll(rows=>rows.map(r=>[...r.querySelectorAll('td')].map(td=>Number(td.textContent)))),[[24,110,24,158],[0,46,0,46],[24,156,24,204]]);
 assert(await edgeClosure.evaluate(()=>{const panel=document.querySelector('#inventory-panel'),a=panel.getBoundingClientRect(),b=document.querySelector('#scene').getBoundingClientRect();return Math.abs(b.right-a.right-10)<1&&Math.abs(b.bottom-a.bottom-10)<1&&getComputedStyle(panel).pointerEvents==='auto';}));
 await edgeClosure.locator('#prev').click();await edgeClosure.waitForFunction(()=>normalRayAudit.proceduralStep===27);
 assert.equal(Number(await edgeClosure.locator('[data-count-row="total"] [data-count-role="total"]').textContent()),completedFaces.length);
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.remainingFaceVisible);
 await edgeClosure.reload();await edgeClosure.waitForFunction(()=>globalThis.normalRayAudit?.remainingFaceVisible);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),allFaces);
 assert.equal(Number(await edgeClosure.locator('[data-count-row="total"] [data-count-role="total"]').textContent()),allFaces.length);
 await edgeClosure.locator('#process-select').selectOption('diamond-construction');
 await edgeClosure.waitForFunction(()=>normalRayAudit.processId==='diamond-construction'&&normalRayAudit.proceduralStep===0);
 for(let k=1;k<=7;k++){
  await castAt(edgeClosure,k,4);
  assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.foundationComplete),true);
  assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.conflicts),[]);
  assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.diamonds.length),k===1?0:2);
  assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.assignments.length),k===1?1:5);
  assert.equal(await edgeClosure.locator('#next').isEnabled(),[3,5,7].includes(k));
  if(k===5){
   await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.proceduralStep===5);
   assert(await edgeClosure.evaluate(()=>normalRayAudit.assignments.some(a=>a.cell===26&&a.role==='proton')));
   assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.radial.orientationCount),9);assert(await edgeClosure.locator('#next').isDisabled());
  }
 }
 const cleanFoundation=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
 await edgeClosure.reload();await edgeClosure.waitForFunction(()=>globalThis.normalRayAudit?.processId==='diamond-construction'&&normalRayAudit.foundationComplete);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),cleanFoundation);
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.proceduralStep===5);
 assert(await edgeClosure.evaluate(()=>normalRayAudit.assignments.find(a=>a.cell===normalRayAudit.radial.centralCell)?.role==='proton'));
 assert(await edgeClosure.evaluate(()=>normalRayAudit.radial.layers.slice(1,3).every(l=>l.assigned.length===0)));
 assert(await edgeClosure.locator('#next').isEnabled());
 await edgeClosure.locator('#radial-audit summary').click();assert(await edgeClosure.locator('#radial-audit').innerText().then(t=>t.includes('corner exception')));
 await edgeClosure.reload();await edgeClosure.waitForFunction(()=>globalThis.normalRayAudit?.processId==='diamond-construction'&&normalRayAudit.proceduralStep===5);
 const centralP=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.proceduralStep===6);
 const core=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
 assert.deepEqual(core.slice(0,centralP.length),centralP);
 assert.deepEqual(core.slice(centralP.length).map(a=>[a.cell,a.role]),[[4,'proton'],[7,'proton'],[10,'proton']]);
 assert(await edgeClosure.evaluate(()=>!normalRayAudit.radial.centralChannel.localConnectionEstablished&&normalRayAudit.radial.centralChannel.pathStatus==='geometric-only'));
 assert.equal(Number(await edgeClosure.locator('[data-count-row="total"] [data-count-role="proton"]').textContent()),6);
 assert.equal(Number(await edgeClosure.locator('[data-count-row="total"] [data-count-role="neutron"]').textContent()),1);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.connectionGuides.length),4);
 assert(await edgeClosure.locator('#next').isEnabled());
 await edgeClosure.locator('#next').click();await edgeClosure.waitForFunction(()=>normalRayAudit.proceduralStep===7);
 assert(await edgeClosure.evaluate(()=>normalRayAudit.collectiveCore.routes.length===2&&normalRayAudit.collectiveCore.routes.every(r=>r.established)&&normalRayAudit.collectiveCore.blocked.length===0));
 assert(await edgeClosure.locator('#next').isDisabled());
 const connected=await edgeClosure.evaluate(()=>normalRayAudit.assignments);
 await edgeClosure.reload();await edgeClosure.waitForFunction(()=>globalThis.normalRayAudit?.proceduralStep===7);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),connected);
 await edgeClosure.locator('#prev').click();await edgeClosure.waitForFunction(()=>normalRayAudit.proceduralStep===6);
 await edgeClosure.reload();await edgeClosure.waitForFunction(()=>globalThis.normalRayAudit?.processId==='diamond-construction'&&normalRayAudit.proceduralStep===6);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),core);
 await edgeClosure.locator('#prev').click();await edgeClosure.waitForFunction(()=>normalRayAudit.proceduralStep===5);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),centralP);
 await edgeClosure.locator('#prev').click();await edgeClosure.waitForFunction(()=>normalRayAudit.proceduralStep===4);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),cleanFoundation);
 await edgeClosure.locator('#prev').click();await edgeClosure.waitForFunction(()=>normalRayAudit.proceduralStep===3);
 assert.equal(await edgeClosure.evaluate(()=>normalRayAudit.diamonds.length),0);
 await edgeClosure.locator('#process-select').selectOption('new-construction');await edgeClosure.waitForFunction(()=>normalRayAudit.processId==='new-construction'&&normalRayAudit.proceduralStep===28);
 assert.deepEqual(await edgeClosure.evaluate(()=>normalRayAudit.assignments),allFaces);
 assert.deepEqual(edgeClosure.errors,[]);await edgeClosure.close();
 const transparency=await page();await ready(transparency);await testFaceCompositor(transparency);assert.deepEqual(transparency.errors,[]);await transparency.close();
 const sorted=await page();await sorted.addInitScript(()=>{const original=WebGL2RenderingContext.prototype.getExtension;WebGL2RenderingContext.prototype.getExtension=function(name){return name==='EXT_color_buffer_float'?null:original.call(this,name);};});await ready(sorted);assert.equal(await sorted.evaluate(()=>NormalRayViewer.snapshot().transparency),'sorted-fallback');assert.deepEqual(sorted.errors,[]);await sorted.close();
 const nojs=await page({javaScriptEnabled:false});await nojs.goto(url);assert(await nojs.locator('#fallback').isVisible());await nojs.close();
 const unavailable=await page();await unavailable.addInitScript(()=>{const original=HTMLCanvasElement.prototype.getContext;HTMLCanvasElement.prototype.getContext=function(type,...args){return /webgl/i.test(type)?null:original.call(this,type,...args);};});await unavailable.goto(url);await unavailable.waitForFunction(()=>globalThis.NormalRayViewer?.snapshot().phase==='fallback');assert(await unavailable.locator('#fallback').isVisible());assert.deepEqual(unavailable.errors,[]);await unavailable.close();
 const loss=await page();await ready(loss);await loss.locator('.webgl-canvas').evaluate(e=>e.dispatchEvent(new Event('webglcontextlost',{cancelable:true})));await loss.waitForFunction(()=>NormalRayViewer.snapshot().disposed);assert(await loss.locator('#fallback').isVisible());assert.deepEqual(loss.errors,[]);await loss.close();
 const missing=await page();await missing.route('**/assets/index-*.js',r=>r.abort());await missing.goto(url);assert(await missing.locator('#fallback').isVisible());await missing.close();
 const pending=await page();let release;const gate=new Promise(r=>release=r);await pending.route('**/assets/scene-*.js',async r=>{await gate;await r.continue().catch(()=>{});});await pending.goto(url);await pending.waitForFunction(()=>globalThis.NormalRayViewer);await pending.evaluate(()=>NormalRayViewer.dispose());release();await pending.waitForTimeout(300);assert.equal(await pending.locator('.webgl-canvas').count(),0);assert(await pending.locator('#fallback').isVisible());assert.deepEqual(pending.errors,[]);await pending.close();
 console.log('PASS normal-ray migration: geometry roles, controls, idle scheduling, panels, mobile, local-only assets, reduced motion, offscreen pause, teardown, pending-start cancellation, fallback and context-loss handler.');
}finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
