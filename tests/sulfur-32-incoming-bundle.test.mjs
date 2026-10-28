import test from 'node:test';
import assert from 'node:assert/strict';
import {buildSulfurIncomingBundle} from '../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {buildPESymmetricSector} from '../research/strominger/pe-symmetric-sector.mjs';
import {createSulfurIncomingBundle} from '../examples/normal-ray/sulfur-incoming-bundle-renderer.js';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
import {createSulfurNTubeMarkers} from '../examples/normal-ray/sulfur-n-tube-markers.js';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import * as T from 'three';
import {setSulfurWiringOpacity} from '../examples/normal-ray/sulfur-wiring-opacity.js';
const key=p=>p.map(x=>Math.round(x*1e9)/1e9).join(',');
test('sixteen conserved identities have complete native paths and full N-group coverage',()=>{
 const m=buildSulfurIncomingBundle(),sector=buildPESymmetricSector(1);
 assert.equal(m.strands.length,16);assert.equal(new Set(m.strands.map(s=>s.id)).size,16);
 assert.deepEqual(m.input.toSorted((a,b)=>a.strandId.localeCompare(b.strandId)),m.output.toSorted((a,b)=>a.strandId.localeCompare(b.strandId)));assert.equal(m.audit.branchSegments,0);
 assert.equal(new Set(m.audit.endpointPermutation).size,16);
 assert.equal(m.strands.filter(s=>s.middleRouting==='rim').length,8);
 assert.equal(m.strands.filter(s=>s.middleRouting==='interior').length,8);
 const expected=[];for(const a of ['+','-'])for(const b of ['+','-'])for(const p of ['+','-'])for(const e of ['+','-'])expected.push(`wire:${a}${b}${p}${e}`);
 assert.deepEqual(m.strands.map(s=>s.id).sort(),expected.sort());
 assert.equal(new Set(m.strands.map(s=>key(s.points[0]))).size,16);
 assert.equal(new Set(m.strands.map(s=>key(s.points.at(-1)))).size,16);
 const height=p=>p.reduce((sum,x,i)=>sum+(x-sector.centre[i])*m.axis[i],0);
 for(const s of m.strands){
  assert.equal(s.branches.length,0);assert.equal(s.edgeIds.length,s.guide.length-1);
  assert.equal(new Set(s.guide.map(key)).size,s.guide.length);
  assert.deepEqual(s.guide[0],m.tip);assert.deepEqual(s.guide.at(-1),m.exitTip);
  const partner=m.strands[s.outputSlot];
  for(let i=0;i<4;i++)assert(partner.guide[i].every((x,j)=>Math.abs(x-2*height(partner.guide[i])*m.axis[j]-s.guide[s.guide.length-1-i][j])<1e-9));
  for(let i=1;i<s.guide.length;i++){
   assert(height(s.guide[i])<=height(s.guide[i-1])+1e-9);
   const edge=m.edges.find(e=>e.id===s.edgeIds[i-1]);assert(edge.strandIds.includes(s.id));
   assert(sector.cells.some(c=>c.faces.some(f=>edge.guide.every(v=>f.some(p=>key(p)===key(v))))));
  }
  assert(partner.points[0].every((x,j)=>Math.abs(x-2*height(partner.points[0])*m.axis[j]-s.points.at(-1)[j])<1e-9));
  assert.equal(m.output[s.outputSlot].strandId,s.id);
  assert.deepEqual(m.output[s.outputSlot].polarities,s.polarities);
  // Reversing presentation recovers the retained record, not a reconstructed copy.
  const reverse={id:s.id,polarities:s.polarities,path:[...s.guide].reverse()};
  assert.deepEqual([...reverse.path].reverse(),s.guide);assert.deepEqual(reverse.polarities,s.polarities);
 }
 assert.equal(m.edges.length,63);assert.equal(m.audit.internalSegments,11);
 for(const edge of m.edges){assert.equal(new Set(edge.strandIds).size,edge.strandIds.length);assert(edge.strandIds.length>0);}
 assert.deepEqual(m.layer2Joins.find(j=>j.cell==='electron:-1,0,1,0').labels,['white','red-white']);
 assert(m.layer2Joins.every(j=>j.inputs.length===4));assert.equal(m.layer3Mixes.length,8);
 // Coverage is an incidence observation, not an inferred tube/particle count.
 assert.equal(m.audit.NCarrierCoverage.count,19);assert.equal(m.audit.NCarrierCoverage.uncovered.length,0);assert.equal(m.audit.NChannelCount,null);
 assert.equal(m.audit.NGroupCoverage.count,16);
 assert.equal(new Set(m.channelGroups.flatMap(g=>g.members)).size,19);
 for(const group of m.channelGroups){
  assert(group.strandIds.length>0);
  for(const id of group.strandIds){const strand=m.strands.find(s=>s.id===id);assert(strand.edgeIds.some(id=>m.edges.find(e=>e.id===id).carrierCells.some(c=>group.members.includes(c))));}
 }
});
test('renderer keeps sixteen continuous tubes, colour identities and equal stripe pitch',()=>{
 const m=buildSulfurIncomingBundle(),mesh=createSulfurIncomingBundle(m);assert.equal(mesh.children.length,16);
 assert.equal(new Set(mesh.children.map(c=>c.userData.incomingStrand)).size,16);
 assert(mesh.children.every(c=>c.geometry.type==='TubeGeometry'&&c.geometry.parameters.radius===.024));
 const striped=mesh.children.filter(c=>c.material.userData.spiral);assert.equal(striped.length,8);
 for(const c of striped){
  assert(Math.abs(c.material.userData.spiral.pitch-striped[0].material.userData.spiral.pitch)<1e-9);
  const shader={uniforms:{},vertexShader:'#include <begin_vertex>',fragmentShader:'#include <color_fragment>'};c.material.onBeforeCompile(shader);
  assert.equal(shader.uniforms.spiralB.value.getHex(),0xffffff);
 }
 mesh.traverse(o=>{o.geometry?.dispose();for(const mat of Array.isArray(o.material)?o.material:[o.material])mat?.dispose();});
});
test('N sleeves follow occupied edges and enclose actual lanes without altering routes',()=>{
 const model=buildSulfurIncomingBundle(),before=JSON.stringify(model),markers=createSulfurNTubeMarkers(model);
 const {identities,selectedIdentity,visibleIdentities,sharedSegments,...baseAudit}=markers.userData.audit;
 assert.deepEqual(baseAudit,{groups:16,pieces:59,schematic:true,alignedToWiring:true,nativeEdges:63,continuousSegments:59,internalJoins:4,closedSegments:0,junctions:28,deferredJunctions:0,endCollars:118});
 assert.equal(identities.length,16);assert.equal(selectedIdentity,'all');assert.equal(visibleIdentities,16);assert.equal(sharedSegments,11);
 assert.equal(markers.children.flatMap(p=>p.userData.edgeIds).length,63);
 assert.equal(new Set(markers.children.flatMap(p=>p.userData.edgeIds)).size,63);
 assert.equal(new Set(markers.children.flatMap(p=>p.userData.sourceCells)).size,19);
 assert.equal(new Set(markers.children.flatMap(p=>p.userData.nGroups)).size,16);
 for(const piece of markers.children){
  assert.equal(piece.children.filter(o=>o.userData.tubePart).length,3); // Shell and two prominent collars.
  assert.equal(piece.children.filter(o=>o.userData.endCollar).length,2);
  const info=piece.userData.hoverInfo;assert.equal(info.kind,'tube');assert.equal(info.id,piece.userData.id);
  assert.deepEqual(info.tube.groups.map(g=>g.id),piece.userData.nGroups);
  assert.deepEqual(info.tube.strands.map(s=>s.id),piece.userData.strandIds);
  assert.equal(info.position.length,4);assert.equal(info.worldPosition.length,3);
  assert.doesNotThrow(()=>JSON.stringify(info));
  const geometry=piece.children[0].geometry,sides=geometry.userData.sides;
  assert.equal(geometry.userData.ringCount,piece.userData.points.length);
  for(let i=0;i<piece.userData.points.length;i++){
   const centre=new T.Vector3();for(let k=0;k<sides;k++)centre.add(new T.Vector3().fromBufferAttribute(geometry.attributes.position,i*sides+k));centre.divideScalar(sides);
   assert(centre.distanceTo(new T.Vector3(...piece.userData.renderPoints[i]))<1e-6);
  }
  for(const edgeId of piece.userData.edgeIds){
   const edge=model.edges.find(e=>e.id===edgeId),a=new T.Vector3(...worldPoint(edge.guide[0])),direction=new T.Vector3(...worldPoint(edge.guide[1])).sub(a).normalize();
   for(const id of edge.strandIds){
    const run=model.strands.find(s=>s.id===id).edgeRuns.find(r=>r.edgeId===edge.id);
    for(const p of run.points){const relative=new T.Vector3(...worldPoint(p)).sub(a),radial=relative.clone().addScaledVector(direction,-relative.dot(direction));assert(radial.length()+.024<piece.userData.radius);}
   }
  }
  assert.deepEqual(piece.userData.nGroups,model.channelGroups.filter(g=>piece.userData.sourceCells.some(c=>g.members.includes(c))).map(g=>g.id));
 }
 // Welded shell/junction surface has only the eight external mouths open.
 const surfaceEdges=new Map();
 markers.traverse(o=>{
  if(!o.isMesh||o.userData.endCollar)return;
  const g=o.geometry,ix=g.index.array,p=g.attributes.position;
  const vertex=i=>[p.getX(i),p.getY(i),p.getZ(i)].map(x=>Math.round(x*1e6)).join(',');
  for(let i=0;i<ix.length;i+=3)for(const [a,b] of [[ix[i],ix[i+1]],[ix[i+1],ix[i+2]],[ix[i+2],ix[i]]]){const k=[vertex(a),vertex(b)].sort().join('|');surfaceEdges.set(k,(surfaceEdges.get(k)??0)+1);}
 });
 assert([...surfaceEdges.values()].every(n=>n===1||n===2));
 assert.equal([...surfaceEdges.values()].filter(n=>n===1).length,8*24);
 assert.equal(JSON.stringify(model),before);
 markers.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
 assert.equal(normalizeSceneSettings({}).appearance.sulfurNTubeMarkers,false);
 assert.equal(normalizeSceneSettings({appearance:{sulfurNTubeMarkers:true}}).appearance.sulfurNTubeMarkers,true);
});
test('N identity selection isolates its segments and preserves shared membership',()=>{
 const model=buildSulfurIncomingBundle(),central=model.channelGroups.find(g=>g.members.includes('neutron:1,1,1,0'));
 const markers=createSulfurNTubeMarkers(model,{selectedIdentity:central.id});
 assert.equal(markers.userData.audit.visibleIdentities,1);assert.equal(markers.children.length,3);
 for(const piece of markers.children){assert(piece.userData.nGroups.includes(central.id));assert.equal(piece.userData.nGroups.length,2);}
 assert.equal(normalizeSceneSettings({appearance:{sulfurNIdentity:central.id}}).appearance.sulfurNIdentity,central.id);
 assert.equal(normalizeSceneSettings({appearance:{sulfurNIdentity:'invalid'}}).appearance.sulfurNIdentity,'all');
 markers.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
test('tube and wire opacity controls are independent, persistent and include zero',()=>{
 const model=buildSulfurIncomingBundle(),root=new T.Group(),wires=createSulfurIncomingBundle(model),tubes=createSulfurNTubeMarkers(model);root.add(wires,tubes);
 const geometries=wires.children.map(c=>c.geometry);
 setSulfurWiringOpacity(root,{wireOpacity:.35,tubeOpacity:.5});
 assert(wires.children.every(c=>c.material.opacity===.35));
 tubes.traverse(o=>{if(o.userData.nTubeOpacityScale===1)assert.equal(o.material.opacity,.5);});
 setSulfurWiringOpacity(root,{wireOpacity:0,tubeOpacity:0});
 root.traverse(o=>{if(o.material)assert.equal(o.material.opacity,0);});
 assert.deepEqual(wires.children.map(c=>c.geometry),geometries);
 const settings=normalizeSceneSettings({appearance:{sulfurWireOpacity:.35,sulfurNTubeOpacity:.5}});
 assert.equal(settings.appearance.sulfurWireOpacity,.35);assert.equal(settings.appearance.sulfurNTubeOpacity,.5);
 assert.equal(normalizeSceneSettings({appearance:{sulfurWireOpacity:0,sulfurNTubeOpacity:0}}).appearance.sulfurWireOpacity,0);
 root.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
test('legacy graph settings stay graph settings; new bundle is opt-in and persists',()=>{
 const legacy=normalizeSceneSettings({process:{id:'sulfur-32'},appearance:{cellGraph:true}});assert(legacy.appearance.cellGraph);assert.equal(legacy.appearance.sulfurWireBundle,false);
 const wire=normalizeSceneSettings({process:{id:'sulfur-32'},appearance:{sulfurWireBundle:true,cellGraph:false}});assert(wire.appearance.sulfurWireBundle);assert.equal(wire.appearance.cellGraph,false);
});
