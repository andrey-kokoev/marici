import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
import {renderedCellulationWitnessInput} from '../examples/normal-ray/cellulation-loop-validation.js';
import {freezeShellEventSpecification,validateShellEventSpecification,shellGuideTrace} from '../research/realization-tower/cellulation-shell-exhaustive-spec.mjs';
import {compileStateSpecification,replayEventTrace,freezeEventPrefix,searchEventStates,eventStateOutcome,eventOutcomeDifferences} from '../research/realization-tower/cellulation-state-search.mjs';
const base=buildCellulationStep(22),root=createCellulation(base);root.userData.animate(Infinity,{});
const input=renderedCellulationWitnessInput(root),spec=freezeShellEventSpecification(base,input),compiled=compileStateSpecification(spec),guide=shellGuideTrace(base,input);

test('the frozen full model contains every shell target and alternative shared-cell construction mode',()=>{
 assert.equal(spec.targets.length,110);assert.equal(spec.programs.length,120);assert.equal(compiled.operations.length,1440);assert.equal(guide.trace.length,1350);assert(validateShellEventSpecification(spec));
 const state=replayEventTrace(compiled,guide.trace);assert.equal(state.cells.size,174);
 const rendered=createCellulation(buildCellulationStep(26));rendered.userData.animate(Infinity,{});const actual=renderedCellulationWitnessInput(rendered),point=p=>p.map(x=>Math.round(x*Math.SQRT2)).join(',');
 assert.deepEqual([...state.arrows].sort(),[...new Set(actual.arrows.map(a=>`${point(a.from)}>${point(a.to)}:${a.colour??a.color}`))].sort());
 assert.deepEqual([...state.cells].sort(),actual.cells.map(c=>c.id).sort());
 for(const f of guide.finalState.faces){const key=f.vertices.map(point).sort().join('|'),record=state.faces.get(key);assert(record);assert.equal(record.colour,f.colour);assert.equal(record.source,f.source);}
 assert.equal(state.dots.size,actual.anchors.length);
 for(const a of actual.anchors){const d=state.dots.get(point(a.point));assert(d);assert.equal(d.id,a.id);assert.equal(d.colour,a.colour);const length=Math.hypot(...d.normal);assert(a.normal.every((x,i)=>Math.abs(x-d.normal[i]/length)<1e-8));assert.equal(d.solid,a.solid);}
});
test('all event interleavings of the two-cell fork are exhausted, yielding exactly two readouts at 422',()=>{
 const prefix=replayEventTrace(compiled,guide.trace.slice(0,15),{requireComplete:false}),local=freezeEventPrefix(compiled,prefix,['face:0/shell:t:3,1,2','face:0/shell:t:3,2,1']);validateShellEventSpecification(local);
 const c=compileStateSpecification(local),r=searchEventStates(c,{maxStates:2000,maxMilliseconds:30000});assert.equal(r.coverage,'complete');assert.equal(r.result,'counterexample-found');assert.equal(r.visitedStates,406);assert.equal(r.completeScheduleCount,'155117520');assert.equal(r.distinctTerminalOutcomes,2);assert.equal(r.deadlocks.length,0);
 const counter=r.counterexamples[0],left=replayEventTrace(c,counter.leftTrace),right=replayEventTrace(c,counter.rightTrace);assert.equal(counter.leftTrace.length,30);assert.equal(counter.rightTrace.length,30);
 assert.deepEqual(new Set([left.dots.get('4,2,2').colour,right.dots.get('4,2,2').colour]),new Set([0xff3030,0xffffff]));assert.equal(left.dots.get('4,2,2').claims.length,2);assert.deepEqual(left.dots.get('4,2,2').claims,right.dots.get('4,2,2').claims);
});
test('all four-arrival orders in a fixed supported octahedron exhaust to one result',()=>{
 const start=guide.trace.findIndex(id=>id.startsWith('face:0/shell:o:')),program=guide.trace[start].split('/action:')[0],prefix=replayEventTrace(compiled,guide.trace.slice(0,start),{requireComplete:false});
 const local=freezeEventPrefix(compiled,prefix,[program]);validateShellEventSpecification(local);const r=searchEventStates(compileStateSpecification(local));assert.equal(r.coverage,'complete');assert.equal(r.result,'verified-for-frozen-model');assert.equal(r.visitedStates,21);assert.equal(r.completeScheduleCount,'24');assert.equal(r.distinctTerminalOutcomes,1);
});
test('prefix extraction cannot silently discard a partially started cell or select nonexistent continuations',()=>{
 const partial=replayEventTrace(compiled,guide.trace.slice(0,1),{requireComplete:false});assert.throws(()=>freezeEventPrefix(compiled,partial,['face:0/shell:t:3,1,2']),/completed-cell/);
 const completed=replayEventTrace(compiled,guide.trace.slice(0,15),{requireComplete:false});assert.throws(()=>freezeEventPrefix(compiled,completed,['nonexistent']),/Unknown/);
});
test('both previously found global failures replay under the independent event model',()=>{
 const a=eventStateOutcome(compiled,replayEventTrace(compiled,guide.trace));
 for(const [options,field] of [[{swapFirstFaceCells:true},'dots'],[{faceOrder:[0,2,1,3]},'arrows']]){const trace=shellGuideTrace(base,input,options).trace,b=eventStateOutcome(compiled,replayEventTrace(compiled,trace));assert(eventOutcomeDifferences(a,b).some(d=>d.field===field));}
});
test('hostile frozen protocols cannot drop return gates, invent arrival serialization, reverse arrows or change normals',()=>{
 for(const mutate of [s=>s.programs[0].operations[4].requires=[],s=>s.programs[0].operations[0].requires.push(s.programs[1].operations.at(-1).id),s=>s.programs[0].operations[0].effects.push({type:'commit'}),s=>{const p=s.programs.find(p=>p.kind==='octahedron');p.operations[2].requires.push(p.operations[1].id);},s=>{const e=s.programs[0].operations[2].effects.find(e=>e.type==='arrow');const [ends,color]=e.key.split(':');e.key=ends.split('>').reverse().join('>')+':'+color;},s=>s.programs[0].operations[0].effects[0].normal=[0,0,1]]){const changed=structuredClone(spec);mutate(changed);assert.throws(()=>validateShellEventSpecification(changed));}
});
