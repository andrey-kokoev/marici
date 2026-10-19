import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {createHelium4Window,helium4ReaderHypothesis} from '../demos/particle-overlap-tetrahedron/helium4-window-model.mjs';
import {lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {makeLatticeItem,acrossFace,itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {createWindowConstruction} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
assert.throws(()=>createHelium4Window(),/explicit/);
assert.throws(()=>createHelium4Window({protonReaderRule:'identity'}),/explicit/);
const required=lattice.cells.map(c=>itemKey(c.map(i=>lattice.nodes[i].address)));
let example;
for(const branch of ['common','positive','negative'])for(const phaseExponent of [0,1,2]){
 const model=createHelium4Window({protonReaderRule:helium4ReaderHypothesis,branch,phaseExponent,complementCoefficients:[[9,-7],[-5,6]],identity:{id:'he4-test'}}),initial=model.snapshot();
 assert.equal(model.pass(1).moved,false);assert.equal(model.crossCycle(1).crossed,false);assert.equal(model.readElectron().moved,false);
 for(let i=0;i<5;i++){
  const before=model.snapshot(),after=model.step();assert.equal(after.committed,true);assert.equal(after.items.length,before.items.length+1);assert.deepEqual(after.items.slice(0,-1),before.items);assert.equal(after.identity,initial.identity);
  for(const [name,p] of Object.entries(before.bindings))assert.deepEqual(after.bindings[name],p);
  assert.equal(after.status,i===4?'complete':'ready');assert.equal(after.tunnel.coverage.required,6);
  if(i===4)assert.deepEqual(after.bindings,before.bindings);
 }
 const built=model.snapshot();if(branch==='positive'&&phaseExponent===0)example=built;
 assert.deepEqual(built.counts,{proton:2,neutron:2,electron:2});assert.deepEqual(built.items.map(i=>required.indexOf(i.key)),[0,13,16,24,14,7]);assert.equal(new Set(built.items.map(i=>i.key)).size,6);assert.equal(built.events.length,5);assert.equal(built.added,5);
 assert.equal(built.tunnel.position,5);assert.deepEqual(built.tunnel.window,['M1','C3','M0']);assert.deepEqual(built.tunnel.mode,{branch,phaseExponent});assert.equal(built.exit.reached,false);
 assert.equal(built.tunnel.coverage.complete,true);assert.equal(built.tunnel.coverage.covered,6);assert.equal(built.tunnel.realizations.requiredStates,branch==='common'?10:30);
 const coverage=model.ambientCoverage(required);assert.equal(coverage.coveredCells,6);assert.equal(coverage.status,'incomplete');assert.equal(coverage.allEnteredStatesReachExit,true);assert.equal(coverage.throughStateIds.length,branch==='common'?10:30);
 const original=built.tunnel.referenceCarrier,one=model.crossCycle(1);assert.equal(one.crossed,true);assert.equal(one.tunnel.chart,5);
 if(branch==='common')assert.deepEqual(one.tunnel.referenceCarrier,original);else assert.notDeepEqual(one.tunnel.referenceCarrier,original);
 assert.deepEqual(one.tunnel.referenceCarrier.coefficients[4],original.coefficients[4]);
 model.crossCycle(-1);assert.deepEqual(model.snapshot().tunnel.referenceCarrier,original);
 for(let i=0;i<3;i++)model.crossCycle(1);assert.deepEqual(model.snapshot().tunnel.referenceCarrier,original);assert.deepEqual(model.snapshot().tunnel.mode,built.tunnel.mode);assert.equal(model.snapshot().tunnel.realizations.cycle,0);
 // Traverse all clock sheets, taking BOTH terminal branches at each phase.
 const exits=new Set();for(let i=0;i<24;i++){
  const s=model.snapshot();if(s.tunnel.canReadElectron){const terminal=model.readElectron();assert.equal(terminal.moved,true);assert.equal(terminal.exit.reached,true);assert.ok([2,4].includes(terminal.tunnel.position));exits.add(terminal.tunnel.position);assert.equal(model.pass(1).moved,false);assert.equal(model.crossCycle(1).crossed,false);
   model.pass(-1);assert.deepEqual(model.snapshot().tunnel.referenceCarrier,s.tunnel.referenceCarrier);assert.equal(model.snapshot().tunnel.chart,s.tunnel.chart);
  }
  const before=model.snapshot();model.pass(1);model.pass(-1);assert.deepEqual(model.snapshot().tunnel.referenceCarrier,before.tunnel.referenceCarrier);assert.equal(model.snapshot().tunnel.chart,before.tunnel.chart);model.pass(1);
 }
 const end=model.snapshot();assert.deepEqual([...exits].sort(),[2,4]);assert.equal(end.tunnel.realizations.observedStates.length,end.tunnel.realizations.requiredStates);assert.deepEqual(end.tunnel.referenceCarrier,original);
 assert.deepEqual(end.items,built.items);assert.deepEqual(end.bindings,built.bindings);assert.deepEqual(end.history,built.history);assert.deepEqual(end.events,built.events);assert.equal(end.identity,initial.identity);assert.ok(end.tunnel.fiberStates.every(s=>s.identity===initial.identity));
 assert.equal(model.step().committed,false);assert.throws(()=>model.pass(0));assert.throws(()=>model.crossCycle(0));
 // Mutating a snapshot cannot change the carried state or construction ledger.
 end.tunnel.referenceCarrier.coefficients[4][0]=1000;end.items[0].vertices[0][0]=1000;assert.deepEqual(model.snapshot().items,built.items);assert.deepEqual(model.snapshot().tunnel.referenceCarrier,original);
}
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]],seed=makeLatticeItem('tetrahedron',[0,0,0,0]);
let admittedMarkingCases=0,rejectedMarkingCases=0;
for(const permutation of permutations([0,1,2,3]))for(const branch of ['common','positive','negative']){
 const bindings=Object.fromEntries(['C0','M0','C1','M1'].map((n,i)=>[n,seed.vertices[permutation[i]]]));
 const model=createHelium4Window({protonReaderRule:helium4ReaderHypothesis,bindings,branch,complementCoefficients:[[9,-7],[-5,6]]});assert.deepEqual(model.snapshot().bindings,bindings,'Requested marking must actually reach the seed constructor');
 const native=createWindowConstruction({bindings}),n=native.step(),owner=acrossFace(seed,n.events[0].face),incoming=[n.bindings.M0,n.bindings.C2,n.bindings.M1];
 if(!owner.faces.some(f=>itemKey(f)===itemKey(incoming))){model.step();model.step();const before=model.snapshot();assert.throws(()=>model.step(),/does not give a regular second proton seed/);assert.deepEqual(model.snapshot(),before);rejectedMarkingCases++;continue;}
 for(let i=0;i<5;i++)model.step();const built=model.snapshot();admittedMarkingCases++;
 assert.equal(model.ambientCoverage(required).coveredCells,6);assert.ok(built.items.every(i=>required.includes(i.key)));
 const degrees=built.items.map((a,i)=>built.items.filter((b,j)=>i!==j&&a.faces.some(f=>b.faces.some(g=>itemKey(f)===itemKey(g)))).length);assert.deepEqual(degrees,[2,4,1,2,1,2]);
 for(let i=0;i<3;i++)model.crossCycle(1);assert.deepEqual(model.snapshot().tunnel.referenceCarrier,built.tunnel.referenceCarrier);assert.deepEqual(model.snapshot().items,built.items);
}
assert.equal(admittedMarkingCases,24);assert.equal(rejectedMarkingCases,48);
const out='research/strominger/results/helium4-window';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'pass-reference-algebra-geometry-only',phaseDisciplineVerified:false,viewerMode:'legacy-model-not-displayed',counts:example.counts,cellIds:example.items.map(i=>required.indexOf(i.key)),constructionCommits:5,addedToHelium3:1,retainedHelium3Prefix:true,finalNeutronAddsNoVertices:true,readerRule:helium4ReaderHypothesis,operatorOrder:3,defaultStateCount:30,commonSectorStateCount:10,fullStateCoverage:6,ambientPrimitiveCount:343,allEnteredStatesReachRetainedElectronExit:true,terminalElectronBodies:[2,4],inverseAndThreeTurnClosure:true,nonzeroComplementTested:true,characterPhaseCases:9,markingBranchCases:72,admittedMarkingCases,rejectedMarkingCases,geometryAndConstructionHistoryUnchangedDuringPassage:true,tubeGeometry:false,physicalReaderRuleDerived:false,physicalStabilityDerived:false,scope:example.tunnel.scope},null,2)+'\n');
console.log('PASS historical He-4 reference algebra ONLY (old model remains phase-unadmitted): one-item construction to 2P/2N/2e; 30 default full reader states; both retained electron exits; three-turn and inverse closure on all five slots; no tubes.');
