// Audit-only necessary nuclear-prefix diagnostic. Never an admission bypass.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {compilePhaseAssembly,selectPhaseAssembly,auditPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
import {auditStateCoverage} from '../demos/particle-overlap-tetrahedron/fiber-coverage-model.mjs';
import {assemblyDomain} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
import {lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
const hash=b=>createHash('sha256').update(b).digest('hex');
const paths=['./check_nuclear_electron_separation.mjs','../electron-M2-carrier-trial-v1.md','../cmc-mcm-carrier-binding-v2.md','../window-transfer-prior-research-recovery.md',...['phase-assembly-model.mjs','window-construction-model.mjs','carrier.mjs','phase-advance-model.mjs','phase-discipline-model.mjs','deuterium-tunnel-model.mjs','fiber-coverage-model.mjs','lithium6-assembly-model.mjs','simplex-model.mjs','simplex-components.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f)],sourceHashes={};
for(const p of paths)sourceHashes[p]=hash(await readFile(new URL(p,import.meta.url)));
// Keep the EXACT compiler prefix through all local interface audits and rooted
// directed reachability. Stop BEFORE any terminal/exit choice is made.
const url=new URL('../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs',import.meta.url),source=await readFile(url,'utf8');
const start=source.indexOf('export function compilePhaseAssembly('),cut=source.indexOf(' const exitPaths=new Map();',start),end=source.indexOf('\nconst cache=new Map();',cut);
assert.ok(start>=0&&cut>start&&end>cut);
const prefix=source.slice(start,cut);
assert.ok(prefix.includes("reason:'phase-directed-carrier-unreachable'"));
assert.ok(!prefix.includes('exitPaths'));
const tail=" return {status:'nuclear-local-compatible',admitted:false,boundaryStatus:'not-assessed',charts,edges,root,paths:Object.fromEntries(paths),requiredNuclearCells:[...nucleus]};\n}\n";
let adapted=source.slice(0,cut)+tail+source.slice(end);
adapted=adapted.replace(/from '(\.[^']+)'/g,(_,p)=>`from '${new URL(p,url).href}'`);
const isolated=await import('data:text/javascript;base64,'+Buffer.from(adapted).toString('base64'));
function nuclearDiagnostic(candidate,orientation){
 assert.deepEqual(candidate.electrons,[],'Nuclear diagnostic cannot accept occupied electrons');
 assert.ok(candidate.interfaces.every(e=>e.kind==='PN'||e.kind==='NN'));
 return isolated.compilePhaseAssembly(candidate,orientation);
}
function strip(reference){
 const {nucleus,types,interfaces}=reference.candidate,vertices=new Set(nucleus.flatMap(i=>lattice.cells[i]));
 return {nucleus:[...nucleus],electrons:[],types:Object.fromEntries(Object.entries(types).filter(([v])=>vertices.has(Number(v)))),interfaces:structuredClone(interfaces.filter(e=>e.kind!=='NE'))};
}
const records=[];
for(const isotope of ['helium3','helium4','lithium6','lithium7','beryllium9','boron10','boron11','carbon12','carbon13','nitrogen15']){
 const full=selectPhaseAssembly(isotope);auditPhaseAssembly(full);const bare=strip(full),local=nuclearDiagnostic(bare,full.orientations),ordinary=compilePhaseAssembly(bare,full.orientations);
 assert.equal(local.status,'nuclear-local-compatible');assert.equal(local.admitted,false);assert.equal(local.boundaryStatus,'not-assessed');
 assert.equal(ordinary.status,'rejected');assert.equal(ordinary.reason,'phase-directed-dead-end');
 assert.equal(new Set(local.charts.map(c=>c.cell)).size,bare.nucleus.length);
 const bad=structuredClone(bare);bad.interfaces.pop();assert.throws(()=>nuclearDiagnostic(bad,full.orientations),/ledger mismatch|Invalid reader assignment/);
 assert.throws(()=>nuclearDiagnostic(full.candidate,full.orientations));
 records.push({isotope,nuclearCells:bare.nucleus.length,localStatus:local.status,productionBareStatus:ordinary,admitted:false,certificateBoundary:'not-assessed'});
}
const prior=JSON.parse(await readFile(new URL('../results/carbon13-proton-capture/verification.json',import.meta.url),'utf8'));
const full=compilePhaseAssembly(prior.witness.reference.candidate,prior.witness.orientation);auditPhaseAssembly(full);
const bare=strip(full),local=nuclearDiagnostic(bare,full.orientations);assert.equal(local.status,'nuclear-local-compatible');
assert.equal(compilePhaseAssembly(bare,full.orientations).reason,'phase-directed-dead-end');
records.push({isotope:'nitrogen14-plus',nuclearCells:14,localStatus:local.status,productionBareStatus:'phase-directed-dead-end',admitted:false,certificateBoundary:'not-assessed'});
const corrupt=structuredClone(bare);corrupt.types[lattice.cells[0][0]]='M';assert.throws(()=>nuclearDiagnostic(corrupt,full.orientations),/MMCC/);
// An isolated physical proton is not covered by an occupied-PN-chart ansatz.
// Keep this countercontrol: the new diagnostic is not a universal nucleus test.
const lone={nucleus:[0],electrons:[],types:Object.fromEntries(lattice.cells[0].map((v,i)=>[v,['C','M','C','M'][i]])),interfaces:[]};
const loneResult=nuclearDiagnostic(lone,0);assert.equal(loneResult.reason,'missing-carrier-reader');
// Logical countermodel ONLY: terminality concerns transitions, not geometric
// adjacency. These arrows are not asserted to be native physical transports.
const eeReceipt=JSON.parse(await readFile(new URL('../results/n14-assumptions/ee.json',import.meta.url),'utf8'));
const ee=eeReceipt.witness.candidate.interfaces.find(e=>e.kind==='EE'),{adjacency}=assemblyDomain();assert.ok(adjacency[ee.from].some(e=>e.to===ee.to));
const graph={states:[{id:'s',cell:'entry'},{id:'e1',cell:String(ee.from)},{id:'e2',cell:String(ee.to)}],transitions:[['s','e1'],['s','e2']],entryStates:['s'],exitStates:['e1','e2'],requiredCells:['entry',String(ee.from),String(ee.to)]};
assert.equal(auditStateCoverage(graph).status,'covered');
assert.throws(()=>auditStateCoverage({...graph,transitions:[...graph.transitions,['e1','e2']]}),/Terminal exit state/);
const open=auditStateCoverage({...graph,exitStates:[]});assert.equal(open.status,'pending-boundary');assert.equal(open.allEnteredStatesReachExit,null);
for(const p of paths)assert.equal(hash(await readFile(new URL(p,import.meta.url))),sourceHashes[p],'Source changed: '+p);
const receipt={status:'source-boundary-and-necessary-prefix-audit-passed',sourceHashes,compilerPrefixSha256:hash(prefix),records,standaloneProtonControl:loneResult,terminalityCountermodel:{kind:'abstract-graph-only-not-native-transport',touchingCells:[ee.from,ee.to],sharedFace:ee.face,terminalCoverage:'covered',physicalAdmission:false},missingExitBoundary:open.status,conclusion:'Tetrahedral E carriers are retained trial inputs; terminal E traversal does not imply geometric EE exclusion; full E-exit coverage is a whole-assembly certificate policy. Nuclear-local compatibility is a necessary prefix diagnostic only, not nuclear admission, binding, stability or a source-derived replacement boundary rule.',productionChanged:false};
await mkdir('research/strominger/results/nuclear-electron-separation',{recursive:true});await writeFile('research/strominger/results/nuclear-electron-separation/verification.json',JSON.stringify(receipt,null,2)+'\n');
console.log(JSON.stringify({status:receipt.status,checkedReferences:records.length,standaloneProtonControl:loneResult,terminalityDoesNotImplyNonadjacency:true,nuclearAdmissionRuleDerived:false,productionChanged:false},null,2));
