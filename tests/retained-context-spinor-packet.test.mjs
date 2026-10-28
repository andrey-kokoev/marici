import test from 'node:test';
import assert from 'node:assert/strict';
import {createRetainedContextMachine,splitCoordinates,joinCoordinates} from '../research/strominger/retained-context-spinor-packet.mjs';
import {GenerativeAssemblyRules} from '../research/nima/generative-phase-assembly.mjs';
const value=[[1,2],[-3,4],[5,-6],[7,8],[-9,10]],norm=v=>v.flat().reduce((s,x)=>s+x*x,0);
const near=(a,b)=>assert(Math.hypot(...a.flat().map((x,i)=>x-b.flat()[i]))<1e-10);
function choose(m,p,kind){const op=m.choices(p).find(o=>o.kind===kind);assert(op,`Missing ${kind}`);return m.step(p,op);}
test('all species retain the full five-vector, including zero-contrast context',()=>{
 for(const species of ['proton','neutron','electron']){
  const p=splitCoordinates(species,value);near(joinCoordinates(species,p),value);
  assert(Math.abs(norm(p.contrast)+norm([p.context.mean,...p.context.outside.map(x=>x.value)])-norm(value))<1e-10);
  const bad=structuredClone(p);delete bad.context;assert.throws(()=>joinCoordinates(species,bad),/context/);
 }
 const p=splitCoordinates('neutron',[[0,0],[0,0],[0,0],[0,0],[1,0]]);assert.equal(p.pairedFrame,null);assert.equal(norm(joinCoordinates('neutron',p)),1);
});
test('actual N advance moves retained context into contrast without inventing a zero-state ray',()=>{
 const m=createRetainedContextMachine([[0,0],[0,0],[0,0],[0,0],[1,0]]),n=choose(m,m.initial(),'PN');
 assert.equal(n.coordinates.pairedFrame,null);
 const next=choose(m,n,'reader-phase-advance');assert(Math.abs(next.coordinates.contrastNormSquared-2/3)<1e-10);
 assert.equal(next.native.origin,n.native.origin+1);assert(next.history.at(-1).phaseWitness.referenceContext);
 assert.equal(norm(m.decode(next)),1);near(next.movingFrame.rootCoordinates,n.movingFrame.rootCoordinates);
});
test('two coefficient-periodic advances retain different origins and histories',()=>{
 const m=createRetainedContextMachine(value),p=m.initial(),p2=choose(m,choose(m,p,'reader-phase-advance'),'reader-phase-advance');
 assert.deepEqual(m.decode(p2),m.decode(p));assert.equal(p2.native.origin,2);assert.equal(p2.history.length,2);
 assert.notEqual(m.serialize(p2),m.serialize(p));const bad=structuredClone(p2);bad.history=[];assert.throws(()=>m.validate(bad),/replay/);
});
test('even a native PN/inverse-PN round trip retains a distinct history commitment',()=>{
 const m=createRetainedContextMachine(value),root=m.initial(),back=choose(m,choose(m,root,'PN'),'inverse-PN');
 assert.deepEqual(back.native,root.native);assert.deepEqual(m.decode(back),m.decode(root));assert.notEqual(back.historyCommitment,root.historyCommitment);
 const erased=structuredClone(back);erased.history=[];assert.throws(()=>m.validate(erased),/replay/);
});
test('serialization replays against fresh geometry and rejects corrupted records',()=>{
 const m=createRetainedContextMachine(value),p=choose(m,choose(m,m.initial(),'PN'),'reader-phase-advance'),fresh=createRetainedContextMachine(value,{rules:new GenerativeAssemblyRules()});
 assert.deepEqual(fresh.restore(m.serialize(p)),p);
 for(const mutate of [p=>delete p.coordinates.context,p=>p.coordinates.contrast[0][0]++,p=>p.native.origin++,p=>p.history[0].face.pop(),p=>p.history.at(-1).phaseWitness.referenceContext.to.index++,p=>p.movingFrame.currentSlotsForRootCoordinates.reverse()]){
  const bad=structuredClone(p);mutate(bad);assert.throws(()=>fresh.validate(bad));
 }
 const wrong=createRetainedContextMachine(value.map(z=>[...z].reverse()));assert.throws(()=>wrong.restore(m.serialize(p)),/source/);
});
test('no inverse electron operation or arbitrary phase operation is admitted',()=>{
 const m=createRetainedContextMachine(value),e=choose(m,choose(m,m.initial(),'PN'),'NE');assert.deepEqual(m.choices(e),[]);
 assert.throws(()=>m.step(e,{kind:'inverse-NE'}),/not admitted/);assert.throws(()=>m.step(e,{kind:'phase-correction'}),/not admitted/);
});
test('bounded native paths preserve coefficients, contexts and source anchoring',()=>{
 const m=createRetainedContextMachine(value),queue=[{packet:m.initial(),depth:0}],kinds=new Set();let checked=0;
 for(let i=0;i<queue.length;i++){
  const {packet,depth}=queue[i];assert(m.validate(packet));near(joinCoordinates(packet.native.species,packet.coordinates),m.decode(packet));assert.equal(norm(m.decode(packet)),norm(value));assert.deepEqual(packet.movingFrame.rootCoordinates,value);assert.deepEqual(m.restore(m.serialize(packet)),packet);checked++;
  if(depth<5)for(const op of m.choices(packet)){kinds.add(op.kind);queue.push({packet:m.step(packet,op),depth:depth+1});}
 }
 assert(checked>50);for(const kind of ['PN','NE','inverse-PN','NN-phase-advance','reader-phase-advance'])assert(kinds.has(kind));
});
