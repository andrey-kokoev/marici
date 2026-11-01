import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {cellulationDotAnchors} from '../research/realization-tower/cellulation-anchors.mjs';
test('only displayed dot vertices provide outward unit normal anchors',()=>{
 assert.deepEqual(cellulationDotAnchors(buildCellulationStep(1)),[]);
 assert.equal(cellulationDotAnchors(buildCellulationStep(2)).length,1);
 for(const size of [.5,1,2]){
  const model=buildCellulationStep(5,size),anchors=cellulationDotAnchors(model);assert.deepEqual(anchors.map(a=>a.id),['seed','witness']);
  for(const a of anchors){
   assert(Math.abs(Math.hypot(...a.normal)-1)<1e-12);
   const base=model.cells[0].vertices.filter(p=>p.some((x,i)=>Math.abs(x-a.point[i])>1e-12));assert.equal(base.length,3);
   for(const p of base.slice(1))assert(Math.abs(p.reduce((s,x,i)=>s+(x-base[0][i])*a.normal[i],0))<1e-12);
   assert(a.point.reduce((s,x,i)=>s+(x-base[0][i])*a.normal[i],0)>0);
  }
 }
});
