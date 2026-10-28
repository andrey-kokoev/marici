import {nativeFaceRole} from './native-face-role.mjs';
import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {worldPoint} from './normal-ray-model.mjs';
const add=(a,b)=>a.map((v,i)=>v+b[i]),sub=(a,b)=>a.map((v,i)=>v-b[i]),mul=(a,s)=>a.map(v=>v*s),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],unit=a=>mul(a,1/Math.hypot(...a)),mean=ps=>mul(ps.reduce(add,ps[0].map(()=>0)),1/ps.length),key=p=>p.join(',');
// Select complete existing ESD7 cells, with integer barycentric addresses.
// This coordinate box in sum(q)=1 is a regular edge-two octahedron.
const geometry=buildFoldedFibration().geometry;
const faceKey=vs=>vs.map(key).sort().join('|'),tetrahedronAtFace=new Map();
for(const c of geometry.filter(c=>c.kind==='tetrahedron'))for(const f of c.faces)tetrahedronAtFace.set(faceKey(f),c);
// Extend the source lattice's tetrahedral orientation colors to every unit
// triangle, even at the finite source boundary. This is not a flux map.
function faceColor(indices){
 const vs=indices.map(i=>nativeVertices[i]),upper=vs[0].map((_,j)=>Math.max(...vs.map(v=>v[j]))),sum=upper.reduce((a,b)=>a+b,0);
 if(sum!==2&&sum!==3)throw Error('Unexpected native unit triangle');
 const colorRole=nativeFaceRole(vs),c=tetrahedronAtFace.get(faceKey(vs));
 if(c&&c.role!==colorRole)throw Error('Face color disagrees with native tetrahedron');
 return {colorRole,colorSourceGeometry:c?.id??null,colorRule:'native-tetrahedral-orientation'};
}
const nativeCentre=[1,0,0,0],source=geometry.filter(c=>c.vertices.every(v=>v.every((q,i)=>Math.abs(q-nativeCentre[i])<=1)));
const nativeVertices=[...new Map(source.flatMap(c=>c.vertices).map(v=>[key(v),v])).values()],index=new Map(nativeVertices.map((v,i)=>[key(v),i])),nativeWorld=nativeVertices.map(worldPoint),centre=worldPoint(nativeCentre);
const faceMap=new Map();
for(const c of source)for(const triangle of c.faces){const indices=triangle.map(v=>index.get(key(v))),k=[...indices].sort((a,b)=>a-b).join(':');if(!faceMap.has(k))faceMap.set(k,{indices,owners:[]});faceMap.get(k).owners.push(c.id);}
const nativeFaces=[...faceMap.values()],boundary=nativeFaces.filter(f=>f.owners.length===1),boundaryIndices=[...new Set(boundary.flatMap(f=>f.indices))];
const upper=boundary.filter(f=>f.indices.every(i=>nativeVertices[i][0]===2)),upperVertices=[...new Set(upper.flatMap(f=>f.indices))],upperCentre=mean(upperVertices.map(i=>nativeWorld[i]));
const corners=upperVertices.filter(i=>nativeVertices[i].every((q,j)=>Math.abs(q-nativeCentre[j])===1)).sort((a,b)=>key(nativeVertices[a]).localeCompare(key(nativeVertices[b])));
const nativeNormal=unit(sub(upperCentre,centre)),nativeY=unit(sub(nativeWorld[corners[0]],upperCentre)),nativeX=cross(nativeY,nativeNormal);
const halfLength=Math.hypot(...sub(upperCentre,centre)),unitEdge=Math.hypot(...sub(nativeWorld[nativeFaces[0].indices[0]],nativeWorld[nativeFaces[0].indices[1]]));
export const nativeOctahedralBeltMetrics=Object.freeze({unitEdge,halfLength,spacing:halfLength/2.5,pitch:Math.hypot(...sub(nativeWorld[corners[0]],upperCentre))/2/1.25});
export function buildOctahedralBeltSurface(layout){
 const {origin,x,y,normal}=layout;
 // Rigid presentation transform only: no radial projection, scaling or shear.
 const pose=p=>{const d=sub(p,centre);return add(origin,add(add(mul(x,dot(d,nativeX)),mul(y,dot(d,nativeY))),mul(normal,dot(d,nativeNormal))));};
 const allVertices=nativeWorld.map(pose),vertices=boundaryIndices.map(i=>allVertices[i]),boundaryIndex=new Map(boundaryIndices.map((i,j)=>[i,j]));
 function oriented(indices){const [a,b,c]=indices.map(i=>allVertices[i]);return dot(cross(sub(b,a),sub(c,a)),sub(mean([a,b,c]),origin))<0?[indices[0],indices[2],indices[1]]:indices;}
 const faces=boundary.map((f,i)=>{const indices=oriented(f.indices),patch=indices.every(i=>nativeVertices[i][0]===2)?'original':indices.every(i=>nativeVertices[i][0]===0)?'clone':null,fc=mean(indices.map(i=>allVertices[i]));let slot=null;
  if(patch){const sign=patch==='original'?1:-1,d=sub(fc,add(origin,mul(normal,sign*halfLength)));if(Math.hypot(...d)<1e-10)slot=3;else{const angle=Math.atan2(sign*dot(d,y),sign*dot(d,x));slot=((Math.round((angle-Math.PI/2)/(2*Math.PI/3))%3)+3)%3;}}
  return {id:`belt:surface:face:${i}`,indices:indices.map(i=>boundaryIndex.get(i)),owners:[...f.owners],slot,centre:fc,patch,...faceColor(f.indices)};
 });
 function edgesOf(fs){const map=new Map();for(const f of fs)for(let i=0;i<3;i++){const indices=[f.indices[i],f.indices[(i+1)%3]].sort((a,b)=>a-b),k=indices.join(':');if(!map.has(k))map.set(k,{indices,faces:[]});map.get(k).faces.push(f.id);}return [...map.values()];}
 const edges=edgesOf(faces),cellFaces=nativeFaces.map((f,i)=>({...f,...faceColor(f.indices),id:`belt:cell-face:${i}`,surfaceFace:faces[boundary.indexOf(f)]?.id??null})),cells=source.map(c=>({id:`belt:cell:${c.id}`,sourceGeometry:c.id,kind:c.kind,indices:c.vertices.map(v=>index.get(key(v))),faces:cellFaces.filter(f=>f.owners.includes(c.id)).map(f=>f.id)}));
 if(cells.length!==14||faces.length!==32||vertices.length!==18||edges.length!==48)throw Error('Unexpected native octahedral cellulation');
 return {id:'belt:surface:octahedral-2-0',notation:'{3,4+}_{2,0}',embedding:'Native ESD7 tetrahedral–octahedral cellulation; rigid placement at unchanged unit edge length.',vertices,edges,faces,nativeVertices:boundaryIndices.map(i=>nativeVertices[i]),counts:{vertices:18,edges:48,faces:32,euler:2},patches:['original','clone'].map((copy,i)=>({id:`belt:surface:patch:${copy}`,copy,layer:i===0?1:6,faces:faces.filter(f=>f.patch===copy).sort((a,b)=>a.slot-b.slot).map(f=>f.id)})),cellulation:{vertices:allVertices,nativeVertices,cells,faces:cellFaces,edges:edgesOf(cellFaces),nativeCentre,unitEdge,counts:{vertices:19,edges:60,faces:56,cells:14,tetrahedra:8,octahedra:6,internalFaces:24},source:'buildFoldedFibration().geometry',transform:'rigid only',parentLatticeAttachment:null},scope:'Exact cell subcomplex of the ESD7 source lattice, separately rigidly posed. Shared lattice registration and face attachment to the posed parents remain unverified; no native field map.'};
}
