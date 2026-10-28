import {esd7NodePlanes,esd7PlaneOf} from '../examples/normal-ray/esd7-node-planes.js';
import test from 'node:test';import assert from 'node:assert/strict';
import {filterComplexVisibility} from '../examples/normal-ray/complex-visibility.js';
import {processState} from '../research/realization-tower/normal-ray-processes.mjs';
test('each actual ESD7 node plane can be hidden independently on either half',()=>{
 const p=processState('double-esd7',7,0,1,{rimAssembly:true}),before=JSON.stringify(p);
 assert.equal(esd7NodePlanes.reduce((s,p)=>s+p.count,0),175);assert.deepEqual(esd7NodePlanes.slice(0,2).map(p=>p.count),[28,21]);
 for(const copy of ['original','clone'])for(const plane of esd7NodePlanes){
  const mask=esd7NodePlanes.map(p=>p.index!==plane.index),shown=filterComplexVisibility(p,{},undefined,{[copy]:mask});
  assert.equal(shown.complexVisibilityAudit.visibleParentCells,350-plane.count);assert.equal(shown.attachmentBodies.length,64);
  assert.ok([...shown.retainedBodies,...shown.emptyBodies].every(b=>{const q=esd7PlaneOf.get(b.id);return q.copy!==copy||q.index!==plane.index;}));
 }
 assert.equal(filterComplexVisibility(p,{},undefined,{original:esd7NodePlanes.map(()=>false),clone:esd7NodePlanes.map(()=>false)}).complexVisibilityAudit.visibleParentCells,0);
 assert.equal(JSON.stringify(p),before);
});
test('all 64 belt-layer masks filter nodes, links and square labels without touching parents',()=>{
 const p=processState('double-esd7',7,0,1,{rimAssembly:true}),before=JSON.stringify(p),counts=[16,4,12,12,4,16];
 for(let mask=0;mask<64;mask++){
  const layers=counts.map((_,i)=>Boolean(mask&(1<<i))),shown=filterComplexVisibility(p,{},layers),ids=new Set([...shown.attachmentBodies,...shown.terminalBundles].map(b=>b.id));
  assert.equal(shown.attachmentBodies.length,counts.reduce((s,n,i)=>s+(layers[i]?n:0),0));
  assert.deepEqual(shown.complexVisibilityAudit.visibleBeltLayerCounts,counts.map((n,i)=>layers[i]?n:0));
  assert.ok(shown.beltGraphLinks.every(e=>ids.has(e.from)&&ids.has(e.to)));
  assert.equal(shown.presentationLabels.filter(p=>p.cell.startsWith('belt:square:')).length,0);
  assert.deepEqual(shown.retainedBodies,p.retainedBodies);assert.deepEqual(shown.emptyBodies,p.emptyBodies);
  assert.equal(filterComplexVisibility(p,{belt:false},layers).attachmentBodies.length,0);
 }
 assert.equal(JSON.stringify(p),before);
});
test('all eight visibility combinations are render-only and keep belt independent of parents',()=>{
 const p=processState('double-esd7',7,0,1,{rimAssembly:true}),before=JSON.stringify(p);
 for(const original of [false,true])for(const clone of [false,true])for(const belt of [false,true]){
  const v={original,clone,belt},shown=filterComplexVisibility(p,v);
  assert.equal(shown.complexVisibilityAudit.visibleParentCells,175*(Number(original)+Number(clone)));
  assert.equal(shown.attachmentBodies.length,belt?64:0);assert.equal(shown.terminalBundles.length,belt?Number(original)+Number(clone):0);
  const endpoints=new Set([...shown.attachmentBodies,...shown.terminalBundles].map(b=>b.id));assert.ok(shown.beltGraphLinks.every(e=>endpoints.has(e.from)&&endpoints.has(e.to)));
  assert.equal(shown.doubleEsd7Audit,p.doubleEsd7Audit);
  for(const body of [...shown.retainedBodies,...shown.emptyBodies])assert.ok(v[body.id.split(':')[0]]);
  if(!original&&!clone)assert.equal(shown.presentationLabels.length,0);
  if(!original&&!clone&&!belt)assert.equal(shown.interfaceGuides.length,0);
 }
 assert.equal(JSON.stringify(p),before);
});
