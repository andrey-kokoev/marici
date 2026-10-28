import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {analyzeSeamLattice} from './seam-lattice.mjs';
import {centralParentPoint,buildCentralBeltLayout} from './central-belt-layout.mjs';
import {worldPoint} from './normal-ray-model.mjs';
import {deriveBeltFlux} from './belt-flux-audit.mjs';
const sub=(a,b)=>a.map((v,i)=>v-b[i]),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0));
const sameFace=(a,b)=>a.length===b.length&&a.every(p=>b.some(q=>Math.hypot(...sub(p,q))<1e-7));
// Inventory only: owner particle roles and geometric normals are NOT transport
// directions, capacities, or full-fiber boundary maps.
export function buildBeltParentPortInventory(){
 const parent=buildFoldedFibration(),seam=analyzeSeamLattice(parent.occurrences),owners=new Map(parent.occurrences.map(o=>[o.id,o])),layout=buildCentralBeltLayout(),flow=deriveBeltFlux(layout);
 const ports=seam.pairs.flatMap(pair=>['original','clone'].map(copy=>{
  const owner=owners.get(pair.cells.find(id=>owners.get(id).copy===copy)),faceIndex=owner.faces.findIndex(f=>sameFace(f,pair.face));
  if(faceIndex<0)throw Error('Missing owner face');
  const nativeFace=owner.faces[faceIndex],displayFace=nativeFace.map(p=>centralParentPoint(p,copy)),worldFace=displayFace.map(worldPoint),centroid=mean(worldFace),ownerCentre=mean(owner.vertices.map(p=>worldPoint(centralParentPoint(p,copy))));
  let normal=cross(sub(worldFace[1],worldFace[0]),sub(worldFace[2],worldFace[0]));const magnitude=Math.hypot(...normal);if(magnitude<1e-12)throw Error('Degenerate parent face');normal=normal.map(v=>v/magnitude*(dot(normal,sub(centroid,ownerCentre))<0?-1:1));
  return {id:`${copy}:belt-seam:${pair.id}`,copy,seamPair:pair.id,owner:owner.id,ownerFaceIndex:faceIndex,sourceGeometry:owner.sourceGeometry,sourceParticleRole:owner.role,nativeFace,displayFace,worldFace,centroid,outwardNormal:normal,area:magnitude/2,pairedPort:`${copy==='original'?'clone':'original'}:belt-seam:${pair.id}`,transportDirections:null,fluxCapacity:null,fiberBoundaryMap:null};
 }));
 const requirements=[['original',layout.layers[0]],['clone',layout.layers.at(-1)]].flatMap(([copy,layer])=>layer.nodes.map(n=>({copy,beltNode:n.id,layer:layer.label,star:n.group,arm:n.arm,starCentre:n.starCentre,position:n.position,transportDirection:n.direction,flow:flow.injection[n.id]>0?'parent-to-belt':'belt-to-parent',requiredFlux:flow.nodeRates[n.id],normal:layout.normal.map(v=>v*(n.direction==='P'?1:-1))})));
 const summary=['original','clone'].map(copy=>{const ps=ports.filter(p=>p.copy===copy),rs=requirements.filter(r=>r.copy===copy);return {copy,facePorts:ps.length,uniqueOwners:new Set(ps.map(p=>p.owner)).size,sourceParticleRoles:ps.reduce((a,p)=>(a[p.sourceParticleRole]=(a[p.sourceParticleRole]??0)+1,a),{}),knownDirectionPorts:ps.filter(p=>p.transportDirections!==null).length,knownCapacityPorts:ps.filter(p=>p.fluxCapacity!==null).length,requiredIncomingFlux:rs.filter(r=>r.flow==='parent-to-belt').reduce((s,r)=>s+r.requiredFlux,0),requiredOutgoingFlux:rs.filter(r=>r.flow==='belt-to-parent').reduce((s,r)=>s+r.requiredFlux,0)};});
 return {status:'blocked-missing-parent-transport-contract',scope:'Actual former shared seam faces exposed by the separated parent presentation; no parent links installed.',coordinateSystem:'centroids, normals and requirement positions are world coordinates; displayFace is the viewer chart',normalization:'one unit per outer majority satellite, not a native capacity',ports,requirements,summary,assignment:null,blockers:['Per-face allowed P/E transport directions are absent from the current parent occurrence records.','Per-face flux capacities and full-fiber boundary maps are not specified.','Particle roles, face area and geometric normals cannot substitute for those contracts.'],acceptance:['Retain owner, face and fiber identities in every attachment.','Satisfy every boundary flux demand without exceeding declared port capacity.','Derive both attachments through the parent correspondence, not independent rotated indices.','Replace axial boundary stubs with actual paths and rerun conservation, moment and anisotropy checks.']};
}
