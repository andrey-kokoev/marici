import test from 'node:test';
import assert from 'node:assert/strict';
import {fibration12Process,fibration12Stages,fibrationClonePoint} from '../research/realization-tower/fibration12-process.mjs';
import {cells} from '../research/realization-tower/normal-ray-model.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const sites=new Set(cells.flatMap(c=>c.vertices.map(v=>v.join(','))));
test('seven recorded steps yield twelve distinct directed three-step paths',()=>{
 assert.equal(fibration12Stages.length,7);
 for(let step=0;step<7;step++){
  const p=fibration12Process(7,step),a=p.fibrationAudit;
  assert.equal(a.pathCount,step*2);assert.equal(a.pathOccurrences,step*6);
  assert.equal(a.distinctDirectedRoutes,a.pathCount);assert.equal(a.multiTypedSites,0);
  assert.equal(p.canAdvance,step<6);
  for(const s of a.sites)assert.ok(sites.has(s.point.join(',')));
  for(const path of a.paths){
   assert.equal(path.points.length,4);
   for(let j=1;j<4;j++)assert.equal(path.points[j].reduce((s,x,i)=>s+(x-path.points[j-1][i])**2,0),2);
  }
 }
 const a=fibration12Process(7,6).fibrationAudit;
 assert.equal(a.sites.length,40);
 const expected={ 'E>P':'EEE','P>E':'PPP','E>N2':'NNN','P>N1':'NNN','P>N2':'ENN','E>N1':'PNN','N1>N2':'NNN','N2>N1':'NNN','N1>P':'PNN','N2>E':'ENN','N1>E':'EPN','N2>P':'PEN'};
 assert.deepEqual(Object.fromEntries(a.paths.map(p=>[`${p.from}>${p.to}`,p.word.join('')])),expected);
 for(const p of a.paths){const q=a.paths.find(q=>q.from===p.to&&q.to===p.from);assert.equal(p.points[3].reduce((s,x,i)=>s+(x-q.points[3][i])**2,0),2);}
});
test('clone is a rigid half-turn with a conforming shared PNN face',()=>{
 const p=fibration12Process(7,6),a=p.fibrationAudit,c=a.cornerBinding;
 const near=(x,y)=>assert.ok(Math.abs(x-y)<1e-9);
 const same=(x,y)=>x.forEach((v,i)=>near(v,y[i]));
 same(fibrationClonePoint(c.P),c.P);same(fibrationClonePoint(c.N1),c.N2);same(fibrationClonePoint(c.N2),c.N1);
 assert.ok(c.E[1]<2);assert.ok(a.gluedClone.exit[1]>2);
 const key=vs=>vs.map(v=>v.map(x=>x.toFixed(8)).join(',')).sort().join('|');
 const faceIndices=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]];
 const seam=cells.flatMap(t=>faceIndices.map(f=>f.map(i=>t.vertices[i]))).filter(f=>f.every(v=>v[1]===2));
 assert.equal(new Set(seam.map(key)).size,49);
 assert.deepEqual([...new Set(seam.map(key))].sort(),[...new Set(seam.map(f=>key(f.map(fibrationClonePoint))))].sort());
 for(const cell of cells){
  const clone=cell.vertices.map(fibrationClonePoint);
  cell.vertices.forEach((v,i)=>{same(fibrationClonePoint(clone[i]),v);for(let j=0;j<4;j++)near(v.reduce((s,x,k)=>s+(x-cell.vertices[j][k])**2,0),clone[i].reduce((s,x,k)=>s+(x-clone[j][k])**2,0));});
  assert.ok(clone.every(v=>v[1]>=2-1e-9));
 }
 assert.ok(p.presentationLabels.some(l=>l.text==='E′'));
});
test('saved progress is independent and bounded',()=>{
 const s=normalizeSceneSettings({process:{id:'fibration-12x12',k:2,step:99,progress:{'from-center-cell':{k:7,step:4}}}});
 assert.equal(s.process.k,7);assert.equal(s.process.step,50);assert.equal(s.process.progress['from-center-cell'].step,4);
 assert.throws(()=>fibration12Process(7,7));
});
