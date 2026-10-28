import test from 'node:test';
import assert from 'node:assert/strict';
import {fibrationRestartProcess} from '../research/realization-tower/fibration-restart-process.mjs';
import {reflectAcrossFibrationSeam} from '../research/realization-tower/fibration-step-machine.mjs';
import {fibrationDisplayEnvelope} from '../research/realization-tower/fibration12-process.mjs';
const key=face=>face.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
test('every triangle on all three face pairs is the geometric reflection of its canonical triangle',()=>{
 const pairs={F154:'F124',F453:'F423',F351:'F321'};
 for(let step=1;step<=6;step++){
  const p=fibrationRestartProcess(7,step),a=p.fibrationAudit.surfaceAssignments;
  assert.equal(p.retainedBodies.length,step===6?210:8+6*step*(step+1));
  if(step===6){const layer=a.filter(f=>f.layer===6);assert.equal(layer.length,26);assert.ok(layer.every(f=>['F453','F423'].includes(f.face)));}
  assert.equal(new Set(p.retainedBodies.map(b=>b.id)).size,p.retainedBodies.length);
  assert.equal(p.fibrationAudit.mixedCells.length,0);
  const original=a.filter(f=>f.copy==='original'),clone=a.filter(f=>f.copy==='clone');
  assert.equal(original.length,clone.length);
  for(const c of clone){
   const f=original.find(a=>a.canonicalId===c.canonicalId);
   assert.equal(f.type,c.type);assert.equal(f.face,pairs[c.face]);
   assert.equal(key(f.vertices),key(c.vertices.map(reflectAcrossFibrationSeam)));
   assert.equal(key(c.vertices),key(f.vertices.map(reflectAcrossFibrationSeam)));
  }
 }
});
test('reflection fixes all shared vertices and exchanges the tips',()=>{
 for(const i of [0,2,3])assert.equal(key([reflectAcrossFibrationSeam(fibrationDisplayEnvelope[i])]),key([fibrationDisplayEnvelope[i]]));
 assert.equal(key([reflectAcrossFibrationSeam(fibrationDisplayEnvelope[1])]),key([fibrationDisplayEnvelope[5]]));
});
