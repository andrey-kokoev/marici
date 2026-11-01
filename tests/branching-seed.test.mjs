import {test} from 'node:test';
import * as T from 'three';
import {createBranchingSeed} from '../examples/normal-ray/branching-seed-renderer.js';
import assert from 'node:assert/strict';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('white-rooted depth eight is the merged planar honeycomb, not a duplicated binary tree',()=>{
 const full=buildBranchingSeed(),m=full.layers[0];assert.equal(full.audit.depth,8);assert.equal(full.audit.edgeLayers,16);
 assert.equal(m.nodes.length,81);assert.equal(m.edges.length,108);assert.equal(m.routes.length,256);assert.equal(new Set(m.routes.map(r=>r.output)).size,9);
 assert(m.nodes.every(n=>n.point[2]===0));assert.equal(new Set(m.nodes.map(n=>n.lattice.join(','))).size,81);
 assert.equal(new Set(m.edges.map(e=>e.id)).size,108);
 const rootEdges=m.edges.filter(e=>e.from===m.root||e.to===m.root);assert.equal(rootEdges.length,1);assert.equal(rootEdges[0].role,'white');
 for(const role of ['white','red','blue'])assert.equal(m.edges.filter(e=>e.role===role).length,36);
 for(const route of m.routes){
  const edges=route.edges.map(id=>m.edges.find(e=>e.id===id));assert.equal(edges.length,16);assert.equal(edges[0].from,m.root);
  edges.forEach((e,i)=>{assert(i%2===0?e.role==='white':e.role==='red'||e.role==='blue');if(i)assert.equal(edges[i-1].to,e.from);});
 }
});
test('edge colours follow the three specified directions and complete stars have 120-degree arms',()=>{
 const m=buildBranchingSeed(),angles={white:0,blue:120,red:240};
 for(const e of m.edges){
  const d=e.points[1].map((x,i)=>x-e.points[0][i]),angle=angles[e.role]*Math.PI/180,axis=[Math.sin(angle),Math.cos(angle)*(e.id.includes('mirror:')?-1:1),0];
  assert(Math.abs(Math.hypot(...d)-1)<1e-12);assert(Math.abs(Math.abs(d.reduce((s,x,i)=>s+x*axis[i],0))-1)<1e-12);
 }
 for(const n of m.nodes){
  const edges=m.edges.filter(e=>e.from===n.id||e.to===n.id);assert(edges.length<=3);
  if(edges.length!==3)continue;
  assert.equal(new Set(edges.map(e=>e.role)).size,3);
  const arms=edges.map(e=>(e.from===n.id?e.points[1]:e.points[0]).map((x,i)=>x-n.point[i]));
  for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)assert(Math.abs(arms[i].reduce((s,x,k)=>s+x*arms[j][k],0)+.5)<1e-12);
 }
});
test('every white segment has one midpoint arrow pointing away from the root',()=>{
 const m=buildBranchingSeed(),group=createBranchingSeed(m);
 try{
  const arrows=group.children.filter(o=>o.userData.whiteDirection);
  assert.equal(arrows.length,288);assert.equal(group.userData.audit.whiteArrows,288);
  assert.equal(new Set(arrows.map(a=>a.userData.whiteDirection.edge)).size,288);
  for(const arrow of arrows){
   const e=m.edges.find(e=>e.id===arrow.userData.whiteDirection.edge);
   assert.equal(e.role,'white');assert.equal(arrow.userData.whiteDirection.from,e.from);assert.equal(arrow.userData.whiteDirection.to,e.to);
   const a=new T.Vector3(...e.points[0]),b=new T.Vector3(...e.points[1]);
   assert(arrow.position.distanceTo(a.clone().add(b).multiplyScalar(.5))<1e-12);
   const facing=new T.Vector3(0,1,0).applyQuaternion(arrow.quaternion);
   assert(facing.dot(b.sub(a).normalize())>1-1e-12);
  }
 }finally{group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});}
});
test('lower clone is exactly a point reflection, with reversed directed edges and no added joins',()=>{
 for(const gap of [0,2,6]){
  const m=buildBranchingSeed({seedLayerGap:gap}),[original,clone]=m.layers;
  assert.equal(m.nodes.length,648);assert.equal(m.edges.length,864);assert.equal(m.routes.length,2048);
  assert.equal(new Set(m.nodes.map(n=>n.id)).size,648);
  for(const n of clone.nodes){
   const source=original.nodes.find(s=>s.id===n.source);
   assert.deepEqual(n.point,m.reflect(source.point));assert.equal(n.point[2],-gap);
   assert(m.reflect(n.point).every((x,i)=>Math.abs(x-source.point[i])<1e-12));
  }
  for(const e of clone.edges){
   const source=original.edges.find(s=>s.id===e.source);
   assert.equal(e.role,source.role);assert.equal(e.from,'clone:'+source.from);assert.equal(e.to,'clone:'+source.to);
   for(let i=0;i<3;i++)assert(Math.abs(e.points[1][i]-e.points[0][i]+source.points[1][i]-source.points[0][i])<1e-12);
  }
  for(const r of clone.routes){const source=original.routes.find(s=>s.id===r.source);assert.deepEqual(r.edges,source.edges.map(id=>'clone:'+id));}
 }
});
test('layers 3–4 mirror the pair perpendicular to the central white arrow, preserving colours and routes',()=>{
 for(const gap of [0,2,6]){
  const m=buildBranchingSeed({seedLayerGap:gap});assert.equal(m.layers.length,8);
  assert.deepEqual(m.audit.pairReflectionNormal,[0,-1,0]);assert.deepEqual(m.audit.pairReflectionPoint,[0,-6.5,0]);
  for(let i=0;i<2;i++){
   const original=m.layers[i],copy=m.layers[i+2];assert.equal(copy.source,original.id);
   assert.equal(copy.nodes.length,original.nodes.length);assert.equal(copy.edges.length,original.edges.length);assert.equal(copy.routes.length,original.routes.length);
   for(const n of copy.nodes){
    const source=original.nodes.find(s=>s.id===n.source);
    assert.deepEqual(n.point,m.reflectLower(source.point));
    assert(n.point.every((x,j)=>Math.abs(x-[source.point[0],-13-source.point[1],source.point[2]-2*gap][j])<1e-12));
   }
   for(const e of copy.edges){const source=original.edges.find(s=>s.id===e.source);assert.equal(e.role,source.role);assert.equal(e.from,'mirror:'+source.from);assert.equal(e.to,'mirror:'+source.to);assert.deepEqual(e.points,source.points.map(m.reflectLower));}
   for(const r of copy.routes){const source=original.routes.find(s=>s.id===r.source);assert.deepEqual(r.edges,source.edges.map(id=>'mirror:'+id));}
  }
  // Points on the mirror plane retain XY; the two central-edge ends exchange.
  assert.deepEqual(m.reflectLower([1,-6.5,0]).slice(0,2),[1,-6.5]);
  assert.deepEqual(m.reflectLower([0,-6,0]).slice(0,2),[0,-7]);
  const p=[1,-5,0],twice=m.reflectLower(m.reflectLower(p));
  assert.deepEqual(twice.slice(0,2),p.slice(0,2));assert(Math.abs(twice[2]+4*gap)<1e-12);
 }
});
test('layers 5–8 copy every source layer lower and invert XY in their own planes',()=>{
 for(const gap of [0,2,6]){
  const m=buildBranchingSeed({seedLayerGap:gap});
  for(let i=0;i<4;i++){
   const source=m.layers[i],copy=m.layers[i+4];assert.equal(copy.source,source.id);
   assert.equal(copy.nodes.length,source.nodes.length);assert.equal(copy.edges.length,source.edges.length);assert.equal(copy.routes.length,source.routes.length);
   const center=[m.reflectionCenter[0],m.reflectionCenter[1],copy.nodes[0].point[2]];
   for(const n of copy.nodes){
    const p=source.nodes.find(s=>s.id===n.source).point;
    const dropped=[p[0],p[1],p[2]-4*gap];
    assert(n.point.every((x,j)=>Math.abs(x-(2*center[j]-dropped[j]))<1e-12));
    assert.deepEqual(n.point,m.reflectBlockLower(p));
   }
   for(const e of copy.edges){const original=source.edges.find(s=>s.id===e.source);assert.equal(e.role,original.role);assert.equal(e.from,'central:'+original.from);assert.equal(e.to,'central:'+original.to);assert.deepEqual(e.points,original.points.map(m.reflectBlockLower));}
   for(const r of copy.routes){const original=source.routes.find(s=>s.id===r.source);assert.deepEqual(r.edges,original.edges.map(id=>'central:'+id));}
   assert(m.centerMarkers.some(marker=>marker.layers.includes(i+4)&&marker.point.every((x,j)=>Math.abs(x-center[j])<1e-12)));
  }
  assert(m.audit.layerPlanes.every((z,i)=>Math.abs(z+i*gap)<1e-12));
 }
});
test('reflection center is the white-edge midpoint below the central vertex, not the vertex',()=>{
 const m=buildBranchingSeed(),edge=m.layers[0].edges.find(e=>e.id===m.audit.reflectionCenterEdge);
 assert.equal(edge.role,'white');assert.deepEqual(edge.points,[[0,-6,0],[0,-7,0]]);
 assert.deepEqual(m.reflectionCenter,[0,-6.5,-1]);
 for(const p of edge.points)assert(m.reflect(p).slice(0,2).every((x,i)=>x===edge.points.find(q=>q!==p)[i]));
 assert(!m.layers[0].nodes.some(n=>n.point[0]===m.reflectionCenter[0]&&n.point[1]===m.reflectionCenter[1]));
});
test('layer buttons filter geometry and arrows without changing the construction',()=>{
 const m=buildBranchingSeed(),before=JSON.stringify(m.nodes);
 for(const visible of [[true,false,false,false,false,false,false,false],[false,true,false,true,false,true,false,true],Array(8).fill(false)]){
  const group=createBranchingSeed(m,{seedVisibleLayers:visible});
  try{
   const count=visible.filter(Boolean).length;
   assert.deepEqual(group.userData.audit.visibleLayers,visible.flatMap((on,i)=>on?[i+1]:[]));
   assert.equal(group.children.filter(o=>o.userData.seedEdge).length,count*108);
   assert.equal(group.userData.audit.whiteArrows,count*36);
   if(!count)assert.equal(group.children.length,0);
  }finally{group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});}
 }
 assert.equal(JSON.stringify(m.nodes),before);
 assert.deepEqual(normalizeSceneSettings({appearance:{seedVisibleLayers:[false,true,false,true]}}).appearance.seedVisibleLayers,[false,true,false,true,true,true,true,true]);
});
test('view selection persists and obsolete twist controls are removed',()=>{
 const a=normalizeSceneSettings({appearance:{sulfurBranchSeed:true,seedLayerGap:3.5,seedPlaneAngle:90,seedShowPlanes:true}}).appearance;
 assert.equal(a.seedLayerGap,3.5);assert.equal(a.sulfurBranchSeed,true);assert.equal(a.seedPlaneAngle,undefined);assert.equal(a.seedShowPlanes,undefined);
});
