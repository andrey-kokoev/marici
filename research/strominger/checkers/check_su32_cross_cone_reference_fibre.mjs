import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt,validateComparisonNode} from '../su32-layer4-comparison.mjs';
import {identifyCone,targetFixture} from '../su32-cone-operation-transport.mjs';
import {attachReference,splitAttachment,refineReference} from '../su32-cross-cone-reference-fibre.mjs';
import {buildSulfur32Wiring,groupSulfurPayloads,restoreSulfurPayloads} from '../../realization-tower/sulfur-32-wiring.mjs';
const root='research/strominger',paths={source:root+'/results/su32-hopf-tests-v1/fixture.json',
 carrier:root+'/results/su32-edge5-extension-contract-v1/verification.json',
 transport:root+'/results/su32-edge5-operadic-transport-v1/verification.json',
 contract:root+'/contracts/su32-cross-cone-reference-fibre-v1.json'};
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const docs={},sourceHashes={};for(const [k,p] of Object.entries(paths)){
 docs[k]=JSON.parse(await fs.readFile(p,'utf8'));sourceHashes[p]=await digest(p);
 for(const [s,h] of Object.entries(docs[k].sourceHashes??{}))assert.equal(await digest(s),h,`Stale ${s}`);
}
const source=docs.source,carrier=docs.carrier.edge5Carrier,sa=buildSu32SignedReferenceAtlas(source);
const reading=source.readings.find(r=>r.id==='reading:0:-1'),sc=sa.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);
const sourceCone=reading.cones.find(c=>c.source===sc.source&&c.target===sc.target);
const iso=carrier.comparisonCones.map(c=>identifyCone(source,sc,sourceCone,carrier,c));
const atlas={charts:iso.map(i=>i.chart),roles:Object.fromEntries(carrier.cells.map(c=>[c.id,c.role])),globalAssignment:null};
const fixture=targetFixture(carrier),charts=new Map(atlas.charts.map(c=>[c.id,c]));
const bindings=[[0,0],[0,1],[1,0],[1,1]],layouts=new Map();
for(const c of atlas.charts)for(const b of bindings)layouts.set(JSON.stringify([c.id,b]),comparisonLayout(atlas,fixture,c.id,b));
const layout=(id,b)=>layouts.get(JSON.stringify([id,b]));
const contacts=docs.transport.crossLevelContacts;assert.equal(contacts.length,224);
// Complete contextual support FIRST. Reference values are fields, not the
// comparison-packet inputs of the old C→R two-corolla fragment.
const family=contacts.map(c=>{
 const consumer=charts.get(c.consumerChart),appearances=consumer.joints.filter(j=>j.P===c.cell||j.E===c.cell);
 assert.equal(appearances.length,2);
 const attachments=appearances.map(j=>{
  const face=carrier.faces.filter(f=>f.owners.length===2&&f.owners.includes(c.cell)&&f.owners.includes(j.cell));assert.equal(face.length,1);
  return {joint:j.cell,face:face[0].id};
 });
 return {...c,classification:'reference-value reuse; exposed types differ',
  producerColour:'context-indexed full comparison packet',consumerField:'opaque JSON payload of a referenced record',
  sameExposedColour:false,rerootingAloneSuffices:false,attachments};
});
// A complete bank of test source points is prepared before evaluating readers.
const producers=new Map();
for(const c of contacts)for(const b of bindings)for(let sample=0;sample<2;sample++){
 const id=JSON.stringify([c.producerChart,c.cell,b,sample]);if(producers.has(id))continue;
 const l=layout(c.producerChart,b),comparison=l.template.comparisons.find(x=>x.cell===c.cell);assert(comparison);
 const registry=Object.fromEntries(Object.entries(l.template.referenceBinding).map(([cell,label])=>[label,
  sample===0?null:{reference:cell,opaque:['unchanged',false],literal:sc.source}]));
 const children=comparison.inputs.map(j=>channelOperand(l,j,registry));
 producers.set(id,{id,layout:l,point:compareAt(l,c.cell,...children),sample});
}
let squares=0,restrictions=0,scalarControls=0,headerControls=0,wrapperControls=0;
let example=null,typeWitness=null;const occurrenceWitnesses=[];
for(const c of family)for(const sb of bindings)for(const tb of bindings)for(let sample=0;sample<2;sample++){
 const p=producers.get(JSON.stringify([c.producerChart,c.cell,sb,sample])),sl=p.layout,tl=layout(c.consumerChart,tb);
 const selected=tl.template.referenceBinding[c.cell];assert(selected);
 const retained=[];
 for(const {joint,face} of c.attachments){
  const refs=tl.template.channels.find(x=>x.cell===joint),other=[refs.P,refs.E].find(r=>r.referenceCell!==c.cell);
  const z=sample===0?false:{otherReference:other.referenceCell,retain:[sc.source,null]};
  const value=attachReference(sl,tl,c.cell,joint,p.point,z);
  const globalEvaluation=channelOperand(tl,joint,{[selected]:p.point,[other.record]:z});
  assert.deepEqual(value,globalEvaluation);
  const parts=splitAttachment(sl,tl,c.cell,joint,value);
  assert.deepEqual(parts.point,p.point);assert.deepEqual(parts.producerInputs,p.point.children);assert.deepEqual(parts.otherPayload,z);
  assert.deepEqual(attachReference(sl,tl,c.cell,joint,parts.point,parts.otherPayload),value);squares++;
  retained.push(value.records[selected].payload);
  // The old unrestricted reference fibre is strictly larger than the producer fibre.
  const scalar=channelOperand(tl,joint,{[selected]:false,[other.record]:z});validateComparisonNode(tl,scalar);
  assert.throws(()=>splitAttachment(sl,tl,c.cell,joint,scalar));scalarControls++;
  const {children,...header}=p.point;
  const reduced=channelOperand(tl,joint,{[selected]:header,[other.record]:z});
  assert.throws(()=>splitAttachment(sl,tl,c.cell,joint,reduced));headerControls++;
  const wrapped=channelOperand(tl,joint,{[selected]:{retained:p.point},[other.record]:z});
  assert.throws(()=>splitAttachment(sl,tl,c.cell,joint,wrapped));wrapperControls++;
  example??={contact:c,sourceBinding:sb,targetBinding:tb,sourcePoint:p.point,otherPayload:z,consumer:value,parts,sharedFace:face};
  typeWitness??={sourceType:'valid comparison packet at the specified occurrence',targetAcceptedScalar:scalar,
   observation:'The unrefined target accepts false; the source comparison fibre does not. Arc reversal or re-rooting cannot make these exposed types identical.'};
 }
 assert.deepEqual(retained[0],retained[1]);assert.deepEqual(retained[0],p.point);restrictions++;
}
// An actual different valid producer at the SAME cell is not the same fibre point.
const byCell=new Map();for(const p of producers.values())if(p.sample===1&&p.layout.anchor.binding.every(x=>x===0)){
 if(!byCell.has(p.point.at))byCell.set(p.point.at,[]);byCell.get(p.point.at).push(p);
}
for(const [cell,ps] of byCell)if(ps.length>1){
 assert.equal(ps.length,2,'Enumerate every same-cell context pair, not just a selected pair');
 const [a,b]=ps;assert.notDeepEqual(a.point.anchor,b.point.anchor);assert.notDeepEqual(a.point,b.point);
 refineReference(a.layout,cell,a.point);refineReference(b.layout,cell,b.point);
 assert.throws(()=>refineReference(a.layout,cell,b.point));
 const profile=n=>({kind:n.kind,at:n.at,
  records:Object.values(n.records).map(r=>r.referenceCell).sort(),
  inputPorts:n.children.map(x=>({at:x.at,records:Object.values(x.records).map(r=>r.referenceCell).sort()}))});
 const leftProfile=profile(a.point),rightProfile=profile(b.point);
 const sameBoundaryProfile=JSON.stringify(leftProfile)===JSON.stringify(rightProfile);
 occurrenceWitnesses.push({cell,left:a.point.anchor,right:b.point.anchor,leftProfile,rightProfile,
  samePhysicalCell:true,sameBoundaryProfile,
  classification:sameBoundaryProfile?'Same structural profile: contextual comparison remains to be extracted.':'Different boundary profiles: equality is not a cyclic-operad gluing requirement.'});
}
assert(occurrenceWitnesses.length>0);
// Audit the existing global fibration API independently. Its preserved wire ID
// is not automatically a signed occurrence-record ID or an edge-five seam.
const wiring=buildSulfur32Wiring(),rows=wiring.wires.map((w,i)=>({wire:w.id,payload:{index:i,opaque:[sc.source,null]}}));
const canonical=xs=>[...xs].sort((a,b)=>a.wire.localeCompare(b.wire));
for(const direction of ['P|E','E|P'])assert.deepEqual(restoreSulfurPayloads(groupSulfurPayloads(wiring,rows,direction)),canonical(rows));
const sources=[root+'/su32-cross-cone-reference-fibre.mjs',root+'/checkers/check_su32_cross_cone_reference_fibre.mjs',
 root+'/su32-cone-operation-transport.mjs',root+'/su32-layer4-comparison.mjs',root+'/su32-signed-reference-encoder.mjs',
 'research/realization-tower/sulfur-32-wiring.mjs','research/realization-tower/sulfur-32-process.mjs',
 root+'/global-coherence-standing-assumption.md',root+'/sulfur-32-reversible-channel-specification.md'];
