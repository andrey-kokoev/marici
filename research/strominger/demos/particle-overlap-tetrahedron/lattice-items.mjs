// Local honeycomb geometry only: no assembled layers, particle counts or layout search.
import {primitives} from './simplex-components.mjs';
const units=primitives.regular.vertices,permutations=[[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]];
const faces=[[0,2,1],[0,1,3],[0,3,2],[1,2,3]];
export const itemKey=vertices=>vertices.map(p=>p.join(',')).sort().join('|');
const templates=[{kind:'tetrahedron',inverted:false,vertices:units},{kind:'tetrahedron',inverted:true,vertices:units.map(p=>p.map(x=>-x))},{kind:'octahedron',inverted:false,vertices:units.flatMap((a,i)=>units.slice(i+1).map(b=>a.map((x,j)=>x+b[j])))}];
export function makeLatticeItem(kind,origin,inverted=false){
 if(!['tetrahedron','octahedron'].includes(kind)||origin.length!==4||!origin.every(Number.isInteger)||origin.reduce((a,b)=>a+b,0)!==(kind==='octahedron'?-1:inverted?2:0))throw RangeError('Invalid lattice item');
 const components=kind==='tetrahedron'?[units.map(p=>origin.map((x,i)=>x+(inverted?-p[i]:p[i])))]:permutations.map(perm=>primitives.splitOctahedron.vertices.map(p=>origin.map((x,i)=>x+p[perm[i]])));
 const vertices=[...new Map(components.flat().map(p=>[p.join(','),p])).values()],table=new Map();
 for(const c of components)for(const f of faces){const face=f.map(i=>c[i]),k=itemKey(face);if(!table.has(k))table.set(k,{vertices:face,count:0});table.get(k).count++;}
 return {kind,origin:[...origin],inverted,components,vertices,key:itemKey(vertices),faces:[...table.values()].filter(f=>f.count===1).map(f=>f.vertices),center:vertices.reduce((a,p)=>a.map((x,i)=>x+p[i]/vertices.length),[0,0,0,0])};
}
export function acrossFace(source,face){
 const fk=itemKey(face);if(!source.faces.some(f=>itemKey(f)===fk))throw RangeError('Attachment must be a complete boundary face');
 const candidates=new Map();
 for(const t of templates)for(const offset of t.vertices){
  const origin=face[0].map((x,i)=>x-offset[i]),vertices=t.vertices.map(p=>p.map((x,i)=>x+origin[i]));
  if(!face.every(p=>vertices.some(q=>p.every((x,i)=>x===q[i]))))continue;
  const s=makeLatticeItem(t.kind,origin,t.inverted);if(s.key!==source.key&&s.faces.some(f=>itemKey(f)===fk))candidates.set(s.key,s);
 }
 if(candidates.size!==1)throw Error('Expected one neighboring lattice item across '+fk+'; found '+candidates.size);
 return [...candidates.values()][0];
}
