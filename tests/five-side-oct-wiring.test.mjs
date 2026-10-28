import test from 'node:test';
import assert from 'node:assert/strict';
import {buildOctahedralFullFibration} from '../research/realization-tower/octahedral-full-fibration.mjs';
import {buildOctahedralCoherentRouting,validateOctahedralCoherentRouting} from '../research/realization-tower/octahedral-coherent-routing.mjs';
import {buildFiveSideOctWiring} from '../research/realization-tower/five-side-oct-wiring.mjs';
import {buildSulfur32Wiring,isSulfurPeriod} from '../research/realization-tower/sulfur-32-wiring.mjs';
import {createDenseOctWiring} from '../examples/normal-ray/dense-oct-wiring-renderer.js';
import {setSulfurWiringOpacity} from '../examples/normal-ray/sulfur-wiring-opacity.js';
const key=vs=>vs.map(String).sort().join('|');

test('Sulfur regression checks both endpoint correspondence and actual N coherence memberships',()=>{
 const reference=buildSulfur32Wiring(),m=buildOctahedralCoherentRouting(1),cells=new Map(reference.groups.map(g=>[g.id,g.members[0].id]));
 assert.deepEqual(new Set(m.fibration.wires.map(w=>`${w.source}|${w.axis}|${w.target}`)),new Set(reference.wires.map(w=>`${cells.get(w.source)}|${w.axis}|${cells.get(w.target)}`)));
 assert.deepEqual(new Set(m.coherenceGroups.map(g=>[...g.members].sort().join('|'))),new Set(reference.channels.map(g=>g.members.map(m=>m.id).sort().join('|'))));
 for(const r of m.routes){const expected=reference.wires.find(w=>cells.get(w.source)===r.source&&w.axis===r.axis),group=m.coherenceGroups.find(g=>g.wireIds.includes(r.id));assert.deepEqual([...group.members].sort(),reference.channels.find(c=>c.id===expected.channel).members.map(m=>m.id).sort());}
});
test('full 80-fibre correspondence retains every cell, coordinate slot and payload',()=>{
 const f=buildOctahedralFullFibration(2),byWire=new Map(f.wires.map(w=>[w.id,w]));
 assert.deepEqual(f.counts,{sourceFibers:80,targetFibers:80,slotWires:320,geometricNCells:85});
 for(const [fibres,role,side] of [[f.sourceFibers,'proton','source'],[f.targetFibers,'electron','target']]){
  assert.deepEqual(new Set(fibres.map(x=>x.cell)),new Set(f.sector.cells.filter(c=>c.role===role).map(c=>c.id)));
  assert.equal(fibres.flatMap(x=>x.slots).length,320);assert.equal(new Set(fibres.flatMap(x=>x.slots)).size,320);
  for(const fibre of fibres)for(let axis=0;axis<4;axis++){const w=byWire.get(fibre.slots[axis]);assert.equal(w.axis,axis);assert.equal(w[side],fibre.cell);assert(isSulfurPeriod(w.transport));}
 }
 const payloads=new Map(f.wires.map((w,i)=>[w.id,{id:w.id,value:[i,-i],history:[`original:${i}`]}]));
 assert.deepEqual(new Map(f.targetFibers.flatMap(f=>f.slots.map(id=>[id,payloads.get(id)]))),new Map(f.sourceFibers.flatMap(f=>f.slots.map(id=>[id,payloads.get(id)]))));
});
test('every filler has four actual opposite-face channels and all native interfaces are retained',()=>{
 const m=buildOctahedralCoherentRouting(2),cells=new Map(m.fibration.sector.cells.map(c=>[c.id,c])),ports=new Map(m.ports.map(p=>[p.id,p]));
 assert.equal(m.slots.length,340);assert.equal(m.coherenceGroups.length,62);assert.equal(m.audit.nativeInterfaces,560);assert.equal(m.audit.occupiedNativeFaces,760);assert.equal(m.audit.interiorAdmissions,19);assert.equal(m.audit.boundarySeams,119);
 for(const s of m.slots){const c=cells.get(s.cell),a=ports.get(s.entry),b=ports.get(s.exit);assert(s.wireIds.length>0);assert.equal(a.cell,b.cell);assert.equal(a.axis,b.axis);assert.notEqual(a.face,b.face);assert(c.faces.some(f=>key(f)===a.face));assert(c.faces.some(f=>key(f)===b.face));
  for(const p of s.points){assert(Math.abs(p.reduce((a,b)=>a+b,0)-1)<1e-9);for(let i=0;i<4;i++)assert(p[i]>=Math.min(...c.vertices.map(v=>v[i]))-1e-9&&p[i]<=Math.max(...c.vertices.map(v=>v[i]))+1e-9);}
 }
 for(const r of m.routes){assert(r.slots.length>0);assert.equal(new Set(r.ports).size,r.ports.length);assert.equal(m.coherenceGroups.filter(g=>g.wireIds.includes(r.id)).length,1);}
 for(const l of m.links.filter(l=>l.kind==='native-interface')){assert.equal(ports.get(l.from).face,ports.get(l.to).face);assert.notEqual(ports.get(l.from).cell,ports.get(l.to).cell);}
 assert.equal(validateOctahedralCoherentRouting(m).unwiredFillerSlots,0);
});
test('validation rejects missing internal routing, copied records, and missing group membership',()=>{
 const original=buildOctahedralCoherentRouting(2);
 const missing=structuredClone(original);missing.slots.pop();assert.throws(()=>validateOctahedralCoherentRouting(missing),/slot inventory/);
 const copied=structuredClone(original);copied.links[0].wireIds.push(copied.links[0].wireIds[0]);assert.throws(()=>validateOctahedralCoherentRouting(copied),/copies or loses/);
 const group=structuredClone(original);group.coherenceGroups[0].wireIds.pop();assert.throws(()=>validateOctahedralCoherentRouting(group),/internal wiring/);
 const severed=structuredClone(original);severed.routes[0].links.splice(1,1);assert.throws(()=>validateOctahedralCoherentRouting(severed),/Invalid retained route/);
});
test('renderer draws internal port routes and exposes isolated coherence groups, not edge-fill paths',()=>{
 const m=buildFiveSideOctWiring(),rendered=createDenseOctWiring(m);assert.equal(rendered.children.length,5);assert.equal(m.renderPaths.filter(p=>p.kind==='N-interior').length,340);assert.equal(m.renderPaths.filter(p=>p.kind==='boundary-seam').length,119);
 assert.equal(rendered.userData.audit.retainedFibres,80);assert.equal(rendered.userData.audit.retainedSlotWires,320);assert.equal(rendered.userData.audit.internalChannels,340);assert(rendered.userData.audit.triangles<84000);
 for(const mesh of rendered.children){const g=mesh.geometry;assert([...g.attributes.position.array,...g.attributes.normal.array,...g.attributes.uv.array].every(Number.isFinite));assert([...g.index.array].every(i=>i<g.attributes.position.count));}
 setSulfurWiringOpacity(rendered,{wireOpacity:1});assert(rendered.children.every(o=>!o.material.transparent&&o.material.depthWrite));setSulfurWiringOpacity(rendered,{wireOpacity:0});assert(rendered.children.every(o=>!o.visible));
 const warm=createDenseOctWiring(m);assert(warm.userData.audit.meshDataCacheHit);for(let i=0;i<5;i++){assert.notEqual(rendered.children[i].geometry,warm.children[i].geometry);assert.equal(rendered.children[i].geometry.attributes.position.array,warm.children[i].geometry.attributes.position.array);}
 const group=m.coherenceGroups.find(g=>g.members.length>1),selected=buildFiveSideOctWiring(group.id);assert.equal(selected.strands.length,group.wireIds.length);assert.equal(selected.renderPaths.filter(p=>p.kind==='N-interior').length,group.members.length*4);assert(selected.renderPaths.every(p=>p.wireIds.some(id=>group.wireIds.includes(id))));
 for(const g of [rendered,warm])g.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
