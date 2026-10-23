// Channel roundtrip and adversarial tests. Only the encoder/checker sees the target fixture.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {CHANNEL_SCHEMA,NativeChannelAssembler,encodeFixture,decodeChannel,semanticAssembly} from './native_retained_channel.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const base='research/strominger/results/';
const source=base+'joint-field-sewing-fixture.json',fieldSource=base+'joint-field-assembly-sewing.json';
const contractPath='research/strominger/contracts/native-retained-channel.v1.json';
const contract=JSON.parse(await fs.readFile(path.join(root,contractPath),'utf8'));
const original=JSON.parse(await fs.readFile(path.join(root,source),'utf8'));
const fields=JSON.parse(await fs.readFile(path.join(root,fieldSource),'utf8'));
const stream=encodeFixture(original),assembler=new NativeChannelAssembler(),checks=[];
const check=(name,f)=>{f();checks.push(name);};
check('declared channel schema and generated record types agree',()=>{
 assert.equal(contract.schema,CHANNEL_SCHEMA);assert.equal(stream[0].schema,contract.schema);
 assert(stream.every(r=>Object.hasOwn(contract.recordTypes,r.type)));
 assert(!stream.some(r=>['cells','packets','charts','readouts','census'].some(k=>Object.hasOwn(r,k))));
});
for(const r of stream)assembler.feed(r);
const reconstructed=assembler.finish();
check('native whole assembly reconstructed from operations and references',()=>assert.deepEqual(semanticAssembly(reconstructed,reconstructed.channelReferences),semanticAssembly(original)));
check('all14 packets and18 interfaces are derived and retained',()=>{
 assert.equal(reconstructed.packets.length,14);assert.equal(reconstructed.operations.length,18);
 assert.equal(reconstructed.audit.exitPackets.length,2);assert(reconstructed.audit.certifiedExit);
});
check('ordered occurrence histories survive graph packet reuse',()=>{
 assert.deepEqual(reconstructed.histories.map(h=>h.word),original.histories.map(h=>h.word));
 const occurrences=reconstructed.histories.flatMap(h=>h.occurrences);
 assert.equal(new Set(occurrences).size,occurrences.length);
 assert.deepEqual(reconstructed.channelLog,stream);
 assert.equal(occurrences.length,original.histories.reduce((n,h)=>n+h.word.length,0));
});
check('derived field frames reproduce the prior exact sewing frames',()=>{
 for(const binding of fields.packetBindings){
  const id=reconstructed.channelReferences['packet-'+binding.packet];
  const expected=fields.frameTypes[binding.species+binding.frameParity].forwardFactorWord;
  assert.deepEqual(reconstructed.fieldFrames[id],expected);
 }
});
check('order-five comparison computed from distinct history positions',()=>{
 assert.equal(reconstructed.comparisons.length,1);assert.equal(reconstructed.comparisons[0].order,5);
 assert.notEqual(reconstructed.comparisons[0].left,reconstructed.comparisons[0].right);
});
check('every valid record has an incremental compatible prefix',()=>{
 assert.equal(reconstructed.prefixes.length,stream.length);
 assert(reconstructed.prefixes.slice(0,-1).every(p=>!p.closed));
 assert(reconstructed.prefixes.at(-1).closed);
 assert(reconstructed.prefixes.some(p=>p.pendingInterfaceWitnesses.length>0));
 assert.deepEqual(reconstructed.prefixes.at(-1).pendingInterfaceWitnesses,[]);
});
// Independent histories may be transmitted in the other order, preserving each local order.
const blocks=[];let current;
for(const r of stream){if(r.type==='begin'){current=[];blocks.push(current);}if(r.type==='begin'||r.type==='execute')current.push(r);}
const reordered=[stream[0],...blocks.reverse().flat(),...stream.filter(r=>['witness','compare','close'].includes(r.type))];
const other=decodeChannel(reordered);
check('independent serialization order changes allocation but not the retained labelled assembly',()=>{
 assert.deepEqual(semanticAssembly(other,other.channelReferences),semanticAssembly(original));
 assert.notDeepEqual(other.channelLog,reconstructed.channelLog);
});
const executeIndex=stream.findIndex(r=>r.type==='execute'),witnessIndex=stream.findIndex(r=>r.type==='witness');
assert(witnessIndex>=0);
const hostileCases=[
 ['dropped context',s=>{delete s[executeIndex].context;}],
 ['forged context',s=>{s[executeIndex].context.vertex='999,0,0,0';}],
 ['swapped dependent occurrences',s=>{[s[executeIndex],s[executeIndex+1]]=[s[executeIndex+1],s[executeIndex]];}],
 ['duplicated occurrence identity',s=>{s[executeIndex+1].occurrence=s[executeIndex].occurrence;}],
 ['unknown source reference',s=>{s[executeIndex].source='not-yet-created';}],
 ['rebound target identity',s=>{s[executeIndex].target=s[0].root;}],
 ['missing incidental interface witness',s=>{s.splice(witnessIndex,1);}],
 ['forged comparison position',s=>{s.find(r=>r.type==='compare').left.after=10000;}],
 ['missing closing record',s=>{s.pop();}],
 ['record appended after close',s=>{s.push(structuredClone(s[executeIndex]));}],
 ['completed target injected into opening',s=>{s[0].cells=original.cells;}]
];
for(const [name,mutate] of hostileCases){const bad=structuredClone(stream);mutate(bad);check('reject '+name,()=>assert.throws(()=>decodeChannel(bad)));}
check('failed replay cannot resume with partially mutated state',()=>{
 const a=new NativeChannelAssembler();a.feed(stream[0]);const bad=structuredClone(stream[executeIndex]);
 assert.throws(()=>a.feed(bad));assert.throws(()=>a.feed(stream[1]));assert.throws(()=>a.finish());
});
const channelPath=base+'native-retained-channel.json';
await fs.writeFile(path.join(root,channelPath),JSON.stringify({schema:CHANNEL_SCHEMA,records:stream},null,2)+'\n');
const decoderInputs=[channelPath,contractPath,'research/strominger/checkers/native_retained_channel.mjs',
 'research/nima/generative-phase-assembly.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/carrier.mjs'];
