import test from 'node:test';
import assert from 'node:assert/strict';
import {buildCellFibration,cellFibrationProcess} from '../research/realization-tower/cell-fibration-process.mjs';
import {geometricCellLayer} from '../research/realization-tower/cell-fibration-cut.mjs';
import {esd7CellId} from '../research/realization-tower/esd7-cell-ids.mjs';
const before=cellFibrationProcess(7,4),after=cellFibrationProcess(7,5),growth=buildCellFibration().faceMiddleGrowth;
const key=ps=>ps.map(p=>p.join(',')).sort().join('|');
test('face 214 adds 22, 72, 91 from 9, 69, 96 as P',()=>{
 for(const [child,parent] of [[22,9],[72,69],[91,96]]){
  const g=growth.find(g=>esd7CellId(g.body.id)===child);assert.ok(g);
  assert.equal(esd7CellId(g.parent),parent);assert.equal(g.sourceRole,'electron');assert.equal(g.body.role,'proton');
  assert.deepEqual(g.face,[1,2,4]);
 }
});
test('step 5 also fills 134 and 165 from 138 and 171',()=>{
 for(const [child,parent] of [[134,138],[165,171]]){
  const g=growth.find(g=>esd7CellId(g.body.id)===child);
  assert.equal(esd7CellId(g.parent),parent);assert.equal(g.body.role,'proton');
  assert.equal(g.position,'edge-adjacent');assert.equal(g.witnesses.length,2);
 }
 const middle=growth.find(g=>esd7CellId(g.body.id)===148);
 assert.equal(esd7CellId(middle.parent),153);assert.equal(middle.body.role,'electron');
});
test('all face-middle and edge positions use adjacent triangles, with shared cells counted once',()=>{
 assert.equal(growth.length,24);
 assert.equal(growth.filter(g=>g.position==='face-middle').length,12);
 assert.equal(growth.filter(g=>g.position==='edge-adjacent').length,12);
 const faces=new Map(),swap={proton:'electron',electron:'proton',neutron:'neutron'};
 for(const g of growth){
  const parent=before.retainedBodies.find(b=>b.id===g.parent);assert.ok(parent);
  assert.equal(parent.kind,'tetrahedron');assert.equal(g.body.kind,'octahedron');
  assert.equal(geometricCellLayer(parent,g.source),2);assert.equal(geometricCellLayer(g.body,g.source),3);
  assert.equal(g.body.role,swap[parent.role]);assert.deepEqual(g.body.edgeSource,{cell:g.parent,role:parent.role,assignedRole:g.body.role,face:g.face,faces:g.faces,source:g.source});
  for(const w of g.witnesses){
   assert.equal(w.parent,g.parent);assert.equal(w.sourceRole,parent.role);
   assert.ok(parent.faces.some(f=>key(f)===key(w.sourceFace)));assert.ok(g.body.faces.some(f=>key(f)===key(w.surfaceFace)));
   const shared=w.surfaceFace.filter(v=>w.sourceFace.some(q=>key([q])===key([v])));assert.equal(shared.length,2);assert.equal(key(shared),key(w.sharedEdge));
   const face=w.face.join(',');faces.set(face,(faces.get(face)??0)+1);
  }
  assert.ok(!before.retainedBodies.some(b=>b.id===g.body.id));
 }
 assert.equal(faces.size,4);assert.ok([...faces.values()].every(n=>n===9));
});
test('step 5 preserves previous cells and adds twenty-four whole cells',()=>{
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(g=>g.id===b.id),b);
 assert.equal(new Set(after.retainedBodies.map(b=>b.id)).size,80);
 assert.deepEqual(after.cellFibrationAudit.counts.total,{proton:17,neutron:46,electron:17,total:80});
 assert.equal(after.retainedBodies.filter(b=>b.kind==='tetrahedron').length,40);
 assert.equal(after.emptyBodies.length,95);assert.equal(after.canAdvance,true);assert.equal(before.canAdvance,true);
});
