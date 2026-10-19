import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {createHelium3Tunnel,deriveHelium3Branch,sharedNeutronTransfer} from '../demos/particle-overlap-tetrahedron/helium3-tunnel-model.mjs';
import {createWindowConstruction} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
const cellKeys=lattice.cells.map(c=>itemKey(c.map(i=>lattice.nodes[i].address)));
const first=createWindowConstruction();first.step();const firstEnd=first.step(),plan=deriveHelium3Branch(firstEnd);
assert.equal(plan.rejected.length,1);assert.equal(new Set(plan.ports).size,4);
assert.equal(plan.packet.items[1].key,firstEnd.items[1].key);assert.notEqual(plan.packet.items[2].key,firstEnd.items[2].key);
assert.deepEqual(plan.initialMode,{branch:'negative',phaseExponent:1});
let example;
for(const branch of ['common','positive','negative'])for(const phaseExponent of [0,1,2]){
 const model=createHelium3Tunnel({branch,phaseExponent,complementCoefficients:[[9,-7],[-5,6]]}),initial=model.snapshot();
 assert.equal(model.crossCycle(1).crossed,false);assert.equal(model.pass(1).moved,false);
 for(let i=0;i<4;i++){
  const before=model.snapshot(),after=model.step();assert.equal(after.committed,true);assert.equal(after.items.length,before.items.length+1);assert.deepEqual(after.items.slice(0,-1),before.items);assert.equal(after.identity,initial.identity);
  for(const [n,p] of Object.entries(before.bindings))assert.deepEqual(after.bindings[n],p);
  assert.equal(after.tunnel.coverage.covered,after.items.length);assert.equal(new Set(after.items.map(s=>s.key)).size,after.items.length);
 }
 const end=model.snapshot();if(branch==='positive'&&phaseExponent===0)example=end;
 assert.deepEqual(end.counts,{proton:2,neutron:1,electron:2});assert.equal(end.items.filter(i=>i.species==='neutron').length,1);assert.equal(end.events.length,4);assert.equal(end.readEvents.length,1);assert.equal(end.readEvents[0].newGeometry,false);assert.equal(Object.keys(end.bindings).length,8);
 assert.equal(end.tunnel.coverage.complete,true);assert.equal(end.tunnel.realizations.observedStates.length,6);assert.ok(end.items.every(i=>cellKeys.includes(i.key)));assert.equal(model.ambientCoverage(cellKeys).coveredCells,5);
 const n0=end.tunnel.fiberStates.find(s=>s.id==='R0:1'),n1=end.tunnel.fiberStates.find(s=>s.id==='R1:1');assert.equal(n0.cell,n1.cell);assert.notDeepEqual(n0.window,n1.window);assert.deepEqual(sharedNeutronTransfer(n0.referenceCarrier),n1.referenceCarrier);
 const wrong=n1.referenceCarrier.map((z,i)=>i===4?z.map(x=>-x):[...z]);assert.deepEqual(wrong.slice(1,4),n1.referenceCarrier.slice(1,4));assert.notDeepEqual(wrong,n1.referenceCarrier,'The fifth coefficient must participate in gluing comparisons');
 // Same shared-N endpoint reached by the direct chart transition and by
 // N0 → E0 → (cycle boundary) → P1 → N1. Compare all five coefficients.
 model.pass(-1);model.crossCycle(-1);model.crossCycle(1);const direct=model.snapshot();
 model.crossCycle(-1);model.pass(1);model.crossCycle(1);const secondEntry=model.snapshot();
 if(branch!=='common')assert.notDeepEqual(secondEntry.tunnel.referenceCarrier.coefficients,initial.tunnel.referenceCarrier.coefficients,'Old canonical identity gluing does not fit the shared-neutron comparison');
 model.pass(1);const indirect=model.snapshot();assert.deepEqual(indirect.tunnel.referenceCarrier,direct.tunnel.referenceCarrier);assert.deepEqual(indirect.tunnel.mode,direct.tunnel.mode);assert.equal(indirect.tunnel.position,1);
 assert.deepEqual(indirect.items,end.items);assert.deepEqual(indirect.bindings,end.bindings);assert.deepEqual(indirect.history,end.history);assert.equal(indirect.identity,initial.identity);
 model.pass(-1);model.crossCycle(-1);model.pass(-1);model.pass(-1);const back=model.snapshot();assert.equal(back.tunnel.position,0);assert.deepEqual(back.tunnel.referenceCarrier.coefficients,initial.tunnel.referenceCarrier.coefficients);assert.deepEqual(back.tunnel.mode,initial.tunnel.mode);assert.deepEqual(back.items,end.items);assert.equal(model.step().committed,false);
}
// This is a branched spatial star, NOT a five-cell Hamiltonian spatial path.
const degrees=example.items.map((a,i)=>example.items.filter((b,j)=>i!==j&&a.faces.some(f=>b.faces.some(g=>itemKey(f)===itemKey(g)))).length);assert.deepEqual(degrees,[1,4,1,1,1]);
const out='research/strominger/results/helium3-tunnel';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'pass-reference-algebra-geometry-only',phaseDisciplineVerified:false,viewerMode:'legacy-model-not-displayed',counts:example.counts,cellIds:example.items.map(i=>cellKeys.indexOf(i.key)),bindings:example.bindings,sourceNeutronPorts:plan.ports,rejectedOrientation:plan.rejected,realizationWindows:example.tunnel.fiberStates.map(s=>({id:s.id,window:s.window,mode:s.mode})),constructionCommits:4,sharedNeutronConstructedOnce:true,physicalCarriers:5,realizationStates:6,coverage:example.tunnel.coverage,fullFiveSlotPathAgreement:true,canonicalIdentityGluingSufficient:false,nonzeroComplementTested:true,phaseCasesTested:9,physicalSpatialDegrees:degrees,singleSpatialHamiltonianTunnel:false,physicalBoundaryLawDerived:false,scope:example.tunnel.scope},null,2)+'\n');
console.log('PASS historical He-3 reference algebra ONLY (old model remains phase-unadmitted): 2P/1N/2e, one shared neutron, four covered face ports, one-item commits, full five-slot branch agreement and inverse transport. Reference/context gluing remains conditional.');
