// Read-only audit of the current construction; this does not assign new roles.
import {cells,apex,worldPoint} from './normal-ray-model.mjs';
import {edgeRayPoint,edgeProcedure} from './edge-ray-model.mjs';
import {assembleComponents} from '../strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs';
const pointKey=p=>p.join(','),key=vs=>vs.map(pointKey).sort().join('|');
const index=new Map(cells.map(c=>[key(c.vertices),c.id]));
const assembly=assembleComponents();
const opposite=r=>r==='electron'?'proton':r==='proton'?'electron':r;
const faceIds=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]];
const shared=(a,b)=>a.filter(p=>b.some(q=>pointKey(p)===pointKey(q)));
const check=(ok,message)=>{if(!ok)throw Error(message);};
export function exchangeEP(k,p){
 if(!Number.isInteger(k)||k<1||k>7)throw Error('k must be 1..7');
 return [p[2]+k-7,p[3],p[0]+7-k,p[1]];
}
const midpoint=(a,b)=>a.map((x,i)=>(x+b[i])/2);
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const det=(a,b,c)=>a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);
export function auditEdgePairSymmetry(k,branch=1){
 const transform=p=>exchangeEP(k,p),level=k-5;
 const region=cells.filter(c=>c.vertices.every(p=>p[0]<=level)),ids=new Set(region.map(c=>c.id));
 const mapping=new Map(region.map(c=>[c.id,index.get(key(c.vertices.map(transform)))]));
 check([...mapping.values()].every(id=>ids.has(id)),`k=${k}: cell subdivision not preserved`);
 for(const [a,b] of mapping)check(mapping.get(b)===a,'Cell exchange is not involutive');
 for(const c of region)for(const p of c.vertices)check(pointKey(transform(transform(p)))===pointKey(p),'Point exchange is not involutive');
 const corners=[apex,edgeRayPoint(k),apex.map((x,i)=>x+k*([1,-1,0,0][i])),apex.map((x,i)=>x+k*([1,0,0,-1][i]))];
 check(key([transform(corners[0]),transform(corners[1])])===key(corners.slice(0,2)),'E/P endpoints not exchanged');
 const world=corners.map(worldPoint),moved=corners.map(transform).map(worldPoint);
 const volume=ps=>det(...ps.slice(1).map(p=>sub(p,ps[0])));
 check(Math.abs(volume(world)-volume(moved))<1e-8,'Exchange is not a proper isometry');
 for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){
  const sq=(a,b)=>sub(a,b).reduce((s,x)=>s+x*x,0);
  check(Math.abs(sq(world[i],world[j])-sq(moved[i],moved[j]))<1e-8,'Metric changed');
 }
 const axis=[midpoint(corners[0],corners[1]),midpoint(corners[2],corners[3])];
 check(axis.every(p=>pointKey(transform(p))===pointKey(p)),'Opposite-edge midpoint axis moved');
 const faceOwners=new Map();
 for(const c of region)for(const f of faceIds){const face=f.map(i=>c.vertices[i]),s=key(face);if(!faceOwners.has(s))faceOwners.set(s,{face,owners:[]});faceOwners.get(s).owners.push(c.id);}
 for(const {face,owners} of faceOwners.values()){
  const target=faceOwners.get(key(face.map(transform)));
  check(target&&key([owners.map(id=>mapping.get(id)).sort((a,b)=>a-b)])===key([target.owners.slice().sort((a,b)=>a-b)]),'Face incidence changed');
 }
 const groups=assembly.groups.filter(g=>g.children.every(id=>ids.has(id)));
 const groupIndex=new Map(groups.map(g=>[g.children.slice().sort((a,b)=>a-b).join(','),g]));
 const diagonal=g=>g.children.reduce((vs,id)=>shared(vs,cells[id].vertices),cells[g.children[0]].vertices);
 for(const g of groups){
  const target=groupIndex.get(g.children.map(id=>mapping.get(id)).sort((a,b)=>a-b).join(','));
  check(target,'Octahedral grouping changed');
  check(diagonal(g).length===2&&key(diagonal(g).map(transform))===key(diagonal(target)),'Selected octahedral diagonal changed');
 }
 let step=10,state=edgeProcedure(k,step,branch);
 while(state.nextClosure.length){check(step<9+cells.length,'Closure failed to terminate');state=edgeProcedure(k,++step,branch);}
 const completedStages=[2,4,5,6,7,8,9,...Array.from({length:step-9},(_,i)=>10+i)];
 for(const stage of completedStages){
  const s=edgeProcedure(k,stage,branch),roles=new Map(s.assignments.map(a=>[a.cell,a.role]));
  for(const [id,role] of roles)check(roles.get(mapping.get(id))===opposite(role),`Role exchange failed at k=${k}, step=${stage}, cell=${id}`);
  for(const round of s.closureRounds){
   const candidates=new Map(round.map(c=>[c.cell,c]));
   for(const candidate of round){
    const image=candidates.get(mapping.get(candidate.cell));check(image,'Closure round not equivariant');
    const expected=candidate.supports.map(v=>`${mapping.get(v.cell)}:${key(v.face.map(transform))}`).sort();
    const actual=image.supports.map(v=>`${v.cell}:${key(v.face)}`).sort();
    check(JSON.stringify(expected)===JSON.stringify(actual),'Attachment face witnesses not transported');
   }
  }
 }
 const roles=new Map(state.assignments.map(a=>[a.cell,a.role])),segments=[];
 for(let i=0;i<k;i++){
  const endpoints=[edgeRayPoint(i),edgeRayPoint(i+1)];
  const candidates=region.filter(c=>endpoints.every(p=>c.vertices.some(q=>pointKey(p)===pointKey(q))));
  check(candidates.length===1,'Edge segment has no unique carrier cell');
  const c=candidates[0],neighbors=region.filter(d=>d.id!==c.id&&shared(c.vertices,d.vertices).length===3);
  const exteriorFaces=[0,1,2,3].filter(j=>c.vertices.filter(p=>p[j]===(j===0?level:2)).length===3);
  segments.push({segment:i+1,cell:c.id,mirrorCell:mapping.get(c.id),mirrorSegment:k-i,role:roles.get(c.id)??null,exteriorFaces,faceNeighbors:neighbors.map(d=>({cell:d.id,role:roles.get(d.id)??null})),assignedFaceCount:neighbors.filter(d=>roles.has(d.id)).length});
 }
 for(const s of segments)check(segments[s.mirrorSegment-1].cell===s.mirrorCell,'Edge segments do not reverse');
 const empty=segments.filter(s=>s.role===null),pairs=empty.filter(s=>s.segment<s.mirrorSegment).map(s=>[s.cell,s.mirrorCell]);
 const fixed=empty.filter(s=>s.cell===s.mirrorCell).map(s=>s.cell);
 return {k,branch,transform:'[q2+k-7, q3, q0+7-k, q1]',properHalfTurn:true,axis,regionCells:region.length,faces:faceOwners.size,octahedralGroups:groups.length,subdivisionPreserved:true,completedStages,terminalStep:step,closureRoundSizes:state.closureRounds.map(r=>r.length),segments,unassignedEdgePairs:pairs,fixedUnassignedEdgeCells:fixed};
}
