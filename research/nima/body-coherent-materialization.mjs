import {inspectContraction} from './experimental-terminal-pe.mjs';
// Atomic planner macros only; native transfer and PE eligibility rules are unchanged.
export function materializationCandidates(u,ids){
 const before=inspectContraction(u,ids);if(!before.valid||!before.rooted)throw Error('Materialization requires a compatible rooted start');
 const groups=new Map();for(const o of before.shortcuts){const b=o.referenceNeutronCell;if(!groups.has(b))groups.set(b,[]);groups.get(b).push(o);}
 return [...groups].map(([body,shortcuts])=>{const added=[...new Set(shortcuts.map(o=>o.referenceNeutronPacket))].filter(p=>!ids.includes(p)),selected=[...ids,...added],after=inspectContraction(u,selected);
  return {body,shortcuts:shortcuts.map(o=>o.id),added,selected,valid:after.valid,reason:after.reason??null,rooted:after.rooted??false,noExit:after.noExit??null,missingContacts:after.missingContacts??null,certified:!!after.certifiedExit};
 });
}
