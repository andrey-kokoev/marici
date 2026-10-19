// Independent bounded search with independently specified P, N, E counts.
import {probeSpace,domainOf} from './n14-probe-model.mjs';
export const space=probeSpace(),domain=domainOf(space);
const {adjacency,species}=domain,key=a=>[...a].sort((a,b)=>a-b).join(',');
function* choose(ids,n,start=0,p=[]){if(!n){yield p;return;}for(let i=start;i<=ids.length-n;i++)yield* choose(ids,n-1,i+1,[...p,ids[i]]);}
const markings=[...choose(space.cells[0],2)];
function color(nucleus,ms){
 const types=new Map(space.cells[0].map(v=>[v,ms.includes(v)?'M':'C'])),chosen=new Set(nucleus),seen=new Set([0]),queue=[0];
 for(let i=0;i<queue.length;i++)for(const {to,face} of adjacency[queue[i]])if(chosen.has(to)){
  const count=face.filter(v=>types.get(v)==='M').length,nn=species[queue[i]]==='neutron'&&species[to]==='neutron';if(count!==(nn?1:2))return null;
  const apex=space.cells[to].find(v=>!face.includes(v)),t=count===1?'M':'C';if(types.has(apex)&&types.get(apex)!==t)return null;types.set(apex,t);if(!seen.has(to)){seen.add(to);queue.push(to);}
 }
 return seen.size===nucleus.length?types:null;
}
export function searchCounts(protonCount,neutronCount,electronCount){
 for(const n of [protonCount,neutronCount,electronCount])if(!Number.isInteger(n)||n<0)throw Error('Nonnegative integer counts required');
 const size=protonCount+neutronCount,maxNN=Math.floor((2*neutronCount-electronCount)/2);let prefixes=new Map([['0',[0]]]);const prefixCounts=[1];
 for(let s=1;s<size;s++){
  const next=new Map(),examined=new Set();for(const set of prefixes.values())for(const i of set)for(const {to} of adjacency[i])if(!set.includes(to)){
   const expanded=[...set,to].sort((a,b)=>a-b),k=key(expanded),p=expanded.filter(i=>species[i]==='proton').length;if(p>protonCount||expanded.length-p>neutronCount||examined.has(k))continue;examined.add(k);
   if(!markings.some(ms=>color(expanded,ms)))continue;
   const nn=expanded.reduce((sum,i)=>sum+adjacency[i].filter(e=>i<e.to&&expanded.includes(e.to)&&species[i]==='neutron'&&species[e.to]==='neutron').length,0);if(nn>maxNN)continue;next.set(k,expanded);
  }prefixes=next;prefixCounts.push(prefixes.size);
 }
 const candidates=[],electronPools={};let typedNuclei=0,adjacencyRejected=0;
 for(const nucleus of prefixes.values()){
  if(nucleus.some(i=>species[i]==='neutron'&&!adjacency[i].some(e=>nucleus.includes(e.to)&&species[e.to]==='proton')))continue;
  const nuclearEdges=nucleus.flatMap(i=>adjacency[i].filter(e=>i<e.to&&nucleus.includes(e.to)).map(e=>({from:i,to:e.to,face:e.face,kind:species[i]===species[e.to]?'NN':'PN'})));
  for(const ms of markings){const types=color(nucleus,ms);if(!types)continue;typedNuclei++;const possible=new Map();
   for(const n of nucleus.filter(i=>species[i]==='neutron'))for(const edge of adjacency[n]){
    if(nucleus.includes(edge.to)||species[edge.to]!=='neutron'||edge.face.filter(v=>types.get(v)==='M').length!==1)continue;
    const apex=space.cells[edge.to].find(v=>!edge.face.includes(v));if(types.has(apex)&&types.get(apex)!=='M')continue;
    if(adjacency[edge.to].some(e=>nucleus.includes(e.to)&&(species[e.to]!=='neutron'||e.face.filter(v=>types.get(v)==='M').length!==1)))continue;possible.set(edge.to,apex);
   }
   const ids=[...possible.keys()].sort((a,b)=>a-b);electronPools[ids.length]=(electronPools[ids.length]??0)+1;
   for(const electrons of choose(ids,electronCount)){
    if(electrons.some(i=>adjacency[i].some(e=>electrons.includes(e.to)))){adjacencyRejected++;continue;}
    const allTypes=new Map(types);electrons.forEach(i=>allTypes.set(possible.get(i),'M'));
    const ne=electrons.flatMap(e=>adjacency[e].filter(x=>nucleus.includes(x.to)).map(x=>({from:x.to,to:e,face:x.face,kind:'NE'})));
    candidates.push({nucleus:[...nucleus],electrons,types:Object.fromEntries([...allTypes].sort(([a],[b])=>a-b)),interfaces:structuredClone([...nuclearEdges,...ne]),nuclearCycleRank:nuclearEdges.length-size+1});
   }
  }
 }
 candidates.sort((a,b)=>b.nuclearCycleRank-a.nuclearCycleRank||key([...a.nucleus,...a.electrons]).localeCompare(key([...b.nucleus,...b.electrons]))||JSON.stringify(a.types).localeCompare(JSON.stringify(b.types)));
 return {protonCount,neutronCount,electronCount,geometryComplete:true,prefixCounts,typedNuclei,electronPools,adjacencyRejected,candidates};
}
