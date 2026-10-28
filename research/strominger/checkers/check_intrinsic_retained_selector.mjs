// Attempt to falsify intrinsic next-operation selection under the implemented native contract.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {applyPhasePermutation,phaseFrame} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const hash=x=>createHash('sha256').update(JSON.stringify(x)).digest('hex');
const names=['C0','M0','C1','M1'];
const initial=[[2,1],[3,-2],[5,3],[7,-4],[11,5]];
const base=new GenerativeAssemblyRules();
const vertices=names.map(n=>base.charts[base.packets[base.root].chart].aliases[n]);
const prefixes=[[],['reader-phase-advance'],['reader-phase-advance','reader-phase-advance'],['PN','inverse-PN']];
const suffixes=[['PN','NE'],['reader-phase-advance','PN','NE']];
const checks=[];
const check=(name,f)=>{f();checks.push(name);};
function prepare(bindings,prefix){
 const rules=new GenerativeAssemblyRules({seedBindings:bindings});
 const run={rules,active:rules.root,retained:[rules.root],history:[],coefficients:structuredClone(initial)};
 for(const kind of prefix)step(run,kind);
 return run;
}
function step(run,kind){
 const {rules}=run;
 const candidates=rules.outgoing(run.active).map(i=>rules.operations[i]).filter(o=>o.kind===kind);
 assert.equal(candidates.length,1);const op=candidates[0];assert(rules.validateTransfer(op));
 const before=structuredClone(run.coefficients);
 run.coefficients=applyPhasePermutation(before,op.permutation);
 assert.deepEqual(applyPhasePermutation(run.coefficients,op.permutation,-1),before);
 run.history.push({operation:structuredClone(op),coefficientsBefore:before,coefficientsAfter:structuredClone(run.coefficients)});
 run.active=op.target;if(!run.retained.includes(op.target))run.retained.push(op.target);
 assert(rules.describe(run.retained).valid);
 return op;
}
function snapshot(run){
 const {rules}=run;
 // Realize all currently offered local alternatives, not a chosen future.
 const offered=rules.outgoing(run.active).map(i=>rules.operations[i]);
 const assembly=rules.inspect(run.retained);assert(assembly.valid);
 const packets=run.retained.map(id=>structuredClone(rules.packets[id]));
 const charts=[...new Set(packets.map(p=>p.chart))].map(i=>structuredClone(rules.charts[i]));
 const cells=[...new Set(charts.map(c=>c.cell))].map(i=>structuredClone(rules.geometry.cells[i]));
 const references=[...new Set(charts.flatMap(c=>Object.values(c.aliases)))];
 return {active:run.active,coefficients:structuredClone(run.coefficients),initialCoefficients:initial,
  orderedHistory:structuredClone(run.history),retainedPackets:packets,charts,cells,
  referencePoints:Object.fromEntries(references.map(k=>[k,rules.geometry.points.get(k)])),
  frames:packets.map(p=>phaseFrame(rules.charts[p.chart],p.origin)),
  assembly,offeredOperations:structuredClone(offered)};
}
const records=[];
for(const [marking,order] of permutations(vertices).entries()){
 const bindings=Object.fromEntries(names.map((n,i)=>[n,order[i]]));
 for(const [prefixIndex,prefix] of prefixes.entries()){
  const exemplar=prepare(bindings,prefix),source=snapshot(exemplar),sourceHash=hash(source);
  const branches=[];
  for(const suffix of suffixes){
   const run=prepare(bindings,prefix),fork=snapshot(run);
   assert.deepEqual(fork,source);assert.equal(hash(fork),sourceHash);
   const first=step(run,suffix[0]);
   const immediate=run.rules.inspect(run.retained);
   assert(immediate.valid);assert(immediate.allContactsWitnessed);
   for(const kind of suffix.slice(1))step(run,kind);
   const target=run.rules.inspect(run.retained);
   assert(target.valid);assert(target.certifiedExit);assert(target.allPacketsCanReachExit);
   assert(target.allCellsOnEntryExitPaths);assert(target.allContactsWitnessed);assert.equal(target.pendingContacts.length,0);
   const packet=run.rules.packets[run.active],chart=run.rules.charts[packet.chart];
   assert.equal(chart.species,'electron');
   // Keep the whole ordered history; do not identify a source return with an empty history.
   assert.equal(run.history.length,prefix.length+suffix.length);
   assert.deepEqual(run.history.slice(0,prefix.length),source.orderedHistory);
   branches.push({sourceHash,firstOperation:first,suffix,immediateAssembly:immediate,
    terminalPacket:packet,terminalChart:chart,coefficients:run.coefficients,
    retainedPackets:run.retained,history:run.history,terminalAssembly:target});
  }
  check(`marking${marking}/prefix${prefixIndex}: exact retained source forks to two certified exits`,()=>{
   assert.equal(branches[0].sourceHash,branches[1].sourceHash);
   assert.notEqual(branches[0].firstOperation.kind,branches[1].firstOperation.kind);
   assert.notEqual(branches[0].firstOperation.target,branches[1].firstOperation.target);
   assert.equal(branches[1].terminalPacket.origin,branches[0].terminalPacket.origin+1);
   assert.notDeepEqual(branches[0].coefficients,branches[1].coefficients);
  });
  records.push({marking,prefixIndex,seedBindings:bindings,prefix,sourceHash,source,branches});
 }
}
check('nonempty reference-return history is retained rather than collapsed to the seed',()=>{
 const seed=records.find(r=>r.marking===0&&r.prefixIndex===0);
 const returned=records.find(r=>r.marking===0&&r.prefixIndex===3);
 assert.equal(returned.source.active,seed.source.active);
 assert.deepEqual(returned.source.coefficients,seed.source.coefficients);
 assert.equal(returned.source.orderedHistory.length,2);
 assert.notEqual(returned.sourceHash,seed.sourceHash);
 assert(returned.source.retainedPackets.length>seed.source.retainedPackets.length);
});
check('invalid coefficient or phase witnesses are rejected by the source validator',()=>{
 const run=prepare(null,[]),op=run.rules.outgoing(run.active).map(i=>run.rules.operations[i]).find(o=>o.kind==='PN');
 assert.throws(()=>run.rules.validateTransfer({...op,permutation:[0,1,2,3,4]}));
 assert.throws(()=>run.rules.validateTransfer({...op,phaseDelta:1}));
});
const paths=['research/nima/generative-phase-assembly.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs',
 'research/strominger/checkers/check_intrinsic_retained_selector.mjs'];
