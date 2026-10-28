import test from 'node:test';
import assert from 'node:assert/strict';
import {previewPathRules} from '../research/realization-tower/path-rule-preview.mjs';
import {doubleEsd7Process} from '../research/realization-tower/double-esd7-process.mjs';
test('closure alternates N/P along matching wires only and deduplicates arrivals',()=>{
 const input={bodies:[{id:'a',role:'neutron'}],states:[{node:'a',front:'+P',suffix:'PN'}],wires:[{from:'a',to:'b',direction:'P'},{from:'b',to:'c',direction:'+N'},{from:'b',to:'c',direction:'−N'},{from:'b',to:'e',direction:'E'},{from:'c',to:'d',direction:'P'}]};
 const before=structuredClone(input),r=previewPathRules(input);assert.deepEqual(input,before);assert.equal(r.valid,true);
 assert.deepEqual(r.candidates.map(c=>[c.id,c.role]),[['b','proton'],['c','neutron'],['d','proton']]);assert.equal(r.rounds.length,3);
 const second=previewPathRules({...input,bodies:[...input.bodies,...r.candidates]});assert.equal(second.candidates.length,0);
});
test('wrong suffix and E wires do not fire; cycles terminate',()=>{
 const r=previewPathRules({bodies:[{id:'a',role:'proton'}],states:[{node:'a',front:'x',suffix:'PP'}],wires:[{from:'a',to:'a',direction:'P'},{from:'a',to:'b',direction:'+N'}]});assert.equal(r.candidates.length,0);
});
test('opposing proposals or existing colours are reported, never overwritten',()=>{
 for(const bodies of [[{id:'c',role:'electron'}],[]]){
  const r=previewPathRules({bodies,states:[{node:'a',front:'+',suffix:'PN'},{node:'b',front:'−',suffix:'NP'}],wires:[{from:'a',to:'c',direction:'P'},{from:'b',to:'c',direction:'+N'}]});assert.equal(r.valid,false);assert.equal(r.conflicts.length,1);assert.equal(r.candidates.length,0);
 }
});
test('seam transports every colour and preserves NP history for continuation',()=>{
 for(const [suffix,role] of [['NP','proton'],['PN','neutron'],['PE','electron']]){
  const r=previewPathRules({bodies:[{id:'a',role}],states:[{node:'a',front:'+P',suffix}],interfaces:[{from:'a',to:'b'},{from:'b',to:'a'}],wires:[{from:'b',to:'c',direction:'+N'}]});
  assert.equal(r.valid,true);assert.equal(r.candidates.find(c=>c.id==='b').role,role);
  assert.equal(r.interfaceIdentifications[0].suffix,suffix);
  assert.equal(r.interfaceIdentifications[0].pOrientation,-1);
  assert.equal(r.candidates.find(c=>c.id==='b').round,0);
  if(suffix==='NP')assert.equal(r.candidates.find(c=>c.id==='c').round,1);
  assert.equal(r.candidates.some(c=>c.id==='c'),suffix==='NP');
 }
 const conflict=previewPathRules({bodies:[{id:'a',role:'electron'},{id:'b',role:'proton'}],states:[{node:'a',front:'x',suffix:'PE'}],wires:[],interfaces:[{from:'a',to:'b'}]});assert.equal(conflict.valid,false);
});
test('extended rules produce correct roles and suffixes for all directed inputs',()=>{
 for(const [suffix,direction,role,next] of [['PE','P','neutron','EN'],['PN','E','electron','NE'],['PN','+N','electron','NE'],['PN','−N','electron','NE']]){
  const r=previewPathRules({bodies:[],states:[{node:'a',front:'x',suffix}],wires:[{from:'a',to:'b',direction}],extended:true});
  assert.equal(r.valid,true);assert.equal(r.candidates[0].role,role);assert.equal(r.candidates[0].arrivals[0].suffix,next);
 }
});
test('double ESD7 step four previews 124 unique additions without filling them',()=>{
 const p=doubleEsd7Process(7,4),r=p.doubleEsd7Audit.rulePreview;
 assert.equal(r.valid,true);assert.equal(r.candidates.length,124);assert.equal(r.rounds.length,8);assert.equal(new Set(r.candidates.map(c=>c.id)).size,124);
 assert.ok(r.candidates.every(c=>p.emptyBodies.some(b=>b.id===c.id)&&c.role!=='electron'));
 assert.equal(p.retainedBodies.length,38);assert.equal(p.emptyBodies.length,312);
});
