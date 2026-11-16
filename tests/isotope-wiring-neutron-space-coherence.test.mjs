import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildNeutronCoherence,studyNeutronCoherence} from '../examples/isotope-wiring/core/neutron-space-coherence.mjs';
import {auditFrameReturn} from '../examples/isotope-wiring/core/frame-return.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),svg=c.IsotopeWiring.renderSVG(d,{interactive:true});
const build=()=>buildLayeredCalcium(d,svg),I=[[1,0,0],[0,1,0],[0,0,1]];
test('retains eight local and six wrapper alternatives without imposing unique arrows',()=>{
 const b=build(),before=JSON.stringify(b),r=buildNeutronCoherence(b);assert.equal(JSON.stringify(b),before);
 assert.deepEqual(r.counts,{vertices:64,supports:116,components:1,cycleRank:53,basisCycles:53,localPathPairs:8,wrapperPathPairs:6,comparisonWalks:14});assert.equal(r.topology.walks.length,67);
 const edges=new Map(r.topology.edges.map(e=>[e.id,e]));for(const pair of [...r.localComparisons,...r.wrapperComparisons]){assert.equal(pair.paths.length,2);assert.notDeepEqual(pair.paths[0],pair.paths[1]);for(const path of pair.paths){let at=pair.from;for(const id of path){const e=edges.get(id);assert.equal(e.from,at);at=e.to;}assert.equal(at,pair.to);}}
 assert(r.topology.vertices.every(v=>v.layer!=='PE'));assert(r.topology.edges.every(e=>e.kind!=='PE-cycle'&&e.kind!=='PE-to-neutron-space'));
});
test('basis is independent over supports and reaches the full graph cycle rank',()=>{
 const r=buildNeutronCoherence(build()),edges=new Map(r.topology.edges.map(e=>[e.id,e])),supports=[...new Set(r.topology.edges.map(e=>e.support))],index=new Map(supports.map((id,i)=>[id,i]));
 const pivots=new Map();for(const w of r.basis){let vector=0n;for(const id of w.edges)vector^=1n<<BigInt(index.get(edges.get(id).support));while(vector){const pivot=vector.toString(2).length-1;if(pivots.has(pivot))vector^=pivots.get(pivot);else{pivots.set(pivot,vector);break;}}assert.notEqual(vector,0n,'dependent fundamental cycle');}assert.equal(pivots.size,53);
});
test('missing transport is unknown for every actual comparison, never assumed identity',()=>{
 const r=studyNeutronCoherence(build());assert.equal(r.status,'unknown');assert.equal(r.actual.status,'unknown');assert.equal(r.actual.walks.length,67);assert(r.actual.walks.every(w=>w.status==='unknown'&&w.issues.some(i=>i.code==='missing-frame-transport')));
 assert.equal(r.flatControl.status,'verified');assert.equal(r.twistedControl.status,'refuted');assert(r.twistedControl.walks.some(w=>w.id.startsWith('local-comparison:')&&w.status==='refuted'));assert(!r.twistedControl.walks.some(w=>w.issues.some(i=>i.code==='reverse-transport-not-inverse')));
});
test('explicit identity transports make alternative paths coherent, not unique',()=>{
 const b=build();for(const e of b.topology.edges)e.transport=structuredClone(I);const r=buildNeutronCoherence(b);assert.equal(auditFrameReturn(r.topology).status,'verified');assert.equal(r.localComparisons.length,8);
 const missing=structuredClone(r.topology);delete missing.edges.find(e=>e.id===r.localComparisons[0].paths[0][0]).transport;assert.equal(auditFrameReturn(missing).status,'unknown');
});
test('a local support twist is observed in an actual supplied connection',()=>{
 const b=build();for(const e of b.topology.edges)e.transport=structuredClone(I);const first=buildNeutronCoherence(b).localComparisons[0].paths[0][0],e=b.topology.edges.find(e=>e.id===first),inverse=b.topology.edges.find(r=>r.id===e.reverse);
 e.transport=[[0,-1,0],[1,0,0],[0,0,1]];inverse.transport=[[0,1,0],[-1,0,0],[0,0,1]];
 const result=auditFrameReturn(buildNeutronCoherence(b).topology);assert.equal(result.status,'refuted');assert(result.walks.find(w=>w.id==='local-comparison:0:1').issues.some(i=>i.code==='frame-does-not-return'));
});
test('incomplete attachments and missing reverses cannot receive complete coherence coverage',()=>{
 const b=build();b.topology.edges=b.topology.edges.filter(e=>e.kind!=='neutron-space-contact');assert.throws(()=>buildNeutronCoherence(b),/blocked transfers/);
 const bad=build();bad.topology.edges.pop();assert.throws(()=>buildNeutronCoherence(bad),/Invalid reverse interface/);
 const restricted=build();restricted.topology.turns=[];assert.throws(()=>buildNeutronCoherence(restricted),/cannot discard routing restrictions/);
});
test('path enumeration limits fail explicitly rather than truncate alternative paths',()=>{
 assert.throws(()=>buildNeutronCoherence(build(),{maxPathsPerPair:1}),/integer >= 2/);assert.equal(buildNeutronCoherence(build(),{maxPathsPerPair:2}).localComparisons.length,8);
 const b=build();b.topology.edges.push(...b.topology.edges.filter(e=>e.kind==='neutron-space-contact').map(e=>({...e,id:e.id+':extra',reverse:e.reverse+':extra',support:e.support+':extra'})));assert.throws(()=>buildNeutronCoherence(b,{maxPathsPerPair:2}),/Path enumeration limit exceeded/);
});
