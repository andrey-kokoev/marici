import test from 'node:test';
import assert from 'node:assert/strict';
import {centerInterfaceProcess,centerInterfaceStages} from '../research/realization-tower/center-interface-process.mjs';
import {cells} from '../research/realization-tower/normal-ray-model.mjs';
import {processes} from '../research/realization-tower/normal-ray-processes.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
const d2=(v,w)=>v.reduce((s,x,j)=>s+(x-w[j])**2,0);
const det=(a,b,c)=>a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);
const volume=vs=>Math.abs(det(...vs.slice(1).map(v=>v.slice(0,3).map((x,i)=>x-vs[0][i]))));
const permutations=xs=>xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>j!==i)).map(t=>[x,...t])):[[]];
function congruent(a,b){return permutations([0,1,2,3]).some(p=>a.every((v,i)=>a.every((w,j)=>d2(v,w)===d2(b[p[i]],b[p[j]]))));}
const common=(a,b)=>a.filter(v=>b.some(w=>v.every((x,i)=>x===w[i])));
test('all numbered steps use only existing esd7 vertices and cells',()=>{
 assert.ok(processes.some(p=>p.id==='from-center-cell'));
 assert.ok(centerInterfaceProcess(7,0).presentationDot);
 for(let step=0;step<centerInterfaceStages.length;step++){
  const p=centerInterfaceProcess(7,step);
  assert.match(p.summary,new RegExp(`^Step ${step}`));
  assert.equal(p.assignments.length,0);
  assert.equal(p.presentationAudit.nativeRealization,false);
  assert.equal(p.presentationAudit.nativeGeometry,true);
  assert.equal(p.presentationAudit.fixedCellSize,true);
  assert.equal(p.presentationAudit.fillingAvailable,step>=5);
  assert.equal(p.canAdvance,step<centerInterfaceStages.length-1);
  const nativeIds=p.retainedBodies.map(b=>b.nativeCellId);
  assert.equal(new Set(nativeIds).size,nativeIds.length);
  for(const b of p.retainedBodies){
   assert.equal(key(b.components[0]),key(cells[b.nativeCellId].vertices));
   assert.ok(b.components[0].every(v=>v.every(Number.isInteger)));
  }
  if(step>=2)assert.deepEqual(p.presentationLabels.slice(1,5).map(l=>l.role),['proton','electron','neutron','neutron']);
 }
 assert.equal(centerInterfaceProcess(7,4).interfaceGuides.length,8);
 assert.throws(()=>centerInterfaceProcess(7,6));
});
test('boundary relocation preserves exact congruence and center geometry',()=>{
 const before=centerInterfaceProcess(7,2).retainedBodies;
 for(const step of [3,4,5]){
  const after=centerInterfaceProcess(7,step).retainedBodies;
  assert.deepEqual(after[0],before[0]);
  for(let i=0;i<5;i++){
   const a=before[i].components[0],b=after[i].components[0];
   assert.ok(congruent(a,b));assert.equal(volume(a),volume(b));
   if(i>0)assert.notEqual(before[i].nativeCellId,after[i].nativeCellId);
  }
 }
});
test('step 5 builds the four assigned words on face-connected native routes',()=>{
 const previous=centerInterfaceProcess(7,4),p=centerInterfaceProcess(7,5);
 assert.deepEqual(p.retainedBodies.slice(0,5),previous.retainedBodies);
 assert.equal(p.retainedBodies.length,13);assert.equal(p.interfaceGuides.length,0);
 assert.equal(p.previewBodies,undefined);assert.equal(p.collisionWitnesses,undefined);
 assert.deepEqual(p.presentationAudit.branchWords.map(w=>w.map(r=>r[0].toUpperCase()).join('')),['PPPP','PNNE','PNEN','PNPN']);
 for(const r of p.presentationAudit.routes){
  const i=r.branch,route=['central-P',`gap-${i}-0`,`gap-${i}-1`,`boundary-${i}`].map(id=>p.retainedBodies.find(b=>b.id===id));
  assert.deepEqual(route.map(b=>b.role),r.roles);
  assert.deepEqual(route.map(b=>b.nativeCellId),r.nativeCellIds);
  for(let j=1;j<4;j++){
   const face=common(route[j-1].components[0],route[j].components[0]);
   assert.equal(face.length,3);assert.equal(key(face),key(r.interfaces[j-1]));
   assert.ok(p.retainedContacts.some(c=>c.owners.includes(route[j-1].id)&&c.owners.includes(route[j].id)));
  }
 }
});
test('persisted steps clamp and retain other process progress',()=>{
 const s=normalizeSceneSettings({process:{id:'from-center-cell',k:2,step:8,progress:{'retained-construction':{k:7,step:2}}}});
 assert.equal(s.process.k,7);assert.equal(s.process.step,5);assert.equal(s.process.progress['retained-construction'].step,2);
});
