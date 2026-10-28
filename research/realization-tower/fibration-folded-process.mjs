// Whole octahedra remove the subdivision obstruction to the V5 -> V2 fold.
import definition from '../strominger/fibration-steps-v1.json' with {type:'json'};
import {cells,seed} from './normal-ray-model.mjs';
import {fibrationClonePoint,fibrationDisplayEnvelope} from './fibration12-process.mjs';
import {executeCornerStep,reflectAcrossFibrationSeam} from './fibration-step-machine.mjs';
import {oppositeComparisonRole,pairedPolarityProbe} from '../strominger/paired-polarity-model.mjs';
import {evaluateNativeFillerComparison} from '../strominger/four-by-four-filler-comparison.mjs';
import {buildCollectivePairCell} from './collective-pair-cell.mjs';
import {buildNeutralExtension,zeroNeutralValues,validateNeutralValues,inspectNeutralValues} from './neutral-state-extension.mjs';
export const foldedFibrationEnvelope=fibrationDisplayEnvelope.slice(0,4);
const key=vs=>vs.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
const faceSet=faces=>faces.map(key).sort().join('::');
const center=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i]/vs.length,0));
const unique=vs=>[...new Map(vs.map(v=>[key([v]),v])).values()];
const distance=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);
function boundary(components){
 const faces=new Map();for(const c of components)for(let i=0;i<4;i++){
  const f=c.filter((_,j)=>i!==j),k=key(f);if(!faces.has(k))faces.set(k,{face:f,count:0});faces.get(k).count++;
 }
 if([...faces.values()].some(f=>f.count>2))throw Error('Nonmanifold coarse cell');
 return [...faces.values()].filter(f=>f.count===1).map(f=>f.face);
}
export function buildFoldedFibration(){
 const groups=new Map();
 for(const cell of cells){
  let longest=-1,edge;for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){const d=distance(cell.vertices[i],cell.vertices[j]);if(d>longest){longest=d;edge=[cell.vertices[i],cell.vertices[j]];}}
  const id=longest===2?`tet-${cell.id}`:`oct-${key([center(edge)])}`;
  if(!groups.has(id))groups.set(id,[]);groups.get(id).push(cell);
 }
 const geometry=[...groups].map(([id,parts])=>{
  const vertices=unique(parts.flatMap(p=>p.vertices)),faces=boundary(parts.map(p=>p.vertices)),oct=parts.length>1;
  if(oct&&(parts.length!==4||vertices.length!==6||faces.length!==8))throw Error('Incomplete whole octahedron');
  const upper=vertices[0].map((_,i)=>Math.max(...vertices.map(v=>v[i])));
  const role=oct?'neutron':upper.reduce((a,b)=>a+b,0)===2?'proton':'electron';
  return {id,kind:oct?'octahedron':'tetrahedron',vertices,faces,primitiveIds:parts.map(p=>p.id),role,components:[]};
 });
 const byShape=new Map(geometry.map(g=>[key(g.vertices),g])),bindings=executeCornerStep(definition.steps[0]),occurrences=[];
 for(const copy of ['original','clone'])for(const source of geometry){
  const transform=copy==='clone'?fibrationClonePoint:p=>p,vertices=source.vertices.map(transform),faces=source.faces.map(f=>f.map(transform));
  const fold=copy==='clone'?reflectAcrossFibrationSeam:p=>p,target=byShape.get(key(vertices.map(fold)));
  if(!target||faceSet(faces.map(f=>f.map(fold)))!==faceSet(target.faces))throw Error('Whole-cell fold failed');
  const cornerBindings=bindings.filter(b=>b.copies.includes(copy)&&vertices.some(v=>key([v])===key([b.point])));
  const roles=new Set(cornerBindings.map(b=>b.role));if(roles.size>1)throw Error('Conflicting corner roles');
  const role=cornerBindings[0]?.role??source.role;
  occurrences.push({id:`${copy}:${source.id}`,copy,sourceGeometry:source.id,geometryId:target.id,vertices,faces,role,boundary:cornerBindings.map(b=>b.text)});
 }
 for(const g of geometry){
  const preimages=occurrences.filter(o=>o.geometryId===g.id);
  if(preimages.length!==2||new Set(preimages.map(o=>o.role)).size!==1)throw Error('Folded preimages disagree');
  g.role=preimages[0].role;g.polarityRoles={positive:g.role,negative:oppositeComparisonRole(g.role)};g.occurrences=preimages.map(o=>o.id);
 }
 const byId=new Map(occurrences.map(o=>[o.id,o])),faces=new Map(),neighbors=new Map(occurrences.map(o=>[o.id,[]]));
 for(const o of occurrences)for(const face of o.faces){const k=key(face);if(!faces.has(k))faces.set(k,{face,owners:[]});faces.get(k).owners.push(o.id);}
 for(const f of faces.values()){
  if(f.owners.length>2)throw Error('Nonmanifold unfolded incidence');
  if(f.owners.length===2){const [a,b]=f.owners;
   for(const [from,to]of [[a,b],[b,a]])neighbors.get(from).push({to,face:f.face});
   if(byId.get(a).copy===byId.get(b).copy&&[a,b].every(id=>byId.get(id).role!=='neutron'))throw Error('Unmediated charged contact');
  }
 }
 const entry=occurrences.filter(o=>o.boundary.includes('−P')),exit=occurrences.filter(o=>o.boundary.includes('+P'));
 if(entry.length!==1||exit.length!==1)throw Error('Unique flow endpoints required');
 function traverse(start,end){
  const depths=new Map([[start,0]]),rounds=[[start]],admissions=[];
  for(let round=1;;round++){
   const next=occurrences.filter(o=>!depths.has(o.id)&&neighbors.get(o.id).some(n=>depths.has(n.to)&&depths.get(n.to)<round));
   if(!next.length)break;
   for(const o of next)admissions.push({body:o.id,round,witnesses:neighbors.get(o.id).filter(n=>depths.has(n.to)&&depths.get(n.to)<round).map(n=>({parent:n.to,face:n.face.map(v=>[...v])}))});
   next.forEach(o=>depths.set(o.id,round));rounds.push(next.map(o=>o.id));
  }
  if(depths.size!==occurrences.length||rounds.at(-1).length!==1||rounds.at(-1)[0]!==end)throw Error('Traversal failed endpoint or coverage');
  return {rounds,admissions};
 }
 const outward=traverse(entry[0].id,exit[0].id),back=traverse(exit[0].id,entry[0].id);
 const foldedFaces=new Map();for(const g of geometry)for(const f of g.faces){const k=key(f);if(!foldedFaces.has(k))foldedFaces.set(k,{vertices:f,owners:[]});foldedFaces.get(k).owners.push(g.id);}
 if([...foldedFaces.values()].some(f=>f.owners.length>2))throw Error('Folded incidence is not conforming');
 const outer=[...foldedFaces.values()].filter(f=>f.owners.length===1);
 return {geometry,occurrences,bindings,entry:entry[0].id,exit:exit[0].id,outward,back,outer,
  audit:{tetrahedra:geometry.filter(g=>g.kind==='tetrahedron').length,octahedra:geometry.filter(g=>g.kind==='octahedron').length,geometricCells:geometry.length,flowOccurrences:occurrences.length,matchedFoldPairs:geometry.length,outerTriangles:outer.length,primitiveReferences:2*cells.length,internalOctahedralFacesRemoved:groups.size<cells.length,removedInternalTrianglesPerHalf:(4*cells.length-geometry.reduce((s,g)=>s+g.faces.length,0))/2,removedDiagonalsPerHalf:geometry.filter(g=>g.kind==='octahedron').length,physicalHalfFaceSplits:0}};
}
export function confirmFoldedRound(model,direction,round){
 const traversal=direction==='outward'?model.outward:direction==='return'?model.back:null;
 if(!traversal||!Number.isInteger(round)||round<1||round>=traversal.rounds.length)throw Error('Invalid flow round');
 const byId=new Map(model.occurrences.map(o=>[o.id,o])),depth=new Map(traversal.rounds.flatMap((ids,i)=>ids.map(id=>[id,i])));
 const records=traversal.admissions.filter(a=>a.round===round);
 if(records.length!==traversal.rounds[round].length)throw Error('Incomplete round');
 for(const record of records){
  const child=byId.get(record.body);if(!child||depth.get(child.id)!==round||!record.witnesses.length)throw Error('Invalid child occurrence');
  for(const w of record.witnesses){const parent=byId.get(w.parent);
   if(!parent||depth.get(parent.id)>=round||![parent,child].every(o=>o.faces.some(f=>key(f)===key(w.face))))throw Error('Unconfirmed retained whole face');
  }
 }
 return {direction,round,status:'positively-confirmed',bodies:records.map(r=>r.body),faceWitnessCount:records.reduce((s,r)=>s+r.witnesses.length,0)};
}
const model=buildFoldedFibration(),outCount=model.outward.rounds.length-1,backCount=model.back.rounds.length-1;
const fillerComparison=evaluateNativeFillerComparison(),collectivePairCell=buildCollectivePairCell(model),neutralExtension=buildNeutralExtension(model.geometry);
const probe=pairedPolarityProbe(),byId=new Map(model.occurrences.map(o=>[o.id,o]));
const returnCertificates=model.back.rounds.slice(1).map((_,i)=>confirmFoldedRound(model,'return',i+1));
export const foldedFibrationStages=Object.freeze([
 ...model.outward.rounds.map((ids,i)=>i===0?'Start at the −P occurrence; V5 is folded onto V2.':`−P → +P: coarse-face round ${i}, ${ids.length} flow occurrences.`),
 ...model.back.rounds.slice(1).map((ids,i)=>`+P → −P: return ${i+1}, confirm ${ids.length} retained occurrences.`),
 'Apply the candidate 4×4 boundary operator to all five native coefficients. Extract the collective P/E readings and fourteen residual directions.',
 'Confirm exact reconstruction and zero boundary charge of the residual. No additional particle counts are assigned.',
 'Materialize the collective P*/E* comparison cell at the existing minority boundary port. Keep every internal member and contrast; do not add overlapping geometry.',
 'Enable the declared neutral-state extension: 56 + 56 independent site channels and 14 residual channels. These are added state freedoms, not established physical neutrons.'
]);
export function foldedFibrationProcess(k,step,{neutralValues,selectedNeutralMode=0}={}){
 if(!Number.isInteger(k)||k<1||k>7||!Number.isInteger(step)||step<0||step>=foldedFibrationStages.length)throw Error('Invalid folded fibration step');
 const fillerStep=Math.min(2,Math.max(0,step-outCount-backCount)),collectiveActive=step>=outCount+backCount+3;
 const neutralActive=step===foldedFibrationStages.length-1;
 if(!Number.isInteger(selectedNeutralMode)||selectedNeutralMode<0||selectedNeutralMode>=neutralExtension.modes.length)throw Error('Invalid neutral mode selection');
 const neutral=neutralActive?{...neutralExtension,values:validateNeutralValues(neutralValues??zeroNeutralValues()),selectedMode:selectedNeutralMode}:null;
 if(neutral)Object.assign(neutral,inspectNeutralValues(neutralExtension,neutral.values));
 const returning=step>outCount,round=returning?Math.min(step-outCount,backCount):step;
 const admitted=new Set(model.outward.rounds.slice(0,Math.min(step,outCount)+1).flat()),visible=model.geometry.filter(g=>g.occurrences.some(id=>admitted.has(id)));
 const visibleIds=new Set(visible.map(g=>g.id)),active=(returning?model.back:model.outward).admissions.filter(a=>a.round===round);
 const fold=(p,o)=>o.copy==='clone'?reflectAcrossFibrationSeam(p):p;
 const guides=(fillerStep?[]:active).flatMap(a=>a.witnesses.flatMap((w,i)=>{
  const parent=byId.get(w.parent),child=byId.get(a.body),from=fold(center(parent.vertices),parent),middle=fold(center(w.face),parent),to=fold(center(child.vertices),child);
  return [[from,middle],[middle,to]].flatMap((points,j)=>distance(...points)<1e-12?[]:[{id:`${a.body}-${i}-${j}`,points,color:0x70d5ff},{id:`${a.body}-${i}-${j}-dual`,points:[...points].reverse(),color:0xff91c8}]);
 }));
 const labels=visible.filter(g=>!collectiveActive||g.id!==collectivePairCell.port).flatMap(g=>{
  const reached=g.occurrences.filter(id=>admitted.has(id)).map(id=>byId.get(id));const text=[...new Set(reached.flatMap(o=>o.boundary))].join('/');
  return text?[{cell:g.id,point:center(g.vertices),text,role:g.role}]:[];
 });
 if(collectiveActive)labels.push({cell:collectivePairCell.id,point:collectivePairCell.point,text:'E*',role:'electron',polarityRoles:collectivePairCell.polarityRoles,polarityText:{positive:'E*',negative:'P*'}});
 if(neutral){
  const selected=neutral.modes[selectedNeutralMode];
  if(selected.kind==='residual-channel'){const i=labels.findIndex(l=>l.cell===collectivePairCell.id);if(i>=0)labels.splice(i,1);}
  labels.push({cell:selected.id,point:selected.point??collectivePairCell.point,role:'neutron',text:selected.kind==='residual-channel'?'N*':selected.sheet==='positive'?'N+':'N−'});
 }
 const exposed=new Set(model.outer.flatMap(f=>f.owners)),sheets=Object.fromEntries(['positive','negative'].map(sheet=>[sheet,{exposedElectrons:model.geometry.filter(g=>exposed.has(g.id)&&g.polarityRoles[sheet]==='electron').length}]));
 return {k:7,step,end:seed,assignments:[],retainedBodies:visible,collectiveCells:collectiveActive?[collectivePairCell]:[],presentationLabels:labels,
  presentationPoints:collectiveActive?[{point:collectivePairCell.point,role:'electron',polarityRoles:collectivePairCell.polarityRoles}]:[],presentationAudit:{nativeGeometry:true,nativeRealization:false},
  fibrationAudit:{generated:true,folded:true,flow:returning?'+P → −P':'−P → +P',phase:neutralActive?'neutral-extension':collectiveActive?'collective-cell':fillerStep?'filler-comparison':returning?'reverse-confirmation':'growth',neutral,collective:collectiveActive?collectivePairCell:null,filler:{step:fillerStep,state:fillerStep===0?'pending':fillerStep===1?'applied':'confirmed',...fillerComparison},entry:model.entry,exit:model.exit,growthRounds:outCount,returnRounds:backCount,totalSteps:foldedFibrationStages.length,
   arrivedAtPlusP:step>=outCount,returnedToMinusP:step>=outCount+backCount,complete:step>=outCount,geometryComplete:visible.length===model.geometry.length,bodyCount:visible.length,totalBodies:model.geometry.length,admittedOccurrences:admitted.size,totalOccurrences:model.occurrences.length,
   coarse:model.audit,polarity:{sheets,bank:probe,physicalGeometryDuplicated:false,display:'whole face; sheet selected for display, both retained',nativeParticleRealization:false},
   confirmations:returning?returnCertificates.slice(0,round):[],mixedCells:[],surfaceAssignments:model.outer.filter(f=>visibleIds.has(f.owners[0])),vertexBindings:model.bindings,
   scope:'Coarse geometric quotient: distinct copy, flow and polarity records share geometry. Not a proof of native particle dynamics or of the channel count.'},
  firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],interfaceGuides:guides,
  summary:`State ${step}/${foldedFibrationStages.length-1} — ${foldedFibrationStages[step]} ${visible.length}/${model.geometry.length} whole geometric cells; ${admitted.size}/${model.occurrences.length} retained flow occurrences.`,
  history:foldedFibrationStages.slice(0,step+1).map((rule,i)=>({step:i,rule})),canAdvance:step<foldedFibrationStages.length-1};
}
