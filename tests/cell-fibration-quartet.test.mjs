import test from 'node:test';
import assert from 'node:assert/strict';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-process.mjs';
import {quartetCellCoherence} from '../research/realization-tower/quartet-cell-coherence.mjs';
import {esd7CellId} from '../research/realization-tower/esd7-cell-ids.mjs';
const key=f=>f.map(p=>p.join(',')).sort().join('|');
test('two N and two non-N completion adds only N or P, independently of neighbour order',()=>{
 for(const [roles,role] of [[['neutron','neutron','proton'],'proton'],[['neutron','neutron','electron'],'proton'],[['neutron','proton','electron'],'neutron'],[['neutron','proton','proton'],'neutron'],[['neutron','electron','electron'],'neutron']]){
  for(let i=0;i<3;i++){
   const order=[...roles.slice(i),...roles.slice(0,i)];
   assert.deepEqual(quartetCellCoherence(order),{pattern:'2N + 2 non-N',role});
   assert.deepEqual(quartetCellCoherence(order.reverse()),{pattern:'2N + 2 non-N',role});
  }
 }
 for(const roles of [[],['neutron','proton'],['neutron','neutron','neutron'],['proton','proton','electron']])assert.throws(()=>quartetCellCoherence(roles));
});
test('step 6 fills four centres, including 95 as N from 91=P, 104=N, 150=E',()=>{
 const before=cellFibrationProcess(7,5),after=cellFibrationProcess(7,6),added=after.retainedBodies.filter(b=>b.layer===6);
 assert.equal(added.length,4);
 const expected=new Map([[24,'proton'],[74,'neutron'],[93,'proton'],[95,'neutron']]);
 for(const b of added){
  assert.equal(b.kind,'tetrahedron');assert.equal(b.role,expected.get(esd7CellId(b.id)));assert.equal(b.coherence.neighbors.length,3);
  for(const n of b.coherence.neighbors){
   const parent=before.retainedBodies.find(g=>g.id===n.cell);assert.ok(parent);assert.equal(n.role,parent.role);
   assert.ok(parent.faces.some(f=>key(f)===key(n.sharedFace)));assert.ok(b.faces.some(f=>key(f)===key(n.sharedFace)));
  }
  assert.equal([b.role,...b.coherence.neighbors.map(n=>n.role)].filter(r=>r==='neutron').length,2);
  assert.ok(['neutron','proton'].includes(b.role));
 }
 const example=added.find(b=>esd7CellId(b.id)===95);
 assert.deepEqual(example.coherence.neighbors.map(n=>[esd7CellId(n.cell),n.role]).sort((a,b)=>a[0]-b[0]),[[91,'proton'],[104,'neutron'],[150,'electron']]);
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(g=>g.id===b.id),b);
 assert.equal(new Set(after.retainedBodies.map(b=>b.id)).size,84);
 assert.deepEqual(after.cellFibrationAudit.counts.total,{proton:19,neutron:48,electron:17,total:84});
 assert.equal(after.emptyBodies.length,91);assert.equal(after.canAdvance,true);assert.equal(before.canAdvance,true);
});
