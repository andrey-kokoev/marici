import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {compilePhaseAssembly,auditPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const out='research/strominger/results/lithium-discrimination',digest=b=>createHash('sha256').update(b).digest('hex');
const empirical=JSON.parse(await readFile(out+'/empirical-baseline.json','utf8')),rows=[];let baseline=null;
for(const mass of [5,6,7,8]){
 const {summary:s,acceptedGeometries,firstWitness}=JSON.parse(await readFile(`${out}/li${mass}.json`,'utf8'));
 assert.equal(s.complete,true);assert.equal(s.isotope,'Li-'+mass);assert.equal(s.retainedPreviousIsotopeRequired,false);assert.equal(s.allowNN,true);
 if(baseline)assert.deepEqual(s.sourceHashes,baseline);else baseline=s.sourceHashes;
 assert.equal(s.protocolSha256,digest(await readFile(new URL('../lithium-discrimination-protocol-v1.md',import.meta.url))));
 assert.equal(s.checkerSha256,digest(await readFile(new URL('./check_lithium_discrimination.mjs',import.meta.url))));
 assert.equal(s.readerAssignments,s.admittedAssignments+Object.values(s.rejections).reduce((a,b)=>a+b,0));
 assert.equal(acceptedGeometries.length,s.admittedGeometries);assert.equal(acceptedGeometries.reduce((n,g)=>n+g.orientations.length,0),s.admittedAssignments);
 for(const g of acceptedGeometries)for(const orientation of g.orientations){const r=compilePhaseAssembly(g.candidate,orientation);assert.equal(r.status,'phase-coherent-reference');assert.equal(auditPhaseAssembly(r).coverage.coveredCells,mass+3);}
 if(s.admittedAssignments){assert.ok(firstWitness);assert.equal(auditPhaseAssembly(firstWitness.reference).coverage.coveredCells,mass+3);}else assert.equal(firstWitness,null);
 const e=empirical.rows.find(e=>e.isotope===s.isotope);assert.ok(e);
 rows.push({isotope:s.isotope,empirical:e.description,empiricallyStable:e.stable,compatible:s.admittedAssignments>0,geometryCandidates:s.geometryCandidates,readerAssignments:s.readerAssignments,admittedGeometries:s.admittedGeometries,admittedAssignments:s.admittedAssignments});
}
for(const [f,h] of Object.entries(baseline))assert.equal(digest(await readFile(new URL('../demos/particle-overlap-tetrahedron/'+f,import.meta.url))),h,'Stale source: '+f);
const acceptedUnstable=rows.filter(r=>r.compatible&&!r.empiricallyStable).map(r=>r.isotope),rejectedStable=rows.filter(r=>!r.compatible&&r.empiricallyStable).map(r=>r.isotope);
const result={status:'complete-frozen-rule-comparison',rows,acceptedUnstable,rejectedStable,empiricalSource:empirical.url,interpretation:acceptedUnstable.length?'Compatibility is not sufficient for empirical nuclear stability.':'No unstable acceptance in this bounded sample; not a physical stability derivation.',bindingVersusDecay:'Li-5 is proton-unbound; Li-8 is bound but beta-radioactive. A compatible Li-8 assembly is not itself a contradiction. The rules do not calculate binding energies, decay channels or lifetimes.',scope:'Neutral 3P lithium targets, same bounded geometry/phase rules, exhaustive reader assignments for all emitted candidates. No retained-isotope filter or fitted count threshold. Counts are not probabilities.'};
await writeFile(out+'/verification.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
