import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {constructRetainedCarrier,retainedPbProcess,retainedPbStages} from '../research/realization-tower/retained-pb-process.mjs';
import {assembleComponents} from '../research/strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs';
import {processes} from '../research/realization-tower/normal-ray-processes.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
test('Process 4 starts with one central seed, not the completed target',()=>{
 const p=retainedPbProcess(7,0);
 assert.equal(p.retainedBodies.length,1);assert.equal(p.retainedAudit.primitiveComponents,1);
 assert.deepEqual(p.retainedBodies[0].vertices,[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]);
 assert.equal(p.retainedContacts.length,0);assert.equal(p.canAdvance,true);
 assert.ok(processes.some(p=>p.id==='retained-construction'));
 const source=readFileSync(new URL('../research/realization-tower/retained-pb-process.mjs',import.meta.url),'utf8');
 assert.ok(!source.includes('lead208-model'));assert.ok(!source.includes('assembleComponents('));
});
test('each step only adds attached cells; old coordinates and identities never mutate',()=>{
 for(let s=1;s<retainedPbStages.length;s++){
  const before=retainedPbProcess(7,s-1),after=retainedPbProcess(7,s),old=new Map(before.retainedBodies.map(b=>[b.id,b]));
  assert.ok(after.retainedBodies.length>old.size);
  for(const body of after.retainedBodies){
   if(old.has(body.id))assert.deepEqual(body,old.get(body.id));
   else {assert.ok(body.parents.length>0);for(const p of body.parents){assert.ok(old.has(p.id));assert.ok(body.faces.some(f=>key(f)===p.face));assert.ok(old.get(p.id).faces.some(f=>key(f)===p.face));}}
  }
  assert.equal(new Set(after.retainedBodies.map(b=>b.id)).size,after.retainedBodies.length);
  assert.deepEqual(retainedPbProcess(7,s-1),before);
 }
});
test('four seed faces start four branches; all shared contacts retained without traversal selection',()=>{
 const first=retainedPbProcess(7,1);assert.equal(first.retainedBodies.length,5);
 assert.deepEqual(first.retainedBodies.slice(1).flatMap(b=>b.branches).sort(),[1,2,3,4]);
 const a=constructRetainedCarrier(),b=constructRetainedCarrier({reverse:true});assert.deepEqual(a,b);
 assert.ok(a.bodies.some(b=>b.branches.length>1));
 assert.equal(new Set(a.contacts.map(c=>c.face)).size,a.contacts.length);
});
test('generated geometry matches independent esd7 target only in the test, with no species claim',()=>{
 const p=retainedPbProcess(7,retainedPbStages.length-1),target=assembleComponents();
 assert.deepEqual(p.retainedBodies.flatMap(b=>b.components).map(key).sort(),target.components.map(c=>key(c.addresses)).sort());
 assert.equal(p.retainedAudit.bodyCount,175);assert.equal(p.retainedAudit.primitiveComponents,343);
 assert.equal(p.canAdvance,false);assert.equal(p.retainedAudit.envelopeComplete,true);
 for(const field of ['particleRolesAssigned','nativeWitnessEstablished','isotopeFormationEstablished','full4x28Established'])assert.equal(p.retainedAudit[field],false);
 assert.equal(p.assignments.length,0);assert.throws(()=>retainedPbProcess(7,retainedPbStages.length));
});
test('new process namespace discards the old preassembled experiment progress',()=>{
 assert.equal(normalizeSceneSettings({process:{id:'retained-pb',k:7,step:6}}).process,null);
 const s=normalizeSceneSettings({process:{id:'retained-construction',k:2,step:100,progress:{'diamond-construction':{k:5,step:3}}}});
 assert.equal(s.process.k,7);assert.equal(s.process.step,retainedPbStages.length-1);
 assert.equal(s.process.progress['diamond-construction'].step,3);assert.deepEqual(normalizeSceneSettings(s),s);
});
