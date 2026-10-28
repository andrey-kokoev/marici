// Replay actual native constructors; no new scheduler, geometry or turn rule.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {phaseAdvancePermutations} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const permute=a=>a.length?a.flatMap((x,i)=>permute(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const names=['C0','M0','C1','M1'];
const base=new GenerativeAssemblyRules();
const seed=base.charts[base.packets[base.root].chart];
const vertices=names.map(n=>seed.aliases[n]);
const checks=[];
function check(name,f){f();checks.push(name);}
const records=[];
for(const [index,order] of permute(vertices).entries()){
 const rules=new GenerativeAssemblyRules({seedBindings:Object.fromEntries(names.map((n,i)=>[n,order[i]]))});
 const initial=rules.packets[rules.root],initialChart=rules.charts[initial.chart];
 let id=rules.root;const trace=[];
 for(let stage=0;stage<=28;stage++){
  const packet=rules.packets[id],chart=rules.charts[packet.chart];
  const outgoing=rules.outgoing(id).map(i=>rules.operations[i]);
  trace.push({stage,species:chart.species,origin:packet.origin,chart:packet.chart,permutation:packet.permutation,available:outgoing.map(o=>o.kind)});
  if(stage===28)break;
  const advance=outgoing.filter(o=>o.kind==='reader-phase-advance');
  assert.equal(advance.length,1);assert.equal(rules.validateTransfer(advance[0]),true);id=advance[0].target;
 }
 check(`marking ${index}: native reader evolution stays P for all 28 stages`,()=>{
  assert(trace.every(r=>r.species==='proton'));assert(trace.every(r=>r.origin===r.stage));
 });
 check(`marking ${index}: even endpoints restore chart and coefficients, not origin`,()=>{
  for(const r of trace.filter(r=>r.stage%2===0)){assert.equal(r.chart,initial.chart);assert.deepEqual(r.permutation,initial.permutation);}
  assert.notEqual(trace[28].origin,initial.origin);
 });
 check(`marking ${index}: source supplies choices, not unique next operation`,()=>{
  for(const r of trace.slice(0,28))assert.deepEqual([...r.available].sort(),['PN','reader-phase-advance']);
 });
 // The P reader update swaps opposite vertex pairs. Check the actual bindings.
 const next=rules.charts[trace[1].chart];
 check(`marking ${index}: reader advance swaps both native vertex pairs`,()=>{
  assert.equal(next.aliases.C0,initialChart.aliases.C1);assert.equal(next.aliases.C1,initialChart.aliases.C0);
  assert.equal(next.aliases.M0,initialChart.aliases.M1);assert.equal(next.aliases.M1,initialChart.aliases.M0);
 });
 const pn=rules.operations[rules.outgoing(rules.root).find(i=>rules.operations[i].kind==='PN')];
 const ne=rules.outgoing(pn.target).map(i=>rules.operations[i]).find(o=>o.kind==='NE');
 check(`marking ${index}: native two-transfer E endpoint exists and is terminal`,()=>{
  assert(ne);assert(rules.validateTransfer(pn));assert(rules.validateTransfer(ne));
  assert.equal(rules.charts[rules.packets[ne.target].chart].species,'electron');
  assert.deepEqual(rules.outgoing(ne.target),[]);
 });
 records.push({marking:index,seedBindings:Object.fromEntries(names.map((n,i)=>[n,order[i]])),readerTrace:trace,
  nativeExit:{word:['PN','NE'],steps:2,origin:rules.packets[ne.target].origin},
  scope:'Local packet transfers checked; no global assembly coherence or interpretation as the conjectured whole-object P/E readout asserted.'});
}
check('documented five-slot P and N phase maps are involutions',()=>{
 for(const p of Object.values(phaseAdvancePermutations))assert.deepEqual(p.map(i=>p[i]),[0,1,2,3,4]);
});
const inputs=['research/nima/generative-phase-assembly.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs',
 'research/strominger/checkers/check_global_28_stage_pe_candidates.mjs'];
const sourceSha256=Object.fromEntries(await Promise.all(inputs.map(async p=>[p,createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex')])));
const report={status:'passed',checks,checkCount:checks.length,markingCount:records.length,records,sourceSha256,
 disposition:{nativeReaderOnlyCandidate:'rejected: no P/E exchange at 28',nativeGrammarAsUniqueScheduler:'not supplied: at least two choices at each tested P state',nativePNNEAs28StageLaw:'rejected: two transfers, not 28 rotation stages',globalConjecture:'open: not identified with any tested candidate'},
 boundary:'24 ordered native seed markings, not a proof of arbitrary continuous-frame covariance. Reader phase is not identified with a physical time or whole-complex fibration. No fitted schedule or added stage counter.'};
const dest=path.join(root,'research/strominger/results/global-28-stage-pe-candidates.json');
await fs.mkdir(path.dirname(dest),{recursive:true});await fs.writeFile(dest,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:'passed',checks:checks.length,markings:records.length,result:dest}));
