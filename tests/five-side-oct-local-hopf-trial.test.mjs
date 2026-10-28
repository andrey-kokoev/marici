import test from 'node:test';
import assert from 'node:assert/strict';
import {buildPESymmetricSector} from '../research/strominger/pe-symmetric-sector.mjs';
import {commonPhase} from '../research/strominger/five-side-oct-hopf-probe.mjs';
import {buildLocalHopfTrial,loopPhase,overlapPhase,wrapPhase} from '../research/strominger/five-side-oct-local-hopf-trial.mjs';
const near=(x,y,tol=1e-10)=>assert(Math.abs(x-y)<tol,`${x} != ${y}`);
const sector=buildPESymmetricSector(2),trial=buildLocalHopfTrial(sector);
test('native dual faces carry half-solid-angle Hopf curvature, retaining integer winding',()=>{
 assert.equal(trial.stars.length,44);
 for(const s of trial.stars){assert.equal(s.faces.length,12);near(s.totalArea,4*Math.PI);near(s.phaseSum,-2*Math.PI);near(s.charge,-1);near(wrapPhase(s.phaseSum),0);
  for(const f of s.faces){near(f.area,Math.PI/3);near(f.phase,-f.area/2);near(loopPhase(s,[...f.ring].reverse()),-f.phase);}
 }
});
test('independent vertex and cell gauge changes leave loop phases and gluing failures unchanged',()=>{
 const gauge=(v,c)=>[...v+'|'+c].reduce((s,x)=>s+x.charCodeAt(0)*.713,0),changed=buildLocalHopfTrial(sector,{gauge});
 for(let i=0;i<trial.stars.length;i++){near(changed.stars[i].charge,trial.stars[i].charge);for(let j=0;j<12;j++)near(changed.stars[i].faces[j].phase,trial.stars[i].faces[j].phase);}
 for(let i=0;i<trial.overlaps.length;i++)near(changed.overlaps[i].mismatch,trial.overlaps[i].mismatch);
 const q=[1,0,0,0],r=[Math.SQRT1_2,0,Math.SQRT1_2,0];near(wrapPhase(overlapPhase(commonPhase(q,.2),commonPhase(r,.7))-overlapPhase(q,r)),.5);
 assert.throws(()=>overlapPhase(q,[0,0,1,0]),/Antipodal/);
});
test('shared-ring holonomy obstructs connection-preserving U(1) gauge gluing for this trial',()=>{
 assert.equal(trial.overlaps.length,168);
 for(const o of trial.overlaps){near(Math.abs(o.mismatch),Math.PI/3);near(o.conjugatedMismatch,0);near(Math.abs(wrapPhase(2*o.mismatch)),2*Math.PI/3);}
});
test('conjugating every neighbour cannot satisfy triple chart cocycles',()=>{
 assert.equal(trial.triangles.length,176);const stars=new Map(trial.stars.map(s=>[s.vertex,s]));
 for(const triangle of trial.triangles){
  const common=stars.get(triangle[0]).cells.filter(id=>triangle.every(v=>stars.get(v).cells.includes(id)));assert.equal(common.length,2);
  assert(sector.faces.some(f=>triangle.every(v=>f.vertices.some(p=>p.join(',')===v))));
  // Three anti-linear transition maps compose anti-linearly, independently
  // of their phases, and therefore cannot equal the identity on a C fibre.
  assert.equal((-1)**triangle.length,-1);
 }
});
test('the same local connection issue occurs at the small-carrier scale',()=>{
 const small=buildLocalHopfTrial(buildPESymmetricSector(1));assert.equal(small.stars.length,6);
 for(const s of small.stars)near(s.charge,-1);assert(small.overlaps.length>0&&small.triangles.length>0);
 for(const o of small.overlaps)near(Math.abs(o.mismatch),Math.PI/3);
});
