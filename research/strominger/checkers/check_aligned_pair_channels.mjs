import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {makeAlignedPairChannels} from '../aligned-pair-channel-model.mjs';
import {contextFrameActions,composeFrames} from '../retained-context-braid-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex');
const protocol=makeAlignedPairChannels(),checks=[];
function check(name,f){f();checks.push(name);}
const dot=(a,b)=>a.reduce(([r,s],[x,y],i)=>[r+x*b[i][0]+y*b[i][1],s+x*b[i][1]-y*b[i][0]],[0,0]);
const source=Array.from({length:8},(_,i)=>[i+1,2*i-3]),dual=Array.from({length:8},(_,i)=>[3*i-2,5-i]);
const result=protocol.run(source,dual);
check('twenty-eight distinct pair channels, not renamed sequential events',()=>{
 assert.equal(protocol.channels.length,28);assert.equal(new Set(protocol.channels.map(c=>c.id)).size,28);
 for(let i=0;i<8;i++)assert.equal(protocol.channels.filter(c=>c.slots.includes(i)).length,7);
});
check('seven matchings cover every pair once and every reference once per round',()=>{
 assert.equal(protocol.rounds.length,7);
 for(const round of protocol.rounds){assert.equal(round.channelIds.length,4);assert.deepEqual(protocol.channels.filter(c=>round.channelIds.includes(c.id)).flatMap(c=>c.slots).sort(),[0,1,2,3,4,5,6,7]);}
 assert.equal(new Set(protocol.rounds.flatMap(r=>r.channelIds)).size,28);
});
check('fourteen stages pair the forward cover with reverse-order dual returns',()=>{
 assert.equal(result.records.length,14);
 for(let i=0;i<7;i++){
  const forward=result.records[i],reverse=result.records[13-i];
  assert.equal(forward.operation,'matching-projection');assert.equal(reverse.operation,'dual-pullback');assert.deepEqual(reverse.channelIds,forward.channelIds);assert.equal(reverse.round,forward.round);
 }
});
const basis=Array.from({length:8},(_,i)=>Array.from({length:8},(_,j)=>[Number(i===j),0]));
check('each stage has exact projection/reconstruction on every reference basis vector',()=>{
 for(const round of protocol.rounds)for(const v of basis)assert.deepEqual(protocol.pullback(round,protocol.project(round,v)),v);
});
check('contravariant return is the actual adjoint and preserves evaluation',()=>{
 for(const round of protocol.rounds){
  const fields=protocol.project(round,source);
  // Independent dual weights on each matching's ports, not copied source values.
  const weights=fields.map((p,i)=>({...p,values:[[i+2,3-i],[7-2*i,i+1]]}));
  const local=fields.map((p,i)=>dot(p.values,weights[i].values)).reduce(([a,b],[c,d])=>[a+c,b+d],[0,0]);
  assert.deepEqual(local,dot(source,protocol.pullback(round,weights)));
 }
});
check('all shared-reference occurrences glue without creating fifty-six independent values',()=>{
 assert.deepEqual(protocol.glue(result.atlas),source);assert.deepEqual(result.sourceRetained,source);
 assert.equal(result.atlas.flatMap(p=>p.values).length,56);
});
check('seven returned presentations are not summed into seven times the field',()=>{
 assert.equal(result.returns.length,7);for(const r of result.returns)assert.deepEqual(r,dual);
});
check('missing, duplicated, relabelled and inconsistent packets are rejected',()=>{
 assert.throws(()=>protocol.glue(result.atlas.slice(1)),/twenty-eight/);
 const duplicate=structuredClone(result.atlas);duplicate[1]=duplicate[0];assert.throws(()=>protocol.glue(duplicate),/provenance/);
 const swapped=structuredClone(result.atlas);swapped[0].slots.reverse();assert.throws(()=>protocol.glue(swapped),/provenance/);
 const changed=structuredClone(result.atlas);changed[0].values[0]=[99,99];assert.throws(()=>protocol.glue(changed),/Inconsistent/);
 const incomplete=protocol.project(protocol.rounds[0],source).slice(1);assert.throws(()=>protocol.pullback(protocol.rounds[0],incomplete),/Incomplete/);
});
const frames=[[0,1,2,3]],seen=new Set(['0123']);
for(let i=0;i<frames.length;i++)for(const g of Object.values(contextFrameActions)){const p=composeFrames(g,frames[i]);if(!seen.has(p.join(''))){seen.add(p.join(''));frames.push(p);}}
const alignments=[];
for(const g of frames){
 const p=protocol.context.permutation(g),transported=protocol.context.push(source,g),directionMap={};
 for(const round of protocol.rounds){
  const moved=protocol.project(round,source).map(packet=>protocol.transportChannel(packet,p));
  const directions=new Set(moved.map(m=>m.slots[0]^m.slots[1]));assert.equal(directions.size,1);
  const direction=[...directions][0],targetRound=protocol.rounds.find(r=>r.direction===direction);directionMap[round.direction]=direction;
  const expected=protocol.project(targetRound,transported).sort((a,b)=>a.channel.localeCompare(b.channel));
  assert.deepEqual(moved.map(({orientation,...packet})=>packet).sort((a,b)=>a.channel.localeCompare(b.channel)),expected);
 }
 alignments.push({frame:g,referencePermutation:p,directionMap});
}
checks.push('all eight native context frames transport entire matchings and all twenty-eight channels covariantly');
check('fourteen-stage scheduler order is transported rather than silently reset in a new frame',()=>{
 for(const a of alignments){const forward=protocol.rounds.map(r=>a.directionMap[r.direction]);const reverse=forward.toReversed();assert.equal(new Set(forward).size,7);for(let i=0;i<7;i++)assert.equal(forward[i],reverse[6-i]);}
});
const distances=protocol.channels.map(c=>({channel:c.id,squaredDistance:c.references[0].split(',').map(Number).reduce((s,x,i)=>s+(x-Number(c.references[1].split(',')[i]))**2,0)}));
check('pair channels are not falsely identified with elementary lattice edges',()=>assert.ok(distances.some(x=>x.squaredDistance!==2)));
const sourcePaths=['research/strominger/aligned-pair-channel-steps-v1.json','research/strominger/aligned-pair-channel-model.mjs','research/strominger/retained-context-braid-model.mjs','research/nima/generative-phase-assembly.mjs'];
const receipt={status:'passed',classification:'Declared 28-channel / 14-stage communication atlas, not a derived growth law',checks,
 sourceSha256:Object.fromEntries(sourcePaths.map(p=>[p,hash(p)])),references:protocol.references,channels:protocol.channels,stages:protocol.stages,alignments,distances,example:result,
 retainedDimensions:{independentReferenceValues:8,pairChannels:28,endpointOccurrences:56,activeChannelsPerStage:4},
 scope:'Each channel is activated once in the forward cover and once in the reverse cover. Twenty-eight channels are retained, not all simultaneously active at every stage. The full bank and histories remain present.',
 unbound:['Identification with the separate 28-event LRRR trace','Native attachment or propagation along nonlocal pair channels','PNE particle readout and generation of the surface layers','Boundary preparation of the three additional context values']};
const out=path.join(root,'research/strominger/results/aligned-pair-channels-v1.json');fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,JSON.stringify(receipt,null,2)+'\n');
console.log(JSON.stringify({status:receipt.status,checks:checks.length,channels:protocol.channels.length,stages:protocol.stages.length,activePerStage:4},null,2));
