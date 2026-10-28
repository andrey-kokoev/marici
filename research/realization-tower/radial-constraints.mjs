import {cells,apex,seed} from './normal-ray-model.mjs';
import {lattice,measureSurfaceLayers,cellWeights} from '../strominger/demos/particle-overlap-tetrahedron/simplex-model.mjs';
const key=face=>face.map(p=>p.join(',')).sort().join('|');
const center=id=>cells[id].vertices[0].map((_,i)=>cells[id].vertices.reduce((s,p)=>s+p[i]/4,0));
const cache=new Map();
const permutations=xs=>xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(rest=>[x,...rest])):[[]];
function topology(k){
 if(cache.has(k))return cache.get(k);
 const ids=cells.filter(c=>c.vertices.every(p=>p[0]<=-5+k)).map(c=>c.id);
 const corners=[apex,...[1,2,3].map(j=>apex.map((x,i)=>x+(i===0?k:i===j?-k:0)))];
 const barycenter=apex.map((_,i)=>corners.reduce((s,p)=>s+p[i]/4,0));
 const containing=ids.filter(id=>cellWeights(barycenter,lattice.cells[id]).every(w=>w>=-1e-9));
 // Even sizes have a central octahedron / multiple triangulation pieces.
 // Do not choose an arbitrary tetrahedron or overwrite the k=1 E seed.
 const centralCell=k>1&&containing.length===1?containing[0]:null;
 const incidence=new Map(),neighbors=new Map(ids.map(id=>[id,[]])),surface=new Set();
 for(const id of ids)for(let omit=0;omit<4;omit++){
  const face=cells[id].vertices.filter((_,i)=>i!==omit),signature=key(face);
  if(!incidence.has(signature))incidence.set(signature,{face,ids:[]});incidence.get(signature).ids.push(id);
 }
 for(const {face,ids:owners} of incidence.values()){
  if(owners.length===1)surface.add(owners[0]);
  else if(owners.length===2){neighbors.get(owners[0]).push({cell:owners[1],sharedFace:face});neighbors.get(owners[1]).push({cell:owners[0],sharedFace:face});}
 }
 const depth=measureSurfaceLayers({cells:ids.map(id=>lattice.cells[id]),assembly:{components:ids.map(id=>lattice.assembly.components[id])}});
 const centralNeighbors=centralCell===null?[]:neighbors.get(centralCell).slice().sort((a,b)=>a.cell-b.cell);
 const cornerCells=corners.map(p=>ids.find(id=>cells[id].vertices.some(q=>q.every((x,i)=>x===p[i]))));
 const distances=cornerCells.map(target=>{
  const d=new Map([[target,0]]),queue=[target];
  for(let i=0;i<queue.length;i++)for(const n of neighbors.get(queue[i]))if(n.cell!==centralCell&&!d.has(n.cell)){d.set(n.cell,d.get(queue[i])+1);queue.push(n.cell);}
  return d;
 });
 let options=[],minimum=Infinity;
 if(centralNeighbors.length===4)for(const order of permutations(centralNeighbors.map(n=>n.cell))){
  const cost=order.reduce((s,id,i)=>s+(distances[i].get(id)??Infinity),0);
  if(cost<minimum){minimum=cost;options=[];}if(cost===minimum&&Number.isFinite(cost))options.push(order);
 }
 function route(first,vertex){
  const d=distances[vertex],target=cornerCells[vertex],path=[centralCell,first];
  const a=center(centralCell),b=center(target),v=b.map((x,i)=>x-a[i]),len=v.reduce((s,x)=>s+x*x,0);
  const deviation=id=>{const p=center(id),t=p.reduce((s,x,i)=>s+(x-a[i])*v[i],0)/len;return p.reduce((s,x,i)=>s+(x-a[i]-t*v[i])**2,0);};
  while(path.at(-1)!==target){
   const next=neighbors.get(path.at(-1)).filter(n=>n.cell!==centralCell&&d.get(n.cell)===d.get(path.at(-1))-1).sort((x,y)=>deviation(x.cell)-deviation(y.cell)||x.cell-y.cell)[0];
   if(!next)throw Error('Broken radial route');path.push(next.cell);
  }
  return {vertex:vertex+1,neighbor:first,target,path,faces:path.slice(1).map((id,i)=>neighbors.get(path[i]).find(n=>n.cell===id).sharedFace),pathStatus:'geometric-only',roleContinuityVerified:false};
 }
 const connections=options.length===1?options[0].map(route):[];
 const result={ids,corners,barycenter,containing,centralCell,centralNeighbors,cornerCells,neighbors,surface,depth,options,connections};cache.set(k,result);return result;
}
// Collective trial: reserve N corridors before any further P-core growth.
// An existing surface P may terminate a corridor at its E partner.
export function collectiveCorePlan(k,assignments){
 const t=topology(k),roles=new Map(assignments.map(a=>[a.cell,a.role])),core=new Set(),queue=[];
 if(roles.get(t.centralCell)==='proton'){core.add(t.centralCell);queue.push(t.centralCell);}
 for(let i=0;i<queue.length;i++)for(const n of t.neighbors.get(queue[i]))if(!t.surface.has(n.cell)&&roles.get(n.cell)==='proton'&&!core.has(n.cell)){core.add(n.cell);queue.push(n.cell);}
 const disconnectedProtons=assignments.filter(a=>a.role==='proton'&&!t.surface.has(a.cell)&&!core.has(a.cell)).map(a=>a.cell);
 const routes=[],blocked=[],pending=new Set();
 for(const electron of assignments.filter(a=>a.role==='electron'&&t.surface.has(a.cell)).map(a=>a.cell).sort((a,b)=>a-b)){
  const paths=[[electron]],seen=new Set([electron]);let found=null;
  for(let i=0;i<paths.length&&!found;i++){
   const path=paths[i],last=path.at(-1);
   if(core.has(last)){found=path.slice().reverse();break;}
   for(const {cell} of t.neighbors.get(last).slice().sort((a,b)=>a.cell-b.cell)){
    const role=roles.get(cell);
    const permitted=core.has(cell)||role==='neutron'||!role||(path.length===1&&role==='proton'&&t.surface.has(cell));
    if(permitted&&!seen.has(cell)){seen.add(cell);paths.push([...path,cell]);}
   }
  }
  if(!found){blocked.push({electron,reason:'No face-connected N corridor to the central P component'});continue;}
  const newNeutrons=found.filter(id=>!roles.has(id));newNeutrons.forEach(id=>pending.add(id));
  routes.push({electron,path:found,faces:found.slice(1).map((id,i)=>t.neighbors.get(found[i]).find(n=>n.cell===id).sharedFace),established:newNeutrons.length===0,viaSurfaceProton:roles.get(found.at(-2))==='proton'&&t.surface.has(found.at(-2))});
 }
 return {core:[...core],disconnectedProtons,routes,blocked,members:disconnectedProtons.length?[]:[...pending].sort((a,b)=>a-b).map(cell=>({cell,role:'neutron'})),status:!core.size?'no-core':disconnectedProtons.length?'disconnected-core':blocked.length?'partially-blocked':routes.every(r=>r.established)?'connected':'planned'};
}
export function radialConstraints(k,assignments){
 if(!Number.isInteger(k)||k<1||k>7)throw Error('k must be 1..7');
 const t=topology(k),roles=new Map(assignments.map(a=>[a.cell,a.role]));
 const first=t.connections.find(c=>c.vertex===1);
 const centralChannel=first?{...first,cell:first.neighbor,sharedFace:first.faces[0],role:null,orientation:'toward-V1',localConnectionEstablished:false}:null;
 const layers=Array.from({length:t.depth.maxLayer},(_,i)=>{
  const insideLayer=i+1,ids=t.ids.filter((_,j)=>t.depth.maxLayer-t.depth.cellLayers[j]+1===insideLayer);
  // Only the central P has an explicit per-cell constraint;
  // grouped shell depth alone is not a unique central-cell selector at k=5.
  const allowedRoles=insideLayer<t.depth.maxLayer?['proton','neutron']:['electron','proton','neutron'];
  const exceptions=ids.filter(id=>id===t.centralCell).map(cell=>({cell,allowedRoles:['proton']}));
  return {insideLayer,cells:ids,allowedRoles,exceptions,assigned:ids.filter(id=>roles.has(id)).map(cell=>({cell,role:roles.get(cell)})),unassigned:ids.filter(id=>!roles.has(id))};
 });
 const conflicts=layers.flatMap(l=>l.assigned.filter(a=>!(l.exceptions.find(e=>e.cell===a.cell)?.allowedRoles??l.allowedRoles).includes(a.role)).map(a=>({...a,insideLayer:l.insideLayer})));
 const surfaceElectrons=assignments.filter(a=>a.role==='electron'&&t.surface.has(a.cell)).map(a=>({cell:a.cell,
  protonPartners:t.neighbors.get(a.cell).filter(n=>roles.get(n.cell)==='proton').map(n=>({cell:n.cell,onSurface:t.surface.has(n.cell)})),
  inwardCandidates:t.neighbors.get(a.cell).filter(n=>!t.surface.has(n.cell)&&(!roles.has(n.cell)||roles.get(n.cell)==='proton')).map(n=>n.cell),
  blockedInward:t.neighbors.get(a.cell).filter(n=>!t.surface.has(n.cell)&&roles.has(n.cell)&&roles.get(n.cell)!=='proton').map(n=>({cell:n.cell,role:roles.get(n.cell)})),
  hasInteriorFaceNeighbor:t.neighbors.get(a.cell).some(n=>!t.surface.has(n.cell)),
 }));
 return {available:t.centralCell!==null,centralCell:t.centralCell,center:t.barycenter,centerCandidates:t.containing,centralNeighbors:t.centralNeighbors,centralChannel,layers,conflicts,surfaceElectrons,
  orientationCount:t.options.length,orientationOptions:t.options.map(order=>order.map((cell,i)=>({vertex:i+1,cell}))),connections:t.connections,
  status:k===1?'degenerate-seed':t.centralCell===null?'center-needs-octahedral-rule':t.options.length!==1?'branch-orientation-ambiguous':'unique-branch-orientation'};
}
