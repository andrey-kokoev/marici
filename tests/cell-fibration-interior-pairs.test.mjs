import test from 'node:test';
import assert from 'node:assert/strict';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-process.mjs';
import {geometricCellLayer} from '../research/realization-tower/cell-fibration-cut.mjs';
import {esd7CellId} from '../research/realization-tower/esd7-cell-ids.mjs';
const address=b=>[1,2,3,4].map(v=>geometricCellLayer(b,v)).join('');
const before=cellFibrationProcess(7,8),after=cellFibrationProcess(7,9),added=after.retainedBodies.filter(b=>b.layer===9);
test('four paired copies fill six distinct interior cells',()=>{
 assert.equal(added.length,6);assert.equal(added.filter(b=>b.kind==='octahedron').length,4);assert.equal(added.filter(b=>b.kind==='tetrahedron').length,2);
 for(const [source,targets] of [['6444',['5554','4554']],['4644',['5545','5445']],['4464',['5455','5445']],['4446',['4555','4554']]]){
  const parent=before.retainedBodies.find(b=>address(b)===source);assert.ok(parent);
  for(const target of targets){
   const b=added.find(b=>address(b)===target);assert.ok(b);assert.equal(b.role,parent.role);
   assert.ok(b.interiorCopy.sources.some(s=>s.cell===parent.id&&s.role===parent.role&&s.layers.join('')===source));
   assert.ok(before.emptyBodies.some(g=>g.id===b.id));
  }
 }
 for(const b of added){
  assert.equal(b.interiorCopy.layers.join(''),address(b));
  assert.equal(b.interiorCopy.sources.length,b.kind==='tetrahedron'?2:1);
  assert.ok(b.interiorCopy.sources.every(s=>s.role===b.role));
 }
});
test('further interior cells inherit the specified matching-address colours',()=>{
 const final=cellFibrationProcess(7,10),added=final.retainedBodies.filter(b=>b.layer===10);
 assert.equal(added.length,4);
 for(const [target,source,role] of [['4455','2466','neutron'],['5454','6462','neutron'],['4545','2646','neutron'],['5544','6642','neutron']]){
  const from=before.retainedBodies.find(b=>address(b)===source),to=added.find(b=>address(b)===target);
  assert.ok(from);assert.ok(to);assert.equal(to.role,role);assert.equal(to.kind,'tetrahedron');
  assert.deepEqual(to.interiorCopy.sources.map(s=>s.layers.join('')),[source]);
 }
 assert.deepEqual(final.cellFibrationAudit.counts.total,{proton:27,neutron:105,electron:20,total:152});
});
test('removed 5545 extension leaves tied targets empty',()=>{
 const final=cellFibrationProcess(7,10);
 for(const target of ['4646','6446','6644','5645'])assert.ok(final.emptyBodies.some(b=>address(b)===target));
});
test('removed step 11 leaves all four path targets empty',()=>{
 const final=cellFibrationProcess(7,10);
 for(const target of ['4565','5465','6545','6554'])assert.ok(final.emptyBodies.some(b=>address(b)===target));
 const cell=final.emptyBodies.find(b=>address(b)==='6545');assert.equal(esd7CellId(cell.id),98);assert.equal(cell.role,null);
 assert.equal(final.canAdvance,true);
});
test('removed nearest-vertex step leaves all twelve targets empty',()=>{
 const final=cellFibrationProcess(7,10);
 for(const target of ['6662','6626','6455','6266','5654','5645','5564','5546','5456','4655','4556','2666'])assert.ok(final.emptyBodies.some(b=>address(b)===target));
 assert.equal(final.canAdvance,true);
});
test('all direction pairs copy four sources to twelve distinct destinations',()=>{
 const prior=cellFibrationProcess(7,10),final=cellFibrationProcess(7,11),added=final.retainedBodies.filter(b=>b.layer===11);
 assert.equal(added.length,12);assert.equal(new Set(added.map(b=>b.id)).size,12);
 for(const [source,target,role,sourceId,targetId] of [['6444','6554','neutron',63,99],['4644','5645','proton',140,144],['4464','4565','proton',44,77],['4446','5456','neutron',42,45],['4464','5465','proton',44,46],['6444','6455','neutron',63,55],['4446','4556','neutron',42,76],['4644','4655','proton',140,132],['4464','5564','proton',44,87],['4644','5654','proton',140,145],['4446','5546','neutron',42,85],['6444','6545','neutron',63,98]]){
  const cell=added.find(b=>address(b)===target);assert.ok(cell);assert.equal(cell.role,role);assert.equal(esd7CellId(cell.id),targetId);
  const copy=cell.interiorCopy;assert.equal(copy.sources[0].layers.join(''),source);assert.equal(esd7CellId(copy.sources[0].cell),sourceId);
  assert.equal(copy.directions.length,2);
  assert.deepEqual(copy.layers,copy.sources[0].layers.map((n,i)=>n+(copy.directions.includes(i+1)?1:0)));
 }
 for(const cell of prior.retainedBodies)assert.deepEqual(final.retainedBodies.find(b=>b.id===cell.id),cell);
 assert.deepEqual(final.cellFibrationAudit.counts.total,{proton:33,neutron:111,electron:20,total:164});
 assert.equal(final.canAdvance,true);
});
test('four-neighbour NEPN filler coherence fills six centres once, without changing witnesses',()=>{
 const prior=cellFibrationProcess(7,11),final=cellFibrationProcess(7,12),added=final.retainedBodies.filter(b=>b.layer===12);
 assert.deepEqual(added.map(b=>esd7CellId(b.id)).sort((a,b)=>a-b),[39,54,56,131,133,160]);
 for(const b of added){
  assert.equal(b.role,'proton');assert.equal(b.coherence.word,'NEPN');
  assert.deepEqual(b.coherence.neighbors.map(n=>n.vertex),[1,2,3,4]);
  assert.deepEqual(b.coherence.neighbors.map(n=>n.role),['neutron','electron','proton','neutron']);
  for(const n of b.coherence.neighbors){
   const expected=[...address(b)].map(Number);expected[n.vertex-1]--;assert.deepEqual(n.layers,expected);
   assert.equal(prior.retainedBodies.find(c=>c.id===n.cell).role,n.role);
  }
 }
 for(const b of prior.retainedBodies)assert.deepEqual(final.retainedBodies.find(c=>c.id===b.id),b);
 assert.deepEqual(final.cellFibrationAudit.counts.total,{proton:39,neutron:111,electron:20,total:170});
 assert.equal(final.emptyBodies.length,5);assert.equal(final.canAdvance,true);
});
test('surface-to-filler crossing copies P/N and converts E to P in all four directions',()=>{
 const prior=cellFibrationProcess(7,12),final=cellFibrationProcess(7,13),added=final.retainedBodies.filter(b=>b.layer===13);
 assert.equal(added.length,4);
 for(const [source,target,role] of [[3,10,'proton'],[163,158,'proton'],[113,116,'neutron'],[168,162,'neutron']]){
  const b=added.find(b=>esd7CellId(b.id)===target);assert.ok(b);assert.equal(b.role,role);
  assert.equal(esd7CellId(b.interiorCopy.sources[0].cell),source);assert.equal(b.interiorCopy.boundaryCrossing,true);
  assert.ok(prior.emptyBodies.some(c=>c.id===b.id));
 }
 for(const b of prior.retainedBodies)assert.deepEqual(final.retainedBodies.find(c=>c.id===b.id),b);
 assert.deepEqual(final.cellFibrationAudit.counts.total,{proton:41,neutron:113,electron:20,total:174});
 assert.equal(final.emptyBodies.length,1);assert.equal(final.canAdvance,true);
});
test('final NPPN coherence fills only the central tetrahedron with P',()=>{
 const prior=cellFibrationProcess(7,13),final=cellFibrationProcess(7,14),added=final.retainedBodies.filter(b=>b.layer===14);
 assert.equal(added.length,1);const b=added[0];assert.equal(esd7CellId(b.id),86);assert.equal(address(b),'5555');assert.equal(b.role,'proton');
 assert.equal(b.coherence.word,'NPPN');assert.deepEqual(b.coherence.neighbors.map(n=>esd7CellId(n.cell)),[79,48,89,90]);
 for(const c of prior.retainedBodies)assert.deepEqual(final.retainedBodies.find(b=>b.id===c.id),c);
 assert.equal(new Set(final.retainedBodies.map(b=>b.id)).size,175);assert.equal(final.emptyBodies.length,0);assert.equal(final.canAdvance,false);
 assert.deepEqual(final.cellFibrationAudit.counts.total,{proton:42,neutron:113,electron:20,total:175});
});
test('previous assignments remain unchanged; shared targets count once',()=>{
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(g=>g.id===b.id),b);
 assert.equal(new Set(after.retainedBodies.map(b=>b.id)).size,148);
 assert.deepEqual(after.cellFibrationAudit.counts.total,{proton:27,neutron:101,electron:20,total:148});
 assert.equal(after.emptyBodies.length,27);assert.equal(after.canAdvance,true);assert.equal(before.canAdvance,true);
});
