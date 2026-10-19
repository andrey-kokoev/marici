// Read-only source-owner audit, with outputs confined to Strominger's locus.
import assert from 'node:assert/strict';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {compileTessellatedAtlas} from '../../nima/tessellated-atlas.mjs';
import {replayExecution} from '../../nima/atlas-execution-plans.mjs';
const root=new URL('../../../',import.meta.url);
const hash=b=>createHash('sha256').update(b).digest('hex');
const load=async path=>JSON.parse(await readFile(new URL(path,root),'utf8'));
const reports=[];
for(const path of ['research/nima/results/experimental-terminal-pe/verification.json','research/nima/results/tessellated-atlas/verification.json','research/nima/results/atlas-execution-plans/verification.json']){
 const r=await load(path);
 const expected={'research/nima/results/experimental-terminal-pe/verification.json':'pass-small-complete-guarded-families-and-saved-controls','research/nima/results/tessellated-atlas/verification.json':'pass-side-by-side-refactor','research/nima/results/atlas-execution-plans/verification.json':'pass'};
 assert.equal(r.status,expected[path]);let checked=0;
 for(const [source,digest] of Object.entries(r.sourceHashes??{})){
  assert.equal(hash(await readFile(new URL(source.replaceAll('\\','/'),root))),digest,`stale source: ${source}`);checked++;
 }
 if(r.plansPath)assert.equal(hash(await readFile(new URL(r.plansPath,root))),r.plansSha256);
 reports.push({path,sourceHashesChecked:checked,scope:r.scope??null});
}
const planPath='research/nima/results/atlas-execution-plans/two-reader-plan.json',plan=await load(planPath);
const model=compileTessellatedAtlas({maxOrigin:plan.maxOrigin,mode:plan.mode});
const replay=replayExecution(model,plan);assert.equal(replay.status,'pass');assert.equal(replay.batches,1);
const bad=structuredClone(plan);bad.steps=[];assert.throws(()=>replayExecution(model,bad));
const result={status:'pass',reports,twoReaderPlanFreshReplay:replay,deletedStepRejected:true,
 scope:'Hash audit of three later Nima receipts plus fresh source replay of one atomic two-reader plan; not fresh exhaustive atlas generation, an occupancy derivation, new isotope search or native adoption.'};
const out=new URL('../results/isotope-resume-audit/',import.meta.url);await mkdir(out,{recursive:true});
await writeFile(new URL('verification.json',out),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result,null,2));
