// Whole-assembly search. No He-4 prefix or between-element addition order.
import {lattice,faces} from './simplex-model.mjs';
const copy=x=>structuredClone(x),key=a=>[...a].sort((x,y)=>x-y).join(',');
export const lithiumNNHypothesis='NN-MCC/reversed-edge/full-context-reference';
export function assemblyDomain(){
 const incidence=new Map(),adjacency=lattice.cells.map(()=>[]);
 lattice.cells.forEach((cell,id)=>faces.forEach(f=>{const face=f.map(i=>cell[i]),k=key(face);if(!incidence.has(k))incidence.set(k,{face,cells:[]});incidence.get(k).cells.push(id);}));
 for(const {face,cells} of incidence.values())if(cells.length===2){const [a,b]=cells;adjacency[a].push({to:b,face});adjacency[b].push({to:a,face});}else if(cells.length!==1)throw Error('Non-manifold search domain');
 const species=lattice.assembly.components.map(c=>c.primitive==='regular'?'proton':'neutron');
 return {adjacency,species};
}
function coloring(nucleus,rootM,domain){
 const types=new Map(lattice.cells[0].map(v=>[v,rootM.includes(v)?'M':'C'])),seen=new Set([0]),queue=[0],chosen=new Set(nucleus);
 for(let i=0;i<queue.length;i++)for(const {to,face} of domain.adjacency[queue[i]])if(chosen.has(to)){
  const count=face.filter(v=>types.get(v)==='M').length,nn=domain.species[queue[i]]==='neutron'&&domain.species[to]==='neutron';
  if(count!==(nn?1:2))return null;
  const apex=lattice.cells[to].find(v=>!face.includes(v)),type=count===1?'M':'C';
  if(types.has(apex)&&types.get(apex)!==type)return null;types.set(apex,type);
  if(!seen.has(to)){seen.add(to);queue.push(to);}
 }
 return seen.size===nucleus.length?types:null;
}
export function searchLithium6Assemblies(options={}){return searchLithiumAssemblies({...options,neutronCount:3});}
export function searchLithiumAssemblies({allowNN=false,neutronCount=3,pruneRoles=false}={}){
 if(![2,3,4,5].includes(neutronCount))throw RangeError('Supported lithium neutron counts: 2 through 5 (Li-5 through Li-8)');
 return searchTypedAssemblies({allowNN,neutronCount,protonCount:3,pruneRoles});
}
export function searchBeryllium9Assemblies(){return searchTypedAssemblies({allowNN:true,protonCount:4,neutronCount:5});}
export function searchBoronAssemblies({neutronCount=5,retained=null}={}){
 if(![5,6].includes(neutronCount))throw RangeError('Supported boron targets: B-10 and B-11');
 return searchTypedAssemblies({allowNN:true,protonCount:5,neutronCount,retained});
}
export function searchCarbonAssemblies({neutronCount=6,retained=null}={}){
 if(![6,7].includes(neutronCount))throw RangeError('Supported carbon targets: C-12 and C-13');
 return searchTypedAssemblies({allowNN:true,protonCount:6,neutronCount,retained});
}
export function searchNitrogenAssemblies({neutronCount=7,retained=null,pruneRoles=true}={}){
 if(![7,8].includes(neutronCount))throw RangeError('Supported nitrogen targets: N-14 and N-15');
 return searchTypedAssemblies({allowNN:true,protonCount:7,neutronCount,retained,pruneRoles});
}
function* combinations(ids,count,start=0,prefix=[]){
 if(!count){yield prefix;return;}
 for(let i=start;i<=ids.length-count;i++)yield* combinations(ids,count-1,i+1,[...prefix,ids[i]]);
}
function searchTypedAssemblies({allowNN,protonCount,neutronCount,retained=null,pruneRoles=false}){
 const nuclearCount=protonCount+neutronCount,electronCount=protonCount;
 const domain=assemblyDomain(),{adjacency,species}=domain,seed=retained?[...retained.nucleus].sort((a,b)=>a-b):[0];
 if(!seed.includes(0)||new Set(seed).size!==seed.length||seed.some(i=>!lattice.cells[i])||seed.filter(i=>species[i]==='proton').length>protonCount||seed.filter(i=>species[i]==='neutron').length>neutronCount)throw Error('Invalid retained nucleus');
 let prefixes=new Map([[key(seed),seed]]);
 const rootMarkings=[...combinations(lattice.cells[0],2)];
 const prefixCounts=[1];
 for(let size=seed.length;size<nuclearCount;size++){
  const next=new Map(),examined=new Set();for(const set of prefixes.values())for(const cell of set)for(const {to} of adjacency[cell])if(!set.includes(to)&&!retained?.electrons.includes(to)){
   const expanded=[...set,to].sort((a,b)=>a-b),p=expanded.filter(i=>species[i]==='proton').length;if(p>protonCount||expanded.length-p>neutronCount)continue;
   if(pruneRoles){const k=key(expanded);if(examined.has(k))continue;examined.add(k);
    // Any valid final coloring restricts to a valid coloring of this connected
    // prefix. Adding cells cannot repair a contradiction on its existing faces.
    if(!rootMarkings.some(ms=>coloring(expanded,ms,domain)))continue;
   }
   const nn=expanded.reduce((n,i)=>n+adjacency[i].filter(e=>i<e.to&&expanded.includes(e.to)&&species[i]==='neutron'&&species[e.to]==='neutron').length,0);
   // Each N supplies two MCC ports; each NN contact consumes two.
   // Reserve one port for each distinct terminal electron.
   if(nn>(allowNN?Math.floor((2*neutronCount-electronCount)/2):0))continue;next.set(key(expanded),expanded);
  }prefixes=next;prefixCounts.push(prefixes.size);
 }
 const candidates=[],electronPoolHistogram={};let typedNuclei=0,electronAdjacencyRejections=0;
 for(const nucleus of prefixes.values()){
  const nuclearEdges=nucleus.flatMap(i=>adjacency[i].filter(e=>i<e.to&&nucleus.includes(e.to)).map(e=>({from:i,to:e.to,face:e.face,kind:species[i]===species[e.to]?'NN':'PN'})));
  if(nucleus.some(i=>species[i]==='neutron'&&!adjacency[i].some(e=>nucleus.includes(e.to)&&species[e.to]==='proton')))continue;
  for(let a=0;a<4;a++)for(let b=a+1;b<4;b++){
   const types=coloring(nucleus,[lattice.cells[0][a],lattice.cells[0][b]],domain);if(!types)continue;typedNuclei++;
   const possible=new Map();for(const n of nucleus.filter(i=>species[i]==='neutron'))for(const edge of adjacency[n]){
    if(nucleus.includes(edge.to)||species[edge.to]!=='neutron'||edge.face.filter(v=>types.get(v)==='M').length!==1)continue;
    const apex=lattice.cells[edge.to].find(v=>!edge.face.includes(v));if(types.has(apex)&&types.get(apex)!=='M')continue;
    if(adjacency[edge.to].some(e=>nucleus.includes(e.to)&&(species[e.to]!=='neutron'||e.face.filter(v=>types.get(v)==='M').length!==1)))continue;
    possible.set(edge.to,apex);
   }
   const ids=[...possible.keys()].sort((a,b)=>a-b);electronPoolHistogram[ids.length]=(electronPoolHistogram[ids.length]??0)+1;
   for(const electrons of combinations(ids,electronCount)){
    if(electrons.some(i=>adjacency[i].some(e=>electrons.includes(e.to)))){electronAdjacencyRejections++;continue;}
    const allTypes=new Map(types);electrons.forEach(i=>allTypes.set(possible.get(i),'M'));
    if(retained&&(!retained.electrons.every(i=>electrons.includes(i))||Object.entries(retained.types).some(([v,t])=>allTypes.get(Number(v))!==t)))continue;
    const ne=electrons.flatMap(e=>adjacency[e].filter(x=>nucleus.includes(x.to)).map(x=>({from:x.to,to:e,face:x.face,kind:'NE'})));
    candidates.push({nucleus:[...nucleus],electrons,types:Object.fromEntries([...allTypes].sort(([a],[b])=>a-b)),interfaces:copy([...nuclearEdges,...ne]),nuclearCycleRank:nuclearEdges.length-(nuclearCount-1)});
   }
  }
 }
 candidates.sort((a,b)=>b.nuclearCycleRank-a.nuclearCycleRank||key([...a.nucleus,...a.electrons]).localeCompare(key([...b.nucleus,...b.electrons]))||JSON.stringify(a.types).localeCompare(JSON.stringify(b.types)));
 return {status:candidates.length?'whole-assembly-geometry-candidates':'no-candidate-in-bounded-domain',allowNN,protonCount,neutronCount,electronCount,primitiveCells:lattice.cells.length,anchorProton:0,earlyRolePruning:pruneRoles,prefixStartSize:seed.length,retainedNucleus:retained?[...seed]:null,prefixCounts,typedNuclei,electronPoolHistogram,electronAdjacencyRejections,candidates,
  scope:`Connected ${nuclearCount}-cell nuclei containing proton cell 0 in the existing 343-cell domain, ${protonCount} regular P and ${neutronCount} split N, globally consistent MMCC typing, PN on MCM, optional NN on MCC, ${electronCount} distinct nonadjacent terminal split-cell electrons on MCC. Every N has a native P reference.${retained?' Search restricted to extensions retaining the supplied nucleus, electrons and roles.':''} This is a bounded ansatz, not all nuclear geometries; search prefixes are an enumeration device, not physical construction steps.`};
}
