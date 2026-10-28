// A proposed lossless face OFFER, not a native transfer or receiver operation.
// The outgoing face is a required control parameter, not inferred from records.
import assert from 'node:assert/strict';
import {validateCentralReferencePacket} from './su32-central-reference-completion.mjs';
const copy=x=>structuredClone(x);
const exact=(x,names)=>assert.deepEqual(Object.keys(x).sort(),[...names].sort());
export function centralOutgoingAttachments(layout,fixture,domain){
 assert.equal(domain.id,layout.chart.reading);
 return domain.arrows.filter(a=>a.from===layout.chart.target).map(a=>{
  const face=fixture.interfaces.find(f=>f.id===a.id);assert(face,'Outgoing arrow has no original physical face');
  assert.deepEqual([...face.ports].sort(),[a.from+'@'+a.id,a.to+'@'+a.id].sort());
  return {interfaceId:a.id,from:a.from,to:a.to,sourcePort:a.from+'@'+a.id,destinationPort:a.to+'@'+a.id,
   nativeInterfaceWitness:copy(face.witness)};
 });
}
export function offerCentralPacketAtFace(layout,fixture,domain,packet,interfaceId){
 validateCentralReferencePacket(layout,packet);
 assert.equal(typeof interfaceId,'string','An explicit outgoing interface choice is required');
 const attachment=centralOutgoingAttachments(layout,fixture,domain).find(a=>a.interfaceId===interfaceId);
 assert(attachment,'Chosen interface is not an outgoing face at this central occurrence');
 return {kind:'su32-central-outgoing-face-offer-candidate',attachment,packet:copy(packet),
  faceChoiceAuthority:'supplied-control-not-derived-from-records',nativeExecution:null};
}
export function recoverCentralPacketFromOffer(layout,fixture,domain,offer){
 exact(offer,['kind','attachment','packet','faceChoiceAuthority','nativeExecution']);
 assert.equal(offer.kind,'su32-central-outgoing-face-offer-candidate');
 assert.deepEqual(offer,offerCentralPacketAtFace(layout,fixture,domain,offer.packet,offer.attachment.interfaceId));
 return copy(offer.packet);
}
