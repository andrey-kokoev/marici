import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedFullInterface} from '../examples/isotope-wiring/core/stacked-full-interface.mjs';
import {auditLayeredTransfers} from '../examples/isotope-wiring/core/layered-transfer-audit.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),b=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true}));
function reachable(t,start,removed){const seen=new Set([start]),q=[start];for(let i=0;i<q.length;i++)for(const e of t.edges)if(e.from===q[i]&&e.support!==removed&&!seen.has(e.to)){seen.add(e.to);q.push(e.to);}return seen;}
test('both full-model variants retain all cells, PE occurrences, wrapper boundaries, and inventory',()=>{
 const before=JSON.stringify(b);for(const mode of ['direct','neutron-mediated']){const r=buildStackedFullInterface(b,{mode});assert.equal(r.counts.PEOccurrences,20);assert.equal(r.counts.neutronSpaces,10);assert.equal(r.counts.wrappers,6);assert.equal(r.counts.cycleRank,73);assert.deepEqual(r.model.inventory,b.inventory);
  for(const w of b.wrappers){const actual=r.model.wrappers.find(a=>a.id===w.id);assert.deepEqual(actual.boundary,w.boundary);assert.deepEqual(actual.spans,w.spans);for(const id of w.boundary)assert(r.model.topology.edges.some(e=>e.id===id));}
 }assert.equal(JSON.stringify(b),before);
});
test('the channel is a global cut, not just a local shortest path',()=>{
 for(const mode of ['direct','neutron-mediated']){const r=buildStackedFullInterface(b,{mode}),t=r.model.topology;assert.equal(reachable(t,r.interface.from).size,t.vertices.length);assert.equal(r.interface.globalShell1ExitSupports.length,1);
  for(const support of r.interface.channelSupports){const upstream=reachable(t,r.interface.from,support);assert(!upstream.has(r.interface.to));assert.equal([...upstream].filter(id=>id.startsWith('PE:')).length,6);}
 }
});
test('old bypass terminals are explicitly removed or delegated, not silently erased with wrappers',()=>{
 const r=buildStackedFullInterface(b);assert.deepEqual(r.changes.map(c=>[c.wrapper,c.action]),[['wrapper:1','remove-upstream-terminal'],['wrapper:3','delegate-downstream'],['wrapper:6','delegate-downstream']]);assert.equal(r.model.wrappers[0].gateways.length,1);assert.equal(r.counts.wrapperAttachments,11);
 assert(!r.model.topology.edges.some(e=>e.id==='attach:wrapper:1:T'));for(const id of ['attach:wrapper:3:T','attach:wrapper:6:T'])assert.equal(r.model.topology.edges.find(e=>e.id===id).from,r.interface.to);
 assert.throws(()=>auditLayeredTransfers(r.model),/does not apply/);
});
test('full-model PE excursion reverses, but absent frame law remains unknown',()=>{
 const r=buildStackedFullInterface(b),t=r.model.transfer;assert.deepEqual(t.reverseVertices,[...t.forwardVertices].reverse());assert.equal(r.frameAudit.status,'unknown');assert.equal(r.frameAudit.walks.length,21);assert(r.frameAudit.walks.every(w=>w.status==='unknown'));
});
test('an extra upstream exit is detected instead of accepting a false bottleneck',()=>{
 const bad=structuredClone(b),from='space:s1-00:B',to='space:s3-00:T';bad.topology.edges.push({id:'bypass',from,to,support:'bypass',reverse:'bypass:r',kind:'test'},{id:'bypass:r',from:to,to:from,support:'bypass',reverse:'bypass',kind:'test'});assert.throws(()=>buildStackedFullInterface(bad),/extra exit/);
});
