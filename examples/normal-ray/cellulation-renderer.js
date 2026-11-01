import * as T from 'three';
import {createWitnessedShell} from './cellulation-shell-renderer.js';
import {crossEdgeDuration,crossEdgePoint,crossEdgeVector} from '../../research/realization-tower/cellulation-cross-edge.mjs';
import {cellulationEdgeContext} from '../../research/realization-tower/cellulation-neighborhood.mjs';
import {whiteCloneDuration,closingWhitePoint,closingWhiteVector} from '../../research/realization-tower/cellulation-white-clone.mjs';
import {blueCloneColour,blueCloneDuration,blueClonePoint,blueCloneVector} from '../../research/realization-tower/cellulation-blue-clone.mjs';
import {whiteRepeatAt,whiteRepeatDuration} from '../../research/realization-tower/cellulation-white-repeat.mjs';
import {cellulationCycleAt,cellulationExtensionsAt} from '../../research/realization-tower/cellulation-cycle.mjs';
import {cellulationDotAnchors} from '../../research/realization-tower/cellulation-anchors.mjs';
import {createCellulationCompletion} from './cellulation-completion-renderer.js';
import {completionTiming} from '../../research/realization-tower/cellulation-completion.mjs';
import {createOctahedralArrows} from './cellulation-octahedron-renderer.js';
import {cellulationRepeatAt,repeatTiming} from '../../research/realization-tower/cellulation-repeat.mjs';
import {witnessTiming} from '../../research/realization-tower/cellulation-witness.mjs';
import {createCellulationArrow} from './cellulation-arrow.js';
import {createCellulationWitness,createCellulationProposition} from './cellulation-witness-renderer.js';
// Deduplicated complete faces and elementary edges, with no role decoration.
export function createCellulation(model,state={}){
 if(model.shellFace)return createWitnessedShell(model,state,createCellulation);
 if(model.crossEdge)return createCrossEdge(model,state);
 if(model.closingWhiteClone)return createClosingWhiteClone(model,state);
 if(model.blueClone)return createBlueCellulationClone(model,state);
 if(model.retained){
  const group=new T.Group();Object.assign(group.userData,{cellulationCells:[],cellulationAnchors:[],cellulationPoints:[],animate:()=>false,audit:{source:model.source,step:model.step,cells:0,tetrahedra:0,octahedra:0,faces:0,edges:0}});return group;
 }
 if(model.whiteRepeats)return createWhiteCellulationRepeats(model,state);
 if(model.solidClosure)return createSolidCellulationClosure(model,state);
 if(model.sequentialFaces)return createSequentialCellulationFaces(model,state);
 if(model.triangleClosure)return createCellulationTriangleClosure(model,state);
 if(model.faceClosure)return createCellulationFaceClosure(model,state);
 if(model.directedArrow)return createDirectedCellulationArrow(model,state);
 if(model.extensions)return createCellulationExtensions(model,state);
 if(model.cycle)return createCellulationCycle(model,state);
 if(model.bridge)return createBridgedCellulation(model,state);
 if(model.repeat)return createRepeatedCellulation(model,state);
 const group=new T.Group();group.visible=state.bodies!==false;group.userData.cellulationCells=model.cells;group.userData.cellulationAnchors=cellulationDotAnchors(model);
 if(model.fade)group.userData.cellulationDepth={normal:{value:new T.Vector3(0,0,1)},center:{value:new T.Vector3(...model.fade.center)},width:{value:model.cellSize}};
 function depthFade(material){
  if(!model.fade)return material;
  material.onBeforeCompile=shader=>{
   const u=group.userData.cellulationDepth;Object.assign(shader.uniforms,{cellNormal:u.normal,cellCenter:u.center,cellDepth:u.width});
   shader.vertexShader='varying vec3 cellWorld;\n'+shader.vertexShader;
   shader.vertexShader=shader.vertexShader.replace('#include <begin_vertex>','#include <begin_vertex>\ncellWorld=(modelMatrix*vec4(position,1.0)).xyz;');
   shader.fragmentShader='varying vec3 cellWorld; uniform vec3 cellNormal; uniform vec3 cellCenter; uniform float cellDepth;\n'+shader.fragmentShader;
   shader.fragmentShader=shader.fragmentShader.replace('#include <color_fragment>','#include <color_fragment>\ndiffuseColor.a *= exp(-pow(dot(cellWorld-cellCenter,cellNormal)/cellDepth,2.0));');
  };
  return material;
 }
 function geometryOf(records){
  const points=records.flatMap(f=>f.vertices),geometry=new T.BufferGeometry().setFromPoints(points.map(p=>new T.Vector3(...p)));
  if(model.fade){const {center,radius,width}=model.fade;geometry.setAttribute('color',new T.Float32BufferAttribute(points.flatMap(p=>{const t=model.fade.viewport?1:Math.max(0,Math.min(1,(radius-Math.hypot(...p.map((x,i)=>x-center[i])))/width));return [1,1,1,t*t*(3-2*t)];}),4));}
  return geometry;
 }
 const geometry=geometryOf(model.faces),baseOpacity=model.fade ? .03 : .12;
 const faces=new T.Mesh(geometry,new T.MeshBasicMaterial({color:0xb8cde7,side:T.DoubleSide,transparent:true,opacity:baseOpacity*(state.faceOpacity??1),vertexColors:!!model.fade,depthWrite:false}));
 faces.visible=!state.edgesOnly;faces.userData.cellulationFaces=true;faces.userData.baseOpacity=baseOpacity;depthFade(faces.material);group.add(faces);
 group.add(new T.LineSegments(geometryOf(model.edges),new T.LineBasicMaterial({color:0x8ba9d0,transparent:true,opacity:model.fade ? .35 : .65,vertexColors:!!model.fade,depthWrite:false})));
 depthFade(group.children[1].material);
 for(const arrow of model.arrows??[])group.add(createCellulationArrow(arrow,model.cellSize));
 if(model.markedVertex){
  const dot=new T.Mesh(new T.SphereGeometry(.025*model.cellSize,16,12),new T.MeshBasicMaterial({color:0xffffff,transparent:true,depthTest:false,depthWrite:false}));
  dot.position.fromArray(model.markedVertex);dot.renderOrder=10;dot.userData.vertexMarker=true;group.add(dot);
 }
 group.userData.audit={source:model.source,step:model.step,proposedVertex:model.proposedVertex??null,arrows:model.arrows??[],markedVertex:model.markedVertex??null,vertexMarkers:model.markedVertex?1:0,cellSize:model.cellSize,window:model.window,cells:model.cells.length,tetrahedra:model.cells.filter(c=>c.kind==='tetrahedron').length,octahedra:model.cells.filter(c=>c.kind==='octahedron').length,faces:model.faces.length,edges:model.edges.length,interiorFaces:model.faces.filter(f=>f.owners.length===2).length,labels:0,internalOctahedralDiagonals:0};
 if(model.proposedVertex&&!model.witness)group.add(createCellulationProposition(model.proposedVertex,model.cellSize));
 if(model.witness){
  const witness=createCellulationWitness(model.witness,model.cellSize);group.add(witness.group);
  const completion=model.completion?createCellulationCompletion(model.completion,model.cellSize):null;if(completion)group.add(completion.group);
  group.userData.audit.animation=completion?.audit??witness.audit;
  group.userData.animate=(elapsed,appearance)=>{
   let active;
   if(completion){
    active=completion.update(elapsed,appearance);witness.update(witnessTiming.total,appearance,completion.audit.vertexFillProgress);
    Object.assign(completion.audit,{turnMarkers:witness.audit.turnMarkers,redFaceCount:witness.audit.redFaceCount,whiteDotVisible:witness.audit.whiteDotVisible,proposalVisible:witness.audit.proposalVisible});
   }else active=witness.update(elapsed,appearance);
   group.userData.cellulationAnchors=cellulationDotAnchors(model,witness.audit.turnMarkers);return active;
  };
  group.userData.animate(0,state);
 }
 return group;
}

