import test from 'node:test';
import assert from 'node:assert/strict';
import {cellFibrationProcess,cellFibrationStages,buildCellFibration} from '../research/realization-tower/cell-fibration-process.mjs';
import {cellFibrationProcess as historical} from '../research/realization-tower/cell-fibration-history.mjs';
import {geometricCellLayer,applyCellFibrationCut} from '../research/realization-tower/cell-fibration-cut.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('original steps 0–2 are unchanged; removed growth never enters the active construction',()=>{
 assert.equal(cellFibrationStages.length,15);
 for(let step=0;step<=2;step++)assert.deepEqual(cellFibrationProcess(7,step).retainedBodies,historical(7,step).retainedBodies);
 assert.deepEqual(Array.from({length:15},(_,s)=>cellFibrationProcess(7,s).retainedBodies.length),[4,16,40,44,56,80,84,126,142,148,152,164,170,174,175]);
 const oldIds=new Set(historical(7,5).retainedBodies.filter(b=>b.layer>=3).map(b=>b.id));
 for(let step=0;step<=4;step++){
  const p=cellFibrationProcess(7,step);
  for(const b of p.retainedBodies){assert.ok(!oldIds.has(b.id));assert.ok([1,2,3,4].some(v=>geometricCellLayer(b,v)<=2));}
  assert.equal(p.canAdvance,true);
 }
 const m=buildCellFibration();assert.equal(m.midpointGrowth,undefined);assert.equal(m.sharedInterior,undefined);assert.equal(m.faceCenters,undefined);
});
test('remaining octahedron rules stay intact with new step indices',()=>{
 const p=cellFibrationProcess(7,4);
 assert.deepEqual(p.cellFibrationAudit.counts.total,{proton:11,neutron:34,electron:11,total:56});
 assert.equal(p.retainedBodies.filter(b=>b.layer===3).length,4);
 assert.equal(p.retainedBodies.filter(b=>b.layer===4&&b.role==='neutron').length,12);
 assert.deepEqual(p.emptyBodies.filter(b=>[1,2,3,4].some(v=>geometricCellLayer(b,v)===2)).map(b=>b.id).sort(),['tet-27','tet-31','tet-41','tet-60']);
 for(let v=1;v<=4;v++)assert.equal(applyCellFibrationCut(p,{enabled:true,vertex:v,startLayer:3,layer:3,showEmpty:false}).retainedBodies.length,0);
});
test('removed saved steps clamp to the remaining endpoint without affecting other processes',()=>{
 for(const step of [15,99]){
  assert.throws(()=>cellFibrationProcess(7,step),/Invalid/);
  const p=normalizeSceneSettings({process:{id:'cell-fibration',step,progress:{'cell-fibration':{k:7,step},'fibration-12x12':{k:7,step:50}}}}).process;
  assert.equal(p.step,14);assert.equal(p.progress['cell-fibration'].step,14);assert.equal(p.progress['fibration-12x12'].step,50);
 }
});
