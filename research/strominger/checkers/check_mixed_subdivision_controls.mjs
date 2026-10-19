// Exhaust all 3^3 small worlds, comparing SAT with explicit source execution.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {spawnSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {mixedUniverse,buildMixedInput} from './mixed-subdivision-model.mjs';
const out='research/strominger/results/mixed-subdivision-n14',u=mixedUniverse({maxOrigin:1}),input=buildMixedInput(u,{proton:7,neutron:7,electron:7}),{rules}=u;
assert.equal(u.complete,true);assert.equal(input.items.length,3);
const worlds=[];function assign(i,entries=[]){if(i===input.items.length){worlds.push(new Map(entries));return;}for(let d=0;d<3;d++)assign(i+1,[...entries,[input.items[i],d]]);}assign(0);
const queries=[],expected=[],summary=[];
for(const [worldIndex,world] of worlds.entries()){
 const roots=u.roots.filter(p=>rules.requirements(p).every(([k,d])=>world.get(k)===d));assert.equal(roots.length,1);
 rules.operationCache.clear();const nodes=[[roots[0]]],seen=new Set([String(roots[0])]);
 for(let cursor=0;cursor<nodes.length;cursor++){
  const ids=nodes[cursor];for(const p of ids){rules.geometry.setWorld(world,0);for(const i of rules.outgoing(p)){
   const op=rules.operations[i];if(rules.packets[op.target].origin>1||ids.includes(op.target))continue;assert.ok(u.packets.includes(op.target));assert.ok(rules.requirements(op.target).every(([k,d])=>world.get(k)===d));
   const next=[...ids,op.target].sort((a,b)=>a-b),key=next.join(',');if(seen.has(key))continue;if(!rules.describe(next).valid)continue;seen.add(key);nodes.push(next);assert.ok(nodes.length<5000,'Explicit small-world cap');
  }}
 }
 const profiles=new Map();for(const ids of nodes){const inspection=rules.inspectWorld(ids,world);assert.equal(inspection.valid,true);const key=JSON.stringify(inspection.counts);if(!profiles.has(key))profiles.set(key,{counts:inspection.counts,certified:[]});if(inspection.certifiedExit)profiles.get(key).certified.push(ids);}
 for(const p of [...profiles.values(),{counts:{proton:7,neutron:7,electron:7},certified:[]}]){queries.push({target:p.counts,fixedChoices:Object.fromEntries(world)});expected.push({worldIndex,counts:p.counts,certified:p.certified});}
 summary.push({worldIndex,choices:Object.fromEntries(world),explicitConfigurations:nodes.length,compositionProfiles:profiles.size});
}
await mkdir(out,{recursive:true});await writeFile(out+'/controls-input.json',JSON.stringify({...input,queries})+'\n');
const child=spawnSync(process.platform==='win32'?'uv.exe':'uv',['run','--with','z3-solver','python','research/strominger/checkers/solve_mixed_n14.py',out+'/controls-input.json',out+'/controls-solver.json'],{encoding:'utf8',timeout:240000});assert.equal(child.status,0,child.stderr??String(child.error));const solved=JSON.parse(await readFile(out+'/controls-solver.json'));assert.equal(solved.answers.length,expected.length);
for(const [i,a] of solved.answers.entries()){
 const e=expected[i];assert.equal(a.status,e.certified.length?'sat':'unsat',JSON.stringify({i,worldIndex:e.worldIndex,counts:e.counts}));
 if(a.status==='sat'){assert.ok(e.certified.some(ids=>ids.join(',')===[...a.selectedPackets].sort((a,b)=>a-b).join(',')));assert.equal(rules.inspectWorld(a.selectedPackets,worlds[e.worldIndex]).certifiedExit,true);}
}
// Hostile: records requiring two diagonals for the same octahedron cannot
// coexist, even if each is valid on its own.
assert.equal(rules.describe([u.roots[0],u.roots[1]]).reason,'global-diagonal-conflict');
const hashes={};for(const f of ['./mixed-subdivision-model.mjs','./solve_mixed_n14.py','./check_mixed_subdivision_controls.mjs','../../nima/generative-phase-assembly.mjs'])hashes[f]=createHash('sha256').update(await readFile(new URL(f,import.meta.url))).digest('hex');
await writeFile(out+'/controls-verification.json',JSON.stringify({status:'all-small-worlds-crosschecked',hashes,maxOrigin:1,worlds:worlds.length,queries:expected.length,summary,hostile:'same-item-different-diagonals-rejected',scope:'All 27 assignments to three relevant small-universe item choices; explicit source-operation enumeration and SAT agree on all emitted composition profiles plus impossible target. No high-origin completeness or physical sewing inferred.'},null,2)+'\n');console.log(JSON.stringify({status:'all-small-worlds-crosschecked',worlds:worlds.length,queries:expected.length,configurations:summary.map(s=>s.explicitConfigurations)},null,2));
