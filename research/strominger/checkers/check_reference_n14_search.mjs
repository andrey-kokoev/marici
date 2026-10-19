// Cross-check targeted SAT encoding against complete small prior enumeration.
import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {enumerateOriginAssemblies,phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
const hash=b=>createHash('sha256').update(b).digest('hex'),out='research/strominger/results/reference-n14-search',main=JSON.parse(await readFile(out+'/verification.json'));
for(const [f,h] of Object.entries(main.sourceHashes))assert.equal(hash(await readFile(new URL(f,import.meta.url))),h,'Stale source receipt: '+f);
for(const row of main.rows){const input=await readFile(out+`/D${row.maxOrigin}-input.json`);assert.equal(hash(input),row.inputSha256);assert.equal(row.packetUniverseComplete,true);assert.ok(['sat','unsat'].includes(row.solver.status),'Incomplete bounded solver result');}
const run=enumerateOriginAssemblies({maxOrigin:1,maxConfigurations:1000});assert.equal(run.complete,true);assert.ok(run.nodes.length>0);
const universe=phaseUniverse({maxOrigin:1}),allowed=new Set(universe.packets),large=JSON.parse(await readFile(out+'/D3-input.json')),bodies=[],remap=new Map();
large.bodies.forEach((b,i)=>{const packets=b.packets.filter(p=>allowed.has(p));if(packets.length){remap.set(i,bodies.length);bodies.push({...b,packets});}});
const projected={...large,maxOrigin:1,packets:universe.packets,operations:large.operations.filter(o=>allowed.has(o.source)&&allowed.has(o.target)),conflicts:large.conflicts.filter(([a,b])=>allowed.has(a)&&allowed.has(b)),bodies,contacts:large.contacts.filter(c=>c.bodies.every(b=>remap.has(b))).map(c=>({bodies:c.bodies.map(i=>remap.get(i)),links:c.links.filter(([a,b])=>allowed.has(a)&&allowed.has(b))})),exits:large.exits.filter(p=>allowed.has(p))};
assert.deepEqual(projected.operations,universe.operations.map(i=>universe.rules.operations[i]));
// Add impossible quotas as negative controls, not just satisfiable profiles.
const profiles=[...run.profiles.map(p=>({counts:p.counts,expected:p.selectedRecordExitCertificates>0})),{counts:{proton:7,neutron:7,electron:7},expected:false},{counts:{proton:1,neutron:0,electron:0},expected:false}],controls=[];
for(const [index,p] of profiles.entries()){
 const inputPath=out+`/control-${index}-input.json`,outputPath=out+`/control-${index}-solver.json`;await writeFile(inputPath,JSON.stringify({...projected,target:p.counts})+'\n');
 const child=spawnSync(globalThis.process.platform==='win32'?'uv.exe':'uv',['run','--with','z3-solver','python','research/strominger/checkers/solve_reference_n14.py',inputPath,outputPath],{encoding:'utf8',timeout:150000});assert.equal(child.status,0,child.stderr??String(child.error));
 const solved=JSON.parse(await readFile(outputPath));assert.equal(solved.status,p.expected?'sat':'unsat');
 if(p.expected){const selected=solved.selectedPackets,i=universe.rules.inspect(selected);assert.equal(i.certifiedExit,true);assert.deepEqual(i.counts,p.counts);assert.ok(run.nodes.some(n=>JSON.stringify([...n.packets].sort((a,b)=>a-b))===JSON.stringify([...selected].sort((a,b)=>a-b))));}
 controls.push({...p,status:solved.status});
}
const result={status:'small-exhaustive-enumeration-crosscheck-passed',explicitConfigurations:run.nodes.length,maxOrigin:1,controls,checkedN14Bounds:main.rows.map(r=>({maxOrigin:r.maxOrigin,status:r.solver.status,packetUniverseComplete:r.packetUniverseComplete})),scope:'All D1 composition profiles and impossible quotas compared against complete unchanged enumerator; SAT models replayed and located in its configuration list. Large-bound negatives remain solver results for finite supplied universes, not independent formal UNSAT certificates or an unbounded theorem.'};
await writeFile(out+'/crosscheck.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
