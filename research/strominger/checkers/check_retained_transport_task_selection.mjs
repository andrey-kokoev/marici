// Observable task predicates are declared separately from native operation kinds.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {applyPhasePermutation,phaseFrame} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const contractPath='research/strominger/contracts/retained-transport-task-selection.v1.json';
const contract=JSON.parse(await fs.readFile(path.join(root,contractPath),'utf8'));
const permute=a=>a.length?a.flatMap((v,i)=>permute(a.filter((_,j)=>i!==j)).map(t=>[v,...t])):[[]];
const hash=x=>createHash('sha256').update(JSON.stringify(x)).digest('hex');
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const names=['C0','M0','C1','M1'],initial=[[2,1],[3,-2],[5,3],[7,-4],[11,5]];
const base=new GenerativeAssemblyRules(),vertices=names.map(n=>base.charts[base.packets[base.root].chart].aliases[n]);
const checks=[];function check(name,f){f();checks.push(name);}
function prepare(bindings,prefix){
 const rules=new GenerativeAssemblyRules({seedBindings:bindings});
 const run={rules,active:rules.root,retained:[rules.root],history:[],coefficients:structuredClone(initial)};
 for(const kind of prefix)commitKind(run,kind);
 return run;
}
function commit(run,op){
 const r=run.rules;assert.equal(op.source,run.active);assert(r.validateTransfer(op));
 const before=structuredClone(run.coefficients);run.coefficients=applyPhasePermutation(before,op.permutation);
 assert.deepEqual(applyPhasePermutation(run.coefficients,op.permutation,-1),before);
 run.history.push({operation:structuredClone(op),before,after:structuredClone(run.coefficients)});
 run.active=op.target;if(!run.retained.includes(run.active))run.retained.push(run.active);
 assert(r.describe(run.retained).valid);
}
function commitKind(run,kind){
 const ops=run.rules.outgoing(run.active).map(i=>run.rules.operations[i]).filter(o=>o.kind===kind);
 assert.equal(ops.length,1);commit(run,ops[0]);
}
function sourceState(run){
 const r=run.rules,offered=r.outgoing(run.active).map(i=>structuredClone(r.operations[i]));
 const assembly=r.inspect(run.retained);assert(assembly.valid);
 const packets=run.retained.map(i=>structuredClone(r.packets[i]));
 const charts=[...new Set(packets.map(p=>p.chart))].map(i=>structuredClone(r.charts[i]));
 return {active:run.active,coefficients:structuredClone(run.coefficients),history:structuredClone(run.history),
  retainedPackets:packets,charts,cells:[...new Set(charts.map(c=>c.cell))].map(i=>structuredClone(r.geometry.cells[i])),
  referencePoints:Object.fromEntries([...new Set(charts.flatMap(c=>Object.values(c.aliases)))].map(k=>[k,r.geometry.points.get(k)])),
  frames:packets.map(p=>phaseFrame(r.charts[p.chart],p.origin)),assembly,offered};
}
function meetsTask(run,op,task){
 // No op.kind condition: select by independently declared state changes.
 const r=run.rules,from=r.packets[op.source],to=r.packets[op.target];
 const a=r.charts[from.chart],b=r.charts[to.chart];
 if(to.origin-from.origin!==contract.common.originDelta||a.species!==b.species)return false;
 const f=phaseFrame(a,from.origin),g=phaseFrame(b,to.origin);
 if(!same(f.window[2],g.window[0])||!same(f.context,g.window[1]))return false;
 if(task.geometry==='same'&&a.cell!==b.cell)return false;
 if(task.geometry==='shared-face'){
  if(a.cell===b.cell)return false;
  const common=r.geometry.cells[a.cell].vertices.filter(v=>r.geometry.cells[b.cell].vertices.includes(v));
  if(common.length!==3)return false;
 }
 assert(r.validateTransfer(op));
 const next=applyPhasePermutation(run.coefficients,op.permutation);
 assert.deepEqual(applyPhasePermutation(next,op.permutation,-1),run.coefficients);
 const d=r.inspect([...new Set([...run.retained,op.target])]);
 return d.valid&&d.allContactsWitnessed;
}
const records=[];
for(const [marking,order] of permute(vertices).entries()){
 const bindings=Object.fromEntries(names.map((n,i)=>[n,order[i]]));
 for(const [species,prefix] of [['proton',[]],['neutron',['PN']]]){
  const run=prepare(bindings,prefix),source=sourceState(run),sourceHash=hash(source);
  const offered=source.offered.map(o=>run.rules.operations[o.id]);
  const selected=Object.fromEntries(contract.tasks.map(task=>[task.id,offered.filter(op=>meetsTask(run,op,task))]));
  const activeChart=run.rules.charts[run.rules.packets[run.active].chart];
  const c1=activeChart.aliases.C1.split(',').map(Number),c2=activeChart.aliases.C2.split(',').map(Number);
  const contextDistanceSquared=c1.reduce((n,x,i)=>n+(x-c2[i])**2,0);
  const phaseAvailable=species==='proton'||contextDistanceSquared===4;
  check(`marking${marking}/${species}: observable task counts and subdivision domain`,()=>{
   assert.equal(selected['advance-realization'].length,phaseAvailable?(species==='proton'?1:2):0);
   assert.equal(selected['reread-fixed-carrier'].length,phaseAvailable?1:0);
   assert.equal(selected['propagate-across-face'].length,species==='neutron'&&phaseAvailable?1:0);
  });
  const branches=[];
  for(const selectedOp of selected['advance-realization']){
   const fork=prepare(bindings,prefix),snapshot=sourceState(fork);
   assert.deepEqual(snapshot,source);assert.equal(hash(snapshot),sourceHash);
   const op=fork.rules.outgoing(fork.active).map(i=>fork.rules.operations[i]).find(o=>o.id===selectedOp.id);
   for(const task of contract.tasks)assert.equal(meetsTask(fork,op,task),selected[task.id].some(o=>o.id===op.id));
   commit(fork,op);
   const targetPacket=structuredClone(fork.rules.packets[fork.active]);
   const targetChart=structuredClone(fork.rules.charts[targetPacket.chart]);
   const targetGeometry=structuredClone(fork.rules.geometry.cells[targetChart.cell]);
   const taskResultCoefficients=structuredClone(fork.coefficients);
   // These suffixes prove viability only; they are not used to choose the task's first step.
   if(species==='proton')commitKind(fork,'PN');
   commitKind(fork,'NE');
   const exit=fork.rules.inspect(fork.retained);
   assert(exit.valid&&exit.certifiedExit&&exit.allContactsWitnessed&&exit.allPacketsCanReachExit&&exit.allCellsOnEntryExitPaths);
   assert.equal(exit.pendingContacts.length,0);
   branches.push({sourceHash,operation:op,targetPacket,targetChart,targetGeometry,taskResultCoefficients,
     certifiedExit:exit,completeHistory:fork.history,terminalCoefficients:fork.coefficients});
  }
  if(species==='neutron'&&phaseAvailable)check(`marking${marking}: fixed task and full source retain two distinct viable successors`,()=>{
   assert.equal(branches[0].sourceHash,branches[1].sourceHash);
   assert.notEqual(branches[0].targetChart.cell,branches[1].targetChart.cell);
   assert.equal(branches[0].targetPacket.origin,branches[1].targetPacket.origin);
   assert.deepEqual(branches[0].taskResultCoefficients,branches[1].taskResultCoefficients);
   assert.notDeepEqual(branches[0].targetChart.aliases,branches[1].targetChart.aliases);
   assert.notDeepEqual(branches[0].completeHistory,branches[1].completeHistory);
  });
  records.push({marking,species,bindings,prefix,sourceHash,source,contextDistanceSquared,phaseAvailable,
   taskMatches:Object.fromEntries(Object.entries(selected).map(([id,ops])=>[id,ops.map(o=>({id:o.id,kind:o.kind}))])),branches});
 }
}
check('eight neutron markings admit the task and sixteen do not in the fixed subdivision',()=>{
 assert.equal(records.filter(r=>r.species==='neutron'&&r.phaseAvailable).length,8);
 assert.equal(records.filter(r=>r.species==='neutron'&&!r.phaseAvailable).length,16);
});
check('all counterexamples use a nonempty retained PN history',()=>{
 for(const r of records.filter(r=>r.species==='neutron'&&r.phaseAvailable)){
  assert.equal(r.source.history.length,1);assert.equal(r.source.retainedPackets.length,2);
 }
});
const files=[contractPath,'research/nima/generative-phase-assembly.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs',
 'research/strominger/checkers/check_retained_transport_task_selection.mjs'];
