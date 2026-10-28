// Straight edge-aligned ray. Select the corner cell at the growing tetrahedron's ray endpoint.
import {cells,seed,apex,slice} from './normal-ray-model.mjs';
import {neutronMediation} from './neutron-mediated-connection.mjs';
const key=p=>p.join(','),mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0));
const edgeEnd=seed.vertices.find(p=>p[1]===2&&p[2]===1&&p[3]===2);
export const edgeDirection=edgeEnd.map((x,i)=>x-apex[i]);
export const edgeRayPoint=k=>apex.map((x,i)=>x+k*edgeDirection[i]);
function selectedCell(k){
 if(k===1)return seed;
 const endpoint=edgeRayPoint(k),level=-5+k;
 // Contain the new corner and lie inside the growing tetrahedron, not beyond
 // its support plane or in the middle of its face.
 const candidates=cells.filter(c=>c.vertices.some(p=>key(p)===key(endpoint))&&c.vertices.every(p=>p[0]<=level));
 if(candidates.length!==1)throw Error('Growing tetrahedron corner cell is not unique');
 return candidates[0];
}
export function edgeProbe(k){
 if(!Number.isInteger(k)||k<1||k>7)throw Error('k must be 1..7');
 const point=edgeRayPoint(k);
 const end=selectedCell(k);
 const shared=seed.vertices.filter(p=>end.vertices.some(q=>key(p)===key(q)));

 return {k,point,end,polygons:slice(k).polygons,traversed:rayContacts(apex,point,-5+k).map(contact=>contact.cell),atStop:[end.id],linePoints:[[...apex],point],crossings:shared.length===2?[shared]:[],surfaceFace:'opposite V2',plane:{coordinate:0,value:-5+k}};
}
// Clip a segment against each closed tetrahedron. Include vertex-only contacts:
// these are also unassigned cells connected to the ray, not endpoint roles.
function rayContacts(start,end,level){
 const sub=(a,b)=>a.slice(0,3).map((x,i)=>x-b[i]);
 const det=(a,b,c)=>a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);
 const eps=1e-9,contacts=[];
 for(const cell of cells){
  if(cell.vertices.some(p=>p[0]>level))continue;
  const v=cell.vertices,basis=v.slice(1).map(p=>sub(p,v[0])),den=det(...basis);
  const bary=p=>{const r=sub(p,v[0]),b=[det(r,basis[1],basis[2])/den,det(basis[0],r,basis[2])/den,det(basis[0],basis[1],r)/den];return [1-b.reduce((s,x)=>s+x,0),...b];};
  const a=bary(start),b=bary(end);let lo=0,hi=1,valid=true;
  for(let i=0;i<4;i++){const delta=b[i]-a[i];if(Math.abs(delta)<eps){if(a[i]<-eps)valid=false;}else if(delta>0)lo=Math.max(lo,-a[i]/delta);else hi=Math.min(hi,-a[i]/delta);}
  if(valid&&lo<=hi+eps&&lo<=1+eps&&hi>=-eps)contacts.push({cell:cell.id,interval:[Math.max(0,lo),Math.min(1,hi)]});
 }
 return contacts;
}
export function secondEdgeRay(k,branch=1){
 if(![1,3].includes(branch))throw Error('Second edge must lead toward V2 or V4');
 const start=edgeProbe(k).point,direction=[0,0,1,0];direction[branch]=-1;
 const end=start.map((x,i)=>x+k*direction[i]);
 const candidates=cells.filter(c=>c.vertices.some(p=>key(p)===key(end))&&c.vertices.every(p=>p[0]<=-5+k));
 if(candidates.length!==1)throw Error('Second ray corner cell is not unique');
 return {start,end,direction,length:k,branch,cell:candidates[0].id,contacts:rayContacts(start,end,-5+k)};
}
export function thirdEdgeRay(k,branch=1){
 const previous=secondEdgeRay(k,branch),start=previous.end,other=branch===1?3:1;
 const direction=[0,0,0,0];direction[branch]=1;direction[other]=-1;
 const end=start.map((x,i)=>x+k*direction[i]);
 const candidates=cells.filter(c=>c.vertices.some(p=>key(p)===key(end))&&c.vertices.every(p=>p[0]<=-5+k));
 if(candidates.length!==1)throw Error('Third ray corner cell is not unique');
 return {start,end,direction,length:k,branch,cell:candidates[0].id,contacts:rayContacts(start,end,-5+k)};
}
export function cornerRay(k,start,end){
 const candidates=cells.filter(c=>c.vertices.some(p=>key(p)===key(end))&&c.vertices.every(p=>p[0]<=-5+k));
 if(candidates.length!==1)throw Error('Ray endpoint corner cell is not unique');
 return {start:[...start],end:[...end],direction:end.map((x,i)=>(x-start[i])/k),length:k,cell:candidates[0].id,contacts:rayContacts(start,end,-5+k)};
}
export function exteriorFaceNeighbors(k){
 const probe=edgeProbe(k);if(k===1)return [];
 const level=-5+k,result=[];
 for(const [role,corner] of [['electron',seed],['proton',probe.end]]){
  const candidates=[];
  for(const cell of cells){
   if(cell.id===corner.id||cell.vertices.some(p=>p[0]>level))continue;
   const sharedFace=cell.vertices.filter(p=>corner.vertices.some(q=>key(p)===key(q)));
   if(sharedFace.length!==3)continue;
   const exteriorFaces=[0,1,2,3].map(coordinate=>({coordinate,value:coordinate===0?level:2,vertices:cell.vertices.filter(p=>p[coordinate]===(coordinate===0?level:2))})).filter(f=>f.vertices.length===3);
   if(exteriorFaces.length)candidates.push({role,corner:corner.id,cell:cell.id,sharedFace,exteriorFaces});
  }
  if(candidates.length!==1)throw Error(`Expected one exterior-facing neighbor of ${role} at k=${k}`);
  result.push(candidates[0]);
 }
 return result;
}
export function oppositePartners(assignments){
 const roles=new Map();
 for(const a of assignments){
  if(roles.has(a.cell)&&roles.get(a.cell)!==a.role)throw Error(`Conflicting roles on cell ${a.cell}`);
  roles.set(a.cell,a.role);
 }
 const charged=[...roles].filter(([,role])=>role==='electron'||role==='proton');
 return charged.map(([cell,role])=>{
  const opposite=role==='electron'?'proton':'electron';
  const neighbors=charged.filter(([other,r])=>r===opposite&&cells[cell].vertices.filter(p=>cells[other].vertices.some(q=>key(p)===key(q))).length===3);
  if(neighbors.length!==1)throw Error(`Cell ${cell} must have exactly one opposite face-neighbor; found ${neighbors.length}`);
  return {cell,partner:neighbors[0][0]};
 });
}
export function interiorNeutronRound(k,assignments){
 if(!Number.isInteger(k)||k<1||k>7)throw Error('k must be 1..7');
 const assigned=new Set(assignments.map(a=>a.cell)),level=-5+k,eligible=[];
 for(const cell of cells){
  if(assigned.has(cell.id)||cell.vertices.some(p=>p[0]>level))continue;
  if([0,1,2,3].some(i=>cell.vertices.filter(p=>p[i]===(i===0?level:2)).length===3))continue;
  const supports=[];
  for(const id of assigned){
   const face=cell.vertices.filter(p=>cells[id].vertices.some(q=>key(p)===key(q)));
   if(face.length===3)supports.push({cell:id,face});
  }
  if(supports.length>=2)eligible.push({cell:cell.id,supports});
 }
 return eligible;
}
export function localFaceVertexComparisons(k,assignments,neighbors=exteriorFaceNeighbors(k)){
 const comparisons=[];
 for(const paired of neighbors)for(const face of paired.exteriorFaces){
  const owner=assignments.find(a=>a.cell===paired.cell);
  if(!owner)continue;
  // The exposed central triangle consists of the midpoints of a side-two face.
  const center=mean(face.vertices),caps=center.map((x,i)=>i===face.coordinate?face.value:Math.round(x+2/3));
  const corners=caps.map((_,i)=>caps.map((x,j)=>x-(i===j?2:0))),oppositeVertex=corners[face.coordinate];
  const targets=cells.filter(c=>c.vertices.some(p=>key(p)===key(oppositeVertex))&&c.vertices.every(p=>p.every((x,i)=>x<=caps[i]+1e-9)));
  if(targets.length!==1)throw Error('Local opposite-vertex cell is not unique');
  const target=targets[0],role=owner.role==='proton'?'electron':'proton',existing=assignments.find(a=>a.cell===target.id);
  const oppositeRole=role==='proton'?'electron':'proton';
  const facePartners=assignments.filter(a=>a.role===oppositeRole&&target.vertices.filter(p=>cells[a.cell].vertices.some(q=>key(p)===key(q))).length===3).map(a=>a.cell);
  comparisons.push({owner:paired.cell,ownerRole:owner.role,face:face.vertices,corners,oppositeVertex,cell:target.id,role,existingRole:existing?.role??null,facePartners,status:existing?(existing.role===role?'already-assigned':'conflict'):'candidate'});
 }
 for(const c of comparisons)if(comparisons.some(d=>d.cell===c.cell&&d.role!==c.role))c.status='conflict';
 return comparisons;
}
// Branch sideways from each original EP/PE pair with the opposite role. This is an
// explicit construction step, not a consequence of the interior N rule.
export function surfacePairContinuations(k,assignments,neighbors=exteriorFaceNeighbors(k)){
 const result=[];
 for(const paired of neighbors)for(const exterior of paired.exteriorFaces){
  const owner=assignments.find(a=>a.cell===paired.cell);if(!owner)continue;
  const cornerFace=cells[paired.corner].vertices.filter(p=>p[exterior.coordinate]===exterior.value);
  const sharedVertex=exterior.vertices.find(p=>!cornerFace.some(q=>key(p)===key(q)));
  if(!sharedVertex)continue;
  // Translation-equivalent triangles at the forward vertex are the two
  // lateral branches; the straight-ahead triangle has the other orientation.
  const orientation=face=>face.map(p=>key(p.map((x,i)=>3*x-face.reduce((s,q)=>s+q[i],0)))).sort().join(';');
  const pattern=orientation(exterior.vertices);
  const candidates=cells.filter(c=>!assignments.some(a=>a.cell===c.id)&&c.vertices.every(p=>p[0]<=-5+k)).map(c=>({cell:c.id,face:c.vertices.filter(p=>p[exterior.coordinate]===exterior.value)})).filter(c=>c.face.length===3&&c.face.some(p=>key(p)===key(sharedVertex))&&orientation(c.face)===pattern);
  if(candidates.length!==2)continue;
  for(const candidate of candidates)result.push({...candidate,role:owner.role==='proton'?'electron':'proton',source:owner.cell,coordinate:exterior.coordinate,value:exterior.value,sharedVertex});
 }
 return result;
}
export function edgeProcedure(k,step,branch=1){
 if(!Number.isInteger(step)||step<0||step>9+cells.length)throw Error('Invalid construction step');
 const probe=edgeProbe(k),end={...probe.end,outsideEnvelope:false};
 // Visit corners in order E → P → N1 → N2 → P → E.
 const secondRay=step>=3?secondEdgeRay(k,branch):null;
 const thirdRay=step>=4?thirdEdgeRay(k,branch):null;
 const returnRay=step>=5?cornerRay(k,thirdRay.end,probe.point):null;
 const closingRay=step>=6?cornerRay(k,probe.point,apex):null;
 const rays=[secondRay,thirdRay,returnRay,closingRay].filter(Boolean);
 const assignments=step<2||k<2?[]:[
  {id:'electron',kind:'cell-role',cell:seed.id,role:'electron',boundary:'entry',point:mean(seed.vertices)},
  {id:'proton',kind:'cell-role',cell:end.id,role:'proton',boundary:'corner',point:mean(end.vertices)},
 ];
 for(const [id,ray,role] of [['first-neutron',secondRay,'neutron'],['second-neutron',thirdRay,'neutron']])if(ray){
  assignments.push({id,kind:'cell-role',cell:ray.cell,role,boundary:'corner',point:mean(cells[ray.cell].vertices)});
 }
 const faceNeighbors=step>=7?exteriorFaceNeighbors(k):[];
 for(const neighbor of faceNeighbors){
  assignments.push({id:`partner-of-${neighbor.corner}`,kind:'cell-role',cell:neighbor.cell,role:neighbor.role==='electron'?'proton':'electron',boundary:'face-neighbor',point:mean(cells[neighbor.cell].vertices)});
 }
 const neutronNeighbors=[];
 if(step>=8)for(const paired of faceNeighbors){
  const adjacent=cells.filter(c=>c.id!==paired.cell&&c.id!==paired.corner&&c.vertices.every(p=>p[0]<=-5+k)).map(c=>({cell:c.id,sharedFace:c.vertices.filter(p=>cells[paired.cell].vertices.some(q=>key(p)===key(q)))})).filter(c=>c.sharedFace.length===3);
  if(adjacent.length!==2)throw Error(`Paired cell ${paired.cell} must have two remaining interior face-neighbors`);
  for(const neighbor of adjacent){
   neutronNeighbors.push({owner:paired.cell,...neighbor});
   const existing=assignments.find(a=>a.cell===neighbor.cell);
   if(existing&&existing.role!=='neutron')throw Error(`Neutron rule conflicts with ${existing.role} on cell ${neighbor.cell}`);
   if(!existing)assignments.push({id:`neutron-${neighbor.cell}`,kind:'cell-role',cell:neighbor.cell,role:'neutron',boundary:'face-neighbor',point:mean(cells[neighbor.cell].vertices)});
  }
 }
 const surfaceNeutronNeighbors=[];
 if(step>=9)for(const paired of faceNeighbors)for(const exterior of paired.exteriorFaces){
  const adjacent=cells.filter(c=>c.id!==paired.cell&&c.id!==paired.corner&&c.vertices.every(p=>p[0]<=-5+k)).map(c=>{
   const surfaceFace=c.vertices.filter(p=>p[exterior.coordinate]===exterior.value);
   const sharedEdge=surfaceFace.filter(p=>exterior.vertices.some(q=>key(p)===key(q)));
   return {cell:c.id,surfaceFace,sharedEdge};
  }).filter(c=>c.surfaceFace.length===3&&c.sharedEdge.length===2);
  if(adjacent.length!==2)throw Error(`Paired cell ${paired.cell} must have two remaining exterior-surface neighbors`);
  for(const neighbor of adjacent){
   surfaceNeutronNeighbors.push({owner:paired.cell,coordinate:exterior.coordinate,value:exterior.value,...neighbor});
   const existing=assignments.find(a=>a.cell===neighbor.cell);
   if(existing&&existing.role!=='neutron')throw Error(`Surface neutron rule conflicts with ${existing.role} on cell ${neighbor.cell}`);
   if(!existing)assignments.push({id:`neutron-${neighbor.cell}`,kind:'cell-role',cell:neighbor.cell,role:'neutron',boundary:'surface-neighbor',point:mean(cells[neighbor.cell].vertices)});
  }
 }
 const closureRounds=[];
 for(let round=0;round<step-9;round++){
  // Snapshot first; additions in this round cannot enable each other.
  const additions=interiorNeutronRound(k,assignments);
  if(!additions.length&&round>0)break;
  closureRounds.push(additions);
  for(const candidate of additions)assignments.push({id:`neutron-${candidate.cell}`,kind:'cell-role',cell:candidate.cell,role:'neutron',boundary:'interior-closure',round:round+1,point:mean(cells[candidate.cell].vertices)});
  if(!additions.length)break;
 }
 let nextClosure=step>=9?interiorNeutronRound(k,assignments):[];
 const comparisonVisible=step>=10&&!nextClosure.length&&step>9+closureRounds.length;
 const faceVertexComparisons=comparisonVisible?localFaceVertexComparisons(k,assignments,faceNeighbors):[];
 // Face-pair checks apply to the face-pair construction above. The next
 // operation uses the distinct local face–opposite-vertex correspondence.
 const partners=step>=7?oppositePartners(assignments):[];
 for(const comparison of faceVertexComparisons)if(comparison.status==='candidate'){
  assignments.push({id:`face-vertex-${comparison.cell}`,kind:'cell-role',cell:comparison.cell,role:comparison.role,boundary:'face-vertex',source:comparison.owner,point:mean(cells[comparison.cell].vertices)});
  comparison.status='assigned';
 }
 const chargedCorners=assignments.filter(a=>a.boundary==='face-vertex');
 const mediationAvailable=chargedCorners.some(a=>a.role==='electron')&&chargedCorners.some(a=>a.role==='proton');
 const mediationVisible=comparisonVisible&&step>10+closureRounds.length;
 let mediation=null;
 if(mediationVisible&&mediationAvailable){
  const from=chargedCorners.find(a=>a.role==='electron'),to=chargedCorners.find(a=>a.role==='proton');
  mediation=neutronMediation(k,assignments,from.cell,to.cell);
  if(!mediation.connected)throw Error('No face-connected neutron mediation between the charged corners');
  for(const id of mediation.fillerCells){
   const existing=assignments.find(a=>a.cell===id);
   if(existing&&existing.role!=='neutron')throw Error('Signal route crosses another charged cell');
   if(!existing)assignments.push({id:`neutron-${id}`,kind:'cell-role',cell:id,role:'neutron',boundary:'neutron-mediation',point:mean(cells[id].vertices)});
  }
 }
 const postMediationRounds=[];
 if(mediation){
  for(let round=0;round<step-(11+closureRounds.length);round++){
   const additions=interiorNeutronRound(k,assignments);
   if(!additions.length)break;
   postMediationRounds.push(additions);
   for(const candidate of additions)assignments.push({id:`neutron-${candidate.cell}`,kind:'cell-role',cell:candidate.cell,role:'neutron',boundary:'post-mediation-closure',round:round+1,point:mean(cells[candidate.cell].vertices)});
  }
  nextClosure=interiorNeutronRound(k,assignments);
 }
 const surfaceContinuations=mediation&&!nextClosure.length?surfacePairContinuations(k,assignments,faceNeighbors):[];
 const surfaceContinuationAvailable=surfaceContinuations.length===4;
 const surfaceContinuationVisible=surfaceContinuationAvailable&&step>=12+closureRounds.length+postMediationRounds.length;
 if(surfaceContinuationVisible)for(const candidate of surfaceContinuations)assignments.push({id:`surface-continuation-${candidate.cell}`,kind:'cell-role',cell:candidate.cell,role:candidate.role,boundary:'surface-continuation',source:candidate.source,point:mean(cells[candidate.cell].vertices)});
 return {k,step,end,probe,faceNeighbors,neutronNeighbors,surfaceNeutronNeighbors,closureRounds,postMediationRounds,nextClosure,surfaceContinuations,surfaceContinuationAvailable,surfaceContinuationVisible,comparisonVisible,faceVertexComparisons,mediationAvailable,mediationVisible,mediation,partners,firstRay:step>=1?{start:[...apex],end:probe.point,length:k}:null,secondRay,returnRay,thirdRay,closingRay,rays,assignments};
}
