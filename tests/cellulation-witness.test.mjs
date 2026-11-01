import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {cellulationWitnessAt,witnessTiming} from '../research/realization-tower/cellulation-witness.mjs';
import {createCellulationArrow} from '../examples/normal-ray/cellulation-arrow.js';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
import {createCellulationWitness} from '../examples/normal-ray/cellulation-witness-renderer.js';
test('the hollow circle is present at step 3 and remains hollow throughout step 4',()=>{
 const third=buildCellulationStep(3),scene=createCellulation(third);assert.deepEqual(third.proposedVertex,third.arrows[0].to);assert(scene.children.some(o=>o.userData.cellulationBillboard&&o.geometry.type==='RingGeometry'));
 scene.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
 const {proposal,edge,total}=witnessTiming,model=buildCellulationStep(4),renderer=createCellulationWitness(model.witness,1);
 const [outline,dot]=renderer.group.children;assert.equal(outline.geometry.type,'RingGeometry');assert(outline.geometry.parameters.innerRadius>0);assert.equal(outline.geometry.parameters.outerRadius,dot.geometry.parameters.radius);assert.equal(outline.material.color.getHex(),0xffffff);assert.equal(outline.userData.cellulationBillboard,true);
 for(const time of [0,proposal,proposal+edge,proposal+2*edge-1]){
  renderer.update(time);assert.equal(renderer.audit.whiteDotVisible,false);assert.equal(renderer.audit.redFaceVisible,false);assert.equal(renderer.audit.proposalVisible,true);
 }
 assert.equal(cellulationWitnessAt(proposal+edge).first,1);assert.equal(cellulationWitnessAt(proposal+edge).second,0);
 renderer.update(proposal+2*edge);assert.equal(renderer.audit.witnessed,true);assert.equal(renderer.audit.whiteDotVisible,false);assert.equal(renderer.group.children[1].material.color.getHex(),0xffffff);assert.equal(renderer.audit.proposalVisible,true);
 assert.equal(renderer.update(total,{faceOpacity:.4}),false);assert.equal(renderer.audit.redFaceVisible,false);assert.equal(renderer.audit.redFaceCount,0);assert.equal(renderer.audit.faceOpacity,0);
 renderer.update(total,{edgesOnly:true});assert.equal(renderer.audit.redFaceVisible,false);
 renderer.update(0);assert.equal(renderer.audit.whiteDotVisible,false);assert.equal(renderer.audit.first,0);
 renderer.group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
test('step 5 fills the proposed white dot and colours exactly two faces only after the second return closes',()=>{
 const {proposal,edge,total}=witnessTiming,model=buildCellulationStep(5),renderer=createCellulationWitness(model.witness,1);
 assert.equal(model.arrows.length,3);assert.equal(model.arrows.filter(a=>a.colour===0xffffff).length,2);
 assert.deepEqual(model.witness.returnPath[0],model.markedVertex);assert.deepEqual(model.witness.returnPath.at(-1),model.arrows[0].to);
 const key=p=>p.join(','),faces=model.cells[0].faces.map(f=>f.map(key).sort().join('|'));
 assert.equal(model.witness.faces.length,2);assert.equal(new Set(model.witness.faces.map(f=>f.map(key).sort().join('|'))).size,2);
 for(const face of model.witness.faces){assert(faces.includes(face.map(key).sort().join('|')));for(const vertex of [model.arrows[0].from,model.arrows[0].to])assert(face.some(p=>key(p)===key(vertex)));}
 for(const t of [0,proposal,proposal+edge,proposal+2*edge-1]){renderer.update(t);assert.equal(renderer.audit.proposalVisible,true);assert.equal(renderer.audit.whiteDotVisible,false);assert.equal(renderer.audit.redFaceCount,0);}
 assert.equal(renderer.update(total,{faceOpacity:.4}),false);assert.equal(renderer.audit.redFaceCount,2);assert.equal(renderer.audit.whiteDotVisible,true);assert.equal(renderer.audit.proposalVisible,false);assert(Math.abs(renderer.audit.faceOpacity-.22)<1e-12);
 renderer.update(total,{edgesOnly:true});assert.equal(renderer.audit.redFaceCount,0);
 renderer.update(0);assert.equal(renderer.audit.redFaceCount,0);assert.equal(renderer.audit.whiteDotVisible,false);
 renderer.group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
test('red turning vertices appear on the second white turn but remain candidates through step 5',()=>{
 const {proposal,edge,fill,total}=witnessTiming;
 for(const stage of [4,5]){
  const model=buildCellulationStep(stage),renderer=createCellulationWitness(model.witness,1),current=()=>renderer.audit.turnMarkers.at(-1);
  assert.deepEqual(model.witness.turnMarker.point,model.witness.returnPath[1]);
  renderer.update(proposal+edge-1);assert.equal(current().outlineVisible,false);assert.equal(current().solidVisible,false);
  renderer.update(proposal+edge);assert.equal(current().outlineVisible,true);assert.equal(current().solidVisible,false);
  renderer.update(total);
  assert.equal(current().outlineVisible,true);assert.equal(current().solidVisible,false);
  if(stage===5){
   assert.equal(renderer.audit.turnMarkers.length,2);assert(renderer.audit.turnMarkers.every(m=>m.outlineVisible&&!m.solidVisible&&m.fillProgress===0));assert.equal(renderer.audit.redFaceCount,2);
   renderer.update(proposal+2*edge+fill/2);assert(renderer.audit.turnMarkers.every(m=>m.fillProgress===0));
   renderer.update(0);assert.equal(renderer.audit.turnMarkers[0].outlineVisible,true);assert.equal(current().outlineVisible,false);assert(renderer.audit.turnMarkers.every(m=>!m.solidVisible));
  }
  renderer.group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
 }
});
test('arrowheads have half the former dimensions and sit at the midpoint',()=>{
 const arrow={from:[0,0,0],to:[1,0,0],colour:0xff3030},group=createCellulationArrow(arrow,1),[shaft,head]=group.children;
 assert.deepEqual(head.position.toArray(),[.5,0,0]);assert.equal(head.geometry.parameters.height,.08);assert.equal(head.geometry.parameters.radius,.0225);
 group.userData.setProgress(.25);assert.equal(shaft.scale.y,.25);assert.equal(head.visible,false);
 group.userData.setProgress(1);assert.equal(head.visible,true);assert.deepEqual(head.position.toArray(),[.5,0,0]);
 group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
