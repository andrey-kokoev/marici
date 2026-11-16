import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedCellInterface} from '../examples/isotope-wiring/core/stacked-cell-interface.mjs';
import {auditFrameReturn} from '../examples/isotope-wiring/core/frame-return.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),b=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true}));
function reachable(topology,start,excluded){const seen=new Set([start]),q=[start];for(let i=0;i<q.length;i++)for(const e of topology.edges)if(e.from===q[i]&&e.support!==excluded&&!seen.has(e.to)){seen.add(e.to);q.push(e.to);}return seen;}
test('one reversible bridge joins exactly the selected stacked cells without changing the full model',()=>{
 const before=JSON.stringify(b),r=buildStackedCellInterface(b);assert.equal(JSON.stringify(b),before);assert.equal(r.counts.cells,2);assert.equal(r.counts.PEOccurrences,4);assert.equal(r.interface.from,'space:s1-00:B');assert.equal(r.interface.to,'space:s2-01:T');assert.equal(r.interface.channelSupports.length,1);
 const rows=r.topology.edges.filter(e=>e.kind==='stacked-interface');assert.equal(rows.length,2);assert.equal(rows[0].reverse,rows[1].id);assert.equal(rows[1].reverse,rows[0].id);assert.equal(rows[0].support,rows[1].support);
 assert.equal(reachable(r.topology,r.interface.from).size,r.topology.vertices.length);assert(!reachable(r.topology,r.interface.from,r.interface.channelSupports[0]).has(r.interface.to));
});
test('neutron-mediated version subdivides one channel without adding a cycle or particle',()=>{
 const direct=buildStackedCellInterface(b),r=buildStackedCellInterface(b,{mode:'neutron-mediated'});assert.equal(r.counts.vertices,direct.counts.vertices+1);assert.equal(r.counts.supports,direct.counts.supports+1);assert.equal(r.counts.cycleRank,direct.counts.cycleRank);assert.equal(r.counts.neutralCycleRank,6);assert.equal(r.inventory.addedNeutrons,0);assert.deepEqual(r.inventory.fullIsotope,b.inventory);
 const middle=r.topology.vertices.find(v=>v.layer==='neutron-interface');assert.equal(middle.position,undefined);assert.equal(r.topology.edges.filter(e=>e.from===middle.id).length,2);
 for(const support of r.interface.channelSupports)assert(!reachable(r.topology,r.interface.from,support).has(r.interface.to));
});
test('both modes reverse their transfers exactly and preserve internal branching',()=>{
 for(const mode of ['direct','neutron-mediated']){const r=buildStackedCellInterface(b,{mode}),edges=new Map(r.topology.edges.map(e=>[e.id,e]));assert.deepEqual(r.transfer.reverseVertices,[...r.transfer.forwardVertices].reverse());assert.deepEqual(r.transfer.reverseEdges,[...r.transfer.edges].reverse().map(id=>edges.get(id).reverse));
  for(const s of r.spaces){assert.equal(s.neutronLegs.length,2);assert.equal(s.boundary.length,4);for(const port of Object.values(s.ports))assert(r.topology.edges.filter(e=>e.from===port).length>=3);}
  let at=r.transfer.forwardVertices[0];for(const id of r.transfer.excursion){assert.equal(edges.get(id).from,at);at=edges.get(id).to;}assert.equal(at,r.transfer.forwardVertices[0]);
 }
});
test('does not claim global uniqueness or frame return by deleting evidence',()=>{
 const r=buildStackedCellInterface(b);assert(r.bypassInOriginalModel);assert(r.excludedInterfaces.some(e=>e.kind==='space-to-wrapper'));assert(r.excludedInterfaces.some(e=>e.kind==='neutron-space-contact'));assert(!r.topology.edges.some(e=>e.kind==='space-to-wrapper'));
 const topology=structuredClone(r.topology);topology.walks.push({id:'stacked-excursion',kind:'PE',base:r.transfer.forwardVertices[0],edges:r.transfer.excursion});assert.equal(auditFrameReturn(topology).status,'unknown');assert.equal(r.frameReturn,'unknown');
});
test('rejects unknown modes and incorrect contact provenance',()=>{
 assert.throws(()=>buildStackedCellInterface(b,{mode:'one-way'}),/Unknown interface mode/);const bad=structuredClone(b);bad.wrappers[0].gateways[0].spacePort='T';assert.throws(()=>buildStackedCellInterface(bad),/Unexpected stacked ports/);
});
