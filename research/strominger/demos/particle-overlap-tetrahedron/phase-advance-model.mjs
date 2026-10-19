import {windowProtocol} from './window-construction-model.mjs';
import {windowModeCoefficients} from './deuterium-tunnel-model.mjs';
import {auditPhaseFrame,auditPhaseSuccessor} from './phase-discipline-model.mjs';
const copy=x=>structuredClone(x),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
export const phaseAdvanceRule='retained-edge/next-realization/full-five-slot';
export const phaseAdvancePermutations=Object.freeze({proton:Object.freeze([2,3,0,1,4]),neutron:Object.freeze([0,3,4,1,2])});
export const activePhaseSlots={proton:[0,1,2],neutron:[1,2,3],electron:[3,2,4]};
export function phaseFrame(chart,origin=0){
 if(!Number.isSafeInteger(origin)||origin<0)throw Error('Nonnegative integer realization origin required');
 const spec=windowProtocol.find(p=>p.species===chart.species);if(!spec)throw Error('Unknown carrier');
 const occurrence=name=>{const role=name[0],index=Number(name.slice(1))+origin,vertex=chart.aliases[name];if(typeof vertex!=='string'||!vertex)throw Error('Explicit geometric binding required');return {role,index,vertex};};
 return {id:chart.id+'@'+origin,species:chart.species,window:spec.window.map(occurrence),context:occurrence(spec.continuation)};
}
export function phaseAdvanceWitness(source,target,origin=0){
 if(source.species!==target.species||!['proton','neutron'].includes(source.species))throw Error('Phase advance requires matching P or N carriers');
 const from=phaseFrame(source,origin),to=phaseFrame(target,origin+1),p=source.species==='proton';
 if([from,to].some(f=>auditPhaseFrame(f).status!=='native-template-compatible'))throw Error('Invalid local phase frame');
 const retained=[[from.window[2],to.window[0]],[from.context,to.window[1]]];
 if(retained.some(([a,b])=>!same(a,b)))throw Error('Next realization must retain the actual next C/M occurrences');
 if(p&&(from.window[0].vertex!==to.window[2].vertex||from.window[1].vertex!==to.context.vertex))throw Error('P re-reading must retain all four geometric vertices');
 if(!p&&from.window[1].vertex!==to.context.vertex)throw Error('Old C1 must become the new C3 context, not remain active C1');
 const traces=p?{C:[from.window[0],from.window[2],to.window[2]],M:[from.window[1],from.context,to.context]}:{C:[from.window[1],from.context,to.context],M:[from.window[0],from.window[2],to.window[2]]};
 for(const trace of Object.values(traces))for(let i=1;i<trace.length;i++)if(auditPhaseSuccessor(trace[i-1],trace[i]).status!=='consecutive')throw Error('Skipped realization phase');
 // The fifth reference coordinate also has a phase-bearing provenance. It
 // is not identified with the active C occurrence merely by equal index.
 const outside=p?'C2':'C0',q=Number(outside.slice(1));
 const referenceContext={from:{role:'C',index:origin+q,vertex:source.aliases[outside]},to:{role:'C',index:origin+q+1,vertex:target.aliases[outside]},coefficientRule:'retain',physicalLawDerived:false};
 if(typeof referenceContext.from.vertex!=='string'||typeof referenceContext.to.vertex!=='string'||auditPhaseSuccessor(referenceContext.from,referenceContext.to).status!=='consecutive')throw Error('Missing reference-context phase successor');
 const permutation=[...phaseAdvancePermutations[source.species]];
 return {rule:phaseAdvanceRule,from,to,retained:retained.map(([x])=>copy(x)),traces,referenceContext,phaseDelta:1,permutation,
  scope:'Ordered next-realization witness, with distinct geometric and occurrence identities. Outside-context coefficient retention remains an explicit reference law, not derived particle dynamics.'};
}
export function applyPhasePermutation(value,permutation,direction=1){
 if(![1,-1].includes(direction)||!Array.isArray(value)||value.length!==5||value.some(z=>!Array.isArray(z)||z.length!==2||z.some(x=>!Number.isFinite(x)))||!same([...permutation].sort((a,b)=>a-b),[0,1,2,3,4]))throw Error('Finite five-slot vector and bijective map required');
 const p=direction===1?permutation:permutation.map((_,i)=>permutation.indexOf(i));return p.map(i=>[...value[i]]);
}
// Retain ALL Fourier components of the active face. A phase fold can bring a
// nonzero complementary coefficient into that face; no rank-one reset occurs.
export function spectralReadout(species,value){
 const slots=activePhaseSlots[species],active=slots.map(i=>value[i]),branches=['common','positive','negative'];
 const components=branches.map(branch=>{const basis=windowModeCoefficients({branch,phaseExponent:0}),coefficient=basis.reduce(([re,im],[a,b],i)=>[re+a*active[i][0]+b*active[i][1],im+a*active[i][1]-b*active[i][0]],[0,0]);return {branch,coefficient,basis};});
 const reconstructed=active.map((_,i)=>components.reduce(([re,im],c)=>{const [a,b]=c.coefficient,[x,y]=c.basis[i];return [re+a*x-b*y,im+a*y+b*x];},[0,0]));
 return {slots,components,reconstructed,complement:value.flatMap((coefficient,slot)=>slots.includes(slot)?[]:[{slot,coefficient:[...coefficient]}])};
}
