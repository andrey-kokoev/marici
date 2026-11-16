import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),svg=c.IsotopeWiring.renderSVG(d,{interactive:true});
const build=()=>buildLayeredCalcium(d,svg);
function components(topology,keep=()=>true){const adj=new Map(topology.vertices.map(v=>[v.id,[]]));for(const e of topology.edges.filter(keep))adj.get(e.from).push(e.to);const seen=new Set();let n=0;for(const v of adj.keys())if(!seen.has(v)){n++;const q=[v];seen.add(v);for(let i=0;i<q.length;i++)for(const w of adj.get(q[i]))if(!seen.has(w)){seen.add(w);q.push(w);}}return n;}
test('distinct PE, local neutron-space, and wrapper layers retain ownership and counts',()=>{
 const before=JSON.stringify(d),b=build();assert.equal(b.counts.PEOccurrences,20);assert.equal(b.counts.neutronSpaces,10);assert.equal(b.counts.wrappers,6);assert.equal(b.counts.localPEAttachments,20);assert.equal(b.counts.wrapperAttachments,12);assert.equal(b.counts.sameShellContacts,20);assert.equal(b.counts.components,1);assert.equal(JSON.stringify(d),before);
 assert.deepEqual(b.inventory,{PE:20,N:26,localAssignedN:20,wrapperN:6,neutronSpacesAddInventory:false});
 const vertices=new Map(b.topology.vertices.map(v=>[v.id,v]));for(const a of b.attachments.filter(a=>a.kind==='local-PE')){assert.equal(vertices.get(a.from).layer,'PE');assert.equal(vertices.get(a.to).layer,'neutron-space');assert.notEqual(a.from,a.to);}
});
test('each neutron space retains a square boundary and disjoint tetrahedral neutron legs',()=>{
 const b=build(),edges=new Map(b.topology.edges.map(e=>[e.id,e]));for(const s of b.spaces){assert.equal(Object.keys(s.ports).length,4);assert.equal(s.boundary.length,4);assert.equal(s.neutronLegs.length,2);assert.equal(s.tetrahedralTopology.centralJunction,false);
  assert.equal(new Set(s.neutronLegs.flatMap(id=>[edges.get(id).from,edges.get(id).to])).size,4);
  for(const p of Object.values(s.ports))assert.equal([...s.boundary,...s.neutronLegs].filter(id=>edges.get(id).from===p||edges.get(id).to===p).length,3);
 }
});
test('spans and containment do not silently create intermediate-shell attachments',()=>{
 const b=build();assert.deepEqual(b.wrappers.map(w=>w.spans),[['s1','s2'],['s2','s3'],['s1','s2','s3'],['s3','s4'],['s2','s3','s4'],['s1','s2','s3','s4']]);
 for(const w of b.wrappers){assert.equal(w.gateways.length,2);assert.deepEqual(w.intermediateAttachments,[]);assert.deepEqual(w.gateways.map(g=>g.shell),[w.spans[0],w.spans.at(-1)]);}
 assert(b.containment.length>0);assert(b.containment.every(r=>r.createsAttachment===false));
 assert(!b.topology.edges.some(e=>e.kind==='containment'));
});
test('explicit interfaces, not visual enclosure, connect the trial into one graph',()=>{
 const b=build();assert.equal(components(b.topology),1);assert.equal(components(b.topology,e=>e.kind!=='space-to-wrapper'),10);assert.equal(components(b.topology,e=>e.kind!=='PE-to-neutron-space'),21);
});
test('PE excursion uses typed interfaces and reverses exactly with no frame assignment',()=>{
 const b=build(),t=b.transfer,edges=new Map(b.topology.edges.map(e=>[e.id,e]));assert.equal(t.from,'s1-00-lower');assert.equal(t.to,'s2-01-upper');assert.deepEqual(t.reverseVertices,[...t.forwardVertices].reverse());assert.deepEqual(t.reverseEdges,[...t.edges].reverse().map(id=>edges.get(id).reverse));
 let at=t.forwardVertices[0];for(const id of t.PEExcursion){const e=edges.get(id);assert.equal(e.from,at);at=e.to;}assert.equal(at,t.forwardVertices[0]);
 for(const e of b.topology.edges){const r=edges.get(e.reverse);assert.equal(r.from,e.to);assert.equal(r.to,e.from);assert.equal(r.kind,e.kind);assert.equal(r.reverse,e.id);assert.equal(e.transport,undefined);}
 assert.equal(t.edges.length,6);assert.equal(t.PEExcursion.length,18);
});
