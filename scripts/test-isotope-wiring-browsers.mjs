import {spawnSync,execFileSync} from 'node:child_process';
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {createHash,randomUUID} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
import {launchBrowser} from './isotope-browser.mjs';
import {selectBrowserMatrix,browserMatrixResult} from './isotope-browser-matrix-contract.mjs';

const root=fileURLToPath(new URL('../',import.meta.url));
const matrixPath='config/isotope-wiring-browser-matrix.v1.json';
const manifest=JSON.parse(await fs.readFile(path.join(root,matrixPath),'utf8'));
const selection=selectBrowserMatrix(manifest,process.argv.slice(2));
const runId=randomUUID(),output=path.join(root,'.ai/isotope-browser-matrix',runId);
await fs.mkdir(output,{recursive:true});
const sources=[matrixPath,'scripts/isotope-browser.mjs','scripts/isotope-browser-matrix-contract.mjs','scripts/test-isotope-wiring-browsers.mjs',
 'examples/isotope-wiring/index.html','examples/isotope-wiring/core/ne20-inventory.json',
 'website/.vitepress/components/IsotopeWiring.vue','website/experiments/isotope-wiring.md',
 'website/.vitepress/dist/experiments/isotope-wiring-standalone.html',
 ...manifest.cases.map(c=>'scripts/'+c.script)];
const fingerprint=async()=>Object.fromEntries(await Promise.all(sources.map(async file=>[file,createHash('sha256').update(await fs.readFile(path.join(root,file))).digest('hex')])));
const before=await fingerprint();
const require=createRequire(import.meta.url);
const report={schema:'marici.isotope-wiring-browser-report.v1',run_id:runId,matrix:matrixPath,contract:manifest.contract,
 base_commit:execFileSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8'}).trim(),
 worktree_dirty:!!execFileSync('git',['status','--porcelain','--untracked-files=normal'],{cwd:root,encoding:'utf8'}).trim(),
 recorded_at_host_utc:new Date().toISOString(),clock_scope:'Host clock metadata; not an independently verified calendar or scientific execution date',
 node:process.version,playwright:require('@playwright/test/package.json').version,platform:os.platform(),
 selected_engines:selection.engines,selected_cases:selection.cases.map(c=>c.id),engine_versions:{},runs:[],source_sha256:before,
 source_scope:'Declared delivered HTML/embedded snapshot, host wrapper, matrix and test scripts; not a transitive dependency certificate',limits:manifest.limits};
const reportFile=path.join(output,'report.json');
const save=()=>fs.writeFile(reportFile,JSON.stringify(report,null,2)+'\n');
await save();
for(const engine of selection.engines){
 let unavailable;
 try{const browser=await launchBrowser(engine);try{report.engine_versions[engine]=browser.version();}finally{await browser.close();}}
 catch(error){unavailable=error.message;report.engine_versions[engine]=null;}
 let failed=!!unavailable;
 for(const c of selection.cases){
  if(failed){report.runs.push({engine,case:c.id,status:'not_run',reason:unavailable?'engine_unavailable: '+unavailable:'stopped_after_failure'});await save();continue;}
  console.log(`=== ${engine}: ${c.id} ===`);
  const start=performance.now();
  const result=spawnSync(process.execPath,[path.join(root,'scripts',c.script)],{
   cwd:root,env:{...process.env,ISOTOPE_BROWSER:engine},encoding:'utf8',timeout:180000,maxBuffer:16*1024*1024,shell:false,
  });
  const log=engine+'-'+c.id+'.log';
  await fs.writeFile(path.join(output,log),(result.stdout||'')+(result.stderr||'')+(result.error?'\n'+result.error.message:''));
  const actualVersion=result.stdout?.match(new RegExp('Browser version: '+engine+' ([^\\r\\n]+)'))?.[1];
  const passed=!result.error&&result.status===0&&actualVersion===report.engine_versions[engine];
  report.runs.push({engine,case:c.id,status:passed?'passed':'failed',exit_code:result.status,signal:result.signal??null,duration_ms:Math.round(performance.now()-start),log,scope:c.scope,engine_version:actualVersion??null});
  if(!passed)failed=true;
  console.log(`${passed?'PASS':'FAIL'} ${engine}: ${c.id}`);await save();
 }
}
const after=await fingerprint();
report.source_unchanged=JSON.stringify(before)===JSON.stringify(after);
report.result=browserMatrixResult(manifest,selection,report.runs,report.source_unchanged);
report.passed=report.runs.filter(r=>r.status==='passed').length;
report.failed=report.runs.filter(r=>r.status==='failed').length;
report.not_run=report.runs.filter(r=>r.status==='not_run').length;
await save();
console.log(JSON.stringify({result:report.result,passed:report.passed,failed:report.failed,not_run:report.not_run,engine_versions:report.engine_versions,report:path.relative(root,reportFile).split(path.sep).join('/')}));
if(!['passed','partial_pass'].includes(report.result))process.exitCode=1;
