import test from 'node:test';
import assert from 'node:assert/strict';
import {cellFibrationProcess} from '../research/realization-tower/cell-fibration-process.mjs';
import {geometricCellLayer} from '../research/realization-tower/cell-fibration-cut.mjs';
import {simplexMovementPaths} from '../research/realization-tower/simplex-cell-movement.mjs';
const process=cellFibrationProcess(7,0),all=[...process.retainedBodies,...process.emptyBodies],byId=new Map(all.map(b=>[b.id,b]));
const address=id=>[1,2,3,4].map(v=>geometricCellLayer(byId.get(id),v)).join('');
const target=all.find(b=>address(b.id)==='4555');
test('dual-graph paths encode every one-unit simplex-coordinate move from each vertex',()=>{
 const paths=simplexMovementPaths(target.id);assert.deepEqual(paths.map(p=>p.label),['N₁','P','E','N₂']);
 for(const path of paths){
  assert.equal(path.cells.length,path.steps.length+1);assert.equal(path.target,target.id);
  assert.equal(path.cells[0],path.root);assert.equal(path.cells.at(-1),target.id);
  for(let i=0;i<path.steps.length;i++){
   const step=path.steps[i],from=address(path.cells[i]).split('').map(Number),to=address(path.cells[i+1]).split('').map(Number);
   assert.equal(step.from,from.join(''));assert.equal(step.to,to.join(''));
   const delta=from.map((x,j)=>to[j]-x);
   assert.equal(delta.filter(x=>x!==0).length,1);assert.equal(Math.abs(delta.find(x=>x!==0)),1);
  }
 }
 assert.deepEqual(paths[0].cells.map(address),['0666','1666','2666','2566','3566','3556','3555','4555']);
 assert.deepEqual(paths[0].code,['N₁+','N₁+','P−','N₁+','E−','N₂−','N₁+']);
});
