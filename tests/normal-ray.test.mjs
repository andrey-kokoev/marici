import test from 'node:test';
import assert from 'node:assert/strict';
import {useViewerModel} from '../examples/normal-ray/useViewerModel.js';
import {sceneSettingsKey,loadSceneSettings} from '../examples/normal-ray/settings.js';
import {seed,apex,cells} from '../research/realization-tower/normal-ray-model.mjs';
import {cornerRay,edgeProbe,edgeDirection,secondEdgeRay,thirdEdgeRay,exteriorFaceNeighbors,oppositePartners,interiorNeutronRound,localFaceVertexComparisons} from '../research/realization-tower/edge-ray-model.mjs';
import {procedureState} from '../research/realization-tower/normal-ray-procedure.mjs';
import {particleCounts} from '../research/realization-tower/particle-counts.mjs';
import {fillRayDiamonds} from '../research/realization-tower/ray-diamond-pattern.mjs';
function assertRayDiamonds(before,after,ray,domain,codomain){
 assert.deepEqual(ray.blockedDiamonds,[]);
 const members=new Set();
 for(const d of ray.diamonds){
  assert.equal(d.sharedFace.length,3);assert.equal(after.assignments.find(a=>a.cell===d.domain).role,domain);assert.equal(after.assignments.find(a=>a.cell===d.codomain).role,codomain);
  members.add(d.domain);members.add(d.codomain);
  const index=ray.contacts.findIndex(c=>c.cell===d.codomain);
  if(index+1<ray.contacts.length)assert.equal(after.assignments.find(a=>a.cell===ray.contacts[index+1].cell).role,'neutron');
 }
 for(const a of after.assignments.filter(a=>!before.assignments.some(b=>b.cell===a.cell)&&a.boundary.startsWith(`${ray.id}-`)&&a.role!=='neutron'))assert(members.has(a.cell));
}
test('straight ray along a seed edge, not a triangle path',()=>{
 assert(seed.vertices.some(p=>p.every((x,i)=>x===apex[i]+edgeDirection[i])));
 for(let k=1;k<=7;k++){
  const p=edgeProbe(k);assert.equal(p.linePoints.length,2);
  assert.deepEqual(p.point,apex.map((x,i)=>x+k*edgeDirection[i]));
  assert(p.linePoints.every(v=>v[1]===2));
  assert.equal(p.polygons.length,k*k);
  assert.equal(p.point[p.plane.coordinate],p.plane.value);
  assert(p.polygons.flat().every(v=>Math.abs(v[p.plane.coordinate]-p.plane.value)<1e-9));
 }
});
test('k1 seed unchanged; ending shape occupies the growing tetrahedron corner at every k',()=>{
 const first=procedureState(1,2);assert.deepEqual(first.assignments,[]);assert.equal(first.end.id,seed.id);
 const next=procedureState(2,2);assert.deepEqual(next.assignments.map(a=>a.role),['electron','proton']);assert.notEqual(next.end.id,seed.id);
 const shared=seed.vertices.filter(p=>next.end.vertices.some(q=>p.every((x,i)=>x===q[i])));assert.equal(shared.length,1);
 assert.equal(next.end.id,132);
 assert(next.end.vertices.some(p=>p.every((x,i)=>x===next.probe.point[i])));
 for(let k=3;k<=7;k++){
  const later=procedureState(k,2);
  assert.deepEqual(later.assignments.map(a=>a.role),['electron','proton']);
  assert.equal(later.assignments[1].cell,later.end.id);
  assert(later.end.vertices.some(p=>p.every((x,i)=>x===later.probe.point[i])));
  assert(later.end.vertices.every(p=>p[0]<=-5+k));
  assert(edgeProbe(k-1).traversed.every(id=>later.probe.traversed.includes(id)));
  assert(later.assignments.every(a=>later.probe.traversed.includes(a.cell)));
 }
});
test('second ray follows either remaining corner edge for k units on the support plane',()=>{
 for(let k=1;k<=7;k++)for(const branch of [1,3]){
  const first=edgeProbe(k),r=secondEdgeRay(k,branch),p=procedureState(k,3,branch);
  assert.deepEqual(r.start,first.point);
  // The first edge includes contact-only cells too, not just k corner cells.
  if(k>=2)assert(first.traversed.length>k);
  assert(first.traversed.every(id=>cells[id].vertices.some(v=>{
   const t=v[0]-apex[0];return t>=0&&t<=k&&v.every((x,i)=>x===apex[i]+t*edgeDirection[i]);
  })));
  assert.deepEqual(r.end,r.start.map((x,i)=>x+k*r.direction[i]));
  assert.equal(r.end[0],first.plane.value);
  assert(first.end.vertices.some(v=>v.every((x,i)=>x===r.start[i]+r.direction[i])));
  assert.deepEqual(p.secondRay,r);
  assert(r.contacts.some(c=>c.cell===first.end.id));assert(r.contacts.some(c=>c.cell===r.cell));
  assert(r.contacts.every(c=>c.interval[0]>=-1e-9&&c.interval[1]<=1+1e-9));
  if(k>=2)assert(r.contacts.some(c=>c.cell!==first.end.id&&c.cell!==r.cell));
  assert.deepEqual(p.assignments.filter(a=>a.role!=='neutron'),procedureState(k,2).assignments);
  assert.deepEqual(p.assignments.filter(a=>a.role==='neutron').map(a=>a.cell),[r.cell]);
 }
 const m=useViewerModel();m.move(3);assert.equal(m.process.step,3);m.process.branch=3;
 assert.equal(m.state.value.secondRay.branch,3);m.process.k=4;assert.equal(m.process.step,3);assert.equal(m.state.value.secondRay.length,4);
 m.move(-1);assert.equal(m.state.value.secondRay,null);
});
test('six steps trace E-P-N-N-P-E in the requested order',()=>{
 for(let k=1;k<=7;k++)for(const branch of [1,3]){
  const second=secondEdgeRay(k,branch),third=thirdEdgeRay(k,branch);
  const expected=[[second.start,second.end],[second.end,third.end],[third.end,second.start],[second.start,apex]];
  for(let step=3;step<=6;step++){
   const p=procedureState(k,step,branch);
   assert.deepEqual(p.rays.map(r=>[r.start,r.end]),expected.slice(0,step-2));
   for(const r of p.rays){
    assert.equal(r.length,k);assert.deepEqual([...r.direction].sort((a,b)=>a-b),[-1,0,0,1]);
    assert.deepEqual(r.end,r.start.map((x,i)=>x+k*r.direction[i]));
    assert(r.contacts.some(c=>c.cell===r.cell));
   }
   assert.deepEqual(p.assignments.filter(a=>a.role==='neutron').map(a=>a.cell),[second.cell,...(step>=4?[third.cell]:[])]);
   assert.deepEqual(p.rays.slice(0,-1),procedureState(k,step-1,branch).rays);
  }
 }
 const m=useViewerModel();m.move(6);assert.equal(m.process.step,6);assert(m.state.value.closingRay);
 m.move(-1);assert.equal(m.state.value.closingRay,null);assert(m.state.value.returnRay);
});
test('step 7 assigns reciprocal opposite partners with exactly one opposite face-neighbor',()=>{
 assert.deepEqual(exteriorFaceNeighbors(1),[]);
 for(let k=2;k<=7;k++){
  const previous=procedureState(k,6),current=procedureState(k,7),neighbors=exteriorFaceNeighbors(k);
  assert.equal(neighbors.length,2);assert.deepEqual(current.faceNeighbors,neighbors);
  assert.deepEqual(current.assignments.slice(0,-2),previous.assignments);assert.deepEqual(current.rays,previous.rays);
  assert.equal(current.partners.length,4);
  for(const pair of current.partners)assert(current.partners.some(p=>p.cell===pair.partner&&p.partner===pair.cell));
  assert.throws(()=>oppositePartners(previous.assignments),/exactly one/);
  for(const n of neighbors){
   const cell=cells[n.cell],corner=cells[n.corner],same=(p,q)=>p.every((x,i)=>x===q[i]);
   assert.equal(cell.vertices.filter(p=>corner.vertices.some(q=>same(p,q))).length,3);
   assert.equal(n.sharedFace.length,3);assert(n.exteriorFaces.length>0);
   for(const f of n.exteriorFaces){assert.equal(f.vertices.length,3);assert(f.vertices.every(p=>p[f.coordinate]===f.value));}
   assert.equal(current.assignments.find(a=>a.cell===n.cell).role,n.role==='electron'?'proton':'electron');
  }
 }
 assert.deepEqual(exteriorFaceNeighbors(7).map(n=>[n.role,n.cell]),[['electron',341],['proton',155]]);
});
test('step 8 assigns N across the two remaining faces of each paired cell',()=>{
 assert.deepEqual(procedureState(1,8).neutronNeighbors,[]);
 for(let k=2;k<=7;k++)for(const branch of [1,3]){
  const before=procedureState(k,7,branch),after=procedureState(k,8,branch);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.partners,before.partners);assert.deepEqual(after.rays,before.rays);
  assert.equal(after.neutronNeighbors.length,4);
  assert.equal(new Set(after.neutronNeighbors.map(n=>n.cell)).size,k===2?2:4);
  for(const pair of after.faceNeighbors)assert.equal(after.neutronNeighbors.filter(n=>n.owner===pair.cell).length,2);
  for(const n of after.neutronNeighbors){
   assert.equal(n.sharedFace.length,3);
   assert.equal(after.assignments.filter(a=>a.cell===n.cell).length,1);
   assert.equal(after.assignments.find(a=>a.cell===n.cell).role,'neutron');
  }
 }
});
test('step 9 assigns surface-edge neighbors, distinct from interior face-neighbors',()=>{
 assert.deepEqual(procedureState(1,9).surfaceNeutronNeighbors,[]);
 for(let k=2;k<=7;k++)for(const branch of [1,3]){
  const before=procedureState(k,8,branch),after=procedureState(k,9,branch);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.partners,before.partners);assert.deepEqual(after.rays,before.rays);
  assert.equal(after.surfaceNeutronNeighbors.length,4);
  for(const paired of after.faceNeighbors)assert.equal(after.surfaceNeutronNeighbors.filter(n=>n.owner===paired.cell).length,2);
  for(const n of after.surfaceNeutronNeighbors){
   assert.equal(n.sharedEdge.length,2);assert.equal(n.surfaceFace.length,3);
   assert(n.surfaceFace.every(v=>v[n.coordinate]===n.value));
   assert.equal(cells[n.cell].vertices.filter(p=>cells[n.owner].vertices.some(q=>p.every((x,i)=>x===q[i]))).length,2);
   assert(!after.neutronNeighbors.some(f=>f.cell===n.cell));
   assert.equal(after.assignments.filter(a=>a.cell===n.cell).length,1);
   assert.equal(after.assignments.find(a=>a.cell===n.cell).role,'neutron');
  }
  if(k===2)assert.deepEqual(after.assignments,before.assignments);
 }
 assert.deepEqual(procedureState(7,9).surfaceNeutronNeighbors.map(n=>n.cell),[131,133,66,73]);
});
test('interior closure is a recurring, simultaneous two-face attachment rule',()=>{
 for(let k=1;k<=7;k++)for(const branch of [1,3]){
  let before=procedureState(k,9,branch),step=10;
  do{
   const expected=interiorNeutronRound(k,before.assignments),after=procedureState(k,step,branch),known=new Set(before.assignments.map(a=>a.cell));
   assert.deepEqual(interiorNeutronRound(k,[...before.assignments].reverse()).map(c=>c.cell),expected.map(c=>c.cell));
   assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
   assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>a.cell),expected.map(c=>c.cell));
   for(const c of expected){
    assert(c.supports.length>=2);assert(c.supports.every(s=>known.has(s.cell)&&s.face.length===3));
    assert(cells[c.cell].vertices.every(p=>p[0]<=-5+k));
    assert(![0,1,2,3].some(i=>cells[c.cell].vertices.filter(p=>p[i]===(i===0?-5+k:2)).length===3));
    assert.equal(after.assignments.find(a=>a.cell===c.cell).role,'neutron');
   }
   assert.deepEqual(after.partners,before.partners);before=after;step++;
   assert(step<30);
  }while(before.nextClosure.length);
 }
 assert(procedureState(4,10).closureRounds[0].some(c=>c.cell===313));
 assert.equal(procedureState(3,10).nextClosure.length,1);
 const m=useViewerModel();m.process.k=3;m.move(10);assert.equal(m.process.step,10);assert(m.canAdvance.value);
 m.move(1);assert.equal(m.process.step,11);assert(m.canAdvance.value);m.move(1);assert.equal(m.process.step,12);assert(!m.canAdvance.value);
 m.move(-1);assert(m.canAdvance.value);
});
test('local face/vertex step assigns opposite roles without overwriting existing roles',()=>{
 for(let k=2;k<=7;k++){
  let step=10,before=procedureState(k,step);while(before.nextClosure.length)before=procedureState(k,++step);
  const after=procedureState(k,step+1);assert(after.comparisonVisible);assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);assert.deepEqual(after.partners,before.partners);
  for(const c of after.faceVertexComparisons){
   const other=c.corners.filter(v=>!v.every((x,i)=>x===c.oppositeVertex[i]));
   const midpoints=[[0,1],[0,2],[1,2]].map(([a,b])=>other[a].map((x,i)=>(x+other[b][i])/2));
   assert(c.face.every(p=>midpoints.some(q=>p.every((x,i)=>x===q[i]))));
   assert(cells[c.cell].vertices.some(p=>p.every((x,i)=>x===c.oppositeVertex[i])));
   assert.equal(c.role,c.ownerRole==='proton'?'electron':'proton');
   if(c.status==='assigned')assert.equal(after.assignments.find(a=>a.cell===c.cell).role,c.role);
  }
 }
 const s=procedureState(4,10),cs=localFaceVertexComparisons(4,s.assignments);
 assert.deepEqual(cs.map(c=>[c.owner,c.cell,c.role,c.status]),[[341,132,'electron','candidate'],[311,127,'proton','candidate']]);
 assert(cs.every(c=>c.facePartners.length===0));
 assert(procedureState(2,11).faceVertexComparisons.every(c=>c.status==='conflict'));
 assert(procedureState(3,12).faceVertexComparisons.every(c=>c.status==='conflict'));
});
test('next step constructs bidirectional N mediation through actual shared faces',()=>{
 for(let k=4;k<=7;k++)for(const branch of [1,3]){
  const before=procedureState(k,11,branch),after=procedureState(k,12,branch),m=after.mediation;
  assert(before.mediationAvailable);assert.equal(before.mediation,null);assert(after.mediationVisible&&m.connected);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(m.reversePaths,m.paths.map(p=>[...p].reverse()));
  for(const w of m.witnesses){
   assert.equal(after.assignments.find(a=>a.cell===w.path[0]).role,'electron');
   assert.equal(after.assignments.find(a=>a.cell===w.path.at(-1)).role,'proton');
   assert(w.path.slice(1,-1).every(id=>after.assignments.find(a=>a.cell===id)?.role==='neutron'));
   assert(w.faces.every(f=>f.vertices.length===3));
  }
  if(k===4){assert.equal(m.paths.length,2);assert.deepEqual(m.fillerCells,[331,332,333,334]);}
 }
 const model=useViewerModel();model.process.k=4;model.move(11);assert(model.canAdvance.value);
 model.move(1);assert.equal(model.process.step,12);assert(model.canAdvance.value);assert(model.state.value.mediation);
 model.move(1);assert.equal(model.process.step,13);assert(model.canAdvance.value);
 model.move(1);assert.equal(model.process.step,14);assert(!model.canAdvance.value);
});
test('k4 step 13 applies the same two-face interior closure after mediation',()=>{
 for(const branch of [1,3]){
  const before=procedureState(4,12,branch),after=procedureState(4,13,branch);
  assert.deepEqual(before.nextClosure.map(c=>c.cell),[58,60]);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[[58,'neutron'],[60,'neutron']]);
  assert.deepEqual(after.postMediationRounds[0].map(c=>c.supports.map(s=>s.cell).sort((a,b)=>a-b)),[[313,331],[333,339]]);
  assert.deepEqual(after.nextClosure,[]);assert.deepEqual(after.mediation,before.mediation);
 }
});
test('surface continuation branches sideways with two opposite-role cells on each face',()=>{
 for(let k=4;k<=7;k++)for(const branch of [1,3]){
  const before=procedureState(k,13,branch),after=procedureState(k,14,branch);
  assert(before.surfaceContinuationAvailable);assert(!before.surfaceContinuationVisible);assert(after.surfaceContinuationVisible);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  const additions=after.assignments.slice(before.assignments.length);
  assert.equal(additions.length,4);assert.deepEqual(additions.map(a=>a.role),['electron','electron','proton','proton']);
  assert.deepEqual(after.surfaceContinuations.map(c=>c.coordinate),[2,2,0,0]);
  for(const c of after.surfaceContinuations){assert.equal(c.face.length,3);assert(c.sharedVertex);assert(c.face.every(p=>p[c.coordinate]===c.value));}
  if(k===4){
   assert.deepEqual(additions.map(a=>a.cell),[329,337,307,319]);
   assert(!after.assignments.some(a=>[128,26].includes(a.cell)));
  }
 }
});
test('process selection isolates the fresh construction and preserves experimental progress',()=>{
 const m=useViewerModel({processId:'new-construction'});m.process.k=4;
 assert(m.canAdvance.value);assert.deepEqual(m.state.value.assignments.map(a=>a.role),['electron']);
 m.move(4);assert.equal(m.process.step,4);assert(m.canAdvance.value);
 const newAssignments=m.state.value.assignments;
 m.selectProcess('edge-ray');m.move(14);assert.equal(m.process.step,14);
 const saved=m.state.value.assignments;
 m.selectProcess('new-construction');assert.equal(m.process.step,4);assert.deepEqual(m.state.value.assignments,newAssignments);m.process.k=2;
 m.selectProcess('edge-ray');assert.equal(m.process.k,4);assert.equal(m.process.step,14);assert.deepEqual(m.state.value.assignments,saved);
 m.selectProcess('new-construction');assert.equal(m.process.k,2);assert.equal(m.renderState.value.processId,'new-construction');
 assert.throws(()=>m.selectProcess('unknown'));
});
test('new process casts 13, 32, then 21 with immediate endpoint roles',()=>{
 for(let k=1;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;
  assert.equal(m.state.value.firstRay,null);assert.deepEqual(m.state.value.assignments.map(a=>a.role),['electron']);
  m.move(1);const first=m.state.value;assert.equal(first.firstRay.id,'ray13');assert.equal(first.firstRay.length,k);assert.deepEqual(first.rays,[]);
  assert.deepEqual(first.assignments.map(a=>a.role),k===1?['electron']:['electron','proton']);
  m.move(1);const next=m.state.value;assert.deepEqual(next.rays.map(r=>r.id),['ray32']);
  assert.deepEqual(next.rays[0].start,first.firstRay.end);
  const apex=first.firstRay.start;
  assert.deepEqual(next.rays[0].end,apex.map((x,i)=>x+(i===0?k:i===1?-k:0)));
  assert.equal(next.rays[0].length,k);
  assert.deepEqual(next.assignments.map(a=>a.role),k===1?['electron']:['electron','proton','neutron']);
  assert(m.canAdvance.value);m.move(1);const closed=m.state.value;
  assert.deepEqual(closed.rays.map(r=>r.id),['ray32','ray21']);
  assert.deepEqual(closed.rays[1].start,next.rays[0].end);assert.deepEqual(closed.rays[1].end,apex);assert.equal(closed.rays[1].length,k);
  assert.deepEqual(closed.assignments,next.assignments);assert(m.canAdvance.value);
  m.move(-1);assert.deepEqual(m.state.value,next);m.move(-1);assert.deepEqual(m.state.value,first);
 }
});
test('opposing edge fronts fill E/P halves and N at their meeting',()=>{
 for(let k=2;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;m.move(3);
  const before=m.state.value;m.move(1);const after=m.state.value;
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.edgeFronts.map(r=>r.id),['ray13','ray31']);
  assert(after.edgeFronts.every(r=>r.length===k/2));assert.deepEqual(after.edgeFronts[0].end,after.edgeFronts[1].end);
  assert.equal(after.edgeMeeting.cells.length,k%2===0?4:1);
  assert(after.edgeMeeting.cells.every(id=>after.assignments.find(a=>a.cell===id)?.role==='neutron'));
  const edge=after.firstRay.contacts.filter(c=>c.interval[1]-c.interval[0]>1e-9).sort((a,b)=>a.interval[0]-b.interval[0]);
  assert.equal(edge.length,k);
  assert.deepEqual(edge.map(c=>after.assignments.find(a=>a.cell===c.cell).role),Array.from({length:k},(_,i)=>i<Math.floor(k/2)?'electron':i>=Math.ceil(k/2)?'proton':'neutron'));
  if(k===4)assert.deepEqual([...after.edgeMeeting.cells].sort((a,b)=>a-b),[331,332,333,334]);
  assert.equal(m.canAdvance.value,k>=3);m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('new step 5 adds unique exterior-facing opposite corner partners without overwrites',()=>{
 for(let k=1;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;m.move(4);
  const before=m.state.value;
  if(k<3){assert(!m.canAdvance.value);continue;}
  m.move(1);const after=m.state.value;
  assert.equal(m.process.step,5);assert(m.canAdvance.value);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>a.role),['proton','electron']);
  assert.equal(after.faceNeighbors.length,2);
  for(const n of after.faceNeighbors){assert.equal(n.sharedFace.length,3);assert(n.exteriorFaces.length>0);assert(n.exteriorFaces.every(f=>f.vertices.length===3));}
  if(k===4)assert.deepEqual(after.faceNeighbors.map(n=>n.cell),[341,311]);
  m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('new process builds the same face and surface supports as Process 1 before interior closure',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;m.move(5);
  const before=m.state.value;m.move(1);const faces=m.state.value;
  assert.equal(m.process.step,6);assert(m.canAdvance.value);
  assert.deepEqual(faces.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(faces.neutronNeighbors,procedureState(k,8).neutronNeighbors);
  assert.deepEqual(faces.assignments.slice(before.assignments.length).map(a=>a.role),Array(4).fill('neutron'));
  m.move(1);const surface=m.state.value;
  assert.deepEqual(surface.surfaceNeutronNeighbors,procedureState(k,9).surfaceNeutronNeighbors);
  assert.deepEqual(surface.assignments.slice(faces.assignments.length).map(a=>a.role),Array(4).fill('neutron'));
  assert.deepEqual(surface.nextClosure,interiorNeutronRound(k,surface.assignments));
  m.move(1);const closed=m.state.value;
  assert.deepEqual(closed.closureRounds[0],surface.nextClosure);
  for(const c of closed.closureRounds[0]){
   assert(c.supports.length>=2);
   assert(c.supports.every(s=>s.face.length===3&&surface.assignments.some(a=>a.cell===s.cell)));
  }
  if(k===4){
   assert(!surface.assignments.some(a=>[313,339].includes(a.cell)));
   assert.deepEqual(closed.closureRounds[0].map(c=>c.cell),[313,339]);
   assert.deepEqual(closed.nextClosure.map(c=>c.cell),[58,60]);
  }
  m.move(-1);assert.deepEqual(m.state.value,surface);
  m.move(100);assert(!m.canAdvance.value);assert.deepEqual(m.state.value.nextClosure,[]);assert.deepEqual(m.state.value.nextPatternClosure,[]);
 }
});
test('meeting rays propagate over both surfaces and fill every crossed triangle N',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;m.move(7);
  while(!m.state.value.surfacePropagationAvailable){assert(m.process.step<10);m.move(1);}
  const before=m.state.value;assert(!before.surfacePropagationVisible);m.move(1);const after=m.state.value;
  assert(after.surfacePropagationVisible);assert(m.canAdvance.value);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.surfaceRays.map(r=>r.id),['meeting-to-V2','meeting-to-V4']);
  for(const ray of after.surfaceRays){
   assert.deepEqual(ray.start,before.edgeMeeting.point);assert(ray.start[ray.coordinate]===2&&ray.end[ray.coordinate]===2);
   let covered=0;
   for(const contact of ray.surfaceCells){
    assert.equal(contact.face.length,3);assert(contact.face.every(p=>p[ray.coordinate]===2));
    assert(contact.interval[1]-contact.interval[0]>1e-9);assert(contact.interval[0]<=covered+1e-9);covered=Math.max(covered,contact.interval[1]);
    assert.equal(after.assignments.find(a=>a.cell===contact.cell).role,'neutron');
   }
   assert(Math.abs(covered-1)<1e-9);
  }
  const crossed=new Set(after.surfaceRays.flatMap(r=>r.surfaceCells.map(c=>c.cell)));
  assert(after.assignments.slice(before.assignments.length).every(a=>a.role==='neutron'&&crossed.has(a.cell)));
  if(k===4){assert.equal(m.process.step,10);assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>a.cell).sort((a,b)=>a-b),[116,126,129,304,326]);}
  m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('opposing V2/V4 rays fill the complete base edge N',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;m.move(7);
  while(!m.state.value.surfacePropagationVisible){assert(m.process.step<11);m.move(1);}
  const before=m.state.value;m.move(1);const after=m.state.value;
  assert(after.baseEdgeVisible);assert(m.canAdvance.value);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.baseEdgeRays.map(r=>r.id),['ray24','ray42']);
  const [a,b]=after.baseEdgeRays;
  assert.deepEqual(a.start,before.surfaceRays[0].end);assert.deepEqual(b.start,before.surfaceRays[1].end);
  assert.deepEqual(a.end,b.end);assert.deepEqual(a.end,a.start.map((x,i)=>(x+b.start[i])/2));
  assert(a.length===k/2&&b.length===k/2);
  const traversed=cornerRay(k,a.start,b.start).contacts.filter(c=>c.interval[1]-c.interval[0]>1e-9);
  assert.equal(traversed.length,k);assert(traversed.every(c=>after.assignments.some(x=>x.cell===c.cell&&x.role==='neutron')));
  assert(after.assignments.slice(before.assignments.length).every(x=>traversed.some(c=>c.cell===x.cell)));
  if(k===4)assert.equal(m.process.step,11);
  m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('ray34 and mirrored ray14 run in separate reversible steps',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;m.move(7);
  while(!m.state.value.baseEdgeVisible){assert(m.process.step<12);m.move(1);}
  const before=m.state.value;m.move(1);const first=m.state.value;
  assert(first.ray34Visible);assert(!first.ray14Visible);assert.equal(first.ray14,null);assert.deepEqual(first.edge14Assignments,[]);assert(m.canAdvance.value);
  if(k===4){assert.equal(m.process.step,12);assert.deepEqual(first.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[[308,'proton'],[117,'electron']]);}
  m.move(1);const after=m.state.value;
  assert(after.ray14Visible);assert(m.canAdvance.value);
  assert.deepEqual(after.assignments.slice(0,first.assignments.length),first.assignments);
  assert.deepEqual(after.ray34.start,before.firstRay.end);assert.deepEqual(after.ray34.end,before.surfaceRays[1].end);
  assert.equal(after.ray34.length,k);assert.equal(after.ray34.contacts.length,k);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assertRayDiamonds(before,first,first.ray34,'proton','electron');
  assert.deepEqual(after.ray14.start,before.firstRay.start);assert.deepEqual(after.ray14.end,after.ray34.end);
  assertRayDiamonds(first,after,after.ray14,'electron','proton');
  for(const predecessor of after.edge14Predecessors){
   assert.equal(predecessor.sharedFace.length,3);
   assert.equal(after.assignments.find(a=>a.cell===predecessor.cell).role,'electron');
   assert.equal(after.assignments.find(a=>a.cell===predecessor.proton).role,'proton');
  }
  const affected=new Set([...after.ray34.contacts,...after.ray14.contacts,...after.edge34Predecessors,...after.edge14Predecessors].map(c=>c.cell));
  for(const predecessor of after.edge34Predecessors){
   assert.equal(predecessor.sharedFace.length,3);
   assert(!before.assignments.some(a=>a.cell===predecessor.cell));
   assert.equal(after.assignments.find(a=>a.cell===predecessor.cell).role,'proton');
   assert.equal(after.assignments.find(a=>a.cell===predecessor.electron).role,'electron');
  }
  assert.deepEqual(after.assignments.filter(a=>!affected.has(a.cell)),before.assignments.filter(a=>!affected.has(a.cell)));
  assert.deepEqual(after.rays.slice(0,-2),before.rays);assert.deepEqual(after.rays.slice(-2).map(r=>r.id),['ray34','ray14']);
  assert(!after.rays.some(r=>r.id==='ray12'));
  assert.equal(new Set(after.assignments.map(a=>a.cell)).size,after.assignments.length);
  if(k===4){
   assert.equal(m.process.step,13);
   assert.deepEqual(after.ray34.contacts.map(c=>after.assignments.find(a=>a.cell===c.cell).role),['proton','neutron','electron','neutron']);
   assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[[308,'proton'],[117,'electron'],[328,'electron'],[125,'proton']]);
   assert.deepEqual(after.edge14Predecessors.map(c=>[c.cell,c.proton]),[[328,125]]);
   assert.deepEqual(after.edge14Assignments.map(a=>a.role),['electron','neutron','proton','neutron']);
   assert.deepEqual(after.edge34Predecessors.map(c=>[c.cell,c.electron]),[[308,117]]);
  }
  m.move(-1);assert.deepEqual(m.state.value,first);m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('ray12 follows in its own step using the same N-preserving EPN rule',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;m.move(7);
  while(!m.state.value.ray14Visible){assert(m.process.step<14);m.move(1);}
  const before=m.state.value;assert.equal(before.ray12,null);m.move(1);const after=m.state.value;
  assert(after.ray12Visible);assert(m.canAdvance.value);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.ray12.start,before.firstRay.start);assert.deepEqual(after.ray12.end,before.ray32.end);
  assert.equal(after.ray12.length,k);assert.equal(after.ray12.contacts.length,k);
  assert.deepEqual(after.rays.slice(0,-1),before.rays);assert.equal(after.rays.at(-1).id,'ray12');
  assertRayDiamonds(before,after,after.ray12,'electron','proton');
  for(const c of after.edge12Predecessors){assert.equal(c.sharedFace.length,3);assert.equal(after.assignments.find(a=>a.cell===c.cell).role,'electron');assert.equal(after.assignments.find(a=>a.cell===c.proton).role,'proton');}
  if(k===4){assert.equal(m.process.step,14);assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[[338,'electron'],[130,'proton']]);}
  m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('ray32 continues PEN in the next step without overwrites or duplicate rays',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;m.move(7);
  while(!m.state.value.ray12Visible){assert(m.process.step<15);m.move(1);}
  const before=m.state.value;assert.equal(before.ray32Pattern,null);m.move(1);const after=m.state.value;
  assert(after.ray32PatternVisible);assert(m.canAdvance.value);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.rays,before.rays);
  assert.deepEqual(after.ray32Pattern.start,before.firstRay.end);assert.deepEqual(after.ray32Pattern.end,before.ray32.end);
  assertRayDiamonds(before,after,after.ray32Pattern,'proton','electron');
  for(const c of after.edge32Predecessors){assert.equal(c.sharedFace.length,3);assert.equal(after.assignments.find(a=>a.cell===c.cell).role,'proton');assert.equal(after.assignments.find(a=>a.cell===c.electron).role,'electron');}
  if(k===4){assert.equal(m.process.step,15);assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[[322,'proton'],[123,'electron']]);}
  m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('replayed ray diamonds remove same-color surface contacts without recoloring N',()=>{
 const m=useViewerModel({processId:'new-construction'});m.process.k=7;
 while(!m.state.value.baseEdgeVisible)m.move(1);
 const before=m.state.value;
 for(let step=0;step<4;step++){
  m.move(1);const charged=m.state.value.assignments.filter(a=>a.role!=='neutron');
  for(let i=0;i<charged.length;i++)for(let j=i+1;j<charged.length;j++){
   const a=charged[i],b=charged[j];if(a.role!==b.role)continue;
   const va=cells[a.cell].vertices,vb=cells[b.cell].vertices;
   if(va.filter(p=>vb.some(q=>String(p)===String(q))).length!==2)continue;
   assert(![0,1,2,3].some(c=>va.filter(p=>p[c]===2).length===3&&vb.filter(p=>p[c]===2).length===3),`Same-color surface contact: ${a.cell}/${b.cell}`);
  }
  for(const n of before.assignments.filter(a=>a.role==='neutron'))assert.deepEqual(m.state.value.assignments.find(a=>a.cell===n.cell),n);
 }
 assert.deepEqual([m.state.value.ray34,m.state.value.ray14,m.state.value.ray12,m.state.value.ray32Pattern].map(r=>r.diamonds.length),[2,2,2,2]);
});
test('diamond validation rejects whole pairs rather than overwriting N or creating same-color contacts',()=>{
 const m=useViewerModel({processId:'new-construction'});m.process.k=7;while(!m.state.value.baseEdgeVisible)m.move(1);
 const ray={...cornerRay(7,m.state.value.firstRay.end,m.state.value.surfaceRays[1].end),id:'ray34'};
 for(const [cell,role] of [[144,'neutron'],[140,'electron']]){
  const assignments=[...m.state.value.assignments,{cell,role}],before=[...assignments];
  const result=fillRayDiamonds(7,ray,['proton','electron','neutron'],assignments,(cell,role,boundary)=>assignments.push({cell,role,boundary}));
  assert.deepEqual(assignments.slice(0,before.length),before);assert(!assignments.some(a=>a.cell===63));
  assert(result.blocked.some(b=>b.cell===63));assert(!result.diamonds.some(d=>d.codomain===63));
 }
});
test('post-pattern closure adds simultaneous two-face-supported N rounds',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;
  while(!m.state.value.ray32PatternVisible){assert(m.process.step<16);m.move(1);}
  let rounds=0;
  while(m.state.value.nextPatternClosure.length){
   assert(rounds++<10);const before=m.state.value;
   assert.deepEqual(before.nextPatternClosure,interiorNeutronRound(k,before.assignments));
   m.move(1);const after=m.state.value;
   assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
   assert.deepEqual(after.patternClosureRounds.at(-1),before.nextPatternClosure);
   assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),before.nextPatternClosure.map(c=>[c.cell,'neutron']));
   for(const c of after.patternClosureRounds.at(-1)){assert(c.supports.length>=2);assert(c.supports.every(s=>s.face.length===3&&before.assignments.some(a=>a.cell===s.cell)));}
   if(k===4&&rounds===1){assert.equal(m.process.step,16);assert.deepEqual(after.patternClosureRounds[0].map(c=>c.cell),[309,321,327,335]);}
   m.move(-1);assert.deepEqual(m.state.value,before);m.move(1);
  }
  assert.deepEqual(interiorNeutronRound(k,m.state.value.assignments),[]);
 }
});
test('base neutron pass fills vertex-contact octahedral gaps without overwrites',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;m.move(7);
  while(!m.state.value.baseNeutronPassAvailable){assert(m.process.step<25);m.move(1);}
  const before=m.state.value;assert(!before.baseNeutronPassVisible);m.move(1);const after=m.state.value;
  assert(after.baseNeutronPassVisible);assert(m.canAdvance.value);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.baseNeutronPass.start,before.surfaceRays[0].end);assert.deepEqual(after.baseNeutronPass.end,before.surfaceRays[1].end);
  assert.deepEqual(after.baseNeutronPass.contacts,cornerRay(k,after.baseNeutronPass.start,after.baseNeutronPass.end).contacts);
  assert(after.baseNeutronPass.contacts.every(c=>after.assignments.find(a=>a.cell===c.cell)?.role==='neutron'));
  assert(after.assignments.slice(before.assignments.length).every(a=>a.role==='neutron'&&after.baseNeutronPass.contacts.some(c=>c.cell===a.cell)));
  if(k===4){assert.equal(m.process.step,19);assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>a.cell),[303,305,315,317,323,325]);}
  m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('edge completion fills all remaining vertex-only gaps without touching assigned roles',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;
  while(!m.state.value.baseNeutronPassVisible){assert(m.process.step<25);m.move(1);}
  const before=m.state.value;
  if(!before.edgeVertexFillAvailable){assert.equal(k,3);assert(m.canAdvance.value);continue;}
  m.move(1);const after=m.state.value;assert(after.edgeVertexFillVisible);assert(m.canAdvance.value);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),before.edgeVertexNeutrons.map(c=>[c.cell,'neutron']));
  for(const c of after.edgeVertexNeutrons){assert(!before.assignments.some(a=>a.cell===c.cell));assert(c.contacts.every(x=>x.interval[1]-x.interval[0]<=1e-9));assert(c.contacts.every(x=>x.edge!=='24'));}
  const corners=[apex,...[1,2,3].map(vertex=>apex.map((x,i)=>x+(i===0?k:i===vertex?-k:0)))];
  for(const [a,b] of [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]])for(const c of cornerRay(k,corners[a],corners[b]).contacts)if(c.interval[1]-c.interval[0]<=1e-9)assert(after.assignments.some(role=>role.cell===c.cell));
  if(k===7){assert.equal(after.edgeVertexNeutrons.length,40);assert.equal(m.process.step,16);}
  m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('edge filling enables sequential simultaneous N closure rounds and terminates',()=>{
 for(let k=4;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;
  while(!m.state.value.edgeVertexFillVisible){assert(m.process.step<25);m.move(1);}
  const counts=[];
  while(m.state.value.nextEdgeClosure.length){
   assert(counts.length<20);const before=m.state.value;
   assert.deepEqual(before.nextEdgeClosure,interiorNeutronRound(k,before.assignments));
   m.move(1);const after=m.state.value,added=after.edgeClosureRounds.at(-1);counts.push(added.length);
   assert.deepEqual(added,before.nextEdgeClosure);
   assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
   assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),added.map(c=>[c.cell,'neutron']));
   for(const c of added){assert(c.supports.length>=2);assert(c.supports.every(s=>s.face.length===3&&before.assignments.some(a=>a.cell===s.cell)));}
   m.move(-1);assert.deepEqual(m.state.value,before);m.move(1);
  }
  assert.deepEqual(interiorNeutronRound(k,m.state.value.assignments),[]);
  if(k===7){assert.deepEqual(counts,[14,8,4]);assert.equal(m.process.step,19);}
  if(k===4)assert.deepEqual(counts,[]);
 }
});
test('surface medians from V3 then V1 alternate PE and EP without another N ray',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;
  while(!m.state.value.faceMedianAvailable){assert(m.process.step<30);m.move(1);}
  const before=m.state.value;m.move(1);const first=m.state.value;
  assert(first.median3To24Visible);assert(!first.median1To24Visible);assert.equal(first.faceMedianRays.length,1);assert(m.canAdvance.value);
  m.move(1);const after=m.state.value;assert(after.median1To24Visible);assert.equal(m.canAdvance.value,after.diamondGapAvailable||after.neutronBoundaryAvailable);
  assert.deepEqual(first.assignments.slice(0,before.assignments.length),before.assignments);assert.deepEqual(after.assignments.slice(0,first.assignments.length),first.assignments);
  assert.deepEqual(after.faceMedianRays.map(r=>r.id),['ray3-24','ray1-24']);
  assert.deepEqual(after.rays.slice(0,-2),before.rays);
  for(const [index,ray] of after.faceMedianRays.entries()){
   const preceding=index===0?before:first,pattern=index===0?['proton','electron']:['electron','proton'];let phase=0,covered=0;
   assert.deepEqual(ray.start,index===0?before.firstRay.end:before.firstRay.start);
   assert.deepEqual(ray.end,before.surfaceRays[0].end.map((x,i)=>(x+before.surfaceRays[1].end[i])/2));
   assert.equal(ray.coordinate,index===0?0:2);
   for(const contact of ray.surfaceCells){
    assert.equal(contact.face.length,3);assert(contact.face.every(p=>p[ray.coordinate]===ray.value));assert(contact.interval[0]<=covered+1e-9);covered=Math.max(covered,contact.interval[1]);
    const prior=preceding.assignments.find(a=>a.cell===contact.cell),role=after.assignments.find(a=>a.cell===contact.cell).role,expected=pattern[phase%2];
    assert.equal(role,prior?.role??expected);if(role===expected)phase++;
   }
   assert(Math.abs(covered-1)<1e-9);
  }
  if(k===7)assert.equal(m.process.step,21);
  if(k===4){assert.deepEqual(first.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[[26,'proton']]);assert.deepEqual(after.assignments.slice(first.assignments.length).map(a=>[a.cell,a.role]),[[128,'electron']]);}
  m.move(-1);assert.deepEqual(m.state.value,first);m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('meeting surface diamonds force only their one- or two-triangle N gaps',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;
  while(!m.state.value.median1To24Visible){assert(m.process.step<30);m.move(1);}
  const before=m.state.value;if(!before.diamondGapAvailable){assert.equal(m.canAdvance.value,before.neutronBoundaryAvailable);continue;}
  m.move(1);const after=m.state.value;assert(after.diamondGapVisible);assert.equal(m.canAdvance.value,after.neutronBoundaryAvailable);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),before.diamondGapPlan.cells.map(c=>[c.cell,'neutron']));
  for(const w of after.diamondGapPlan.witnesses){
   assert(w.gap.length===1||w.gap.length===2);
   const face=id=>cells[id].vertices.filter(p=>p[w.coordinate]===w.value);
   for(const id of w.path){assert.equal(face(id).length,3);assert(face(id).some(p=>String(p)===String(w.vertex)));}
   for(let i=1;i<w.path.length;i++)assert.equal(face(w.path[i]).filter(p=>face(w.path[i-1]).some(q=>String(p)===String(q))).length,2);
   for(const [a,b] of w.diamonds){assert.notEqual(before.assignments.find(x=>x.cell===a).role,before.assignments.find(x=>x.cell===b).role);assert.equal(cells[a].vertices.filter(p=>cells[b].vertices.some(q=>String(p)===String(q))).length,3);}
   assert(w.fillCells.every(id=>!before.assignments.some(a=>a.cell===id)&&after.assignments.find(a=>a.cell===id).role==='neutron'));
  }
  if(k===7){assert.equal(m.process.step,22);assert.deepEqual(after.diamondGapPlan.cells.map(c=>c.cell),[71,77,120,122,167,187,285,293]);assert.equal(after.diamondGapPlan.witnesses.length,4);}
  m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('surface rays complete N gaps without moving the existing N-cell boundary',()=>{
 for(let k=3;k<=7;k++){
  const m=useViewerModel({processId:'new-construction'});m.process.k=k;
  while(!m.state.value.median1To24Visible||(m.state.value.diamondGapAvailable&&!m.state.value.diamondGapVisible)){assert(m.process.step<30);m.move(1);}
  const before=m.state.value;if(!before.neutronBoundaryAvailable){assert(!m.canAdvance.value);continue;}
  m.move(1);const after=m.state.value;assert(after.neutronBoundaryVisible);assert.equal(m.canAdvance.value,after.identifiedSurfaceAvailable);
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),before.neutronBoundaryPlan.cells.map(c=>[c.cell,'neutron']));
  for(const w of after.neutronBoundaryPlan.witnesses){
   assert.equal(before.assignments.find(a=>a.cell===w.boundary).role,'neutron');
   assert(['proton','electron'].includes(before.assignments.find(a=>a.cell===w.source).role));
   assert(w.gap.length===1||w.gap.length===2);
   const face=id=>cells[id].vertices.filter(p=>p[w.coordinate]===w.value);
   for(const id of w.path){assert.equal(face(id).length,3);assert(face(id).some(p=>String(p)===String(w.vertex)));}
   for(let i=1;i<w.path.length;i++)assert.equal(face(w.path[i]).filter(p=>face(w.path[i-1]).some(q=>String(p)===String(q))).length,2);
   assert(w.fillCells.every(id=>!before.assignments.some(a=>a.cell===id)));
  }
  if(k===7){assert.equal(m.process.step,23);assert.deepEqual(after.neutronBoundaryPlan.cells.map(c=>c.cell),[75,80,97,99]);assert.equal(after.neutronBoundaryPlan.witnesses.length,4);}
  m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('identified F134 and F123 patches add exactly eight N cells in one reversible step',()=>{
 const m=useViewerModel({processId:'new-construction'});m.process.k=7;
 while(!m.state.value.neutronBoundaryVisible){assert(m.process.step<30);m.move(1);}
 const before=m.state.value;assert(m.canAdvance.value);m.move(1);const after=m.state.value;
 assert.equal(m.process.step,24);assert(after.identifiedSurfaceVisible);assert(m.canAdvance.value);
 assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
 assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[91,93,96,100,105,114,126,129].map(id=>[id,'neutron']));
 for(const c of after.identifiedSurfacePlan){
  const face=cells[c.cell].vertices.filter(p=>p[c.coordinate]===2);
  assert.equal(face.length,3);assert.equal(Math.min(...face.map(p=>p[c.layerCoordinate])),c.minimum);
  assert(c.supports.some(s=>s.role==='neutron'));assert(c.supports.some(s=>s.role==='electron'||s.role==='proton'));
  for(const s of c.supports){assert.equal(before.assignments.find(a=>a.cell===s.cell).role,s.role);assert.equal(face.filter(p=>cells[s.cell].vertices.some(q=>String(p)===String(q))).length,2);}
 }
 m.move(-1);assert.deepEqual(m.state.value,before);
});
test('F134 fourth-layer diamonds continue PE from V3 and EP from V1',()=>{
 const m=useViewerModel({processId:'new-construction'});m.process.k=7;
 while(!m.state.value.identifiedSurfaceVisible){assert(m.process.step<30);m.move(1);}
 const before=m.state.value;m.move(1);const after=m.state.value;
 assert.equal(m.process.step,25);assert(after.f134DiamondVisible);assert(m.canAdvance.value);
 assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
 assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[[232,'proton'],[92,'electron'],[308,'electron'],[117,'proton']]);
 for(const pair of after.f134DiamondPlan){
  assert.equal(pair.sharedFace.length,3);
  const faces=[pair.domain,pair.codomain].map(member=>cells[member.cell].vertices.filter(p=>p[1]===2));
  for(const face of faces){assert.equal(face.length,3);assert.equal(Math.min(...face.map(p=>p[pair.coordinate])),-2);}
  assert(faces[0].reduce((n,p)=>n+p[pair.coordinate],0)<faces[1].reduce((n,p)=>n+p[pair.coordinate],0));
  assert.equal(faces[0].filter(p=>faces[1].some(q=>String(p)===String(q))).length,2);
 }
 m.move(-1);assert.deepEqual(m.state.value,before);
});
test('F123 repeats the fourth-layer PE/EP diamonds in a separate reversible step',()=>{
 const m=useViewerModel({processId:'new-construction'});m.process.k=7;
 while(!m.state.value.f134DiamondVisible){assert(m.process.step<30);m.move(1);}
 const before=m.state.value;assert(!before.f123DiamondVisible);m.move(1);const after=m.state.value;
 assert.equal(m.process.step,26);assert(after.f123DiamondVisible);assert(m.canAdvance.value);
 assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
 assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[[246,'proton'],[98,'electron'],[322,'electron'],[123,'proton']]);
 for(const pair of after.f123DiamondPlan){
  assert.equal(pair.faceCoordinate,3);assert.equal(pair.sharedFace.length,3);
  const faces=[pair.domain,pair.codomain].map(member=>cells[member.cell].vertices.filter(p=>p[3]===2));
  for(const face of faces){assert.equal(face.length,3);assert.equal(Math.min(...face.map(p=>p[pair.coordinate])),-2);}
  assert(faces[0].reduce((n,p)=>n+p[pair.coordinate],0)<faces[1].reduce((n,p)=>n+p[pair.coordinate],0));
  assert.equal(faces[0].filter(p=>faces[1].some(q=>String(p)===String(q))).length,2);
 }
 m.move(-1);assert.deepEqual(m.state.value,before);
});
test('remaining F123/F134 gaps become N simultaneously without changing diamonds',()=>{
 const m=useViewerModel({processId:'new-construction'});m.process.k=7;
 while(!m.state.value.f123DiamondVisible){assert(m.process.step<30);m.move(1);}
 const before=m.state.value;m.move(1);const after=m.state.value;
 assert.equal(m.process.step,27);assert(after.surfaceRemainderVisible);assert(m.canAdvance.value);
 assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
 assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[107,110,118,121,228,254,272,298].map(id=>[id,'neutron']));
 for(const c of after.surfaceRemainderPlan){
  const face=cells[c.cell].vertices.filter(p=>p[c.coordinate]===2);
  assert.equal(face.length,3);assert.equal(c.supports.length,3);assert.equal(c.supports.filter(s=>s.role==='neutron').length,2);
  for(const s of c.supports){assert.equal(before.assignments.find(a=>a.cell===s.cell).role,s.role);assert.equal(face.filter(p=>cells[s.cell].vertices.some(q=>String(p)===String(q))).length,2);}
 }
 for(const c of cells.filter(c=>[1,3].some(i=>c.vertices.filter(p=>p[i]===2).length===3)))assert(after.assignments.some(a=>a.cell===c.id));
 m.move(-1);assert.deepEqual(m.state.value,before);
});
test('remaining faces receive four oriented diamonds and four N witnesses',()=>{
 const m=useViewerModel({processId:'new-construction'});m.process.k=7;
 while(!m.state.value.surfaceRemainderVisible){assert(m.process.step<30);m.move(1);}
 const before=m.state.value;m.move(1);const after=m.state.value;
 assert.equal(m.process.step,28);assert(after.remainingFaceVisible);assert(!m.canAdvance.value);
 assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
 assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[[70,'proton'],[163,'electron'],[81,'proton'],[199,'electron'],[109,'electron'],[241,'proton'],[113,'electron'],[257,'proton'],...[69,84,95,101].map(id=>[id,'neutron'])]);
 for(const pair of after.remainingFacePlan.diamonds){
  assert.equal(pair.sharedFace.length,3);
  const faces=[pair.domain,pair.codomain].map(member=>cells[member.cell].vertices.filter(p=>p[pair.faceCoordinate]===2));
  assert(faces.every(f=>f.length===3));assert.equal(faces[0].filter(p=>faces[1].some(q=>String(p)===String(q))).length,2);
  assert(faces[0].reduce((n,p)=>n+p[pair.sourceCoordinate],0)<faces[1].reduce((n,p)=>n+p[pair.sourceCoordinate],0));
 }
 for(const c of cells.filter(c=>[0,1,2,3].some(i=>c.vertices.filter(p=>p[i]===2).length===3)))assert(after.assignments.some(a=>a.cell===c.id));
 assert.deepEqual(m.counts.value,{surface:{proton:24,neutron:110,electron:24,total:158},filler:{proton:0,neutron:46,electron:0,total:46},total:{proton:24,neutron:156,electron:24,total:204}});
 assert.deepEqual(particleCounts(7,[...after.assignments,...after.assignments]),m.counts.value);
 m.move(-1);assert.deepEqual(m.state.value,before);assert.equal(m.counts.value.total.total,before.assignments.length);
});
test('particle counts follow k, step and process, independent of display settings',()=>{
 const m=useViewerModel({processId:'new-construction'});
 for(const k of [1,4,7]){
  m.process.k=k;m.process.step=0;assert.equal(m.counts.value.total.total,m.state.value.assignments.length);
  m.move(4);const counts=m.counts.value;
  for(const role of ['proton','neutron','electron','total'])assert.equal(counts.surface[role]+counts.filler[role],counts.total[role]);
  for(const row of Object.values(counts))assert.equal(row.proton+row.neutron+row.electron,row.total);
  assert.equal(counts.total.total,m.state.value.assignments.length);
  m.appearance.bodies=false;m.appearance.faceOpacity=0;m.appearance.labels=false;assert.deepEqual(m.counts.value,counts);
 }
 m.selectProcess('edge-ray');assert.equal(m.counts.value.total.total,0);m.move(2);assert.equal(m.counts.value.total.total,m.state.value.assignments.length);
});
test('cell face opacity supports zero and clamps without changing construction',()=>{
 const m=useViewerModel();m.process.k=4;m.move(9);const state=m.state.value;
 assert.equal(m.renderState.value.faceOpacity,1);
 for(const [value,expected] of [[0,0],[.35,.35],[1,1],[-1,0],[2,1],['invalid',1]]){
  m.appearance.faceOpacity=value;assert.equal(m.renderState.value.faceOpacity,expected);assert.equal(m.state.value,state);
 }
});
test('cell opacity defaults to 100 percent and persists including zero',()=>{
 const descriptor=Object.getOwnPropertyDescriptor(globalThis,'localStorage'),values=new Map();
 try{
  Object.defineProperty(globalThis,'localStorage',{configurable:true,value:{getItem:key=>values.get(key)??null,setItem:(key,value)=>values.set(key,value)}});
  const m=useViewerModel();assert.equal(m.appearance.faceOpacity,1);
  for(const value of [0,.42,1]){m.appearance.faceOpacity=value;assert.equal(JSON.parse(values.get(sceneSettingsKey)).appearance.faceOpacity,value);assert.equal(useViewerModel().appearance.faceOpacity,value);}
  for(const [raw,expected] of [['bad',1],['',1],['Infinity',1],['-1',0],['2',1]]){values.set(sceneSettingsKey,JSON.stringify({version:1,appearance:{faceOpacity:raw}}));assert.equal(useViewerModel().appearance.faceOpacity,expected);}
  Object.defineProperty(globalThis,'localStorage',{configurable:true,get(){throw Error('Storage denied');}});
  const blocked=useViewerModel();assert.equal(blocked.appearance.faceOpacity,1);blocked.appearance.faceOpacity=.3;assert.equal(blocked.renderState.value.faceOpacity,.3);
 }finally{if(descriptor)Object.defineProperty(globalThis,'localStorage',descriptor);else delete globalThis.localStorage;}
});
test('PNE label visibility persists and rehydrates safely',()=>{
 const descriptor=Object.getOwnPropertyDescriptor(globalThis,'localStorage'),values=new Map();
 try{
  Object.defineProperty(globalThis,'localStorage',{configurable:true,value:{getItem:key=>values.get(key)??null,setItem:(key,value)=>values.set(key,value)}});
  const m=useViewerModel();assert.equal(m.appearance.labels,true);
  m.appearance.labels=false;assert.equal(JSON.parse(values.get(sceneSettingsKey)).appearance.labels,false);assert.equal(useViewerModel().appearance.labels,false);
  m.appearance.labels=true;assert.equal(JSON.parse(values.get(sceneSettingsKey)).appearance.labels,true);assert.equal(useViewerModel().appearance.labels,true);
  values.set(sceneSettingsKey,JSON.stringify({version:1,appearance:{labels:'invalid'}}));assert.equal(useViewerModel().appearance.labels,true);
  Object.defineProperty(globalThis,'localStorage',{configurable:true,get(){throw Error('Storage denied');}});
  const blocked=useViewerModel();assert.equal(blocked.appearance.labels,true);blocked.appearance.labels=false;assert.equal(blocked.appearance.labels,false);
 }finally{if(descriptor)Object.defineProperty(globalThis,'localStorage',descriptor);else delete globalThis.localStorage;}
});
test('k storage rehydrates, clamps and tolerates unavailable storage',()=>{
 const descriptor=Object.getOwnPropertyDescriptor(globalThis,'localStorage');let saved=JSON.stringify({version:1,k:4});
 try{
  Object.defineProperty(globalThis,'localStorage',{configurable:true,value:{getItem:key=>key===sceneSettingsKey?saved:null,setItem:(key,value)=>{assert.equal(key,sceneSettingsKey);saved=value;}}});
  const m=useViewerModel();assert.equal(m.k.value,4);m.process.k=6;assert.equal(JSON.parse(saved).k,6);
  saved=JSON.stringify({version:1,k:99});assert.equal(useViewerModel().k.value,7);saved='bad';assert.equal(useViewerModel().k.value,1);
  Object.defineProperty(globalThis,'localStorage',{configurable:true,get(){throw Error('Storage denied');}});
  const blocked=useViewerModel();assert.equal(blocked.k.value,1);blocked.process.k=3;assert.equal(blocked.k.value,3);
 }finally{if(descriptor)Object.defineProperty(globalThis,'localStorage',descriptor);else delete globalThis.localStorage;}
});
test('namespaced scene settings round-trip all controls and migrate legacy values once',()=>{
 const descriptor=Object.getOwnPropertyDescriptor(globalThis,'localStorage');
 const values=new Map([['normal-ray:k','4'],['normal-ray:labels','false'],['normal-ray:face-opacity','.35'],['other-app:scene-settings','untouched']]);
 try{
  Object.defineProperty(globalThis,'localStorage',{configurable:true,value:{getItem:key=>values.get(key)??null,setItem:(key,value)=>values.set(key,value)}});
  const m=useViewerModel();assert.equal(m.k.value,4);assert.equal(m.appearance.labels,false);assert.equal(m.appearance.faceOpacity,.35);
  Object.assign(m.appearance,{grid:false,opacity:.24,faceOpacity:.6,prior:true,bodies:false,labels:true});
  Object.assign(m.motion,{spin:true,speed:-2});Object.assign(m.locks,{v1:true,v3:true});Object.assign(m.panels,{process:false,scene:false});Object.assign(m.sections,{appearance:false,view:false,motion:false});
  const camera={offset:[3,4,5],targetOffset:[.2,.3,.4],up:[0,0,1],zoom:2};m.captureCamera(camera);m.flushSettings();
  const hydrated=useViewerModel();
  for(const key of ['appearance','motion','locks','panels','sections'])assert.deepEqual({...hydrated[key]},{...m[key]});
  assert.deepEqual(hydrated.savedCamera,camera);assert.equal(hydrated.process.step,0);
  assert.equal(values.get('other-app:scene-settings'),'untouched');assert.equal(values.get('normal-ray:face-opacity'),'.35');
  values.set('normal-ray:labels','false');assert.equal(useViewerModel().appearance.labels,true);
  m.suspendMotion();assert.equal(m.motion.spin,false);assert.equal(loadSceneSettings().motion.spin,true);
  m.disposeSettings();m.motion.spin=false;assert.equal(loadSceneSettings().motion.spin,true);
  values.set(sceneSettingsKey,'broken');assert.equal(loadSceneSettings().appearance.faceOpacity,1);
  values.set(sceneSettingsKey,JSON.stringify({version:1,camera:{offset:[0,0,0],up:[0,1,0],targetOffset:[0,0,0]},motion:{speed:99},sections:{view:'false'}}));
  assert.equal(loadSceneSettings().camera,null);assert.equal(loadSceneSettings().motion.speed,4);assert.equal(loadSceneSettings().sections.view,true);
 }finally{if(descriptor)Object.defineProperty(globalThis,'localStorage',descriptor);else delete globalThis.localStorage;}
});
test('process namespace restores selection, step, branch, k and independent progress',()=>{
 const descriptor=Object.getOwnPropertyDescriptor(globalThis,'localStorage'),values=new Map();
 try{
  Object.defineProperty(globalThis,'localStorage',{configurable:true,value:{getItem:key=>values.get(key)??null,setItem:(key,value)=>values.set(key,value)}});
  const m=useViewerModel({processId:'new-construction'});m.process.k=7;m.move(4);
  m.selectProcess('edge-ray');m.process.k=4;m.process.branch=3;m.move(6);m.disposeSettings();
  const persisted=JSON.parse(values.get(sceneSettingsKey)).process;
  assert.deepEqual(persisted,{id:'edge-ray',k:4,step:6,branch:3,progress:{'new-construction':{k:7,step:4,branch:1},'edge-ray':{k:4,step:6,branch:3}}});
  const restored=useViewerModel({processId:'new-construction'});
  assert.deepEqual({...restored.process},{id:'edge-ray',k:4,step:6,branch:3});assert.deepEqual(restored.state.value,m.state.value);
  restored.selectProcess('new-construction');assert.deepEqual({...restored.process},{id:'new-construction',k:7,step:4,branch:1});
  restored.move(-1);assert.equal(loadSceneSettings().process.step,3);
  restored.selectProcess('edge-ray');assert.deepEqual({...restored.process},{id:'edge-ray',k:4,step:6,branch:3});restored.disposeSettings();
  values.set(sceneSettingsKey,JSON.stringify({version:1,k:4,process:{id:'invalid',step:9}}));
  assert.equal(loadSceneSettings().process,null);assert.equal(useViewerModel({processId:'new-construction'}).process.step,0);
  values.set(sceneSettingsKey,JSON.stringify({version:1,process:{id:'new-construction',k:99,step:-8,branch:2,progress:{'edge-ray':{k:-1,step:'bad',branch:3},unknown:{step:9}}}}));
  assert.deepEqual(loadSceneSettings().process,{id:'new-construction',k:7,step:0,branch:1,progress:{'edge-ray':{k:1,step:0,branch:3},'new-construction':{k:7,step:0,branch:1}}});
  Object.defineProperty(globalThis,'localStorage',{configurable:true,get(){throw Error('blocked');}});
  const blocked=useViewerModel();blocked.move(1);blocked.selectProcess('new-construction');blocked.disposeSettings();
 }finally{if(descriptor)Object.defineProperty(globalThis,'localStorage',descriptor);else delete globalThis.localStorage;}
});
test('setup stays uncast; k changes rebuild the selected stage',()=>{
 const m=useViewerModel();assert.equal(m.process.step,0);assert.equal(m.state.value.firstRay,null);
 m.process.k=2;assert.equal(m.state.value.firstRay,null);assert.deepEqual(m.state.value.assignments,[]);
 m.move(1);assert.equal(m.state.value.firstRay.length,2);m.move(1);
 assert.deepEqual(m.state.value.assignments.map(a=>a.role),['electron','proton']);
 const state=JSON.stringify(m.state.value);m.appearance.opacity=.31;m.locks.v1=true;m.motion.spin=true;m.panels.scene=false;
 assert.equal(JSON.stringify(m.state.value),state);m.move(-1);assert.deepEqual(m.state.value.assignments,[]);assert.equal(m.k.value,2);
 m.process.k=3;assert.equal(m.process.step,1);assert.equal(m.state.value.firstRay.length,3);assert.equal(m.state.value.rays.length,0);
 for(let step=0;step<=14;step++){
  m.process.step=step;
  for(const k of [2,5,3]){
   m.process.k=k;assert.equal(m.process.step,step);
   assert.deepEqual(m.state.value,procedureState(k,step,m.process.branch));
  }
 }
});
