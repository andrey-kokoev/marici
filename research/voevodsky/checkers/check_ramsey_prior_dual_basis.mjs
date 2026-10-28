// Search follow-up: distinguish a native numeric transfer check from a typed basis binding.
import assert from 'node:assert/strict';
import {writeFileSync,readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {makeLatticeItem} from '../../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {activePhaseSlots} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {windowProtocol} from '../../strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs';
const incoming=['C0','M0','C1','M1','C2'],outgoing=['M0','C1','M1','C2','M2'],Q=[4,3,2,1,0];
const J={C0:'M2',M0:'C2',C1:'M1',M1:'C1',C2:'M0',M2:'C0'},apply=(p,x)=>p.map(i=>x[i]);
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
assert.deepEqual(outgoing.map(n=>incoming.findIndex(m=>J[m]===n)),Q);
const readouts=windowProtocol.map(p=>({species:p.species,requiredMarks:[...p.window],nativeSlots:activePhaseSlots[p.species],
 literalOutgoingMarksAtNativeSlots:activePhaseSlots[p.species].map(i=>outgoing[i]),outgoingSlotsForRequiredMarks:p.window.map(n=>outgoing.indexOf(n))}));
for(const x of readouts)assert.notDeepEqual(x.requiredMarks,x.literalOutgoingMarksAtNativeSlots);
assert.deepEqual(readouts.find(x=>x.species==='proton').outgoingSlotsForRequiredMarks,[-1,0,1]);
const seed=makeLatticeItem('tetrahedron',[0,0,0,0]),rows=[];
for(const marking of permutations([0,1,2,3])){
 const r=new GenerativeAssemblyRules({seedBindings:Object.fromEntries(incoming.slice(0,4).map((n,i)=>[n,seed.vertices[marking[i]].join(',')]))});
 const op=(id,kind)=>r.outgoing(id).map(i=>r.operations[i]).find(o=>o.kind===kind),pn=op(r.root,'PN'),ne=op(pn.target,'NE');
 assert(r.validateTransfer(pn));assert(r.validateTransfer(ne));
 const packets=[r.root,pn.target,ne.target].map(id=>r.packets[id]),charts=packets.map(p=>r.charts[p.chart]);
 const geometry=r.geometry.cells[charts[2].cell].geometry;
 if(geometry!=='proton'){rows.push({marking,electronGeometry:geometry,nativeReverseChartEligible:false});continue;}
 const aliases=Object.fromEntries(Object.keys(J).map(n=>[n,charts[2].aliases[J[n]]]));
 const ids=[r.completeP(charts[2].cell,aliases),r.completeN(charts[1].cell,aliases),r.chart(charts[0].cell,'electron',aliases)];assert(ids.every(x=>x!==null));
 const dual=ids.map((c,i)=>r.packet(c,0,apply(Q,packets[2-i].permutation)));
 const proposed=[{source:dual[0],target:dual[1],kind:'PN',phaseDelta:0,permutation:pn.permutation,face:ne.face},
                 {source:dual[1],target:dual[2],kind:'NE',phaseDelta:0,permutation:ne.permutation,face:pn.face}];
 for(const transfer of proposed)assert(r.validateTransfer(transfer));
 assert.equal(op(dual[0],'PN').target,dual[1]);assert.equal(op(dual[1],'NE').target,dual[2]);assert.equal(r.outgoing(ne.target).length,0);
 rows.push({marking,electronGeometry:geometry,nativeReverseChartEligible:true,numericQRebasedTransfersPass:true,
  nativePacketKeys:Object.keys(r.packets[dual[0]]),outgoingBasisBindingEstablished:false,originalElectronOutgoingCount:0});
}
assert.equal(rows.filter(r=>r.numericQRebasedTransfersPass).length,8);
const root=new URL('../../../',import.meta.url),sources=['research/voevodsky/checkers/check_ramsey_prior_dual_basis.mjs','research/strominger/checkers/check_T_seam_transition.mjs','research/strominger/T-seam-transition-v1.md','research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs'];
const result={status:'passed',scope:'Fresh numeric and named-readout audit of a prior candidate, not admission of a role-changing operation',priorBasisMap:Q,incoming,outgoing,
 freshMarkings:24,numericRebasedNativeChains:8,shapeIneligible:16,readouts,rows,
 source_sha256:Object.fromEntries(sources.map(p=>[p,createHash('sha256').update(readFileSync(new URL(p,root))).digest('hex')]))};
writeFileSync(new URL('../results/ramsey-prior-dual-basis-v1.json',import.meta.url),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({...result,rows:undefined,source_sha256:undefined},null,2));
