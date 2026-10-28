// Historical 0–7 construction, retained only for structural research and old geometry fixtures.
// The viewer imports cell-fibration-process.mjs, never this module.
import {buildFoldedFibration,foldedFibrationEnvelope} from './fibration-folded-process.mjs';
import {seed} from './normal-ray-model.mjs';
import {innerLayerHexReflection} from './inner-layer-hex-reflection.mjs';
export const cellFibrationStages=Object.freeze([
 'Seed the four vertex cells of the folded 12x12 carrier, with their original corner colours.',
 'Layer 1: grow three whole cells from each vertex cell, through its inward vertices. Each new cell takes the colour of its target corner.',
 'Layer 2: extend each edge branch by one lattice unit. Edge cells take their originating corner colour. Add a cell between each pair on a face, coloured by the corner opposite that face.',
 'Layer 3: join the two fronts with one midpoint cell per edge. P–E gets N; N–N gets E; P–N gets E; E–N gets P. In the same layer, add six cells per face, coloured by the nearest other corner on that face. Fill each corner’s depth-3 interior gap in its own colour.',
 'Layer 4: fill the shared interior gaps using each source’s nearest other vertex, resolving competing colours with P > N > E.',
 'Layer 5: fill the sole remaining tetrahedral cell on each carrier face, coloured by the vertex opposite that face.',
 'Complementary layer 1: at each vertex, fill only the adjoining octahedron in the vertex colour.',
 'Inner layer-2 hexagons: viewed from inside each vertex complex, the hexagon has three filled and three empty cells. Fill each empty whole cell in the colour of its opposite filled cell across the hexagon centre, except an E or P result becomes N.'
]);
const key=vs=>vs.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
const center=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i]/vs.length,0));
export function buildCellFibration(){
 const model=buildFoldedFibration(),byShape=new Map(model.geometry.map(g=>[key(g.vertices),g]));
 const corners=foldedFibrationEnvelope.map((point,i)=>{
  const matches=model.geometry.filter(g=>g.vertices.some(v=>key([v])===key([point])));
  if(matches.length!==1||matches[0].kind!=='tetrahedron')throw Error('Unique native corner tetrahedron required');
  return {vertex:i+1,point,cell:matches[0].id,role:matches[0].role,geometry:matches[0]};
 });
 const body=(g,role,layer)=>({id:g.id,kind:g.kind,vertices:g.vertices,faces:g.faces,primitiveIds:g.primitiveIds,components:[],role,layer});
 const seeds=corners.map(c=>body(c.geometry,c.role,0)),growth=[];
 for(const source of corners)for(const target of corners.filter(c=>c!==source)){
  const delta=target.point.map((x,i)=>(x-source.point[i])/7),attachment=source.point.map((x,i)=>x+delta[i]);
  if(!source.geometry.vertices.some(v=>key([v])===key([attachment])))throw Error('Target direction must pass through an inward source vertex');
  const translated=source.geometry.vertices.map(v=>v.map((x,i)=>x+delta[i])),child=byShape.get(key(translated));
  if(!child||child.kind!=='tetrahedron')throw Error('Growth must use an existing whole lattice cell');
  const shared=child.vertices.filter(v=>source.geometry.vertices.some(w=>key([w])===key([v])));
  if(shared.length!==1||key(shared)!==key([attachment]))throw Error('Growth must attach at exactly one vertex, not a face');
  growth.push({source:source.vertex,target:target.vertex,parent:source.cell,attachment,body:body(child,target.role,1)});
 }
 if(new Set([...seeds,...growth.map(g=>g.body)].map(b=>b.id)).size!==16)throw Error('Layer 1 collides with another cell');
 const edgeGrowth=growth.map(previous=>{
  const source=corners.find(c=>c.vertex===previous.source),target=corners.find(c=>c.vertex===previous.target);
  const delta=target.point.map((x,i)=>(x-source.point[i])/7);
  const child=byShape.get(key(previous.body.vertices.map(v=>v.map((x,i)=>x+delta[i]))));
  if(!child||child.kind!=='tetrahedron')throw Error('Edge extension must use a whole native tetrahedron');
  const attachment=previous.attachment.map((x,i)=>x+delta[i]);
  const shared=child.vertices.filter(v=>previous.body.vertices.some(w=>key([w])===key([v])));
  if(shared.length!==1||key(shared)!==key([attachment]))throw Error('Edge extension must attach at its forward vertex');
  return {source:source.vertex,target:target.vertex,parent:previous.body.id,attachment,body:body(child,source.role,2)};
 });
 if(new Set([...seeds,...growth.map(g=>g.body),...edgeGrowth.map(g=>g.body)].map(b=>b.id)).size!==28)throw Error('Layer 2 collides with retained cells');
 const faceGrowth=[];
 for(const source of corners){
  const others=corners.filter(c=>c!==source);
  for(let i=0;i<others.length;i++)for(let j=i+1;j<others.length;j++){
   const a=others[i],b=others[j],opposite=others.find(c=>c!==a&&c!==b);
   const delta=source.point.map((x,k)=>(a.point[k]+b.point[k]-2*x)/7);
   const child=byShape.get(key(source.geometry.vertices.map(v=>v.map((x,k)=>x+delta[k]))));
   if(!child||child.kind!=='tetrahedron')throw Error('Face growth must use a whole native tetrahedron');
   const parents=[a,b].map(target=>edgeGrowth.find(g=>g.source===source.vertex&&g.target===target.vertex));
   const attachments=parents.map(parent=>{
    const shared=child.vertices.filter(v=>parent.body.vertices.some(w=>key([w])===key([v])));
    if(shared.length!==1)throw Error('Face cell must meet both new edge cells at vertices');
    return {parent:parent.body.id,point:shared[0]};
   });
   const axis=source.point.findIndex((x,k)=>a.point[k]===x&&b.point[k]===x&&opposite.point[k]!==x);
   if(axis<0||!child.faces.some(f=>f.every(v=>v[axis]===source.point[axis])))throw Error('Face cell must lie on its stated carrier face');
   faceGrowth.push({source:source.vertex,face:[source.vertex,a.vertex,b.vertex].sort(),opposite:opposite.vertex,attachments,kind:'face',body:body(child,opposite.role,2)});
  }
 }
 if(new Set([...seeds,...growth.map(g=>g.body),...edgeGrowth.map(g=>g.body),...faceGrowth.map(g=>g.body)].map(b=>b.id)).size!==40)throw Error('Face additions collide with retained cells');
 const midpointGrowth=[],letters={proton:'P',neutron:'N',electron:'E'};
 // Explicit unordered neighbour-pair rule, not a contiguous NPNE substring test.
 const midpointRoles={'electron|proton':'neutron','neutron|neutron':'electron','neutron|proton':'electron','electron|neutron':'proton'};
 for(let i=0;i<corners.length;i++)for(let j=i+1;j<corners.length;j++){
  const source=corners[i],target=corners[j],delta=target.point.map((x,k)=>(x-source.point[k])/7);
  const child=byShape.get(key(source.geometry.vertices.map(v=>v.map((x,k)=>x+3*delta[k]))));
  const reverse=byShape.get(key(target.geometry.vertices.map(v=>v.map((x,k)=>x-3*delta[k]))));
  if(!child||child.kind!=='tetrahedron'||reverse?.id!==child.id)throw Error('Edge fronts must select the same midpoint tetrahedron');
  const parents=[edgeGrowth.find(g=>g.source===source.vertex&&g.target===target.vertex),edgeGrowth.find(g=>g.source===target.vertex&&g.target===source.vertex)];
  const role=midpointRoles[parents.map(g=>g.body.role).sort().join('|')];
  if(!role)throw Error('No midpoint colour rule for neighbouring cells');
  const attachments=parents.map(parent=>{
   const shared=child.vertices.filter(v=>parent.body.vertices.some(w=>key([w])===key([v])));
   if(shared.length!==1)throw Error('Midpoint must meet both retained edge fronts at vertices');
   return {parent:parent.body.id,point:shared[0]};
  });
  midpointGrowth.push({source:source.vertex,target:target.vertex,attachments,kind:'midpoint',word:[parents[0].body.role,role,parents[1].body.role].map(r=>letters[r]).join(''),body:body(child,role,3)});
 }
 if(new Set([...seeds,...growth.map(g=>g.body),...edgeGrowth.map(g=>g.body),...faceGrowth.map(g=>g.body),...midpointGrowth.map(g=>g.body)].map(b=>b.id)).size!==46)throw Error('Midpoint cells collide with retained cells');
 const faceCompletion=[];
 for(const edge of edgeGrowth){
  const source=corners.find(c=>c.vertex===edge.source),target=corners.find(c=>c.vertex===edge.target);
  for(const third of corners.filter(c=>c!==source&&c!==target)){
   const face=[source.vertex,target.vertex,third.vertex].sort();
   const delta=third.point.map((x,i)=>(x-source.point[i])/7);
   const child=byShape.get(key(edge.body.vertices.map(v=>v.map((x,i)=>x+delta[i]))));
   if(!child||child.kind!=='tetrahedron')throw Error('Face completion must use a whole native tetrahedron');
   const previousFace=faceGrowth.find(g=>g.source===source.vertex&&g.face.join(',')===face.join(','));
   const midpoint=midpointGrowth.find(g=>[g.source,g.target].includes(source.vertex)&&[g.source,g.target].includes(target.vertex));
   if(!previousFace||!midpoint)throw Error('Missing face-completion supports');
   const attachments=[edge,previousFace,midpoint].map(parent=>{
    const shared=child.vertices.filter(v=>parent.body.vertices.some(w=>key([w])===key([v])));
    if(shared.length!==1)throw Error('Face completion must meet each support at one vertex');
    return {parent:parent.body.id,point:shared[0]};
   });
   const axis=source.point.findIndex((x,i)=>target.point[i]===x&&third.point[i]===x);
   if(axis<0||!child.faces.some(f=>f.every(v=>v[axis]===source.point[axis])))throw Error('Face completion is outside its assigned face');
   const point=center(child.vertices),distance=c=>point.reduce((s,x,i)=>s+(x-c.point[i])**2,0);
   if(!(distance(target)<distance(third)))throw Error('Nearest other face corner must be unique');
   faceCompletion.push({source:source.vertex,target:target.vertex,third:third.vertex,face,attachments,kind:'face-completion',body:body(child,target.role,3)});
  }
 }
 if(faceCompletion.length!==24||new Set([...seeds,...growth.map(g=>g.body),...edgeGrowth.map(g=>g.body),...faceGrowth.map(g=>g.body),...midpointGrowth.map(g=>g.body),...faceCompletion.map(g=>g.body)].map(b=>b.id)).size!==70)throw Error('Face completion count or collision failure');
 const retained=[...seeds,...growth.map(g=>g.body),...edgeGrowth.map(g=>g.body),...faceGrowth.map(g=>g.body),...midpointGrowth.map(g=>g.body),...faceCompletion.map(g=>g.body)];
 const interiorGrowth=corners.map(source=>{
  const others=corners.filter(c=>c!==source),delta=source.point.map((x,i)=>others.reduce((s,c)=>s+(c.point[i]-x)/7,0));
  const child=byShape.get(key(source.geometry.vertices.map(v=>v.map((x,i)=>x+delta[i]))));
  if(!child||child.kind!=='tetrahedron'||retained.some(g=>g.id===child.id)||model.outer.some(f=>f.owners.includes(child.id)))throw Error('Depth-3 gap must be an unfilled interior tetrahedron');
  const attachments=retained.flatMap(parent=>{
   const shared=child.vertices.filter(v=>parent.vertices.some(w=>key([w])===key([v])));
   return shared.length?[{parent:parent.id,points:shared}]:[];
  });
  return {source:source.vertex,offset:[1,1,1],attachments,kind:'corner-interior',body:body(child,source.role,3)};
 });
 retained.push(...interiorGrowth.map(g=>g.body));
 if(new Set(retained.map(g=>g.id)).size!==74)throw Error('Interior additions collide');
 const shared=new Map(),priority={proton:2,neutron:1,electron:0};
 for(const source of corners)for(const target of corners.filter(c=>c!==source)){
  const parent=interiorGrowth.find(g=>g.source===source.vertex),delta=target.point.map((x,i)=>(x-source.point[i])/7);
  const child=byShape.get(key(parent.body.vertices.map(v=>v.map((x,i)=>x+delta[i]))));
  if(!child||child.kind!=='tetrahedron'||retained.some(g=>g.id===child.id)||model.outer.some(f=>f.owners.includes(child.id)))throw Error('Layer 4 requires unfilled interior tetrahedra');
  const point=center(child.vertices),distance=c=>point.reduce((s,x,i)=>s+(x-c.point[i])**2,0);
  if(!corners.filter(c=>c!==source&&c!==target).every(c=>distance(target)<distance(c)))throw Error('Nearest other vertex is not unique');
  if(!shared.has(child.id))shared.set(child.id,{child,proposals:[]});
  shared.get(child.id).proposals.push({source:source.vertex,target:target.vertex,role:target.role});
 }
 const sharedInterior=[...shared.values()].map(({child,proposals})=>{
  if(proposals.length!==2)throw Error('Shared interior cell must have two vertex-relative proposals');
  const role=proposals.reduce((best,p)=>priority[p.role]>priority[best]?p.role:best,proposals[0].role);
  const attachments=retained.flatMap(parent=>{const points=child.vertices.filter(v=>parent.vertices.some(w=>key([w])===key([v])));return points.length?[{parent:parent.id,points}]:[];});
  return {kind:'shared-interior',proposals,priority:['proton','neutron','electron'],attachments,body:body(child,role,4)};
 });
 retained.push(...sharedInterior.map(g=>g.body));
 if(sharedInterior.length!==6||new Set(retained.map(g=>g.id)).size!==80)throw Error('Shared interior cells must be counted once');
 const occupied=new Set(retained.map(g=>g.id)),faceCenters=[];
 for(const opposite of corners){
  const faceCorners=corners.filter(c=>c!==opposite),face=faceCorners.map(c=>c.vertex);
  const axis=faceCorners[0].point.findIndex((x,i)=>faceCorners.every(c=>c.point[i]===x)&&opposite.point[i]!==x),plane=faceCorners[0].point[axis];
  const candidates=model.geometry.filter(g=>g.kind==='tetrahedron'&&!occupied.has(g.id)&&g.faces.some(f=>f.every(v=>v[axis]===plane)));
  if(candidates.length!==1)throw Error('Each face must have exactly one remaining tetrahedral cell');
  const child=candidates[0],attachments=retained.flatMap(parent=>{
   const shared=child.vertices.filter(v=>parent.vertices.some(w=>key([w])===key([v])));
   return shared.length?[{parent:parent.id,points:shared}]:[];
  });
  faceCenters.push({face,opposite:opposite.vertex,attachments,kind:'face-center',body:body(child,opposite.role,5)});
 }
 if(new Set([...occupied,...faceCenters.map(g=>g.body.id)]).size!==84)throw Error('Face-centre additions collide');
 const complementaryGrowth=[];
 for(const source of corners){
  const seedFaces=new Set(source.geometry.faces.map(key));
  const octs=model.geometry.filter(g=>g.kind==='octahedron'&&g.faces.some(f=>seedFaces.has(key(f))));
  if(octs.length!==1)throw Error('Each corner must have one inward face-adjacent octahedron');
  const oct=octs[0],sharedFace=oct.faces.find(f=>seedFaces.has(key(f)));
  complementaryGrowth.push({source:source.vertex,kind:'complementary',complementaryLayer:1,parent:source.cell,sharedFace,body:body(oct,source.role,6)});
 }
 if(new Set([...occupied,...faceCenters.map(g=>g.body.id),...complementaryGrowth.map(g=>g.body.id)]).size!==88)throw Error('Complementary layer 1 must add four distinct new cells');
 const previous=[...retained,...faceCenters.map(g=>g.body),...complementaryGrowth.map(g=>g.body)];
 const reflection=innerLayerHexReflection(model.geometry,previous,corners);
 const reflectionEntry=({cell,...g})=>({...g,kind:'inner-hex-reflection',complementaryLayer:2,body:{...body(cell,g.role,7),reflection:g.hexWitnesses[0]}});
 const hexReflectionGrowth=reflection.agreed.map(reflectionEntry),hexReflectionConflicts=reflection.unresolved.map(reflectionEntry);
 if(new Set([...previous,...hexReflectionGrowth.map(g=>g.body)].map(g=>g.id)).size!==previous.length+hexReflectionGrowth.length)throw Error('Reflection must not overwrite an occupied cell');
 return {geometry:model.geometry,corners:corners.map(({geometry,...c})=>c),seeds,growth,edgeGrowth,faceGrowth,midpointGrowth,faceCompletion,interiorGrowth,sharedInterior,faceCenters,complementaryGrowth,hexReflectionGrowth,hexReflectionConflicts,envelope:foldedFibrationEnvelope};
}
const construction=buildCellFibration();
export function cellFibrationProcess(k,step){
 if(!Number.isInteger(k)||k<1||k>7||!Number.isInteger(step)||step<0||step>=cellFibrationStages.length)throw Error('Invalid cell fibration step');
 const layer=step;
 const growth=[...(step>=1?construction.growth:[]),...(step>=2?[...construction.edgeGrowth,...construction.faceGrowth]:[]),...(step>=3?[...construction.midpointGrowth,...construction.faceCompletion,...construction.interiorGrowth]:[]),...(step>=4?construction.sharedInterior:[]),...(step>=5?construction.faceCenters:[]),...(step>=6?construction.complementaryGrowth:[]),...(step>=7?construction.hexReflectionGrowth:[])],retainedBodies=[...construction.seeds,...growth.map(g=>g.body)];
 const zero=()=>({proton:0,neutron:0,electron:0,total:0}),counts={surface:zero(),filler:zero(),total:zero()};
 const planes=[0,1,2,3].map(axis=>foldedFibrationEnvelope.map(p=>p[axis]).find(value=>foldedFibrationEnvelope.filter(p=>p[axis]===value).length===3));
 for(const b of retainedBodies){
  const surface=b.faces.some(f=>planes.some((value,axis)=>f.every(p=>p[axis]===value))),row=counts[surface?'surface':'filler'];
  row[b.role]++;row.total++;counts.total[b.role]++;counts.total.total++;
 }
 const placed=new Set([...retainedBodies,...(step>=7?construction.hexReflectionConflicts.map(g=>g.body):[])].map(g=>g.id));
 const emptyBodies=construction.geometry.filter(g=>!placed.has(g.id)).map(g=>({...g,role:null,layer:null,unfilled:true}));
 return {k:7,step,end:seed,assignments:[],retainedBodies,emptyBodies,
  conflictBodies:step>=7?construction.hexReflectionConflicts.map(g=>({...g.body,color:0xbcbcbc,conflicts:g.hexWitnesses})):[],
  presentationLabels:retainedBodies.map(b=>({cell:b.id,role:b.role,point:center(b.vertices)})),
  presentationAudit:{nativeGeometry:true,nativeParticleRealization:false,wholeCellColour:true},
  cellFibrationAudit:{layer,unresolvedOctahedra:step>=7?construction.hexReflectionConflicts.map(({body,...g})=>({...g,cell:body.id})):[],complementaryLayer:Math.max(0,step-5),corners:construction.corners,growth: growth.map(({body,...g})=>({...g,child:body.id,role:body.role,layer:body.layer})),counts,bodyCount:retainedBodies.length,vertexAttachment:true,faceSubdivision:false,envelope:construction.envelope},
  interfaceGuides:[],firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],
  summary:`${step===0?'Layer 0 — ':''}${cellFibrationStages[step]} ${retainedBodies.length} whole cells.`,
  history:cellFibrationStages.slice(0,step+1).map((rule,index)=>({layer:index,rule})),canAdvance:step<cellFibrationStages.length-1};
}