function createCrossEdge(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),chain=model.crossEdge,copy=createCellulation(chain.source,state),animation={};
 previous.userData.animate(Infinity,state);copy.userData.animate(Infinity,state);
 const arrows=chain.arrows.map(a=>createCellulationArrow(a,model.cellSize)),contexts=chain.arrows.map(a=>cellulationEdgeContext(a.from,a.to,model.cellSize));
 const key=p=>p.map(x=>Math.round(x*Math.SQRT2/model.cellSize)).join(','),faceKey=f=>f.map(key).sort().join('|'),edgeKey=(a,b)=>[key(a),key(b)].sort().join('|'),map=p=>crossEdgePoint(chain,p);
 const existing=new Set(previous.userData.cellulationAnchors.map(a=>key(a.point))),existingFaces=new Set(model.previous.faces.map(f=>faceKey(f.vertices))),oldCells=model.previous.cells.map(c=>new Set(c.vertices.map(key))),mainEdges=new Set(chain.arrows.map(a=>edgeKey(a.from,a.to)));
 const direction=new T.Vector3(...chain.points.at(-1)).sub(new T.Vector3(...chain.points[0])).normalize(),origin=new T.Vector3(...chain.points[0]);
 const stage=points=>Math.max(1,Math.min(6,Math.ceil(Math.max(...points.map(p=>new T.Vector3(...p).sub(origin).dot(direction)/model.cellSize))-1e-7)));
 const r=chain.linearTransform;copy.matrixAutoUpdate=false;copy.matrix.set(...r[0],0,...r[1],0,...r[2],0,0,0,0,1);copy.matrix.setPosition(new T.Vector3(...chain.attachment).sub(new T.Vector3(...chain.sourceStart).applyMatrix4(copy.matrix)));copy.matrixWorldNeedsUpdate=true;
 group.add(previous,copy,...arrows);group.visible=state.bodies!==false;group.updateWorldMatrix(true,true);
 const inverse=group.matrixWorld.clone().invert(),pieces=[],hidden=[];
 copy.traverse(o=>{
  if(o.material){for(const material of Array.isArray(o.material)?o.material:[o.material])material.color?.setHex(0xffffff);}
  const arrow=o.userData.cellulationArrow;
  if(arrow){const a=map(arrow.from),b=map(arrow.to);if(mainEdges.has(edgeKey(a,b))||oldCells.some(vertices=>vertices.has(key(a))&&vertices.has(key(b))))hidden.push(o);}
  if(!o.geometry)return;
  const matrix=new T.Matrix4().multiplyMatrices(inverse,o.matrixWorld),isFace=o.isMesh&&o.geometry.type==='BufferGeometry'&&!o.geometry.index;
  if(isFace){
   const original=Array.from(o.geometry.attributes.position.array),trimmed=[];
   for(let i=0;i<original.length;i+=9){const triangle=original.slice(i,i+9),points=[0,3,6].map(j=>new T.Vector3(...triangle.slice(j,j+3)).applyMatrix4(matrix).toArray());if(!existingFaces.has(faceKey(points)))trimmed.push(...triangle);}
   if(trimmed.length!==original.length){o.geometry.dispose();o.geometry.setAttribute('position',new T.Float32BufferAttribute(trimmed,3));o.geometry.boundingBox=null;o.geometry.boundingSphere=null;}
  }
  if(['SphereGeometry','RingGeometry'].includes(o.geometry.type)&&existing.has(key(new T.Vector3().setFromMatrixPosition(matrix).toArray())))hidden.push(o);
  const position=o.geometry.attributes.position,points=Array.from({length:position.count},(_,i)=>new T.Vector3().fromBufferAttribute(position,i).applyMatrix4(matrix).toArray());
  const marker=['SphereGeometry','RingGeometry'].includes(o.geometry.type);
  pieces.push({o,visible:o.visible&&points.length>0,isFace,stage:stage(marker?[new T.Vector3().setFromMatrixPosition(matrix).toArray()]:points)});
 });
 const axisKeys=new Set(chain.points.slice(1,-1).map(key)),copiedAnchors=copy.userData.cellulationAnchors.map(a=>{const point=map(a.point);return {...a,id:axisKeys.has(key(point))?`${chain.axisPrefix}${key(point)}`:`${chain.prefix}${a.id}`,point,normal:crossEdgeVector(chain,a.normal),stage:stage([point])};}).filter(a=>!existing.has(key(a.point)));
 const cellStages=chain.newCells.map(c=>({cell:c,stage:stage(c.vertices)}));
 group.userData.audit={...previous.userData.audit,step:model.step,previous:previous.userData.audit,cells:model.cells.length,tetrahedra:model.cells.filter(c=>c.kind==='tetrahedron').length,octahedra:model.cells.filter(c=>c.kind==='octahedron').length,faces:previous.userData.audit.faces+model.faces.filter(f=>!existingFaces.has(faceKey(f.vertices))).length,edges:model.edges.length,arrows:chain.arrows,latticePath:chain.latticePoints,newTetrahedra:chain.newCells.filter(c=>c.kind==='tetrahedron').length,newOctahedra:chain.newCells.filter(c=>c.kind==='octahedron').length,animation};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous.userData.animate(Infinity,appearance);copy.userData.animate(Infinity,appearance);
  const progress=arrows.map((_,i)=>Math.max(0,Math.min(1,elapsed/(crossEdgeDuration/arrows.length)-i))),completed=progress.filter(p=>p===1).length;
  arrows.forEach((a,i)=>a.userData.setProgress(progress[i]));
  for(const p of pieces)p.o.visible=p.visible&&p.stage<=completed&&!(p.isFace&&appearance.edgesOnly);
  for(const o of hidden)o.visible=false;
  const complete=completed===6,added=cellStages.filter(c=>c.stage<=completed).map(c=>c.cell),anchors=copiedAnchors.filter(a=>a.stage<=completed).map(({stage,...a})=>a);
  Object.assign(group.userData,{cellulationCells:[...previous.userData.cellulationCells,...added],cellulationAnchors:[...previous.userData.cellulationAnchors,...anchors],cellulationPoints:[...previous.userData.cellulationPoints,...chain.cells.flatMap(c=>c.vertices)],cellulationGridSeeds:contexts.flatMap((cells,i)=>progress[i]>0?cells:[])});
  Object.assign(animation,{phase:complete?'complete':'growing-cross-complex',progress,completedArrows:completed,completedCells:added.length,newDots:anchors.length});return !complete;
 };
 group.userData.animate(0,state);return group;
}

