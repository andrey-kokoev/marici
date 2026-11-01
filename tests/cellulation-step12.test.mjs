import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
test('step 12 retains 927→828, adds 927→817 and closes the two remaining white faces',()=>{
 for(const size of [.5,1,2]){
  const model=buildCellulationStep(12,size),c=model.faceClosure;assert.deepEqual(model.cells.slice(0,-1),model.previous.cells);assert.equal(model.cells.length,16);assert.equal(model.faces.length,77);
  assert.deepEqual(c.latticeFace,[[8,1,7],[8,2,6],[7,2,7]]);
  assert.deepEqual(c.finish.latticeFaces,[[[8,1,7],[8,2,6],[7,1,6]],[[8,2,6],[7,2,7],[7,1,6]]]);
  assert.equal(c.arrow.colour,0xffffff);assert.equal(c.finish.arrow.colour,0xffffff);assert.deepEqual(c.finish.arrow.from,c.faces[0][1]);assert.deepEqual(c.finish.arrow.to,[7,1,6].map(x=>x*size/Math.SQRT2));
  for(const face of [...c.faces,...c.finish.faces])for(let i=0;i<3;i++){const a=face[i],b=face[(i+1)%3];assert(Math.abs(Math.hypot(...a.map((v,j)=>v-b[j]))-size)<1e-12);}
 }
});
test('fill 927 after its second arrow, then fill both faces; retain all previous work and IDs',()=>{
 const model=buildCellulationStep(12),g=createCellulation(model),audit=g.userData.audit.animation,previous=g.children[0],dot=g.children[3];
 const ids=g.userData.cellulationAnchors.map(a=>a.id);
 for(const elapsed of [0,500,1325,1650,2150,2650,2825,3000,3325,Infinity]){
  g.userData.animate(elapsed,{});assert.equal(previous.userData.audit.animation.arrowProgress,1);assert.equal(previous.userData.audit.animation.candidateVisible,true);
  assert.deepEqual(g.userData.cellulationAnchors.map(a=>a.id),ids);
  assert.equal(audit.first.arrowProgress,Math.min(1,elapsed/1000));
  assert.equal(audit.finish.arrowProgress,Math.min(1,Math.max(0,(elapsed-1650)/1000)));
  assert.equal(audit.vertexFillProgress,Math.min(1,Math.max(0,(elapsed-2650)/350)));
  assert.equal(audit.finish.faceFillProgress,Math.min(1,Math.max(0,(elapsed-3000)/650)));
  assert.equal(dot.visible,elapsed>2650);assert.equal(g.userData.cellulationCells.length,elapsed>=2650?16:15);
  if(elapsed>=1650)assert.equal(audit.first.whiteFaceCount,1);
 }
 assert.equal(dot.material.color.getHex(),0xffffff);assert.equal(dot.geometry.type,'SphereGeometry');assert.equal(dot.scale.x,1);assert.deepEqual(dot.position.toArray(),model.faceClosure.finish.filledVertex);
 assert.equal(audit.newlyClosedFaceCount,2);assert.equal(audit.whiteFaceCount,3);
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(audit.whiteFaceCount,0);assert.equal(dot.visible,true);
 g.userData.animate(Infinity,{faceOpacity:.4});assert(Math.abs(audit.whiteFaceOpacity-.22)<1e-12);assert.equal(audit.whiteFaceCount,3);
});
