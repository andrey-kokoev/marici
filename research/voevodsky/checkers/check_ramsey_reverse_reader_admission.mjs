import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules as Native} from '../../nima/generative-phase-assembly.mjs';
import {GenerativeAssemblyRules as Local} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {makeLatticeItem} from '../../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseCombination} from '../../strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const ROOT=new URL('../../../',import.meta.url),canonical=x=>Array.isArray(x)?x.map(canonical):x&&typeof x==='object'?Object.fromEntries(Object.keys(x).sort().map(k=>[k,canonical(x[k])])):x;
const key=x=>JSON.stringify(canonical(x));
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const five=['C0','M0','C1','M1','C2'],four=five.slice(0,4),six=[...five,'M2'];
const reverseName={C0:'M2',M0:'C2',C1:'M1',M1:'C1',C2:'M0',M2:'C0'};
const order={proton:[2,3,1,0],neutron:[3,2,1,0],electron:[3,2,0,1]},swapSpecies={proton:'electron',neutron:'neutron',electron:'proton'};
function reverseFrame(f){const all=[...f.window,f.context].map(o=>({...o,role:o.role==='C'?'M':'C',index:2-o.index})),q=order[f.species].map(i=>all[i]);return {...f,species:swapSpecies[f.species],window:q.slice(0,3),context:q[3]};}
const semanticFrame=({id,...f})=>f,apply=(p,x)=>p.map(i=>x[i]),inverse=p=>p.map((_,i)=>p.indexOf(i));
function attempt(f){try{return {ok:true,value:f()};}catch(e){return {ok:false,error:String(e.message)};}}
for(const name of ['chart','completeP','completeN','packet','outgoing','validateTransfer'])assert.equal(Native.prototype[name].toString(),Local.prototype[name].toString(),'owning method divergence '+name);
function audit(Rules){
 const rows=[],seed=makeLatticeItem('tetrahedron',[0,0,0,0]);
 for(const marking of permutations([0,1,2,3])){
  const seedBindings=Object.fromEntries(four.map((n,i)=>[n,seed.vertices[marking[i]].join(',')]));
  const r=new Rules({seedBindings}),p=r.root,pn=r.outgoing(p).map(i=>r.operations[i]).find(o=>o.kind==='PN');assert(pn);
  const n=pn.target,ne=r.outgoing(n).map(i=>r.operations[i]).find(o=>o.kind==='NE');assert(ne);const e=ne.target;
  assert(r.validateTransfer(pn));assert(r.validateTransfer(ne));
  const packets=[p,n,e].map(id=>r.packets[id]),charts=packets.map(p=>r.charts[p.chart]);
  const originalBodies=charts.map(c=>({cell:c.cell,species:c.species,vertices:r.geometry.cells[c.cell].vertices.slice(),aliases:{...c.aliases}}));
  const coordinateRecord=key(originalBodies.map(c=>c.vertices));
  const frames=charts.map((c,i)=>phaseFrame(c,packets[i].origin));
  frames.forEach(f=>assert.equal(key(reverseFrame(reverseFrame(f))),key(f)));
  const [rp,rn,re]=[frames[2],frames[1],frames[0]].map(reverseFrame);
  const phaseAudit=auditPhaseCombination([rp,rn,re],[{from:rp.id,to:rn.id,kind:'PN',identification:'same-occurrence',vertices:ne.face},{from:rn.id,to:re.id,kind:'NE',identification:'same-occurrence',vertices:pn.face}]);assert.equal(phaseAudit.status,'native-phase-compatible');
  const originalOutgoingE=r.outgoing(e);assert.equal(originalOutgoingE.length,0);
  const old=charts[2].aliases,reversed=Object.fromEntries(six.map(name=>[name,old[reverseName[name]]]));
  assert(six.every(name=>typeof reversed[name]==='string'));
  const oldFive=five.map(name=>old[name]),newFive=five.map(name=>reversed[name]);
  const lost=oldFive.filter(v=>!newFive.includes(v)),added=newFive.filter(v=>!oldFive.includes(v));
  assert.deepEqual(lost,[old.C0]);assert.deepEqual(added,[old.M2]);
  const pAttempt=attempt(()=>r.completeP(charts[2].cell,reversed));
  const nAttempt=attempt(()=>r.completeN(charts[1].cell,reversed));
  const eAttempt=attempt(()=>r.chart(charts[0].cell,'electron',reversed));assert(eAttempt.ok);
  const geometry=r.geometry.cells[charts[2].cell].geometry;
  const row={marking,seedBindings,electronGeometry:geometry,originalBodies,forwardPackets:packets,forwardOperations:[pn,ne],reversedAliases:reversed,
   phaseAudit:phaseAudit.status,doubleReaderReversal:true,oldElectronOutgoingCount:originalOutgoingE.length,
   fullChartAttempts:{proton:pAttempt,neutron:nAttempt,electron:eAttempt},referenceScope:{oldFive,newFive,oldReferenceNoLongerInFive:lost,newReferenceEnteringFive:added,allSixRetainedInAudit:true}};
  const referenceRebasings=permutations([0,1,2,3,4]).filter(q=>five.every((name,i)=>reversed[name]===old[five[q[i]]]));assert.equal(referenceRebasings.length,0);
  row.referenceInducedFiveSlotPermutationCount=referenceRebasings.length;
  if(geometry==='proton'){
   assert(pAttempt.ok&&pAttempt.value!==null);assert(nAttempt.ok&&nAttempt.value!==null);
   const revCharts=[pAttempt.value,nAttempt.value,eAttempt.value];
   revCharts.forEach((id,i)=>{
    const c=r.charts[id];assert.equal(c.cell,charts[2-i].cell);
    for(const name of i===2?six:five)assert.equal(c.aliases[name],reversed[name]);
    assert.equal(key(semanticFrame(phaseFrame(c,0))),key(semanticFrame([rp,rn,re][i])));
   });
   // The old B convention carries the original coefficient reference basis unchanged.
   const carried=[2,1,0].map((oldIndex,i)=>r.packet(revCharts[i],0,packets[oldIndex].permutation));
   const proposed=[{source:carried[0],target:carried[1],kind:'PN',phaseDelta:0,permutation:inverse(ne.permutation),face:ne.face},
                   {source:carried[1],target:carried[2],kind:'NE',phaseDelta:0,permutation:inverse(pn.permutation),face:pn.face}];
   const carriedChecks=proposed.map(op=>attempt(()=>r.validateTransfer(op)));
   for(const check of carriedChecks){assert(!check.ok);assert.match(check.error,/Lost a full coefficient coordinate/);}
   const generatedPN=r.outgoing(carried[0]).map(i=>r.operations[i]).find(o=>o.kind==='PN');assert(generatedPN);assert(r.validateTransfer(generatedPN));
   const generatedNE=r.outgoing(generatedPN.target).map(i=>r.operations[i]).find(o=>o.kind==='NE');assert(generatedNE);assert(r.validateTransfer(generatedNE));
   assert.equal(r.packets[generatedPN.target].chart,revCharts[1]);assert.equal(r.packets[generatedNE.target].chart,revCharts[2]);
   assert.notEqual(key(r.packets[generatedPN.target].permutation),key(packets[1].permutation));
   const bridge={source:e,target:carried[0],kind:'reader-reversal',phaseDelta:0,permutation:[0,1,2,3,4],face:null};
   const bridgeCheck=attempt(()=>r.validateTransfer(bridge));assert(!bridgeCheck.ok);assert.match(bridgeCheck.error,/Unknown native transfer/);
   const PN=generatedPN.permutation,NE=generatedNE.permutation,ID=[0,1,2,3,4];
   const conjugacies=permutations(ID).filter(q=>key(apply(PN,apply(q,ID)))===key(apply(q,apply(inverse(ne.permutation),ID)))&&key(apply(NE,apply(q,ID)))===key(apply(q,apply(inverse(pn.permutation),ID))));assert.equal(conjugacies.length,4);
   Object.assign(row,{completeReversedChartsValid:true,carriedCoefficientChecks:carriedChecks,hostConfiguredReverseRoot:carried[0],
    generatedReverseOperations:[generatedPN,generatedNE],generatedReversePackets:[carried[0],generatedPN.target,generatedNE.target].map(id=>r.packets[id]),
    bridgeCheck,bareCoefficientConjugacies:conjugacies,bareConjugaciesSourceAuthorized:false});
  }else{
   assert.equal(geometry,'split');assert(!pAttempt.ok);assert.match(pAttempt.error,/Wrong native P\/N reference geometry/);
   assert(nAttempt.ok&&nAttempt.value===null);
   Object.assign(row,{completeReversedChartsValid:false,firstFailure:'old electron is split; reversed proton rejected; reversed neutron has no regular proton reference'});
  }
  assert.equal(key(charts.map(c=>r.geometry.cells[c.cell].vertices)),coordinateRecord);
  rows.push(row);
 }
 return rows;
}
const native=audit(Native),local=audit(Local);assert.equal(key(native),key(local));
const regular=native.filter(r=>r.electronGeometry==='proton'),split=native.filter(r=>r.electronGeometry==='split');assert.equal(regular.length,8);assert.equal(split.length,16);
const hashes={};function pin(path){if(path in hashes)return;const bytes=readFileSync(new URL(path,ROOT));hashes[path]=createHash('sha256').update(bytes).digest('hex');
 if(path.endsWith('.mjs'))for(const m of bytes.toString().matchAll(/(?:from\s*|import\s*)['"]([^'"]+\.mjs)['"]/g))if(m[1].startsWith('.'))pin(decodeURIComponent(new URL(m[1],new URL(path,ROOT)).href.slice(ROOT.href.length)));}
