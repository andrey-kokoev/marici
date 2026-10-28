import test from 'node:test';
import assert from 'node:assert/strict';
import {oppositeComparisonRole,reverseComparisonPolarity,retainedPolarityPair,pairedPolarityProbe} from '../research/strominger/paired-polarity-model.mjs';
import {makeSinglePEPair} from '../research/strominger/single-pe-pair-model.mjs';
import {applyPhasePermutation} from '../research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {buildCoherentFibration,coherentFibrationProcess} from '../research/realization-tower/fibration-coherent-process.mjs';
const native=makeSinglePEPair(),PN=native.pn.permutation,NE=native.ne.permutation;
const bases=Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>[Number(i===j),Number(i===j)*2]));
test('both sheets are retained and full coefficient polarity is an involution',()=>{
 for(const role of ['proton','electron','neutron'])for(const coefficients of bases){
  const p={role,coefficients,polarity:1,interfaceFlow:1,provenance:{occurrence:'kept'}},saved=structuredClone(p),s=retainedPolarityPair(p);
  assert.deepEqual(p,saved);assert.deepEqual(s.positive,p);assert.notEqual(s.negative,s.positive);
  assert.equal(s.negative.role,oppositeComparisonRole(role));assert.equal(s.negative.interfaceFlow,-1);
  assert.deepEqual(reverseComparisonPolarity(s.negative),p);
 }
});
test('polarity interchanges native PN/NE with their opposite interface readings on every coefficient',()=>{
 for(const p of bases){
  const n=applyPhasePermutation(p,PN),e=applyPhasePermutation(n,NE);
  const jP=reverseComparisonPolarity({role:'proton',coefficients:p,polarity:1});
  assert.deepEqual(applyPhasePermutation(jP.coefficients,NE,-1),n);
  const jE=reverseComparisonPolarity({role:'electron',coefficients:e,polarity:1});
  assert.deepEqual(jE.coefficients,applyPhasePermutation(n,PN,-1));
 }
});
test('bank has eight indexed readings and retains both N flow orientations',()=>{
 const b=pairedPolarityProbe();assert.deepEqual(Object.keys(b),['aa','ab','ba','bb']);
 assert.equal(b.aa.positive.role,'proton');assert.equal(b.aa.negative.role,'electron');
 assert.equal(b.bb.positive.role,'electron');assert.equal(b.bb.negative.role,'proton');
 assert.deepEqual(b.ab.positive.coefficients,b.ab.negative.coefficients);
 assert.equal(b.ab.positive.interfaceFlow,-b.ab.negative.interfaceFlow);
 assert.equal(b.ba.positive.interfaceFlow,-b.ba.negative.interfaceFlow);
});
const tiling=buildCoherentFibration();
test('opposite sheet exposes E without creating a single extra geometric cell',()=>{
 assert.equal(tiling.primitives.length,686);assert.equal(tiling.bodies.length,660);
 assert.equal(tiling.bodies.reduce((s,b)=>s+b.components.length,0),686);
 assert.equal(tiling.polaritySheets.positive.exposedElectrons,1);
 assert.equal(tiling.polaritySheets.negative.exposedElectrons,107);
 for(const b of tiling.bodies)assert.equal(b.polarityRoles.negative,oppositeComparisonRole(b.polarityRoles.positive));
});
test('both sheets obey the same neutral-mediated contact rule',()=>{
 const faces=new Map(),key=vs=>vs.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
 for(const b of tiling.bodies)for(const c of b.components)for(let i=0;i<4;i++){
  const k=key(c.filter((_,j)=>i!==j));if(!faces.has(k))faces.set(k,[]);faces.get(k).push(b);
 }
 for(const bs of faces.values())if(bs.length===2&&bs[0].id!==bs[1].id)for(const sheet of ['positive','negative'])assert.ok(bs.some(b=>b.polarityRoles[sheet]==='neutron'));
});
test('single-entry traversal and full retained return remain unchanged',()=>{
 const first=coherentFibrationProcess(7,0),last=coherentFibrationProcess(7,74);
 assert.equal(first.retainedBodies.length,1);assert.deepEqual(first.retainedBodies[0].boundary,['−P']);
 assert.equal(last.fibrationAudit.returnedToMinusP,true);assert.equal(last.fibrationAudit.polarity.physicalGeometryDuplicated,false);
 assert.equal(last.retainedBodies.length,660);
 assert.equal(new Set(last.interfaceGuides.map(g=>g.color)).size,2);
});