const sourceSha256=Object.fromEntries(await Promise.all(files.map(async p=>[p,createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex')])));
const report={status:'passed',conjectureOutcome:'general task-relative uniqueness falsified under the native contract',
 checks,checkCount:checks.length,contract,sourceSha256,records,
 counts:{sources:records.length,fixedTaskCounterexamples:records.filter(r=>r.branches.length===2).length,certifiedContinuations:records.reduce((n,r)=>n+r.branches.length,0)},
 disposition:{advanceRealization:'one successor at24 P states; two at8 N states despite identical task/history/origin increment/coefficient output; unavailable at16 N states in the fixed subdivision',
 fixedCarrierRefinement:'unique on32 tested sources, unavailable on16 N sources',crossFaceRefinement:'unique on8 tested N sources, unavailable on all24 P sources and16 N sources',
 missingDatum:'the task must distinguish rereading the same carrier from propagation to a neighboring carrier; broad phase/species/coefficient requirements do not do this',
 globalExtension:'not established; these local tasks preserve species and cannot alone generate P/E exchange or a seven-stage clock'},
 scope:'Twenty-four native seed markings, one P and one retained PN-prepared N state per marking. A counterexample to uniqueness from the stated task constraints, not to existence of a separately specified deterministic policy or an enriched global theory. No operation-name predicate or stage schedule is used to select the first step.'};
const dest=path.join(root,'research/strominger/results/retained-transport-task-selection.json');
await fs.mkdir(path.dirname(dest),{recursive:true});await fs.writeFile(dest,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,outcome:report.conjectureOutcome,checks:checks.length,...report.counts,result:dest}));
