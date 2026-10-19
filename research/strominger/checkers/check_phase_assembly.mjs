import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {selectPhaseAssembly,compilePhaseAssembly,createPhaseAssembly,auditPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
import {phaseAdvanceWitness,phaseFrame,applyPhasePermutation,spectralReadout} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {createAssemblyDisplay} from '../demos/particle-overlap-tetrahedron/assembly-display-model.mjs';
import {referenceCarrierMarks,windowModeCoefficients} from '../demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs';
const copy=x=>structuredClone(x),norm=v=>v.reduce((s,[a,b])=>s+a*a+b*b,0),near=(a,b)=>Math.abs(a-b)<1e-10;
const generic=[[2,-3],[1,4],[-2,5],[7,-1],[-5,6]],rows=[];
for(const [isotope,counts,total] of [['helium3',[2,1,2],5],['helium4',[2,2,2],6],['lithium6',[3,3,3],9],['lithium7',[3,4,3],10],['beryllium9',[4,5,4],13],['boron10',[5,5,5],15],['boron11',[5,6,5],16],['carbon12',[6,6,6],18],['carbon13',[6,7,6],19],['nitrogen15',[7,8,7],22]]){
 const r=selectPhaseAssembly(isotope),audit=auditPhaseAssembly(r),s=createPhaseAssembly(isotope,{coefficients:generic}).snapshot();
 assert.equal(audit.status,'phase-coherent-reference');assert.equal(audit.coverage.coveredCells,total);assert.equal(audit.coverage.requiredCells,total);assert.equal(audit.coverage.allEnteredStatesReachExit,true);
 assert.deepEqual(['proton','neutron','electron'].map(k=>s.counts[k]),counts);assert.equal(new Set(s.items.map(i=>i.key)).size,total);
 assert.deepEqual(s.phaseViews[0].frame.window.map(o=>o.role+o.index),['C0','M0','C1']);
 assert.ok(s.phaseViews.every((v,i)=>!i||v.origin>=s.phaseViews[i-1].origin));
 for(const edge of r.edges){
  const value=applyPhasePermutation(generic,edge.permutation),back=applyPhasePermutation(value,edge.permutation,-1);assert.deepEqual(back,generic);assert.equal(norm(value),norm(generic));
  const read=spectralReadout(r.charts[edge.to].species,value);read.slots.forEach((slot,i)=>read.reconstructed[i].forEach((x,j)=>assert.ok(near(x,value[slot][j]))));assert.equal(read.complement.length,2);
  if(edge.phaseDelta){
   const a=r.charts[edge.from],b=r.charts[edge.to],w=phaseAdvanceWitness(a,b,7);assert.equal(w.phaseDelta,1);
   for(const trace of Object.values(w.traces))for(let i=1;i<trace.length;i++)assert.equal(trace[i].index-trace[i-1].index,1);
   const shared=[...w.from.window,w.from.context].map(o=>o.vertex).filter(v=>[...w.to.window,w.to.context].some(o=>o.vertex===v));
   for(const vertex of shared){const from=referenceCarrierMarks.findIndex(name=>a.aliases[name]===vertex),to=referenceCarrierMarks.findIndex(name=>b.aliases[name]===vertex);assert.deepEqual(value[to],generic[from]);}
   if(a.species==='neutron'){assert.deepEqual(edge.permutation,[0,3,4,1,2]);assert.deepEqual(value[2],generic[4]);assert.deepEqual(value[4],generic[2]);}
   else assert.deepEqual(edge.permutation,[2,3,0,1,4]);
  }
 }
 for(const view of s.phaseViews){assert.ok(near(norm(view.coefficients),norm(generic)));const spectrum=view.spectrum;for(let i=0;i<3;i++)spectrum.reconstructed[i].forEach((x,j)=>assert.ok(near(x,view.coefficients[spectrum.slots[i]][j])));}
 for(const branch of ['common','positive','negative'])for(const phaseExponent of [0,1,2]){
  const input=[...windowModeCoefficients({branch,phaseExponent}),[2,-3],[-5,6]],trial=createPhaseAssembly(isotope,{coefficients:input}).snapshot();
  assert.deepEqual(trial.phaseViews.map(v=>v.frame),s.phaseViews.map(v=>v.frame));
  for(const view of trial.phaseViews){assert.ok(near(norm(view.coefficients),norm(input)));assert.equal(view.spectrum.components.length,3);view.spectrum.slots.forEach((slot,i)=>view.spectrum.reconstructed[i].forEach((x,j)=>assert.ok(near(x,view.coefficients[slot][j]))));}
 }
 const display=createAssemblyDisplay(()=>createPhaseAssembly(isotope)),prefixes=[display.snapshot()];
 for(let i=1;i<total;i++){const next=display.next();assert.equal(next.items.length,i+1);assert.deepEqual(next.items.slice(0,-1),prefixes.at(-1).items);assert.equal(next.assemblyDisplay.mode,'phase-reference');assert.equal(next.displayVertexLabels.length,new Set(next.items.flatMap(item=>item.vertices.map(p=>JSON.stringify(p)))).size);assert.equal(next.displayVertexLabels.reduce((sum,label)=>sum+label.occurrences.length,0),4*next.items.length);
  next.phaseViews.forEach((view,itemIndex)=>{for(const o of [...view.frame.window,view.frame.context])assert.ok(next.displayVertexLabels.some(label=>label.vertex===o.vertex&&label.occurrences.some(shown=>shown.itemIndex===itemIndex&&shown.role===o.role&&shown.index===o.index&&shown.origin===view.origin)));});prefixes.push(next);}
 for(let i=total-2;i>=0;i--)assert.deepEqual(display.previous(),prefixes[i]);
 for(let i=1;i<total;i++)assert.deepEqual(display.next(),prefixes[i]);
 const cycling=createAssemblyDisplay(()=>createPhaseAssembly(isotope),{loop:true,initiallyAssembled:true});assert.equal(cycling.snapshot().items.length,total);assert.equal(cycling.snapshot().assemblyDisplay.canNext,true);assert.equal(cycling.next().items.length,1);assert.equal(cycling.previous().items.length,total);
 assert.ok(cycling.snapshot().displayVertexLabels.every(label=>/^[CM]\d+( \/ [CM]\d+)*$/.test(label.text)));
 const corrupt=copy(r);corrupt.certificate.states.find(x=>x.origin>0).origin+=1;assert.throws(()=>auditPhaseAssembly(corrupt),/Phase indices|skipped/);
 const locallyValidGap=copy(r),gap=locallyValidGap.certificate.states.find(x=>x.origin>0);gap.origin++;gap.frame=phaseFrame(locallyValidGap.charts[gap.chart],gap.origin);assert.throws(()=>auditPhaseAssembly(locallyValidGap),/skipped a phase/);
 const badContext=copy(r);badContext.edges.find(e=>e.phaseDelta).witness.referenceContext.to.index++;assert.throws(()=>auditPhaseAssembly(badContext),/witness/);
 const badMap=copy(r);const fold=badMap.edges.find(e=>e.phaseDelta&&badMap.charts[e.from].species==='neutron');fold.permutation=[0,3,2,1,4];assert.throws(()=>auditPhaseAssembly(badMap),/map was changed/);
 const missing=copy(r);missing.certificate.requiredCells.pop();assert.throws(()=>auditPhaseAssembly(missing),/omitted/);
 const mismatch=copy(r.candidate);mismatch.interfaces.pop();assert.throws(()=>compilePhaseAssembly(mismatch,0),/ledger mismatch/);
 rows.push({isotope,counts,total,orientations:r.orientations,nucleus:r.candidate.nucleus,electrons:r.candidate.electrons,phaseStateCount:audit.phaseStateCount,coverage:audit.coverage.status,windows:s.phaseViews.map(v=>({origin:v.origin,window:v.frame.window.map(o=>o.role+o.index),context:v.frame.context.role+v.frame.context.index,history:v.history}))});
}
const li6=selectPhaseAssembly('lithium6'),li7=selectPhaseAssembly('lithium7');
assert.deepEqual(li7.candidate.electrons,li6.candidate.electrons);
assert.ok(li6.candidate.nucleus.every(i=>li7.candidate.nucleus.includes(i)));
for(const [v,t] of Object.entries(li6.candidate.types))assert.equal(li7.candidate.types[v],t);
assert.deepEqual(li7.retainedAssembly.addedNeutrons,[7]);
const chartKey=c=>JSON.stringify([c.cell,c.species,c.aliases]);
for(const c of li6.charts)assert.ok(li7.charts.some(d=>chartKey(c)===chartKey(d)));
for(const e of li6.edges)assert.ok(li7.edges.some(f=>chartKey(li6.charts[e.from])===chartKey(li7.charts[f.from])&&chartKey(li6.charts[e.to])===chartKey(li7.charts[f.to])&&e.kind===f.kind&&e.phaseDelta===f.phaseDelta&&JSON.stringify(e.permutation)===JSON.stringify(f.permutation)));
const h=selectPhaseAssembly('helium3'),edge=h.edges.find(e=>e.phaseDelta&&h.charts[e.from].species==='neutron'),a=h.charts[edge.from],b=h.charts[edge.to];
const w1=phaseAdvanceWitness(a,b),w2=phaseAdvanceWitness(b,a,1);
assert.deepEqual(w1.from.window.map(o=>o.role+o.index),['M0','C1','M1']);assert.deepEqual(w1.to.window.map(o=>o.role+o.index),['M1','C2','M2']);assert.equal(w1.to.context.role+w1.to.context.index,'C3');
assert.deepEqual(w2.to,phaseFrame(a,2));assert.notDeepEqual(w2.to,w1.from);assert.deepEqual(applyPhasePermutation(applyPhasePermutation(generic,w1.permutation),w2.permutation),generic);
const frozen=copy(b);frozen.aliases.C1=a.aliases.C1;frozen.aliases.C2=a.aliases.C2;assert.throws(()=>phaseAdvanceWitness(a,frozen),/retain the actual next/);
const pure=windowModeCoefficients({branch:'positive',phaseExponent:0}),input=[[2,-3],...pure,[-5,6]],after=applyPhasePermutation(input,w1.permutation),spectrum=spectralReadout('neutron',after);
assert.equal(spectrum.components.filter(c=>norm([c.coefficient])>1e-12).length,3);assert.deepEqual(after[2],input[4]);assert.deepEqual(after[4],input[2]);
await mkdir('research/strominger/results/phase-assembly',{recursive:true});
await writeFile('research/strominger/results/phase-assembly/verification.json',JSON.stringify({status:'pass-phase-coherent-reference-assemblies',rows,fullFiveSlotTests:true,allThreeFaceModesRetained:true,contextEntersActiveWindow:true,characterPhaseCases:90,lithium7RetainsLithium6GeometryRolesAndReaders:true,lithium7AddedNeutronCell:7,coefficientClosureDoesNotResetPhase:true,skippedPhaseAndFrozenCNegatives:true,physicalBindingLawDerived:false,scope:'Native templates plus explicit ordered realization advances and reference outside-context retention. Finite history-bearing entry/exit certificates, not a quotient of absolute phase or a physical stability derivation.'},null,2)+'\n');
console.log('PASS phase-first He-3 / He-4 / Li-6 / Li-7 / Be-9 / B-10 / B-11 / C-12 / C-13 / N-15: consecutive C and M histories, context-to-active transfer, all five coefficients and all three face modes retained, full assembly entry/exit witnesses. Coefficient closure does not close realization phase.');