for(const f of sources)sourceHashes[f]=await digest(f);
const result={schema:'su32.cross-cone-reference-fibre.v1',passed:true,
 counts:{contacts:family.length,geometricReferenceAppearances:family.reduce((s,c)=>s+c.attachments.length,0),
 preparedSourcePoints:producers.size,crossConeSegalSquares:squares,sharedPointRestrictions:restrictions,
 scalarControls,headerControls,wrapperControls,sameCellDistinctContextWitnesses:occurrenceWitnesses.length,
 sameCellSameProfile:occurrenceWitnesses.filter(w=>w.sameBoundaryProfile).length,
 sameCellDifferentProfile:occurrenceWitnesses.filter(w=>!w.sameBoundaryProfile).length},
 conclusion:'All contacts admit one literal-content attachment after refining the reference value by its producer occurrence. This is a uniform typed candidate, not 224 independently chosen transformations.',
 existingFibrationAudit:{source:'sulfur-32-wiring.mjs',wireCount:wiring.wires.length,cellFibres:wiring.groups.length,
 directionsChecked:2,payloadRowsPreserved:true,closure:wiring.closure,
 edgeFiveTransferAuthorized:false,reason:'The source is an edge-three periodic coordinate-axis wiring. No map to these context-indexed record fields is supplied by the tested exports.'},
 limits:['The refinement selects the image of a specified producer fibre inside a larger JSON fibre; it is not proved selected by the full native fibration.',
 'Both channel appearances retain the same source point; serialized occurrences are not new independent contents.',
 'Different boundary profiles are not automatically equality obligations. Global restrictions and higher fillers must be stated at fixed typed profiles.',
 'No period-four seam, native reverse command, physical payload interpretation or eighty-fibre assignment was introduced.'],
 family,example,typeWitness,occurrenceWitnesses,sourceHashes};
const dir=root+'/results/su32-cross-cone-reference-fibre-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,counts:result.counts,conclusion:result.conclusion,existingFibrationAudit:result.existingFibrationAudit,limits:result.limits},null,2));
