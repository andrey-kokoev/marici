import test from 'node:test';
import assert from 'node:assert/strict';
import * as T from 'three';
import {buildSulfurTubeNetwork} from '../research/realization-tower/sulfur-32-tube-network.mjs';
import {buildSulfurIncomingBundle} from '../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {createHoneycombTubeGeometry} from '../examples/normal-ray/honeycomb-tube-geometry.js';
const model=(edges,strands)=>({edges:edges.map(([id,a,b,ids])=>({id,guide:[a,b],strandIds:ids,carrierCells:['N']})),strands,channelGroups:[{id:'N-group',members:['N']}]});
const a=[-1,0,0],b=[0,0,0],c=[0,1,0],d=[0,-1,0],e=[1,0,0];
test('same-bundle bends are continuous and independent crossings do not merge',()=>{
 const m=model([['a',a,b,['x']],['b',b,c,['x']],['c',d,b,['y']],['d',b,e,['y']]],[{id:'x',edgeIds:['a','b']},{id:'y',edgeIds:['c','d']}]);
 const network=buildSulfurTubeNetwork(m);assert.equal(network.segments.length,2);assert.equal(network.audit.internalJoins,2);assert.equal(network.junctions.length,0);
 assert(network.segments.every(s=>s.edgeIds.length===2&&s.points.length===3));
 assert.deepEqual(buildSulfurTubeNetwork({...m,edges:[...m.edges].reverse().map(e=>({...e,guide:[...e.guide].reverse()}))}),network);
});
test('splits and changes in strand membership remain genuine boundaries',()=>{
 const m=model([['a',a,b,['x','y']],['b',b,c,['x']],['c',b,e,['y']]],[{id:'x',edgeIds:['a','b']},{id:'y',edgeIds:['a','c']}]);
 const network=buildSulfurTubeNetwork(m);assert.equal(network.segments.length,3);
 assert.equal(network.junctions.length,1);assert.equal(network.junctions[0].ports.length,3);
});
test('closed continuations retain every edge exactly once',()=>{
 const vs=[[0,0,0],[1,0,0],[1,1,0],[0,1,0]];
 const m=model(vs.map((p,i)=>[String(i),p,vs[(i+1)%4],['x']]),[{id:'x',edgeIds:['0','1','2','3'],closed:true}]);
 const result=buildSulfurTubeNetwork(m);assert.equal(result.segments.length,1);assert(result.segments[0].closed);assert.equal(result.segments[0].edgeIds.length,4);
});
test('sixteen N identities are mapped by native provenance, not forced into a partition',()=>{
 const model=buildSulfurIncomingBundle(),network=buildSulfurTubeNetwork(model);
 assert.equal(network.identities.length,16);assert.equal(new Set(network.identities.map(g=>g.label)).size,16);
 assert.equal(network.identities.filter(g=>g.members.length===2).length,3);
 for(const identity of network.identities){
  const source=model.channelGroups.find(g=>g.id===identity.id);assert.deepEqual(identity.members,source.members);assert.equal(identity.label,source.label);
  assert.equal(identity.components.length,identity.members.length);
  assert.deepEqual(identity.components.flat().sort(),[...identity.edgeIds].sort());
  assert.deepEqual(identity.edgeIds,model.edges.filter(e=>e.carrierCells.some(c=>identity.members.includes(c))).map(e=>e.id).sort((a,b)=>a.localeCompare(b)));
  assert.deepEqual(identity.segmentIds,network.segments.filter(s=>s.nGroups.includes(identity.id)).map(s=>s.id));
 }
 assert.equal(new Set(network.identities.flatMap(g=>g.segmentIds)).size,59);
 assert.equal(network.segments.filter(s=>s.nGroups.length===2).length,11);
});
const boundaryCount=geometry=>{
 const counts=new Map(),ix=geometry.index.array;
 for(let i=0;i<ix.length;i+=3)for(const [a,b] of [[ix[i],ix[i+1]],[ix[i+1],ix[i+2]],[ix[i+2],ix[i]]]){const key=[a,b].sort((x,y)=>x-y).join(',');counts.set(key,(counts.get(key)??0)+1);}
 assert([...counts.values()].every(n=>n===1||n===2));return [...counts.values()].filter(n=>n===1).length;
};
test('miter sweep welds bend rings, keeps the native centreline and has no internal rim',()=>{
 const points=[a,b,c].map(p=>new T.Vector3(...p)),{geometry,rings}=createHoneycombTubeGeometry(points,.1);
 assert.equal(boundaryCount(geometry),48);
 for(let i=0;i<rings.length;i++)assert(rings[i].reduce((sum,p)=>sum.add(p),new T.Vector3()).divideScalar(24).distanceTo(points[i])<1e-9);
 for(const p of geometry.attributes.position.array)assert(Number.isFinite(p));geometry.dispose();
 const loop=[[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,0]].map(p=>new T.Vector3(...p));
 const closed=createHoneycombTubeGeometry(loop,.1,{closed:true});assert.equal(boundaryCount(closed.geometry),0);closed.geometry.dispose();
});