function createClosingWhiteClone(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),clone=model.closingWhiteClone,copy=createCellulation(clone.source,state),animation={};
 copy.matrixAutoUpdate=false;group.add(previous,copy);group.visible=state.bodies!==false;
 const key=p=>p.map(x=>Math.round(x*Math.SQRT2/model.cellSize)).join(','),map=point=>closingWhitePoint(clone,point);
 const sharedFaces=new Set(clone.sharedCells.flatMap(c=>c.faces).map(f=>f.map(key).sort().join('|'))),sharedVertices=clone.sharedCells.map(c=>new Set(c.vertices.map(key))),masked=[];
 copy.traverse(o=>{
  if(!o.isMesh||o.geometry?.type!=='BufferGeometry'||o.geometry.index||Object.keys(o.geometry.attributes).length!==1)return;
  const original=Array.from(o.geometry.attributes.position.array),trimmed=[];
  for(let i=0;i<original.length;i+=9){const triangle=original.slice(i,i+9),face=[0,3,6].map(j=>key(map(triangle.slice(j,j+3)))).sort().join('|');if(!sharedFaces.has(face))trimmed.push(...triangle);}
  if(trimmed.length!==original.length)masked.push({o,original,trimmed});
 });
 let maskedComplete=false,suppressed=[];const axis=new T.Vector3(...clone.rotationAxis),inversion=new T.Matrix4().makeScale(-1,-1,-1),r=clone.linearTransform,target=new T.Matrix4().set(...r[0],0,...r[1],0,...r[2],0,0,0,0,1);
 group.userData.audit={source:model.source,step:model.step,cellSize:model.cellSize,cells:model.cells.length,tetrahedra:model.cells.filter(c=>c.kind==='tetrahedron').length,octahedra:model.cells.filter(c=>c.kind==='octahedron').length,faces:previous.userData.audit.faces+copy.userData.audit.faces-sharedFaces.size,edges:model.edges.length,arrows:clone.arrows,attachmentLattice:clone.attachmentLattice,endLattice:clone.endLattice,reflectionPoint:clone.reflectionPoint,rotationDegrees:clone.rotationDegrees,sharedCells:clone.sharedCells.length,previous:previous.userData.audit,animation};
 group.userData.animate=(elapsed,appearance=state)=>{
  for(const o of suppressed)o.visible=true;suppressed=[];previous.userData.animate(Infinity,appearance);copy.userData.animate(Infinity,appearance);
  const progress=Math.max(0,Math.min(1,elapsed/whiteCloneDuration)),complete=progress===1,matrix=complete?target.clone():new T.Matrix4().makeRotationAxis(axis,progress*Math.PI/2).multiply(inversion);
  matrix.setPosition(new T.Vector3(...clone.attachment).sub(new T.Vector3(...clone.sourceStart).applyMatrix4(matrix)));copy.matrix.copy(matrix);copy.matrixWorldNeedsUpdate=true;
  if(maskedComplete!==complete){maskedComplete=complete;for(const {o,original,trimmed} of masked){o.geometry.dispose();o.geometry.setAttribute('position',new T.Float32BufferAttribute(complete?trimmed:original,3));o.geometry.boundingSphere=null;o.geometry.boundingBox=null;}}
  const anchors=[...previous.userData.cellulationAnchors],seen=new Set(anchors.map(a=>key(a.point))),prior=new Set(seen);
  if(complete){
   for(const a of copy.userData.cellulationAnchors){const point=map(a.point);if(seen.has(key(point)))continue;seen.add(key(point));anchors.push({...a,id:`closing-white:${a.id}`,point,normal:closingWhiteVector(clone,a.normal)});}
   group.updateWorldMatrix(true,true);const inverse=group.matrixWorld.clone().invert();
   copy.traverse(o=>{
    if(!o.visible)return;const arrow=o.userData.cellulationArrow;
    const sharedArrow=arrow&&sharedVertices.some(vertices=>vertices.has(key(map(arrow.from)))&&vertices.has(key(map(arrow.to))));
    const sharedDot=['SphereGeometry','RingGeometry'].includes(o.geometry?.type)&&prior.has(key(new T.Vector3().setFromMatrixPosition(o.matrixWorld).applyMatrix4(inverse).toArray()));
    if(sharedArrow||sharedDot){suppressed.push(o);o.visible=false;}
   });
  }
  Object.assign(group.userData,{cellulationAnchors:anchors,cellulationCells:complete?model.cells:previous.userData.cellulationCells,cellulationPoints:[...previous.userData.cellulationPoints,...copy.userData.cellulationPoints.map(p=>new T.Vector3(...p).applyMatrix4(matrix).toArray())]});
  Object.assign(animation,{phase:complete?'complete':'turning-closing-white-bar',progress,rotationDegrees:progress*90,closed:complete});return !complete;
 };
 group.userData.animate(0,state);return group;
}

