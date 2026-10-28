// Process 4: seed-first retained carrier construction.
// No completed Pb loadout, particle-count assignment or chart permutation input.
import {primitives} from '../strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs';
import {seed} from './normal-ray-model.mjs';
const units=primitives.regular.vertices;
const permutations=[[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]];
const triangleIndices=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]];
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
const templates=[
 {kind:'tetrahedron',inverted:false,vertices:units},
 {kind:'tetrahedron',inverted:true,vertices:units.map(v=>v.map(x=>-x))},
 {kind:'octahedron',vertices:units.flatMap((a,i)=>units.slice(i+1).map(b=>a.map((x,j)=>x+b[j])))},
];
function shape(kind,origin,inverted=false){
 const components=kind==='tetrahedron'?[units.map(v=>v.map((x,i)=>origin[i]+(inverted?-x:x)))]:permutations.map(p=>primitives.splitOctahedron.vertices.map(v=>origin.map((x,i)=>x+v[p[i]])));
 const vertices=[...new Map(components.flat().map(v=>[v.join(','),v])).values()],boundary=new Map();
 for(const c of components)for(const indices of triangleIndices){const face=indices.map(i=>c[i]),id=key(face);const prior=boundary.get(id);boundary.set(id,{vertices:face,count:(prior?.count??0)+1});}
 return {id:key(vertices),kind,components,vertices,faces:[...boundary.values()].filter(f=>f.count===1).map(f=>f.vertices)};
}
const neighborCache=new Map();
function across(body,face){
 const id=body.id+'>'+key(face);if(neighborCache.has(id))return neighborCache.get(id);
 const choices=new Map();
 for(const t of templates)for(const v of t.vertices){
  const origin=face[0].map((x,i)=>x-v[i]);
  const vertices=t.vertices.map(v=>v.map((x,i)=>origin[i]+x));
  if(!face.every(p=>vertices.some(q=>p.every((x,i)=>x===q[i]))))continue;
  const candidate=shape(t.kind,origin,t.inverted);
  if(candidate.id!==body.id&&candidate.faces.some(f=>key(f)===key(face)))choices.set(candidate.id,candidate);
 }
 if(choices.size!==1)throw Error('Ambiguous honeycomb face continuation');
 const result=[...choices.values()][0];neighborCache.set(id,result);return result;
}
const inside=b=>b.vertices.every(v=>v.every(x=>x<=2));

// Each round reads ONE prior snapshot. Merge all parents, rather than selecting
// a privileged first-arrival branch. No counts or target body IDs guide growth.
export function constructRetainedCarrier({reverse=false}={}){
 const central=shape('tetrahedron',[0,0,0,0]);
 const accepted=new Map([[central.id,{...central,round:0,parents:[],branches:[]}]]);
 const rounds=[[central.id]],history=[{round:0,added:[central.id],rule:'upright unit-simplex seed'}];
 let frontier=[accepted.get(central.id)];
 while(frontier.length){
  const pending=new Map();
  for(const parent of reverse?[...frontier].reverse():frontier)for(const face of reverse?[...parent.faces].reverse():parent.faces){
   const candidate=across(parent,face);if(!inside(candidate)||accepted.has(candidate.id))continue;
   if(!pending.has(candidate.id))pending.set(candidate.id,{...candidate,round:rounds.length,parents:[],branches:[]});
  }
  if(!pending.size)break;
  // Recover every previously admitted contact, including older rounds.
  for(const candidate of pending.values()){
   const branches=new Set();
   for(const face of candidate.faces){
    const parent=accepted.get(across(candidate,face).id);if(!parent)continue;
    candidate.parents.push({id:parent.id,face:key(face)});
    if(parent.round===0){const branch=units.findIndex(v=>!face.some(p=>p.every((x,i)=>x===v[i])));if(branch<0)throw Error('Missing seed-face branch');branches.add(branch+1);}
    else for(const branch of parent.branches)branches.add(branch);
   }
   candidate.parents.sort((a,b)=>a.id.localeCompare(b.id));candidate.branches=[...branches].sort();
   if(!candidate.parents.length)throw Error('Unattached growth candidate');
  }
  frontier=[...pending.values()].sort((a,b)=>a.id.localeCompare(b.id));
  for(const body of frontier)accepted.set(body.id,body);
  rounds.push(frontier.map(b=>b.id));history.push({round:rounds.length-1,added:rounds.at(-1),rule:'simultaneous complete-face attachment; all prior parents retained'});
  if(rounds.length>100)throw Error('Construction failed to terminate');
 }
 // Retain all shared incidences, including contacts within one growth round.
 const faceTable=new Map();
 for(const body of accepted.values())for(const face of body.faces){const id=key(face);if(!faceTable.has(id))faceTable.set(id,[]);faceTable.get(id).push(body.id);}
 const contacts=[...faceTable].filter(([,owners])=>owners.length===2).map(([face,owners])=>({face,owners:owners.sort()})).sort((a,b)=>a.face.localeCompare(b.face));
 if([...faceTable.values()].some(owners=>owners.length>2))throw Error('Nonmanifold attachment');
 return {bodies:[...accepted.values()],rounds,history,contacts};
}
const plan=constructRetainedCarrier();
export const retainedPbStages=plan.rounds.map((ids,i)=>i===0?'Start with one central retained seed. No Pb assembly is loaded.':`Round ${i}: attach ${ids.length} new whole cells across complete faces; retain all parents and branch histories.`);
export function retainedPbProcess(k,step){
 if(!Number.isInteger(k)||k<1||k>7||!Number.isInteger(step)||step<0||step>=retainedPbStages.length)throw Error('Invalid Process 4 state');
 const bodies=plan.bodies.filter(b=>b.round<=step),ids=new Set(bodies.map(b=>b.id));
 const contacts=plan.contacts.filter(c=>c.owners.every(id=>ids.has(id)));
 const last=step===retainedPbStages.length-1;
 return {k:7,step,end:seed,assignments:[],firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],
 history:plan.history.slice(0,step+1),retainedBodies:bodies,canAdvance:!last,
 summary:retainedPbStages[step]+(last?' Carrier envelope complete. Particle/carrier and marked-contact binding is the next gate; Pb species counts have not been assigned.':''),
 retainedAudit:{input:'central unit simplex and k=7 envelope; no completed loadout',geometryOnly:true,bodyCount:bodies.length,
 tetrahedra:bodies.filter(b=>b.kind==='tetrahedron').length,octahedra:bodies.filter(b=>b.kind==='octahedron').length,
 primitiveComponents:bodies.reduce((n,b)=>n+b.components.length,0),contacts:contacts.length,
 branches:[1,2,3,4].map(branch=>({branch,bodies:bodies.filter(b=>b.branches.includes(branch)).length})),
 envelopeComplete:last,particleRolesAssigned:false,nativeWitnessEstablished:false,isotopeFormationEstablished:false,full4x28Established:false},
 retainedContacts:contacts};
}
