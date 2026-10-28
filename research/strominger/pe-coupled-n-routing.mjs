import {buildPESymmetricSector,dualPoint} from './pe-symmetric-sector.mjs';
import {buildNEdgeTubes} from './n-edge-tubes.mjs';
import {worldPoint} from '../realization-tower/normal-ray-model.mjs';
const key=ps=>ps.map(p=>p.join(',')).sort().join('|'),mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i],0)/ps.length),sub=(a,b)=>a.map((x,i)=>x-b[i]),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],passKey=(cell,a,b)=>`${cell}::${[a,b].sort().join('::')}`,endKey=p=>[p.fromPort,p.toPort].sort().join('::');
export function probePECoupledNRouting(radius=3,extraShell=2,{occupied=true,routingPolicy='cyclic'}={}){
 if(!Number.isInteger(radius)||radius<0||radius>3||![2,3].includes(extraShell))throw Error('Radius 0..3, ambient shell 2 or 3 required');
 if(!['cyclic','reverse','vacancy-reversed','occupied-reversed','occupied-only','vacancy-only','both-triplets','equator-reversed','both-triplets-odd'].includes(routingPolicy))throw Error('Unknown routing policy');
 const object=buildPESymmetricSector(radius),ambient=buildPESymmetricSector(radius+extraShell),baseline=buildNEdgeTubes(ambient),occupiedFaces=new Map();
 if(occupied)for(const c of object.cells.filter(c=>c.role!=='neutron'))for(const f of c.faces)occupiedFaces.set(key(f),c.role);
 const locals=new Map(),edgeOwners=new Map(),points=new Map();for(const p of baseline.passes){if(!locals.has(p.cell))locals.set(p.cell,new Map());const m=locals.get(p.cell),[a,b]=p.portKeys;m.set(a,b);m.set(b,a);for(let i=0;i<2;i++){const port=p.portKeys[i];points.set(port,p.points[i]);if(!edgeOwners.has(port))edgeOwners.set(port,[]);edgeOwners.get(port).push(p.cell);}}
 const switches=[];
 for(const c of ambient.cells.filter(c=>c.role==='neutron')){const typed=c.faces.map(face=>({face,role:occupiedFaces.get(key(face))})),active=typed.filter(f=>f.role),drive=active.reduce((s,f)=>s+(f.role==='proton'?1:-1),0);if(!drive)continue;
  const candidates=active.length===1?active:active.length===7?typed.filter(f=>!f.role):[];if(Math.abs(drive)!==1||candidates.length!==1)throw Error(`Unspecified P/E coupling at ${c.id}`);
  if((routingPolicy==='occupied-only'&&active.length!==1)||(routingPolicy==='vacancy-only'&&active.length!==7))continue;
  const face=[...candidates[0].face],centre=mean(c.vertices),v=face.map(worldPoint);if(dot(cross(sub(v[1],v[0]),sub(v[2],v[0])),sub(worldPoint(mean(face)),worldPoint(centre)))<0)[face[1],face[2]]=[face[2],face[1]];
  const ports=face.map((p,i)=>key([p,face[(i+1)%3]])),m=locals.get(c.id),opposites=ports.map(p=>m.get(p));
  // A reversible matching: three face ports to three opposite-face ports.
  // Sign reverses the cyclic permutation; the other three strands are intact.
  const handedness=routingPolicy==='reverse'||(routingPolicy==='vacancy-reversed'&&active.length===7)||(routingPolicy==='occupied-reversed'&&active.length===1)?-1:1;
  for(let i=0;i<3;i++){const j=(i+(drive*handedness>0?1:2))%3;m.set(ports[i],opposites[j]);m.set(opposites[j],ports[i]);}
  if(['both-triplets','equator-reversed','both-triplets-odd'].includes(routingPolicy)){
   const oppositeVertices=face.map(p=>p.map((x,i)=>2*centre[i]-x)),equator=face.map((p,i)=>key([p,oppositeVertices[(i+1)%3]])),across=equator.map(p=>m.get(p)),turn=routingPolicy==='both-triplets-odd'?drive:routingPolicy==='equator-reversed'?-1:1;
   for(let i=0;i<3;i++){const j=(i+(turn>0?1:2))%3;m.set(equator[i],across[j]);m.set(across[j],equator[i]);}
  }
  switches.push({cell:c.id,drive,occupiedFaces:active.length,facePorts:ports,faceVertices:face});
 }
 for(const sw of switches){const c=ambient.cells.find(c=>c.id===sw.cell),centre=mean(c.vertices),face=sw.faceVertices,opposite=face.map(p=>p.map((x,i)=>2*centre[i]-x)),rotate=new Map();for(const tri of [face,opposite])for(let i=0;i<3;i++)rotate.set(tri[i].join(','),tri[(i+1)%3]);const edgeR=edge=>key(edge.split('|').map(p=>rotate.get(p))),m=locals.get(sw.cell);for(const[a,b]of m)if(m.get(edgeR(a))!==edgeR(b))throw Error('Coupling broke threefold symmetry');}
 for(const m of locals.values())for(const[a,b]of m)if(a===b||m.get(b)!==a)throw Error('Routing is not a reversible port matching');
 const paths=[],seen=new Set();
 function trace(startCell,startPort){let cell=startCell,entry=startPort;const passes=[],polyline=[points.get(entry)];let closed=false,endPort;
  while(true){const exit=locals.get(cell).get(entry),id=passKey(cell,entry,exit);if(seen.has(id))throw Error('Strands merged or were counted twice');seen.add(id);passes.push({cell,entry,exit,id});polyline.push(points.get(exit));const next=edgeOwners.get(exit).find(id=>id!==cell);if(!next){endPort=exit;break;}if(next===startCell&&exit===startPort){closed=true;endPort=exit;break;}cell=next;entry=exit;}
  paths.push({id:`coupled-N:${paths.length}`,fromPort:startPort,toPort:endPort,closed,passes,points:polyline});
 }
 for(const[port,owners]of edgeOwners)if(owners.length===1&&!seen.has(passKey(owners[0],port,locals.get(owners[0]).get(port))))trace(owners[0],port);
 for(const[cell,m]of locals)for(const[port,exit]of m)if(!seen.has(passKey(cell,port,exit)))trace(cell,port);
 const baselineEnds=new Set(baseline.paths.map(endKey)),baselinePasses=new Set(baseline.passes.map(p=>passKey(p.cell,...p.portKeys))),open=paths.filter(p=>!p.closed),loops=paths.filter(p=>p.closed),changed=open.filter(p=>p.passes.some(pass=>!baselinePasses.has(pass.id))),rerouted=open.filter(p=>!baselineEnds.has(endKey(p)));
 if(seen.size!==baseline.passes.length)throw Error('Lost local fibre states');
 const dualEdge=edge=>key(edge.split('|').map(p=>dualPoint(p.split(',').map(Number)))),geometries=new Map(ambient.cells.map(c=>[key(c.vertices),c.id]));
 for(const c of ambient.cells.filter(c=>c.role==='neutron')){const dual=locals.get(geometries.get(key(c.vertices.map(dualPoint))));for(const[a,b]of locals.get(c.id))if(dual.get(dualEdge(a))!==dualEdge(b))throw Error('Coupling broke P/E geometric duality');}
 const traceKey=points=>{const a=points.map(p=>p.join(',')).join(';'),b=[...points].reverse().map(p=>p.join(',')).join(';');return a<b?a:b;},changedByTrace=new Map(changed.map(p=>[traceKey(p.points),p])),paired=new Set(),dualPairs=[];let selfDual=0;
 for(const p of changed){if(paired.has(p.id))continue;const other=changedByTrace.get(traceKey(p.points.map(dualPoint)));if(!other)throw Error('Response trace lacks its full geometric dual');paired.add(p.id);paired.add(other.id);if(other.id===p.id)selfDual++;else dualPairs.push([p.id,other.id]);}
 for(const p of changed){const touched=p.passes.flatMap((pass,i)=>baselinePasses.has(pass.id)?[]:[i]);p.responsePoints=p.points.slice(touched[0],touched.at(-1)+2);}
 return {paths,changedPaths:changed,dualPairs,switches,localRouting:locals,baseline,audit:{radius,extraShell,routingPolicy,occupiedPECells:occupied?object.cells.filter(c=>c.role!=='neutron').length:0,coupledNCells:switches.length,positiveSwitches:switches.filter(s=>s.drive>0).length,negativeSwitches:switches.filter(s=>s.drive<0).length,ambientOpenChannels:baseline.paths.length,openChannels:open.length,unchangedOpenChannels:open.length-changed.length,changedOpenChannels:changed.length,reroutedBoundaryPairs:rerouted.length,closedLoops:loops.length,dualResponsePairs:dualPairs.length,selfDualResponses:selfDual,dualityVerified:true,threefoldSymmetryVerified:true,loopPasses:loops.reduce((s,p)=>s+p.passes.length,0),localPasses:seen.size,branchingJunctions:0,localizedNeutronCount:null,scope:'Trial occupancy-driven port matching; routingPolicy identifies the chosen extension. Balanced cells remain straight. Reversibility, threefold symmetry and geometric P/E duality are checked, but do not uniquely fix the matching. No particle count or trapping stability inferred.'}};
}
