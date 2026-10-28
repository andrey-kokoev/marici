import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders,compareAt} from '../su32-layer4-comparison.mjs';
import {prepareCentralReferencePacket,selectCentralReference} from '../su32-central-reference-completion.mjs';
import {centralOutgoingAttachments,offerCentralPacketAtFace,recoverCentralPacketFromOffer} from '../su32-central-outgoing-face-offer.mjs';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h);
const atlas=buildSu32SignedReferenceAtlas(fixture),reading=fixture.readings.find(r=>r.id==='reading:0:-1');
const chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);assert(chart);
// Fix the complete source incidence domain before any payload or face choice.
const domain=buildFiveSideOctComparisonDomain(buildPESymmetricSector(1),{readingIds:[reading.id]}).readings[0];
const labels=['P+','P-','E+','E-'];
const registries=[...Array.from({length:16},(_,bits)=>Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1]))),
 Object.fromEntries(labels.map((k,i)=>[k,{id:'input:'+k,value:i,provenance:{entry:reading.incomingN}}]))];
let preparations=0,exactRecoveries=0,selectionSquares=0,historyDistinctions=0;let example;
for(const p of [0,1])for(const e of [0,1]){
 const layout=comparisonLayout(atlas,fixture,chart.id,[p,e]);
 const menu=centralOutgoingAttachments(layout,fixture,domain);assert.equal(menu.length,4);
 assert.equal(new Set(menu.map(a=>a.interfaceId)).size,4);
 assert.equal(new Set(menu.map(a=>a.to)).size,4);
 for(const registry of registries){
  const built=reconcileBothOrders(layout,registry),start=prepareCentralReferencePacket(layout,built.byE,built.byP);
  const changed=selectCentralReference(layout,start,'E-'),returned=selectCentralReference(layout,changed,'E+');
  assert.deepEqual(start.core,returned.core);assert.notDeepEqual(start,returned);preparations++;
  for(const packet of [start,changed,returned])for(const face of menu){
   const snapshot=structuredClone(packet),offer=offerCentralPacketAtFace(layout,fixture,domain,packet,face.interfaceId);
   assert.deepEqual(recoverCentralPacketFromOffer(layout,fixture,domain,offer),packet);exactRecoveries++;
   assert.deepEqual(offer.packet.core.records,packet.core.records);assert.deepEqual(packet,snapshot);
   assert.equal(offer.attachment.from,packet.core.at);assert.equal(offer.nativeExecution,null);
   assert.equal(offer.attachment.nativeInterfaceWitness,null);
   // Selection and face offering commute as DATA operations at a FIXED supplied
   // face. This is not a command executed by the receiving physical cell.
   const after=selectCentralReference(layout,packet,packet.activeReference==='E+'?'E-':'E+');
   const selectThenOffer=offerCentralPacketAtFace(layout,fixture,domain,after,face.interfaceId);
   const offerThenSelect={...structuredClone(offer),packet:selectCentralReference(layout,
    recoverCentralPacketFromOffer(layout,fixture,domain,offer),after.activeReference)};
   assert.deepEqual(selectThenOffer,offerThenSelect);selectionSquares++;
  }
  for(const face of menu){
   const initialOffer=offerCentralPacketAtFace(layout,fixture,domain,start,face.interfaceId);
   const returnOffer=offerCentralPacketAtFace(layout,fixture,domain,returned,face.interfaceId);
   assert.deepEqual(initialOffer.attachment,returnOffer.attachment);
   assert.deepEqual(initialOffer.packet.core,returnOffer.packet.core);
   assert.notDeepEqual(initialOffer,returnOffer);historyDistinctions++;
  }
  if(!example&&registry['P+']?.id)example={layout,built,start,menu,
   offers:menu.map(face=>offerCentralPacketAtFace(layout,fixture,domain,start,face.interfaceId))};
 }
}
const {layout,built,start,menu,offers}=example;
// Four different attachment extensions of EXACTLY THE SAME complete packet.
// This shows current constraints underdetermine a choice, not that a separately
// supplied deterministic selector is impossible.
for(const offer of offers)assert.deepEqual(offer.packet,start);
assert.equal(new Set(offers.map(o=>JSON.stringify(o.attachment))).size,4);
let negativeControls=0;const reject=f=>{assert.throws(f);negativeControls++;};
reject(()=>offerCentralPacketAtFace(layout,fixture,domain,start));
reject(()=>offerCentralPacketAtFace(layout,fixture,domain,start,'absent'));
const incoming=domain.arrows.find(a=>a.to===chart.target);assert(incoming);
reject(()=>offerCentralPacketAtFace(layout,fixture,domain,start,incoming.id));
const corrupt=f=>{const bad=structuredClone(offers[0]);f(bad);reject(()=>recoverCentralPacketFromOffer(layout,fixture,domain,bad));};
corrupt(o=>{o.attachment.destinationPort=o.attachment.sourcePort;});
corrupt(o=>{o.attachment.to=menu[1].to;});
corrupt(o=>{o.packet.core.at=o.attachment.to;});
corrupt(o=>{delete o.packet.core.records['E-'];});
corrupt(o=>{o.packet.core.derivations.byP=o.packet.core.derivations.byE;});
corrupt(o=>{o.nativeExecution={claimed:true};});
corrupt(o=>{o.faceChoiceAuthority='derived-from-records';});
// The offered copy does not alias mutable callers.
const mutable=structuredClone(start),snapshot=structuredClone(mutable);
const copied=offerCentralPacketAtFace(layout,fixture,domain,mutable,menu[0].interfaceId);
mutable.core.records['P+'].payload={laterMutation:true};assert.deepEqual(copied.packet,snapshot);
const receiverRefusals=[];
for(const face of menu){
 assert.throws(()=>compareAt(layout,face.to,built.byE,built.byP),error=>{
  assert.match(error.message,/Not a layer-4 comparison/);
  receiverRefusals.push({at:face.to,error:error.message});return true;
 });
}
const continuationBoundaries=domain.comparisons.filter(c=>c.source===chart.target);
assert(continuationBoundaries.length>0);
assert(continuationBoundaries.every(c=>c.comparisonMap===null&&c.fillingWitness===null));
const sources=[fixturePath,'research/strominger/su32-central-outgoing-face-offer.mjs',
 'research/strominger/su32-central-reference-completion.mjs','research/strominger/su32-layer4-comparison.mjs',
 'research/strominger/su32-signed-reference-encoder.mjs','research/realization-tower/five-side-oct-comparison-domain.mjs',
 'research/strominger/checkers/check_su32_central_outgoing_face_offer.mjs'];
