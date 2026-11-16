import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {auditChannelTransport,bindChannelTransport,compareDirectAndMediatedTransport} from '../examples/isotope-wiring/core/channel-frame-transport.mjs';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedFullInterface} from '../examples/isotope-wiring/core/stacked-full-interface.mjs';
const A=[[1,0,0],[0,0,-1],[0,1,0]],B=[[0,-1,0],[1,0,0],[0,0,1]],R=[[0,0,1],[1,0,0],[0,1,0]],H=[[0,0,1],[0,1,0],[-1,0,0]],wrong=[[0,-1,0],[0,0,-1],[1,0,0]],I=[[1,0,0],[0,1,0],[0,0,1]];
const tr=a=>a[0].map((_,i)=>a.map(r=>r[i]));
test('noncommuting segment transports compose in traversal order and reverse in opposite order',()=>{
 const r=auditChannelTransport([A,B]);assert.equal(r.status,'verified');assert.deepEqual(r.forwardTransport,R);assert.deepEqual(r.reverseTransport,tr(R));assert.equal(auditChannelTransport([A,B],{reverse:[tr(B),tr(A)]}).status,'verified');assert.equal(auditChannelTransport([A,B],{reverse:[tr(A),tr(B)]}).status,'refuted');
});
test('individually reversible channels can disagree on endpoint action',()=>{
 const r=compareDirectAndMediatedTransport({direct:wrong,entry:A,exit:B});assert.equal(r.direct.status,'verified');assert.equal(r.mediated.status,'verified');assert.equal(r.status,'refuted');assert(r.endpointError>0);assert.equal(compareDirectAndMediatedTransport({direct:R,entry:A,exit:B}).status,'verified');
});
test('changing only the intermediate frame preserves external endpoint action',()=>{
 const r=compareDirectAndMediatedTransport({direct:R,entry:A,exit:B,intermediateGauge:H});assert.equal(r.status,'verified');assert.equal(r.gauge.status,'verified');assert.notDeepEqual(r.gauge.entry,A);assert.notDeepEqual(r.gauge.exit,B);assert.deepEqual(auditChannelTransport([r.gauge.entry,r.gauge.exit]).forwardTransport,R);
});
test('missing transport remains unknown; malformed rotations and bad inverses fail',()=>{
 assert.equal(compareDirectAndMediatedTransport().status,'unknown');assert.equal(auditChannelTransport([A,undefined]).status,'unknown');assert.equal(auditChannelTransport([[[1,0,0],[0,1,0],[0,0,-1]]]).status,'refuted');assert.equal(auditChannelTransport([[[1]]]).status,'refuted');assert.equal(auditChannelTransport([A],{reverse:[I]}).status,'refuted');assert.throws(()=>auditChannelTransport([]),/at least one/);assert.throws(()=>auditChannelTransport([A],{reverse:[]}),/equal length/);
});
test('assignment changes only channel segments, not the model or unprovided neutral transports',()=>{
 const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),model=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true}));
 for(const mode of ['direct','neutron-mediated']){const f=buildStackedFullInterface(model,{mode}),before=JSON.stringify(f),values=mode==='direct'?[R]:[A,B],r=bindChannelTransport(f,values);assert.equal(r.status,'verified');assert.equal(JSON.stringify(f),before);assert.equal(r.topology.edges.filter(e=>e.transport!==undefined).length,2*values.length);assert(r.topology.edges.filter(e=>e.kind!=='stacked-interface').every(e=>e.transport===undefined));assert.equal(bindChannelTransport(f,values.map(()=>undefined)).status,'unknown');assert.throws(()=>bindChannelTransport(f,[]),/count must match/);}
});
