import test from 'node:test';
import assert from 'node:assert/strict';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-process.mjs';
import {esd7CellId} from '../research/realization-tower/esd7-cell-ids.mjs';
const before=cellFibrationProcess(7,7),after=cellFibrationProcess(7,8),added=after.retainedBodies.filter(b=>b.layer===8);
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
test('step 8 copies all four quartets by translation, preserving shapes and colours',()=>{
 assert.equal(added.length,16);assert.equal(added.filter(b=>b.kind==='tetrahedron').length,4);assert.equal(added.filter(b=>b.kind==='octahedron').length,12);
 for(let source=1;source<=4;source++){
  const group=added.filter(b=>b.translation.source===source);
  assert.equal(group.length,4);assert.equal(group.filter(b=>b.role==='neutron').length,2);
  assert.equal(group.filter(b=>b.role!=='neutron').length,2);
  const middle=group.find(b=>b.kind==='tetrahedron');
  for(const b of group){
   const original=before.retainedBodies.find(g=>g.id===b.translation.cell);assert.ok(original);
   assert.equal(b.kind,original.kind);assert.equal(b.role,original.role);
   assert.deepEqual(b.translation.delta,[0,1,2,3].map(i=>i===source-1?3:-1));
   assert.equal(key(b.vertices),key(original.vertices.map(v=>v.map((x,i)=>x+b.translation.delta[i]))));
   assert.ok(b.faces.some(f=>f.every(v=>v[source-1]===2)));
   assert.ok(before.emptyBodies.some(g=>g.id===b.id));
   if(b!==middle)assert.ok(b.faces.some(f=>middle.faces.some(q=>key(f)===key(q))));
  }
 }
});
test('72/74/71/125 copy to 59/63/58/103 with the same colours',()=>{
 for(const [from,to,role] of [[72,59,'proton'],[74,63,'neutron'],[71,58,'neutron'],[125,103,'electron']]){
  const b=added.find(g=>esd7CellId(g.id)===to);assert.ok(b);
  assert.equal(esd7CellId(b.translation.cell),from);assert.equal(b.role,role);
 }
});
test('earlier cells remain unchanged and copies are counted once',()=>{
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(g=>g.id===b.id),b);
 assert.equal(new Set(after.retainedBodies.map(b=>b.id)).size,142);
 assert.deepEqual(after.cellFibrationAudit.counts.total,{proton:24,neutron:98,electron:20,total:142});
 const copy=added.find(b=>esd7CellId(b.id)===140);assert.equal(esd7CellId(copy.translation.cell),24);assert.equal(copy.role,'proton');
 assert.equal(after.emptyBodies.length,33);assert.equal(after.canAdvance,true);assert.equal(before.canAdvance,true);
});
