import test from 'node:test';
import assert from 'node:assert/strict';
import {buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-process.mjs';
import {applyCellFibrationCut,geometricCellLayer} from '../research/realization-tower/cell-fibration-cut.mjs';
import {makeEsd7CellIds,esd7CellId,esd7GeometryId} from '../research/realization-tower/esd7-cell-ids.mjs';
const geometry=buildFoldedFibration().geometry;
test('ESD7 IDs start at the proton corner and cover whole layers consecutively',()=>{
 const ids=makeEsd7CellIds(geometry),proton=cellFibrationProcess(7,0).cellFibrationAudit.corners.find(c=>c.role==='proton');
 assert.equal(ids.get(proton.cell),1);
 assert.deepEqual([...ids.values()].sort((a,b)=>a-b),Array.from({length:175},(_,i)=>i+1));
 const bounds=[[1,1],[2,5],[6,15],[16,34],[35,65],[66,111],[112,175]];
 for(let layer=0;layer<=6;layer++){
  const numbers=geometry.filter(g=>geometricCellLayer(g,2)===layer).map(g=>ids.get(g.id)).sort((a,b)=>a-b);
  const [first,last]=bounds[layer];assert.deepEqual(numbers,Array.from({length:last-first+1},(_,i)=>first+i));
 }
 assert.equal(esd7CellId('oct-0.5,0.5,1.5,-1.5'),91);
 for(const [key,id] of ids)assert.equal(esd7GeometryId(id),key);
});
test('IDs ignore enumeration order, fill state, construction step and cuts',()=>{
 const normalize=m=>[...m].sort((a,b)=>a[1]-b[1]);
 assert.deepEqual(normalize(makeEsd7CellIds([...geometry].reverse())),normalize(makeEsd7CellIds(geometry)));
 assert.throws(()=>makeEsd7CellIds(geometry.slice(1)),/complete/);
 for(let step=0;step<=14;step++){
  const p=cellFibrationProcess(7,step);
  assert.equal(new Set([...p.retainedBodies,...p.emptyBodies].map(b=>esd7CellId(b.id))).size,175);
  for(let vertex=1;vertex<=4;vertex++){
   const cut=applyCellFibrationCut(p,{enabled:true,vertex,startLayer:1,layer:3,showEmpty:false});
   for(const b of [...cut.retainedBodies,...cut.emptyBodies])assert.equal(esd7GeometryId(esd7CellId(b.id)),b.id);
  }
 }
 assert.equal(esd7CellId('unsplit-octahedron'),'unsplit-octahedron');
});
