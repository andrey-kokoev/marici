import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
import {renderedCellulationWitnessInput} from '../examples/normal-ray/cellulation-loop-validation.js';
import {buildShellWitnessPlan,validateShellWitnessPlan,shellWitnessFrame} from '../research/realization-tower/cellulation-shell-witness.mjs';

test('all four patches are built by complete source protocols, with explicit reuse and reverse-direction additions',()=>{
 for(const size of [.5,1,2]){
  const root=createCellulation(buildCellulationStep(26,size));root.userData.animate(Infinity,{});let g=root;
  while(g.userData.witnessPlan){
   const p=g.userData.witnessPlan;assert(p.complete);assert.deepEqual(p.blockers,[]);assert(validateShellWitnessPlan(p));assert.equal(p.cells.length,g.userData.audit.newCells);
   assert(p.events.some(e=>e.type==='reuse-arrow'));assert(p.arrows.some(a=>a.oppositeRetained));
   assert.equal(new Set(p.arrows.map(a=>a.id)).size,p.arrows.length);
   for(const a of p.arrows.filter(a=>a.oppositeRetained))assert(p.events.some(e=>e.id===a.event&&e.type==='draw-arrow'));
   const completed=shellWitnessFrame(p,Infinity);assert.equal(completed.completedCells.length,p.cells.length);assert(completed.faceProgress.every(x=>x===1));assert(completed.dotStates.every(x=>x.fill===1));
   g=g.children[0];
  }
  assert.equal(root.userData.cellulationCells.length,174);
 }
});
test('every event boundary, midpoint, reverse seek and replay obeys dot/arrow/face/cell gates',()=>{
 const g=createCellulation(buildCellulationStep(23)),p=g.userData.witnessPlan,byId=new Map(p.events.map(e=>[e.id,e]));
 const times=new Set([0,Infinity]);for(const e of p.events)for(const t of [Math.max(0,e.start-.001),e.start,(e.start+e.end)/2,e.end])times.add(t);
 for(const t of [...times].reverse()){
  const f=shellWitnessFrame(p,t);
  for(const [i,face] of p.faces.entries())if(f.faceProgress[i]>0){const event=byId.get(face.event);assert.equal(event.type,'fill-faces');for(const dep of event.requires)if(dep!=='retained-step')assert(byId.get(dep).end<=t);}
  for(const [i,d] of p.dots.entries())if(f.dotStates[i].fill>0){assert.equal(byId.get(d.event).type,'witness-dots');assert(t>d.fillStart);}
  for(const c of f.completedCells){const event=byId.get(p.cells.find(r=>r.cell.id===c.id).event);assert.equal(event.faceProofs.length,c.faces.length);for(const proof of event.faceProofs)if(proof.event!=='retained-step')assert(byId.get(proof.event).end<=t);}
 }
 // Exercise actual meshes, not only the timeline evaluator.
 for(const t of [...new Set([0,...p.events.flatMap(e=>[Math.max(0,e.end-.001),e.end]),Infinity]),0]){
  g.userData.animate(t,{});const f=shellWitnessFrame(p,t);assert.equal(g.userData.cellulationCells.length,64+f.completedCells.length);
  const meshes=g.children.filter(o=>o.userData.cellulationFaces);assert.equal(meshes.length,p.faces.length);
  meshes.forEach((mesh,i)=>{assert.equal(mesh.visible,f.faceProgress[i]>0);assert(Math.abs(mesh.material.opacity-mesh.userData.baseOpacity*f.faceProgress[i])<1e-10);});
  const arrows=g.children.filter(o=>o.userData.cellulationArrow);assert.equal(arrows.length,p.arrows.length);
  arrows.forEach((arrow,i)=>{assert.equal(arrow.children[0].visible,f.arrowProgress[i]>0);assert.equal(arrow.children[0].scale.y,f.arrowProgress[i]);});
  for(const marker of g.children.filter(o=>o.userData.witnessDotId)){
   const index=p.dots.findIndex(d=>d.id===marker.userData.witnessDotId),d=f.dotStates[index],solid=marker.geometry.type==='SphereGeometry';
   assert.equal(marker.visible,solid?d.visible&&d.fill>0:d.visible&&d.fill<1);if(solid)assert.equal(marker.material.opacity,d.fill);
  }
 }
});
test('hostile traces reject missing returns, premature fill, incorrect arrows, unwitnessed sources and missing face certificates',()=>{
 const g=createCellulation(buildCellulationStep(23)),original=g.userData.witnessPlan;
 const reject=mutate=>{const p=structuredClone(original);mutate(p);assert.throws(()=>validateShellWitnessPlan(p));};
 reject(p=>{p.events.find(e=>e.type==='first-return-witness').type='skipped-witness';});
 reject(p=>{const e=p.events.find(e=>e.type==='fill-faces');e.start=0;});
 reject(p=>{p.events.find(e=>e.type==='fill-faces').requires=[];});
 reject(p=>{const e=p.events.find(e=>e.type==='draw-arrow');[e.from,e.to]=[e.to,e.from];});
 reject(p=>{p.retainedDotKeys=[];});
 reject(p=>{p.events.find(e=>e.type==='commit-cell').faceProofs.pop();});
 reject(p=>{const e=p.events.find(e=>e.type==='four-arrival-witness');e.requires=e.requires.slice(1);});
});
test('absence of starting witnesses blocks construction instead of admitting a bulk fill',()=>{
 const model=buildCellulationStep(23),previous=createCellulation(model.previous);previous.userData.animate(Infinity,{});
 const input=renderedCellulationWitnessInput(previous),p=buildShellWitnessPlan(model,{...input,anchors:[]});
 assert.equal(p.complete,false);assert(p.blockers.length>0);assert.equal(p.cells.length,0);assert.equal(p.faces.length,0);assert.equal(shellWitnessFrame(p,Infinity).phase,'blocked');
});
