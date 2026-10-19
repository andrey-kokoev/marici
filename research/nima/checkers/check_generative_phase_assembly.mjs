import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir,stat} from 'node:fs/promises';
import {createWriteStream,createReadStream} from 'node:fs';
import {createHash} from 'node:crypto';
import {createGzip,createGunzip} from 'node:zlib';
import {pipeline} from 'node:stream/promises';
import {once} from 'node:events';
import {createInterface} from 'node:readline';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const root=fileURLToPath(new URL('../../../',import.meta.url)),out=path.join(root,'research/nima/results/generative-phase-assembly');
const sourceBase='research/strominger/demos/particle-overlap-tetrahedron/';
const dependencies=['lattice-items','simplex-components','carrier','model','window-construction-model','phase-advance-model','phase-discipline-model','deuterium-tunnel-model','fiber-coverage-model'].map(n=>sourceBase+n+'.mjs');
const own=['research/nima/generative-phase-assembly.mjs','research/nima/inputs/generative-phase-assembly-v1.json','research/nima/checkers/check_generative_phase_assembly.mjs','research/nima/demos/generative-phase-assembly.template.html'];
const sha=b=>createHash('sha256').update(b).digest('hex');
async function fingerprint(){return Object.fromEntries(await Promise.all([...dependencies,...own].map(async p=>[p,sha(await readFile(path.join(root,p)))])));}
const hashes=await fingerprint(),contract=JSON.parse(await readFile(path.join(root,own[1]),'utf8'));
const {GenerativeAssemblyRules,enumerateAssemblies,applyPhasePermutation}=await import('../generative-phase-assembly.mjs');
const {createWindowConstruction,windowProtocol}=await import('../../strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs');
const generator=await readFile(path.join(root,own[0]),'utf8');
assert.doesNotMatch(generator,/selectPhaseAssembly|searchTypedAssemblies|assemblyDomain|phase-assembly-model|simplex-model|helium|lithium|lead208/i,'Preset target/layout entered the generator');
const r=enumerateAssemblies({maxTransitions:contract.maxSourceTransitions,maxStates:contract.maxConfigurations});
assert.equal(r.complete,true,'Nine-operation search did not finish; partial output cannot pass');
assert.equal(r.stop,null);
assert.deepEqual(r.summary.minimalStageCounts,[1,2,6,21,82,333,1381,5804,24593,104756]);
assert.equal(r.summary.configurations,136979);
const rules=r.rules,sets=r.nodes.map(n=>new Set(n.packets)),byKey=new Map(r.nodes.map(n=>[n.packets.join(','),n.id])),outgoing=r.nodes.map(()=>new Map());
let edgeChecks=0;
for(const e of r.edges){
 const op=r.operations[e.operation],parent=r.nodes[e.from],child=r.nodes[e.to];
 assert.ok(sets[e.from].has(op.source));assert.ok(sets[e.to].has(op.target));
 const expected=[...new Set([...parent.packets,op.target])].sort((a,b)=>a-b);
 assert.deepEqual(child.packets,expected);assert.ok(parent.minTransitions<contract.maxSourceTransitions);
 assert.equal(outgoing[e.from].has(e.operation),false);outgoing[e.from].set(e.operation,e.to);edgeChecks++;
}
// Full outgoing-fanout audit independent of the BFS visited-node implementation.
for(const node of r.nodes){
 assert.equal(node.minTransitions,node.packets.length-1);
 if(node.id){const op=r.operations[node.operation];assert.ok(sets[node.parent].has(op.source));assert.ok(!sets[node.parent].has(op.target));assert.equal(outgoing[node.parent].get(node.operation),node.id);}
 if(node.minTransitions===contract.maxSourceTransitions)continue;
 const expected=new Map();
 for(const id of node.packets)for(const index of rules.outgoing(id)){
  const op=rules.operations[index],ids=[...new Set([...node.packets,op.target])].sort((a,b)=>a-b);
  if(!rules.describe(ids).valid)continue;
  const target=byKey.get(ids.join(','));assert.notEqual(target,undefined,'Compatible generated continuation missing');expected.set(index,target);
 }
 assert.deepEqual([...outgoing[node.id]].sort(([a],[b])=>a-b),[...expected].sort(([a],[b])=>a-b));
}
// Direct, unmerged short-word enumeration checks order retention and configuration congruence.
function signature(engine,ids){return ids.map(id=>{const p=engine.packets[id],c=engine.charts[p.chart];return JSON.stringify([engine.geometry.cells[c.cell].key,c.species,c.aliases,p.origin,p.permutation]);}).sort().join('|');}
const naive=new GenerativeAssemblyRules(),wordSignatures=new Set();let shortWords=0;
function visit(ids,depth){shortWords++;wordSignatures.add(signature(naive,ids));if(depth===3)return;
 for(const id of ids)for(const index of naive.outgoing(id)){const op=naive.operations[index],next=[...new Set([...ids,op.target])].sort((a,b)=>a-b);if(naive.describe(next).valid)visit(next,depth+1);}}
