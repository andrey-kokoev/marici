import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {selectBrowserMatrix,browserMatrixResult} from './isotope-browser-matrix-contract.mjs';
const root=fileURLToPath(new URL('../',import.meta.url));

export function validateBrowserEvidence(evidence,manifest){
 assert.equal(evidence.schema,'marici.isotope-wiring-browser-evidence.v1');
 assert.equal(evidence.result,'passed');assert.equal(evidence.source_unchanged,true);
 assert.equal(evidence.matrix,'config/isotope-wiring-browser-matrix.v1.json');
 assert.match(evidence.base_commit,/^[a-f0-9]{40}$/);assert.equal(typeof evidence.worktree_dirty,'boolean');
 const selection=selectBrowserMatrix(manifest),count=selection.engines.length*selection.cases.length;
 assert.equal(evidence.passed,count);assert.equal(evidence.failed,0);assert.equal(evidence.not_run,0);
 assert.equal(browserMatrixResult(manifest,selection,evidence.runs,evidence.source_unchanged),'passed');
 for(const run of evidence.runs){
  assert.equal(typeof evidence.engine_versions[run.engine],'string');
  assert.equal(run.engine_version,evidence.engine_versions[run.engine]);
  assert.match(run.diagnostic_log_sha256,/^[a-f0-9]{64}$/);
 }
 const required=['examples/isotope-wiring/index.html',evidence.matrix,'scripts/isotope-browser.mjs',...manifest.cases.map(c=>'scripts/'+c.script)];
 for(const file of required)assert(Object.hasOwn(evidence.source_sha256,file),'Missing tested source identity: '+file);
 for(const [file,hash] of Object.entries(evidence.source_sha256)){
  assert(!file.startsWith('/')&&!file.includes('\\')&&!file.split('/').includes('..')&&!file.includes(':'),'Unsafe tested source path');
  assert.match(hash,/^[a-f0-9]{64}$/);
 }
 return count;
}

export async function checkBrowserEvidence(base=root){
 const manifest=JSON.parse(await fs.readFile(path.join(base,'config/isotope-wiring-browser-matrix.v1.json'),'utf8'));
 const evidence=JSON.parse(await fs.readFile(path.join(base,'config/isotope-wiring-browser-evidence.v1.json'),'utf8'));
 const count=validateBrowserEvidence(evidence,manifest);
 for(const [file,hash] of Object.entries(evidence.source_sha256)){
  const current=createHash('sha256').update(await fs.readFile(path.join(base,file))).digest('hex');
  assert.equal(current,hash,'Recorded browser evidence has stale source bytes: '+file);
 }
 return {scope:'Recorded local browser evidence and byte freshness only; no browser replay or scientific acceptance',run_id:evidence.run_id,cases:count,engine_versions:evidence.engine_versions};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))console.log(JSON.stringify(await checkBrowserEvidence()));
