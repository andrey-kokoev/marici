// Budget-only retry of the unresolved Ne-21 bound. Preserve prior evidence.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';
const base='research/strominger/results/reference-ne21-search',out=base+'/origin9-600s',source='research/strominger/checkers/solve_reference_n14.py',hash=b=>createHash('sha256').update(b).digest('hex');
const preserved=[base+'/D9-input.json',base+'/D9-solver.json',base+'/D9-verification.json',base+'/verification.json',source],before={};for(const f of preserved)before[f]=hash(await readFile(f));
const text=await readFile(source,'utf8');assert.equal(text.split('120000').length,3);const snapshot=text.replaceAll('120000','600000');
await mkdir(out,{recursive:true});const solverFile=out+'/solve_reference_600s.py',output=out+'/solver.json';await writeFile(solverFile,snapshot);
const startedAt=new Date().toISOString(),start=Date.now();
const child=spawnSync(process.platform==='win32'?'uv.exe':'uv',['run','--with','z3-solver==5.3.1','python',solverFile,base+'/D9-input.json',output],{encoding:'utf8',timeout:900000});
await writeFile(out+'/process.log',(child.stdout??'')+'\n'+(child.stderr??''));
let solver=null;if(child.status===0){solver=JSON.parse(await readFile(output));assert.equal(solver.timeoutMs,600000);assert.equal(solver.solver,'z3-5.3.1');}
for(const f of preserved)assert.equal(hash(await readFile(f)),before[f],f+' changed during retry');
const receipt={status:solver?.status??'unknown',startedAt,elapsedSeconds:(Date.now()-start)/1000,solverTimeoutMs:600000,processTimeoutMs:900000,processStatus:child.status,signal:child.signal,error:child.error?.message??null,preservedHashes:before,solverSnapshotSha256:hash(snapshot),solver,scope:'Identical saved origin-9 Ne-21 input, Z3 version and random seed. Only solver budget increased from 120s to 600s. Prior evidence preserved. SAT requires source-rule reconstruction and fresh replay before certification or viewer admission.'};
await writeFile(out+'/verification.json',JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify({status:receipt.status,elapsedSeconds:receipt.elapsedSeconds,solverSeconds:solver?.elapsedSeconds,unknownReason:solver?.unknownReason,error:receipt.error}));
