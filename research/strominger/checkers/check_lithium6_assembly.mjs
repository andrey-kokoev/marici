import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import './check_simplex_components.mjs';
import {lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {searchLithium6Assemblies,lithiumNNHypothesis} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
import {compileLithium6Reference,applyLithiumReferenceEdge} from '../demos/particle-overlap-tetrahedron/lithium6-reference-model.mjs';
import {createLithium6Assembly,selectLithium6Reference} from '../demos/particle-overlap-tetrahedron/lithium6-viewer-model.mjs';
const strict=searchLithium6Assemblies(),relaxed=searchLithium6Assemblies({allowNN:true}),keys=lattice.cells.map(c=>itemKey(c.map(v=>lattice.nodes[v].address)));
assert.equal(strict.candidates.length,0);assert.equal(relaxed.candidates.length,96);assert.equal(relaxed.typedNuclei,48);
const histogram={},rejected={},examples={},sample=[[2,-3],[4,5],[-6,7],[9,-7],[-5,6]],norm=c=>c.reduce((s,z)=>s+z[0]**2+z[1]**2,0);let checked=0,admitted=0;
for(const candidate of relaxed.candidates){
 const bytes=JSON.stringify(candidate),pn=candidate.interfaces.filter(e=>e.kind==='PN').length;
 assert.equal(candidate.interfaces.filter(e=>e.kind==='NN').length,1);assert.ok([0,1].includes(candidate.nuclearCycleRank));assert.equal(new Set([...candidate.nucleus,...candidate.electrons]).size,9);
 for(let orientations=0;orientations<2**pn;orientations++){
  const r=compileLithium6Reference(candidate,{nnRule:lithiumNNHypothesis,orientations});checked++;
  if(r.status!=='reference-algebra-only'){rejected[r.reason]=(rejected[r.reason]??0)+1;continue;}
  assert.equal(r.viewerAdmitted,false);assert.equal(r.phaseAudit.status,'not-phase-admitted');assert.ok(r.phaseAudit.issues.some(i=>i.kind==='shared-face-phase-conflict'));admitted++;histogram[r.operatorOrder]=(histogram[r.operatorOrder]??0)+1;examples[r.operatorOrder]??={candidate,r};
  assert.equal(r.coverage.coveredCells,9);assert.equal(r.coverage.allEnteredStatesReachExit,true);assert.equal(r.rootHolonomies.length,r.operatorOrder);assert.equal(r.states.length,r.charts.length*r.operatorOrder);
  assert.ok(r.exitStates.every(id=>!r.transitions.some(([from])=>from===id)));
  for(const edge of r.edges){const slots={proton:[0,1,2],neutron:[1,2,3],electron:[3,2,4]};assert.deepEqual(slots[r.charts[edge.to].species].map(i=>edge.permutation[i]).sort((a,b)=>a-b),slots[r.charts[edge.from].species].slice().sort((a,b)=>a-b));const transported=applyLithiumReferenceEdge(sample,edge);assert.deepEqual(applyLithiumReferenceEdge(transported,edge,-1),sample);assert.equal(norm(transported),norm(sample));
   if(edge.kind==='NN-reference'){
    const a=r.charts[edge.from],b=r.charts[edge.to];assert.equal(a.aliases.M1,b.aliases.M0);assert.equal(a.aliases.C1,b.aliases.C1);assert.equal(a.aliases.C2,b.aliases.C2);
    assert.deepEqual(transported[1],sample[3]);assert.deepEqual(transported[2],sample[2]);assert.deepEqual(transported[4],sample[4]);assert.deepEqual(transported[0],sample[0]);assert.equal(edge.conditional,true);
   }
  }
  let value=structuredClone(sample);for(let turn=0;turn<r.operatorOrder;turn++)for(const h of r.tour)value=applyLithiumReferenceEdge(value,r.edges[h.edge],h.direction);assert.deepEqual(value,sample);
  for(const h of r.rootHolonomies){assert.equal(h[3],3);assert.equal(h[4],4);}
 }
 assert.equal(JSON.stringify(candidate),bytes);
}
assert.equal(checked,2304);assert.equal(admitted,240);assert.deepEqual(histogram,{2:96,3:144});
const selected=selectLithium6Reference();assert.equal(selected.reference.orientations,9);assert.equal(selected.reference.operatorOrder,2);assert.equal(selected.reference.states.length,28);
assert.ok(![0,13,24,7].every(i=>selected.candidate.nucleus.includes(i)),'Default assembly is not constrained to the old He-4 nucleus');
assert.throws(()=>createLithium6Assembly(),/withdrawn/);assert.throws(()=>createLithium6Assembly({nnRule:lithiumNNHypothesis}),/withdrawn/);assert.throws(()=>compileLithium6Reference(selected.candidate,{nnRule:lithiumNNHypothesis,orientations:-1}),/orientation/);
const bad=structuredClone(selected.candidate);bad.interfaces.pop();assert.throws(()=>compileLithium6Reference(bad,{nnRule:lithiumNNHypothesis}),/ledger/);
const wrong=structuredClone(selected.candidate);wrong.types[lattice.cells[0][0]]='X';assert.throws(()=>compileLithium6Reference(wrong,{nnRule:lithiumNNHypothesis}),/MMCC/);
for(const branch of ['common','positive','negative'])for(const phaseExponent of [0,1,2]){
 const m=createLithium6Assembly({researchOnly:true,nnRule:lithiumNNHypothesis,branch,phaseExponent,complementCoefficients:[[9,-7],[-5,6]]}),first=m.snapshot();
 assert.deepEqual(first.counts,{proton:3,neutron:3,electron:3});assert.equal(first.items.length,9);assert.equal(first.added,0);assert.deepEqual(first.events,[]);assert.equal(first.construction.retainedHe4PrefixRequired,false);assert.equal(m.step().committed,false);assert.equal(m.ambientCoverage(keys).coveredCells,9);assert.equal(m.ambientCoverage(keys).status,'incomplete');
 const one=m.crossCycle(1);assert.notDeepEqual(one.tunnel.referenceCarrier.permutation,first.tunnel.referenceCarrier.permutation);if(branch==='common')assert.deepEqual(one.tunnel.referenceCarrier.coefficients,first.tunnel.referenceCarrier.coefficients);else assert.notDeepEqual(one.tunnel.referenceCarrier.coefficients,first.tunnel.referenceCarrier.coefficients);
 m.crossCycle(-1);assert.deepEqual(m.snapshot().tunnel.referenceCarrier,first.tunnel.referenceCarrier);
 const exits=new Set();for(let i=0;i<24;i++){
  const s=m.snapshot();if(s.tunnel.canReadElectron){const e=m.readElectron();exits.add(e.tunnel.position);assert.equal(e.exit.reached,true);assert.equal(m.pass(1).moved,false);assert.equal(m.crossCycle(1).crossed,false);m.pass(-1);assert.deepEqual(m.snapshot().tunnel.referenceCarrier,s.tunnel.referenceCarrier);}
  m.pass(1);m.pass(-1);assert.deepEqual(m.snapshot().tunnel.referenceCarrier,s.tunnel.referenceCarrier);m.pass(1);
 }
 const end=m.snapshot();assert.equal(exits.size,3);assert.equal(end.tunnel.realizations.observedStates.length,28);assert.deepEqual(end.tunnel.referenceCarrier,first.tunnel.referenceCarrier);assert.deepEqual(end.items,first.items);assert.deepEqual(end.bindings,first.bindings);assert.equal(end.identity,first.identity);assert.ok(end.tunnel.fiberStates.every(s=>s.identity===first.identity));
 end.items[0].vertices[0][0]=100;end.tunnel.referenceCarrier.coefficients[4][0]=100;assert.deepEqual(m.snapshot().items,first.items);assert.deepEqual(m.snapshot().tunnel.referenceCarrier,first.tunnel.referenceCarrier);
}
const out='research/strominger/results/lithium6-assembly';await mkdir(out,{recursive:true});
await writeFile(out+'/candidate.json',JSON.stringify({status:'withdrawn-phase-discipline',...selected,items:createLithium6Assembly({researchOnly:true,nnRule:lithiumNNHypothesis}).snapshot().items},null,2)+'\n');
await writeFile(out+'/verification.json',JSON.stringify({status:'pass-reference-algebra-only-withdrawn',viewerAdmitted:false,phaseDisciplineVerified:false,phaseAdmittedAssignments:0,phaseAudit:selected.reference.phaseAudit,target:{proton:3,neutron:3,electron:3},domain:relaxed.scope,strictPNOnlyCandidates:0,typedNuclei:48,typedWholeAssemblies:96,readerAssignmentsChecked:checked,algebraCompatibleReaderAssignments:admitted,operatorOrderHistogram:histogram,rejectedReaderAssignments:rejected,nnRule:lithiumNNHypothesis,defaultNuclearCells:selected.candidate.nucleus,defaultElectronCells:selected.candidate.electrons,defaultReaderOrientationMask:9,defaultOperatorOrder:2,defaultOperatorFrameStates:28,defaultTourSteps:12,selection:'cycle-bearing candidates first, then lexicographic cells and first admitted orientation mask; not an energy or stability criterion',allFiveSlotsRetained:true,NNSharedFaceCoefficientsFixed:3,outsideContextIdentificationAssumed:true,allEnteredStatesReachElectron:true,localCoverage:'9/9',ambientCoverage:'9/343',retainedHe4PrefixRequired:false,betweenElementSingleCarrierGrowthRequired:false,ambiguityResolved:false,physicalStabilityDerived:false,tubes:false,characterPhaseCases:9,scope:selected.reference.scope},null,2)+'\n');
console.log('PASS withdrawn frozen-C Li-6 model: 240/2304 algebra-compatible assignments, ZERO phase-admitted under that old rule. The corrected phase-advance construction is checked separately.');
