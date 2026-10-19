// Test whether the proposed R/link torus generators supply independent M/C
// winding coordinates. Use explicit occurrences, not a renaming of circles.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {phaseFrame} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const source='research/strominger/results/hydrogen-edge-attachment/verification.json',bytes=await readFile(source),samples=JSON.parse(bytes).rows,rows=[];
function coordinates(frame,context){const os=context?[...frame.window,frame.context]:frame.window;return ['M','C'].map(role=>Math.max(...os.filter(o=>o.role===role).map(o=>o.index)));}
const delta=(a,b)=>b.map((x,i)=>x-a[i]);
for(const sample of samples){
 const r=new GenerativeAssemblyRules({seedBindings:sample.seedBindings});let p=r.root;const states=[];
 for(let origin=0;origin<=2;origin++){
  const pn=r.outgoing(p).map(i=>r.operations[i]).find(o=>o.kind==='PN'),n=pn.target,ne=r.outgoing(n).map(i=>r.operations[i]).find(o=>o.kind==='NE'),e=ne.target,ids=[p,n,e],frames=ids.map(i=>phaseFrame(r.charts[r.packets[i].chart],r.packets[i].origin));
  const active=frames.map(f=>coordinates(f,false)),withContext=frames.map(f=>coordinates(f,true));
  assert.deepEqual(delta(active[0],active[1]),[1,0]);assert.deepEqual(delta(active[1],active[2]),[0,1]);
  assert.deepEqual(delta(withContext[0],withContext[1]),[0,1]);assert.deepEqual(delta(withContext[1],withContext[2]),[1,0]);
  assert.equal(r.outgoing(e).length,0);
  states.push({origin,ids,active,withContext});
  if(origin<2)p=r.operations[r.outgoing(p).find(i=>r.operations[i].kind==='reader-phase-advance')].target;
 }
 for(const key of ['active','withContext']){
  assert.deepEqual(delta(states[0][key][0],states[2][key][0]),[2,2]);
  assert.deepEqual(delta(states[0][key][2],states[1][key][0]),[0,0]);assert.deepEqual(delta(states[0][key][0],states[1][key][0]),[1,1]);
  const [P,N,E]=states[0][key],loop=[delta(P,N),delta(N,E),delta(E,P)];assert.deepEqual(loop.reduce((s,d)=>s.map((x,i)=>x+d[i]),[0,0]),[0,0]);
 }
 rows.push({marking:sample.marking,states,nativeRealizationTwoStepDeltaMC:[2,2],sameOriginReferenceLinkReturnDeltaMC:[0,0],hypotheticalNextOriginLinkDeltaMC:[1,1],EtoPClosingStepNative:false});
}
// Period-two M/C readouts also lose distinctions between reader presentations.
const phaseReadouts=[];for(let phase=0;phase<2;phase++)for(const [i,species] of ['P','N','E'].entries()){const coord=rows[0].states[phase].active[i].map(x=>x%2);phaseReadouts.push({phase,species,MCmod2:coord});}
assert.equal(new Set(phaseReadouts.map(r=>r.MCmod2.join(','))).size,4);
const out='research/strominger/results/MC-cycle-identification';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'direct-MC-torus-identification-fails-independence-test',source,sourceSha256:createHash('sha256').update(bytes).digest('hex'),checkerSha256:createHash('sha256').update(await readFile(new URL('./check_MC_cycle_identification.mjs',import.meta.url))).digest('hex'),rows,MCgeneratorMatrix:[[2,0],[2,0]],nextOriginSeamAlternativeMatrix:[[2,1],[2,1]],matrixRank:1,phaseReadouts,scope:'Candidate M/C coordinates are maximal active or context-inclusive absolute occurrence indices. Both readouts give diagonal (+2,+2) for native two-step realization return and zero for exact same-origin PNEP reference return. A nonzero winding on the link closure requires an extra occurrence identification; native E is terminal. Does not exclude alternative M/C coordinate constructions. Proposed R/link torus topology remains intact; its identification as two independent M/C circles is not established. No production/viewer changes.'},null,2)+'\n');console.log(JSON.stringify({markings:rows.length,realizationDelta:[2,2],linkReturnDelta:[0,0],windingRank:1,sixReaderPhaseStatesGiveDistinctMCmod2:4}));
