import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('single seed has 120-degree white/red–white/blue opening, preserving lengths and connectivity',()=>{
 const model=buildBranchingSeed({processId:'beryllium-9',be9View:'3d-assembly',be9AssemblyStep:1});
 const original=buildBranchingSeed({processId:'beryllium-9',seedDepth:8}).layers[0];
 assert.equal(model.audit.depth,8);assert.equal(model.audit.paths,256);assert.equal(model.layers.length,1);assert.equal(model.sidePairs.length,0);assert.equal(model.centerMarkers.length,0);
 assert.deepEqual(model.routes,original.routes);assert.deepEqual(model.nodes.map(n=>n.id),original.nodes.map(n=>n.id));
 const directions={};
 for(const [i,e] of model.edges.entries()){
  assert.equal(e.id,original.edges[i].id);assert.equal(e.from,original.edges[i].from);assert.equal(e.to,original.edges[i].to);assert.equal(e.role,original.edges[i].role);
  const d=e.points[1].map((x,j)=>x-e.points[0][j]);assert(Math.abs(Math.hypot(...d)-1)<1e-12);
  if(directions[e.role])assert(d.every((x,j)=>Math.abs(x-directions[e.role][j])<1e-12));else directions[e.role]=d;
 }
 const r=[directions.red[0],directions.red[2]],b=[directions.blue[0],directions.blue[2]];
 const cosine=r.reduce((s,x,i)=>s+x*b[i],0)/(Math.hypot(...r)*Math.hypot(...b));assert(Math.abs(cosine-Math.cos(2*Math.PI/3))<1e-12);
 assert(model.nodes.some(n=>n.point[2]>0));assert.equal(model.audit.planar,false);
 assert.equal(normalizeSceneSettings({appearance:{be9AssemblyStep:1}}).appearance.be9AssemblyStep,undefined);
});
test('step 2 folds at red/blue midpoints above the fifth white layer',()=>{
 const options={processId:'beryllium-9',be9View:'3d-assembly'},base=buildBranchingSeed(options),folded=buildBranchingSeed({...options,be9AssemblyFold:true});
 assert.equal(folded.layers.length,1);assert.deepEqual(folded.routes,base.routes);assert.equal(folded.nodes.length,81);assert.equal(folded.edges.length,108);
 const distance=(a,b)=>Math.hypot(...a.map((x,i)=>x-b[i]));
 for(const [i,n]of folded.nodes.entries())if(n.lattice[0]<=13)assert.deepEqual(n,base.nodes[i]);
 const creases=folded.edges.filter(e=>e.points.length===3);assert.equal(creases.length,8);assert.equal(creases.filter(e=>e.role==='red').length,4);assert.equal(creases.filter(e=>e.role==='blue').length,4);
 for(const [i,e]of folded.edges.entries()){
  assert.equal(e.id,base.edges[i].id);assert.equal(e.from,base.edges[i].from);assert.equal(e.to,base.edges[i].to);
  assert(Math.abs(e.points.slice(1).reduce((sum,p,j)=>sum+distance(p,e.points[j]),0)-1)<1e-12);
 }
 for(const e of creases){
  assert.notEqual(e.role,'white');const original=base.edges.find(x=>x.id===e.id),mid=original.points[0].map((x,i)=>(x+original.points[1][i])/2);assert.deepEqual(e.points[1],mid);
  const axis=folded.audit.hingeAxis,offset=mid.map((x,i)=>x-folded.audit.hinge[i]),dot=offset.reduce((s,x,i)=>s+x*axis[i],0);assert(Math.hypot(...offset.map((x,i)=>x-dot*axis[i]))<1e-12);
  // Remove the component along the hinge before measuring the rotation.
  const perpendicular=v=>{const d=v.reduce((s,x,i)=>s+x*axis[i],0);return v.map((x,i)=>x-d*axis[i]);};
  const a=perpendicular(e.points[1].map((x,i)=>x-e.points[0][i])),b=perpendicular(e.points[2].map((x,i)=>x-e.points[1][i]));assert(Math.abs(a.reduce((s,x,i)=>s+x*b[i],0)/(Math.hypot(...a)*Math.hypot(...b))-.5)<1e-12);
 }
 const lower=base.nodes.map((n,i)=>n.lattice[0]>13.5?i:null).filter(i=>i!==null);
 for(const i of lower)for(const j of lower)assert(Math.abs(distance(base.nodes[i].point,base.nodes[j].point)-distance(folded.nodes[i].point,folded.nodes[j].point))<1e-12);
 assert.equal(normalizeSceneSettings({appearance:{be9AssemblyFold:true}}).appearance.be9AssemblyFold,true);
});
test('step 3 derives four triangular patches with same-side 60-degree folds and intact junctions',()=>{
 const options={processId:'beryllium-9',be9View:'3d-assembly'},base=buildBranchingSeed({...options,be9AssemblyFold:true}),model=buildBranchingSeed({...options,be9AssemblySides:true});
 assert.equal(model.layers.length,1);assert.equal(model.faces.length,4);assert.equal(model.nodes.length,81);assert.equal(model.edges.length,108);assert.deepEqual(model.routes,base.routes);
 const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),sub=(a,b)=>a.map((x,i)=>x-b[i]);
 const [upper,central,red,blue]=model.faces,normal=model.audit.commonSideNormal,origin=central.points[0];
 for(const tip of [upper.points[0],red.points[1],blue.points[2]])assert(dot(sub(tip,origin),normal)>0);
 for(const hinge of model.audit.sideHinges)assert.equal(Math.abs(hinge.angle),60);
 for(const [i,n]of model.nodes.entries())if(n.lattice[0]<=13)assert.deepEqual(n,base.nodes[i]);
 const nodes=new Map(model.nodes.map(n=>[n.id,n.point]));
 for(const e of model.edges){
  assert.deepEqual(e.points[0],nodes.get(e.from));assert.deepEqual(e.points.at(-1),nodes.get(e.to));
  const length=e.points.slice(1).reduce((s,p,i)=>s+Math.hypot(...sub(p,e.points[i])),0);assert(Math.abs(length-1)<1e-12);
 }
 assert.equal(model.audit.terminalClosures.length,1);assert.equal(model.audit.terminalClosures[0].id,'v(26,0)');
 const saved=normalizeSceneSettings({appearance:{be9AssemblySides:true}});assert.equal(saved.appearance.be9AssemblyFold,true);assert.equal(saved.appearance.be9AssemblySides,true);
});
