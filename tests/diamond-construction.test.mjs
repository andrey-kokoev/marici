import test from 'node:test';
import assert from 'node:assert/strict';
import {diamondConstruction,commitDiamondPlan,commitAssignmentPlan} from '../research/realization-tower/diamond-construction.mjs';
import {radialConstraints} from '../research/realization-tower/radial-constraints.mjs';
import {cells,seed} from '../research/realization-tower/normal-ray-model.mjs';
import {oppositePartners} from '../research/realization-tower/edge-ray-model.mjs';
import {pairedRayProcess} from '../research/realization-tower/paired-ray-process.mjs';
import {useViewerModel} from '../examples/normal-ray/useViewerModel.js';
import {sceneSettingsKey,loadSceneSettings} from '../examples/normal-ray/settings.js';

test('Process 3 replays independent seed/ray/diamond stages at every k',()=>{
 for(let k=1;k<=7;k++){
  let previous=[];
  for(let step=0;step<=4;step++){
   const s=diamondConstruction(k,step);
   assert.deepEqual(s.assignments.slice(0,previous.length),previous);assert.deepEqual(s.conflicts,[]);
   assert.equal(new Set(s.assignments.map(a=>a.cell)).size,s.assignments.length);
   assert.equal(s.canAdvance,step<4||([3,5,7].includes(k)&&step===4));assert.equal(s.foundationComplete,step===4);
   for(const a of s.assignments)assert(cells[a.cell].vertices.every(p=>p[0]<=-5+k));
   assert.equal(Boolean(s.firstRay),step>=1);assert.equal(s.rays.length,Math.max(0,Math.min(2,step-1)));
   if(step>=3){assert.equal(s.rays[1].cell,seed.id);assert.deepEqual(s.rays[1].end,s.firstRay.start);}
   if(k===1)assert.deepEqual(s.assignments.map(a=>[a.cell,a.role]),[[seed.id,'electron']]);
   if(step===4&&k>1){
    assert.equal(s.diamonds.length,2);assert.equal(s.assignments.length,5);assert.equal(oppositePartners(s.assignments).length,4);
    for(const d of s.diamonds){assert.equal(d.sharedFace.length,3);assert.notEqual(d.domain.role,d.codomain.role);for(const member of [d.domain,d.codomain])assert.equal(s.assignments.find(a=>a.cell===member.cell).role,member.role);}
   }
   assert.deepEqual(s,diamondConstruction(k,step));previous=s.assignments;
  }
 }
 assert.throws(()=>diamondConstruction(8,0));assert.throws(()=>diamondConstruction(7,8));
});
test('radial constraints establish only central P and expose unresolved inner layers and corner pairing',()=>{
 const before=diamondConstruction(7,4),after=diamondConstruction(7,5),r=after.radial;
 assert(r.available);assert.equal(r.layers.length,4);assert.deepEqual(r.conflicts,[]);
 assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
 assert.deepEqual(after.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[[r.centralCell,'proton']]);
 assert.deepEqual(r.layers[0].cells,[r.centralCell]);assert.deepEqual(r.layers[0].unassigned,[]);
 for(const layer of r.layers.slice(1,3)){assert.deepEqual(layer.allowedRoles,['proton','neutron']);assert.equal(layer.assigned.length,0);assert.equal(layer.unassigned.length,layer.cells.length);}
 const seedAudit=r.surfaceElectrons.find(e=>e.cell===seed.id);assert.equal(seedAudit.hasInteriorFaceNeighbor,false);assert.deepEqual(seedAudit.inwardCandidates,[]);assert(seedAudit.protonPartners.some(p=>p.onSurface));
 assert.equal(after.canAdvance,true);assert.deepEqual(diamondConstruction(4,5).assignments,diamondConstruction(4,4).assignments);
 const m=useViewerModel({processId:'diamond-construction'});m.process.k=7;m.move(5);m.move(-1);assert.deepEqual(m.state.value,before);
});
test('central shell trial places three P and leaves the V1-side neighbor unresolved',()=>{
 const before=diamondConstruction(7,5),after=diamondConstruction(7,6);
 assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
 const added=after.assignments.slice(before.assignments.length);
 assert.deepEqual(added.map(a=>[a.cell,a.role]),[[4,'proton'],[7,'proton'],[10,'proton']]);
 assert.equal(after.radial.centralNeighbors.length,4);
 const faces=new Set();
 for(const n of after.radial.centralNeighbors){assert.equal(n.sharedFace.length,3);faces.add(n.sharedFace.map(p=>String(p)).sort().join('|'));assert(after.radial.layers[1].cells.includes(n.cell));}
 assert.equal(faces.size,4);assert.equal(after.radial.layers[1].assigned.length,3);assert.equal(after.radial.layers[1].assigned.filter(a=>a.role==='proton').length,3);
 const channel=after.radial.centralChannel;assert.equal(channel.cell,13);assert.equal(channel.target,seed.id);assert.equal(channel.pathStatus,'geometric-only');assert(!channel.localConnectionEstablished);assert.equal(channel.role,null);assert(!before.radial.centralChannel.localConnectionEstablished);
 const plane=channel.sharedFace[0][0];assert(channel.sharedFace.every(p=>p[0]===plane));
 const meanX=id=>cells[id].vertices.reduce((sum,p)=>sum+p[0]/4,0);
 assert(meanX(channel.cell)<plane);assert(meanX(seed.id)<plane);assert(meanX(after.radial.centralCell)>plane);
 assert(!after.assignments.some(a=>a.cell===channel.cell));
 assert(radialConstraints(7,[...after.assignments,{cell:channel.cell,role:'electron'}]).conflicts.some(c=>c.cell===channel.cell));
 assert.equal(after.radial.layers[1].unassigned.length,13);assert.equal(after.radial.layers[2].assigned.length,0);assert.deepEqual(after.radial.conflicts,[]);assert(after.canAdvance);
 const m=useViewerModel({processId:'diamond-construction'});m.process.k=7;m.move(6);assert.deepEqual(m.state.value,after);m.move(-1);assert.deepEqual(m.state.value,before);
 assert.deepEqual(diamondConstruction(4,6).assignments,diamondConstruction(4,4).assignments);
});
test('k=5 has a visible central P but nine tied branch orientations, not a guessed shell',()=>{
 const before=diamondConstruction(5,4),core=diamondConstruction(5,5),later=diamondConstruction(5,6);
 assert.equal(core.radial.centralCell,26);assert.deepEqual(core.radial.centerCandidates,[26]);
 assert.deepEqual(core.assignments.slice(before.assignments.length).map(a=>[a.cell,a.role]),[[26,'proton']]);
 assert.deepEqual(core.radial.center,[-1.25,.75,.75,.75]);
 assert.equal(core.radial.status,'branch-orientation-ambiguous');assert.equal(core.radial.orientationCount,9);assert.equal(core.radial.connections.length,0);assert(!core.canAdvance);
 assert.deepEqual(later.assignments,core.assignments);assert.deepEqual(later.connectionGuides,[]);
 for(const option of core.radial.orientationOptions){assert.equal(new Set(option.map(c=>c.cell)).size,4);assert.deepEqual(option.map(c=>c.vertex),[1,2,3,4]);}
 const m=useViewerModel({processId:'diamond-construction'});m.process.k=5;m.move(100);assert.equal(m.process.step,5);assert.equal(m.state.value.assignments.find(a=>a.cell===26).role,'proton');
});
test('all four vertex routes use complete shared faces at k=3 and k=7',()=>{
 for(const k of [3,7]){
  const s=diamondConstruction(k,6);assert.deepEqual(s.conflicts,[]);assert.deepEqual(s.radial.conflicts,[]);assert.equal(s.radial.orientationCount,1);assert.equal(s.connectionGuides.length,4);
  assert.equal(new Set(s.connectionGuides.map(c=>c.neighbor)).size,4);
  for(const c of s.connectionGuides){
   assert.equal(c.path[0],s.radial.centralCell);assert.equal(c.path[1],c.neighbor);assert.equal(c.path.at(-1),c.target);assert.equal(new Set(c.path).size,c.path.length);
   assert.equal(c.faces.length,c.path.length-1);assert.equal(c.roleContinuityVerified,false);
   for(let i=1;i<c.path.length;i++)assert.equal(cells[c.path[i]].vertices.filter(p=>cells[c.path[i-1]].vertices.some(q=>String(p)===String(q))).length,3);
   assert.equal(s.assignments.find(a=>a.cell===c.neighbor)?.role,c.vertex===1?undefined:'proton');
  }
 }
 for(const k of [2,4,6]){const s=diamondConstruction(k,5);assert.equal(s.radial.centralCell,null);assert(s.radial.centerCandidates.length>1);assert.deepEqual(s.assignments,diamondConstruction(k,4).assignments);}
});
test('collective core connects existing surface E pairs through N without individual P/E matching',()=>{
 for(const k of [3,7]){
  const before=diamondConstruction(k,6),after=diamondConstruction(k,7),a=after.collectiveCore;
  assert.deepEqual(after.assignments.slice(0,before.assignments.length),before.assignments);
  assert(after.assignments.slice(before.assignments.length).every(x=>x.role==='neutron'));
  assert.deepEqual(a.disconnectedProtons,[]);assert.deepEqual(a.blocked,[]);assert.equal(a.routes.length,2);assert.equal(a.core.length,4);
  assert.deepEqual(after.radial.conflicts,[]);assert(!after.canAdvance);
  const roles=new Map(after.assignments.map(x=>[x.cell,x.role]));
  for(const r of a.routes){
   assert(r.established);assert(a.core.includes(r.path[0]));assert.equal(roles.get(r.path.at(-1)),'electron');
   const middle=r.path.slice(1,r.viaSurfaceProton?-2:-1);assert(middle.length);assert(middle.every(id=>roles.get(id)==='neutron'));
   if(r.viaSurfaceProton)assert.equal(roles.get(r.path.at(-2)),'proton');
   for(let i=1;i<r.path.length;i++)assert.equal(cells[r.path[i]].vertices.filter(p=>cells[r.path[i-1]].vertices.some(q=>String(p)===String(q))).length,3);
  }
  const m=useViewerModel({processId:'diamond-construction'});m.process.k=k;m.move(100);assert.equal(m.process.step,7);assert.deepEqual(m.state.value,after);m.move(-1);assert.deepEqual(m.state.value,before);
 }
});
test('atomic diamond batches never partially commit or overwrite protected N',()=>{
 const before=diamondConstruction(7,3),plan=diamondConstruction(7,4).diamonds;
 const protectedCell=plan[1].codomain.cell,assignments=[...before.assignments,{cell:protectedCell,role:'neutron'}],snapshot=structuredClone(assignments);
 const blocked=commitDiamondPlan(7,assignments,plan,'test');
 assert.equal(blocked.assignments,assignments);assert.deepEqual(blocked.added,[]);assert.equal(blocked.conflicts.length,1);
 assert.deepEqual(assignments,snapshot);assert(!blocked.assignments.some(a=>a.cell===plan[0].codomain.cell));
 const valid=commitDiamondPlan(7,before.assignments,plan,'test');assert.equal(valid.added.length,2);assert.deepEqual(before.assignments,diamondConstruction(7,3).assignments);
 const repeated=commitDiamondPlan(7,valid.assignments,plan,'test');assert.deepEqual(repeated.added,[]);assert.deepEqual(repeated.conflicts,[]);
 const invalid=commitDiamondPlan(7,before.assignments,[{domain:plan[0].domain,codomain:plan[1].domain}],'test');assert(invalid.conflicts.length);assert.deepEqual(invalid.added,[]);
 const conflicting=commitAssignmentPlan(7,[],[{cell:protectedCell,role:'proton'},{cell:protectedCell,role:'electron'}],'test');assert(conflicting.conflicts.length);assert.deepEqual(conflicting.assignments,[]);
});
test('Process 3 navigation and persistence remain isolated from frozen Process 2',()=>{
 const descriptor=Object.getOwnPropertyDescriptor(globalThis,'localStorage'),values=new Map();
 try{
  Object.defineProperty(globalThis,'localStorage',{configurable:true,value:{getItem:key=>values.get(key)??null,setItem:(key,value)=>values.set(key,value)}});
  const m=useViewerModel({processId:'new-construction'});m.process.k=7;m.process.step=28;
  const old=structuredClone(pairedRayProcess(7,28));
  m.selectProcess('diamond-construction');assert.equal(m.process.step,0);m.move(6);assert.equal(m.process.step,6);assert(m.canAdvance.value);
  const clean=m.state.value;assert.equal(m.counts.value.total.total,9);m.move(-3);assert.equal(m.state.value.diamonds.length,0);m.move(3);assert.deepEqual(m.state.value,clean);
  m.disposeSettings();const restored=useViewerModel();assert.equal(restored.process.id,'diamond-construction');assert.equal(restored.process.step,6);assert.deepEqual(restored.state.value,clean);
  restored.selectProcess('new-construction');assert.equal(restored.process.step,28);assert.deepEqual(restored.state.value,old);
  restored.selectProcess('diamond-construction');assert.deepEqual(restored.state.value,clean);restored.disposeSettings();
  values.set(sceneSettingsKey,JSON.stringify({version:1,process:{id:'diamond-construction',k:7,step:999}}));assert.equal(loadSceneSettings().process.step,7);
 }finally{if(descriptor)Object.defineProperty(globalThis,'localStorage',descriptor);else delete globalThis.localStorage;}
});
