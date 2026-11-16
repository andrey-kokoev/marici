import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedFullInterface} from '../examples/isotope-wiring/core/stacked-full-interface.mjs';
import {studyTetrahedralContact} from '../examples/isotope-wiring/core/tetrahedral-contact-trial.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),b=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true})),full=buildStackedFullInterface(b);
const near=(a,b)=>Math.abs(a-b)<1e-9;
test('candidate regular tetrahedra meet at exactly the declared contact',()=>{
 for(const sourceDepth of [1,-1])for(const targetDepth of [1,-1]){const r=studyTetrahedralContact(full,{sourceDepth,targetDepth}),{source,target}=r.embedding;assert.deepEqual(source.B,target.T);
  for(const cell of [source,target]){const points=Object.values(cell);for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)assert(near(Math.hypot(...points[i].map((x,k)=>x-points[j][k])),2));}
  assert(Object.values(source).every(v=>v[1]<=1));assert(Object.values(target).every(v=>v[1]>=1));
 }
});
test('PE marker ports come from declared circulation rather than invented screen routing',()=>{
 const r=studyTetrahedralContact(full);assert.equal(r.sourceMarker.pair,'s1-00-lower');assert.equal(r.targetMarker.pair,'s2-01-upper');assert.equal(r.sourceMarker.port,'R');assert.equal(r.targetMarker.port,'R');assert.equal(studyTetrahedralContact(full,{targetLeg:'incoming'}).targetMarker.port,'L');
 const trace=r.alignment.rotation.reduce((sum,row,i)=>sum+row[i],0);assert(near((trace-1)/2,1/3));assert.equal(r.channelAudit.status,'verified');assert.equal(r.status,'conditional');
});
test('same projected contact admits different frame matrices under unselected depth and marker choices',()=>{
 const trials=[];for(const sourceDepth of [1,-1])for(const targetDepth of [1,-1])for(const targetLeg of ['outgoing','incoming'])trials.push(studyTetrahedralContact(full,{sourceDepth,targetDepth,targetLeg}));
 const projection=r=>JSON.stringify([r.embedding.source,r.embedding.target].map(cell=>Object.values(cell).map(v=>v.slice(0,2))));assert.equal(new Set(trials.map(projection)).size,1);
 const matrix=r=>JSON.stringify(r.alignment.rotation.map(row=>row.map(x=>Math.round(x*1e9)/1e9)));assert.equal(new Set(trials.map(matrix)).size,8);assert(trials.every(r=>r.channelAudit.status==='verified'));
});
test('metric height is an explicit hypothesis and does not modify the isotope',()=>{
 const before=JSON.stringify(full),regular=studyTetrahedralContact(full),changed=studyTetrahedralContact(full,{height:0.3});assert.notDeepEqual(regular.alignment.rotation,changed.alignment.rotation);assert.equal(JSON.stringify(full),before);assert(full.model.topology.edges.every(e=>e.transport===undefined));
});
test('unsupported geometry is rejected rather than defaulted',()=>{
 assert.throws(()=>studyTetrahedralContact(full,{height:0}),/Height/);assert.throws(()=>studyTetrahedralContact(full,{sourceDepth:0}),/Depth order/);assert.throws(()=>studyTetrahedralContact(full,{targetLeg:'nearest'}),/Unknown PE/);assert.throws(()=>studyTetrahedralContact(buildStackedFullInterface(b,{mode:'neutron-mediated'})),/mediator pose/);
});
