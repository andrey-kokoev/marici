// Finite discrete-base prototype, not a full homotopy-pullback formalization.
import assert from 'node:assert/strict';
import {writeFile} from 'node:fs/promises';
import {selectPhaseAssembly,auditPhaseAssembly} from '../strominger/demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
import {applyPhasePermutation,phaseFrame} from '../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const ref=selectPhaseAssembly('helium4');auditPhaseAssembly(ref);
const copy=x=>structuredClone(x),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const generic=[[2,-3],[1,4],[-2,5],[7,-1],[-5,6]];
const basis=Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>[i===j?1:0,0]));
const packets=[];
for(const [pnId,pn] of ref.edges.entries())if(pn.kind==='PN'){
 for(const [neId,ne] of ref.edges.entries())if(ne.kind==='NE'&&ne.from===pn.to){
  assert.equal(pn.phaseDelta,0);assert.equal(ne.phaseDelta,0);
  packets.push({pnId,neId,pn,ne});
 }
}
assert(packets.length);
function endpoint(chart,origin,value,history){return {chart,origin,frame:phaseFrame(ref.charts[chart],origin),coefficients:copy(value),history:copy(history)};}
function pullback(packet,p,e){
 const {pn,ne}=packet;
 assert.equal(p.chart,pn.from,'wrong proton chart');assert.equal(e.chart,ne.to,'wrong electron chart');
 assert.deepEqual(p.frame,phaseFrame(ref.charts[p.chart],p.origin));assert.deepEqual(e.frame,phaseFrame(ref.charts[e.chart],e.origin));
 assert.equal(p.origin,e.origin,'different occurrence origins');
 const left=applyPhasePermutation(p.coefficients,pn.permutation);
 // Inverse here is a coordinate comparison, NOT an admitted E->N event.
 const right=applyPhasePermutation(e.coefficients,ne.permutation,-1);
 assert.deepEqual(left,right,'incompatible full five-slot data');
 return {kind:'strict-pullback-over-fixed-native-neutron-chart',
  proton:copy(p),electron:copy(e),
  base:{chart:pn.to,frame:phaseFrame(ref.charts[pn.to],p.origin),origin:p.origin,
        aliases:copy(ref.charts[pn.to].aliases),coefficients:left},
  witness:{leftEdge:packet.pnId,rightComparison:{inverseCoefficientMapOf:packet.neId,nativeReverseEvent:false},
           equality:'exact-all-five-slots',templateOrigin:0,realizationOrigin:p.origin,
           nativePNWitnessTemplate:copy(pn.witness),nativeNEWitnessTemplate:copy(ne.witness)},
  scope:'Endpoint histories retained separately; not identified by equality in the comparison base.'};
}
// Canonical symmetry of a pullback under reversing its two diagram legs.
// Species tags remain attached to their endpoints. This is not a species duality.
function swap(presentation){return {left:copy(presentation.right),right:copy(presentation.left),
 base:copy(presentation.base),witness:{...copy(presentation.witness),direction:-presentation.witness.direction}};}
let tested=0;const examples=[],negative=[];
function reject(label,fn){assert.throws(fn);negative.push(label);}
for(const packet of packets){
 for(const origin of [0,1,7])for(const input of [generic,...basis]){
  const n=applyPhasePermutation(input,packet.pn.permutation),e=applyPhasePermutation(n,packet.ne.permutation);
  const pState=endpoint(packet.pn.from,origin,input,['retained-proton-input']);
  const eState=endpoint(packet.ne.to,origin,e,['retained-proton-input',packet.pnId,packet.neId]);
  const result=pullback(packet,pState,eState);
  assert.deepEqual(result.base.coefficients,n);
  const presentation={left:result.proton,right:result.electron,base:result.base,witness:{data:result.witness,direction:1}};
  assert.deepEqual(swap(swap(presentation)),presentation);
  // The mediating neutron packet recovers both endpoints via the fixed maps.
  assert.deepEqual(applyPhasePermutation(n,packet.pn.permutation,-1),input);
  assert.deepEqual(applyPhasePermutation(n,packet.ne.permutation),e);
  tested++;
  if(origin===0&&same(input,generic)){
   examples.push(result);
   const wrong=copy(eState);wrong.coefficients[4][0]++;
   reject('changed-electron-coefficient',()=>pullback(packet,pState,wrong));
   const later=endpoint(eState.chart,2,eState.coefficients,eState.history);
   reject('same-coefficients-different-origin',()=>pullback(packet,pState,later));
   const changedHistory=copy(eState);changedHistory.history.push('additional-retained-comparison');
   const other=pullback(packet,pState,changedHistory);
   assert.deepEqual(other.base,result.base);assert.notDeepEqual(other,result);
   // Source edge witnesses are originally at origin 0. At other origins the
   // prototype retains their template plus the explicit shifted base frame.
  }
 }
}
const noNativeElectronReverse=packets.every(({ne})=>!ref.edges.some(edge=>edge.from===ne.to&&edge.to===ne.from));
const out={status:'pass-local-discrete-pullback-prototype',nativePackets:packets.length,tested,examples,
 rejectedCases:negative.length,noNativeElectronReverse,
 statements:{compatibleNeutronPacketUniqueForFixedCharts:true,allFiveCoefficientsRetained:true,
 formalLegSwapIsInvolutive:true,speciesDualityDerived:false,historiesIdentified:false,
 globalBranchLiftConstructed:false,particleCountsDerived:false},
 scope:'Fixed current neutron chart chosen as comparison base. Demonstrates compatibility of existing PN/NE maps, not independent derivation of neutrons. Coordinate inversion is not physical history reversal. No general homotopy universal-property proof.'};
await writeFile(new URL('./results/neutron-pullback-v1.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({status:out.status,nativePackets:packets.length,tested,rejectedCases:negative.length,noNativeElectronReverse}));
