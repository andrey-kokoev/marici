import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {selectPhaseAssembly,auditPhaseAssembly,createPhaseAssembly} from '../../strominger/demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
import {phaseFrame,phaseAdvanceWitness,applyPhasePermutation,activePhaseSlots,phaseAdvancePermutations} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';

// A concrete route interpreter for existing atom commands. The compiler has one
// input; every subsequent payload is computed, not supplied as another seed.
const clone=structuredClone, id=[0,1,2,3,4];
function compile(r,route,input,{chart=r.root,origin=0}={}) {
  applyPhasePermutation(input,id);
  const seed={chart,origin,coefficients:clone(input)},steps=[];
  let value=clone(input),permutation=[...id];
  for(const index of route){
    const e=r.edges[index];
    assert(e && e.from===chart,'typed command source mismatch');
    const from=phaseFrame(r.charts[chart],origin);
    const witness=e.phaseDelta?phaseAdvanceWitness(r.charts[e.from],r.charts[e.to],origin):clone(e.witness);
    value=applyPhasePermutation(value,e.permutation);
    permutation=e.permutation.map(i=>permutation[i]);
    origin+=e.phaseDelta; chart=e.to;
    steps.push({index,kind:e.kind,from,to:phaseFrame(r.charts[chart],origin),witness,permutation:clone(e.permutation),output:clone(value)});
  }
  return {seed,route:clone(route),steps,target:{chart,origin,coefficients:value},permutation};
}
function inversePayload(packet){
  let v=clone(packet.target.coefficients);
  for(const step of [...packet.steps].reverse())v=applyPhasePermutation(v,step.permutation,-1);
  return v;
}
const counts={certificate_routes:0,route_splits:0,viewer_reads:0,basis_routes:0,local_frame_covariance_routes:0,distinct_equal_effect_histories:0};
const after=(q,p)=>q.map(i=>p[i]);
const inverse=p=>p.map((_,i)=>p.indexOf(i));
const frame=(chart,origin)=>id.map(i=>(i+chart+2*origin+1)%5);
const rows=[];
for(const isotope of ['helium3','helium4','lithium6']){
  const r=selectPhaseAssembly(isotope); auditPhaseAssembly(r);
  const input=[[1,2],[3,-4],[5,6],[-7,8],[9,-10]];
  const states=r.certificate.states;
  for(const s of states){
    const p=compile(r,s.history,input);
    assert.equal(p.target.chart,s.chart);assert.equal(p.target.origin,s.origin);
    assert.deepEqual(p.permutation,s.permutation);
    assert.deepEqual(p.target.coefficients,applyPhasePermutation(input,s.permutation));
    assert.deepEqual(inversePayload(p),input);
    counts.certificate_routes++;
    // Passive local frame changes telescope along the exact same typed route.
    let primed=applyPhasePermutation(input,frame(r.root,0));
    let chart=r.root,origin=0;
    for(const index of s.history){
      const e=r.edges[index],gs=frame(chart,origin),gt=frame(e.to,origin+e.phaseDelta);
      const transformed=after(gt,after(e.permutation,inverse(gs)));
      primed=applyPhasePermutation(primed,transformed);chart=e.to;origin+=e.phaseDelta;
    }
    assert.deepEqual(primed,applyPhasePermutation(p.target.coefficients,frame(chart,origin)));
    counts.local_frame_covariance_routes++;
    for(let k=0;k<=s.history.length;k++){
      const a=compile(r,s.history.slice(0,k),input);
      const b=compile(r,s.history.slice(k),a.target.coefficients,{chart:a.target.chart,origin:a.target.origin});
      assert.deepEqual(b.target,p.target);
      assert.deepEqual([...a.route,...b.route],p.route);
      counts.route_splits++;
    }
    for(let j=0;j<5;j++){
      const basis=id.map(i=>[Number(i===j),0]);
      assert.deepEqual(compile(r,s.history,basis).target.coefficients,applyPhasePermutation(basis,s.permutation));
      counts.basis_routes++;
    }
  }
  const snapshot=createPhaseAssembly(isotope,{coefficients:input}).snapshot();
  for(const view of snapshot.phaseViews){
    const p=compile(r,view.history,input);
    assert.deepEqual(p.target.coefficients,view.coefficients);
    assert.equal(p.target.origin,view.origin);
    assert.deepEqual(p.steps.at(-1)?.to??phaseFrame(r.charts[r.root]),view.frame);
    counts.viewer_reads++;
  }
  const first=r.edges.findIndex(e=>e.from===r.root&&e.kind==='PN');
  const back=r.edges.findIndex(e=>e.from===r.edges[first].to&&e.to===r.root&&e.kind==='inverse-PN');
  assert(first>=0&&back>=0);
  const roundTrip=compile(r,[first,back],input),stationary=compile(r,[],input);
  assert.deepEqual(roundTrip.target,stationary.target);
  assert.notDeepEqual(roundTrip.route,stationary.route);
  counts.distinct_equal_effect_histories++;
  const wrong=r.edges.findIndex(e=>e.from!==r.root);
  assert(wrong>=0);assert.throws(()=>compile(r,[wrong],input));
  rows.push({isotope,charts:r.charts.length,commands:r.edges.length,certificateStates:states.length,carriers:snapshot.items.length,
    commandsByKind:Object.fromEntries([...new Set(r.edges.map(e=>e.kind))].map(k=>[k,r.edges.filter(e=>e.kind===k).length]))});
}

