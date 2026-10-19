// Source audit: geometry references, available readers and occupied bodies differ.
import assert from 'node:assert/strict';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {GenerativeAssemblyRules,applyPhasePermutation} from '../demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {phaseUniverse} from '../demos/particle-overlap-tetrahedron/local-reference-universe.mjs';
const root=new URL('../../../',import.meta.url),base=new URL('../results/',import.meta.url),hashes={};
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
async function load(url){const bytes=await readFile(url);hashes[fileURLToPath(url).slice(fileURLToPath(root).length).replaceAll('\\','/')]=hash(bytes);return JSON.parse(bytes);}
function rooted(rules,ids){const selected=new Set(ids),seen=new Set([rules.root]),queue=[rules.root];assert(selected.has(rules.root));for(let i=0;i<queue.length;i++)for(const index of rules.outgoing(queue[i])){const op=rules.operations[index];if(selected.has(op.target)&&!seen.has(op.target)){seen.add(op.target);queue.push(op.target);}}return seen.size===selected.size;}
const hydrogen=await load(new URL('hydrogen-edge-attachment/verification.json',base));
const local=[];let rejected=0;
for(const [mark,h] of hydrogen.rows.entries()){
 const aliases=h.bodies[0].aliases,seedBindings=Object.fromEntries(['C0','M0','C1','M1'].map(name=>[name,aliases[name]]));
 const rules=new GenerativeAssemblyRules({seedBindings}),p=rules.root;
 const pn=rules.operations[rules.outgoing(p).find(index=>rules.operations[index].kind==='PN')],n=pn.target;
 const ne=rules.operations[rules.outgoing(n).find(index=>rules.operations[index].kind==='NE')],e=ne.target;
 const pc=rules.charts[rules.packets[p].chart],nc=rules.charts[rules.packets[n].chart],ec=rules.charts[rules.packets[e].chart];
 const seed=rules.describe([p]);assert(seed.valid);assert(!seed.bodies.has(nc.cell));
 assert.equal(rules.geometry.neighbor(pc.cell,['M0','C1','M1'].map(k=>pc.aliases[k])),nc.cell);
 assert.equal(pc.aliases.C2,nc.aliases.C2);assert.equal(rules.geometry.cells[nc.cell].geometry,'split');
 // Generation/validation creates available reader maps, not selected bodies.
 assert(rules.validateTransfer(pn));assert(rules.validateTransfer(ne));
 const afterGeneration=rules.inspect([p]);assert.deepEqual(afterGeneration.counts,{proton:1,neutron:0,electron:0});
 const input=Array.from({length:5},(_,i)=>[i+1,0]),zero=Array.from({length:5},()=>[0,0]);
 const intermediate=applyPhasePermutation(input,rules.packets[n].permutation);
 const absentResponse=applyPhasePermutation(zero,rules.packets[n].permutation);
 assert(intermediate.some(([x,y])=>x!==0||y!==0));assert(absentResponse.every(([x,y])=>x===0&&y===0));
 assert.deepEqual(rules.inspect([p]).counts,afterGeneration.counts);
 const pe=rules.inspect([p,e]),pne=rules.inspect([p,n,e]);
 assert(pe.valid&&!pe.certifiedExit&&!rooted(rules,[p,e]));
 assert.deepEqual(pe.counts,{proton:1,neutron:0,electron:1});
 assert(pne.valid&&pne.certifiedExit&&rooted(rules,[p,n,e]));
 assert.deepEqual(pne.counts,{proton:1,neutron:1,electron:1});
 assert(pe.allContactsWitnessed);assert.equal(pe.links.length,0);
 const edge=rules.geometry.cells[pc.cell].vertices.filter(v=>rules.geometry.cells[ec.cell].vertices.includes(v));
 assert.equal(edge.length,2);
 const composite=ne.permutation.map(i=>pn.permutation[i]);
 for(const kind of ['PE','NE','PN']){
  const forged={source:p,target:e,kind,phaseDelta:0,permutation:composite,face:edge};
  assert.throws(()=>rules.validateTransfer(forged));rejected++;
 }
 local.push({mark,referenceNeutronCell:nc.cell,referenceNeutronOccupied:false,availableNeutronReader:n,
   coefficientResponseCanBeNonzeroWithoutSelection:true,geometryOnlyPECompatible:pe.valid,nativePERooted:false,nativePEExitCertified:false,nativePNECertified:true});
}
const isotopeReferences=[];
for(const isotope of ['n15','ne22']){
 const directory=new URL(`reference-${isotope}-search/`,base),summary=await load(new URL('verification.json',directory));
 const row=summary.rows.find(row=>row.witnessFile),saved=(await load(new URL(row.witnessFile,directory))).witness;
 const universe=phaseUniverse({maxOrigin:row.maxOrigin}),{rules}=universe;assert(universe.complete);
 // Fresh generation, exact saved identity checks, then original whole-assembly gates.
 for(const packet of saved.packets)assert.deepEqual(rules.packets[packet.id],packet);
 for(const chart of saved.charts)assert.deepEqual(rules.charts[Number(chart.id.split('-').at(-1))],chart);
 for(const op of saved.operations)assert.deepEqual(rules.operations[op.id],op);
 const ids=saved.selectedPackets,selected=new Set(ids),description=rules.describe(ids),inspection=rules.inspect(ids);
 assert(description.valid&&inspection.certifiedExit&&inspection.allContactsWitnessed&&rooted(rules,ids));
 assert.deepEqual(inspection.counts,saved.inspection.counts);
 const missing=[];
 for(const id of ids){
  const packet=rules.packets[id],chart=rules.charts[packet.chart];if(chart.species!=='neutron')continue;
  const face=['M0','C1','M1'].map(k=>chart.aliases[k]),reference=rules.geometry.neighbor(chart.cell,face);
  assert.equal(rules.geometry.cells[reference].geometry,'proton');
  assert.equal(chart.aliases.C0,rules.geometry.apex(reference,face));
  if(description.bodies.has(reference))continue;
  const incoming=inspection.links.map(index=>rules.operations[index]).filter(op=>op.target===id);
  assert(incoming.length>0);assert(incoming.every(op=>['NN-phase-advance','reader-phase-advance'].includes(op.kind)));
  assert(incoming.every(op=>selected.has(op.source)&&description.bodies.has(rules.charts[rules.packets[op.source].chart].cell)));
  missing.push({packet:id,neutronCell:chart.cell,referenceProtonCell:reference,incoming:incoming.map(op=>({id:op.id,kind:op.kind,source:op.source}))});
 }
 for(const opId of inspection.links){const op=rules.operations[opId];assert(selected.has(op.source)&&selected.has(op.target));}
 isotopeReferences.push({isotope,maxOrigin:row.maxOrigin,completeUniversePackets:universe.packets.length,counts:inspection.counts,
   rooted:true,allContactsWitnessed:true,allSelectedRecordsReachExit:true,referenceOnlyProtonRecords:missing});
}
assert.equal(isotopeReferences.find(row=>row.isotope==='n15').referenceOnlyProtonRecords.length,0);
assert.equal(isotopeReferences.find(row=>row.isotope==='ne22').referenceOnlyProtonRecords.length,2);
assert(isotopeReferences.find(row=>row.isotope==='ne22').referenceOnlyProtonRecords.every(row=>row.incoming.every(op=>op.kind==='reader-phase-advance')));
const result={schema:'marici.reference-occupancy-semantics.v1',status:'pass',localCases:local,
 isotopeReferences,invalidNativePEControlsRejected:rejected,
 sourceDefinition:{occupied:'image of selected packet charts under cell/species; duplicate readers on a body do not add particles',
 reference:'completeP and completeN fill geometric context without selecting the referenced body',
 response:'permutation of root coefficients, available independently of whether its packet is selected',
 admission:'selected source/target operation links plus rooted construction, role/contact guards and selected-record exits'},
 conclusion:'Reference-only geometry is already allowed for both P and N. The experimental PE proposal adds use of an unselected N reader as an operational intermediate, not merely permission to reference N geometry.',
 scope:'Source implementation and finite generated-witness audit, not a derived physical number operator, amplitude-based occupancy criterion or new native isotope admission.'};
for(const relative of ['research/strominger/checkers/check_reference_occupancy_semantics.mjs','research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs','research/strominger/demos/particle-overlap-tetrahedron/local-reference-universe.mjs','research/strominger/reference-occupancy-semantics-v1.md'])hashes[relative]=hash(await readFile(new URL(relative,root)));
result.sourceHashes=hashes;
const out=new URL('reference-occupancy-semantics/',base);await mkdir(out,{recursive:true});await writeFile(new URL('verification.json',out),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,hydrogenMarkings:local.length,invalidNativePEControlsRejected:rejected,
 referenceOnlyProtonRecords:isotopeReferences.map(row=>({isotope:row.isotope,records:row.referenceOnlyProtonRecords.length})),conclusion:result.conclusion},null,2));
