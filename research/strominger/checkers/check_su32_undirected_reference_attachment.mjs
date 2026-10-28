import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt,reconcileAt} from '../su32-layer4-comparison.mjs';
import {decomposeRootedComparison,glueRootedComparison} from '../su32-rooted-comparison-gluing.mjs';
import {buildUndirectedAttachmentProblem,orientAttachmentProblem,recoverAtBoundary,referencePortType} from '../su32-undirected-reference-attachment.mjs';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h);
const atlas=buildSu32SignedReferenceAtlas(fixture),reading=fixture.readings.find(r=>r.id==='reading:0:-1');
const chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);assert(chart);
const labels=['P+','P-','E+','E-'],roots=['a','b','other','out'];
const without=(state,key)=>Object.fromEntries(Object.entries(state).filter(([k])=>k!==key));
let preparations=0,queries=0,gluingChecks=0,rootChangeChecks=0,reversedPhysicalMessages=0,physicalMessages=0,localReadoutMessages=0;let example;
const globalInterfaces=fixture.interfaces.map(f=>({id:f.id,cells:f.ports.map(p=>p.split('@')[0]),ports:f.ports,nativeWitness:f.witness}));
// Native face endpoints define an orientation reversal, independent of all
// reader choices and all payload assignments. It is not a P/E sign flip.
for(const face of globalInterfaces){
 assert.deepEqual([...face.ports].sort(),face.cells.map(cell=>cell+'@'+face.id).sort());
 const arc={interface:face.id,from:face.ports[0],to:face.ports[1]};
 const reverse=a=>({interface:a.interface,from:a.to,to:a.from});assert.deepEqual(reverse(reverse(arc)),arc);
 assert.notDeepEqual(reverse(arc),arc);
}
for(const p of [0,1])for(const e of [0,1]){
 const layout=comparisonLayout(atlas,fixture,chart.id,[p,e]);
 const problem=buildUndirectedAttachmentProblem(layout,fixture),problemBefore=structuredClone(problem);
 const orientations=Object.fromEntries(roots.map(root=>[root,orientAttachmentProblem(layout,problem,root)]));
 const plus=layout.template.comparisons.find(c=>c.sharedRecord==='E+'),minus=layout.template.comparisons.find(c=>c.sharedRecord==='E-');
 const registries=[...Array.from({length:16},(_,bits)=>Object.fromEntries(labels.map((k,i)=>[k,(bits>>i)&1]))),
  Object.fromEntries(labels.map((k,i)=>[k,{id:'input:'+k,value:i,provenance:{entry:reading.incomingN,label:k}}]))];
 for(const registry of registries)for(const flipB of [false,true]){
  const plusInputs=plus.inputs.map(id=>channelOperand(layout,id,registry));
  const minusInputs=minus.inputs.map(id=>channelOperand(layout,id,registry));
  const C=compareAt(layout,plus.cell,...plusInputs),B=compareAt(layout,minus.cell,...(flipB?[...minusInputs].reverse():minusInputs));
  const O=reconcileAt(layout,C,B),state={a:plusInputs[0],b:plusInputs[1],other:B,out:O};preparations++;
  const answers={};
  for(const root of roots){
   const known=without(state,root),snapshot=structuredClone(known),answer=recoverAtBoundary(layout,problem,root,known);
   assert.deepEqual(answer.result,state[root]);assert.deepEqual(known,snapshot);queries++;
   assert.deepEqual(answer.orientation,orientations[root]);
   const vertices=Object.fromEntries(answer.vertices.map(v=>[v.node,v.relationPorts]));
   assert.deepEqual(vertices.C[2],vertices.R[0]);
   assert.deepEqual({a:vertices.C[0],b:vertices.C[1],other:vertices.R[1],out:vertices.R[2]},state);
   assert.deepEqual(glueRootedComparison(layout,decomposeRootedComparison(layout,vertices.R[2],[0])),O);gluingChecks++;
   for(const message of answer.messages){
    const wire=problem.wires.find(w=>w.id===message.wire);assert.deepEqual(referencePortType(message.packet),wire.portType);
    assert.equal(message.retainedOrigin,message.packet.at);
    if(message.attachment.kind==='shared-face'){
     const face=globalInterfaces.find(f=>f.id===message.attachment.interfaceId);assert(face);
     assert.deepEqual([message.fromCell,message.toCell].sort(),[...face.cells].sort());
     assert.deepEqual([message.fromFacePort,message.toFacePort].sort(),[...face.ports].sort());physicalMessages++;
     const original=orientations.out.oriented.find(w=>w.wire===message.wire);
     if(message.from===original.to){assert.equal(message.to,original.from);reversedPhysicalMessages++;}
    }else{assert.equal(message.fromCell,message.toCell);localReadoutMessages++;}
   }
   answers[root]={...known,[root]:answer.result};
   if(!example&&registry['P+']?.id&&root==='a')example={layout,problem,registry,state,answer};
  }
  // A complete retained boundary recovered with one chosen root gives precisely
  // the same answers under any subsequent root choice, without changing rules.
  for(const first of roots)for(const second of roots){
   const next=recoverAtBoundary(layout,problem,second,without(answers[first],second));
   assert.deepEqual(next.result,state[second]);rootChangeChecks++;
  }
 }
 assert.deepEqual(problem,problemBefore);
}
const {layout,problem,state,registry}=example;let negativeControls=0;
const reject=fn=>{assert.throws(fn);negativeControls++;};
reject(()=>recoverAtBoundary(layout,problem,'out',state));
reject(()=>recoverAtBoundary(layout,problem,'out',{a:state.a,b:state.b}));
reject(()=>recoverAtBoundary(layout,problem,'C',without(state,'out')));
const badFrame=structuredClone(problem);badFrame.anchor.binding=[1,1];reject(()=>orientAttachmentProblem(layout,badFrame,'out'));
const badFace=structuredClone(problem);badFace.wires[0].attachment.interfaceId=globalInterfaces.find(f=>!f.cells.includes(problem.nodes.find(n=>n.id==='a').cell)).id;
reject(()=>orientAttachmentProblem(layout,badFace,'out'));
const badSlot=structuredClone(problem);badSlot.wires[0].ends[1].slot=1;reject(()=>orientAttachmentProblem(layout,badSlot,'out'));
const badOrigin=structuredClone(problem);badOrigin.wires[0].portType.origin='absent';reject(()=>orientAttachmentProblem(layout,badOrigin,'out'));
const fakeOutputFace=structuredClone(problem);fakeOutputFace.wires.find(w=>w.id==='R-out').attachment={kind:'shared-face',interfaceId:globalInterfaces[0].id};
reject(()=>orientAttachmentProblem(layout,fakeOutputFace,'out'));
// Full reference types match, but independently changed shared payloads must
// still fail the one operation relation at reconciliation.
const minus=layout.template.comparisons.find(c=>c.sharedRecord==='E-');
const changedRegistry={...registry,'P+':{changed:true}};
const conflictingB=compareAt(layout,minus.cell,...minus.inputs.map(id=>channelOperand(layout,id,changedRegistry)));
assert.deepEqual(referencePortType(conflictingB),referencePortType(state.other));
reject(()=>recoverAtBoundary(layout,problem,'out',{a:state.a,b:state.b,other:conflictingB}));
const headerOnly=structuredClone(state.out);delete headerOnly.children;
reject(()=>recoverAtBoundary(layout,problem,'a',{b:state.b,other:state.other,out:headerOnly}));
const sources=[fixturePath,'research/strominger/su32-layer4-comparison.mjs','research/strominger/su32-signed-reference-encoder.mjs',
 'research/strominger/su32-rooted-comparison-gluing.mjs','research/strominger/su32-undirected-reference-attachment.mjs',
 'research/strominger/checkers/check_su32_undirected_reference_attachment.mjs'];