// Recover the coefficient permutation skeleton separately from typed phase routes.
// This forgets admissibility/history; it is not the atom's realization group.
const generators=[[3,1,2,0,4],[0,4,2,3,1],phaseAdvancePermutations.proton,phaseAdvancePermutations.neutron];
const group=new Map([[id.join(),id]]),queue=[id];
for(let i=0;i<queue.length;i++)for(const g of generators){const p=g.map(j=>queue[i][j]),key=p.join();if(!group.has(key)){group.set(key,p);queue.push(p);}}
assert.equal(group.size,120);
const fiveCycle=queue.find(p=>{let q=[...id];for(let i=1;i<=5;i++){q=p.map(j=>q[j]);if(q.every((v,j)=>v===j))return i===5;}return false;});
assert(fiveCycle);

// Find an ACTUAL neutron advance and typed continuation that reveals its outside
// coefficient. The rival keeps that step's four geometric coefficients exactly,
// but changes the independently declared outside-context retention law.
let discriminator=null;
for(const isotope of ['helium3','helium4','lithium6']){
  const r=selectPhaseAssembly(isotope);
  for(let index=0;index<r.edges.length&&!discriminator;index++){
    const edge=r.edges[index];
    if(!edge.phaseDelta||r.charts[edge.from].species!=='neutron')continue;
    const input=[[1,2],[3,-4],[5,6],[-7,8],[9,-10]];
    const normal=compile(r,[...r.paths[edge.from],index],input);
    const rival=clone(normal.target.coefficients);rival[0]=rival[0].map(x=>-x);
    assert.deepEqual(normal.target.coefficients.slice(1),rival.slice(1));
    assert.equal(rival.flat().reduce((s,x)=>s+x*x,0),normal.target.coefficients.flat().reduce((s,x)=>s+x*x,0));
    const q=[{chart:edge.to,origin:normal.target.origin,path:[],p:[...id]}];
    const seen=new Set();
    for(let j=0;j<q.length&&j<10000&&!discriminator;j++){
      const s=q[j],key=s.chart+':'+s.p.join();if(seen.has(key))continue;seen.add(key);
      const slots=activePhaseSlots[r.charts[s.chart].species];
      if(slots.some(slot=>s.p[slot]===0)){
        const a=compile(r,s.path,normal.target.coefficients,{chart:edge.to,origin:normal.target.origin});
        const b=compile(r,s.path,rival,{chart:edge.to,origin:normal.target.origin});
        const readerSlot=slots.find(slot=>s.p[slot]===0);
        assert.notDeepEqual(a.target.coefficients[readerSlot],b.target.coefficients[readerSlot]);
        const commonIntensity=v=>{const z=slots.reduce((s,i)=>s.map((x,j)=>x+v[i][j]),[0,0]);return z[0]**2+z[1]**2;};
        const commonA=commonIntensity(a.target.coefficients),commonB=commonIntensity(b.target.coefficients);
        assert.notEqual(commonA,commonB);
        discriminator={isotope,sourcePath:r.paths[edge.from],neutronAdvance:index,advanceKind:edge.kind,continuation:s.path,
          continuationKinds:s.path.map(i=>r.edges[i].kind),readerSpecies:r.charts[s.chart].species,readerSlot,
          retainedLawAmplitude:a.target.coefficients[readerSlot],outsideSignRivalAmplitude:b.target.coefficients[readerSlot],
          unnormalizedCommonFaceIntensity:{retained:commonA,rival:commonB,normalization:'Divide by3 for the normalized three-slot common character intensity'},
          interpretation:'Both maps are coefficient equivalences with identical immediate four-vertex values. The rival violates the chosen outside-context coefficient-retention law. A generic retained equivalence alone does not select that law.'};
        break;
      }
      if(s.path.length>=8)continue;
      for(let k=0;k<r.edges.length;k++){const e=r.edges[k];if(e.from===s.chart)q.push({chart:e.to,origin:s.origin+e.phaseDelta,path:[...s.path,k],p:e.permutation.map(i=>s.p[i])});}
    }
  }
  if(discriminator)break;
}
assert(discriminator,'an actual typed continuation must reveal the context difference');

const pins=['research/nima/agda/SingleSourceRouteCompiler.agda','research/nima/agda/RetainedTransportResolution.agda',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-assembly-model.mjs'];
const result={status:'pass-concrete-atom-retained-route-adapter',counts,assemblies:rows,
 coefficientSkeleton:{order:group.size,fiveCycle,typedHistoryQuotientClaimed:false,
 consequence:'The four unrestricted coefficient generators generate S5. They cannot all be one faithful action of the old S4 group alone. Chart restrictions and absolute phase histories remain separate.'},
 outsideContextDiscriminator:discriminator,
 boundary:{newAgdaInstantiationChecked:false,existingFormalTheoremImportedAsNewProof:false,native137RecordT9IdentificationConstructed:false,
 genericTransportMissing:false,outsideRetentionSelectedByGenericEquivalence:false,scatteringOrYangMillsEquivalenceProved:false,ownerSourcesModified:false},
 sourceSha256:Object.fromEntries(pins.map(p=>[p,crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex')]))};
fs.mkdirSync('research/kitaev/results',{recursive:true});
fs.writeFileSync('research/kitaev/results/atom-retained-transport-ancestry-v1.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));
