import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSulfur32Wiring,groupSulfurPayloads,restoreSulfurPayloads} from '../../realization-tower/sulfur-32-wiring.mjs';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt} from '../su32-layer4-comparison.mjs';
import {attachReference} from '../su32-cross-cone-reference-fibre.mjs';
const root='research/strominger',paths={source:root+'/results/su32-hopf-tests-v1/fixture.json',
 span:root+'/results/su32-boundary-composition-span-v1/verification.json',carrier:root+'/results/su32-edge5-extension-contract-v1/verification.json',
 contract:root+'/contracts/su32-native-boundary-extraction-v1.json'};
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const docs={},sourceHashes={};for(const [k,p] of Object.entries(paths)){
 docs[k]=JSON.parse(await fs.readFile(p,'utf8'));sourceHashes[p]=await digest(p);
 for(const [s,h] of Object.entries(docs[k].sourceHashes??{}))assert.equal(await digest(s),h,`Stale ${s}`);
}
const source=docs.source,atlas=buildSu32SignedReferenceAtlas(source),charts=new Map(atlas.charts.map(c=>[c.id,c]));
const wiring=buildSulfur32Wiring(),ports=new Map(wiring.ports.map(p=>[p.id,p]));
const groupOf=new Map(wiring.groups.flatMap(g=>g.members.map(m=>[m.id,g.id])));
const wireOf=new Map();for(const w of wiring.wires)for(const p of w.ports){assert(!wireOf.has(p));wireOf.set(p,w.id);}
const shape=vs=>vs.map(v=>v.join(',')).sort().join('|'),faces=new Map(docs.carrier.edge5Carrier.faces.map(f=>[f.id,f]));
const axis=f=>{const a=[0,1,2,3].filter(i=>f.vertices.every(v=>v[i]===f.vertices[0][i]));assert.equal(a.length,1);return a[0];};
const globalAxisAudit=docs.span.motifs.map(m=>({producerChart:m.producerChart,consumerChart:m.consumerChart,
 cell:m.joint,incomingAxis:axis(faces.get(m.internalFaces[0])),outgoingAxis:axis(faces.get(m.internalFaces[1]))}));
