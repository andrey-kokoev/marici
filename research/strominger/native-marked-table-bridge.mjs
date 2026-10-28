import {table,runMarkedTableDiagram} from './marked-table-diagram.mjs';
import {validateNativeFixture,auditRetainedDiagram} from './retained-diagram-audit.mjs';
import {boundary,composeEvidence} from './fibration-evidence.mjs';
import {isDeepStrictEqual} from 'node:util';
const equal=isDeepStrictEqual;
// Presentation of a retained native diagram, NOT a producer of native geometry.
// Operations live only in rows; the remaining full native context is retained.
export function nativeDiagramToTable(fixture){
 const errors=validateNativeFixture(fixture);if(errors.length)throw Error(`Malformed native diagram: ${JSON.stringify(errors)}`);
 const {operations,...nativeContext}=structuredClone(fixture);
 const rows=operations.map(({source,target,kind,...operation},ordinal)=>({id:`operation:${operation.id}`,label:kind,source,target,payload:{ordinal,operation}}));
 const carriers={label:[...new Set(rows.map(r=>r.label))],source:fixture.packets.map(p=>p.id),target:fixture.packets.map(p=>p.id)};
 return {kind:'native-marked-table-envelope',nativeContext,table:table(rows,carriers,[{operation:'present-native-diagram',root:fixture.rootPacket}]),scope:'Native histories remain in nativeContext; table history records presentation changes, not new native executions.'};
}
export function tableToNativeDiagram(envelope){
 if(envelope?.kind!=='native-marked-table-envelope'||!envelope.nativeContext||Object.hasOwn(envelope.nativeContext,'operations')||envelope.table?.kind!=='marked-table')throw Error('Expected marked native envelope without a hidden operation table');
 const t=table(envelope.table.rows,envelope.table.carriers,envelope.table.history),ids=envelope.nativeContext.packets?.map(p=>p.id);
 if(!equal(t.carriers.source,ids)||!equal(t.carriers.target,ids))throw Error('Native packet carrier mismatch');
 const ordinals=new Set();const entries=t.rows.map(r=>{
  const p=r.payload,op=p?.operation;if(!op||r.id!==`operation:${op.id}`||!Number.isSafeInteger(p.ordinal)||p.ordinal<0||p.ordinal>=t.rows.length||ordinals.has(p.ordinal))throw Error('Invalid operation identity or occurrence order');
  if(['source','target','kind'].some(k=>Object.hasOwn(op,k)))throw Error('Hidden endpoint/label fields cannot override marked columns');
  ordinals.add(p.ordinal);return {ordinal:p.ordinal,operation:{...structuredClone(op),source:r.source,target:r.target,kind:r.label}};
 });
 const result={...structuredClone(envelope.nativeContext),operations:entries.sort((a,b)=>a.ordinal-b.ordinal).map(e=>e.operation)};
 const errors=validateNativeFixture(result);if(errors.length)throw Error(`Recovered native diagram is malformed: ${JSON.stringify(errors)}`);return result;
}
export function runNativeTableBridge(fixture){
 const envelope=nativeDiagramToTable(fixture),cycle=runMarkedTableDiagram(envelope.table),restoredEnvelope={...envelope,table:cycle.stages[4]},recovered=tableToNativeDiagram(restoredEnvelope);
 const nativeAudit=auditRetainedDiagram(recovered,fixture),fullRecovery=equal(recovered,fixture);
 const premises=[{id:'bridge:context-retention',status:'assumed',statement:'The full native carrier/packet/context records remain attached; grouped rows are not a standalone geometric assembly or a scalar encoding.'}];
 const encode={id:'bridge:encode',adapter:'native-table-bridge',input:boundary('native-diagram',fixture),output:boundary('marked-table',envelope.table),dependsOn:[],premises,claim:'Native operations become marked rows, with all other native data retained in the attached envelope.',checks:[{id:'operation-coverage',passed:envelope.table.rows.length===fixture.operations.length},{id:'no-hidden-operation-copy',passed:!Object.hasOwn(envelope.nativeContext,'operations')}]};
 const decode={id:'bridge:decode',adapter:'native-table-bridge',input:boundary('marked-table',restoredEnvelope.table),output:boundary('native-diagram',recovered),dependsOn:['table:4','bridge:encode'],premises,claim:'After four table presentation steps, recover every native packet, interface, carrier, occurrence and comparison.',checks:[{id:'full-native-recovery',passed:fullRecovery},{id:'native-diagram-consistency',passed:nativeAudit.status==='native-diagram-consistent'},{id:'native-histories-not-reset',passed:equal(recovered.histories,fixture.histories)}]};
 const records=[encode,...cycle.records,decode],links=records.slice(1).map((r,i)=>({from:records[i].id,to:r.id}));
 // The side context is required evidence, not an unrecorded global variable.
 encode.retainedContext=boundary('native-retained-context',envelope.nativeContext);decode.retainedContext=boundary('native-retained-context',restoredEnvelope.nativeContext);
 links.push({from:encode.id,fromPort:'retainedContext',to:decode.id,toPort:'retainedContext'});
 return {status:fullRecovery&&nativeAudit.status==='native-diagram-consistent'?'recovered-native-diagram':'rejected',envelope,cycle,restoredEnvelope,recovered,nativeAudit,records,links,composition:composeEvidence(records,links),retainedContextUnchanged:equal(envelope.nativeContext,restoredEnvelope.nativeContext),scope:'Representation bridge only. Physical reverse transport is not inferred from endpoint transposition; exact field sewing must be rerun on the recovered native diagram.'};
}
