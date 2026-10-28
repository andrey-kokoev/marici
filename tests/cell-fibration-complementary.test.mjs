import test from 'node:test';
import assert from 'node:assert/strict';
import {buildCellFibration,cellFibrationProcess,cellFibrationStages} from '../research/realization-tower/cell-fibration-history.mjs';
import {applyCellFibrationCut,geometricCellDepth,geometricCellLayer} from '../research/realization-tower/cell-fibration-cut.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const model=buildCellFibration(),prior=cellFibrationProcess(7,5),after=cellFibrationProcess(7,6);
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
test('step 6 adds only four vertex-coloured octahedra in layer 1',()=>{
 assert.equal(model.complementaryGrowth.length,4);
 for(const corner of model.corners){
  const entries=model.complementaryGrowth.filter(g=>g.source===corner.vertex),seed=prior.retainedBodies.find(b=>b.id===corner.cell);
  assert.equal(entries.length,1);
  const oct=entries[0];assert.equal(oct.body.kind,'octahedron');assert.equal(oct.body.role,corner.role);
  assert.equal(oct.parent,corner.cell);assert.ok(seed.faces.some(f=>key(f)===key(oct.sharedFace)));
  const ds=oct.body.vertices.map(v=>geometricCellDepth({vertices:[v]},corner.vertex));
  assert.deepEqual([Math.min(...ds),Math.max(...ds)],[.25,1.25]);
  assert.equal(geometricCellLayer(oct.body,corner.vertex),1);
 }
});
test('step 6 preserves steps 0–5; saved progress is bounded by the reflection step',()=>{
 assert.equal(cellFibrationStages.length,8);
 assert.deepEqual(Array.from({length:7},(_,step)=>cellFibrationProcess(7,step).retainedBodies.length),[4,16,40,74,80,84,88]);
 assert.equal(new Set(after.retainedBodies.map(b=>b.id)).size,88);
 for(const b of prior.retainedBodies)assert.deepEqual(after.retainedBodies.find(g=>g.id===b.id),b);
 assert.deepEqual(after.cellFibrationAudit.counts.total,{proton:24,neutron:42,electron:22,total:88});
 assert.equal(after.retainedBodies.filter(b=>b.kind==='tetrahedron').length,84);
 assert.equal(after.retainedBodies.filter(b=>b.kind==='octahedron').length,4);
 assert.ok(after.retainedBodies.every(b=>b.layer<=6));
 assert.equal(after.canAdvance,true);assert.equal(prior.canAdvance,true);
 for(const step of [8,9,99]){
  assert.throws(()=>cellFibrationProcess(7,step),/Invalid/);
  const saved=normalizeSceneSettings({process:{id:'cell-fibration',k:7,step,progress:{'cell-fibration':{k:7,step}}}});
  assert.equal(saved.process.step,Math.min(step,14));assert.equal(saved.process.progress['cell-fibration'].step,Math.min(step,14));
 }
 assert.equal(model.complementaryLayer2Growth,undefined);assert.equal(model.complementaryTetrahedra,undefined);
});
test('cuts include the layer-1 octahedron without adding later shapes',()=>{
 for(let vertex=1;vertex<=4;vertex++){
  const cut=layer=>applyCellFibrationCut(after,{enabled:true,vertex,layer,showEmpty:true});
  assert.equal(cut(0).retainedBodies.length,1);assert.equal(cut(1).retainedBodies.length,5);
  assert.equal(cut(2).retainedBodies.length,11);assert.equal(cut(2).cutAudit.contextBodyCount,3);
  assert.equal(cut(2).cutAudit.emptyCount,0);assert.equal(cut(6).retainedBodies.length,88);
 }
});
