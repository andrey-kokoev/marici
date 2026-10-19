import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {createDeuteriumTunnel,identityBoundaryHypothesis,transportCycleBoundaryCoefficients,transportCarrierCoefficients,isTypedWindowOrder} from '../demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs';
assert.throws(()=>createDeuteriumTunnel({realizationCycles:2}));
const ordinary=createDeuteriumTunnel();ordinary.step();ordinary.step();assert.equal(ordinary.crossCycle(1).crossed,false);
let final;
for(const branch of ['common','positive','negative']){
 const run=createDeuteriumTunnel({branch,complementCoefficients:[[9,-7],[-5,6]],realizationCycles:2,boundaryIdentification:identityBoundaryHypothesis}),input=run.snapshot();
 assert.equal(run.crossCycle(1).crossed,false);run.step();run.step();const built=run.snapshot();
 assert.equal(run.crossCycle(-1).crossed,false);const next=run.crossCycle(1);assert.equal(next.crossed,true);assert.equal(next.tunnel.realizations.cycle,1);assert.equal(next.tunnel.position,0);assert.deepEqual(next.tunnel.referenceCarrier,input.tunnel.referenceCarrier);assert.equal(next.tunnel.passages.length,0,'Boundary crossing is not logged as spatial backtracking');
 run.pass(1);run.pass(1);assert.equal(run.snapshot().tunnel.realizations.observedStates.length,6);assert.equal(run.crossCycle(1).crossed,false);
 run.pass(-1);run.pass(-1);assert.equal(run.crossCycle(-1).crossed,true);run.pass(-1);run.pass(-1);final=run.snapshot();
 assert.deepEqual(final.tunnel.referenceCarrier,input.tunnel.referenceCarrier);assert.deepEqual(final.tunnel.mode,input.tunnel.mode);assert.deepEqual(final.items,built.items);assert.deepEqual(final.bindings,built.bindings);assert.deepEqual(final.history,built.history);assert.equal(final.identity,input.identity);assert.equal(final.tunnel.realizations.boundaryPassages.length,2);assert.equal(final.events.length,2);
 const payload=built.tunnel.referenceCarrier.coefficients,events=built.events;
 const a=[...events].reverse().reduce((c,e)=>transportCarrierCoefficients(c,e,-1),payload),b=events.reduce((c,e)=>transportCarrierCoefficients(c,e,-1),payload);assert.deepEqual(a,b);
 assert.equal(isTypedWindowOrder('electron',[...events].reverse(),-1),true);assert.equal(isTypedWindowOrder('electron',events,-1),false,'Commuting frame factors do not admit a second particle branch');
 // A different fifth-slot phase also round-trips: reversibility alone cannot
 // identify the physical boundary map. Keep the nonzero fifth coefficient.
 const twist=c=>c.map((z,i)=>i===4?z.map(x=>-x):[...z]),alternative=twist(a);
 assert.notDeepEqual(alternative,a);assert.deepEqual(transportCycleBoundaryCoefficients(twist(alternative),events,-1),payload);
}
const out='research/strominger/results/deuterium-cycles';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'pass-conditional-two-cycle-trial',hypothesis:identityBoundaryHypothesis,physicalBoundaryDerived:false,realizationStatesVisited:final.tunnel.realizations.observedStates.length,fullCarrierRoundTrip:true,nonzeroComplementRetained:true,spatialGeometryUnchanged:true,commutingFrameOrdersAgree:true,reorderedParticleBranchRejected:true,alternativeFifthSlotGluingAlsoInvertible:true},null,2)+'\n');console.log('PASS conditional two-cycle transport; frame reordering is not a particle branch; physical gluing remains undetermined');