function createBlueCellulationClone(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),clone=model.blueClone,copy=createCellulation(clone.source,state),animation={};
 copy.traverse(o=>{for(const material of o.material?(Array.isArray(o.material)?o.material:[o.material]):[])if(material.color?.getHex()===0xff3030){material.color.setHex(blueCloneColour);o.renderOrder+=1;}});
 copy.matrixAutoUpdate=false;group.add(previous,copy);group.visible=state.bodies!==false;
 const axis=new T.Vector3(...clone.axialNormal),base=new T.Matrix4().makeScale(...clone.axisSigns),r=clone.linearTransform;
 const target=new T.Matrix4().set(...r[0],0,...r[1],0,...r[2],0,0,0,0,1);
 const sharedFaces=new Set(clone.sharedCells.flatMap(c=>c.faces).map(face=>face.map(p=>p.map(x=>Math.round(x*Math.SQRT2/model.cellSize)).join(',')).sort().join('|'))),masked=[];
 previous.traverse(o=>{
  if(!o.isMesh||o.geometry?.type!=='BufferGeometry'||o.geometry.index||Object.keys(o.geometry.attributes).length!==1)return;
  const original=Array.from(o.geometry.attributes.position.array),trimmed=[];
  for(let i=0;i<original.length;i+=9){const triangle=original.slice(i,i+9),keys=[0,3,6].map(j=>triangle.slice(j,j+3).map(x=>Math.round(x*Math.SQRT2/model.cellSize)).join(',')).sort().join('|');if(!sharedFaces.has(keys))trimmed.push(...triangle);}
  if(trimmed.length!==original.length)masked.push({o,original,trimmed});
 });
 let maskedComplete=false;
 const key=p=>p.map(x=>Math.round(x*Math.SQRT2/model.cellSize)).join(',');let suppressed=[];
 group.userData.audit={source:model.source,step:model.step,cellSize:model.cellSize,cells:model.cells.length,tetrahedra:model.cells.filter(c=>c.kind==='tetrahedron').length,octahedra:model.cells.filter(c=>c.kind==='octahedron').length,faces:previous.userData.audit.faces+copy.userData.audit.faces-sharedFaces.size,sharedCells:clone.sharedCells.length,axialNormal:clone.axialNormal,edges:model.edges.length,arrows:clone.arrows,attachmentLattice:clone.attachmentLattice,endLattice:clone.endLattice,reflectionNormal:clone.normal,rotationDegrees:clone.rotationDegrees,previous:previous.userData.audit,animation};
 group.userData.animate=(elapsed,appearance=state)=>{
  for(const marker of suppressed)marker.visible=true;suppressed=[];
  previous.userData.animate(Infinity,appearance);copy.userData.animate(Infinity,appearance);
  const progress=Math.max(0,Math.min(1,elapsed/blueCloneDuration));
  const matrix=progress===1?target.clone():new T.Matrix4().makeRotationAxis(axis,progress*Math.PI).multiply(base);
  if(maskedComplete!==(progress===1)){
   maskedComplete=progress===1;for(const {o,original,trimmed} of masked){o.geometry.dispose();o.geometry.setAttribute('position',new T.Float32BufferAttribute(maskedComplete?trimmed:original,3));o.geometry.boundingSphere=null;o.geometry.boundingBox=null;}
  }
  matrix.setPosition(new T.Vector3(...clone.attachment).sub(new T.Vector3(...clone.sourceStart).applyMatrix4(matrix)));
  copy.matrix.copy(matrix);copy.matrixWorldNeedsUpdate=true;
  const anchors=[...previous.userData.cellulationAnchors],seen=new Set(anchors.map(a=>key(a.point)));
  if(progress===1)for(const a of copy.userData.cellulationAnchors){const point=blueClonePoint(clone,a.point);if(seen.has(key(point)))continue;seen.add(key(point));anchors.push({...a,id:`blue:${a.id}`,point,normal:blueCloneVector(clone,a.normal)});}
  // Preserve the existing dot and its ID/color at shared attachment vertices.
  group.updateWorldMatrix(true,true);const inverse=group.matrixWorld.clone().invert(),prior=new Set(previous.userData.cellulationAnchors.map(a=>key(a.point)));
  copy.traverse(o=>{if(o.visible&&['SphereGeometry','RingGeometry'].includes(o.geometry?.type)){
   const point=new T.Vector3().setFromMatrixPosition(o.matrixWorld).applyMatrix4(inverse);
   if(progress===1&&prior.has(key(point.toArray()))||point.distanceTo(new T.Vector3(...clone.attachment))<1e-8){suppressed.push(o);o.visible=false;}
  }});
  Object.assign(group.userData,{cellulationAnchors:anchors,cellulationCells:progress===1?model.cells:previous.userData.cellulationCells,cellulationPoints:[...previous.userData.cellulationPoints,...clone.source.cells.flatMap(c=>c.vertices).map(p=>new T.Vector3(...p).applyMatrix4(matrix).toArray())]});
  Object.assign(animation,{phase:progress===1?'complete':'rolling-blue-clone',progress,rotationDegrees:clone.rotationDegrees*progress,blueArrowCount:clone.arrows.length,sharedDots:suppressed.length});return progress<1;
 };
 group.userData.animate(0,state);return group;
}