const hashes={};for(const p of sources)hashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const report={schema:'su32.central-outgoing-face-offer-candidate.v1',passed:true,reading:reading.id,
 preparations,exactRecoveries,selectionSquares,historyDistinctions,negativeControls,
 example:{centralPacket:start,outgoingAttachments:menu,distinctOffersForSamePacket:offers},
 receiverRefusals,continuationBoundaries,
 conclusions:{losslessSelectedFaceOffer:'A left-invertible data envelope exists for every supplied outgoing face, preserving all four records and both derivations.',
  selection:'The present constraints admit four different face offers for the same complete packet. An explicit control or further selection law is required to choose one.',
  nativeContinuation:'Unverified: current comparison grammar refuses all four receiver sites; the sourced continuation comparison maps and interface witnesses remain unbound.',
  conjecture:'Conditional information-level face attachment succeeds. This does not verify or universally falsify the stronger native conjecture.'},
 limits:['The offer is a product-like data extension, not an encoding in a proved native face-state carrier.',
  'The chosen interface is additional control information, not a new independent P/E record.',
  'The data selection square supplies no receiver execution or higher coherence.',
  'Receiver rejection is scoped to the current layer-4 comparison API, not an impossibility theorem for another grammar.',
  'No arbitrary-tree theorem or new global physical routing is claimed.'],nativeExecution:null,sourceHashes:hashes};
const dir='research/strominger/results/su32-central-outgoing-face-offer-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,example:undefined,continuationBoundaries:continuationBoundaries.map(c=>({id:c.id,status:c.status,comparisonMap:c.comparisonMap,fillingWitness:c.fillingWitness})),sourceHashes:undefined},null,2));
