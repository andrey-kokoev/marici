import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {comparisonSphereSweep} from '../five-side-oct-hopf-probe.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
import {buildLocalHopfTrial,loopPhase} from '../five-side-oct-local-hopf-trial.mjs';
const sector=buildPESymmetricSector(2),trial=buildLocalHopfTrial(sector),byVertex=new Map(trial.stars.map(s=>[s.vertex,s]));
const reading=buildFiveSideOctComparisonDomain(sector,{readingIds:['reading:0:-1']}).readings[0],sweepResults=[];
for(const overlap of reading.overlaps.filter(o=>o.residualCycleRank)){
 const witness=comparisonSphereSweep(sector,overlap),star=byVertex.get(witness.vertex);
 const windings=witness.sweeps.map(s=>Object.entries(s.coefficients).reduce((sum,[id,n])=>sum+n*loopPhase(star,witness.dualFaces[id]),0)/(2*Math.PI));
 for(let i=0;i<windings.length;i++)assert(Math.abs(Math.abs(windings[i])-Math.abs(witness.sweeps[i].degreeRelativeToFirstSweep))<1e-10);
 sweepResults.push({vertex:witness.vertex,windings});
}
for(const star of trial.stars){assert(Math.abs(star.charge+1)<1e-10);for(const f of star.faces)assert(Math.abs(f.phase+f.area/2)<1e-10);}
assert.equal(trial.overlaps.length,168);assert(trial.overlaps.every(o=>Math.abs(Math.abs(o.mismatch)-Math.PI/3)<1e-10));
assert.equal(trial.triangles.length,176);
for(const triangle of trial.triangles)assert.equal(byVertex.get(triangle[0]).cells.filter(c=>triangle.every(v=>byVertex.get(v).cells.includes(c))).length,2);
const paths=['research/strominger/five-side-oct-local-hopf-trial.mjs','research/strominger/five-side-oct-local-hopf-trial-v1.md','research/strominger/five-side-oct-hopf-probe.mjs','research/strominger/pe-symmetric-sector.mjs','research/realization-tower/five-side-oct-comparison-domain.mjs','research/strominger/checkers/check_five_side_oct_local_hopf_trial.mjs','tests/five-side-oct-local-hopf-trial.test.mjs'];
const evidence=[];for(const path of paths)evidence.push({path,sha256:createHash('sha256').update(await fs.readFile(path)).digest('hex')});
const report={schema:'five-side-oct.local-hopf-trial.v1',constructionAdmitted:false,trialAdmitted:false,status:'local Hopf connection works; naive connection-preserving overlap gluing fails',
 assumptions:['cell-centre directions as link base points','common complex phase as a hypothetical extra fibre','shortest-geodesic/Pancharatnam connection','same-cell correspondence on shared comparison rings','connection-preserving U(1) gauge gluing'],
 local:{stars:trial.stars.length,facesPerStar:12,solidAnglePerFace:Math.PI/3,phasePerOutwardFace:-Math.PI/6,phaseSumPerStar:-2*Math.PI,connectionConvention:'arg <q_a,q_b>; clockwise sign relative to the earlier equatorial section-transition convention',sweepReading:reading.readingId??'reading:0:-1',sphereSweeps:sweepResults},
 overlap:{sharedRings:trial.overlaps.length,mismatches:trial.overlaps,absolutePhaseMismatch:Math.PI/3,gaugeInvariant:true,ordinaryFrameAbsoluteMismatch:2*Math.PI/3},
 conjugationAttempt:{pairwiseHolonomiesMatch:true,tripleOverlaps:trial.triangles,sharedCellsPerTriple:2,parity:'three anti-linear changes compose anti-linearly, not to identity'},
 scope:'Rejects this experimental connection-preserving gluing, not the existence of Hopf bundles or other native lifts. No P/E payload transformation, boundary law, route or rendering is admitted. Different base comparisons or connection corrections require a separate source-bound construction.',evidence};
if(process.argv.includes('--record')){const dir='research/strominger/results/five-side-oct-local-hopf-trial-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(`${dir}/verification.json`,JSON.stringify(report,null,2)+'\n');}
console.log(JSON.stringify({status:report.status,constructionAdmitted:false,stars:trial.stars.length,sphereSweeps:sweepResults.length,chargePerStar:-1,sharedRings:trial.overlaps.length,absoluteMismatch:Math.PI/3,tripleOverlapFailures:trial.triangles.length},null,2));
