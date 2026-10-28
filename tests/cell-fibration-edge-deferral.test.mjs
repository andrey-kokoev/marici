import test from 'node:test';
import assert from 'node:assert/strict';
import {cellFibrationProcess,buildCellFibration} from '../research/realization-tower/cell-fibration-process.mjs';
import {esd7CellId} from '../research/realization-tower/esd7-cell-ids.mjs';
const edgeIds=[16,31,34,127,130,172];
test('the removed edge step assigns none of the six edges; final fill assigns all N',()=>{
 assert.equal(buildCellFibration().edgeCoherenceGrowth,undefined);
 for(let step=0;step<=6;step++){
  const p=cellFibrationProcess(7,step);
  for(const id of edgeIds){
   assert.ok(!p.retainedBodies.some(b=>esd7CellId(b.id)===id));
   assert.equal(p.emptyBodies.find(b=>esd7CellId(b.id)===id)?.role,null);
  }
 }
 const final=cellFibrationProcess(7,7);
 for(const id of edgeIds){
  const b=final.retainedBodies.find(b=>esd7CellId(b.id)===id);
  assert.equal(b.role,'neutron');assert.equal(b.layer,7);assert.equal(b.coherence,undefined);
 }
 const roles=ids=>ids.map(id=>final.retainedBodies.find(b=>esd7CellId(b.id)===id).role);
 assert.deepEqual(roles([6,17,16]),['proton','electron','neutron']);
 assert.deepEqual(roles([15,30,34]),['proton','electron','neutron']);
});