function createWhiteCellulationRepeats(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),cycles=model.whiteRepeats.map(c=>c.stages.map(m=>createCellulation(m,state))),animation={};
 group.add(previous,...cycles.flat());group.visible=state.bodies!==false;
 group.userData.audit={source:model.source,step:model.step,cellSize:model.cellSize,cells:model.cells.length,tetrahedra:model.cells.filter(c=>c.kind==='tetrahedron').length,octahedra:model.cells.filter(c=>c.kind==='octahedron').length,faces:previous.userData.audit.faces+cycles.reduce((sum,c)=>sum+c.at(-1).userData.audit.faces,0),edges:model.edges.length,labels:0,previous:previous.userData.audit,animation};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous.userData.animate(Infinity,appearance);const frame=whiteRepeatAt(elapsed);
  const anchors=[...previous.userData.cellulationAnchors],cells=[...previous.userData.cellulationCells],points=[...previous.userData.cellulationPoints];
  cycles.forEach((stages,i)=>{
   const done=i<frame.completed,local=done?whiteRepeatAt(Infinity):whiteRepeatAt(Math.max(0,elapsed-i*whiteRepeatDuration)),active=stages[done?stages.length-1:local.stage];
   stages.forEach(s=>{s.visible=i<=frame.index&&s===active&&appearance.bodies!==false;});if(i>frame.index)return;
   active.userData.animate(done?Infinity:local.localElapsed,appearance);
   anchors.push(...active.userData.cellulationAnchors);cells.push(...active.userData.cellulationCells);points.push(...active.userData.cellulationPoints);
  });
  Object.assign(group.userData,{cellulationAnchors:anchors,cellulationCells:cells,cellulationPoints:points});
  Object.assign(animation,frame,{current:cycles[frame.index][frame.stage].userData.audit,dotCount:anchors.length});return frame.active;
 };
 group.userData.animate(0,state);return group;
}

