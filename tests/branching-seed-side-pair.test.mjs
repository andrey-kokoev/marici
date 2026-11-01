import {test} from 'node:test';
import assert from 'node:assert/strict';
import * as T from 'three';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {createBranchingSeed} from '../examples/normal-ray/branching-seed-renderer.js';
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
test('eight detached pairs per layer use the actual sixteen height bands, not edge lengths',()=>{
 for(const gap of [0,2,6]){
  const model=buildBranchingSeed({seedLayerGap:gap});assert.equal(model.sidePairs.length,64);
  for(const pair of model.sidePairs){
   const layer=model.layers[pair.layerIndex],root=layer.nodes.find(n=>n.id===layer.root).point;
   assert.equal(pair.totalHeight,12);assert.equal(pair.bands.length,16);assert(pair.clearanceFromSimplex>.6);
   pair.bands.forEach((b,i)=>{
    assert.equal(b.role,i%2===0?'white':'exposed');assert.equal(b.end-b.start,i%2===0?1:.5);
    if(i)assert.equal(b.start,pair.bands[i-1].end);
    for(const id of b.sourceEdges){
     const edge=layer.edges.find(e=>e.id===id),levels=edge.points.map(p=>dot(p.map((x,j)=>x-root[j]),pair.direction)).sort((a,b)=>a-b);
     assert.deepEqual(levels,[b.start,b.end]);
    }
   });
   assert(Math.abs(pair.axis[0][1]-root[1])<1e-12);assert(Math.abs(pair.axis[0][2]-root[2])<1e-12);
   assert.equal(Math.abs(pair.axis[1][1]-pair.axis[0][1]),12);
   const ys=layer.nodes.map(n=>n.point[1]);assert.deepEqual(pair.axis.map(p=>p[1]).sort((a,b)=>a-b),[Math.min(...ys),Math.max(...ys)]);
  }
 }
});
test('blue and red remain two continuous planar guides through every sleeve',()=>{
 const model=buildBranchingSeed();
 for(const pair of model.sidePairs){
  assert.deepEqual(pair.conductors.map(c=>c.colour),['blue','red']);
  for(const conductor of pair.conductors){
   assert(conductor.points.every(p=>p[2]===pair.axis[0][2]));
   assert.equal(conductor.points[0][1],pair.axis[0][1]);assert.equal(conductor.points.at(-1)[1],pair.axis[1][1]);
   for(let i=1;i<conductor.points.length;i++)assert((conductor.points[i][1]-conductor.points[i-1][1])*pair.direction[1]>0);
  }
  for(const band of pair.bands.filter(b=>b.role==='exposed')){
   const blue=pair.conductors[0].points,atStart=blue.find(p=>Math.abs(dot(p.map((x,i)=>x-pair.axis[0][i]),pair.direction)-band.start)<1e-10),atEnd=blue.find(p=>Math.abs(dot(p.map((x,i)=>x-pair.axis[0][i]),pair.direction)-band.end)<1e-10);
   assert((atStart[0]-pair.axis[0][0])*(atEnd[0]-pair.axis[0][0])<0);
  }
 }
});
test('every exposed conductor follows its source colour direction relative to the sleeve arrow',()=>{
 const model=buildBranchingSeed();let checked=0;
 for(const pair of model.sidePairs){
  const index=pair.layerIndex;
  const right=[pair.direction[1],-pair.direction[0],0],edges=new Map(model.layers[index].edges.map(e=>[e.id,e]));
  const height=p=>dot(p.map((x,i)=>x-pair.axis[0][i]),pair.direction);
  for(const band of pair.bands.filter(b=>b.role==='exposed'))for(const conductor of pair.conductors){
   const points=conductor.points.filter(p=>height(p)>=band.start-1e-10&&height(p)<=band.end+1e-10);
   const displacement=points.at(-1).map((x,i)=>x-points[0][i]);
   const sources=band.sourceEdges.map(id=>edges.get(id)).filter(e=>e.role===conductor.colour);
   for(const e of sources){
    const source=e.points[1].map((x,i)=>x-e.points[0][i]);
    assert.equal(Math.sign(dot(displacement,right)),Math.sign(dot(source,right)),`layer ${index+1}, ${conductor.colour}, height ${band.start}`);
    assert(Math.abs(dot(displacement,pair.direction)-dot(source,pair.direction))<1e-10);
   }
   const sign=Math.sign(dot(displacement,right));
   for(let i=1;i<points.length;i++)assert(dot(points[i].map((x,j)=>x-points[i-1][j]),right)*sign>0);
   checked++;
  }
 }
 assert.equal(checked,1024);
});
test('side sleeves carry direction marks and follow existing layer visibility without a new toggle',()=>{
 const m=buildBranchingSeed(),group=createBranchingSeed(m,{seedVisibleLayers:[true,false,false,false,false,false,false,false]});
 try{
  const pairs=group.children.filter(o=>o.userData.seedSidePair);assert.equal(pairs.length,8);assert.equal(group.userData.audit.sidePairs,8);
  assert.equal(group.userData.audit.whiteArrows,36);
  assert.equal(pairs[0].children.filter(o=>o.userData.sidePairConductor).length,2);
  assert.equal(pairs[0].children.filter(o=>o.userData.sidePairSleeve).length,8);
  for(const arrow of pairs[0].children.filter(o=>o.userData.sidePairDirection)){
   const direction=new T.Vector3(...m.sidePairs[0].direction),facing=new T.Vector3(0,1,0).applyQuaternion(arrow.quaternion);assert(facing.dot(direction)>1-1e-12);
  }
 }finally{group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});}
});
test('seven translated copies preserve the first pair and are disjoint parallel pairs',()=>{
 const m=buildBranchingSeed();
 assert.equal(new Set(m.sidePairs.map(p=>p.id)).size,64);
 assert.equal(new Set(m.sidePairs.flatMap(p=>p.conductors.map(c=>c.id))).size,128);
 for(let layerIndex=0;layerIndex<8;layerIndex++){
  const pairs=m.sidePairs.filter(p=>p.layerIndex===layerIndex),first=pairs[0];assert.equal(pairs.length,8);
  assert(Math.abs(first.axis[0][0]-Math.max(...m.layers[layerIndex].nodes.map(n=>n.point[0]))-.8)<1e-12);
  for(const [i,p]of pairs.entries()){
   assert.deepEqual(p.direction,first.direction);
   for(let c=0;c<2;c++)for(let j=0;j<p.conductors[c].points.length;j++){
    const actual=p.conductors[c].points[j],base=first.conductors[c].points[j];
    assert(Math.abs(actual[0]-base[0]-.45*i)<1e-12);assert.deepEqual(actual.slice(1),base.slice(1));
   }
   if(i)assert(p.bounds[0][0]>pairs[i-1].bounds[1][0]);
  }
 }
});
test('camera bounds include the detached pairs while simplex graph counts remain unchanged',()=>{
 const m=buildBranchingSeed();assert.equal(m.edges.length,864);assert.equal(m.nodes.length,648);assert.equal(m.routes.length,2048);
 for(const pair of m.sidePairs)for(const p of pair.bounds)for(let i=0;i<3;i++)assert(p[i]>=Math.min(...m.envelope.map(v=>v[i]))&&p[i]<=Math.max(...m.envelope.map(v=>v[i])));
});