visit([naive.root],0);
assert.deepEqual([...wordSignatures].sort(),r.nodes.filter(n=>n.minTransitions<=3).map(n=>signature(rules,n.packets)).sort());
let negativeControls=0;
const partial=enumerateAssemblies({maxTransitions:9,maxStates:5,inspect:false});assert.equal(partial.complete,false);assert.equal(partial.stop.reason,'explicit-state-resource-limit');negativeControls++;
assert.throws(()=>enumerateAssemblies({maxStates:0}));negativeControls++;
const audit=new GenerativeAssemblyRules(),rootPacket=audit.packets[audit.root],rootChart=audit.charts[rootPacket.chart];
const different=audit.completeP(rootChart.cell,{C0:rootChart.aliases.M0,M0:rootChart.aliases.C0,C1:rootChart.aliases.C1,M1:rootChart.aliases.M1});
const badRoles=audit.packet(different,0,[0,1,2,3,4]);assert.equal(audit.describe([audit.root,badRoles]).reason,'global-CM-role-conflict');negativeControls++;
const native=new GenerativeAssemblyRules(),pn=native.outgoing(native.root).map(i=>native.operations[i]).find(e=>e.kind==='PN');
const branch=native.outgoing(pn.target).map(i=>native.operations[i]),ne=branch.find(e=>e.kind==='NE'),nn=branch.find(e=>e.kind==='NN-phase-advance');
assert.ok(ne&&nn);assert.equal(native.describe([native.root,pn.target,ne.target,nn.target]).reason,'occupied-cell-species-conflict');negativeControls++;
for(const change of [op=>op.phaseDelta++,op=>op.permutation.reverse(),op=>op.face.reverse()]){
 const bad=structuredClone(pn);change(bad);
 if(JSON.stringify(bad.face)===JSON.stringify([...pn.face].reverse())&&bad.phaseDelta===pn.phaseDelta&&JSON.stringify(bad.permutation)===JSON.stringify(pn.permutation)){
  // A geometric face is unordered; reversing its storage order must NOT change admission.
  assert.equal(native.validateTransfer(bad),true);
 }else {assert.throws(()=>native.validateTransfer(bad));negativeControls++;}
}
const badTarget=structuredClone(native.packets[pn.target]);badTarget.permutation.reverse();assert.throws(()=>native.validateTransfer(pn,native.packets[pn.source],badTarget));negativeControls++;
const badOrigin=structuredClone(native.packets[pn.target]);badOrigin.origin++;assert.throws(()=>native.validateTransfer(pn,native.packets[pn.source],badOrigin));negativeControls++;
const nativeConstruction=createWindowConstruction();nativeConstruction.step();const original=nativeConstruction.step();
const pneIds=[native.root,pn.target,ne.target],pneKeys=pneIds.map(id=>native.geometry.cells[native.charts[native.packets[id].chart].cell].key);
assert.deepEqual(pneKeys,original.items.map(i=>i.key),'Seed-generated PN/E no longer reproduces the supplied primitive attachment');
function* permutations(a){if(!a.length){yield [];return;}for(let i=0;i<a.length;i++)for(const rest of permutations(a.filter((_,j)=>j!==i)))yield [a[i],...rest];}
let seedFramesChecked=0,regularElectronTargets=0;
const seedVertices=native.geometry.cells[rootChart.cell].vertices;
for(const order of permutations([0,1,2,3])){
 const bindings=Object.fromEntries(windowProtocol[0].nodes.map((name,i)=>[name,seedVertices[order[i]]])),g=new GenerativeAssemblyRules({seedBindings:bindings});
 const p=g.outgoing(g.root).map(i=>g.operations[i]).find(e=>e.kind==='PN'),e=g.outgoing(p.target).map(i=>g.operations[i]).find(e=>e.kind==='NE');
 const original=createWindowConstruction({bindings:Object.fromEntries(Object.entries(bindings).map(([n,v])=>[n,v.split(',').map(Number)]))});original.step();const end=original.step();
 assert.equal(end.status,'complete');assert.ok(e,'A common-protocol NE continuation was silently pruned');
 const ids=[g.root,p.target,e.target];assert.equal(g.describe(ids).valid,true);
 assert.deepEqual(ids.map(id=>g.geometry.cells[g.charts[g.packets[id].chart].cell].key),end.items.map(i=>i.key));
 if(g.geometry.cells[g.charts[g.packets[e.target].chart].cell].geometry==='proton')regularElectronTargets++;
 seedFramesChecked++;
}
assert.equal(seedFramesChecked,24);assert.ok(regularElectronTargets>0,'Alternate seeds did not exercise regular E geometry');
const samples=[...[0,1,2,3,4].map(i=>[0,1,2,3,4].map(j=>[Number(i===j),0])),...[0,1,2,3,4].map(i=>[0,1,2,3,4].map(j=>[0,Number(i===j)])),[[2,-3],[4,5],[-6,7],[9,-7],[-5,6]]];
let coefficientCases=0;
for(const op of r.operations){
 rules.validateTransfer(op);
 for(const sample of samples){const from=applyPhasePermutation(sample,r.packets[op.source].permutation),to=applyPhasePermutation(from,op.permutation);assert.deepEqual(to,applyPhasePermutation(sample,r.packets[op.target].permutation));assert.deepEqual(applyPhasePermutation(to,op.permutation,-1),from);coefficientCases++;}
}
assert.ok(r.nodes.some(n=>n.inspection.counts.electron>=2),'First exit incorrectly stopped other assembly branches');
assert.ok(r.profiles.some(p=>p.counts.electron!==p.counts.proton),'Neutrality was silently imposed as a generation filter');
assert.ok(r.nodes.some(n=>n.inspection.pendingContacts.length),'Extra geometric contacts were silently treated as witnessed transport');
assert.ok(r.summary.maxCarriers<=contract.maxSourceTransitions+1);
assert.deepEqual(await fingerprint(),hashes,'Source dependencies changed during generation');
const certifiedShapes=r.shapes.filter(s=>s.nodes.some(i=>r.nodes[i].inspection.certifiedExit)).length;
const summary={...r.summary,certifiedGeometryRoleAssemblies:certifiedShapes,localCellsExamined:r.cells.length,retainedPackets:r.packets.length,ruleOperations:r.operations.length};
const Pb208={requestedComposition:{proton:82,neutron:126,electron:82},present:false,
 reason:'A seed plus nine one-body-at-most source operations has at most ten primitive bodies; neutral Pb composition requires290. This is a construction-budget obstruction, not a physical nonexistence result.',minimumSingleBodyAdditions:289};
