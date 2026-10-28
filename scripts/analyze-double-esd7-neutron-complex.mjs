import fs from 'node:fs/promises';
import assert from 'node:assert/strict';
import {doubleEsd7RuleProcess,doubleEsd7Rules} from '../research/realization-tower/double-esd7-process.mjs';
import {cellDualGraph} from '../research/realization-tower/cell-dual-graph.mjs';
const proc=doubleEsd7RuleProcess(7,doubleEsd7Rules.map(r=>r.id));
const bodies=proc.retainedBodies,byId=new Map(bodies.map(b=>[b.id,b])),graph=cellDualGraph(bodies);
const adjacent=new Map(bodies.map(b=>[b.id,[]]));
for(const e of graph.links){adjacent.get(e.from).push(e.to);adjacent.get(e.to).push(e.from);}
const counts=ids=>{const result={P:0,N:0,E:0,tetrahedra:0,octahedra:0,total:ids.length};for(const id of ids){const b=byId.get(id);result[{proton:'P',neutron:'N',electron:'E'}[b.role]]++;result[b.kind==='tetrahedron'?'tetrahedra':'octahedra']++;}return result;};
function distances(seeds){const d=new Map(seeds.map(id=>[id,0])),queue=[...seeds];for(let i=0;i<queue.length;i++)for(const id of adjacent.get(queue[i]))if(!d.has(id)){d.set(id,d.get(queue[i])+1);queue.push(id);}return d;}
const plus=bodies.filter(b=>b.seedLabel==='+N'&&b.layer===0).map(b=>b.id),minus=bodies.filter(b=>b.seedLabel==='−N'&&b.layer===0).map(b=>b.id);
const dp=distances(plus),dm=distances(minus),distance=Math.min(...minus.map(id=>dp.get(id))),ids=bodies.map(b=>b.id);
const shortest=ids.filter(id=>dp.get(id)+dm.get(id)===distance),radius=Math.ceil(distance/2);
const overlap=ids.filter(id=>dp.get(id)<=radius&&dm.get(id)<=radius);
const layers=Array.from({length:distance+1},(_,depth)=>({depth,counts:counts(shortest.filter(id=>dp.get(id)===depth))}));
const shells=Array.from({length:radius+1},(_,depth)=>({radius:depth,plusShell:counts(ids.filter(id=>dp.get(id)===depth)),minusShell:counts(ids.filter(id=>dm.get(id)===depth)),overlap:counts(ids.filter(id=>dp.get(id)<=depth&&dm.get(id)<=depth))}));
const octahedra=shortest.filter(id=>byId.get(id).kind==='octahedron').map(id=>({id,role:byId.get(id).role,depth:dp.get(id),neighbors:counts(adjacent.get(id))}));
const signatures=new Map();for(const o of octahedra){const k=`${o.neighbors.P}P ${o.neighbors.N}N ${o.neighbors.E}E`;signatures.set(k,(signatures.get(k)??0)+1);}
let triangles=0;const sets=new Map([...adjacent].map(([id,ns])=>[id,new Set(ns)]));for(const e of graph.links)for(const n of adjacent.get(e.from))if(sets.get(e.to).has(n))triangles++;triangles/=3;
assert.equal(plus.length,2);assert.equal(minus.length,2);
assert.equal(dp.size,bodies.length);assert.equal(dm.size,bodies.length);
assert.ok(shells.slice(0,-1).every(s=>s.overlap.total===0));
assert.deepEqual(counts(overlap),{P:2,N:2,E:0,tetrahedra:4,octahedra:0,total:4});
assert.equal(triangles,0);
const report={metric:'Shared-facet graph distance; counts are geometric cell counts, not a new particle interpretation. Seam-adjacent cells remain distinct; no assignments are changed.',seeds:{plus,minus},all:counts(ids),distance,firstOverlapRadius:radius,firstOverlap:{ids:overlap,counts:counts(overlap)},shortestPathUnion:{counts:counts(shortest),ids:shortest,layers},growth:shells,octahedronNeighbourSignatures:Object.fromEntries(signatures),octahedra,graphTriangleCount:triangles};
await fs.mkdir('research/strominger/results',{recursive:true});
await fs.writeFile('research/strominger/results/double-esd7-neutron-complex.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,octahedra:undefined,shortestPathUnion:{counts:report.shortestPathUnion.counts,layers},firstOverlap:report.firstOverlap},null,2));
