import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
test('step 17 closes 837→826 and includes both 936/826/837 and 927/826/837 white faces',()=>{
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(17,size),c=m.solidClosure;assert.deepEqual(m.cells.slice(0,-1),m.previous.cells);assert.equal(m.cells.length,17);
  assert.deepEqual(c.latticeFaces,[[[7,3,6],[7,2,5],[8,3,5]],[[7,3,6],[7,2,5],[8,2,6]]]);assert.deepEqual(c.filledLatticeVertices,[[7,3,6],[7,2,5],[8,3,5]]);
  assert.equal(c.arrow.colour,0xffffff);assert.deepEqual(c.arrow.from,c.filledVertices[0]);assert.deepEqual(c.arrow.to,c.filledVertices[1]);
  assert.deepEqual(c.latticeRectangle,[[7,1,6],[7,2,7],[7,3,6],[7,2,5]]);assert.equal(c.faces.length,4);
  const area=c.faces.slice(2).reduce((sum,[a,b,d])=>sum+Math.abs((b[1]-a[1])*(d[2]-a[2])-(b[2]-a[2])*(d[1]-a[1]))/2,0);assert(Math.abs(area-size*size)<1e-12);
  for(const face of c.faces.slice(0,2))for(let i=0;i<3;i++)assert(Math.abs(Math.hypot(...face[i].map((v,j)=>v-face[(i+1)%3][j]))-size)<1e-12);
 }
});
test('arrow first, three solid white dots second, both white faces last; retain candidate IDs',()=>{
 const g=createCellulation(buildCellulationStep(17)),a=g.userData.audit.animation,ids=g.userData.cellulationAnchors.map(a=>a.id),dots=g.children.slice(2);
 for(const elapsed of [0,500,1000,1175,1350,1675,Infinity]){
  g.userData.animate(elapsed,{});assert.equal(g.children[0].userData.audit.animation.whiteFaceCount,2);assert.deepEqual(g.userData.cellulationAnchors.map(a=>a.id),ids);
  assert.equal(a.arrowProgress,Math.min(1,elapsed/1000));assert.equal(a.vertexFillProgress,Math.min(1,Math.max(0,(elapsed-1000)/350)));assert.equal(a.faceFillProgress,Math.min(1,Math.max(0,(elapsed-1350)/650)));
  for(const dot of dots){assert.equal(dot.visible,elapsed>1000);assert.equal(dot.scale.x,a.vertexFillProgress);assert.equal(dot.geometry.type,'SphereGeometry');assert.equal(dot.material.color.getHex(),0xffffff);}
  assert.equal(g.userData.cellulationCells.length,elapsed>=1000?17:16);
 }
 assert.equal(a.whiteFaceCount,4);assert.equal(a.whiteRectangleCount,1);assert.equal(a.filledDotCount,3);assert.equal(g.children[1].children[1].geometry.attributes.position.count,12);
 for(const id of ['step13:candidate','step14:candidate','step15:candidate'])assert(ids.includes(id));
 g.userData.animate(Infinity,{edgesOnly:true});assert.equal(a.whiteFaceCount,0);assert.equal(a.whiteRectangleCount,0);assert.equal(a.filledDotCount,3);
 g.userData.animate(Infinity,{faceOpacity:.4});assert(Math.abs(a.whiteFaceOpacity-.22)<1e-12);assert.equal(a.whiteFaceCount,4);assert.equal(a.whiteRectangleCount,1);
});