const report={schema:r.schema,status:'pass-complete-seed-generated-nine-operation-search',complete:r.complete,contract:r.contract,summary,profiles:r.profiles,
 verification:{allGeneratedEdgesChecked:edgeChecks,fullFanoutAudited:true,shortWordsEnumerated:shortWords,shortWordConfigurations:wordSignatures.size,coefficientCases,negativeControls,
  originalPNEMatched:true,seedFramesChecked,regularElectronTargets,multipleExitsGenerated:true,nonneutralProfilesRetained:true,resourceStopCannotPass:true},
 sourceHashes:hashes,Pb208,
 scope:'All compatible retained-construction-packet configurations through nine common source operations from the declared marked seed in the locally generated honeycomb. No isotope blueprint or target-count filter. This does not exhaust alternate seeds, unprovided source laws, collective stages, or physically bound atoms.'};
await mkdir(out,{recursive:true});
const archive=path.join(out,'assemblies.jsonl.gz'),gzip=createGzip({level:6}),writing=pipeline(gzip,createWriteStream(archive));
async function put(record){if(!gzip.write(JSON.stringify(record)+'\n'))await once(gzip,'drain');}
await put({type:'header',...report});
for(const type of ['cells','charts','packets','operations'])await put({type,records:r[type]});
await put({type:'points',records:r.points});
for(const node of r.nodes)await put({type:'configuration',...node});
for(const edge of r.edges)await put({type:'construction-edge',...edge});
await put({type:'end',configurations:r.nodes.length,edges:r.edges.length,complete:true});gzip.end();await writing;
let archiveNodes=0,archiveEdges=0,archiveEnd=false;
const lines=createInterface({input:createReadStream(archive).pipe(createGunzip()),crlfDelay:Infinity});
for await(const line of lines){const row=JSON.parse(line);if(row.type==='configuration')archiveNodes++;if(row.type==='construction-edge')archiveEdges++;if(row.type==='end')archiveEnd=row.complete;}
assert.equal(archiveNodes,r.nodes.length);assert.equal(archiveEdges,r.edges.length);assert.equal(archiveEnd,true);
report.archive={file:'assemblies.jsonl.gz',bytes:(await stat(archive)).size,decodedConfigurations:archiveNodes,decodedEdges:archiveEdges,completionFooterVerified:true};
const nodeRecords=r.nodes.map(n=>{const i=n.inspection,flags=(i.exitPackets.length?1:0)|(i.certifiedExit?2:0)|(i.allContactsWitnessed?4:0)|(i.allPacketsCanReachExit?8:0)|(i.allCellsOnEntryExitPaths?16:0);return[n.parent??-1,n.operation??-1,n.shape,n.minTransitions,flags];});
const compact={complete:true,contract:r.contract,summary,profiles:r.profiles,Pb208,scope:report.scope,root:rules.root,
 cells:r.cells,points:r.points,charts:r.charts,packets:r.packets,operations:r.operations,
 outgoing:Object.fromEntries([...rules.operationCache]),protocol:Object.fromEntries(windowProtocol.map(p=>[p.species,{window:p.window,continuation:p.continuation}])),shapes:r.shapes,nodes:nodeRecords};
const template=await readFile(path.join(root,own[3]),'utf8');assert.equal(template.split('__ASSEMBLY_JSON__').length,2);
await writeFile(path.join(out,'index.html'),template.replace('__ASSEMBLY_JSON__',JSON.stringify(compact).replaceAll('<','\\u003c')));
assert.deepEqual(await fingerprint(),hashes,'Inputs changed while writing artifacts; no verification receipt admitted');
await writeFile(path.join(out,'verification.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,complete:true,summary,verification:report.verification,archive:report.archive},null,2));