assert.equal(globalAxisAudit.length,448);assert(globalAxisAudit.every(m=>m.incomingAxis!==m.outgoingAxis));
const local=docs.span.motifs.filter(m=>charts.has(m.producerChart)&&charts.has(m.consumerChart));assert.equal(local.length,32);
const fixed=docs.contract.fixedMotif,m=local.find(m=>Object.entries(fixed).every(([k,v])=>m[k]===v));assert(m);
const physicalPort=(cell,face)=>{
 const matches=wiring.ports.filter(p=>p.lifts.some(l=>l.cell===cell&&shape(l.vertices)===face));assert.equal(matches.length,1);return matches[0];
};
const entry=physicalPort(m.joint,m.internalFaces[0]),formalExit=physicalPort(m.joint,m.internalFaces[1]);
assert.notEqual(entry.axis,formalExit.axis);assert.notEqual(wireOf.get(entry.id),wireOf.get(formalExit.id));
const nativeWire=wiring.wires.find(w=>w.id===wireOf.get(entry.id));
const nativeExit=nativeWire.ports.map(p=>ports.get(p)).find(p=>p.cell===entry.cell&&p.id!==entry.id);assert(nativeExit);assert.equal(nativeExit.axis,entry.axis);
// Extract the full native cut, not just the two interfaces used by the formal tree.
const region=new Set([m.producerCell,m.joint,m.downstreamComparison].map(c=>groupOf.get(c)));assert.equal(region.size,3);
const inside=new Set(wiring.ports.filter(p=>region.has(p.cell)).map(p=>p.id));
const internal=wiring.edges.filter(e=>inside.has(e.from)&&inside.has(e.to));
const crossing=wiring.edges.filter(e=>inside.has(e.from)!==inside.has(e.to));
const boundary=crossing.map(e=>({edge:e.id,port:inside.has(e.from)?e.from:e.to,wire:wireOf.get(inside.has(e.from)?e.from:e.to),kind:e.kind}));
assert.equal(new Set(boundary.map(b=>b.port)).size,boundary.length);
const unseen=new Set(inside),components=[];
while(unseen.size){const todo=[unseen.values().next().value];unseen.delete(todo[0]);
 for(let i=0;i<todo.length;i++)for(const e of internal)if(e.from===todo[i]||e.to===todo[i]){
  const n=e.from===todo[i]?e.to:e.from;if(unseen.delete(n))todo.push(n);
 }
 const wires=[...new Set(todo.map(p=>wireOf.get(p)))];assert.equal(wires.length,1);
 const cut=boundary.filter(b=>todo.includes(b.port));assert(cut.length>0);
 components.push({ports:todo,wire:wires[0],boundaryPorts:cut.map(b=>b.port)});
}
const rows=wiring.wires.map((w,i)=>({wire:w.id,payload:{token:i,opaque:[false,null]}}));
const value=new Map(rows.map(r=>[r.wire,r]));
const nativeBoundary=boundary.map(b=>({...b,value:structuredClone(value.get(b.wire))}));
function extendBoundary(rows){
 assert.equal(rows.length,boundary.length);const byPort=new Map(rows.map(r=>[r.port,r]));assert.equal(byPort.size,boundary.length);
 for(const b of boundary){assert(byPort.has(b.port));assert.equal(byPort.get(b.port).wire,b.wire);assert.equal(byPort.get(b.port).value.wire,b.wire);}
 return Object.fromEntries(components.flatMap(c=>{
  const vals=c.boundaryPorts.map(p=>byPort.get(p).value);for(const v of vals)assert.deepEqual(v,vals[0],'Same native wire has inconsistent boundary contents');
  return c.ports.map(p=>[p,structuredClone(vals[0])]);
 }));
}
const restored=extendBoundary(nativeBoundary);
assert.deepEqual(restored,Object.fromEntries(components.flatMap(c=>c.ports.map(p=>[p,value.get(c.wire)]))));
assert.deepEqual(extendBoundary([...nativeBoundary].reverse()),restored);
const repeated=components.find(c=>c.boundaryPorts.length>1);assert(repeated);
const damaged=structuredClone(nativeBoundary);damaged.find(b=>b.port===repeated.boundaryPorts[0]).value.payload={wrong:true};assert.throws(()=>extendBoundary(damaged),/inconsistent boundary/);
function grouped(rows){
 return new Map(['P|E','E|P'].flatMap(direction=>groupSulfurPayloads(wiring,rows,direction)).map(f=>[f.cell,f]));
}
function registry(l,groups){return Object.fromEntries(Object.entries(l.template.referenceBinding).map(([cell,label])=>{
 const f=groups.get(groupOf.get(cell));assert(f);return [label,f];
}));}
function observation(m,rows,sb=[0,0],tb=[0,0]){
 const groups=grouped(rows),sl=comparisonLayout(atlas,source,m.producerChart,sb),tl=comparisonLayout(atlas,source,m.consumerChart,tb);
 const c=sl.template.comparisons.find(c=>c.cell===m.producerCell),d=tl.template.comparisons.find(c=>c.cell===m.downstreamComparison);
 const sr=registry(sl,groups),tr=registry(tl,groups),[a,b]=c.inputs.map(j=>channelOperand(sl,j,sr));
 const j=tl.template.channels.find(j=>j.cell===m.joint),other=[j.P,j.E].find(r=>r.referenceCell!==m.producerCell);
 const z=tr[other.record],k=channelOperand(tl,m.otherChannel,tr),p=compareAt(sl,c.cell,a,b);
 const intermediate=attachReference(sl,tl,c.cell,m.joint,p,z);
 const formalOutput=compareAt(tl,d.cell,...d.inputs.map(id=>id===m.joint?intermediate:k));
 return {formalBoundaryInputs:{a,b,z,k},formalOutput,nativeOutputFibre:groups.get(groupOf.get(m.downstreamComparison)),
  nativeProducerFibre:groups.get(groupOf.get(m.producerCell)),formalProducer:p};
}
function support(m){
 const a=charts.get(m.producerChart),b=charts.get(m.consumerChart),c=a.comparisons.find(c=>c.cell===m.producerCell);
 const refs=new Set(c.inputs.flatMap(id=>{const j=a.joints.find(j=>j.cell===id);return [j.P,j.E];}));
 const j=b.joints.find(j=>j.cell===m.joint),k=b.joints.find(j=>j.cell===m.otherChannel);
 [j.P,j.E].filter(c=>c!==m.producerCell).forEach(c=>refs.add(c));refs.add(k.P);refs.add(k.E);
 const groups=new Set([...refs].map(c=>groupOf.get(c)));
 const input=wiring.wires.filter(w=>groups.has(w.source)||groups.has(w.target)).map(w=>w.id);
 const output=wiring.wires.filter(w=>[w.source,w.target].includes(groupOf.get(m.downstreamComparison))).map(w=>w.id);
 return {referenceCells:[...refs],inputWires:input,outputWires:output,unobservedOutputWires:output.filter(id=>!input.includes(id))};
}
const audits=local.map(m=>({motif:m,...support(m)}));assert(audits.every(a=>a.unobservedOutputWires.length>0));
const selected=support(m),changedWire=selected.unobservedOutputWires[0];
const rival=rows.map(r=>r.wire===changedWire?{wire:r.wire,payload:{changed:true,opaque:[null,false]}}:structuredClone(r));
for(const rs of [rows,rival])for(const direction of ['P|E','E|P'])assert.deepEqual(restoreSulfurPayloads(groupSulfurPayloads(wiring,rs,direction)),[...rs].sort((a,b)=>a.wire.localeCompare(b.wire)));
let nonfactorizationChecks=0;let witness;
for(const sb of [[0,0],[0,1],[1,0],[1,1]])for(const tb of [[0,0],[0,1],[1,0],[1,1]]){
 const x=observation(m,rows,sb,tb),y=observation(m,rival,sb,tb);
 assert.deepEqual(x.formalBoundaryInputs,y.formalBoundaryInputs);assert.deepEqual(x.formalOutput,y.formalOutput);
 assert.notDeepEqual(x.nativeOutputFibre,y.nativeOutputFibre);assert.notDeepEqual(x.formalProducer,x.nativeProducerFibre);
 nonfactorizationChecks++;witness??={binding:{source:sb,target:tb},changedWire,left:x,right:y};
}
const sources=[root+'/checkers/check_su32_native_boundary_extraction.mjs','research/realization-tower/sulfur-32-wiring.mjs',
 root+'/su32-layer4-comparison.mjs',root+'/su32-cross-cone-reference-fibre.mjs',root+'/su32-signed-reference-encoder.mjs'];
