import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {mixedUniverse,buildMixedInput} from './mixed-subdivision-model.mjs';
const hash=b=>createHash('sha256').update(b).digest('hex'),out='research/strominger/results/mixed-subdivision-n14',files=['./search_mixed_n14.mjs','./mixed-subdivision-model.mjs','./solve_mixed_n14.py','../mixed-subdivision-protocol-v1.md','../../nima/generative-phase-assembly.mjs',...['window-construction-model.mjs','lattice-items.mjs','simplex-components.mjs','carrier.mjs','phase-advance-model.mjs','phase-discipline-model.mjs','deuterium-tunnel-model.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f)],sourceHashes={};for(const f of files)sourceHashes[f]=hash(await readFile(new URL(f,import.meta.url)));
await mkdir(out,{recursive:true});const rows=[];
for(const maxOrigin of [3,4,5,6,7,8]){
 const u=mixedUniverse({maxOrigin,maxPackets:5000,maxOperations:50000,maxEvaluations:100000});
 if(!u.complete){rows.push({maxOrigin,universeComplete:false,status:'incomplete',stop:u.stop});break;}
 const input=buildMixedInput(u,{proton:7,neutron:7,electron:7}),inputPath=out+`/D${maxOrigin}-input.json`,outputPath=out+`/D${maxOrigin}-solver.json`;await writeFile(inputPath,JSON.stringify(input)+'\n');console.log(JSON.stringify({maxOrigin,packets:u.packets.length,operations:u.operations.length,choiceItems:input.items.length,stage:'solving'}));
 const child=spawnSync(process.platform==='win32'?'uv.exe':'uv',['run','--with','z3-solver','python','research/strominger/checkers/solve_mixed_n14.py',inputPath,outputPath],{encoding:'utf8',timeout:600000});if(child.status!==0){
  const row={maxOrigin,universeComplete:true,universePackets:u.packets.length,universeOperations:u.operations.length,choiceItems:input.items.length,inputSha256:hash(await readFile(inputPath)),solver:{status:'unknown',reason:'solver-process-did-not-complete',processStatus:child.status,signal:child.signal,error:child.error?.message??null,stderr:child.stderr,processTimeoutMs:600000},witness:null};
  await writeFile(out+`/D${maxOrigin}-verification.json`,JSON.stringify(row,null,2)+'\n');rows.push(row);console.log(JSON.stringify({maxOrigin,status:'unknown',reason:row.solver.error}));break;
 }
 const solver=JSON.parse(await readFile(outputPath));let witness=null;
 if(solver.status==='sat'){
  const ids=solver.selectedPackets,world=new Map(Object.entries(solver.choices)),{rules}=u;assert.ok(rules.selectedWorld(ids,world));const root=u.roots.find(p=>ids.includes(p));assert.notEqual(root,undefined);assert.equal(u.roots.filter(p=>ids.includes(p)).length,1);
  const inspection=rules.inspectWorld(ids,world);assert.equal(inspection.certifiedExit,true);assert.deepEqual(inspection.counts,{proton:7,neutron:7,electron:7});assert.equal(inspection.pendingContacts.length,0);
  const selected=new Set(ids),reached=new Set([root]),word=[],prefixes=[[root]],allowed=u.operations.filter(o=>o.requirements.every(([k,d])=>world.get(k)===d));
  for(let changed=true;changed;){changed=false;for(const op of allowed)if(reached.has(op.source)&&selected.has(op.target)&&!reached.has(op.target)){
   rules.geometry.setWorld(world,0);rules.validateTransfer(op);reached.add(op.target);word.push(op.id);const prefix=[...reached].sort((a,b)=>a-b);assert.equal(rules.describe(prefix).valid,true);prefixes.push(prefix);changed=true;
  }}assert.equal(reached.size,selected.size);assert.equal(rules.inspectWorld([...reached],world).certifiedExit,true);
  const bodies=[...rules.describe(ids).bodies].map(([cell,species])=>({cell,species,key:rules.geometry.cells[cell].key,vertices:rules.geometry.cells[cell].vertices.map(p=>rules.geometry.points.get(p)),owner:rules.geometry.cells[cell].owner}));
  witness={selectedPackets:ids,choices:solver.choices,root,inspection,word,prefixes,grade:Math.max(...ids.map(p=>rules.packets[p].origin)),packets:ids.map(p=>rules.packets[p]),charts:[...new Set(ids.map(p=>rules.packets[p].chart))].map(i=>rules.charts[i]),operations:allowed.filter(o=>selected.has(o.source)&&selected.has(o.target)),bodies,globalFieldSewingAsserted:false};
 }
 const row={maxOrigin,universeComplete:true,universePackets:u.packets.length,universeOperations:u.operations.length,choiceItems:input.items.length,inputSha256:hash(await readFile(inputPath)),solver,witness};await writeFile(out+`/D${maxOrigin}-verification.json`,JSON.stringify(row,null,2)+'\n');rows.push({...row,witness:witness?`D${maxOrigin}-verification.json`:null});console.log(JSON.stringify({maxOrigin,status:solver.status,witness:witness?{counts:witness.inspection.counts,grade:witness.grade,records:witness.selectedPackets.length}:null}));if(witness||solver.status==='unknown')break;
}
for(const f of files)assert.equal(hash(await readFile(new URL(f,import.meta.url))),sourceHashes[f]);await writeFile(out+'/verification.json',JSON.stringify({status:rows.some(r=>r.witness)?'mixed-diagonal-neutral-N14-local-reference-found':rows.some(r=>!r.universeComplete||r.solver?.status==='unknown')?'mixed-diagonal-search-incomplete':'no-neutral-reference-within-tested-origin-bounds',sourceHashes,rows,scope:'Independent diagonal variables for each octahedron, globally consistent across reference and occupied geometry. Original source packet operations, context-role/contact guards, fixed root, exact 7/7/7 body counts and selected-record exit certificate; no global field sewing, physical binding/stability, whole-octahedron particles or viewer admission. Packet cap 5000, operation cap 50000, local evaluation cap 100000, solver timeout 120s, overall solver process limit 600s including constraint construction. Finite negative only at completed bounds.'},null,2)+'\n');
