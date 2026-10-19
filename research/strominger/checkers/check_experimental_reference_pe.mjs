// Replay the explicit constructor against unchanged source rules and old trials.
import assert from 'node:assert/strict';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {GenerativeAssemblyRules} from '../demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {phaseUniverse} from '../demos/particle-overlap-tetrahedron/local-reference-universe.mjs';
import {POLICY,constructReferencePE,verifyReferencePE,auditReferencePEAssembly} from './experimental_reference_pe.mjs';
const root=new URL('../../../',import.meta.url),base=new URL('../results/',import.meta.url),hashes={};
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
async function load(url){const bytes=await readFile(url);hashes[fileURLToPath(url).slice(fileURLToPath(root).length).replaceAll('\\','/')]=hash(bytes);return JSON.parse(bytes);}
const nativeFile=new URL('research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs',root),nativeBefore=hash(await readFile(nativeFile));
const probe=await load(new URL('terminal-pe-probe/verification.json',base));
const hydrogen=await load(new URL('hydrogen-edge-attachment/verification.json',base));
let controls=0,sameBodyVacancyControls=0;const hydrogenResults=[],deletions=[];
function reject(fn){assert.throws(fn);controls++;}
for(const [mark,h] of hydrogen.rows.entries()){
 const aliases=h.bodies[0].aliases,seedBindings=Object.fromEntries(['C0','M0','C1','M1'].map(k=>[k,aliases[k]]));
 const r=new GenerativeAssemblyRules({seedBindings}),p=r.root;
 const pnId=r.outgoing(p).find(i=>r.operations[i].kind==='PN'),n=r.operations[pnId].target;
 const neId=r.outgoing(n).find(i=>r.operations[i].kind==='NE'),e=r.operations[neId].target;
 const h1=auditReferencePEAssembly(r,[p,e],{policy:POLICY,expectedCounts:{proton:1,neutron:0,electron:1}});
 const h2=auditReferencePEAssembly(r,[p,n,e],{policy:POLICY,expectedCounts:{proton:1,neutron:1,electron:1}});
 assert(!h1.nativePass&&h1.experimentalPass&&h1.witnesses.length===1);
 assert(h2.nativePass&&h2.experimentalPass&&h2.witnesses.length===0);
 const witness=h1.witnesses[0];assert.equal(witness.admission,'experimental-only');assert.equal(witness.native,false);
 reject(()=>constructReferencePE(r,[p,e],{pnId,neId}));
 reject(()=>constructReferencePE(r,[p,n,e],{pnId,neId,policy:POLICY}));
 const advance=r.outgoing(p).find(i=>r.operations[i].kind==='reader-phase-advance');
 assert(advance!==undefined);
 reject(()=>constructReferencePE(r,[p,e,r.operations[advance].target],{pnId,neId,policy:POLICY}));
 const nAdvance=r.outgoing(n).find(i=>r.operations[i].kind==='reader-phase-advance');
 if(nAdvance!==undefined){
  const n2=r.operations[nAdvance].target,selected=[p,e,n2];
  assert.equal(r.charts[r.packets[n2].chart].cell,r.charts[r.packets[n].chart].cell);
  assert(r.describe(selected).valid);
  assert.throws(()=>constructReferencePE(r,selected,{pnId,neId,policy:POLICY}),/neutron body is occupied/);controls++;sameBodyVacancyControls++;
 }
 for(const mutate of [w=>{w.permutation[0]=w.permutation[1];},w=>{w.referenceFrames[1].chart.aliases.C0='unregistered';},w=>{w.native=true;},w=>{w.contextSelected=[];}]){
  const bad=structuredClone(witness);mutate(bad);reject(()=>verifyReferencePE(r,[p,e],bad,{policy:POLICY}));
 }
 reject(()=>r.validateTransfer({source:p,target:e,kind:'reference-mediated-PE',phaseDelta:0,permutation:witness.permutation,face:witness.edge}));
 assert(r.operations.every(op=>op.kind!=='reference-mediated-PE'));
 hydrogenResults.push({mark,nativeH1:false,experimentalH1:true,nativeH2:true,experimentalH2Shortcuts:0,witness});
}
for(const isotope of ['n15','ne22']){
 const directory=new URL(`reference-${isotope}-search/`,base),summary=await load(new URL('verification.json',directory));
 const row=summary.rows.find(row=>row.witnessFile),saved=(await load(new URL(row.witnessFile,directory))).witness;
 const universe=phaseUniverse({maxOrigin:row.maxOrigin}),r=universe.rules;assert(universe.complete);
 for(const p of saved.packets)assert.deepEqual(r.packets[p.id],p);
 for(const c of saved.charts)assert.deepEqual(r.charts[Number(c.id.split('-').at(-1))],c);
 for(const op of saved.operations)assert.deepEqual(r.operations[op.id],op);
 for(const old of probe.deletions.filter(d=>d.sourceIsotope===isotope)){
  const result=auditReferencePEAssembly(r,old.selectedPackets,{policy:POLICY,expectedCounts:old.counts});
  assert.equal(result.experimentalPass,old.variants['electron-and-proton-record-terminal'].passesHypotheticalChecks);
  assert.equal(result.nativePass,old.baseline.passesHypotheticalChecks);
  const key=w=>JSON.stringify([w.source,w.target,w.referenceNeutronCell,w.nativeFactors,w.permutation]);
  assert.deepEqual(result.witnesses.map(key).sort(),old.shortcuts.filter(w=>w.recordTerminal).map(key).sort());
  if(result.experimentalPass){
   assert(result.allOccupiedContactsNativelyWitnessed);
   assert.equal(result.extended.construction.length,result.selectedPackets.length-1);
   const badCounts={...old.counts,neutron:old.counts.neutron+1};
   reject(()=>auditReferencePEAssembly(r,old.selectedPackets,{policy:POLICY,expectedCounts:badCounts}));
  }
  deletions.push({sourceIsotope:isotope,deletedNeutronCell:old.deletedNeutron.cell,...result});
 }
 assert(r.operations.every(op=>op.kind!=='reference-mediated-PE'));
}
assert.equal(deletions.length,20);assert.equal(deletions.filter(d=>d.experimentalPass).length,4);
const positives=deletions.filter(d=>d.experimentalPass);
assert.deepEqual(positives.map(d=>[d.sourceIsotope,d.deletedNeutronCell]),[['n15',16],['n15',17],['ne22',16],['ne22',29]]);
assert.equal(positives.reduce((n,d)=>n+d.witnesses.length,0),6);assert(sameBodyVacancyControls>0);
const independentLog=execFileSync(process.env.PYTHON??'python',[fileURLToPath(new URL('check_terminal_pe_independent.py',import.meta.url))],{cwd:fileURLToPath(root),encoding:'utf8',timeout:120000});
const independent=await load(new URL('terminal-pe-independent/verification.json',base));
assert.equal(independent.status,'independent-python-check-passed');
for(const result of deletions){const separate=independent.isotopeTrials.find(row=>row.source===result.sourceIsotope&&row.deleted===result.deletedNeutronCell);assert(separate);assert.equal(separate.passes,result.experimentalPass);assert.equal(separate.shortcuts,result.witnesses.length);}
assert.equal(hash(await readFile(nativeFile)),nativeBefore);
const report={schema:'marici.experimental-reference-PE-replay.v1',status:'pass',policy:POLICY,hydrogenResults,deletions,
 positiveIsotopeConfigurations:positives.map(d=>({source:d.sourceIsotope,deleted:d.deletedNeutronCell,counts:d.counts,constructors:d.witnesses.length})),
 negativeControls:controls,sameBodyVacancyControls,independentPythonAgreement:true,independentLog,
 nativeRuleFileUnchanged:true,nativeAdmissionChanged:false,
 scope:'Explicit experimental constructor and fresh replay of saved finite candidates, not a derived occupancy law, new isotope search, physical stability or viewer admission.'};
for(const relative of ['research/strominger/checkers/experimental_reference_pe.mjs','research/strominger/checkers/check_experimental_reference_pe.mjs','research/strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs','research/strominger/demos/particle-overlap-tetrahedron/local-reference-universe.mjs','research/strominger/experimental-reference-pe-constructor-v1.md'])hashes[relative]=hash(await readFile(new URL(relative,root)));
report.sourceHashes=hashes;const out=new URL('experimental-reference-pe-constructor/',base);await mkdir(out,{recursive:true});await writeFile(new URL('verification.json',out),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,hydrogenMarkings:hydrogenResults.length,deletionTrials:deletions.length,positiveIsotopeConfigurations:report.positiveIsotopeConfigurations,negativeControls:controls,sameBodyVacancyControls,independentPythonAgreement:true,nativeAdmissionChanged:false},null,2));
