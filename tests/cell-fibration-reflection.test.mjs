import test from 'node:test';
import assert from 'node:assert/strict';
import {buildCellFibration,cellFibrationProcess} from '../research/realization-tower/cell-fibration-process.mjs';
import {buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
import {applyCellFibrationCut,geometricCellLayer} from '../research/realization-tower/cell-fibration-cut.mjs';
import {innerLayerHexReflection} from '../research/realization-tower/inner-layer-hex-reflection.mjs';
const model=buildCellFibration(),before=cellFibrationProcess(7,3),after=cellFibrationProcess(7,4),geometry=buildFoldedFibration().geometry;
const key=ps=>ps.map(p=>p.join(',')).sort().join('|');
const byId=new Map(before.retainedBodies.map(b=>[b.id,b]));
test('each inward layer-2 hexagon has three filled triangles opposite three empty octahedra',()=>{
 assert.equal(model.hexReflectionGrowth.length,12);
 for(const source of model.corners){
  const entries=model.hexReflectionGrowth.filter(g=>g.source===source.vertex);
  assert.equal(entries.length,3);
  const triangles=[];
  for(const g of entries){
   assert.equal(g.body.kind,'octahedron');assert.equal(g.hexWitnesses.length,1);
   assert.equal(geometricCellLayer(g.body,source.vertex),2);assert.ok(!byId.has(g.body.id));
   const w=g.hexWitnesses[0],opposite=byId.get(w.oppositeCell);
   assert.equal(w.view,'inside-layer-2');assert.equal(geometricCellLayer(opposite,source.vertex),2);
   assert.ok(g.body.faces.some(f=>key(f)===key(w.triangle)));
   assert.ok(opposite.faces.some(f=>key(f)===key(w.oppositeTriangle)));
   assert.equal(key(w.triangle.map(p=>p.map((x,i)=>2*w.hexCenter[i]-x))),key(w.oppositeTriangle));
   assert.equal(g.body.role,['electron','proton'].includes(opposite.role)?'neutron':opposite.role);assert.equal(w.role,opposite.role);assert.equal(w.assignedRole,g.body.role);
   assert.ok([...w.triangle,...w.oppositeTriangle].every(p=>p[w.axis]===w.plane));
   assert.ok(w.plane!==source.point[w.axis]);
   assert.ok(w.plane!==model.corners.find(c=>c!==source).point[w.axis]);
   triangles.push(w.triangle,w.oppositeTriangle);
  }
  assert.equal(new Set(triangles.map(key)).size,6);
  assert.equal(new Set(entries.map(g=>key([g.hexWitnesses[0].hexCenter]))).size,1);
 }
});
test('inner hexagons preserve earlier layer-1/2 cells without admitting layer 3',()=>{
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(g=>g.id===b.id),b);
 assert.deepEqual(after.cellFibrationAudit.counts.total,{proton:11,neutron:34,electron:11,total:56});
 assert.equal(after.retainedBodies.length,56);assert.equal(new Set(after.retainedBodies.map(g=>g.id)).size,56);
 assert.equal(after.retainedBodies.filter(g=>g.kind==='tetrahedron').length,40);
 assert.equal(after.retainedBodies.filter(g=>g.kind==='octahedron').length,16);
 assert.equal(after.conflictBodies.length,0);assert.equal(after.cellFibrationAudit.unresolvedOctahedra.length,0);
 assert.equal(after.canAdvance,true);assert.equal(before.canAdvance,true);
 const additions=new Map(model.hexReflectionGrowth.map(g=>[g.body.id,g]));
 assert.equal(additions.get('oct-1.5,-2.5,0.5,1.5').body.role,'neutron');
 assert.equal(model.hexReflectionGrowth.filter(g=>g.hexWitnesses[0].role==='electron'&&g.body.role==='neutron').length,3);
 assert.equal(model.hexReflectionGrowth.filter(g=>g.hexWitnesses[0].role==='proton'&&g.body.role==='neutron').length,3);
 assert.ok(model.hexReflectionGrowth.every(g=>g.body.role==='neutron'));
 assert.equal(additions.get('oct-1.5,-2.5,0.5,1.5').hexWitnesses[0].oppositeCell,'tet-101');
 assert.equal(additions.get('oct-0.5,-2.5,1.5,1.5').body.role,'neutron');
 assert.equal(additions.get('oct-0.5,-2.5,1.5,1.5').hexWitnesses[0].oppositeCell,'tet-84');
});
test('inner reflection is independent of enumeration order',()=>{
 const normalize=r=>r.agreed.map(g=>[g.cell.id,g.role,g.hexWitnesses[0].oppositeCell]).sort((a,b)=>a[0].localeCompare(b[0]));
 assert.deepEqual(normalize(innerLayerHexReflection([...geometry].reverse(),[...before.retainedBodies].reverse(),[...model.corners].reverse())),normalize(innerLayerHexReflection(geometry,before.retainedBodies,model.corners)));
});
test('layer-2 cuts contain all twelve newly filled octahedra',()=>{
 for(const showEmpty of [false,true]){
  const cut=applyCellFibrationCut(after,{enabled:true,vertex:'all',startLayer:2,layer:2,showEmpty});
  assert.equal(cut.retainedBodies.length,36);assert.equal(cut.conflictBodies.length,0);assert.equal(cut.cutAudit.emptyCount,0);assert.equal(cut.cutAudit.wireframeCount,0);
 }
 for(let vertex=1;vertex<=4;vertex++){
  const cut=applyCellFibrationCut(after,{enabled:true,vertex,startLayer:2,layer:2,showEmpty:true});
  assert.equal(cut.retainedBodies.length,9);assert.equal(cut.retainedBodies.filter(g=>g.layer===4).length,3);
 }
});