function createSolidCellulationClosure(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),closure=model.solidClosure,completion=createCellulationCompletion(closure,model.cellSize);
 const dots=closure.filledVertices.map(point=>{
  const dot=new T.Mesh(new T.SphereGeometry(.025*model.cellSize,16,12),new T.MeshBasicMaterial({color:0xffffff,transparent:true,depthTest:false,depthWrite:false}));
  dot.position.fromArray(point);dot.renderOrder=12;return dot;
 });
 group.add(previous,completion.group,...dots);group.visible=state.bodies!==false;
 group.userData.cellulationPoints=[...(previous.userData.cellulationPoints??[]),...closure.faces.flat()];
 group.userData.audit={...previous.userData.audit,step:model.step,previous:previous.userData.audit,cells:model.cells.length,tetrahedra:model.cells.filter(c=>c.kind==='tetrahedron').length,arrows:[closure.arrow],whiteFaces:closure.faces,latticeFaces:closure.latticeFaces,latticeRectangle:closure.latticeRectangle,filledLatticeVertices:closure.filledLatticeVertices,faces:previous.userData.audit.faces+closure.faces.length,edges:model.edges.length,interiorFaces:model.faces.filter(f=>f.owners.length===2).length,animation:completion.audit};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous.userData.animate(Infinity,appearance);group.userData.cellulationAnchors=previous.userData.cellulationAnchors;
  const t=elapsed<1000?completionTiming.hold+completionTiming.edge*Math.max(0,elapsed)/1000:completionTiming.hold+completionTiming.edge+elapsed-1000;
  const active=completion.update(t,appearance),fill=completion.audit.vertexFillProgress;
  for(const dot of dots){dot.visible=fill>0;dot.scale.setScalar(fill);}
  group.userData.cellulationCells=completion.audit.arrowProgress===1?model.cells:model.previous.cells;
  completion.audit.filledDotCount=fill>0?dots.length:0;
  completion.audit.whiteRectangleCount=closure.latticeRectangle&&completion.audit.whiteFaceCount>0?1:0;return active;
 };
 group.userData.animate(0,state);return group;
}

function createSequentialCellulationFaces(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),parts=model.sequentialFaces.map(f=>createCellulationCompletion(f,model.cellSize)),animation={};
 group.add(previous,...parts.map(p=>p.group));group.visible=state.bodies!==false;
 group.userData.cellulationCells=model.cells;
 group.userData.cellulationPoints=[...(previous.userData.cellulationPoints??[]),...model.sequentialFaces.flatMap(f=>f.faces.flat())];
 group.userData.audit={...previous.userData.audit,step:model.step,previous:previous.userData.audit,arrows:model.sequentialFaces.map(f=>f.arrow),whiteFaces:model.sequentialFaces.flatMap(f=>f.faces),latticeFaces:model.sequentialFaces.map(f=>f.latticeFace),faces:previous.userData.audit.faces+parts.length,animation};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous.userData.animate(Infinity,appearance);group.userData.cellulationAnchors=previous.userData.cellulationAnchors;
  parts.forEach((part,i)=>{
   const local=Math.max(0,elapsed-i*1650),t=local<1000?completionTiming.hold+completionTiming.edge*local/1000:completionTiming.hold+completionTiming.edge+completionTiming.vertices+local-1000;
   part.update(t,appearance);
  });
  const index=Math.min(parts.length-1,Math.floor(Math.max(0,elapsed)/1650));
  Object.assign(animation,parts[index].audit,{index,parts:parts.map(p=>p.audit),whiteFaceCount:parts.reduce((sum,p)=>sum+p.audit.whiteFaceCount,0)});
  return elapsed<parts.length*1650;
 };
 group.userData.animate(0,state);return group;
}

function createCellulationTriangleClosure(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),closure=model.triangleClosure;
 const first=createCellulationArrow(closure.arrows[0],model.cellSize),completion=createCellulationCompletion({arrow:closure.arrows[1],faces:[closure.face]},model.cellSize),animation={};
 const candidate=createCellulationProposition(closure.arrows[0].to,model.cellSize);
 const candidateAnchor={id:`${model.anchorPrefix??''}step${model.step}:candidate`,name:'candidate',point:[...closure.arrows[0].to],normal:new T.Vector3(...closure.arrows[0].to).sub(new T.Vector3(...closure.arrows[0].from)).normalize().toArray()};
 group.add(previous,first,completion.group,candidate);group.visible=state.bodies!==false;
 group.userData.cellulationCells=model.cells;
 group.userData.cellulationPoints=[...(previous.userData.cellulationPoints??[]),...closure.face];
 group.userData.audit={...previous.userData.audit,step:model.step,previous:previous.userData.audit,arrows:closure.arrows,whiteFaces:[closure.face],latticeFace:closure.latticeFace,faces:previous.userData.audit.faces+1,animation};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous.userData.animate(Infinity,appearance);group.userData.cellulationAnchors=previous.userData.cellulationAnchors;
  const firstProgress=Math.max(0,Math.min(1,elapsed/1000));first.userData.setProgress(firstProgress);candidate.visible=firstProgress===1;
  group.userData.cellulationAnchors=[...previous.userData.cellulationAnchors,...(candidate.visible?[candidateAnchor]:[])];
  const local=Math.max(0,elapsed-1000),t=local<1000?completionTiming.hold+completionTiming.edge*local/1000:completionTiming.hold+completionTiming.edge+completionTiming.vertices+local-1000;
  const active=completion.update(t,appearance);
  Object.assign(animation,completion.audit,{candidateVisible:candidate.visible,firstArrowProgress:firstProgress,secondArrowProgress:completion.audit.arrowProgress,phase:elapsed<1000?'first-arrow':completion.audit.phase});
  return elapsed<1000||active;
 };
 group.userData.animate(0,state);return group;
}

