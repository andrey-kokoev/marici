import test from 'node:test';
import assert from 'node:assert/strict';
import {processes,processState} from '../research/realization-tower/normal-ray-processes.mjs';
import {sulfur32ReflectionProcess,projectReflection} from '../research/realization-tower/sulfur-32-reflection-process.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('reflection process exposes the checked five-stage assembly',()=>{
 assert(processes.some(p=>p.id==='sulfur-32-reflection'&&p.name==='Sulfur-32 reflection'));
 for(const [s,h,n] of [[0,1,1],[1,2,2],[2,4,4],[3,8,8],[4,16,14]]){
  const m=processState('sulfur-32-reflection',7,s);
  assert.equal(m.copies.length,h);assert.equal(m.reflectionCells.length,n);assert.equal(m.canAdvance,s<4);
  assert(m.copies.every(c=>c.vertices.length===5&&c.vertices4.length===5&&c.vertices5.length===5));
 }
 const final=sulfur32ReflectionProcess(7,4);
 assert.equal(final.reflectionWiring.nodes.length,14);assert.equal(final.reflectionWiring.links.length,14);
 assert.equal(final.reflectionWiring.nodes.flatMap(n=>n.copies).length,16);
 for(const link of final.reflectionWiring.links){
  assert.deepEqual(link.points[0],final.reflectionWiring.nodes.find(n=>n.id===link.source).point);
  assert.deepEqual(link.points[2],final.reflectionWiring.nodes.find(n=>n.id===link.target).point);
  const contact=final.reflectionContacts.find(c=>c.cells[0]===link.source&&c.cells[1]===link.target);
  assert.deepEqual(link.points[1],[0,1,2].map(i=>(contact.points[0][i]+contact.points[1][i])/2));
 }
 assert.throws(()=>sulfur32ReflectionProcess(7,5));
});
test('projection uses the regular-simplex metric and does not mutate retained coordinates',()=>{
 const m=sulfur32ReflectionProcess(7,0),points=m.copies[0].vertices4;
 const snapshot=JSON.stringify(points);
 for(const angle of [-90,-25,0,35,90]){
  const vs=points.map(p=>projectReflection(p,{reflectionAngle:angle}));
  for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)assert(vs[i].reduce((s,x,k)=>s+(x-vs[j][k])**2,0)<=2+1e-12);
 }
 assert(points.slice(0,3).map(p=>projectReflection(p)).every(p=>p[2]===0));
 assert.equal(JSON.stringify(points),snapshot);
});
test('reflection process settings and independent progress survive normalization',()=>{
 const s=normalizeSceneSettings({process:{id:'sulfur-32-reflection',k:7,step:4,progress:{'sulfur-32':{k:7,step:1}}},appearance:{reflectionView:'wiring',reflectionAngle:-25,reflectionCopy:'c15',reflectionCycle:false}});
 assert.equal(s.process.step,4);assert.equal(s.process.progress['sulfur-32'].step,1);
 assert.equal(s.appearance.reflectionCopy,'c15');assert.equal(s.appearance.reflectionAngle,-25);assert.equal(s.appearance.reflectionCycle,false);
 assert.equal(normalizeSceneSettings({process:{id:'sulfur-32-reflection',step:99}}).process.step,4);
});
