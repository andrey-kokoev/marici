import test from 'node:test';
import assert from 'node:assert/strict';
import {buildRuthenium98Wiring} from '../research/realization-tower/ruthenium-98-wiring.mjs';
import {buildRuthenium98Carrier} from '../research/realization-tower/ruthenium-98-model.mjs';
import {createSulfurIncomingBundle} from '../examples/normal-ray/sulfur-incoming-bundle-renderer.js';
const key=p=>p.join(',');
test('Ru has sixteen conserved sign tuples on complete native five-edge paths',()=>{
 const m=buildRuthenium98Wiring(),cells=buildRuthenium98Carrier(),expected=[];
 for(const a of ['+','-'])for(const b of ['+','-'])for(const p of ['+','-'])for(const e of ['+','-'])expected.push(`ru:wire:${a}${b}${p}${e}`);
 assert.deepEqual(m.strands.map(s=>s.id).sort(),expected.sort());assert.deepEqual(m.input,m.output);
 assert.equal(new Set(m.strands.map(s=>key(s.incoming))).size,16);assert.equal(new Set(m.strands.map(s=>key(s.outgoing))).size,16);
 assert.equal(new Set(m.strands.map(s=>key(s.incomingPoints[1]))).size,16);assert.equal(new Set(m.strands.map(s=>key(s.outgoingPoints[0]))).size,16);
 for(const s of m.strands){
  assert.equal(s.guide.length,6);assert.equal(s.edgeIds.length,5);assert.equal(s.branches.length,0);assert.equal(new Set(s.guide.map(key)).size,6);
  for(const p of s.guide){assert.equal(p.reduce((a,b)=>a+b,0),1);assert(p.every(x=>x>=-1&&x<=4));}
  for(let i=1;i<6;i++){
   const a=s.guide[i-1],b=s.guide[i];assert.equal(a.reduce((sum,x,j)=>sum+(x-b[j])**2,0),2);
   assert.equal(a.reduce((sum,x,j)=>sum+(x-b[j])*m.axis[j],0),1);
   assert(cells.some(c=>c.faces.some(f=>f.some(p=>key(p)===key(a))&&f.some(p=>key(p)===key(b)))));
  }
  // Exchanging the two coordinate pairs and reversing the path stays in the
  // complete candidate: (a,b,p,e) -> (a,b,-e,-p), with records unmodified.
  const flip=x=>x==='+'?'-':'+',q=s.polarities,dual=m.strands.find(t=>t.id===`ru:wire:${q.a}${q.b}${flip(q.e)}${flip(q.p)}`);
  assert.deepEqual([...s.guide].reverse().map(p=>[p[2],p[3],p[0],p[1]]),dual.guide);
 }
 assert.equal(m.audit.nativeEdgeCount,78);assert.equal(m.audit.NCarrierCoverage.count,20);assert.deepEqual(m.audit.NCarrierCoverage.uncovered,[]);assert.equal(m.audit.NChannelCount,null);
 assert.equal(new Set(m.strands.map(s=>s.guide.map(key).join(';'))).size,16);
});
test('Ru renders sixteen separate tubes with preserved colours and uniform stripe pitch',()=>{
 const model=buildRuthenium98Wiring(),mesh=createSulfurIncomingBundle(model);assert.equal(mesh.children.length,16);
 const striped=mesh.children.filter(c=>c.material.userData.spiral);assert.equal(striped.length,8);
 assert(striped.every(c=>Math.abs(c.material.userData.spiral.pitch-striped[0].material.userData.spiral.pitch)<1e-9));
 assert.equal(new Set(mesh.children.map(c=>c.userData.incomingStrand)).size,16);
 mesh.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});
});