function createCellulationFaceClosure(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),completion=createCellulationCompletion(model.faceClosure,model.cellSize),finish=createCellulationCompletion(model.faceClosure.finish,model.cellSize),animation={};
 const dot=new T.Mesh(new T.SphereGeometry(.025*model.cellSize,16,12),new T.MeshBasicMaterial({color:0xffffff,transparent:true,depthTest:false,depthWrite:false}));
 dot.position.fromArray(model.faceClosure.finish.filledVertex);dot.renderOrder=12;
 group.add(previous,completion.group,finish.group,dot);group.visible=state.bodies!==false;
 group.userData.cellulationPoints=[...(previous.userData.cellulationPoints??[]),...model.faceClosure.faces.flat(),...model.faceClosure.finish.faces.flat()];
 group.userData.audit={...previous.userData.audit,step:model.step,previous:previous.userData.audit,cells:model.cells.length,tetrahedra:model.cells.filter(c=>c.kind==='tetrahedron').length,arrows:[model.faceClosure.arrow,model.faceClosure.finish.arrow],whiteFaces:[...model.faceClosure.faces,...model.faceClosure.finish.faces],latticeFace:model.faceClosure.latticeFace,newlyClosedLatticeFaces:model.faceClosure.finish.latticeFaces,faces:model.faces.length,edges:model.edges.length,interiorFaces:model.faces.filter(f=>f.owners.length===2).length,animation};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous.userData.animate(Infinity,appearance);group.userData.cellulationAnchors=previous.userData.cellulationAnchors;
  // First close 918/927/828, then draw 927→817, fill 927 and the two remaining faces.
  const t=elapsed<1000?completionTiming.hold+completionTiming.edge*Math.max(0,elapsed)/1000:completionTiming.hold+completionTiming.edge+completionTiming.vertices+elapsed-1000;
  completion.update(elapsed>=1650?Infinity:t,appearance);
  const local=Math.max(0,elapsed-1650),lastTime=local<1000?completionTiming.hold+completionTiming.edge*local/1000:completionTiming.hold+completionTiming.edge+local-1000;
  const active=finish.update(lastTime,appearance),fill=finish.audit.vertexFillProgress;
  dot.visible=fill>0;dot.scale.setScalar(fill);
  group.userData.cellulationCells=finish.audit.arrowProgress===1?model.cells:model.previous.cells;
  Object.assign(animation,elapsed<1650?completion.audit:finish.audit,{first:completion.audit,finish:finish.audit,vertexFillProgress:fill,filledDotVisible:dot.visible,newlyClosedFaceCount:finish.audit.whiteFaceCount,whiteFaceCount:completion.audit.whiteFaceCount+finish.audit.whiteFaceCount,whiteFaceOpacity:Math.max(completion.audit.whiteFaceOpacity,finish.audit.whiteFaceOpacity)});
  return elapsed<1650||active;
 };
 group.userData.animate(0,state);return group;
}

function createDirectedCellulationArrow(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),arrow=createCellulationArrow(model.directedArrow,model.cellSize),animation={};
 const candidate=createCellulationProposition(model.directedArrow.to,model.cellSize);
 const candidateAnchor={id:`${model.anchorPrefix??''}step${model.step}:candidate`,name:'candidate',point:[...model.directedArrow.to],normal:new T.Vector3(...model.directedArrow.to).sub(new T.Vector3(...model.directedArrow.from)).normalize().toArray()};
 group.add(previous,arrow,candidate);group.visible=state.bodies!==false;
 group.userData.cellulationCells=model.cells;group.userData.cellulationPoints=[model.directedArrow.from,model.directedArrow.to];
 group.userData.audit={...previous.userData.audit,step:model.step,previous:previous.userData.audit,arrows:[model.directedArrow],proposedVertex:[...model.directedArrow.to],animation};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous.userData.animate(Infinity,appearance);
  const progress=Math.max(0,Math.min(1,elapsed/1000));arrow.userData.setProgress(progress);candidate.visible=progress===1;
  group.userData.cellulationAnchors=[...previous.userData.cellulationAnchors,...(candidate.visible?[candidateAnchor]:[])];
  Object.assign(animation,{phase:progress<1?'growing-arrow':'complete',arrowProgress:progress,candidateVisible:candidate.visible});return progress<1;
 };
 group.userData.animate(0,state);return group;
}

function createCellulationExtensions(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),cycles=model.extensions.map(m=>createCellulation(m,state)),animation={};
 group.add(previous,...cycles);group.visible=state.bodies!==false;
 group.userData.audit={source:model.source,step:model.step,cellSize:model.cellSize,cells:model.cells.length,tetrahedra:model.cells.filter(c=>c.kind==='tetrahedron').length,octahedra:model.cells.filter(c=>c.kind==='octahedron').length,faces:model.faces.length,edges:model.edges.length,interiorFaces:model.faces.filter(f=>f.owners.length===2).length,labels:0,internalOctahedralDiagonals:0,previous:previous.userData.audit,animation};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous.userData.animate(Infinity,appearance);
  group.userData.cellulationCells=[...previous.userData.cellulationCells];
  const frame=cellulationExtensionsAt(elapsed,cycles.length),anchors=[...previous.userData.cellulationAnchors],key=p=>p.map(x=>x.toFixed(8)).join(','),seen=new Set(anchors.map(a=>key(a.point)));
  cycles.forEach((cycle,i)=>{
   cycle.visible=i<=frame.index&&appearance.bodies!==false;if(i>frame.index)return;
   cycle.userData.animate(i<frame.index?Infinity:frame.localElapsed,appearance);
   group.userData.cellulationCells.push(...cycle.userData.cellulationCells);
   for(const a of cycle.userData.cellulationAnchors){if(seen.has(key(a.point)))continue;seen.add(key(a.point));anchors.push({...a,id:`extension:${i}:${a.id}`});}
  });
  group.userData.cellulationAnchors=anchors;
  Object.assign(animation,frame,{current:cycles[frame.index].userData.audit,dotCount:anchors.length});return frame.active;
 };
 group.userData.animate(0,state);return group;
}

