// Same reference grammar and D10 bound, retain 7P/7N but leave E quota free.
import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
const out='research/strominger/results/reference-n14-search',hash=b=>createHash('sha256').update(b).digest('hex'),main=JSON.parse(await readFile(out+'/verification.json'));
for(const [f,h] of Object.entries(main.sourceHashes))assert.equal(hash(await readFile(new URL(f,import.meta.url))),h);
const input=JSON.parse(await readFile(out+'/D10-input.json'));assert.equal(hash(await readFile(out+'/D10-input.json')),main.rows.find(r=>r.maxOrigin===10).inputSha256);input.target={proton:7,neutron:7};
const inputPath=out+'/charge-control-input.json',outputPath=out+'/charge-control-solver.json';await writeFile(inputPath,JSON.stringify(input)+'\n');
const child=spawnSync(globalThis.process.platform==='win32'?'uv.exe':'uv',['run','--with','z3-solver','python','research/strominger/checkers/solve_reference_n14.py',inputPath,outputPath],{encoding:'utf8',timeout:150000});assert.equal(child.status,0,child.stderr??String(child.error));
const solver=JSON.parse(await readFile(outputPath));let witness=null;
if(solver.status==='sat'){
 const u=phaseUniverse({maxOrigin:10,maxPackets:5000});assert.equal(u.complete,true);const {rules}=u,selected=new Set(solver.selectedPackets),inspection=rules.inspect([...selected]);assert.equal(inspection.certifiedExit,true);assert.equal(inspection.counts.proton,7);assert.equal(inspection.counts.neutron,7);assert.notEqual(inspection.counts.electron,7);
 const reached=new Set([rules.root]),word=[];for(let changed=true;changed;){changed=false;for(const i of u.operations){const op=rules.operations[i];if(reached.has(op.source)&&selected.has(op.target)&&!reached.has(op.target)){rules.validateTransfer(op);reached.add(op.target);word.push(i);assert.equal(rules.describe([...reached]).valid,true);changed=true;}}}assert.equal(reached.size,selected.size);
 witness={counts:inspection.counts,formalCharge:7-inspection.counts.electron,inspection,selectedPackets:[...selected],grade:Math.max(...[...selected].map(i=>rules.packets[i].origin)),constructionWord:word,packets:[...selected].map(i=>rules.packets[i]),charts:[...new Set([...selected].map(i=>rules.packets[i].chart))].map(i=>rules.charts[i]),operations:u.operations.filter(i=>selected.has(rules.operations[i].source)&&selected.has(rules.operations[i].target)).map(i=>rules.operations[i]),bodies:[...rules.describe([...selected]).bodies].map(([cell,species])=>({species,key:rules.geometry.cells[cell].key,vertices:rules.geometry.cells[cell].vertices.map(v=>rules.geometry.points.get(v))})),globalFieldSewingAsserted:false};
}
const result={status:solver.status,maxOrigin:10,electronQuota:'unconstrained',fixedCounts:{proton:7,neutron:7},inputSha256:hash(await readFile(inputPath)),solver,witness,scope:'Diagnostic only. Same reference grammar and all-contact/exit certificate as the neutral target, no electron cardinality constraint. A SAT charged example does not classify possible electron counts or show stability/binding/global field sewing.'};await writeFile(out+'/charge-control-verification.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({status:solver.status,counts:witness?.counts,formalCharge:witness?.formalCharge,grade:witness?.grade,records:witness?.selectedPackets.length},null,2));
