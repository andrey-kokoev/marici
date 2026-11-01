// Occurs-check for a precisely declared static identification, not a no-go
// theorem for edge-five or for dependent/graph-backed content in general.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt} from '../su32-layer4-comparison.mjs';
import {identifyCone,targetFixture} from '../su32-cone-operation-transport.mjs';
const root='research/strominger',paths={binding:root+'/results/su32-edge5-fibre-placement-binding-v1/verification.json',
 transport:root+'/results/su32-edge5-operadic-transport-v1/verification.json',
 attachment:root+'/results/su32-cross-cone-reference-fibre-v1/verification.json',
 source:root+'/results/su32-hopf-tests-v1/fixture.json',carrier:root+'/results/su32-edge5-extension-contract-v1/verification.json',
 contract:root+'/contracts/su32-static-payload-identification-v1.json'};
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const docs={},sourceHashes={};for(const [k,p] of Object.entries(paths)){
 docs[k]=JSON.parse(await fs.readFile(p,'utf8'));sourceHashes[p]=await digest(p);
 for(const [s,h] of Object.entries(docs[k].sourceHashes??{}))assert.equal(await digest(s),h,`Stale ${s}`);
}
const fibreOf=new Map(docs.binding.fibres.flatMap(f=>[[f.sourcePresentation,f.id],[f.targetPresentation,f.id]]));
assert.equal(fibreOf.size,160);assert.equal(new Set(fibreOf.values()).size,80);
const contacts=docs.transport.crossLevelContacts;
const constraints=[...new Map(contacts.map(c=>[JSON.stringify([c.producerChart,c.cell]),{
 chart:c.producerChart,cell:c.cell,outputFibre:fibreOf.get(c.cell),
 inputs:c.producerType.recordReferenceCells.map(cell=>({cell,fibre:fibreOf.get(cell)}))}])).values()];
for(const c of constraints){assert(c.outputFibre);assert(c.inputs.every(i=>i.fibre));assert.equal(c.inputs.length,3);}
const self=constraints.filter(c=>c.inputs.some(i=>i.fibre===c.outputFibre));
const selfContacts=contacts.filter(c=>c.producerType.recordReferenceCells.some(r=>fibreOf.get(r)===fibreOf.get(c.cell)));
assert(self.length>0);
const layer=new Map(docs.carrier.edge5Carrier.layers.flatMap(l=>l.cells.map(c=>[c,l.layer])));
// With occurrences kept distinct, every dependency goes strictly forward two
// physical layers. The literal presentation identification creates self edges.
for(const c of constraints)for(const i of c.inputs){assert.notEqual(i.cell,c.cell);assert.equal(layer.get(c.cell)-layer.get(i.cell),2);}
const source=docs.source,sa=buildSu32SignedReferenceAtlas(source),reading=source.readings.find(r=>r.id==='reading:0:-1');
const sc=sa.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);
const sourceCone=reading.cones.find(c=>c.source===sc.source&&c.target===sc.target),carrier=docs.carrier.edge5Carrier;
const ids=carrier.comparisonCones.map(c=>identifyCone(source,sc,sourceCone,carrier,c));
const atlas={charts:ids.map(i=>i.chart),globalAssignment:null},fixture=targetFixture(carrier);
const bank=new Map(docs.binding.fibres.map((f,i)=>[f.id,{token:i,opaque:[f.id,null]}]));
const size=x=>x!==null&&typeof x==='object'?1+Object.values(x).reduce((s,v)=>s+size(v),0):1;
let rankChecks=0,separateWitnessChecks=0;const witnesses=[];
const bankBefore=JSON.stringify([...bank]);
for(const c of constraints){
 const witnessRef=c.inputs.find(i=>i.fibre===c.outputFibre);
 for(const binding of [[0,0],[0,1],[1,0],[1,1]]){
  const l=comparisonLayout(atlas,fixture,c.chart,binding),spec=l.template.comparisons.find(x=>x.cell===c.cell);
  const registry=Object.fromEntries(Object.entries(l.template.referenceBinding).map(([cell,label])=>[label,bank.get(fibreOf.get(cell))]));
  const node=compareAt(l,c.cell,...spec.inputs.map(j=>channelOperand(l,j,registry)));
  // Positive control: this valid comparison can be retained alongside the
  // unchanged global content bank, without equating it to its output fibre.
  separateWitnessChecks++;
  if(!witnessRef)continue;
  const label=l.template.referenceBinding[witnessRef.cell],inner=node.records[label].payload;
  assert.deepEqual(inner,bank.get(c.outputFibre));assert(size(node)>size(inner));assert.notDeepEqual(node,inner);
  assert.deepEqual(JSON.parse(JSON.stringify(node)).records[label].payload,inner);rankChecks++;
  if(binding.every(x=>x===0))witnesses.push({...c,selfReference:witnessRef,label,
   containingPath:['records',label,'payload'],inputRank:size(inner),outputRank:size(node),sampleInput:inner,sampleOutput:node,
   requiredStaticEquation:'The full output must equal the value at its output fibre, which is already its own strict payload subtree.'});
 }
}
assert.equal(JSON.stringify([...bank]),bankBefore);
const proof=root+'/agda/FinitePayloadOccursCheck.agda',receipt=root+'/results/su32-static-payload-identification-v1/agda.json';
const agda=JSON.parse(await fs.readFile(receipt,'utf8'));assert.equal(agda.passed,true);assert.equal(agda.compiler_exit_code,0);
assert.equal(agda.ignore_interfaces,true);assert.equal(agda.inputs_stable_during_check,true);
assert.equal(await digest(proof),agda.source_inventory.source);
assert.equal(await digest(root+'/checkers/check_finite_payload_occurs_agda.py'),agda.source_inventory.checker);
for(const p of [proof,receipt,root+'/checkers/check_finite_payload_occurs_agda.py',
 root+'/checkers/check_su32_static_payload_identification.mjs',root+'/su32-layer4-comparison.mjs',root+'/su32-cone-operation-transport.mjs'])sourceHashes[p]=await digest(p);
const result={schema:'su32.static-payload-identification.v1',passed:true,
 candidateIdentificationPassed:false,
 counts:{namedFibres:80,contacts:contacts.length,distinctProducerConstraints:constraints.length,
 selfDependentProducerConstraints:self.length,selfDependentContacts:selfContacts.length,rankChecks,separateWitnessChecks},
 conclusion:'The declared static finite-JSON identification is impossible: an assigned fibre value would have to equal a comparison object strictly containing that same value.',
 proof:{module:proof,receipt,scope:'Agda checks the rank obstruction; source extraction and JSON containment are executable evidence, not an Agda formalization of the whole model.'},
 controls:{distinctPresentationDependencyStrictlyLayered:true,priorLocalAttachmentReceiptPassed:docs.attachment.passed,
 unchangedGlobalContentBankWithSeparateWitnesses:true,
 scope:'Reject only the conjunction of the four declared static identification hypotheses. No history erasure, new quotient, or replacement representation is installed.'},
 constraints,witnesses,
 next:'Separate the transport/provenance witness from static content, or explicitly supply a different content representation. The local packet-in-payload refinement cannot simply be declared to be the existing static eighty-fibre binding.',
 sourceHashes};
const dir=root+'/results/su32-static-payload-identification-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({...result,constraints:undefined,witnesses:undefined,sourceHashes:undefined},null,2));
