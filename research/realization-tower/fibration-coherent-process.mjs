// Geometry-first replacement for word-painted surface layers.
// Only the corner boundary condition is read from the old definition.
import definition from '../strominger/fibration-steps-v1.json' with {type:'json'};
import {oppositeComparisonRole,pairedPolarityProbe} from '../strominger/paired-polarity-model.mjs';
import {cells,seed,worldPoint} from './normal-ray-model.mjs';
import {fibrationClonePoint} from './fibration12-process.mjs';
import {executeCornerStep} from './fibration-step-machine.mjs';
const key=vs=>vs.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
const center=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i]/vs.length,0));
const near=(a,b)=>a.every((x,i)=>Math.abs(x-b[i])<1e-8);
const sq=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);
const subtract=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
function geometricRole(vertices){
 const regular=vertices.every((a,i)=>vertices.slice(i+1).every(b=>sq(a,b)===2));
 if(!regular)return 'neutron';
 const upper=vertices[0].map((_,i)=>Math.max(...vertices.map(v=>v[i])));
 return upper.reduce((a,b)=>a+b,0)===2?'proton':'electron';
}
export function buildCoherentFibration(cornerStep=definition.steps[0]){
 const bindings=executeCornerStep(cornerStep),primitives=[],faces=new Map();
 for(const copy of ['original','clone'])for(const cell of cells){
  const vertices=cell.vertices.map(copy==='clone'?fibrationClonePoint:p=>[...p]);
  const p={id:`${copy}-${cell.id}`,sourceCell:cell.id,copy,vertices,role:geometricRole(cell.vertices),geometricRole:geometricRole(cell.vertices),boundary:[]};
  for(const b of bindings)if(b.copies.includes(copy)&&vertices.some(v=>near(v,b.point)))p.boundary.push(b.text);
  const pinned=bindings.filter(b=>p.boundary.includes(b.text));
  if(new Set(pinned.map(b=>b.role)).size>1)throw Error('Conflicting corner constraints');
  if(pinned.length)p.role=pinned[0].role;
  primitives.push(p);
  for(let i=0;i<4;i++){
   const polygon=vertices.filter((_,j)=>i!==j),id=key(polygon);
   if(!faces.has(id))faces.set(id,{id,vertices:polygon,owners:[]});faces.get(id).owners.push(p.id);
  }
 }
 const byId=new Map(primitives.map(p=>[p.id,p])),parent=new Map(primitives.map(p=>[p.id,p.id]));
 function find(id){let r=id;while(parent.get(r)!==r)r=parent.get(r);return r;}
 const seamPairs=[];
 for(const face of faces.values()){
  if(face.owners.length>2)throw Error('Nonmanifold triangular face');
  if(face.owners.length!==2)continue;
  const [a,b]=face.owners.map(id=>byId.get(id)),[u,v,w]=face.vertices.map(worldPoint),n=cross(subtract(v,u),subtract(w,u));
  if(dot(n,subtract(worldPoint(center(a.vertices)),u))*dot(n,subtract(worldPoint(center(b.vertices)),u))>=-1e-12)throw Error('Adjacent tetrahedra occupy the same face side');
  if(a.copy!==b.copy){
   if(a.role!==b.role)throw Error('Paired seam does not confirm the same role');
   // Equal charged seam halves are one composite carrier, not two charged
   // particles with a forbidden charged/charged interface. Geometry is kept.
   if(a.role!=='neutron'){
    parent.set(find(b.id),find(a.id));
    seamPairs.push({members:[a.id,b.id],role:a.role,face:face.vertices,confirmation:'same-role/opposite-face-sides',nativePrimitive:false});
   }
  }else if(a.role!=='neutron'&&b.role!=='neutron')throw Error('Unmediated charged adjacency inside a copy');
 }
 const groups=new Map();for(const p of primitives){const id=find(p.id);if(!groups.has(id))groups.set(id,[]);groups.get(id).push(p);}
 const bodies=[...groups].map(([id,members])=>({id,role:members[0].role,components:members.map(p=>p.vertices),members:members.map(p=>p.id),boundary:[...new Set(members.flatMap(p=>p.boundary))],polarityRoles:{positive:members[0].role,negative:oppositeComparisonRole(members[0].role)},round:-1}));
 const bodyById=new Map(bodies.map(b=>[b.id,b])),neighbors=new Map(bodies.map(b=>[b.id,new Set()])),contactFaces=new Map();
 for(const face of faces.values())if(face.owners.length===2){const [a,b]=face.owners.map(find);if(a===b)continue;neighbors.get(a).add(b);neighbors.get(b).add(a);contactFaces.set([a,b].sort().join('|'),face.vertices);if(bodyById.get(a).role!=='neutron'&&bodyById.get(b).role!=='neutron')throw Error('Unmediated charged adjacency after seam identification');}
 const entry=bodies.filter(b=>b.boundary.includes('−P')),exit=bodies.filter(b=>b.boundary.includes('+P'));
 if(entry.length!==1||exit.length!==1)throw Error('Unique −P entry and +P exit required');
 const rounds=[[entry[0].id]];
 for(const id of rounds[0])bodyById.get(id).round=0;
 const admission=[];
 for(let depth=1;;depth++){
  const frontier=bodies.filter(b=>b.round<0&&[...neighbors.get(b.id)].some(n=>bodyById.get(n).round>=0&&bodyById.get(n).round<depth));
  if(!frontier.length)break;
  for(const b of frontier){const parents=[...neighbors.get(b.id)].filter(n=>bodyById.get(n).round>=0&&bodyById.get(n).round<depth);admission.push({body:b.id,round:depth,parents,witnesses:parents.map(parent=>({parent,face:contactFaces.get([parent,b.id].sort().join('|'))}))});}
  for(const b of frontier)b.round=depth;
  rounds.push(frontier.map(b=>b.id));
 }
 if(bodies.some(b=>b.round<0))throw Error('Unreachable tiling component');
 if(rounds.at(-1).length!==1||rounds.at(-1)[0]!==exit[0].id)throw Error('+P must be the outward terminal, not an earlier side contact');
 // Return is a single-entry wave through the retained face network. Merely
 // reversing outward BFS layers would invent return links on side branches.
 const returnRounds=[[exit[0].id]],returnDepth=new Map([[exit[0].id,0]]),returnAdmission=[];
 for(let depth=1;;depth++){
  const frontier=bodies.filter(b=>!returnDepth.has(b.id)&&[...neighbors.get(b.id)].some(n=>returnDepth.has(n)&&returnDepth.get(n)<depth));
  if(!frontier.length)break;
  for(const b of frontier){const parents=[...neighbors.get(b.id)].filter(n=>returnDepth.has(n)&&returnDepth.get(n)<depth);
   returnAdmission.push({body:b.id,round:depth,parents,witnesses:parents.map(parent=>({parent,face:contactFaces.get([parent,b.id].sort().join('|'))}))});}
  for(const b of frontier)returnDepth.set(b.id,depth);
  returnRounds.push(frontier.map(b=>b.id));
 }
 if(returnDepth.size!==bodies.length||returnRounds.at(-1).length!==1||returnRounds.at(-1)[0]!==entry[0].id)throw Error('Return must cover the retained network and end at −P');
 const boundaryFaces=[...faces.values()].filter(f=>f.owners.length===1);
 const boundaryEdges=new Map();for(const f of boundaryFaces)for(let i=0;i<3;i++){const id=key(f.vertices.filter((_,j)=>j!==i));boundaryEdges.set(id,(boundaryEdges.get(id)||0)+1);}
 if([...boundaryEdges.values()].some(n=>n!==2))throw Error('Outer surface is not a closed triangulated manifold');
 const counts=Object.fromEntries(['proton','neutron','electron'].map(role=>[role,bodies.filter(b=>b.role===role).length]));
 const exposed=new Set(boundaryFaces.flatMap(f=>f.owners.map(find)));
 const polaritySheets=Object.fromEntries(['positive','negative'].map(sheet=>[sheet,{
  counts:Object.fromEntries(['proton','neutron','electron'].map(role=>[role,bodies.filter(b=>b.polarityRoles[sheet]===role).length])),
  exposedElectrons:bodies.filter(b=>exposed.has(b.id)&&b.polarityRoles[sheet]==='electron').length,
  interiorElectrons:bodies.filter(b=>!exposed.has(b.id)&&b.polarityRoles[sheet]==='electron').length
 }]));
 return {primitives,bodies,bindings,rounds,admission,seamPairs,boundaryFaces,counts,polaritySheets,entry:entry[0].id,exit:exit[0].id,returnRounds,returnAdmission,
  audit:{primitiveCount:primitives.length,bodyCount:bodies.length,faceCount:faces.size,outerTriangles:boundaryFaces.length,seamFaceCount:[...faces.values()].filter(f=>f.owners.length===2&&byId.get(f.owners[0]).copy!==byId.get(f.owners[1]).copy).length,
   nonmanifoldFaces:0,unmediatedChargedContacts:0,unreachableBodies:0,allSharedFacesOppositeSided:true,closedOuterSurface:true,
   boundaryOverrides:primitives.filter(p=>p.role!==p.geometricRole).map(p=>({id:p.id,geometricRole:p.geometricRole,role:p.role,boundary:p.boundary})),
   nativeParticleRealization:false,scope:'Conforming geometric tiling and whole-body comparison roles. Composite seam carriers and imposed corner roles are not certified native particle packets.'}};
}
export function confirmFibrationRound(tiling,round){
 if(!Number.isInteger(round)||round<1||round>=tiling.rounds.length)throw Error('Invalid confirmation round');
 const byId=new Map(tiling.bodies.map(b=>[b.id,b]));
 const records=tiling.admission.filter(a=>a.round===round);
 if(records.length!==tiling.rounds[round].length)throw Error('Incomplete admission history');
 const hasFace=(body,face)=>body.components.some(c=>[0,1,2,3].some(i=>key(c.filter((_,j)=>i!==j))===key(face)));
 for(const record of records){
  const body=byId.get(record.body);
  if(!body||body.round!==round||!record.parents.length||record.witnesses.length!==record.parents.length)throw Error('Invalid retained admission');
  for(const witness of record.witnesses){const parent=byId.get(witness.parent);
   if(!parent||parent.round>=round||!record.parents.includes(parent.id)||!hasFace(parent,witness.face)||!hasFace(body,witness.face))throw Error('Unconfirmed face attachment');
  }
 }
 return {round,bodies:records.map(r=>r.body),faceWitnessCount:records.reduce((s,r)=>s+r.witnesses.length,0),status:'positively-confirmed',retained:true};
}
export function confirmReturnRound(tiling,round){
 if(!Number.isInteger(round)||round<1||round>=tiling.returnRounds.length)throw Error('Invalid return round');
 const proxy={...tiling,rounds:tiling.returnRounds,admission:tiling.returnAdmission,bodies:tiling.bodies.map(b=>({...b,round:tiling.returnRounds.findIndex(ids=>ids.includes(b.id))}))};
 const result=confirmFibrationRound(proxy,round);
 return {...result,origin:tiling.exit,destination:tiling.entry,direction:'+P → −P',usesRetainedFaceNetwork:true};
}
const tiling=buildCoherentFibration(),growthRounds=tiling.rounds.length-1,returnCount=tiling.returnRounds.length-1;
const returnCertificates=tiling.returnRounds.slice(1).map((_,i)=>confirmReturnRound(tiling,i+1));
const polarityProbe=pairedPolarityProbe();
export const coherentFibrationStages=Object.freeze([
 ...tiling.rounds.map((ids,i)=>i===0?'Initialize −P only. Other corner roles are boundary constraints, not sources.':`−P → +P: round ${i}, admit ${ids.length} bodies across complete shared triangles.`),
 ...tiling.returnRounds.slice(1).map((ids,i)=>`+P → −P: return ${i+1}/${returnCount}, positively confirm ${ids.length} bodies through retained faces.`)
]);
export function coherentFibrationProcess(k,step){
 if(!Number.isInteger(k)||k<1||k>7||!Number.isInteger(step)||step<0||step>=coherentFibrationStages.length)throw Error('Invalid coherent fibration step');
 const returning=step>growthRounds,round=returning?step-growthRounds:step;
 const confirmations=returning?returnCertificates.slice(0,round):[];
 const activeRecords=(returning?tiling.returnAdmission:tiling.admission).filter(a=>a.round===round);
 const byId=new Map(tiling.bodies.map(b=>[b.id,b]));
 const interfaceGuides=activeRecords.flatMap(a=>a.witnesses.flatMap((w,i)=>[
  {id:`${step}-${a.body}-${i}-in`,points:[center(byId.get(w.parent).components.flat()),center(w.face)],color:0xf4c46a},
  {id:`${step}-${a.body}-${i}-out`,points:[center(w.face),center(byId.get(a.body).components.flat())],color:0xf4c46a}
 ]));
 const frontier=(returning?tiling.returnRounds:tiling.rounds)[round];
 const visible=tiling.bodies.filter(b=>b.round<=Math.min(step,growthRounds)),visibleIds=new Set(visible.flatMap(b=>b.members));
 const labels=visible.filter(b=>b.boundary.length).map(b=>({cell:b.id,point:center(b.components.flat()),text:b.boundary.join('/'),role:b.role}));
 const surfaceAssignments=tiling.boundaryFaces.filter(f=>visibleIds.has(f.owners[0])).map(f=>{const primitive=tiling.primitives.find(p=>p.id===f.owners[0]);return {vertices:f.vertices,role:primitive.role,polarityRoles:{positive:primitive.role,negative:oppositeComparisonRole(primitive.role)},type:{proton:'P',electron:'E',neutron:'N'}[primitive.role],sourceCell:primitive.sourceCell,copy:primitive.copy};});
 return {k:7,step,end:seed,assignments:[],retainedBodies:visible,presentationLabels:labels,
  presentationAudit:{nativeGeometry:true,fixedCellSize:true,nativeRealization:false},
  fibrationAudit:{generated:true,policy:'single-entry-minus-P/retained-face-network/plus-P-return',userStep:step+1,totalSteps:coherentFibrationStages.length,growthRounds,returnRounds:returnCount,entry:tiling.entry,exit:tiling.exit,flow:returning?'+P → −P':'−P → +P',phase:returning?'reverse-confirmation':'growth',confirmations,
   polarity:{sheets:tiling.polaritySheets,bank:polarityProbe,physicalGeometryDuplicated:false,rule:'P ↔ E; N fixed; full five-slot interface map; opposite flow',display:'two half-face readings, not new physical triangles',boundaryLabels:'original sheet',nativeParticleRealization:false},
   arrivedAtPlusP:step>=growthRounds,returnedToMinusP:step===growthRounds+returnCount,
   vertexBindings:tiling.bindings,surfaceAssignments,mixedCells:[],bodyCount:visible.length,totalBodies:tiling.bodies.length,filledPrimitives:visible.reduce((s,b)=>s+b.members.length,0),counts:tiling.counts,
   frontier,seamPairs:tiling.seamPairs,coherence:tiling.audit,complete:step>=growthRounds,pathCount:0,pathOccurrences:0,paths:[]},
  firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],interfaceGuides:interfaceGuides.flatMap(g=>[{...g,color:0x70d5ff},{...g,id:g.id+'-opposite',points:[...g.points].reverse(),color:0xff91c8}]),
  summary:`State ${step}/${growthRounds+returnCount} — ${coherentFibrationStages[step]} ${visible.length}/${tiling.bodies.length} bodies; both polarity sheets retained on the same geometry.${step>=growthRounds?' Complete conforming tiling.':''}`,
  history:coherentFibrationStages.slice(0,step+1).map((rule,i)=>({step:i,rule,added:i<=growthRounds?tiling.rounds[i]:[],confirmation:i>growthRounds?confirmations[i-growthRounds-1]:null})),canAdvance:step<coherentFibrationStages.length-1};
}
