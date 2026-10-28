import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {centralParentPoint,buildCentralBeltLayout} from './central-belt-layout.mjs';
import {worldPoint} from './normal-ray-model.mjs';
const sub=(a,b)=>a.map((v,i)=>v-b[i]),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),mul=(a,s)=>a.map(v=>v*s),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],unit=a=>mul(a,1/Math.hypot(...a)),mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0)),key=vs=>vs.map(v=>v.join(',')).sort().join('|');
export function auditBeltParentGluing(){
 const model=buildFoldedFibration(),layout=buildCentralBeltLayout(),parents=[];
 for(const [copy,label,sign] of [['original','+N',-1],['clone','−N',1]]){
  const cells=model.occurrences.filter(c=>c.copy===copy),pose=p=>worldPoint(centralParentPoint(p,copy)),tip=pose(model.bindings.find(b=>b.text===label&&b.copies.includes(copy)).point),axis=mul(layout.normal,sign),faces=new Map();
  for(const c of cells)for(const f of c.faces){const k=key(f);if(!faces.has(k))faces.set(k,{face:f,owners:[]});faces.get(k).owners.push(c);}
  const boundary=[...faces.values()].filter(f=>f.owners.length===1),alignments=boundary.map(({face,owners})=>{const [a,b,c]=face.map(pose),centre=mean(face.map(pose)),ownerCentre=mean(owners[0].vertices.map(pose));let normal=unit(cross(sub(b,a),sub(c,a)));if(dot(normal,sub(centre,ownerCentre))<0)normal=mul(normal,-1);return dot(normal,axis);});
  const unitEdge=Math.hypot(...sub(pose(cells[0].faces[0][0]),pose(cells[0].faces[0][1]))),cutDepth=2*unitEdge*Math.sqrt(2/3),depth=p=>dot(sub(tip,pose(p)),axis),cap=cells.filter(c=>c.vertices.every(v=>depth(v)<=cutDepth+1e-9)),capIds=new Set(cap.map(c=>c.id));
  const cutFaces=[...faces.values()].filter(f=>f.owners.length===2&&f.owners.filter(c=>capIds.has(c.id)).length===1);
  parents.push({copy,label,boundaryFaces:boundary.length,normalClasses:[...new Set(alignments.map(v=>Number(v.toFixed(9))))].sort(),facingParallelFaces:alignments.filter(v=>Math.abs(v-1)<1e-9).length,oppositeFacingParallelFaces:alignments.filter(v=>Math.abs(v+1)<1e-9).length,capAlternative:{applied:false,cutDepth,cells:cap.map(c=>({id:c.id,kind:c.vertices.length===6?'octahedron':'tetrahedron'})),exposedFaces:cutFaces.map(f=>f.face),scope:'Removing this native two-layer corner would expose four faces; not authorized or applied.'}});
 }
 return {obligation:'forward realization / geometric attachment',status:parents.every(p=>p.facingParallelFaces===0)?'blocked-intact-N-axis-face-gluing':'requires-registration',constraints:['intact parents','N vertex normals aligned to belt axis','opposite planar four-triangle belt patches','rigid placement only','nonoverlapping cells'],parents,scope:'Boundary-normal obstruction is invariant under translation and roll about the N axis. This does not reject vertex contact, a bent connector, reorientation or a retained corner decomposition. No geometry or wiring is changed.'};
}