function createCellulationCycle(model,state){
 const group=new T.Group(),previous=model.previous?createCellulation(model.previous,state):null,first=model.cycle.first.map(m=>createCellulation(m,state)),closed=createCellulation(model.cycle.closed,state),parts=[...first,closed],animation={};
 group.add(...(previous?[previous]:[]),...parts);group.visible=state.bodies!==false;
 group.userData.audit={source:model.source,step:model.step,cellSize:model.cellSize,cells:model.cells.length,tetrahedra:model.cells.filter(c=>c.kind==='tetrahedron').length,octahedra:model.cells.filter(c=>c.kind==='octahedron').length,faces:model.faces.length,edges:model.edges.length,interiorFaces:model.faces.filter(f=>f.owners.length===2).length,labels:0,internalOctahedralDiagonals:0,previous:previous?.userData.audit,animation};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous?.userData.animate(Infinity,appearance);
  const frame=cellulationCycleAt(elapsed),construction=frame.construction,active=frame.part===0?first[construction.stage-2]:closed;
  parts.forEach(p=>{p.visible=p===active&&appearance.bodies!==false;});
  if(construction?.stage===3){
   active.children.find(o=>o.userData.setProgress)?.userData.setProgress(construction.arrowProgress);
   active.children.filter(o=>o.userData.cellulationBillboard).forEach(o=>{o.visible=construction.arrowProgress===1;});
  }
  active.userData.animate?.(construction?.localElapsed??frame.localElapsed,appearance);
  group.userData.cellulationCells=[...(previous?.userData.cellulationCells??[]),...active.userData.cellulationCells];
  const anchors=[...(previous?.userData.cellulationAnchors??[])],key=p=>p.map(x=>x.toFixed(8)).join(','),seen=new Set(anchors.map(a=>key(a.point)));
  for(const a of active.userData.cellulationAnchors){
   if(construction?.stage===3&&a.id==='witness'&&construction.arrowProgress<1)continue;
   if(seen.has(key(a.point)))continue;seen.add(key(a.point));anchors.push({...a,id:`cycle:${a.id}`,name:`new ${a.name}`});
  }
  group.userData.cellulationAnchors=anchors;
  Object.assign(animation,frame,{origin:model.cycle.origin,current:active.userData.audit,dotCount:anchors.length});return frame.active;
 };
 group.userData.animate(0,state);return group;
}

function createBridgedCellulation(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),scaffold=createCellulation(model.bridge.scaffold,state),bridge=createOctahedralArrows(model.bridge,model.cellSize);
 group.add(previous,scaffold,bridge.group);group.visible=state.bodies!==false;group.userData.cellulationCells=model.cells;
 group.userData.audit={source:model.source,step:model.step,cellSize:model.cellSize,cells:model.cells.length,tetrahedra:model.cells.filter(c=>c.kind==='tetrahedron').length,octahedra:1,faces:model.faces.length,edges:model.edges.length,interiorFaces:model.faces.filter(f=>f.owners.length===2).length,labels:0,internalOctahedralDiagonals:0,previous:previous.userData.audit,animation:bridge.audit};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous.userData.animate(repeatTiming.total,appearance);const active=bridge.update(elapsed,appearance);
  group.userData.cellulationAnchors=[...previous.userData.cellulationAnchors,bridge.anchor];return active;
 };
 group.userData.animate(0,state);return group;
}

function createRepeatedCellulation(model,state){
 const group=new T.Group(),previous=createCellulation(model.previous,state),stages=model.repeat.stages.map(m=>createCellulation(m,state));
 group.add(previous,...stages);group.visible=state.bodies!==false;group.userData.cellulationCells=model.cells;
 const animation={};
 group.userData.audit={source:model.source,step:model.step,cellSize:model.cellSize,cells:model.cells.length,tetrahedra:2,octahedra:0,faces:model.faces.length,edges:model.edges.length,labels:0,internalOctahedralDiagonals:0,previous:previous.userData.audit,animation};
 group.userData.animate=(elapsed,appearance=state)=>{
  previous.userData.animate(completionTiming.total,appearance);
  const frame=cellulationRepeatAt(elapsed),active=stages[frame.stage-2];
  stages.forEach(s=>{s.visible=s===active&&appearance.bodies!==false;});
  if(frame.stage===3){
   active.children.find(o=>o.userData.setProgress)?.userData.setProgress(frame.arrowProgress);
   active.children.filter(o=>o.userData.cellulationBillboard).forEach(o=>{o.visible=frame.arrowProgress===1;});
  }
  if(active.userData.animate)active.userData.animate(frame.localElapsed,appearance);
  const anchors=[...previous.userData.cellulationAnchors],seen=new Set(anchors.map(a=>a.point.join(',')));
  for(const a of active.userData.cellulationAnchors){
   if(frame.stage===3&&a.id==='witness'&&frame.arrowProgress<1)continue;
   const key=a.point.join(',');if(seen.has(key))continue;seen.add(key);anchors.push({...a,id:`repeat:${a.id}`,name:`next ${a.name}`});
  }
  group.userData.cellulationAnchors=anchors;
  Object.assign(animation,frame,{origin:model.repeat.origin,current:active.userData.audit,dotCount:anchors.length});return frame.active;
 };
 group.userData.animate(0,state);return group;
}
