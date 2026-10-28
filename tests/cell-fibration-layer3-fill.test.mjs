import test from 'node:test';
import assert from 'node:assert/strict';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-process.mjs';
import {applyCellFibrationCut,geometricCellLayer} from '../research/realization-tower/cell-fibration-cut.mjs';
import {esd7CellId} from '../research/realization-tower/esd7-cell-ids.mjs';
const before=cellFibrationProcess(7,6),after=cellFibrationProcess(7,7);
test('step 7 fills every remaining layer-3 cell with N, and nothing else',()=>{
 const expected=before.emptyBodies.filter(b=>[1,2,3,4].some(v=>geometricCellLayer(b,v)===3));
 const added=after.retainedBodies.filter(b=>b.layer===7);
 assert.equal(added.length,42);assert.deepEqual(added.map(b=>b.id).sort(),expected.map(b=>b.id).sort());
 assert.ok(added.every(b=>b.role==='neutron'));
 for(const id of [139,154,108,62,50,81])assert.equal(added.find(b=>esd7CellId(b.id)===id)?.role,'neutron');
 for(let vertex=1;vertex<=4;vertex++)assert.equal(added.filter(b=>geometricCellLayer(b,vertex)===3).length,12);
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(g=>g.id===b.id),b);
 for(const b of before.emptyBodies.filter(b=>!expected.some(g=>g.id===b.id)))assert.ok(after.emptyBodies.some(g=>g.id===b.id));
 assert.equal(new Set(after.retainedBodies.map(b=>b.id)).size,126);
 assert.deepEqual(after.cellFibrationAudit.counts.total,{proton:19,neutron:90,electron:17,total:126});
 assert.equal(after.emptyBodies.length,49);assert.equal(after.canAdvance,true);assert.equal(before.canAdvance,true);
});
test('layer-3 cuts have no remaining empty positions, including interior inverted tetrahedra',()=>{
 for(let vertex=1;vertex<=4;vertex++){
  const cut=applyCellFibrationCut(after,{enabled:true,vertex,startLayer:3,layer:3,showEmpty:true});
  assert.equal(cut.retainedBodies.length,19);assert.equal(cut.emptyBodies.length,0);assert.equal(cut.cutAudit.emptyCount,0);
 }
 const all=applyCellFibrationCut(after,{enabled:true,vertex:'all',startLayer:3,layer:3,showEmpty:true});
 assert.equal(all.retainedBodies.length,70);assert.equal(all.emptyBodies.length,0);
});
