import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildGlobalHopfTrial,connectionMap,pathPhase} from '../five-side-oct-global-hopf-trial.mjs';
import {wrapPhase} from '../five-side-oct-local-hopf-trial.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
const sector=buildPESymmetricSector(2),trial=buildGlobalHopfTrial(sector),connection=connectionMap(trial),readings=[];
for(let axis=0;axis<3;axis++)for(const sign of [-1,1]){
 const id=`reading:${axis}:${sign}`,r=buildFiveSideOctComparisonDomain(sector,{readingIds:[id]}).readings[0];let moves=0,cycles=0,maxContextError=0,maxCycleError=0;
 for(const o of r.overlaps){const paths=new Map(o.paths.map(p=>[p.id,p.cells]));
  for(const m of o.moves){const a=paths.get(m.from),b=paths.get(m.to),i=m.position,full=pathPhase(connection,a)-pathPhase(connection,b),local=pathPhase(connection,a.slice(i-1,i+2))-pathPhase(connection,b.slice(i-1,i+2));maxContextError=Math.max(maxContextError,Math.abs(wrapPhase(full-local)));moves++;}
  for(const cycle of o.cycleBasis){const sum=cycle.steps.reduce((s,step)=>s+pathPhase(connection,paths.get(step.from))-pathPhase(connection,paths.get(step.to)),0);maxCycleError=Math.max(maxCycleError,Math.abs(wrapPhase(sum)));cycles++;}
 }
 assert(maxContextError<1e-9&&maxCycleError<1e-9);readings.push({id,moves,cycles,maxContextError,maxCycleError});
}
const maxFaceError=Math.max(...trial.faces.flatMap(f=>f.occurrences.map(o=>o.phaseAgreementError))),maxSharedError=Math.max(...trial.shared.map(f=>Math.abs(f.occurrences[0].flux+f.occurrences[1].flux)));
assert(maxFaceError<1e-9&&maxSharedError<1e-9);
for(const s of trial.starFlux){assert(Math.abs(s.flux+2*Math.PI)<1e-9);for(const [source,flux]of Object.entries(s.fluxBySource))assert(Math.abs(flux+(source===s.vertex?2*Math.PI:0))<1e-9);}
assert(Math.abs(trial.boundaryFlux+44*2*Math.PI)<1e-9);
assert.deepEqual(new Set(trial.edgePhases.map(e=>e.endpoints.join('|'))),new Set(sector.faces.filter(f=>f.owners.length===2).map(f=>[...f.owners].sort().join('|'))));
const paths=['research/strominger/five-side-oct-global-hopf-trial.mjs','research/strominger/five-side-oct-global-hopf-trial-v1.md','research/strominger/five-side-oct-local-hopf-trial.mjs','research/strominger/five-side-oct-hopf-probe.mjs','research/strominger/pe-symmetric-sector.mjs','research/realization-tower/five-side-oct-comparison-domain.mjs','research/strominger/checkers/check_five_side_oct_global_hopf_trial.mjs','tests/five-side-oct-global-hopf-trial.test.mjs'];
const evidence=[];for(const path of paths)evidence.push({path,sha256:createHash('sha256').update(await fs.readFile(path)).digest('hex')});
const report={schema:'five-side-oct.global-hopf-trial.v1',constructionAdmitted:false,nativeBindingAdmitted:false,status:'conditional global Abelian connection passes overlap and bounded context checks',
 assumptions:['one equal-sign unit monopole at every interior vertex','tensor-product of these hypothetical complex line bundles','cell-centre base points and shortest-geodesic factor connections','retain solid-angle branches and factor labels; do not infer charge from exponentials'],
 coverage:{nativeCells:sector.cells.length,nativeInterfaces:trial.edgePhases.length,dualFaces:trial.faces.length,dualCells:trial.starFlux.length,sharedFaces:trial.shared.length,dualBoundaryFaces:trial.boundary.length},
 maxFaceError,maxSharedError,dualBoundaryFlux:trial.boundaryFlux,dualBoundaryCharge:trial.boundaryFlux/(2*Math.PI),readings,starFlux:trial.starFlux,
 faces:trial.faces.map(f=>({nativeEdge:f.nativeEdge,occurrences:f.occurrences.map(o=>({star:o.star,ring:o.ring,flux:o.flux,loop:o.loop}))})),
 scope:'A new global reference connection, not a gauge repair of the old isolated connections. The extra factors alter local curvature while preserving one unit per dual cell. The 192-face dual boundary is not the native octahedral boundary law. Abelian context cancellation does not establish native nonabelian/history coherence, identify the 80 retained fibres, authorize all potential comparisons, or select any routes.',evidence};
if(process.argv.includes('--record')){const dir='research/strominger/results/five-side-oct-global-hopf-trial-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(`${dir}/verification.json`,JSON.stringify(report,null,2)+'\n');}
console.log(JSON.stringify({status:report.status,constructionAdmitted:false,coverage:report.coverage,maxFaceError,maxSharedError,dualBoundaryCharge:report.dualBoundaryCharge,readings},null,2));
