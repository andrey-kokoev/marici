import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {inspectContraction} from './experimental-terminal-pe.mjs';
import {materializationCandidates} from './body-coherent-materialization.mjs';
import {closeContactObligations} from './tessellated-atlas.mjs';

const sorted=xs=>[...xs].sort((a,b)=>a-b),difference=(xs,ys)=>xs.filter(x=>!ys.includes(x));
const hash=x=>createHash('sha256').update(JSON.stringify(x,(_,v)=>typeof v==='bigint'?v.toString():v)).digest('hex');
export function executionModelFingerprint(c){return hash({mode:c.mode,maxOrigin:c.universe.maxOrigin,geometry:c.geometry,readers:c.readers,interfaces:c.interfaces});}
function audit(c,ids){return inspectContraction(c.universe,ids,{mode:c.mode});}
function checkSelection(c,ids,label){assert.ok(Array.isArray(ids),`${label} must be an array`);assert.equal(new Set(ids).size,ids.length,`${label} repeats a packet`);c.mask(ids);assert.ok(ids.includes(c.universe.rules.root),`${label} lacks root`);const a=audit(c,ids);assert.ok(a.valid&&a.rooted,`${label} must be compatible and rooted`);return a;}
function summary(a){return {noExit:sorted(a.noExit),missingContacts:a.missingContacts.map(x=>x.key).sort(),certified:!!a.certifiedExit};}
function effects(before,after){const b=summary(before),a=summary(after);return {before:b,after:a,resolved:{exitReaders:difference(b.noExit,a.noExit),contacts:difference(b.missingContacts,a.missingContacts)},introduced:{exitReaders:difference(a.noExit,b.noExit),contacts:difference(a.missingContacts,b.missingContacts)},disabledShortcuts:before.shortcuts.filter(o=>!after.shortcuts.some(p=>p.id===o.id)).map(o=>o.id).sort((a,b)=>a-b)};}
function describeStep(c,beforeIds,move){
 const before=audit(c,beforeIds),selected=sorted([...beforeIds,...move.added]),after=audit(c,selected);assert.ok(after.valid&&after.rooted);
 if(move.kind==='singleton'){
  const o=c.interfaces[move.interface];assert.ok(o&&move.added.length===1&&o.target===move.added[0]&&beforeIds.includes(o.source));assert.ok(c.active(c.mask(selected))&o.bit);
  return {...move,selected,justification:{kind:o.kind,source:o.source,target:o.target,nativeFactors:o.nativeFactors},obligations:effects(before,after)};
 }
 assert.equal(move.kind,'body-materialization');const group=before.shortcuts.filter(o=>o.referenceNeutronCell===move.body);assert.ok(group.length);assert.deepEqual(sorted(new Set(group.map(o=>o.referenceNeutronPacket))),sorted(move.added));
 const replacements=group.map(o=>({shortcut:o.id,source:o.source,target:o.target,intermediate:o.referenceNeutronPacket,nativeFactors:o.nativeFactors}));
 for(const r of replacements)for(const id of r.nativeFactors){const o=c.universe.rules.operations[id];assert.ok(selected.includes(o.source)&&selected.includes(o.target));c.universe.rules.validateTransfer(o);}
 return {...move,selected,justification:{referenceBody:move.body,replacements},obligations:effects(before,after)};
}

