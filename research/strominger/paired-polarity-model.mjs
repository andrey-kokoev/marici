// Candidate polarity of comparison roles, not physical charge conjugation.
import {makeSinglePEPair} from './single-pe-pair-model.mjs';
import {applyPhasePermutation} from './demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const pair=makeSinglePEPair(),PN=pair.pn.permutation,NE=pair.ne.permutation;
export function oppositeComparisonRole(role){
 const result={proton:'electron',electron:'proton',neutron:'neutron'}[role];
 if(!result)throw Error('Unknown comparison role');return result;
}
export function reverseComparisonPolarity(packet){
 if(![1,-1].includes(packet.polarity))throw Error('Explicit sheet polarity required');
 const value=packet.coefficients;
 const coefficients=packet.role==='proton'?applyPhasePermutation(applyPhasePermutation(value,PN),NE):packet.role==='electron'?applyPhasePermutation(applyPhasePermutation(value,NE,-1),PN,-1):applyPhasePermutation(value,[0,1,2,3,4]);
 if(packet.interfaceFlow!==undefined&&![1,-1].includes(packet.interfaceFlow))throw Error('Invalid interface direction');
 return {...structuredClone(packet),role:oppositeComparisonRole(packet.role),polarity:-packet.polarity,coefficients,...(packet.interfaceFlow===undefined?{}:{interfaceFlow:-packet.interfaceFlow})};
}
export function retainedPolarityPair(packet){
 if(packet.polarity!==1)throw Error('Positive original sheet required');
 const positive=structuredClone(packet),negative=reverseComparisonPolarity(positive),recovered=reverseComparisonPolarity(negative);
 if(JSON.stringify(recovered)!==JSON.stringify(positive))throw Error('Full polarity confirmation failed');
 return {positive,negative,confirmation:'full-state-involution',nativeParticleRealization:false};
}
export function pairedPolarityProbe(){
 const prepared=pair.prepare([[2,1],[3,-2],[5,3],[7,-4],[11,5]]);
 return Object.fromEntries([
  ['aa','proton',prepared.endpoints.P,1],['ab','neutron',prepared.neutron.coefficients,1],
  ['ba','neutron',prepared.neutron.coefficients,-1],['bb','electron',prepared.endpoints.E,1]
 ].map(([slot,role,coefficients,flow])=>[slot,retainedPolarityPair({role,coefficients,polarity:1,interfaceFlow:flow})]));
}