for(const p of sources)sourceHashes[p]=await digest(p);
const result={schema:'su32.native-boundary-extraction.v1',passed:true,formalNativeIdentificationPassed:false,
 counts:{geometricMotifs:448,axisChangingMotifs:globalAxisAudit.filter(a=>a.incomingAxis!==a.outgoingAxis).length,
 nativeEdgeThreeMotifs:local.length,cutPorts:inside.size,cutInternalEdges:internal.length,cutBoundaryPorts:boundary.length,
 cutComponents:components.length,cutIndependentWireValues:new Set(boundary.map(b=>b.wire)).size,
 formalInputObservedWires:selected.inputWires.length,nativeOutputWires:selected.outputWires.length,
 nativeOutputUnobservedWires:selected.unobservedOutputWires.length,nonfactorizationChecks},
 conclusion:'The formal motif is not the native wire transport: it turns between different axes. Its boundary inputs do not determine the full native output fibre.',
 nativeCut:{motif:m,region:[...region],boundary,components,restored,
  incoming:{port:entry.id,axis:entry.axis,wire:wireOf.get(entry.id)},
  proposedOutgoing:{port:formalExit.id,axis:formalExit.axis,wire:wireOf.get(formalExit.id)},
  actualContinuation:{port:nativeExit.id,axis:nativeExit.axis,wire:nativeWire.id,lifts:nativeExit.lifts}},
 supportAudits:audits,nonfactorizationWitness:witness,globalAssignments:{left:rows,right:rival},
 limits:['This is the existing edge-three periodic wiring candidate; its period lattice is not extended to edge-five.',
 'Failure refutes the tested full-native-fibre identification, not all coarse readouts or all possible fibrations.',
 'Formal comparison operations remain valid as their own information operations; they are not automatically physical wire transfers.'],
 next:'Use the native cut boundary and its actual wire fibres as the source interface. Any smaller formal boundary needs a declared restriction with sufficient information, not more coherence tests of the old motif.',
 sourceHashes};
const dir=root+'/results/su32-native-boundary-extraction-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,formalNativeIdentificationPassed:false,counts:result.counts,conclusion:result.conclusion,limits:result.limits},null,2));