/** Search only within the retained start/target interval. No arbitrary batches. */
export function planExecution(c,startIds,targetIds,{maxStates=100000,maxMilliseconds=10000,allowMaterialization=true}={}){
 assert.ok(Number.isInteger(maxStates)&&maxStates>=1);assert.ok(Number.isFinite(maxMilliseconds)&&maxMilliseconds>=0);assert.equal(typeof allowMaterialization,'boolean');
 checkSelection(c,startIds,'start');const targetAudit=checkSelection(c,targetIds,'target');assert.ok(targetAudit.certifiedExit,'target must be certified');assert.ok(startIds.every(p=>targetIds.includes(p)),'target removes retained packets');
 const start=sorted(startIds),target=sorted(targetIds),startMask=c.mask(start),targetMask=c.mask(target),began=performance.now(),nodes=[{mask:startMask,parent:-1,move:null}],seen=new Map([[startMask,0]]);let found=-1;
 function add(mask,parent,move){if(seen.has(mask))return true;if(nodes.length>=maxStates)return false;seen.set(mask,nodes.length);nodes.push({mask,parent,move});return true;}
 // Stable final-active anchor gives a linear constructive schedule, avoiding subset search.
 const finalActive=c.active(targetMask);
 if(c.reach(startMask,finalActive&c.active(startMask))===startMask){
  let current=startMask;
  while(current!==targetMask){
   if(performance.now()-began>=maxMilliseconds)return {status:'incomplete',reason:'execution-time-limit',states:nodes.length};
   const o=c.interfaces.find(o=>(finalActive&o.bit)&&(current&o.sourceBit)&&!(current&o.targetBit));assert.ok(o);
   const next=current|o.targetBit;if(!add(next,nodes.length-1,{kind:'singleton',added:[o.target],interface:o.index}))return {status:'incomplete',reason:'execution-state-limit',states:nodes.length};current=next;
  }
  found=nodes.length-1;
 }
 for(let i=0;found<0&&i<nodes.length;i++){
  const node=nodes[i];if(node.mask===targetMask){found=i;break;}
  if(performance.now()-began>=maxMilliseconds)return {status:'incomplete',reason:'execution-time-limit',states:nodes.length};
  for(const o of c.interfaces){if(!(node.mask&o.sourceBit)||(node.mask&o.targetBit)||!(targetMask&o.targetBit))continue;const next=node.mask|o.targetBit;
   if(seen.has(next)||!c.compatible(next))continue;const active=c.active(next);if(!(active&o.bit)||c.reach(next,active)!==next)continue;
   if(!add(next,i,{kind:'singleton',added:[o.target],interface:o.index}))return {status:'incomplete',reason:'execution-state-limit',states:nodes.length};
  }
  if(allowMaterialization&&c.mode==='experimental-terminal-PE')for(const m of materializationCandidates(c.universe,c.decode(node.mask))){
   if(!m.valid||!m.rooted||!m.added.length)continue;const next=c.mask(m.selected);if((next&targetMask)!==next)continue;
   if(!add(next,i,{kind:'body-materialization',body:m.body,added:sorted(m.added)}))return {status:'incomplete',reason:'execution-state-limit',states:nodes.length};
  }
 }
 if(found<0)return {status:'unreachable',reason:'no-path-under-declared-operations',states:nodes.length,scope:'Fixed target interval; not impossibility of the target assembly.'};
 const moves=[];for(let i=found;nodes[i].parent>=0;i=nodes[i].parent)moves.push(nodes[i].move);moves.reverse();let ids=start;const steps=moves.map(move=>{const step=describeStep(c,ids,move);ids=step.selected;return step;});
 const plan={schema:'marici.nima.atlas-execution-plan.v1',status:'planned',modelFingerprint:executionModelFingerprint(c),mode:c.mode,maxOrigin:c.universe.maxOrigin,start,target,steps,statesSearched:nodes.length,operations:{singleton:true,bodyMaterialization:!!allowMaterialization&&c.mode==='experimental-terminal-PE'},scope:'Every boundary is compatible and rooted; exits and face witnessing may be pending until the certified target. Atomic batches do not authorize singleton intermediates.'};
 replayExecution(c,plan);return plan;
}

/** Re-derive transitions and metadata from source, never trusting saved audit flags. */
export function replayExecution(c,plan){
 assert.equal(plan.schema,'marici.nima.atlas-execution-plan.v1');assert.equal(plan.status,'planned');assert.equal(plan.modelFingerprint,executionModelFingerprint(c),'model fingerprint mismatch');assert.equal(plan.mode,c.mode);assert.equal(plan.maxOrigin,c.universe.maxOrigin);
 checkSelection(c,plan.start,'start');assert.deepEqual(plan.start,sorted(plan.start));assert.deepEqual(plan.target,sorted(plan.target));assert.ok(checkSelection(c,plan.target,'target').certifiedExit);assert.ok(plan.start.every(p=>plan.target.includes(p)));
 let ids=[...plan.start];let batches=0;
 for(const step of plan.steps){assert.ok(['singleton','body-materialization'].includes(step.kind));assert.ok(step.added.length&&new Set(step.added).size===step.added.length);assert.ok(step.added.every(p=>!ids.includes(p)&&plan.target.includes(p)));
  let move;if(step.kind==='singleton'){assert.equal(plan.operations.singleton,true);move={kind:step.kind,added:step.added,interface:step.interface};}
  else{assert.equal(c.mode,'experimental-terminal-PE');assert.equal(plan.operations.bodyMaterialization,true);const legal=materializationCandidates(c.universe,ids).find(m=>m.body===step.body&&m.valid&&m.rooted&&JSON.stringify(sorted(m.added))===JSON.stringify(sorted(step.added)));assert.ok(legal,'Not a legal whole-body materialization');move={kind:step.kind,body:step.body,added:step.added};batches++;}
  const expected=describeStep(c,ids,move);assert.deepEqual(step,expected,'step witness or obligation annotation changed');ids=expected.selected;
 }
 assert.deepEqual(ids,plan.target);assert.ok(audit(c,ids).certifiedExit);return {status:'pass',steps:plan.steps.length,batches,certified:true};
}

/** A source completion is not successful construction until scheduling succeeds. */
export function completeAndPlan(c,startIds,{closure={},execution={}}={}){
 checkSelection(c,startIds,'start');const result=closeContactObligations(c,startIds,closure);
 if(result.status!=='sat')return {status:result.status,phase:'completion',completion:result};
 const plan=planExecution(c,startIds,result.selectedPackets,execution);
 if(plan.status!=='planned')return {status:plan.status,phase:'scheduling',completion:result,execution:plan};
 return {status:'planned',completion:result,plan};
}
