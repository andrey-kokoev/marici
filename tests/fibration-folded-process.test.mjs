import test from 'node:test';
import assert from 'node:assert/strict';
import {buildFoldedFibration,foldedFibrationProcess,foldedFibrationStages,confirmFoldedRound} from '../research/realization-tower/fibration-folded-process.mjs';
import {processState} from '../research/realization-tower/normal-ray-processes.mjs';
import {reflectAcrossFibrationSeam} from '../research/realization-tower/fibration-step-machine.mjs';
import {cells} from '../research/realization-tower/normal-ray-model.mjs';
const model=buildFoldedFibration(),key=vs=>vs.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
test('175 whole cells partition the original 343 primitive cells exactly',()=>{
 assert.equal(model.geometry.length,175);assert.equal(model.geometry.filter(g=>g.kind==='tetrahedron').length,119);
 assert.equal(model.geometry.filter(g=>g.kind==='octahedron').length,56);
 const ids=model.geometry.flatMap(g=>g.primitiveIds);assert.equal(ids.length,343);assert.equal(new Set(ids).size,343);
 for(const g of model.geometry){assert.equal(g.components.length,0);if(g.kind==='octahedron'){
  assert.equal(g.primitiveIds.length,4);assert.equal(g.vertices.length,6);assert.equal(g.faces.length,8);
  const edges=new Set();for(const f of g.faces)for(let i=0;i<3;i++)edges.add(key(f.filter((_,j)=>i!==j)));
  assert.equal(edges.size,12); // No subdivision diagonal.
 }else{assert.equal(g.primitiveIds.length,1);assert.equal(g.faces.length,4);}}
});
test('fold matches all vertices and whole faces, with exactly two distinct preimages per cell',()=>{
 assert.equal(model.occurrences.length,350);
 for(const g of model.geometry){
  assert.equal(g.occurrences.length,2);
  for(const id of g.occurrences){const o=model.occurrences.find(x=>x.id===id),fold=o.copy==='clone'?reflectAcrossFibrationSeam:p=>p;
   assert.equal(key(o.vertices.map(fold)),key(g.vertices));
   assert.deepEqual(o.faces.map(f=>key(f.map(fold))).sort(),g.faces.map(key).sort());
  }
 }
});
test('folded face complex is a closed sphere with no duplicate or nonmanifold cells',()=>{
 const faces=new Map(),vertices=new Set(),edges=new Set();
 for(const g of model.geometry)for(const f of g.faces)faces.set(key(f),(faces.get(key(f))||0)+1);
 assert.ok([...faces.values()].every(n=>n===1||n===2));
 assert.equal(model.outer.length,196);
 for(const f of model.outer){f.vertices.forEach(v=>vertices.add(key([v])));for(let i=0;i<3;i++)edges.add(key(f.vertices.filter((_,j)=>j!==i)));}
 assert.equal(vertices.size-edges.size+model.outer.length,2);
 assert.equal(new Set(model.geometry.map(g=>key(g.vertices))).size,175);
 // The quotient contains one copy's volume, not two overlapping copies.
 assert.equal(model.geometry.reduce((s,g)=>s+g.primitiveIds.length,0),cells.length);
});
test('coincident −P/+P geometry does not identify their occurrences or short-circuit traversal',()=>{
 const entry=model.occurrences.find(o=>o.id===model.entry),exit=model.occurrences.find(o=>o.id===model.exit);
 assert.notEqual(entry.id,exit.id);assert.equal(entry.geometryId,exit.geometryId);
 assert.deepEqual(model.outward.rounds[0],[entry.id]);assert.deepEqual(model.outward.rounds.at(-1),[exit.id]);
 assert.deepEqual(model.back.rounds[0],[exit.id]);assert.deepEqual(model.back.rounds.at(-1),[entry.id]);
 assert.equal(model.outward.rounds.length,24);assert.equal(model.back.rounds.length,24);assert.equal(foldedFibrationStages.length,51);
 for(const dir of ['outward','return'])for(let i=1;i<24;i++)assert.equal(confirmFoldedRound(model,dir,i).status,'positively-confirmed');
 const first=foldedFibrationProcess(7,0),last=foldedFibrationProcess(7,46);
 assert.equal(first.retainedBodies.length,1);assert.equal(first.fibrationAudit.admittedOccurrences,1);
 assert.equal(last.retainedBodies.length,175);assert.equal(last.fibrationAudit.admittedOccurrences,350);assert.equal(last.fibrationAudit.returnedToMinusP,true);
 assert.equal(last.fibrationAudit.coarse.physicalHalfFaceSplits,0);
 assert.deepEqual(processState('fibration-12x12',7,46),last);
});
test('both polarity states survive on whole cells, independent of display selection',()=>{
 for(const g of model.geometry)assert.deepEqual(Object.keys(g.polarityRoles),['positive','negative']);
 const p=foldedFibrationProcess(7,46);assert.equal(p.fibrationAudit.polarity.physicalGeometryDuplicated,false);
 assert.equal(Object.keys(p.fibrationAudit.polarity.bank).length,4);
 assert.equal(p.fibrationAudit.polarity.sheets.negative.exposedElectrons,71);
});
test('invalid return witness and out-of-range steps fail',()=>{
 const bad=structuredClone(model);bad.back.admissions[0].witnesses[0].face[0][0]+=100;
 assert.throws(()=>confirmFoldedRound(bad,'return',1),/Unconfirmed/);
 assert.throws(()=>foldedFibrationProcess(7,51));
});
