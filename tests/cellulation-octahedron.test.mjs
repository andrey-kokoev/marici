import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {packCellulation} from '../research/realization-tower/cellulation-geometry.mjs';
import {octahedronTiming} from '../research/realization-tower/cellulation-octahedron.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
const key=points=>points.map(p=>p.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
test('one regular whole octahedron joins the two tetrahedra by complete faces',()=>{
 for(const size of [.5,1,2]){
  const m=buildCellulationStep(8,size),b=m.bridge,oct=packCellulation([b.cell],'test');
  assert.equal(m.cells.length,3);assert.equal(b.cell.kind,'octahedron');assert.equal(b.cell.vertices.length,6);assert.equal(b.cell.faces.length,8);assert.equal(oct.edges.length,12);
  for(const {vertices:[a,c]} of oct.edges)assert(Math.abs(Math.hypot(...a.map((x,i)=>x-c[i]))-size)<1e-12);
  for(const tet of m.previous.cells)assert.equal(tet.faces.filter(f=>b.cell.faces.some(g=>key(f)===key(g))).length,1);
  assert.equal(m.faces.filter(f=>f.owners.length===2).length,2);assert(m.faces.every(f=>f.owners.length<=2));assert.equal(m.faces.length,14);assert.equal(m.edges.length,18);
  assert.equal(b.scaffold.faces.length,6);assert.equal(b.scaffold.edges.length,6);
  assert.equal(b.arrows.length,4);assert.equal(new Set(b.arrows.map(a=>key([a.from]))).size,4);
  const red=[m.previous.previous.witness.turnMarker,...m.previous.previous.witness.priorTurnMarkers,m.previous.repeat.stages.at(-1).witness.turnMarker,...m.previous.repeat.stages.at(-1).witness.priorTurnMarkers].map(a=>key([a.point]));
  for(const a of b.arrows){assert.equal(a.colour,0xffffff);assert(red.includes(key([a.from])));assert.deepEqual(a.to,b.opposite);assert(oct.edges.some(e=>key(e.vertices)===key([a.from,a.to])));}
 }
});
test('four arrows grow into the opposite vertex while both completed tetrahedra remain intact',()=>{
 const model=buildCellulationStep(8),group=createCellulation(model),audit=group.userData.audit,{hold,edge,total}=octahedronTiming;
 for(let count=0;count<=4;count++){
  group.userData.animate(hold+count*edge,{});assert.equal(audit.animation.arrived,count);assert.equal(audit.animation.whiteFaceCount,0);assert.equal(audit.previous.animation.phase,'complete');assert.equal(audit.previous.animation.current.animation.whiteFaceCount,2);assert.equal(audit.previous.previous.animation.whiteFaceCount,2);
 }
 assert.equal(group.userData.animate(Infinity,{}),false);assert.equal(audit.animation.phase,'complete');assert.equal(audit.animation.whiteDotVisible,true);assert.equal(audit.animation.proposalVisible,false);assert.equal(audit.animation.whiteFaceCount,8);assert.equal(audit.animation.newWhiteFaces,6);
 group.userData.animate(total,{faceOpacity:.4});assert(Math.abs(audit.animation.whiteFaceOpacity-.22)<1e-12);
 group.userData.animate(total,{edgesOnly:true});assert.equal(audit.animation.whiteFaceCount,0);
 assert.equal(group.userData.cellulationAnchors.length,8);assert.equal(new Set(group.userData.cellulationAnchors.map(a=>key([a.point]))).size,8);
 const anchor=group.userData.cellulationAnchors.at(-1);assert.equal(anchor.id,'octahedron:opposite');assert(Math.abs(Math.hypot(...anchor.normal)-1)<1e-12);
 group.userData.animate(0,{});assert.equal(audit.animation.arrived,0);assert.equal(audit.animation.whiteFaceCount,0);assert.equal(audit.animation.whiteDotVisible,false);assert.equal(audit.animation.proposalVisible,true);
 assert.equal(group.userData.animate(total,{}),false);
 group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
