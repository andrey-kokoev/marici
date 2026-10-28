import test from 'node:test';
import assert from 'node:assert/strict';
import {auditEdgePairSymmetry,exchangeEP} from '../research/realization-tower/edge-pair-symmetry.mjs';
import {apex} from '../research/realization-tower/normal-ray-model.mjs';
import {edgeRayPoint} from '../research/realization-tower/edge-ray-model.mjs';
test('endpoint exchange is an involution on every edge segment',()=>{
 for(let k=1;k<=7;k++){
  assert.deepEqual(exchangeEP(k,apex),edgeRayPoint(k));
  for(let i=0;i<=k;i++){
   assert.deepEqual(exchangeEP(k,edgeRayPoint(i)),edgeRayPoint(k-i));
   assert.deepEqual(exchangeEP(k,exchangeEP(k,edgeRayPoint(i))),edgeRayPoint(i));
  }
 }
 assert.throws(()=>exchangeEP(0,apex),/k must/);
});
test('both continuation choices preserve cells, octahedral diagonals and completed role/closure witnesses',()=>{
 for(let k=1;k<=7;k++)for(const branch of [1,3]){
  const a=auditEdgePairSymmetry(k,branch);
  assert.equal(a.regionCells,k**3);assert(a.subdivisionPreserved);assert(a.properHalfTurn);
  assert.equal(a.unassignedEdgePairs.length,Math.floor(Math.max(0,k-2)/2));
  assert.equal(a.fixedUnassignedEdgeCells.length,k>2&&k%2?1:0);
  if(k===3)assert.equal(a.segments[1].assignedFaceCount,2);
  if(k===4)assert.deepEqual(a.segments.slice(1,-1).map(s=>s.assignedFaceCount),[1,1]);
 }
});
