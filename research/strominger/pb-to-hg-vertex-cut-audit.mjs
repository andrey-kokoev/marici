import {lead208Bodies} from './demos/particle-overlap-tetrahedron/lead208-model.mjs';
import {items,lattice,witnessPairs} from './demos/particle-overlap-tetrahedron/fiber-space-model.mjs';
import {envelopeCoordinates,faces} from './demos/particle-overlap-tetrahedron/simplex-model.mjs';
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
function contextShape(item){
 const components=item.children.map(id=>lattice.cells[id].map(n=>lattice.nodes[n].address));
 const table=new Map();for(const component of components)for(const indices of faces){const polygon=indices.map(i=>component[i]),k=key(polygon);if(!table.has(k))table.set(k,{polygon,count:0});table.get(k).count++;}
 return {vertices:[...new Map(components.flat().map(p=>[p.join(','),p])).values()],faces:[...table.values()].filter(f=>f.count===1).map(f=>f.polygon)};
}
function componentsOf(native){
 const byFace=new Map(),adj=native.map(()=>new Set());
 native.forEach((n,i)=>n.shape.faces.forEach(f=>{const k=key(f);if(!byFace.has(k))byFace.set(k,[]);byFace.get(k).push(i);}));
 for(const owners of byFace.values())for(const a of owners)for(const b of owners)if(a!==b)adj[a].add(b);
 const seen=new Set();let count=0;for(let i=0;i<native.length;i++)if(!seen.has(i)){count++;const q=[i];seen.add(i);for(let j=0;j<q.length;j++)for(const n of adj[q[j]])if(!seen.has(n)){seen.add(n);q.push(n);}}
 return count;
}
export function auditPbToHgVertexCuts(){
 const context=items.filter(i=>i.layer<3).map(i=>({owner:`context:${i.index}`,shape:contextShape(i)}));
 const native=[...context,...lead208Bodies.flatMap(b=>(b.shape.parts??[b.shape]).map(shape=>({owner:b.id,shape})))];
 const caps=envelopeCoordinates.map((tip,axis)=>{
  const proton=lead208Bodies.find(b=>b.species==='proton'&&b.shape.vertices.some(v=>String(v)===String(tip)));
  const bodies=lead208Bodies.filter(b=>b.chain===proton.chain),ids=new Set(bodies.map(b=>b.id));
  const capMaximum=Math.max(...native.filter(n=>ids.has(n.owner)).flatMap(n=>n.shape.vertices.map(v=>v[axis])));
  const restMinimum=Math.min(...native.filter(n=>!ids.has(n.owner)).flatMap(n=>n.shape.vertices.map(v=>v[axis])));
  return {vertex:axis+1,axis,chain:proton.chain,bodies:[...ids],plane:-4,capMaximum,restMinimum,
   separable:capMaximum===-4&&restMinimum>=-4};
 });
 const pairs=caps.flatMap((a,i)=>caps.slice(i+1).map(b=>{
  const removed=new Set([...a.bodies,...b.bodies]),remaining=lead208Bodies.filter(p=>!removed.has(p.id));
  const species=Object.fromEntries(['proton','neutron','electron'].map(s=>[s,remaining.filter(p=>p.species===s).length]));
  return {vertices:[a.vertex,b.vertex],removed:[...removed],...species,
   retainedWitnesses:remaining.filter(p=>p.role==='witness').length,
   witnessMatchingIntact:witnessPairs.every(p=>remaining.some(b=>b.role==='witness'&&b.shape.itemIndex===p.outer)),
   connectedComponents:componentsOf(native.filter(n=>!removed.has(n.owner)))};
 }));
 return {carrier:'existing tetrahedral Pb assembly with outward chains',caps,pairs,
  scope:'Exact planar cap separability, retained witnesses, species counts and shared-face connectivity. No claim of isotope stability or equivalence to the five-unit octahedron.'};
}
