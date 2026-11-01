import {test} from 'node:test';
import assert from 'node:assert/strict';
import {cellulationWindow,buildRepeatingCellulation} from '../research/realization-tower/repeating-cellulation.mjs';
test('viewport slab covers corners beyond the old extent cap, including a distant pan and rotated view',()=>{
 const axes=[[[1,0,0],[0,1,0],[0,0,1]],[[1/Math.SQRT2,-1/Math.SQRT2,0],[-1/Math.sqrt(6),-1/Math.sqrt(6),2/Math.sqrt(6)],[-1/Math.sqrt(3),-1/Math.sqrt(3),-1/Math.sqrt(3)]]];
 for(const [right,up,normal] of axes){
  const center=[40,-23,17],halfWidth=12,halfHeight=3;
  const spec=cellulationWindow(1,center,0,{right,up,normal,halfWidth,halfHeight});assert(spec.extent>12);
  const model=buildRepeatingCellulation(spec),ids=new Set(model.cells.map(c=>c.id));assert.equal(model.fade.viewport,true);
  for(const x of [-1,0,1])for(const y of [-1,0,1]){
   const point=center.map((v,i)=>v+x*halfWidth*right[i]+y*halfHeight*up[i]),base=point.map(v=>Math.floor(v*Math.SQRT2));assert(ids.has(`t:${base}`),`missing viewport sample ${point}`);
  }
  assert.equal(model.cellSize,1);
 }
});
