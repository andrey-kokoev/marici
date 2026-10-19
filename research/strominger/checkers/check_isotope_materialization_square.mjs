// Reuse Nima's planner read-only on the new fixed-footprint isotope family.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {compileTessellatedAtlas} from '../../nima/tessellated-atlas.mjs';
import {planExecution,replayExecution} from '../../nima/atlas-execution-plans.mjs';
const ROOT=new URL('../../../',import.meta.url),OUT=new URL('../results/isotope-obstruction-atlas/',import.meta.url);
const hash=b=>createHash('sha256').update(b).digest('hex'),sourceHashes={};
async function load(path){const b=await readFile(new URL(path,ROOT));sourceHashes[path]=hash(b);return JSON.parse(b);}
const atlas=await load('research/strominger/results/isotope-obstruction-atlas/verification.json');assert.equal(atlas.status,'pass');
const summary=await load('research/strominger/results/reference-ne22-search/verification.json');
const row=summary.rows.find(x=>x.witnessFile),w=(await load('research/strominger/results/reference-ne22-search/'+row.witnessFile)).witness;
const model=compileTessellatedAtlas({maxOrigin:row.maxOrigin,mode:'experimental-terminal-PE'});
for(const p of w.packets)assert.deepEqual(model.universe.rules.packets[p.id],p);
for(const o of w.operations)assert.deepEqual(model.universe.rules.operations[o.id],o);
const positives=atlas.families['ne22-double'].filter(r=>r.predictedPass);assert.equal(positives.length,1);
const pair=positives[0],refs=[...new Set(pair.shortcuts.map(o=>o.referenceBody))].sort((a,b)=>a-b);assert.equal(refs.length,2);
const singles=refs.map(body=>atlas.families['ne22-single'].find(r=>r.label===`ne22:delete:${body}`));assert(singles.every(r=>r.fullAuditPass));
const routes=[...singles.flatMap(s=>[{name:`double-to-${s.label}`,start:pair.selectedPackets,target:s.selectedPackets},{name:`${s.label}-to-native-ne22`,start:s.selectedPackets,target:w.selectedPackets}]),{name:'double-to-native-ne22',start:pair.selectedPackets,target:w.selectedPackets}];
const results=[];
for(const route of routes){
 const plan=planExecution(model,route.start,route.target,{maxStates:100000,maxMilliseconds:10000});
 const replay=plan.status==='planned'?replayExecution(model,plan):null;
 const singletonOnly=planExecution(model,route.start,route.target,{maxStates:100000,maxMilliseconds:10000,allowMaterialization:false});
 results.push({name:route.name,status:plan.status,replay,plan,singletonOnly:{status:singletonOnly.status,reason:singletonOnly.reason??null,steps:singletonOnly.steps?.length??null}});
}
const batchPlan=results.find(r=>r.plan.steps?.some(s=>s.kind==='body-materialization'))?.plan;
assert(batchPlan,'Expected a tested atomic route');
const omitted=structuredClone(batchPlan);omitted.steps=[];assert.throws(()=>replayExecution(model,omitted));
const partial=structuredClone(batchPlan),batch=partial.steps.find(s=>s.kind==='body-materialization');
assert.equal(batch.added.length,2);batch.added.pop();assert.throws(()=>replayExecution(model,partial));
for(const path of ['research/strominger/checkers/check_isotope_materialization_square.mjs','research/nima/tessellated-atlas.mjs','research/nima/atlas-execution-plans.mjs','research/nima/body-coherent-materialization.mjs','research/nima/experimental-terminal-pe.mjs'])sourceHashes[path]=hash(await readFile(new URL(path,ROOT)));
const allPlanned=results.every(r=>r.status==='planned');
const result={status:allPlanned?'pass':'counterexample-or-resource-stop',sourceHashes,maxOrigin:row.maxOrigin,referenceBodies:refs,
 hostileRejections:['omitted-step','partial-two-reader-batch'],
 allFiveRoutesPlanned:results.every(r=>r.status==='planned'),routes:results,
 scope:'Five fixed-target interval planning tests under the existing experimental singleton/whole-body operations. Records unreachable/incomplete results without treating them as scientific impossibilities. No complete origin-four atlas, physical synthesis or equality of intermediate route histories claimed.'};
await mkdir(OUT,{recursive:true});await writeFile(new URL('materialization-square.json',OUT),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,allFiveRoutesPlanned:result.allFiveRoutesPlanned,referenceBodies:refs,routes:results.map(({name,status,replay,singletonOnly})=>({name,status,replay,singletonOnly}))},null,2));
assert(allPlanned,'Not every proposed target route was planned; inspect saved residuals');
