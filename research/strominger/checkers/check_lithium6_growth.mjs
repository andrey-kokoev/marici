import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import './check_simplex_components.mjs';
import {createHelium3Tunnel} from '../demos/particle-overlap-tetrahedron/helium3-tunnel-model.mjs';
import {createWindowConstruction} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {probeLithium6Growth} from '../demos/particle-overlap-tetrahedron/lithium6-growth-probe.mjs';
import {makeLatticeItem,acrossFace,itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
const keys=lattice.cells.map(c=>itemKey(c.map(i=>lattice.nodes[i].address))),seed=makeLatticeItem('tetrahedron',[0,0,0,0]);
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
let admittedMarkings=0,rejectedMarkings=0,characterCases=0,variantCases=0,example;
for(const permutation of permutations([0,1,2,3])){
 const bindings=Object.fromEntries(['C0','M0','C1','M1'].map((n,i)=>[n,seed.vertices[permutation[i]]]));
 const native=createWindowConstruction({bindings}),n=native.step(),owner=acrossFace(seed,n.events[0].face),incoming=[n.bindings.M0,n.bindings.C2,n.bindings.M1];
 const admitted=owner.faces.some(f=>itemKey(f)===itemKey(incoming));
 if(!admitted){const model=createHelium3Tunnel({bindings});assert.deepEqual(model.snapshot().bindings,bindings);model.step();model.step();assert.throws(()=>model.step(),/does not give a regular second proton seed/);rejectedMarkings++;continue;}
 admittedMarkings++;
 for(const branch of ['common','positive','negative'])for(const phaseExponent of [0,1,2]){
  const model=createHelium3Tunnel({bindings,branch,phaseExponent,complementCoefficients:[[9,-7],[-5,6]]});assert.deepEqual(model.snapshot().bindings,bindings);
  for(let i=0;i<4;i++)model.step();const before=model.snapshot(),bytes=JSON.stringify(before),probe=probeLithium6Growth(before);
  assert.equal(JSON.stringify(before),bytes);assert.deepEqual(model.snapshot(),before);assert.deepEqual(probe.items.slice(0,5),before.items);assert.deepEqual(probe.bindings,before.bindings);
  assert.equal(probe.status,'blocked-retained-core-growth');assert.deepEqual(probe.target,{isotope:'lithium6',proton:3,neutron:3,electron:3});assert.deepEqual(probe.retainedCounts,{proton:2,neutron:2,electron:2});assert.equal(probe.items.length,6);assert.equal(new Set(probe.items.map(i=>i.key)).size,6);assert.ok(probe.items.every(i=>keys.includes(i.key)));
  assert.equal(probe.ports.length,16);assert.equal(probe.ports.filter(p=>p.kind==='PN').length,8);assert.equal(probe.nuclearInterfaces,4);assert.equal(probe.freeNuclearPorts,0);assert.equal(probe.freeElectronPorts,2);assert.equal(probe.electronCandidates.length,2);
  for(const index of [0,1,3,5]){const ports=probe.ports.filter(p=>p.item===index&&p.kind==='PN');assert.equal(ports.length,2);assert.ok(ports.every(p=>p.occupiedBy!==null));}
  for(const e of probe.electronCandidates){assert.ok(keys.includes(e.item.key));assert.ok(!probe.items.some(i=>i.key===e.item.key));assert.ok(probe.items[5].faces.some(f=>itemKey(f)===itemKey(e.face)));}
  assert.deepEqual(probe.variants.map(v=>v.operatorOrder),[3,2,2,3]);assert.equal(new Set(probe.variants.map(v=>JSON.stringify(v.choices))).size,4);
  for(const v of probe.variants){assert.equal(v.freeNuclearPorts,0);assert.equal(v.canAddProton,false);assert.equal(v.canAddNeutron,false);assert.equal(v.disposition,'blocked-before-transport');variantCases++;}
  assert.equal(probe.ambiguityResolved,false);assert.equal(probe.constructedLithium,false);assert.equal(probe.newCarriersCommitted,0);characterCases++;
  if(permutation.join('')==='0123'&&branch==='positive'&&phaseExponent===0)example=probe;
 }
}
assert.equal(admittedMarkings,8);assert.equal(rejectedMarkings,16);assert.equal(characterCases,72);assert.equal(variantCases,288);
assert.deepEqual(example.items.map(i=>keys.indexOf(i.key)),[0,13,16,24,14,7]);assert.deepEqual(example.electronCandidates.map(e=>keys.indexOf(e.item.key)).sort((a,b)=>a-b),[6,8]);
assert.throws(()=>probeLithium6Growth(createHelium3Tunnel().snapshot()),/completed retained helium-3/);
const malformedModel=createHelium3Tunnel();for(let i=0;i<4;i++)malformedModel.step();const malformed=malformedModel.snapshot();malformed.items[1].faces.pop();assert.throws(()=>probeLithium6Growth(malformed),/actual tetrahedron/);
const out='research/strominger/results/lithium6-growth';await mkdir(out,{recursive:true});
await writeFile(out+'/probe.json',JSON.stringify(example,null,2)+'\n');
await writeFile(out+'/verification.json',JSON.stringify({status:'pass-blocked-growth-diagnostic',target:example.target,retainedCounts:example.retainedCounts,retainedCellIds:example.items.map(i=>keys.indexOf(i.key)),deficit:example.deficit,nuclearInterfaces:4,nuclearPortIncidences:8,freeNuclearPorts:0,freeElectronPorts:2,defaultElectronContinuationCells:[6,8],admittedSeedMarkings:admittedMarkings,rejectedSeedMarkings:rejectedMarkings,characterPhaseCases:characterCases,readerVariantCases:variantCases,allFourReaderChoicesBlocked:true,ambiguityResolved:false,lithiumConstructed:false,viewerAdmitted:false,physicalLithiumImpossibilityClaimed:false,scope:example.scope},null,2)+'\n');
console.log('PASS Li-6 growth probe: all four He-4 reader choices have saturated PN ports; no new P or N. Two electron continuations do not supply a lithium nucleus. 8 admitted seed markings × 9 characters/phases × 4 alternatives; 16 markings rejected by the fixed subdivision.');
