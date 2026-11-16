// Read-only replay of the saved finite-reader Ne-22 candidate.
// Writes only JSON to stdout; never updates native inputs, drawings or receipts.
import assert from 'node:assert/strict';
import {open,realpath} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';

const root=fileURLToPath(new URL('../../../',import.meta.url));
const nativeDirectory=path.join(root,'research/strominger/results/reference-ne22-search');
const checkerDirectory=path.join(root,'research/strominger/checkers');
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
const bounded=async file=>{
  const handle=await open(file,'r'),buffer=Buffer.alloc(4*1024*1024+1);
  let used=0;
  try {
    while(used<buffer.length){
      const {bytesRead}=await handle.read(buffer,used,buffer.length-used,used);
      if(!bytesRead)break;
      used+=bytesRead;
    }
  } finally { await handle.close(); }
  assert.ok(used<=4*1024*1024,'Artifact size limit');
  return buffer.subarray(0,used);
};
let stage='source-pins';
try {
  assert.ok(process.argv.length<=3,'At most one witness path is allowed');
  const manifestRaw=await bounded(path.join(nativeDirectory,'verification.json'));
  const manifest=JSON.parse(manifestRaw);
  assert.deepEqual(manifest.target,{proton:10,neutron:12,electron:10});
  const requiredPins=['./search_reference_ne22.mjs','./solve_reference_n14.py',
    '../../nima/generative-phase-assembly.mjs','../../nima/origin-bounded-assemblies.mjs',
    ...['window-construction-model.mjs','lattice-items.mjs','simplex-components.mjs','carrier.mjs',
        'phase-advance-model.mjs','phase-discipline-model.mjs','deuterium-tunnel-model.mjs']
      .map(name=>'../demos/particle-overlap-tetrahedron/'+name)];
  assert.deepEqual(Object.keys(manifest.sourceHashes).sort(),requiredPins.sort(),'Declared native dependency set changed');
  const sourceHashes={};
  for(const [relative,pin] of Object.entries(manifest.sourceHashes)){
    assert.match(pin,/^[0-9a-f]{64}$/);
    const file=await realpath(path.resolve(checkerDirectory,relative));
    assert.ok(!path.relative(root,file).startsWith('..')&&!path.isAbsolute(path.relative(root,file)),'Dependency outside repository');
    const digest=hash(await bounded(file));
    assert.equal(digest,pin,`Changed native dependency: ${relative}`);
    sourceHashes[relative]=digest;
  }
  // Import only this fixed implementation, never a module named by input data.
  const {phaseUniverse}=await import('../../nima/origin-bounded-assemblies.mjs');
  stage='input-pin';
  const witnessRaw=await bounded(process.argv[2]||path.join(nativeDirectory,'D4-verification.json'));
  const saved=JSON.parse(witnessRaw),w=saved.witness;
  assert.equal(saved.maxOrigin,4,'This operation supports the saved D4 candidate only');
  const input=await bounded(path.join(nativeDirectory,'D4-input.json'));
  assert.equal(hash(input),saved.inputSha256);
  stage='constructor-replay';
  const u=phaseUniverse({maxOrigin:4,maxPackets:5000});
  assert.equal(u.complete,true);
  const {rules}=u,selected=new Set(w.selectedPackets);
  assert.equal(selected.size,w.selectedPackets.length);
  assert.ok(selected.has(rules.root));
  assert.ok([...selected].every(p=>u.packets.includes(p)));
  const order=w.packets.map(p=>p.id);
  assert.deepEqual([...order].sort((a,b)=>a-b),w.selectedPackets);
  assert.deepEqual(w.packets,order.map(p=>rules.packets[p]));
  assert.deepEqual(w.charts,[...new Set(order.map(p=>rules.packets[p].chart))].map(c=>rules.charts[c]));
  const reached=new Set([rules.root]);
  assert.deepEqual(w.prefixes[0],[rules.root]);
  for(const [index,id] of w.word.entries()){
    assert.ok(u.operations.includes(id));
    const op=rules.operations[id];
    assert.ok(reached.has(op.source)&&selected.has(op.target)&&!reached.has(op.target));
    rules.validateTransfer(op);reached.add(op.target);
    const prefix=[...reached].sort((a,b)=>a-b);
    assert.deepEqual(prefix,w.prefixes[index+1]);
    assert.equal(rules.describe(prefix).valid,true);
  }
  assert.deepEqual([...reached].sort((a,b)=>a-b),w.selectedPackets);
  assert.equal(w.prefixes.length,w.word.length+1);
  const description=rules.describe(order),inspection=rules.inspect(order);
  assert.equal(description.valid,true);
  assert.deepEqual(inspection,w.inspection);
  assert.deepEqual(inspection.counts,manifest.target);
  assert.equal(inspection.certifiedExit,true);
  assert.equal(inspection.pendingContacts.length,0);
  assert.equal(inspection.allPacketsCanReachExit,true);
  const operations=u.operations.map(id=>rules.operations[id]).filter(o=>selected.has(o.source)&&selected.has(o.target));
  assert.deepEqual(operations,w.operations);
  for(const op of operations)rules.validateTransfer(op);
  const bodies=[...description.bodies].map(([cell,species])=>({cell,species,key:rules.geometry.cells[cell].key,vertices:rules.geometry.cells[cell].vertices.map(v=>rules.geometry.points.get(v))}));
  assert.deepEqual(bodies,w.bodies);
  assert.equal(bodies.length,32);
  stage='independent-local-checks';
  let contacts=0;
  for(let a=0;a<bodies.length;a++)for(let b=a+1;b<bodies.length;b++){
    const ca=bodies[a].cell,cb=bodies[b].cell;
    const face=rules.geometry.cells[ca].vertices.filter(v=>rules.geometry.cells[cb].vertices.includes(v));
    if(face.length!==3)continue;
    assert.ok(operations.some(o=>{
      const x=rules.charts[rules.packets[o.source].chart].cell,y=rules.charts[rules.packets[o.target].chart].cell;
      return x===ca&&y===cb||x===cb&&y===ca;
    }),'Unwitnessed occupied face');
    contacts++;
  }
  assert.equal(contacts,description.contacts.length);
  const exits=w.selectedPackets.filter(p=>rules.charts[rules.packets[p].chart].species==='electron');
  const canExit=new Set(exits),queue=[...exits];
  for(let i=0;i<queue.length;i++)for(const op of operations)if(op.target===queue[i]&&!canExit.has(op.source)){
    canExit.add(op.source);queue.push(op.source);
  }
  assert.equal(canExit.size,selected.size);
  console.log(JSON.stringify({status:'native-generator-replayed',nodeVersion:process.version,manifestSha256:hash(manifestRaw),witnessSha256:hash(witnessRaw),inputSha256:hash(input),sourceHashes,
    checkerSha256:hash(await bounded(fileURLToPath(import.meta.url))),counts:inspection.counts,packets:selected.size,operations:operations.length,constructionSteps:w.word.length,contacts,
    scope:'Pinned saved Ne-22 finite-reader constructor replay plus local contact/exit checks; shares the original generator. Not a Turtle import, Ne-20 construction, physical certification or independent model.'}));
}catch(error){
  console.log(JSON.stringify({status:'rejected',stage,error:String(error.message).slice(0,2000)}));
  process.exitCode=1;
}
