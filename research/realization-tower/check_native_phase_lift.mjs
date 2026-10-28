// Current phase-first source audit and explicit geometric-forgetting control.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {selectPhaseAssembly,auditPhaseAssembly,createPhaseAssembly} from '../strominger/demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
import {phaseFrame,phaseAdvanceWitness,applyPhasePermutation,spectralReadout} from '../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const copy=x=>structuredClone(x),generic=[[2,-3],[1,4],[-2,5],[7,-1],[-5,6]];
const ref=selectPhaseAssembly('helium4'),audit=auditPhaseAssembly(ref);
assert.equal(audit.coverage.allEnteredStatesReachExit,true);assert.equal(audit.coverage.coveredCells,6);
const state=createPhaseAssembly('helium4',{coefficients:generic}).snapshot();
assert.deepEqual(state.counts,{proton:2,neutron:2,electron:2});
const region=JSON.parse(await fs.readFile(new URL('./results/six-step-octahedron-v1.json',import.meta.url),'utf8'));
// The earlier six-step receipt uses centre (1,0,0); translate the whole
// six-body source by (0,0,0) in the FCC chart to place it in that region.
const allowed=new Set(region.points.map(p=>p.join(',')));
const toFCC=([a,b,c,d])=>[b+c,b+d,c+d];
const placements=[];
for(let x=-4;x<=4;x++)for(let y=-4;y<=4;y++)for(let z=-4;z<=4;z++){
 const shift=[x,y,z];if((x+y+z)%2)continue;
 const bodies=state.items.map(item=>({species:item.species,sourceKey:item.key,
  vertices:item.vertices.map(p=>toFCC(p).map((v,i)=>v+shift[i]))}));
 if(bodies.every(b=>b.vertices.every(p=>allowed.has(p.join(',')))))placements.push({shift,bodies});
}
assert(placements.length>0);
let edgeChecks=0;
for(const edge of ref.edges){
 const out=applyPhasePermutation(generic,edge.permutation);
 assert.deepEqual(applyPhasePermutation(out,edge.permutation,-1),generic);
 for(let i=0;i<5;i++){
  const basis=Array.from({length:5},(_,j)=>[i===j?1:0,0]);
  assert.deepEqual(applyPhasePermutation(applyPhasePermutation(basis,edge.permutation),edge.permutation,-1),basis);
 }
 const read=spectralReadout(ref.charts[edge.to].species,out);
 read.slots.forEach((slot,i)=>read.reconstructed[i].forEach((v,k)=>assert(Math.abs(v-out[slot][k])<1e-10)));
 if(edge.phaseDelta){const w=phaseAdvanceWitness(ref.charts[edge.from],ref.charts[edge.to],7);assert.equal(w.phaseDelta,1);assert.deepEqual(w.permutation,edge.permutation);}
 edgeChecks++;
}
const edge=ref.edges.find(e=>e.phaseDelta&&ref.charts[e.from].species==='neutron'&&ref.charts[e.from].cell===ref.charts[e.to].cell);
assert(edge,'Need an actual same-body neutron advance');
const a=ref.charts[edge.from],b=ref.charts[edge.to];
const w1=phaseAdvanceWitness(a,b,0),w2=phaseAdvanceWitness(b,a,1);
const after=applyPhasePermutation(generic,w1.permutation),returned=applyPhasePermutation(after,w2.permutation);
assert.deepEqual(returned,generic);
assert.deepEqual(w2.to,phaseFrame(a,2));assert.notDeepEqual(w2.to,phaseFrame(a,0));
const geometry=f=>[...f.window,f.context].map(o=>o.vertex).sort();
assert.deepEqual(geometry(w2.to),geometry(w1.from));
const rejected=[];
function reject(name,fn){assert.throws(fn);rejected.push(name);}
const frozen=copy(b);frozen.aliases.C1=a.aliases.C1;frozen.aliases.C2=a.aliases.C2;
reject('freeze_C_occurrences',()=>phaseAdvanceWitness(a,frozen));
const gap=copy(ref),s=gap.certificate.states.find(s=>s.origin>0);s.origin++;s.frame=phaseFrame(gap.charts[s.chart],s.origin);
reject('skip_phase_with_locally_valid_frame',()=>auditPhaseAssembly(gap));
const corrupt=copy(ref);corrupt.edges.find(e=>e.phaseDelta&&ref.charts[e.from].species==='neutron').permutation=[0,3,2,1,4];
reject('erase_context_to_active_transfer',()=>auditPhaseAssembly(corrupt));
const out={status:'pass',source:'Current phase-first helium4 reference assembly; explicit outside-context law retained',
 audit,counts:state.counts,edgeChecks,placements,
 same_body_control:{sourceChart:a,targetChart:b,first:w1,second:w2,input:generic,afterFirst:after,afterSecond:returned,
  conclusion:'Same geometry and coefficients after two advances, but absolute origin increases by two; full records cannot be identified.'},
 rejected_controls:rejected,
 scope:'Existing phase-first source and its geometric embedding checked. This is NOT a constructed lift of all 1200 shortest-path comparisons to native charts; no 82/126 count is derived.'};
await fs.writeFile(new URL('./results/native-phase-lift-v1.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({status:out.status,coveredCells:audit.coverage.coveredCells,edgeChecks,containedTranslations:placements.length,
 coefficientReturn:true,fullRecordReturn:false,rejected}));
