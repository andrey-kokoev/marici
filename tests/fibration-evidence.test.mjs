import test from 'node:test';import assert from 'node:assert/strict';
import {boundary,composeEvidence} from '../research/strominger/fibration-evidence.mjs';
const record=(id='group')=>({id,adapter:'marked-table',input:boundary('marked-table',{rows:[]}),output:boundary('marked-source-fibers',{groups:[]}),dependsOn:[],premises:[],claim:'Finite marked recovery',checks:[{id:'restore',passed:true}]});
test('evidence checks exact boundary identity and registered carrier contracts',()=>{
 const a=record(),b={...record('unpack'),input:a.output,output:a.input,dependsOn:[a.id]},links=[{from:a.id,to:b.id}];assert.equal(composeEvidence([a,b],links).status,'verified');
 b.input=boundary('marked-source-fibers',{groups:['different']});assert.ok(composeEvidence([a,b],links).failures.some(f=>f.category==='boundary-mismatch'));
 b.input=boundary('scalar-total',{});assert.ok(composeEvidence([b]).failures.some(f=>f.category==='adapter-type-mismatch'));
 b.adapter='invented';assert.ok(composeEvidence([b]).failures.some(f=>f.category==='unsupported-adapter'));
});
test('assumptions and missing premises cannot become unconditional conclusions',()=>{
 const a=record(),b={...record('unpack'),input:a.output,output:a.input,dependsOn:[a.id]},links=[{from:a.id,to:b.id}];a.premises=[{id:'wiring',status:'assumed',statement:'reverse convention'}];
 let r=composeEvidence([a,b],links);assert.equal(r.status,'verified-conditionally');assert.equal(r.assumptions.length,1);
 b.premises=[{id:'native-binding',status:'missing',statement:'native window adapter'}];r=composeEvidence([a,b],links);assert.equal(r.status,'incomplete');assert.equal(r.assumptions.length,1);assert.equal(r.missing.length,1);
 b.premises=[{id:'wiring',status:'missing',statement:'different meaning'}];assert.ok(composeEvidence([a,b],links).failures.some(f=>f.category==='conflicting-premise'));
});
test('nonlinear evidence dependencies, missing witnesses and cycles are checked',()=>{
 const a=record('a'),b=record('b'),c=record('c');b.dependsOn=['a'];c.dependsOn=['a','b'];assert.equal(composeEvidence([a,b,c]).status,'verified');
 a.dependsOn=['c'];assert.ok(composeEvidence([a,b,c]).failures.some(f=>f.category==='cyclic-evidence'));a.dependsOn=['missing'];assert.ok(composeEvidence([a,b,c]).failures.some(f=>f.category==='missing-evidence'));
 a.dependsOn=[];a.checks[0].passed=false;assert.equal(composeEvidence([a]).status,'rejected');assert.equal(composeEvidence([a,a]).status,'rejected');
});
test('boundary identity ignores object key insertion order but never silently erases unsupported values',()=>{
 assert.deepEqual(boundary('packet',{a:1,b:{c:2,d:3}}),boundary('packet',{b:{d:3,c:2},a:1}));assert.notDeepEqual(boundary('packet',[1,2]),boundary('packet',[2,1]));
 for(const value of [{x:undefined},{x:NaN},{x:()=>1},{x:1n}])assert.throws(()=>boundary('packet',value));
});
test('malformed evidence is rejected rather than accepted as a vacuous pass',()=>{
 for(const records of [null,[],[null],[{id:'fake'}],[{...record(),checks:[]}],[{...record(),premises:[null]}]])assert.equal(composeEvidence(records).status,'rejected');
 assert.equal(composeEvidence([record()],[null]).status,'rejected');
});
