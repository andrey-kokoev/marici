// Neutral F-19 baseline: unchanged fixed-subdivision reference grammar.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
const target={proton:9,neutron:10,electron:9},out='research/strominger/results/reference-f19-search',hash=b=>createHash('sha256').update(b).digest('hex');
const files=['./search_reference_f19.mjs','./solve_reference_n14.py','../../nima/generative-phase-assembly.mjs','../../nima/origin-bounded-assemblies.mjs',...['window-construction-model.mjs','lattice-items.mjs','simplex-components.mjs','carrier.mjs','phase-advance-model.mjs','phase-discipline-model.mjs','deuterium-tunnel-model.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f)],sourceHashes={};for(const f of files)sourceHashes[f]=hash(await readFile(new URL(f,import.meta.url)));
await mkdir(out,{recursive:true});const rows=[];
async function summary(){await writeFile(out+'/verification.json',JSON.stringify({status:rows.some(r=>r.witnessFile)?'neutral-F19-local-reference-found':rows.some(r=>r.solver.status!=='unsat')?'search-incomplete':'no-witness-within-completed-bounds',target,sourceHashes,rows,scope:'Fixed canonical root and original subdivision. Reference-only P and regular/split E allowed. Exact 9P/10N/9e, pair guards, contact witnesses, rooted construction and E-exit reachability. Origins 3..10 stopping on SAT or unknown. Packet cap 5000; solver 120s; process 600s including setup. No global field sewing, binding, physical stability or production/viewer admission.'},null,2)+'\n');}
for(const maxOrigin of [3,4,5,6,7,8,9,10]){
 const universe=phaseUniverse({maxOrigin,maxPackets:5000});assert.equal(universe.complete,true,'Incomplete packet universe');const {rules,packets,operations}=universe;
 const conflicts=[];for(let a=0;a<packets.length;a++)for(let b=a+1;b<packets.length;b++)if(!rules.describe([packets[a],packets[b]]).valid)conflicts.push([packets[a],packets[b]]);
 const bodies=[],which=new Map();for(const id of packets){const c=rules.charts[rules.packets[id].chart],k=c.cell+':'+c.species;if(!which.has(k)){which.set(k,bodies.length);bodies.push({cell:c.cell,species:c.species,packets:[]});}bodies[which.get(k)].packets.push(id);}
 const contacts=[];for(let a=0;a<bodies.length;a++)for(let b=a+1;b<bodies.length;b++){
  const u=bodies[a],v=bodies[b];if(u.cell===v.cell||rules.geometry.cells[u.cell].vertices.filter(p=>rules.geometry.cells[v.cell].vertices.includes(p)).length!==3)continue;
  const links=operations.map(i=>rules.operations[i]).filter(op=>u.packets.includes(op.source)&&v.packets.includes(op.target)||v.packets.includes(op.source)&&u.packets.includes(op.target)).map(op=>[op.source,op.target]);contacts.push({bodies:[a,b],links});
 }
 const input={maxOrigin,target,root:rules.root,packets,conflicts,operations:operations.map(i=>rules.operations[i]),bodies,contacts,exits:packets.filter(id=>rules.charts[rules.packets[id].chart].species==='electron')};
 const inputPath=out+`/D${maxOrigin}-input.json`,outputPath=out+`/D${maxOrigin}-solver.json`;await writeFile(inputPath,JSON.stringify(input)+'\n');
 console.log(JSON.stringify({maxOrigin,packets:packets.length,stage:'solving'}));
 const child=spawnSync(process.platform==='win32'?'uv.exe':'uv',['run','--with','z3-solver==5.3.1','python','research/strominger/checkers/solve_reference_n14.py',inputPath,outputPath],{encoding:'utf8',timeout:600000});
 const solver=child.status===0?JSON.parse(await readFile(outputPath,'utf8')):{status:'unknown',reason:'solver-process-did-not-complete',processStatus:child.status,signal:child.signal,error:child.error?.message??null,stderr:child.stderr};let witness=null;
 if(solver.status==='sat'){
  const selected=new Set(solver.selectedPackets);assert.ok(selected.has(rules.root));assert.ok([...selected].every(p=>packets.includes(p)));
  const inspection=rules.inspect([...selected]);assert.equal(inspection.valid,true);assert.deepEqual(inspection.counts,target);assert.equal(inspection.certifiedExit,true);assert.equal(inspection.pendingContacts.length,0);assert.equal(inspection.allPacketsCanReachExit,true);
  const reached=new Set([rules.root]),word=[],prefixes=[[rules.root]];
  for(let changed=true;changed;){changed=false;for(const i of operations){const op=rules.operations[i];if(reached.has(op.source)&&selected.has(op.target)&&!reached.has(op.target)){rules.validateTransfer(op);reached.add(op.target);word.push(i);const ids=[...reached].sort((a,b)=>a-b);assert.equal(rules.describe(ids).valid,true);prefixes.push(ids);changed=true;}}}
  assert.equal(reached.size,selected.size);assert.equal(rules.inspect([...reached]).certifiedExit,true);
  const selectedBodies=[...rules.describe([...selected]).bodies].map(([cell,species])=>({cell,species,key:rules.geometry.cells[cell].key,vertices:rules.geometry.cells[cell].vertices.map(v=>rules.geometry.points.get(v))}));
  witness={selectedPackets:[...selected].sort((a,b)=>a-b),inspection,grade:Math.max(...[...selected].map(i=>rules.packets[i].origin)),word,prefixes,bodies:selectedBodies,packets:[...selected].map(i=>rules.packets[i]),charts:[...new Set([...selected].map(i=>rules.packets[i].chart))].map(i=>rules.charts[i]),operations:operations.filter(i=>selected.has(rules.operations[i].source)&&selected.has(rules.operations[i].target)).map(i=>rules.operations[i]),globalSewingAsserted:false};
 }
 const row={maxOrigin,packetUniverseComplete:true,universePackets:packets.length,universeOperations:operations.length,inputSha256:hash(await readFile(inputPath)),solver};await writeFile(out+`/D${maxOrigin}-verification.json`,JSON.stringify({...row,witness},null,2)+'\n');rows.push({...row,witnessFile:witness?`D${maxOrigin}-verification.json`:null});await summary();console.log(JSON.stringify({maxOrigin,status:solver.status,witness:witness?{grade:witness.grade,bodies:witness.bodies.length,records:witness.selectedPackets.length}:null}));
 if(witness||solver.status!=='unsat')break;
}
for(const f of files)assert.equal(hash(await readFile(new URL(f,import.meta.url))),sourceHashes[f]);await summary();