const sourceSha256=Object.fromEntries(await Promise.all(paths.map(async p=>[p,createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex')])));
const report={status:'passed',conjectureOutcome:'native-contract uniqueness falsified',checks,checkCount:checks.length,
 sourceSha256,sourceCount:records.length,certifiedContinuations:2*records.length,records,
 disposition:{intrinsicNativeSelector:'refuted: the identical retained native state admits both PN and reader-phase-advance, each extendable to a fully certified E exit',
  historyOnlyRepair:'the tested histories do not resolve the ambiguity; includes nonempty PN/inverse-PN return with its N packet retained',
  globalConjecture:'open only for an explicitly richer state or additional selection constraint, neither supplied by this audit',
  sevenAnd28Stages:'not inferred: admissibility and eventual exit do not select a clock'},
 scope:'All24 seed markings and four explicit history prefixes. Full means the implemented native retained packet/assembly/history contract, not an unspecified global field or every analytical esd7 witness. Source validation includes occurrence/phase, coefficient permutation, geometric shared faces, global C/M roles, contact witnesses and exit reachability. No selection law or arbitrary preference is added.'};
const dest=path.join(root,'research/strominger/results/intrinsic-retained-selector.json');
await fs.mkdir(path.dirname(dest),{recursive:true});await fs.writeFile(dest,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,conjectureOutcome:report.conjectureOutcome,checks:checks.length,sources:records.length,certifiedContinuations:report.certifiedContinuations,result:dest}));
