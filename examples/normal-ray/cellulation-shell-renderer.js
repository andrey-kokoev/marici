import * as T from 'three';
import {analyzeDotCompatibility} from '../../research/strominger/cellulation-dot-compatibility.mjs';
import {buildShellWitnessPlan,shellWitnessFrame} from '../../research/realization-tower/cellulation-shell-witness.mjs';
import {renderedCellulationWitnessInput} from './cellulation-loop-validation.js';
import {createCellulationArrow} from './cellulation-arrow.js';
import {createCellulationProposition} from './cellulation-witness-renderer.js';

export function createWitnessedShell(model,state,createPrevious){
 const group=new T.Group(),previous=createPrevious(model.previous,{...state,bodies:true}),animation={},witness={};
 previous.userData.animate(Infinity,{...state,cellulationWitnessAction:-1});group.add(previous);group.visible=state.bodies!==false;
 const plan=previous.userData.audit.animation.phase==='complete'?buildShellWitnessPlan(model,renderedCellulationWitnessInput(previous,model.cellSize)):{events:[],arrows:[],faces:[],dots:[],cells:[],scaffoldEdges:[],duration:0,complete:false,blockers:[{reason:'predecessor-not-completed',step:model.previous.step}],scope:'Construction blocked; no downstream faces admitted.'};
 group.userData.witnessPlan=plan;
 const arrows=plan.arrows.map(a=>createCellulationArrow(a,model.cellSize));group.add(...arrows);
 const faces=plan.faces.map(f=>{
  const mesh=new T.Mesh(new T.BufferGeometry().setFromPoints(f.vertices.map(p=>new T.Vector3(...p))),new T.MeshBasicMaterial({color:f.colour,side:T.DoubleSide,transparent:true,opacity:0,depthWrite:false}));
  Object.assign(mesh.userData,{cellulationFaces:true,baseOpacity:f.boundary?.65:.18,shellReading:f.boundary?f.colour:'neutral-internal-scaffold',shellFaceKeys:[f.id],witnessEvent:f.event});mesh.renderOrder=2;group.add(mesh);return mesh;
 });
 const edges=plan.scaffoldEdges.map(e=>{const line=new T.LineSegments(new T.BufferGeometry().setFromPoints(e.vertices.map(p=>new T.Vector3(...p))),new T.LineBasicMaterial({color:0xffffff,transparent:true,opacity:.65,depthWrite:false}));line.userData.witnessEvent=e.event;group.add(line);return line;});
 const markers=plan.dots.map(d=>{
  const ring=createCellulationProposition(d.point,model.cellSize,d.colour),dot=new T.Mesh(new T.SphereGeometry(.025*model.cellSize,12,8),new T.MeshBasicMaterial({color:d.colour,transparent:true,opacity:0,depthTest:false,depthWrite:false}));dot.position.fromArray(d.point);dot.renderOrder=12;dot.userData.witnessDotId=d.id;ring.userData.witnessDotId=d.id;group.add(ring,dot);return {ring,dot};
 });
 group.userData.audit={...previous.userData.audit,step:model.step,previous:previous.userData.audit,cells:model.cells.length,tetrahedra:model.cells.filter(c=>c.kind==='tetrahedron').length,octahedra:model.cells.filter(c=>c.kind==='octahedron').length,faces:previous.userData.audit.faces+plan.faces.length,edges:model.edges.length,faceCorners:model.shellFace.corners,unitTriangles:model.shellFace.triangles.length,newSurfaceTriangles:model.shellFace.newTriangles.length,newCells:model.shellFace.newCells.length,interiorCellsExcluded:model.shellFace.interiorCellsExcluded,surfaceColorCounts:Object.fromEntries([['red',0xff3030],['blue',0x3080ff],['white',0xffffff]].map(([name,colour])=>[name,plan.faces.filter(f=>f.boundary&&f.colour===colour).length])),surfaceColorRule:'Retained seed-face orientations; witnessed local construction; prior colors retained',animation,witness};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous.userData.animate(Infinity,{...appearance,cellulationWitnessAction:-1});
  const manual=appearance.cellulationStep===model.step&&appearance.cellulationWitnessAction>=0;
  const time=manual?(plan.events[Math.min(appearance.cellulationWitnessAction,plan.events.length-1)]?.end??0):elapsed,frame=shellWitnessFrame(plan,time);
  arrows.forEach((a,i)=>a.userData.setProgress(frame.arrowProgress[i]));
  faces.forEach((mesh,i)=>{mesh.visible=!appearance.edgesOnly&&frame.faceProgress[i]>0;mesh.material.opacity=mesh.userData.baseOpacity*frame.faceProgress[i]*(appearance.faceOpacity??1);});
  edges.forEach((line,i)=>{line.visible=time>=plan.scaffoldEdges[i].end;});
  markers.forEach(({ring,dot},i)=>{const d=frame.dotStates[i];ring.visible=d.visible&&d.fill<1;dot.visible=d.visible&&d.fill>0;dot.material.opacity=d.fill;});
  const anchors=plan.dots.flatMap((d,i)=>frame.dotStates[i].visible?[{id:d.id,name:frame.dotStates[i].fill===1?'witnessed vertex':'candidate',point:d.point,normal:d.normal}]:[]);
  Object.assign(group.userData,{cellulationCells:[...previous.userData.cellulationCells,...frame.completedCells],cellulationAnchors:[...previous.userData.cellulationAnchors,...anchors],cellulationPoints:[...previous.userData.cellulationPoints,...model.shellFace.newCells.flatMap(c=>c.vertices)]});
  const activeClaims=[...(previous.userData.dotClaims??[]),...(plan.dotClaims??[]).filter(c=>c.at<=time)];
  group.userData.dotClaims=activeClaims;
  if(witness.claimCount!==activeClaims.length){
   const compatibility=analyzeDotCompatibility(activeClaims);group.userData.dotCompatibility=compatibility;
   Object.assign(witness,{claimCount:activeClaims.length,compatibilityStatus:compatibility.status,unresolvedVertices:compatibility.unresolvedVertices,sourceRoleViolations:compatibility.sourceViolations.length,dot422:compatibility.readings.find(r=>r.point==='4,2,2')??null});
  }
  const action=manual?Math.min(appearance.cellulationWitnessAction,plan.events.length-1):frame.action,current=plan.events[action];
  Object.assign(animation,{phase:frame.phase,action:frame.action,totalActions:plan.events.length,progress:plan.duration?Math.min(1,time/plan.duration):0,completedCells:frame.completedCells.length});
  Object.assign(witness,{phase:manual?`${current?.type??frame.phase} (completed)`:frame.phase,action,totalActions:plan.events.length,cell:current?.cell??null,requires:current?.requires??[],duration:plan.duration,blockers:plan.blockers,newOpposingArrows:plan.arrows.filter(a=>a.oppositeRetained).length,completedCells:frame.completedCells.length,targetCells:model.shellFace.newCells.length,completedFaces:frame.faceProgress.filter(p=>p===1).length,scope:plan.scope});
  return !manual&&frame.phase!=='complete'&&frame.phase!=='blocked';
 };
 group.userData.animate(0,state);return group;
}