const hashes={};for(const file of sources)hashes[file]=createHash('sha256').update(await fs.readFile(file)).digest('hex');
const report={schema:'su32.undirected-reference-attachment-candidate.v1',passed:true,reading:reading.id,
 nativeSharedFaces:globalInterfaces.length,suppliedNativeInterfaceWitnesses:globalInterfaces.filter(f=>f.nativeWitness!==null).length,
 orientationReversalChecks:globalInterfaces.length,preparations,queries,gluingChecks,rootChangeChecks,
 physicalMessages,reversedPhysicalMessages,localReadoutMessages,negativeControls,
 example:{problem:example.problem,boundaryState:example.state,rerootedRecovery:example.answer},
 verdict:'No attachment conflict on the selected motif under the explicit bidirectional retained-packet policy. Forward-only height orientation is not an algebraic obstruction here.',
 addedAssumptions:['A native undirected shared face may carry a matching typed retained packet in either direction without altering its contents.',
  'Packet at-fields remain retained construction origins; the attachment envelope separately records the current from/to sites.',
  'An existing retained operation relation may be queried at any one missing port when the other complete compatible ports are supplied.',
  'The original output port is a local readout at central N, not an invented fifth physical face.'],
 scope:['A globally defined interface-orientation involution on the 51-cell carrier, tested with a fixed embedded two-operation motif.',
  'All motif wires and root orientations are fixed before reader evaluation. No locally selected path is extended into a global wiring.',
  'The rest of the carrier and outer branches are not assigned a new routing by this construction.',
  'Reverse queries retain and inspect original constructor histories. They do not reverse causal construction or execute native inverse commands.',
  'No cyclic operad, circle fiber, autonomous root-selection law or physical reversible process is established.'],
 nativeReverseOperation:null,sourceHashes:hashes};
const dir='research/strominger/results/su32-undirected-reference-attachment-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,example:undefined,sourceHashes:undefined},null,2));
