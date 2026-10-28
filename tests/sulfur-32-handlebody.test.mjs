import test from 'node:test';
import assert from 'node:assert/strict';
import {buildSulfur32Handlebody} from '../research/realization-tower/sulfur-32-handlebody.mjs';
import {sulfurHandlebodySurface,createSulfurHandlebody} from '../examples/normal-ray/sulfur-handlebody-renderer.js';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const model=buildSulfur32Handlebody();
test('empty carrier retains N chambers and neutral junction incidence, without seam shortcuts',()=>{
 assert.equal(model.nodes.length,51);assert.equal(model.nodes.filter(n=>n.kind==='N-chamber').length,19);assert.equal(model.links.length,104);assert.equal(model.ports.length,6);
 const byId=new Map(model.nodes.map(n=>[n.id,n])),seen=new Set([model.nodes[0].id]);
 for(const e of model.links){assert.notEqual(byId.get(e.from).kind,byId.get(e.to).kind);assert.equal(e.face.length,3);}
 for(let changed=true;changed;){changed=false;for(const e of model.links)if(seen.has(e.from)||seen.has(e.to))for(const id of [e.from,e.to])if(!seen.has(id)){seen.add(id);changed=true;}}
 assert.equal(seen.size,51);assert.equal(model.audit.wireCount,0);
 for(let pair=0;pair<3;pair++){const ps=model.ports.filter(p=>p.pair===pair);assert.equal(ps.length,2);assert(ps[0].position.every((x,i)=>x+ps[1].position[i]===2*model.centre[i]));}
});
test('one nonempty union skin with six clipped mouths, no payload or wire meshes',()=>{
 const surface=sulfurHandlebodySurface(model);assert(surface.triangles>1000);assert(surface.triangles<150000);assert(surface.positions.every(Number.isFinite));
 assert.equal(surface.positions.length,surface.normals.length);
 const group=createSulfurHandlebody(model),skin=group.children.find(c=>c.userData.sulfurHandlebodySkin);
 assert(skin);assert.equal(skin.material.clippingPlanes.length,6);assert.equal(group.children.filter(c=>c.isMesh).length,7);
 assert.equal(group.userData.audit.wireCount,0);assert.equal(group.userData.audit.openMouths,6);
 group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
test('sampled union skin is connected and preserves the graph handle count before mouth clipping',()=>{
 const {positions}=sulfurHandlebodySurface(model),vertices=new Map(),edges=new Map();let faces=0;
 for(let i=0;i<positions.length;i+=9){
  const ids=[];for(let j=0;j<3;j++){const key=[0,1,2].map(a=>positions[i+3*j+a].toFixed(6)).join(',');if(!vertices.has(key))vertices.set(key,vertices.size);ids.push(vertices.get(key));}
  assert.equal(new Set(ids).size,3);faces++;
  for(let j=0;j<3;j++){const a=ids[j],b=ids[(j+1)%3],key=[a,b].sort((x,y)=>x-y).join(',');if(!edges.has(key))edges.set(key,{a,b,count:0,orientation:0});const e=edges.get(key);e.count++;e.orientation+=a<b?1:-1;}
 }
 assert([...edges.values()].every(e=>e.count===2&&e.orientation===0));
 const adjacency=Array.from({length:vertices.size},()=>[]);for(const e of edges.values()){adjacency[e.a].push(e.b);adjacency[e.b].push(e.a);}
 const seen=new Set([0]),queue=[0];for(let i=0;i<queue.length;i++)for(const n of adjacency[queue[i]])if(!seen.has(n)){seen.add(n);queue.push(n);}
 assert.equal(seen.size,vertices.size);
 assert.equal(vertices.size-edges.size+faces,2-2*model.audit.graphCycleRank);
});
test('empty-view setting persists separately from process stage and direction',()=>{
 const s=normalizeSceneSettings({appearance:{sulfurHandlebody:true,cellGraph:true},process:{id:'sulfur-32',step:1,branch:3}});
 assert.equal(s.appearance.sulfurHandlebody,true);assert.equal(s.process.step,1);assert.equal(s.process.branch,3);
 assert.equal(normalizeSceneSettings({appearance:{sulfurHandlebody:'true'}}).appearance.sulfurHandlebody,false);
});
