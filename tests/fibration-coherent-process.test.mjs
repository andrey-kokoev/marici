import test from 'node:test';
import assert from 'node:assert/strict';
import {buildCoherentFibration,coherentFibrationProcess,coherentFibrationStages,confirmFibrationRound,confirmReturnRound} from '../research/realization-tower/fibration-coherent-process.mjs';
import {processState} from '../research/realization-tower/normal-ray-processes.mjs';
import {cells,worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
const tiling=buildCoherentFibration();
const key=vs=>vs.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
const volume=vs=>{const p=vs.map(worldPoint),[a,b,c]=p.slice(1).map(v=>v.map((x,i)=>x-p[0][i]));return Math.abs(a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]))/6;};
test('all native primitives occur exactly once, with no rescaling or volume loss',()=>{
 assert.equal(tiling.primitives.length,2*cells.length);assert.equal(new Set(tiling.bodies.flatMap(b=>b.members)).size,686);
 assert.equal(tiling.bodies.reduce((s,b)=>s+b.members.length,0),686);
 assert.equal(new Set(tiling.bodies.flatMap(b=>b.components.map(key))).size,686);
 const source=cells.reduce((s,c)=>s+volume(c.vertices),0),total=tiling.bodies.reduce((s,b)=>s+b.components.reduce((a,v)=>a+volume(v),0),0);
 assert.ok(Math.abs(total-2*source)<1e-8);
});
test('closed outer sphere and seam certificates are computed from complete faces',()=>{
 assert.equal(tiling.audit.outerTriangles,294);assert.equal(tiling.audit.seamFaceCount,49);
 const vertices=new Set(),edges=new Set();for(const f of tiling.boundaryFaces){for(const p of f.vertices)vertices.add(key([p]));for(let i=0;i<3;i++)edges.add(key(f.vertices.filter((_,j)=>i!==j)));}
 assert.equal(vertices.size-edges.size+tiling.boundaryFaces.length,2);
 assert.equal(tiling.audit.nonmanifoldFaces,0);assert.equal(tiling.audit.allSharedFacesOppositeSided,true);
});
test('seam composites are explicit and all non-seed growth is face witnessed',()=>{
 assert.equal(tiling.seamPairs.length,26);assert.equal(tiling.bodies.length,660);
 for(const pair of tiling.seamPairs){assert.equal(pair.members.length,2);assert.equal(pair.nativePrimitive,false);assert.equal(pair.face.length,3);}
 for(let r=1;r<tiling.rounds.length;r++)assert.equal(confirmFibrationRound(tiling,r).status,'positively-confirmed');
 assert.equal(tiling.audit.unmediatedChargedContacts,0);assert.equal(tiling.audit.boundaryOverrides.length,6);
 assert.equal(tiling.audit.nativeParticleRealization,false);
});
test('only −P seeds growth; +P is the unique outward terminal',()=>{
 const first=coherentFibrationProcess(7,0);
 assert.equal(first.retainedBodies.length,1);assert.deepEqual(first.retainedBodies[0].boundary,['−P']);
 assert.deepEqual(tiling.rounds[0],[tiling.entry]);assert.deepEqual(tiling.rounds.at(-1),[tiling.exit]);
 assert.ok(tiling.bodies.filter(b=>b.boundary.length&&!b.boundary.includes('−P')).every(b=>b.round>0));
 assert.equal(tiling.rounds.length-1,37);assert.equal(coherentFibrationStages.length,75);
});
test('return starts at +P and reaches every retained body through real faces, ending only at −P',()=>{
 assert.deepEqual(tiling.returnRounds[0],[tiling.exit]);assert.deepEqual(tiling.returnRounds.at(-1),[tiling.entry]);
 assert.equal(new Set(tiling.returnRounds.flat()).size,660);
 for(let r=1;r<tiling.returnRounds.length;r++)assert.equal(confirmReturnRound(tiling,r).status,'positively-confirmed');
 let count=0;for(let i=0;i<75;i++){
  const p=coherentFibrationProcess(7,i);assert.ok(p.retainedBodies.length>=count);count=p.retainedBodies.length;
  assert.equal(p.fibrationAudit.mixedCells.length,0);assert.equal(p.canAdvance,i<74);
  if(i>=37){assert.equal(count,660);assert.equal(p.fibrationAudit.filledPrimitives,686);}
  if(i>37)assert.equal(p.fibrationAudit.confirmations.at(-1).round,i-37);
 }
 const last=coherentFibrationProcess(7,74);
 assert.equal(last.fibrationAudit.confirmations.length,37);assert.equal(last.fibrationAudit.returnedToMinusP,true);
 assert.equal(last.fibrationAudit.flow,'+P → −P');assert.ok(last.interfaceGuides.length>0);
 assert.throws(()=>coherentFibrationProcess(7,75));
});
test('the unfolded reference remains available while the viewer uses the folded successor',()=>{
 assert.equal(coherentFibrationProcess(7,14).fibrationAudit.generated,true);
 assert.equal(processState('fibration-12x12',7,14).fibrationAudit.folded,true);
});
test('a broken retained interface cannot receive positive confirmation',()=>{
 const bad=structuredClone(tiling),first=bad.admission[0];first.witnesses[0].face[0][0]+=100;
 assert.throws(()=>confirmFibrationRound(bad,first.round),/Unconfirmed/);
 const brokenReturn=structuredClone(tiling),ret=brokenReturn.returnAdmission[0];ret.witnesses[0].face[0][0]+=100;
 assert.throws(()=>confirmReturnRound(brokenReturn,ret.round),/Unconfirmed/);
});
