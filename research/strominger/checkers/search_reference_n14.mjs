// Targeted finite-origin search using unchanged prior construction rules.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
const target={proton:7,neutron:7,electron:7},out='research/strominger/results/reference-n14-search',hash=b=>createHash('sha256').update(b).digest('hex');
const files=['./search_reference_n14.mjs','./solve_reference_n14.py','../../nima/generative-phase-assembly.mjs','../../nima/origin-bounded-assemblies.mjs',...['window-construction-model.mjs','lattice-items.mjs','simplex-components.mjs','carrier.mjs','phase-advance-model.mjs','phase-discipline-model.mjs','deuterium-tunnel-model.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f)],sourceHashes={};for(const f of files)sourceHashes[f]=hash(await readFile(new URL(f,import.meta.url)));
await mkdir(out,{recursive:true});const rows=[];
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
 console.log(JSON.stringify({maxOrigin,packets:packets.length,conflicts:conflicts.length,potentialBodies:bodies.length,stage:'solving'}));
 const process=spawnSync('uv',['run','--with','z3-solver','python','research/strominger/checkers/solve_reference_n14.py',inputPath,outputPath],{encoding:'utf8',timeout:150000,shell:globalThis.process.platform==='win32'});
 if(process.status!==0)throw Error('Solver process failed: '+process.stderr+' '+process.error);
 const solver=JSON.parse(await readFile(outputPath,'utf8'));let witness=null;
 if(solver.status==='sat'){
  const selected=new Set(solver.selectedPackets);assert.ok(selected.has(rules.root));assert.ok([...selected].every(p=>packets.includes(p)));
  const inspection=rules.inspect([...selected]);assert.equal(inspection.valid,true);assert.deepEqual(inspection.counts,target);assert.equal(inspection.certifiedExit,true);assert.equal(inspection.pendingContacts.length,0);assert.equal(inspection.allPacketsCanReachExit,true);
  // Reconstruct an actual compatible construction word from the root, then
  // check every prefix using the unchanged whole-state guards.
  const reached=new Set([rules.root]),word=[],prefixes=[[rules.root]];
  for(let changed=true;changed;){changed=false;for(const i of operations){const op=rules.operations[i];if(reached.has(op.source)&&selected.has(op.target)&&!reached.has(op.target)){rules.validateTransfer(op);reached.add(op.target);word.push(i);const ids=[...reached].sort((a,b)=>a-b);assert.equal(rules.describe(ids).valid,true);prefixes.push(ids);changed=true;}}}
  assert.equal(reached.size,selected.size);assert.equal(rules.inspect([...reached]).certifiedExit,true);
  const missingOccupiedReferences=[];for(const id of selected){const c=rules.charts[rules.packets[id].chart];if(c.species!=='neutron')continue;const reference=rules.geometry.neighbor(c.cell,['M0','C1','M1'].map(k=>c.aliases[k]));if(!rules.describe([...selected]).bodies.has(reference))missingOccupiedReferences.push({packet:id,neutronCell:c.cell,referenceCell:reference});}
  const selectedBodies=[...rules.describe([...selected]).bodies].map(([cell,species])=>({cell,species,key:rules.geometry.cells[cell].key,vertices:rules.geometry.cells[cell].vertices.map(v=>rules.geometry.points.get(v))}));
  witness={selectedPackets:[...selected].sort((a,b)=>a-b),inspection,grade:Math.max(...[...selected].map(i=>rules.packets[i].origin)),word,prefixes,missingOccupiedReferences,bodies:selectedBodies,packets:[...selected].map(i=>rules.packets[i]),charts:[...new Set([...selected].map(i=>rules.packets[i].chart))].map(i=>rules.charts[i]),operations:operations.filter(i=>selected.has(rules.operations[i].source)&&selected.has(rules.operations[i].target)).map(i=>rules.operations[i]),globalSewingAsserted:false};
 }
 const row={maxOrigin,packetUniverseComplete:true,universePackets:packets.length,universeOperations:operations.length,inputSha256:hash(await readFile(inputPath)),solver,witness};rows.push(row);await writeFile(out+`/D${maxOrigin}-verification.json`,JSON.stringify(row,null,2)+'\n');console.log(JSON.stringify({maxOrigin,status:solver.status,witness:witness?{grade:witness.grade,bodies:witness.bodies.length,records:witness.selectedPackets.length,wordLength:wordLength(witness),missingOccupiedReferenceRecords:witness.missingOccupiedReferences.length}:null}));
 if(witness)break;
}
function wordLength(w){return w.word.length;}
for(const f of files)assert.equal(hash(await readFile(new URL(f,import.meta.url))),sourceHashes[f]);
await writeFile(out+'/verification.json',JSON.stringify({status:rows.some(r=>r.witness)?'neutral-N14-local-reference-found':'no-witness-within-tested-bounds',sourceHashes,target,rows:rows.map(({witness,...r})=>({...r,witnessFile:witness?`D${r.maxOrigin}-verification.json`:null})),scope:'Unchanged prior seed generator: reference-only P allowed, regular/split E, fixed root and subdivision, explicit origin caps 3..10 stopping at first SAT. Pair guards, actual contact witnesses, rooted construction and E-exit reachability; SAT witnesses replayed by original rules. No complete global field sewing, whole-octahedron particle law, physical binding/stability or synthesis dynamics. UNSAT only within stated finite origin bound; unknown is not a negative. Production/viewer unchanged.'},null,2)+'\n');
