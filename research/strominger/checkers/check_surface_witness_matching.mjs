import assert from 'node:assert/strict';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {lattice,faces} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
// User layers 3/4 correspond to zero-based construction layers 2/3.
const inner=lattice.assembly.layers[2].items,outer=lattice.assembly.layers[3].items;
assert.equal(inner.length,44);assert.equal(outer.length,126);
const innerIds=new Set(inner.map(i=>i.id)),outerIds=new Set(outer.map(i=>i.id));
const owner=new Map(lattice.assembly.items.flatMap(item=>item.children.map(id=>[id,item.id])));
const incidence=new Map();
lattice.cells.forEach((cell,id)=>{
 for(const face of faces){const vertices=face.map(i=>cell[i]).sort((a,b)=>a-b),key=vertices.join(',');
  if(!incidence.has(key))incidence.set(key,{vertices,owners:[]});incidence.get(key).owners.push(owner.get(id));}
});
const adjacency=new Map(inner.map(i=>[i.id,new Set()])),sharedFaces=new Map();
for(const {vertices,owners} of incidence.values()){
 assert.ok(owners.length===1||owners.length===2);
 if(owners.length!==2||owners[0]===owners[1])continue;
 for(const [a,b] of [owners,[owners[1],owners[0]]])if(innerIds.has(a)&&outerIds.has(b)){
  adjacency.get(a).add(b);const key=a+'|'+b;
  if(!sharedFaces.has(key))sharedFaces.set(key,[]);
  sharedFaces.get(key).push(vertices.map(id=>lattice.nodes[id].address));
 }
}
const neighbors=new Map([...adjacency].map(([id,set])=>[id,[...set].sort()]));
const matchedOuter=new Map();
function augment(a,visited){
 for(const b of neighbors.get(a)){
  if(visited.has(b))continue;visited.add(b);
  if(!matchedOuter.has(b)||augment(matchedOuter.get(b),visited)){matchedOuter.set(b,a);return true;}
 }
 return false;
}
for(const item of inner)augment(item.id,new Set());
const matchedInner=new Map([...matchedOuter].map(([b,a])=>[a,b]));
const unmatched=inner.filter(i=>!matchedInner.has(i.id)).map(i=>i.id);
const matching=inner.filter(i=>matchedInner.has(i.id)).map(i=>({inner:i.id,outer:matchedInner.get(i.id),sharedFaces:sharedFaces.get(i.id+'|'+matchedInner.get(i.id))}));
assert.equal(new Set(matching.map(m=>m.inner)).size,matching.length);
assert.equal(new Set(matching.map(m=>m.outer)).size,matching.length);
for(const m of matching)assert.ok(m.sharedFaces?.length&&neighbors.get(m.inner).includes(m.outer));
// Alternating reachability gives a Hall-deficiency certificate if saturation fails.
const reachableInner=new Set(unmatched),reachableOuter=new Set(),queue=[...unmatched];
for(let i=0;i<queue.length;i++)for(const b of neighbors.get(queue[i])){
 reachableOuter.add(b);
 const a=matchedOuter.get(b);if(a!==undefined&&!reachableInner.has(a)){reachableInner.add(a);queue.push(a);}
}
let obstruction=null;
if(unmatched.length){
 assert.ok(reachableOuter.size<reachableInner.size);
 obstruction={innerSubset:[...reachableInner],outerNeighborhood:[...reachableOuter],innerCount:reachableInner.size,neighborCount:reachableOuter.size,deficit:reachableInner.size-reachableOuter.size};
 assert.equal(obstruction.deficit,44-matching.length);
}
// Independent unit-capacity max flow verifies the matching cardinality.
const count=2+inner.length+outer.length,source=count-2,sink=count-1;
const capacity=Array.from({length:count},()=>new Int16Array(count));
const innerIndex=new Map(inner.map((x,i)=>[x.id,i])),outerIndex=new Map(outer.map((x,i)=>[x.id,inner.length+i]));
for(const a of inner){const ai=innerIndex.get(a.id);capacity[source][ai]=1;for(const b of neighbors.get(a.id))capacity[ai][outerIndex.get(b)]=1;}
for(const b of outer)capacity[outerIndex.get(b.id)][sink]=1;
let flow=0;
while(true){
 const parent=Array(count).fill(-1),q=[source];parent[source]=source;
 for(let i=0;i<q.length&&parent[sink]<0;i++)for(let j=0;j<count;j++)if(parent[j]<0&&capacity[q[i]][j]>0){parent[j]=q[i];q.push(j);}
 if(parent[sink]<0)break;
 for(let v=sink;v!==source;v=parent[v]){capacity[parent[v]][v]--;capacity[v][parent[v]]++;}flow++;
}
assert.equal(flow,matching.length);
const eligibleOuter=new Set([...neighbors.values()].flat());
const histogram={};for(const ns of neighbors.values())histogram[ns.length]=(histogram[ns.length]||0)+1;
const files=['research/strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs','research/strominger/demos/particle-overlap-tetrahedron/simplex-model.mjs'];
const hashes=Object.fromEntries(await Promise.all(files.map(async f=>[f,createHash('sha256').update(await readFile(path.join(root,f))).digest('hex')])));
const result={schema:'marici.surface-witness-matching.v1',relation:'Shared triangular face between assembled items; one unit of capacity per outer item',
 layers:{inner:{constructionIndex:2,count:44},outer:{constructionIndex:3,count:126}},
 innerDegreeHistogram:histogram,eligibleOuterCount:eligibleOuter.size,maximumMatching:matching.length,independentMaxFlow:flow,
 fullWitnessAssignment:matching.length===44,unmatchedInner:unmatched,hallObstruction:obstruction,
 unusedOuterCount:126-matching.length,unusedOuter:outer.filter(i=>!matchedOuter.has(i.id)).map(i=>i.id),
 matching,adjacency:Object.fromEntries(neighbors),sourceHashes:hashes,
 interpretation:matching.length===44?'The proposed one-distinct-face-neighbor witness rule is feasible; 82 outer items remain unused by this assignment. No physical proton/neutron identification or unique assignment is proved.':'The proposed one-distinct-face-neighbor witness rule fails; subtracting 44 from 126 is not supported by this incidence relation.'};
const out=path.join(root,'research/strominger/results/surface-witness-matching');await mkdir(out,{recursive:true});
await writeFile(path.join(out,'verification.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({fullWitnessAssignment:result.fullWitnessAssignment,maximumMatching:matching.length,eligibleOuterCount:eligibleOuter.size,innerDegreeHistogram:histogram,unusedOuterCount:result.unusedOuterCount,hallObstruction:obstruction},null,2));
