import assert from 'node:assert/strict';
import {writeFile} from 'node:fs/promises';
import {createWindowConstruction,windowProtocol} from '../strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {transportCarrierCoefficients,referenceCarrierMarks,windowModeCoefficients} from '../strominger/demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs';
import {nativePhaseFrame,auditPhaseCombination} from '../strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const copy=x=>structuredClone(x),key=p=>JSON.stringify(p);
const initial=createWindowConstruction().snapshot();
function permutations(xs){return xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(rest=>[x,...rest])):[[]];}
const generic=[[2,-3],[1,4],[-2,5],[7,-1],[-5,6]];
const inputs=[generic,...Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>[i===j?1:0,0])),
 ...['common','positive','negative'].flatMap(branch=>[0,1,2].map(phaseExponent=>[...windowModeCoefficients({branch,phaseExponent}),[9,-7],[-5,6]]))];
let built=0,tested=0,blocked=0;const examples=[];
for(const vertices of permutations(initial.items[0].vertices)){
 const bindings=Object.fromEntries(windowProtocol[0].nodes.map((n,i)=>[n,vertices[i]]));
 const model=createWindowConstruction({bindings});model.step();const packet=model.step();
 if(packet.status!=='complete'){blocked++;continue;}built++;
 const [pn,ne]=packet.events;
 const frames=packet.items.map((item,i)=>nativePhaseFrame(String(i),item.species,Object.fromEntries(Object.entries(packet.bindings).map(([n,p])=>[n,key(p)]))));
 const interfaces=packet.events.map((e,i)=>({from:String(i),to:String(i+1),kind:i===0?'PN':'NE',identification:'same-occurrence',vertices:e.face.map(key)}));
 const phase=auditPhaseCombination(frames,interfaces);assert.equal(phase.status,'native-phase-compatible');
 assert.equal(interfaces[0].to,interfaces[1].from); // literally one N frame
 const nBody=packet.items[1];
 assert.equal(new Set(nBody.vertices.map(key)).size,4);
 const pnSlots=pn.frameExchange.map(n=>referenceCarrierMarks.indexOf(n));
 const neSlots=ne.frameExchange.map(n=>referenceCarrierMarks.indexOf(n));
 assert(pnSlots.every(i=>!neSlots.includes(i)));
 for(const input of inputs){
  const nFromP=transportCarrierCoefficients(input,pn,1);
  const electron=transportCarrierCoefficients(nFromP,ne,1);
  const nFromE=transportCarrierCoefficients(electron,ne,-1);
  assert.deepEqual(nFromE,nFromP);
  assert.deepEqual(transportCarrierCoefficients(nFromE,pn,-1),input);
  assert.deepEqual(transportCarrierCoefficients(transportCarrierCoefficients(input,pn),pn),input);
  assert.deepEqual(transportCarrierCoefficients(transportCarrierCoefficients(nFromP,ne),ne),nFromP);
  // Algebraic coefficient operators commute; NOT a second admitted species route.
  const reversedOperatorOrder=transportCarrierCoefficients(transportCarrierCoefficients(input,ne),pn);
  assert.deepEqual(reversedOperatorOrder,electron);
  assert.deepEqual(transportCarrierCoefficients(transportCarrierCoefficients(electron,pn),ne),input);
  assert.deepEqual([input[2],nFromP[2],electron[2]],[input[2],input[2],input[2]]);
  tested++;
 }
 if(!examples.length){
  const neutron=transportCarrierCoefficients(generic,pn),electron=transportCarrierCoefficients(neutron,ne);
  const wrong=copy(electron);wrong[4][0]++;
  assert.notDeepEqual(transportCarrierCoefficients(wrong,ne,-1),neutron);
  examples.push({bindings:packet.bindings,bodies:packet.items,frames,interfaces,phase,
   slotOrder:referenceCarrierMarks,pnSlots,neSlots,input:generic,neutron,electron,
   sharedNeutronRecord:{bodyKey:nBody.key,frame:frames[1],coefficients:neutron,
    comparisonHistories:{fromProton:['PN'],fromElectron:['inverse-NE']}}});
 }
}
assert(built>0);
const out={status:'pass-shared-native-neutron-reference-duality',rootMarkings:24,built,blocked,tested,examples,
 conclusions:{singleNeutronBodyAndFrame:true,sameFiveSlotNeutronFromBothSides:true,
 PNandNECoefficientMapsInvolutions:true,composedPECoefficientMapInvolution:true,
 independentDirectFaceAttachedPEComparisonVerified:false,historyErased:false},
 scope:['Uses existing native geometry and declared full-five-slot reference maps; no new inverse law.',
 'Inverse coefficient comparison does not assert an admitted forward E->N realization event.',
 'Commutation is an algebraic equality on the common reference carrier, not permission to apply NE to a proton as a typed event.',
 'The two comparison histories are retained, not equated.',
 'P and E in this triple share an edge. Earlier face-attached PE example has a different incidence; no cross-configuration identification is supplied.',
 'Not a physical isotope derivation or a proof that a neutron filler is uniquely forced by arbitrary PE placement.']};
await writeFile(new URL('./results/shared-neutron-duality-v1.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({status:out.status,built,blocked,tested,marks:referenceCarrierMarks,pnSlots:examples[0].pnSlots,neSlots:examples[0].neSlots}));
