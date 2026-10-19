import {lattice as original,faces} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {makeLatticeItem,acrossFace,itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
const key=a=>[...a].sort((a,b)=>a-b).join(',');
export function probeSpace(expand=false){
 const space=structuredClone(original);if(!expand)return space;
 const owners=new Map(original.assembly.components.map(c=>{const item=makeLatticeItem(c.primitive==='regular'?'tetrahedron':'octahedron',c.origin,c.transform.kind==='inversion');return [item.key,item];}));
 const additions=new Map();for(const item of owners.values())for(const face of item.faces){const next=acrossFace(item,face);if(!owners.has(next.key))additions.set(next.key,next);}
 const nodes=new Map(space.nodes.map((n,i)=>[n.address.join(','),i])),cells=new Set(space.cells.map(c=>itemKey(c.map(v=>space.nodes[v].address))));
 const permutations=[[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]];
 for(const item of [...additions.values()].sort((a,b)=>a.key.localeCompare(b.key)))for(const [j,vertices] of item.components.entries()){
  const k=itemKey(vertices);if(cells.has(k))continue;cells.add(k);
  space.cells.push(vertices.map(address=>{const k=address.join(',');if(!nodes.has(k)){nodes.set(k,space.nodes.length);space.nodes.push({address:[...address]});}return nodes.get(k);}));
  space.assembly.components.push({primitive:item.kind==='tetrahedron'?'regular':'splitOctahedron',origin:[...item.origin],transform:item.inverted?{kind:'inversion'}:{kind:'permutation',permutation:item.kind==='tetrahedron'?[0,1,2,3]:permutations[j]}});
 }
 return space;
}
export function domainOf(space){
 const adjacency=space.cells.map(()=>[]),incidence=new Map();
 space.cells.forEach((c,id)=>faces.forEach(f=>{const face=f.map(i=>c[i]),k=key(face);if(!incidence.has(k))incidence.set(k,{face,ids:[]});incidence.get(k).ids.push(id);}));
 for(const {face,ids} of incidence.values()){if(ids.length>2)throw Error('Non-manifold probe domain');if(ids.length===2){const [a,b]=ids;adjacency[a].push({to:b,face});adjacency[b].push({to:a,face});}}
 return {adjacency,species:space.assembly.components.map(c=>c.primitive==='regular'?'proton':'neutron')};
}
function color(space,domain,nucleus,ms){
 const types=new Map(space.cells[0].map(v=>[v,ms.includes(v)?'M':'C'])),chosen=new Set(nucleus),seen=new Set([0]),queue=[0];
 for(let i=0;i<queue.length;i++)for(const {to,face} of domain.adjacency[queue[i]])if(chosen.has(to)){
  const count=face.filter(v=>types.get(v)==='M').length,nn=domain.species[queue[i]]==='neutron'&&domain.species[to]==='neutron';if(count!==(nn?1:2))return null;
  const apex=space.cells[to].find(v=>!face.includes(v)),t=count===1?'M':'C';if(types.has(apex)&&types.get(apex)!==t)return null;types.set(apex,t);if(!seen.has(to)){seen.add(to);queue.push(to);}
 }
 return seen.size===nucleus.length?types:null;
}
function* choose(ids,n,start=0,p=[]){if(!n){yield p;return;}for(let i=start;i<=ids.length-n;i++)yield* choose(ids,n-1,i+1,[...p,ids[i]]);}
export function enumerateProbe(space,{regularElectrons=false,allowEE=false,maxPrefixes=1000000}={}){
 const domain=domainOf(space),{adjacency,species}=domain,markings=[...choose(space.cells[0],2)];let prefixes=new Map([['0',[0]]]);const prefixCounts=[1];
 for(let size=1;size<14;size++){
  const next=new Map(),examined=new Set();for(const set of prefixes.values())for(const cell of set)for(const {to} of adjacency[cell])if(!set.includes(to)){
   const expanded=[...set,to].sort((a,b)=>a-b),k=key(expanded),p=expanded.filter(i=>species[i]==='proton').length;if(p>7||expanded.length-p>7||examined.has(k))continue;examined.add(k);
   if(!markings.some(ms=>color(space,domain,expanded,ms)))continue;
   const nn=expanded.reduce((sum,i)=>sum+adjacency[i].filter(e=>i<e.to&&expanded.includes(e.to)&&species[i]==='neutron'&&species[e.to]==='neutron').length,0);if(nn>3)continue;
   next.set(k,expanded);if(next.size>maxPrefixes)return {complete:false,stop:'prefix resource cap',prefixCounts};
  }
  prefixes=next;prefixCounts.push(prefixes.size);
 }
 const candidates=[];let typedNuclei=0,adjacencyRejected=0;const electronPools={};
 for(const nucleus of prefixes.values()){
  if(nucleus.some(i=>species[i]==='neutron'&&!adjacency[i].some(e=>nucleus.includes(e.to)&&species[e.to]==='proton')))continue;
  const nuclearEdges=nucleus.flatMap(i=>adjacency[i].filter(e=>i<e.to&&nucleus.includes(e.to)).map(e=>({from:i,to:e.to,face:e.face,kind:species[i]===species[e.to]?'NN':'PN'})));
  for(const ms of markings){
   const types=color(space,domain,nucleus,ms);if(!types)continue;typedNuclei++;
   const possible=new Map();for(const n of nucleus.filter(i=>species[i]==='neutron'))for(const edge of adjacency[n]){
    if(nucleus.includes(edge.to)||(!regularElectrons&&species[edge.to]!=='neutron')||edge.face.filter(v=>types.get(v)==='M').length!==1)continue;
    const apex=space.cells[edge.to].find(v=>!edge.face.includes(v));if(types.has(apex)&&types.get(apex)!=='M')continue;
    if(adjacency[edge.to].some(e=>nucleus.includes(e.to)&&(species[e.to]!=='neutron'||e.face.filter(v=>types.get(v)==='M').length!==1)))continue;
    possible.set(edge.to,apex);
   }
   const ids=[...possible.keys()].sort((a,b)=>a-b);electronPools[ids.length]=(electronPools[ids.length]??0)+1;
   for(const electrons of choose(ids,7)){
    const ee=electrons.flatMap(i=>adjacency[i].filter(e=>i<e.to&&electrons.includes(e.to)).map(e=>({from:i,to:e.to,face:e.face,kind:'EE'})));
    if(ee.length&&!allowEE){adjacencyRejected++;continue;}
    const allTypes=new Map(types);electrons.forEach(i=>allTypes.set(possible.get(i),'M'));
    const ne=electrons.flatMap(e=>adjacency[e].filter(x=>nucleus.includes(x.to)).map(x=>({from:x.to,to:e,face:x.face,kind:'NE'})));
    candidates.push({nucleus:[...nucleus],electrons,types:Object.fromEntries([...allTypes].sort(([a],[b])=>a-b)),interfaces:structuredClone([...nuclearEdges,...ne,...ee]),nuclearCycleRank:nuclearEdges.length-13});
   }
  }
 }
 candidates.sort((a,b)=>b.nuclearCycleRank-a.nuclearCycleRank||key([...a.nucleus,...a.electrons]).localeCompare(key([...b.nucleus,...b.electrons]))||JSON.stringify(a.types).localeCompare(JSON.stringify(b.types)));
 return {complete:true,prefixCounts,typedNuclei,electronPools,adjacencyRejected,candidates};
}
