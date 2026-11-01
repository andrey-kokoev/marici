import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
test('step 16 closes the requested two unit triangular faces with white arrows',()=>{
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(16,size);assert.deepEqual(m.cells,m.previous.cells);
  assert.deepEqual(m.sequentialFaces.map(f=>f.latticeFace),[[[8,2,6],[7,2,7],[7,3,6]],[[8,2,6],[7,2,5],[7,1,6]]]);
  for(const f of m.sequentialFaces){
   assert.equal(f.arrow.colour,0xffffff);assert.deepEqual(f.arrow.from,f.faces[0][1]);assert.deepEqual(f.arrow.to,f.faces[0][2]);
   for(let i=0;i<3;i++){const a=f.faces[0][i],b=f.faces[0][(i+1)%3];assert(Math.abs(Math.hypot(...a.map((v,j)=>v-b[j]))-size)<1e-12);}
  }
 }
});
test('arrow, face, arrow, face; previous candidates and completed faces remain unchanged',()=>{
 const g=createCellulation(buildCellulationStep(16)),audit=g.userData.audit.animation,ids=g.userData.cellulationAnchors.map(a=>a.id);
 for(const elapsed of [0,500,1000,1325,1650,2150,2650,2975,Infinity]){
  g.userData.animate(elapsed,{});assert.equal(g.children[0].userData.audit.animation.whiteFaceCount,1);assert.deepEqual(g.userData.cellulationAnchors.map(a=>a.id),ids);
  audit.parts.forEach((part,i)=>{
   const local=Math.max(0,elapsed-i*1650);assert.equal(part.arrowProgress,Math.min(1,local/1000));assert.equal(part.faceFillProgress,Math.min(1,Math.max(0,(local-1000)/650)));
  });
 }
 assert.equal(audit.whiteFaceCount,2);assert.equal(g.userData.audit.faces,g.children[0].userData.audit.faces+2);
 for(const part of g.children.slice(1))assert.equal(part.children[1].material.color.getHex(),0xffffff);
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(audit.whiteFaceCount,0);
 g.userData.animate(Infinity,{faceOpacity:.4});for(const part of audit.parts)assert(Math.abs(part.whiteFaceOpacity-.22)<1e-12);
});
