import {activePhaseSlots,applyPhasePermutation,phaseFrame} from './demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {windowProtocol} from './demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {carriers as coefficientMarks} from './demos/particle-overlap-tetrahedron/model.mjs';
import {boundary,composeEvidence} from './fibration-evidence.mjs';
import {isDeepStrictEqual as equal} from 'node:util';
const complexVector=v=>Array.isArray(v)&&v.length===5&&v.every(z=>Array.isArray(z)&&z.length===2&&z.every(Number.isFinite));
function resolve(f,id){const packet=f.packets.find(p=>p.id===id),chart=f.charts.find(c=>c.index===packet?.chart);if(!packet||!chart)throw Error('Unknown native packet/chart');return {packet,chart};}
export function retainNativeWindow(fixture,packetId,value){
 if(!complexVector(value))throw Error('Expected all five complex native coefficients');
 const {packet,chart}=resolve(fixture,packetId),slots=activePhaseSlots[chart.species];
 return {kind:'native-window-with-complement',packetId,frame:phaseFrame(chart,packet.origin),active:slots.map(slot=>({slot,mark:coefficientMarks[slot],value:[...value[slot]]})),complement:coefficientMarks.flatMap((mark,slot)=>slots.includes(slot)?[]:[{slot,mark,value:[...value[slot]]}]),fullFieldReference:{rootPacket:fixture.rootPacket,framePacket:packetId,dimension:44,status:'reference-to-prior-sewn-field-not-a-materialized-field-value'}};
}
export function restoreNativeWindow(fixture,view){
 if(view?.kind!=='native-window-with-complement')throw Error('Missing retained window packet');
 const {packet,chart}=resolve(fixture,view.packetId),slots=activePhaseSlots[chart.species],complement=coefficientMarks.map((_,i)=>i).filter(i=>!slots.includes(i));
 if(!equal(view.frame,phaseFrame(chart,packet.origin))||!Array.isArray(view.active)||!Array.isArray(view.complement)||!equal(view.active.map(r=>r?.slot),slots)||!equal(view.complement.map(r=>r?.slot),complement))throw Error('Window frame, active order or complement was lost');
 const expected=retainNativeWindow(fixture,packet.id,Array.from({length:5},()=>[0,0])).fullFieldReference;
 if(!equal(view.fullFieldReference,expected))throw Error('Lost whole-field/root-frame reference');
 const value=Array(5);for(const r of [...view.active,...view.complement]){if(r.mark!==coefficientMarks[r.slot])throw Error('Coefficient mark changed');value[r.slot]=r.value;}
 if(!complexVector(value))throw Error('Incomplete native coefficient packet');return structuredClone(value);
}
export function transportNativeWindow(fixture,operationId,view){
 const op=fixture.operations.find(o=>o.id===operationId);if(!op||op.source!==view.packetId)throw Error('Wrong native operation source');
 const value=restoreNativeWindow(fixture,view);return retainNativeWindow(fixture,op.target,applyPhasePermutation(value,op.permutation));
}
function projectionAudit(sourceSlots,targetSlots,permutation){
 const pulls=targetSlots.map(i=>permutation[i]),required=[...new Set(pulls.filter(i=>!sourceSlots.includes(i)))],closed=required.length===0;
 let witness=null;if(!closed){const a=Array.from({length:5},()=>[0,0]),b=structuredClone(a);b[required[0]]=[1,0];witness={sourceA:a,sourceB:b,sourceProjectionEqual:equal(sourceSlots.map(i=>a[i]),sourceSlots.map(i=>b[i])),targetProjectionA:targetSlots.map(i=>applyPhasePermutation(a,permutation)[i]),targetProjectionB:targetSlots.map(i=>applyPhasePermutation(b,permutation)[i])};}
 return {sourceSlots,targetSlots,pulledSourceSlots:pulls,requiredComplementSlots:required,closed,witness};
}
export function auditNativeWindowTransport(fixture){
 const cases=[...Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>[i===j?1:0,0])),[[1,2],[3,-4],[5,6],[-7,8],[9,-10]]];
 const edges=fixture.operations.map(op=>{
  const a=resolve(fixture,op.source),b=resolve(fixture,op.target),active=projectionAudit(activePhaseSlots[a.chart.species],activePhaseSlots[b.chart.species],op.permutation);
  const fourSlots=species=>windowProtocol.find(p=>p.species===species).nodes.map(mark=>({mark,slot:coefficientMarks.indexOf(mark)})),sa=fourSlots(a.chart.species),sb=fourSlots(b.chart.species);
  const unbound=[...sa,...sb].filter(r=>r.slot<0).map(r=>r.mark),four=unbound.length?{status:'not-a-four-coefficient-window',unboundGeometricMarks:[...new Set(unbound)]}:{status:'tested',...projectionAudit(sa.map(r=>r.slot),sb.map(r=>r.slot),op.permutation)};
  const transportedCases=cases.map(value=>{const source=retainNativeWindow(fixture,op.source,value),target=transportNativeWindow(fixture,op.id,source),restored=restoreNativeWindow(fixture,target),expected=applyPhasePermutation(value,op.permutation),root=applyPhasePermutation(value,a.packet.permutation,-1),fromRoot=applyPhasePermutation(root,b.packet.permutation);
   return {fullFivePreserved:equal(restored,expected)&&equal(applyPhasePermutation(restored,op.permutation,-1),value),rootReadoutSquare:equal(restored,fromRoot),activeOrderPreserved:equal(target.active.map(r=>r.slot),activePhaseSlots[b.chart.species]),fullFieldReferenceRetained:target.fullFieldReference.rootPacket===source.fullFieldReference.rootPacket&&target.fullFieldReference.framePacket===op.target};});
  return {operation:op.id,kind:op.kind,source:op.source,target:op.target,sourceSpecies:a.chart.species,targetSpecies:b.chart.species,activeProjection:active,fourGeometricMarkProjection:four,transportedCases};
 });
 const passed=edges.every(e=>e.transportedCases.every(c=>Object.values(c).every(Boolean)));
 const record={id:'native:window-transport',adapter:'native-window-transport',input:boundary('native-diagram',fixture),output:boundary('native-window-transport-audit',edges),dependsOn:[],premises:[{id:'native-window:prior-reference-law',status:'assumed',statement:'Use the existing full-five native permutations and activePhaseSlots. Outside-context retention is the prior explicit reference law, not newly derived dynamics.'},{id:'native-window:full44-scope',status:'assumed',statement:'The full44 state stays referenced through the prior sewn field; this codec materializes five native coefficients only and adds no independent context coefficient.'}],claim:'Active triples plus BOTH retained complementary coefficients transport and reconstruct across every actual native interface.',checks:[{id:'all-full-five-window-squares',passed},{id:'interface-coverage',passed:edges.length===fixture.operations.length}]};
 return {status:passed?'retained-window-transport-passed':'rejected',edges,record,composition:composeEvidence([record]),counts:{interfaces:edges.length,probesPerInterface:cases.length,activeProjectionFailures:edges.filter(e=>!e.activeProjection.closed).length,fourCoefficientProjectionFailures:edges.filter(e=>e.fourGeometricMarkProjection.status==='tested'&&!e.fourGeometricMarkProjection.closed).length,geometricContextWithoutCoefficientSlot:edges.filter(e=>e.fourGeometricMarkProjection.status==='not-a-four-coefficient-window').length},scope:'Exact permutation/retained-context audit on five complex coefficients, linked to the previously sewn native diagram. This does not derive all four alternative context readouts, star capacities, physical flux weights, or an ESD7 parent attachment.'};
}
