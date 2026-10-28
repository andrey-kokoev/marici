import test from 'node:test';
import assert from 'node:assert/strict';
import {refineNeutronBelt} from '../research/realization-tower/refined-neutron-belt.mjs';
const key=face=>face.map(p=>p.map(x=>x.toFixed(8)).join(',')).sort().join('|');
test('ESD7 refinement of the actual annular carrier is conforming and connected',()=>{
 const belt=refineNeutronBelt(),owners=new Map(),neighbors=new Map(belt.bodies.map(b=>[b.id,[]]));
 assert.equal(belt.bodies.length,1050);assert.equal(belt.audit.tetrahedra,714);assert.equal(belt.audit.octahedra,336);
 assert.equal(belt.panelContacts.length,6);assert.ok(belt.panelContacts.every(c=>c.faces===49));
 for(let panel=0;panel<6;panel++)assert.equal(belt.panelContacts.filter(c=>c.panels.includes(panel)).length,2);
 for(const b of belt.bodies){assert.equal(b.role,null);for(const p of b.vertices)assert.ok(Math.abs(p.reduce((a,b)=>a+b,0)-1)<1e-10);for(const f of b.faces){const k=key(f);owners.set(k,(owners.get(k)??0)+1);}}
 assert.ok([...owners.values()].every(n=>n<=2),'no face has more than two owners');
 for(const e of belt.graph.links){neighbors.get(e.from).push(e.to);neighbors.get(e.to).push(e.from);}
 const reached=new Set(),queue=[belt.bodies[0].id];while(queue.length){const id=queue.pop();if(reached.has(id))continue;reached.add(id);queue.push(...neighbors.get(id).filter(n=>!reached.has(n)));}
 assert.equal(reached.size,1050);
 assert.equal([...owners.values()].filter(n=>n===1).length,12*49,'six outer panels plus six radial rim faces, without caps');
});
test('counter-circulation is separate state, not duplicate geometry or new particle labels',()=>{
 const a=refineNeutronBelt({id:'A',circulation:1}),b=refineNeutronBelt({id:'B',circulation:-1});
 for(let i=0;i<a.bodies.length;i++){
  assert.notEqual(a.bodies[i].id,b.bodies[i].id);assert.deepEqual(a.bodies[i].vertices,b.bodies[i].vertices);
  assert.equal(a.bodies[i].refinement.circulation,-b.bodies[i].refinement.circulation);
 }
 // Two parametrizations are NOT an embedded two-belt assembly: insertion still required.
 assert.equal(a.audit.parentInsertion,null);assert.equal(b.audit.parentInsertion,null);
});
