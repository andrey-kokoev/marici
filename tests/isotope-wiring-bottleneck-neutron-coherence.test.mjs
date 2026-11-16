import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedFullInterface} from '../examples/isotope-wiring/core/stacked-full-interface.mjs';
import {studyBottleneckNeutronCoherence} from '../examples/isotope-wiring/core/bottleneck-neutron-coherence.mjs';
import {buildNeutronCoherence} from '../examples/isotope-wiring/core/neutron-space-coherence.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),b=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true}));
const full=mode=>buildStackedFullInterface(b,{mode});
test('fresh neutral coverage works with a single-anchor wrapper in both contact variants',()=>{
 for(const mode of ['direct','neutron-mediated']){const f=full(mode),before=JSON.stringify(f),r=studyBottleneckNeutronCoherence(f);assert.equal(JSON.stringify(f),before);assert.equal(r.comparison.localCoverage,'actual-interface-ports');assert.equal(r.comparison.localAccessPairsChecked,36);assert.equal(r.comparison.basis.length,53);assert.equal(r.comparison.localComparisons.length,8);assert.equal(r.comparison.wrapperComparisons.length,6);assert.equal(r.actual.walks.length,67);assert.equal(r.status,'unknown');assert(r.actual.walks.every(w=>w.status==='unknown'));assert.equal(r.comparison.counts.vertices,mode==='direct'?64:65);}
});
test('cyclic twists fail while inverse-consistent bridge twists preserve coherence',()=>{
 for(const mode of ['direct','neutron-mediated']){const r=studyBottleneckNeutronCoherence(full(mode));assert.equal(r.flatControl.status,'verified');assert.equal(r.twistedControl.status,'refuted');assert.equal(r.bridgeTwistControl.status,'verified');assert(r.bridgeChecks.every(b=>b.isBridge&&!b.isBasisChord));assert.equal(r.bridgeChecks.length,mode==='direct'?1:2);}
});
test('basis remains independent after downstream delegation and bridge subdivision',()=>{
 const r=studyBottleneckNeutronCoherence(full('neutron-mediated')).comparison,edges=new Map(r.topology.edges.map(e=>[e.id,e])),supports=[...new Set(r.topology.edges.map(e=>e.support))],indices=new Map(supports.map((s,i)=>[s,i])),pivots=new Map();
 for(const w of r.basis){let row=0n;for(const id of w.edges)row^=1n<<BigInt(indices.get(edges.get(id).support));while(row){const p=row.toString(2).length-1;if(pivots.has(p))row^=pivots.get(p);else{pivots.set(p,row);break;}}assert.notEqual(row,0n);}assert.equal(pivots.size,53);
});
test('does not use nominal wrapper spans as physical port attachments',()=>{
 const f=full('direct'),r=buildNeutronCoherence(f.model,{localCoverage:'actual-interface-ports'});f.model.wrappers.forEach(w=>{w.spans=['metadata-only'];});const changed=buildNeutronCoherence(f.model,{localCoverage:'actual-interface-ports'});assert.deepEqual(changed.topology,r.topology);assert.deepEqual(changed.localComparisons,r.localComparisons);
 assert.throws(()=>buildNeutronCoherence(f.model),/does not apply/);
});
test('rejects a restored bypass and missing local access instead of reporting stale coverage',()=>{
 const f=full('direct'),from=f.interface.from,to=f.interface.to;f.model.topology.edges.push({id:'bypass',from,to,reverse:'bypass:r',support:'bypass',kind:'test'},{id:'bypass:r',from:to,to:from,reverse:'bypass',support:'bypass',kind:'test'});assert.throws(()=>studyBottleneckNeutronCoherence(f),/neutral bypass/);
 const broken=full('direct');broken.model.topology.edges=broken.model.topology.edges.filter(e=>e.kind!=='neutron-space-contact');assert.throws(()=>studyBottleneckNeutronCoherence(broken),/Missing local route/);
});
