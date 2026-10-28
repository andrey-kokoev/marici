import test from 'node:test';
import assert from 'node:assert/strict';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-process.mjs';
import {applyCellFibrationCut,geometricCellLayer} from '../research/realization-tower/cell-fibration-cut.mjs';
test('every native unfilled cell is available for picking without being assigned or counted',()=>{
 for(let step=0;step<=14;step++){
  const p=cellFibrationProcess(7,step),filled=new Set(p.retainedBodies.map(b=>b.id));
  assert.equal(p.retainedBodies.length+p.emptyBodies.length,175);
  assert.equal(new Set([...filled,...p.emptyBodies.map(b=>b.id)]).size,175);
  assert.equal(p.cellFibrationAudit.counts.total.total,p.retainedBodies.length);
  for(const b of p.emptyBodies){assert.equal(b.unfilled,true);assert.equal(b.role,null);assert.equal(b.layer,null);assert.ok(!filled.has(b.id));assert.ok(b.faces.length>=4);}
 }
 const p=cellFibrationProcess(7,4);assert.equal(p.emptyBodies.length,119);
 assert.equal(p.emptyBodies.filter(b=>b.kind==='octahedron').length,40);
 assert.equal(p.emptyBodies.filter(b=>b.kind==='tetrahedron').length,79);
});
test('invisible hover positions obey the cut, independently of empty-wireframe visibility',()=>{
 const p=cellFibrationProcess(7,4);
 for(const vertex of [1,2,3,4,'all'])for(let layer=0;layer<=6;layer++){
  const vs=vertex==='all'?[1,2,3,4]:[vertex];
  const expected=p.emptyBodies.filter(b=>vs.some(v=>geometricCellLayer(b,v)===layer));
  for(const showEmpty of [false,true]){
   const cut=applyCellFibrationCut(p,{enabled:true,vertex,startLayer:layer,layer,showEmpty});
   assert.deepEqual(cut.emptyBodies,expected);
  }
 }
});