const hashes=async files=>Object.fromEntries(await Promise.all(files.map(async p=>[p,createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex')])));
reconstructed.sourceHashes=await hashes(decoderInputs);
const assembledPath=base+'channel-assembled-native-fixture.json';
await fs.writeFile(path.join(root,assembledPath),JSON.stringify(reconstructed,null,2)+'\n');
const recordCounts={};for(const r of stream)recordCounts[r.type]=(recordCounts[r.type]??0)+1;
const report={status:'passed',checks,check_count:checks.length,recordCount:stream.length,recordCounts,
 counts:{packets:reconstructed.packets.length,interfaces:reconstructed.operations.length,histories:reconstructed.histories.length},
 targetFixtureUsedByDecoder:false,full114ChannelEstablished:false,fullEsd7Established:false,
 sourceHashes:await hashes([...decoderInputs,source,fieldSource,assembledPath,'research/strominger/checkers/check_native_retained_channel.mjs']),
 artifacts:{channel:channelPath,assembledFixture:assembledPath},
 disposition:'First executable bounded channel/assembler constructed. Native geometry, coefficient permutations and field frame words are generated through the existing rules; independent target comparison passes. Full44-channel equations must additionally be replayed on the assembled fixture.',
 scope:'One certified native five-body fixture, not the proposed114-record producer or the full esd7 complex. The input operation words are supplied retained histories, not an emergent global clock. Executed occurrences, interface witnesses and comparison records have different types.'};
const dest=path.join(root,base+'native-retained-channel-verification.json');
await fs.writeFile(dest,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,checks:checks.length,records:stream.length,recordCounts,...report.counts,result:dest}));
