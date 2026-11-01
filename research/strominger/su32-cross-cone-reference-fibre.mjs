// One context-indexed refinement of an existing JSON reference fibre.
// Carries the full producer point literally; not a newly inferred native law.
import assert from 'node:assert/strict';
import {channelOperand,compareAt,validateComparisonNode} from './su32-layer4-comparison.mjs';
export function refineReference(sourceLayout,cell,point){
 assert(point&&typeof point==='object','Not a comparison packet');
 validateComparisonNode(sourceLayout,point);
 assert.equal(point.kind,'comparison');assert.equal(point.at,cell);
 return structuredClone(point);
}
function referenceSlots(targetLayout,cell,joint){
 const c=targetLayout.template.channels.find(c=>c.cell===joint);assert(c,'Not a consumer channel');
 const refs=[c.P,c.E],selected=refs.filter(r=>r.referenceCell===cell);assert.equal(selected.length,1);
 return {selected:selected[0],other:refs.find(r=>r.referenceCell!==cell)};
}
export function attachReference(sourceLayout,targetLayout,cell,joint,point,otherPayload){
 const value=refineReference(sourceLayout,cell,point),slots=referenceSlots(targetLayout,cell,joint);
 // This invokes the unchanged API; the upstream packet is the payload, not a
 // newly decoded scalar, a header, or a wrapper around the packet.
 return channelOperand(targetLayout,joint,{[slots.selected.record]:value,[slots.other.record]:otherPayload});
}
export function splitAttachment(sourceLayout,targetLayout,cell,joint,consumer){
 validateComparisonNode(targetLayout,consumer);assert.equal(consumer.kind,'channel');assert.equal(consumer.at,joint);
 const slots=referenceSlots(targetLayout,cell,joint);
 const point=refineReference(sourceLayout,cell,consumer.records[slots.selected.record].payload);
 const otherPayload=structuredClone(consumer.records[slots.other.record].payload);
 const reconstructed=compareAt(sourceLayout,cell,...point.children);
 assert.deepEqual(reconstructed,point);
 assert.deepEqual(attachReference(sourceLayout,targetLayout,cell,joint,point,otherPayload),consumer);
 return {producerInputs:structuredClone(point.children),point,otherPayload};
}
