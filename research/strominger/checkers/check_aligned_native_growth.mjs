import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {runAlignedNativeGrowth} from '../aligned-native-growth-model.mjs';
import {makeAlignedPairChannels} from '../aligned-pair-channel-model.mjs';
import {contextFrameActions,composeFrames,permuteReference} from '../retained-context-braid-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex');
const checks=[];function check(name,f){f();checks.push(name);}
const dot=(a,b)=>a.reduce(([r,s],[x,y],i)=>[r+x*b[i][0]+y*b[i][1],s+x*b[i][1]-y*b[i][0]],[0,0]);
const values=Array.from({length:8},(_,i)=>[i+2,3*i-1]),dual=Array.from({length:8},(_,i)=>[2*i-3,8-i]);
const r=runAlignedNativeGrowth(values,{dual}),atlas=makeAlignedPairChannels();
check('native attachments are selected by active coefficient channels at stages three and five',()=>{
 assert.deepEqual(r.records.filter(s=>s.operation).map(s=>[s.stage,s.operation.kind]),[[3,'PN'],[5,'NE']]);
 for(const stage of r.records.filter(s=>s.operation))for(let i=0;i<8;i++)if(stage.permutation[i]!==i)assert.equal(i^stage.permutation[i],stage.direction);
});
check('the generated three-cell assembly is certified by native geometry and occurrence rules',()=>{
 assert.equal(r.assembly.certifiedExit,true);assert.equal(r.assembly.allContactsWitnessed,true);assert.equal(r.assembly.allPacketsCanReachExit,true);
 assert.deepEqual(r.assembly.counts,{proton:1,neutron:1,electron:1});assert.equal(new Set(r.charts.map(c=>c.cell)).size,3);
});
check('every native coefficient coordinate matches the source packet permutation',()=>{
 const names=['C0','M0','C1','M1','C2'],indices=names.map(n=>r.references.indexOf(r.charts[0].aliases[n])),seed=indices.map(i=>r.initial[i]);
 for(const stage of r.records){const packet=r.packets.find(p=>p.id===stage.targetPacket);assert.deepEqual(indices.map(i=>stage.after[i]),packet.permutation.map(i=>seed[i]));}
});
check('the channel protocol retains fourteen occurrences and covers all twenty-eight channels twice',()=>{
 assert.equal(r.stageCount,14);assert.equal(r.channelCount,28);
 assert.equal(new Set(r.records.flatMap(s=>s.channelIds)).size,28);
 for(const stage of r.records)assert.deepEqual(r.returns.find(s=>s.forwardStage===stage.stage).channelIds,stage.channelIds);
});
check('dual returns preserve complex evaluation at each native move and globally',()=>{
 for(const ret of r.returns){const fwd=r.records[ret.forwardStage-1];assert.deepEqual(dot(fwd.after,ret.afterDual),dot(fwd.before,ret.beforeDual));}
 assert.deepEqual(dot(r.final,r.terminalDual),dot(r.initial,r.initialDual));
});
check('returns do not invent native inverse-NE growth and do not conflate stage with native origin',()=>{
 assert.ok(r.returns.every(s=>s.kind==='dual-pullback-not-native-growth'));
 assert.ok(r.packets.every(p=>p.origin===0));assert.ok(r.records.filter(s=>s.operation).every(s=>s.operation.phaseDelta===0));
 assert.deepEqual(r.returns.filter(s=>s.nativeOperation).map(s=>[s.stage,s.nativeOperation]),[[10,'NE'],[12,'PN']]);
});
check('time-indexed values require transport alignment before they can glue',()=>{
 assert.throws(()=>atlas.glue(r.records.flatMap(s=>s.packets)),/Inconsistent shared reference/);
 assert.deepEqual(r.normalized,r.initial);assert.deepEqual(r.recovered,r.initial);
});
const symbolic=Array.from({length:8},(_,i)=>({symbol:i<5?`initial-${i}`:`unassigned-${i}`}));
check('three additional context values remain symbolic and all eight values recover',()=>{
 const s=runAlignedNativeGrowth(symbolic);assert.deepEqual(s.recovered,s.initial);assert.deepEqual(s.final.slice(5),s.initial.slice(5));
});
const frames=[[0,1,2,3]],seen=new Set(['0123']);
for(let i=0;i<frames.length;i++)for(const g of Object.values(contextFrameActions)){const p=composeFrames(g,frames[i]);if(!seen.has(p.join(''))){seen.add(p.join(''));frames.push(p);}}
check('growth binding, geometry, coefficient state and attachment timing are covariant in all eight frames',()=>{
 for(const frame of frames){
  const s=runAlignedNativeGrowth(values,{frame,dual});assert.equal(s.assembly.certifiedExit,true);
  assert.deepEqual(s.records.filter(x=>x.operation).map(x=>[x.stage,x.operation.kind]),[[3,'PN'],[5,'NE']]);
  assert.deepEqual(s.final,atlas.context.push(r.final,frame));
  for(let i=0;i<r.bodies.length;i++)assert.deepEqual([...s.bodies[i]].sort(),r.bodies[i].map(v=>permuteReference(v,frame)).sort());
 }
});
check('full-bank basis tests recover every coefficient, not only the displayed readout',()=>{
 for(let i=0;i<8;i++){
  const v=Array.from({length:8},(_,j)=>[Number(i===j),0]),s=runAlignedNativeGrowth(v);
  assert.deepEqual(s.recovered,v);assert.deepEqual(s.normalized,v);
 }
});
check('reference-changing NN continuation is exposed as an excluded obligation, not silently replaced by NE',()=>{
 assert.ok(r.excluded.some(x=>x.operation==='NN-phase-advance'&&x.reason.includes('reference-changing')));
});
const paths=['research/strominger/aligned-native-growth-model.mjs','research/strominger/aligned-pair-channel-model.mjs','research/strominger/aligned-pair-channel-steps-v1.json','research/strominger/retained-context-braid-model.mjs','research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs','research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs'];
const receipt={status:'passed',checks,sourceSha256:Object.fromEntries(paths.map(p=>[p,hash(p)])),
 classification:'Channel-selected certified P-to-N-to-E native attachment chain, not full surface growth',execution:r,
 boundary:'The unchanged-reference, single-frontier policy blocks NN context-changing continuation. E is terminal. Layer words are neither loaded nor used as input; a path is not compared to a surface word as if they were the same observable.',
 next:'Construct the time-indexed context-changing NN port map and retain multiple live frontiers before claiming surface growth.'};
const out=path.join(root,'research/strominger/results/aligned-native-growth-v1.json');fs.writeFileSync(out,JSON.stringify(receipt,null,2)+'\n');
console.log(JSON.stringify({status:receipt.status,checks:checks.length,moves:r.records.filter(s=>s.operation).map(s=>[s.stage,s.operation.kind]),nativeAssembly:r.assembly.counts,certifiedExit:r.assembly.certifiedExit},null,2));
