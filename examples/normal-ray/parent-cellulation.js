import {buildFoldedFibration} from '../../research/realization-tower/fibration-folded-process.mjs';
import {nativeFaceRole} from '../../research/realization-tower/native-face-role.mjs';
import {worldPoint} from '../../research/realization-tower/normal-ray-model.mjs';
const model=buildFoldedFibration(),geometries=new Map(model.geometry.map(c=>[c.id,c])),native=new Map(model.occurrences.map(o=>[o.id,geometries.get(o.sourceGeometry)]));
const key=p=>p.map(v=>Number(v.toFixed(7))).join(',');
export function buildParentCellulations(proc){
 const removed=new Set(proc.parentCutAudit?.removedCellIds??[]),replacements=new Set(proc.parentTipReplacementAudit?.cellIds??[]),bodies=[...new Map([...(proc.emptyBodies??[]),...(proc.retainedBodies??[])].map(b=>[b.id,b])).values()].filter(b=>!removed.has(b.id)||replacements.has(b.id));
 return ['original','clone'].map(copy=>{
  const vertices=[],vertexMap=new Map(),faces=new Map(),cells=[];
  const vertex=p=>{const k=key(p);if(!vertexMap.has(k)){vertexMap.set(k,vertices.length);vertices.push(worldPoint(p));}return vertexMap.get(k);};
  for(const body of bodies.filter(b=>b.id.startsWith(copy+':'))){const source=native.get(body.id);if(!source||source.faces.length!==body.faces.length)throw Error('Parent native-face correspondence missing');
   cells.push({id:body.id,kind:source.kind,role:source.kind==='octahedron'?'neutron':replacements.has(body.id)?'electron':nativeFaceRole(source.faces[0]),sourceGeometry:source.id,indices:body.vertices.map(vertex)});
   body.faces.forEach((face,i)=>{const indices=face.map(vertex),k=[...indices].sort((a,b)=>a-b).join(':'),role=replacements.has(body.id)?'electron':nativeFaceRole(source.faces[i]);
    if(!faces.has(k))faces.set(k,{id:`parent:${copy}:face:${faces.size}`,indices,owners:[],colorRole:role,tipReplacement:false});const f=faces.get(k);f.owners.push(body.id);
    if(replacements.has(body.id)){f.colorRole=role;f.tipReplacement=true;}
   });
  }
  const fs=[...faces.values()],edges=new Map();for(const f of fs){if(f.owners.length>2)throw Error('Nonmanifold parent cellulation');for(let i=0;i<3;i++){const indices=[f.indices[i],f.indices[(i+1)%3]].sort((a,b)=>a-b),k=indices.join(':');if(!edges.has(k))edges.set(k,{indices,faces:[]});edges.get(k).faces.push(f.id);}}
  return {id:`parent:${copy}:native-cellulation`,copy,vertices,faces:fs,edges:[...edges.values()],cells,counts:{tetrahedra:cells.filter(c=>c.kind==='tetrahedron').length,octahedra:cells.filter(c=>c.kind==='octahedron').length,exposedFaces:fs.filter(f=>f.owners.length===1).length},scope:'Same native whole-cell grain and face-color convention as belt; explicit E-tip overrides retained.'};
 });
}
