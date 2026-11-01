import {test} from 'node:test';
import assert from 'node:assert/strict';
import {compileStateSpecification,searchEventStates,replayEventTrace,applyEventOperation,initialEventState} from '../research/realization-tower/cellulation-state-search.mjs';
function toy(conflict=false){return {schema:'cellulation-event-state-v1',initial:{dots:[],arrows:[],faces:[],cells:[]},targets:['A','B'],cells:['A','B'].map(id=>({id,vertices:conflict?['p']:[],faces:[]})),programs:['A','B'].map((id,i)=>({id,cell:id,operations:[{id,requires:[],effects:conflict?[{type:'propose',key:'p',colour:i,normal:[0,1,0]},{type:'solidify',key:'p'},{type:'commit'}]:[{type:'arrow',key:id},{type:'commit'}]}]}))};}
test('exhaustive state enumeration closes commuting diamonds without hiding alternative paths',()=>{
 const c=compileStateSpecification(toy()),r=searchEventStates(c);assert.equal(r.coverage,'complete');assert.equal(r.result,'verified-for-frozen-model');assert.equal(r.visitedStates,4);assert.equal(r.exploredTransitions,4);assert.equal(r.distinctTerminalOutcomes,1);assert.equal(r.completeScheduleCount,'2');
});
test('first-writer conflict and BOTH competing claims survive state canonicalization',()=>{
 const c=compileStateSpecification(toy(true)),r=searchEventStates(c);assert.equal(r.coverage,'complete');assert.equal(r.result,'counterexample-found');assert.equal(r.visitedStates,5);assert.equal(r.distinctTerminalOutcomes,2);
 const witness=r.counterexamples[0],a=replayEventTrace(c,witness.leftTrace),b=replayEventTrace(c,witness.rightTrace);
 assert.notEqual(a.dots.get('p').colour,b.dots.get('p').colour);assert.deepEqual(a.dots.get('p').claims,b.dots.get('p').claims);assert.equal(a.dots.get('p').claims.length,2);
});
test('limits never pass, and replayed guides provide no coverage credit',()=>{
 const c=compileStateSpecification(toy(true));assert.equal(searchEventStates(c,{maxStates:1}).result,'incomplete');
 const r=searchEventStates(c,{maxStates:1,guideTraces:[{name:'left',trace:['A','B']},{name:'right',trace:['B','A']}]});assert.equal(r.result,'counterexample-found');assert.equal(r.coverage,'incomplete');assert.equal(r.visitedStates,1);assert.equal(r.stopReason,'state-limit');
 assert.throws(()=>searchEventStates(c,{maxStates:0}));assert.throws(()=>replayEventTrace(c,['A']));assert.throws(()=>applyEventOperation(c,replayEventTrace(c,['A'],{requireComplete:false}),'A'));
});
test('missing source gates produce a replayable deadlock, rather than a successful terminal state',()=>{
 const spec=toy();for(const p of spec.programs)p.operations[0].requiresSolid=['missing'];const c=compileStateSpecification(spec),r=searchEventStates(c);
 assert.equal(r.result,'counterexample-found');assert.equal(r.coverage,'complete');assert.equal(r.deadlocks.length,1);assert.deepEqual(r.deadlocks[0].missingCells,['A','B']);assert.throws(()=>applyEventOperation(c,initialEventState(c),'A'));
});
test('compiled specifications are immutable snapshots, not mutable caller inputs',()=>{
 const spec=toy(),c=compileStateSpecification(spec);spec.programs[0].operations[0].effects[0].key='changed';assert(replayEventTrace(c,['A','B']).arrows.has('A'));assert.throws(()=>{c.spec.programs[0].operations[0].effects[0].key='changed';});
});
test('cyclic or nonexistent prerequisite identities are rejected',()=>{
 const spec=toy();spec.programs[0].operations[0].requires=['B'];spec.programs[1].operations[0].requires=['A'];assert.throws(()=>compileStateSpecification(spec),/Cyclic/);
 spec.programs[1].operations[0].requires=['unknown'];assert.throws(()=>compileStateSpecification(spec),/Unknown prerequisite/);
});
