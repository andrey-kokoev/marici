import test from 'node:test';
import assert from 'node:assert/strict';
import {buildCellFibration,cellFibrationProcess} from '../research/realization-tower/cell-fibration-history.mjs';
import {foldedFibrationEnvelope,buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
import {processState} from '../research/realization-tower/normal-ray-processes.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const key=v=>JSON.stringify(v),model=buildCellFibration();
test('same folded carrier starts with four distinct original-colour corner cells',()=>{
 assert.deepEqual(model.envelope,foldedFibrationEnvelope);
 const s=cellFibrationProcess(7,0);assert.equal(s.retainedBodies.length,4);
 assert.deepEqual(s.cellFibrationAudit.counts.total,{proton:1,neutron:2,electron:1,total:4});
 assert.equal(s.canAdvance,true);assert.equal(s.cellFibrationAudit.growth.length,0);
});
test('each seed grows three actual whole cells through distinct vertices, in target colours',()=>{
 const native=new Map(buildFoldedFibration().geometry.map(g=>[g.id,g]));
 for(const corner of model.corners){
  const growth=model.growth.filter(g=>g.source===corner.vertex);
  assert.equal(growth.length,3);assert.equal(new Set(growth.map(g=>key(g.attachment))).size,3);
  for(const g of growth){
   const parent=native.get(g.parent),child=native.get(g.body.id);
   assert.equal(g.body.role,model.corners.find(c=>c.vertex===g.target).role);
   assert.deepEqual(g.body.vertices,child.vertices);assert.equal(child.kind,'tetrahedron');
   assert.deepEqual(child.vertices.filter(v=>parent.vertices.some(w=>key(v)===key(w))),[g.attachment]);
   assert.equal(g.body.polarityRoles,undefined); // not recoloured by the old sheet selector
  }
 }
 const s=processState('cell-fibration',7,1);
 assert.equal(new Set(s.retainedBodies.map(g=>g.id)).size,16);
 assert.deepEqual(s.retainedBodies.slice(0,4),cellFibrationProcess(7,0).retainedBodies);
 assert.deepEqual(s.cellFibrationAudit.counts.total,{proton:4,neutron:8,electron:4,total:16});
 assert.equal(s.canAdvance,true);assert.equal(s.fibrationAudit,undefined);
 assert.throws(()=>cellFibrationProcess(7,8),/Invalid/);
});
test('layer 2 extends every branch one unit in its source corner colour',()=>{
 const before=cellFibrationProcess(7,1),after=cellFibrationProcess(7,2);
 assert.deepEqual(after.retainedBodies.slice(0,16),before.retainedBodies);
 assert.equal(model.edgeGrowth.length,12);assert.equal(after.retainedBodies.length,40);
 for(const g of model.edgeGrowth){
  const prior=model.growth.find(p=>p.body.id===g.parent),source=model.corners.find(c=>c.vertex===g.source),target=model.corners.find(c=>c.vertex===g.target);
  const delta=target.point.map((x,i)=>(x-source.point[i])/7);
  const shape=vs=>vs.map(key).sort();
  assert.deepEqual(shape(g.body.vertices),shape(prior.body.vertices.map(v=>v.map((x,i)=>x+delta[i]))));
  assert.equal(g.body.role,source.role);assert.equal(prior.target,g.target);
  assert.deepEqual(g.body.vertices.filter(v=>prior.body.vertices.some(w=>key(v)===key(w))),[g.attachment]);
 }
 assert.deepEqual(after.cellFibrationAudit.counts.total,{proton:10,neutron:20,electron:10,total:40});
 assert.equal(after.canAdvance,true);assert.equal(new Set(after.retainedBodies.map(b=>b.id)).size,40);
});
test('same layer adds three face cells per corner, midway between edge cells and coloured opposite',()=>{
 assert.equal(model.faceGrowth.length,12);
 const center=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i],0)/vs.length);
 for(const corner of model.corners)assert.equal(model.faceGrowth.filter(g=>g.source===corner.vertex).length,3);
 for(const g of model.faceGrowth){
  assert.ok(g.face.includes(g.source));assert.ok(!g.face.includes(g.opposite));
  assert.equal(g.body.role,model.corners.find(c=>c.vertex===g.opposite).role);
  const parents=g.attachments.map(a=>model.edgeGrowth.find(p=>p.body.id===a.parent));
  const points=parents.map(p=>center(p.body.vertices));
  assert.deepEqual(center(g.body.vertices),points[0].map((x,i)=>(x+points[1][i])/2));
  for(const [i,a] of g.attachments.entries())assert.deepEqual(g.body.vertices.filter(v=>parents[i].body.vertices.some(w=>key(v)===key(w))),[a.point]);
  const facePoints=g.face.map(v=>model.corners.find(c=>c.vertex===v).point);
  const axis=facePoints[0].findIndex((x,i)=>facePoints.every(v=>v[i]===x));
  assert.ok(g.body.faces.some(f=>f.every(v=>v[axis]===facePoints[0][axis])));
 }
 assert.equal(cellFibrationProcess(7,2).cellFibrationAudit.growth.filter(g=>g.layer===2).length,24);
 assert.equal(cellFibrationProcess(7,1).cellFibrationAudit.growth.some(g=>g.kind==='face'),false);
});
test('layer 3 adds exactly six midpoint cells with explicit neighbour-pair colours',()=>{
 const before=cellFibrationProcess(7,2),after=cellFibrationProcess(7,3);
 assert.equal(model.midpointGrowth.length,6);assert.deepEqual(after.retainedBodies.slice(0,40),before.retainedBodies);
 const native=new Map(buildFoldedFibration().geometry.map(g=>[g.id,g]));
 const expected={'1-2':'electron','1-3':'proton','1-4':'electron','2-3':'neutron','2-4':'electron','3-4':'proton'};
 const center=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i],0)/vs.length);
 for(const g of model.midpointGrowth){
  assert.equal(g.body.role,expected[`${g.source}-${g.target}`]);
  assert.deepEqual(g.body.vertices,native.get(g.body.id).vertices);
  const parents=g.attachments.map(a=>native.get(a.parent));
  for(const [i,a] of g.attachments.entries())assert.deepEqual(g.body.vertices.filter(v=>parents[i].vertices.some(w=>key(v)===key(w))),[a.point]);
  const points=parents.map(p=>center(p.vertices));
  assert.deepEqual(center(g.body.vertices),points[0].map((x,i)=>(x+points[1][i])/2));
  assert.equal(g.word[1],{proton:'P',neutron:'N',electron:'E'}[g.body.role]);
 }
 assert.equal(new Set(model.midpointGrowth.map(g=>`${g.source}-${g.target}`)).size,6);
 assert.equal(new Set(after.retainedBodies.map(g=>g.id)).size,74);
 assert.deepEqual(after.cellFibrationAudit.counts.total,{proton:19,neutron:35,electron:20,total:74});
 assert.equal(after.canAdvance,true);
});
test('same layer 3 adds six cells per face in nearest-other-corner colours',()=>{
 assert.equal(model.faceCompletion.length,24);
 const native=new Map(buildFoldedFibration().geometry.map(g=>[g.id,g])),faces=new Map();
 for(const g of model.faceCompletion){
  const id=g.face.join(',');faces.set(id,(faces.get(id)??0)+1);
  assert.deepEqual(g.body.vertices,native.get(g.body.id).vertices);
  const point=g.body.vertices[0].map((_,i)=>g.body.vertices.reduce((s,v)=>s+v[i]/4,0));
  const candidates=model.corners.filter(c=>g.face.includes(c.vertex)&&c.vertex!==g.source);
  const d=c=>point.reduce((s,x,i)=>s+(x-c.point[i])**2,0);
  candidates.sort((a,b)=>d(a)-d(b));assert.ok(d(candidates[0])<d(candidates[1]));
  assert.equal(g.target,candidates[0].vertex);assert.equal(g.body.role,candidates[0].role);
  for(const a of g.attachments)assert.deepEqual(g.body.vertices.filter(v=>native.get(a.parent).vertices.some(w=>key(v)===key(w))),[a.point]);
  const corners=g.face.map(v=>model.corners.find(c=>c.vertex===v).point),axis=corners[0].findIndex((x,i)=>corners.every(v=>v[i]===x));
  assert.ok(g.body.faces.some(f=>f.every(v=>v[axis]===corners[0][axis])));
 }
 assert.equal(faces.size,4);assert.deepEqual([...faces.values()],[6,6,6,6]);
 const audit=cellFibrationProcess(7,3).cellFibrationAudit;
 assert.equal(audit.growth.filter(g=>g.layer===3).length,34);
 assert.equal(cellFibrationProcess(7,2).cellFibrationAudit.growth.some(g=>g.kind==='face-completion'),false);
});
test('layer 3 fills four same-orientation interior gaps in their source colours',()=>{
 const before=cellFibrationProcess(7,2),after=cellFibrationProcess(7,3),outer=new Set(buildFoldedFibration().outer.flatMap(f=>f.owners));
 assert.equal(model.interiorGrowth.length,4);
 for(const g of model.interiorGrowth){
  const corner=model.corners.find(c=>c.vertex===g.source),seed=model.seeds.find(b=>b.id===corner.cell);
  const delta=corner.point.map((x,i)=>model.corners.filter(c=>c!==corner).reduce((s,c)=>s+(c.point[i]-x)/7,0));
  assert.deepEqual(g.body.vertices.map(key).sort(),seed.vertices.map(v=>key(v.map((x,i)=>x+delta[i]))).sort());
  assert.equal(g.body.role,corner.role);assert.equal(outer.has(g.body.id),false);
  assert.equal(before.retainedBodies.some(b=>b.id===g.body.id),false);
  assert.ok(after.retainedBodies.some(b=>b.id===g.body.id));
 }
});
test('layer 4 resolves two proposals per shared cell with P > N > E',()=>{
 const before=cellFibrationProcess(7,3),after=cellFibrationProcess(7,4);
 assert.deepEqual(after.retainedBodies.slice(0,74),before.retainedBodies);assert.equal(model.sharedInterior.length,6);
 const rank={proton:2,neutron:1,electron:0};
 for(const g of model.sharedInterior){
  assert.equal(g.proposals.length,2);assert.equal(new Set(g.proposals.map(p=>p.source)).size,2);
  assert.equal(rank[g.body.role],Math.max(...g.proposals.map(p=>rank[p.role])));
  const point=g.body.vertices[0].map((_,i)=>g.body.vertices.reduce((s,v)=>s+v[i]/4,0));
  for(const p of g.proposals){
   const other=model.corners.filter(c=>c.vertex!==p.source),distance=c=>point.reduce((s,x,i)=>s+(x-c.point[i])**2,0);
   other.sort((a,b)=>distance(a)-distance(b));assert.equal(p.target,other[0].vertex);assert.equal(p.role,other[0].role);
   assert.ok(distance(other[0])<distance(other[1]));
  }
 }
 assert.deepEqual(model.sharedInterior.map(g=>g.body.role).sort(),['neutron','neutron','neutron','proton','proton','proton']);
 assert.equal(new Set(after.retainedBodies.map(g=>g.id)).size,80);
 assert.deepEqual(after.cellFibrationAudit.counts.total,{proton:22,neutron:38,electron:20,total:80});
});
test('layer 5 fills the unique remaining tetrahedron per face in its opposite colour',()=>{
 const before=cellFibrationProcess(7,4),after=cellFibrationProcess(7,5),native=buildFoldedFibration().geometry;
 assert.equal(after.cellFibrationAudit.layer,5);assert.equal(model.faceCenters.length,4);
 assert.deepEqual(after.retainedBodies.slice(0,80),before.retainedBodies);
 const occupied=new Set(before.retainedBodies.map(g=>g.id));
 for(const g of model.faceCenters){
  assert.ok(!g.face.includes(g.opposite));assert.equal(g.body.role,model.corners.find(c=>c.vertex===g.opposite).role);
  const points=g.face.map(v=>model.corners.find(c=>c.vertex===v).point),axis=points[0].findIndex((x,i)=>points.every(v=>v[i]===x));
  const remaining=native.filter(b=>b.kind==='tetrahedron'&&!occupied.has(b.id)&&b.faces.some(f=>f.every(v=>v[axis]===points[0][axis])));
  assert.deepEqual(remaining.map(b=>b.id),[g.body.id]);assert.deepEqual(g.body.vertices,remaining[0].vertices);
  assert.ok(g.attachments.length>0);
 }
 assert.equal(new Set(after.retainedBodies.map(g=>g.id)).size,84);
 assert.deepEqual(after.cellFibrationAudit.counts.total,{proton:23,neutron:40,electron:21,total:84});
 assert.deepEqual(after.history.map(h=>h.layer),[0,1,2,3,4,5]);assert.equal(after.canAdvance,true);
});
test('new process has independently bounded persistence',()=>{
 const saved=normalizeSceneSettings({process:{id:'cell-fibration',k:1,step:99,progress:{'fibration-12x12':{k:7,step:50}}}});
 assert.equal(saved.process.k,7);assert.equal(saved.process.step,14);assert.equal(saved.process.progress['fibration-12x12'].step,50);
});
