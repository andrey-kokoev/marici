import test from 'node:test';
import assert from 'node:assert/strict';
import {cellStructuralTypes,classifyCellStructure,compositionAddresses} from '../research/realization-tower/cell-fibration-structure.mjs';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-history.mjs';
import {geometricCellDepth} from '../research/realization-tower/cell-fibration-cut.mjs';
const final=cellFibrationProcess(7,5),roles=final.cellFibrationAudit.corners.map(c=>c.role);
const address=b=>[1,2,3,4].map(v=>6-geometricCellDepth(b,v));
const perms=xs=>xs.length?xs.flatMap((x,i)=>perms(xs.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
test('nine address types exhaust all 84 cells and reproduce every growth layer and colour',()=>{
 const histogram={},strata={};
 for(const b of final.retainedBodies){
  const weights=address(b),c=classifyCellStructure(weights,roles);
  assert.equal(c.layer,b.layer);assert.equal(c.role,b.role);
  histogram[c.profile]=(histogram[c.profile]??0)+1;strata[c.stratum]=(strata[c.stratum]??0)+1;
 }
 assert.deepEqual(final.retainedBodies.map(b=>address(b).join(',')).sort(),compositionAddresses().map(w=>w.join(',')).sort());
 for(const t of cellStructuralTypes)assert.equal(histogram[t.profile],t.count);
 assert.deepEqual(strata,{vertex:4,edge:30,face:40,interior:10});
 for(let layer=0;layer<=5;layer++)assert.deepEqual(new Set(cellFibrationProcess(7,layer).retainedBodies.map(b=>b.id)),new Set(final.retainedBodies.filter(b=>classifyCellStructure(address(b),roles).layer<=layer).map(b=>b.id)));
});
test('classification is covariant under all corner reindexings, with corner roles carried along',()=>{
 for(const permutation of perms([0,1,2,3]))for(const weights of compositionAddresses()){
  const a=classifyCellStructure(weights,roles),b=classifyCellStructure(permutation.map(i=>weights[i]),permutation.map(i=>roles[i]));
  assert.deepEqual(b,a);
 }
});
test('priority and midpoint choices are not P/E exchange symmetric',()=>{
 const swap=r=>r==='proton'?'electron':r==='electron'?'proton':r;
 const w=[1,2,2,1],a=classifyCellStructure(w,roles),b=classifyCellStructure(w,roles.map(swap));
 assert.equal(a.role,'proton');assert.equal(b.role,'proton');assert.notEqual(b.role,swap(a.role));
 const nn=[3,0,0,3];assert.equal(classifyCellStructure(nn,roles).role,'electron');assert.equal(classifyCellStructure(nn,roles.map(swap)).role,'electron');
 assert.throws(()=>classifyCellStructure([0,0,0,0],roles),/summing to 6/);
 assert.throws(()=>classifyCellStructure([3,3,0,0],['proton','proton','neutron','electron']),/not defined/);
});
