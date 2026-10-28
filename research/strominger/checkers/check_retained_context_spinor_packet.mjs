import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {createRetainedContextMachine,joinCoordinates} from '../retained-context-spinor-packet.mjs';
const complex=[[1,2],[-3,4],[5,-6],[7,8],[-9,10]],seeds=[complex,...Array.from({length:5},(_,j)=>Array.from({length:5},(_,i)=>[Number(i===j),0])),Array.from({length:5},()=>[0,0])];
const norm=x=>x.flat().reduce((s,x)=>s+x*x,0),maxDepth=6,results=[];let example;
for(let seed=0;seed<seeds.length;seed++){
 const machine=createRetainedContextMachine(seeds[seed]),queue=[machine.initial()],kinds={},origins=new Set();let maxRecoveryError=0;
 for(let i=0;i<queue.length;i++){
  const packet=queue[i],raw=machine.decode(packet),restored=machine.restore(machine.serialize(packet));assert.deepEqual(restored,packet);
  const recovered=joinCoordinates(packet.native.species,packet.coordinates),error=Math.hypot(...raw.flat().map((x,i)=>x-recovered.flat()[i]));assert(error<1e-10);maxRecoveryError=Math.max(maxRecoveryError,error);
  assert.equal(norm(raw),norm(seeds[seed]));assert.deepEqual(packet.movingFrame.rootCoordinates,seeds[seed]);origins.add(packet.native.origin);
  if(seed===5&&packet.native.species==='neutron'&&packet.coordinates.contrastNormSquared>0&&!example)example=packet;
  if(packet.history.length<maxDepth)for(const op of machine.choices(packet)){kinds[op.kind]=(kinds[op.kind]??0)+1;queue.push(machine.step(packet,op));}
 }
 results.push({seed,pathsIncludingRoot:queue.length,maximumDepth:maxDepth,origins:[...origins].sort((a,b)=>a-b),operations:kinds,maxRecoveryError});
}
const paths=['research/strominger/retained-context-spinor-packet.mjs','research/strominger/retained-context-spinor-packet-v1.md','research/strominger/checkers/check_retained_context_spinor_packet.mjs','tests/retained-context-spinor-packet.test.mjs','research/nima/generative-phase-assembly.mjs',...['lattice-items','phase-advance-model','window-construction-model','phase-discipline-model','deuterium-tunnel-model'].map(p=>`research/strominger/demos/particle-overlap-tetrahedron/${p}.mjs`)];
const evidence=[];for(const path of paths)evidence.push({path,sha256:createHash('sha256').update(await fs.readFile(path)).digest('hex')});
const report={schema:'retained-context-spinor-packet.verification.v1',constructionAdmitted:false,signedPairBindingAdmitted:false,status:'bounded native retained-packet execution and replay verified',results,exampleContextToContrast:example,
 limits:['one native seed marking, not all octahedral readings','three-/five-coordinate numeric decomposition; exact algebra checked separately by native dual-line adapter','existing native five-slot and occurrence laws, not a derivation of the operator signed-pair meaning','no new whole-assembly equivalence, count invariance, filling, boundary law or route','history commitment detects inconsistent edits; it is not a signature or an authority grant'],evidence};
if(process.argv.includes('--record')){const dir='research/strominger/results/retained-context-spinor-packet-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(`${dir}/verification.json`,JSON.stringify(report,null,2)+'\n');}
console.log(JSON.stringify({status:report.status,constructionAdmitted:false,totalSeedPathChecks:results.reduce((s,r)=>s+r.pathsIncludingRoot,0),seedVectors:seeds.length,depth:maxDepth,firstSeed:results[0]},null,2));