pin('research/voevodsky/checkers/check_ramsey_reverse_reader_admission.mjs');pin('research/voevodsky/contracts/ramsey-reverse-reader-admission-attempt.v1.json');
pin('research/strominger/checkers/probe_deuterium_reverse_reading.mjs');
pin('research/voevodsky/checkers/check_ramsey_reverse_reader_admission.py');
const out={schema:'marici.ramsey-reverse-reader-admission.verification.v1',status:'passed',scope_id:'fresh-fixed-coordinate-reader-reversal-native-admission-audit-v1',
 verification_level:'fresh exact runtime chart/transfer audit in both owning implementations; not kernel-verified semantics',
 freshMarkingsPerImplementation:24,implementationsChecked:2,owningCoreMethodsIdentical:true,freshOutcomesAgree:true,
 fixedCoordinateReaderAudits:24,completeReversedChartFamilies:8,shapeRejectedFamilies:16,
 carriedCoefficientTransferRejections:16,hostConfiguredNativeReverseChains:8,originalElectronTerminalCases:24,
 explicitReversalBridgeRejections:8,bareCoefficientConjugaciesPerRegularCase:4,
 referenceInducedFiveSlotPermutationCount:0,sourceAdmittedReversalProduced:false,
 allPathsFromOriginalRootRefuted:false,allCoefficientAdaptersRefuted:false,
 parentDescentResolved:false,nativeSignatureChanged:false,rows:native,source_sha256:hashes};
writeFileSync(new URL('../results/ramsey-reverse-reader-admission-v1.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({...out,rows:undefined,source_sha256:undefined},null,2));
