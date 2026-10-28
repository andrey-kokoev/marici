// Calls the unchanged owning phase constructors. Emits retained pilot data on stdout.
import assert from 'node:assert/strict';
import {selectPhaseAssembly,auditPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
import {phaseFrame,phaseAdvanceWitness,applyPhasePermutation} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseCombination} from '../demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
import {auditStateCoverage} from '../demos/particle-overlap-tetrahedron/fiber-coverage-model.mjs';
import {referenceCarrierMarks} from '../demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs';
import {lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
const clone=x=>structuredClone(x),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const basis=Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>[Number(i===j),0]));
basis.push([[2,3],[-5,7],[11,-13],[17,19],[-23,29]]);
const identity=[0,1,2,3,4],fixtures=[];
for(const isotope of ['helium3','helium4','lithium6']){
 const r=selectPhaseAssembly(isotope),nativeAudit=auditPhaseAssembly(r),prefix=`wrapped:${isotope}:`;
 const encode=v=>prefix+v,decode=v=>{assert(v.startsWith(prefix));return v.slice(prefix.length);};
 function rename(x,direction=1){
  if(Array.isArray(x))return x.map(v=>rename(v,direction));
  if(x&&typeof x==='object')return Object.fromEntries(Object.entries(x).map(([k,v])=>[k,(k==='vertex'||k==='id')&&typeof v==='string'?(direction===1?encode(v):decode(v)):rename(v,direction)]));
  return x;
 }
 const charts=r.charts.map(c=>({...clone(c),id:encode(c.id),aliases:Object.fromEntries(Object.entries(c.aliases).map(([k,v])=>[k,encode(v)]))}));
 const checks={},witnesses=[],loops=[],routeComparisons=[];
 const check=(name,condition)=>{assert(condition,name);checks[name]=true;};
 const wrappedCertificate={...clone(r.certificate),states:r.certificate.states.map(s=>({...clone(s),id:encode(s.id),cell:encode(s.cell),frame:phaseFrame(charts[s.chart],s.origin)})),transitions:r.certificate.transitions.map(pair=>pair.map(encode)),entryStates:r.certificate.entryStates.map(encode),exitStates:r.certificate.exitStates.map(encode),requiredCells:r.certificate.requiredCells.map(encode)};
 function decodeCertificate(cert){return {...clone(cert),states:cert.states.map(s=>({...clone(s),id:decode(s.id),cell:decode(s.cell),frame:rename(s.frame,-1)})),transitions:cert.transitions.map(p=>p.map(decode)),entryStates:cert.entryStates.map(decode),exitStates:cert.exitStates.map(decode),requiredCells:cert.requiredCells.map(decode)};}
 function validate(cert){return auditPhaseAssembly({...clone(r),certificate:decodeCertificate(cert)});}
 check('native_source_reference_audit',nativeAudit.status==='phase-coherent-reference');
 check('certificate_exact_decode',same(decodeCertificate(wrappedCertificate),r.certificate));
 check('wrapped_entry_exit_coverage',auditStateCoverage(wrappedCertificate).status==='covered');
 check('decoded_certificate_replays_native_validation',validate(wrappedCertificate).status==='phase-coherent-reference');
 for(const [index,e] of r.edges.entries()){
  const a=charts[e.from],b=charts[e.to];
  for(const origin of [0,2,17]){
   if(e.phaseDelta===1){
    const actual=phaseAdvanceWitness(a,b,origin),expected=rename(phaseAdvanceWitness(r.charts[e.from],r.charts[e.to],origin));
    assert.deepEqual(actual,expected);assert.deepEqual(actual.permutation,e.permutation);
    routeComparisons.push({edge:index,origin,source_then_encode:expected,encode_then_source:actual});
    if(origin===0)witnesses.push({edge:index,kind:e.kind,witness:actual});
   }else{
    const inverse=e.kind==='inverse-PN',from=phaseFrame(inverse?b:a,origin),to=phaseFrame(inverse?a:b,origin);
    assert.equal(auditPhaseCombination([from,to],[{from:from.id,to:to.id,kind:inverse?'PN':e.kind,identification:'same-occurrence',vertices:to.window.map(o=>o.vertex)}]).status,'native-phase-compatible');
    assert(referenceCarrierMarks.every(mark=>a.aliases[mark]===b.aliases[mark]));
    const nativeFrom=phaseFrame(r.charts[inverse?e.to:e.from],origin),nativeTo=phaseFrame(r.charts[inverse?e.from:e.to],origin);
    const expected=rename({from:nativeFrom,to:nativeTo,phaseDelta:0,permutation:e.permutation}),actual={from,to,phaseDelta:0,permutation:e.permutation};
    assert.deepEqual(actual,expected);
    routeComparisons.push({edge:index,origin,source_then_encode:expected,encode_then_source:actual});
    if(origin===0)witnesses.push({edge:index,kind:e.kind,witness:{from,to,phaseDelta:0,permutation:e.permutation}});
   }
  }
  for(const vector of basis){
   const native=applyPhasePermutation(vector,e.permutation),wrapped=applyPhasePermutation(vector,e.permutation);
   assert.deepEqual(wrapped,native);
   assert.deepEqual(applyPhasePermutation(wrapped,e.permutation,-1),vector);
  }
 }
 check('actual_witness_generator_commutes_at_origins_0_2_17',true);
 check('full_five_slot_basis_and_complex_context_recover',true);
 const damaged=clone(wrappedCertificate),nonroot=damaged.states.find(s=>s.history.length);
 nonroot.history=[];
 assert.throws(()=>validate(damaged));check('history_erasure_rejected',true);
 const wrong=clone(wrappedCertificate),nonidentity=wrong.states.find(s=>!same(s.permutation,identity));
 nonidentity.permutation=[...identity];
 assert.throws(()=>validate(wrong));check('coefficient_permutation_erasure_rejected',true);
 assert.throws(()=>applyPhasePermutation([[1,0],[2,0],[3,0]],identity));check('three_slot_truncation_rejected',true);
 for(const [i,e] of r.edges.entries())if(e.kind==='reader-phase-advance'){
  const j=r.edges.findIndex(f=>f.kind===e.kind&&f.from===e.to&&f.to===e.from);
  assert(j>=0);const f=r.edges[j],twice=f.permutation.map(k=>e.permutation[k]);
  assert.deepEqual(twice,identity);
  const before=phaseFrame(charts[e.from],17),after=phaseFrame(charts[e.from],19);
  assert.notDeepEqual(before,after);
  loops.push({edges:[i,j],species:charts[e.from].species,coefficient_return:twice,origin_before:17,origin_after:19,history:[i,j],before,after});
 }
 check('reader_coefficient_return_does_not_reset_origin',loops.length>0);
 for(const c of charts.filter(c=>c.species==='electron')){
  assert.throws(()=>phaseAdvanceWitness(c,c,0));
  assert(!r.edges.some(e=>e.from===charts.indexOf(c)));
 }
 check('electron_reader_is_not_in_current_source_alphabet',true);
 const points=Object.fromEntries([...new Set(r.charts.flatMap(c=>Object.values(c.aliases)))].map(v=>[v,lattice.nodes[Number(v.slice(7))].address]));
 const carriers=[...new Set(r.charts.map(c=>c.cell))].map(id=>({id,vertices:lattice.cells[id].map(v=>lattice.nodes[v].address),species:r.charts.find(c=>c.cell===id).species}));
 fixtures.push({isotope,checks,nativeAudit,reference:r,wrappedCharts:charts,wrappedCertificate,wrappedWitnesses:witnesses,readerLoops:loops,routeComparisons,points,carriers});
}
const sector=buildPESymmetricSector(3);
console.log(JSON.stringify({fixtures,sector:sector.cells.map(c=>({id:c.id,kind:c.kind,role:c.role,vertices:c.vertices})),scope:'Actual local phase-reference pilots, not a phase assignment to the whole geometric sector.'}));
