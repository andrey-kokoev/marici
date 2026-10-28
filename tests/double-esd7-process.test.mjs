import test from 'node:test';
import {cellDualGraph} from '../research/realization-tower/cell-dual-graph.mjs';
import assert from 'node:assert/strict';
import {doubleEsd7Process,doubleEsd7RuleProcess,doubleEsd7Rules} from '../research/realization-tower/double-esd7-process.mjs';
import {processState,processes} from '../research/realization-tower/normal-ray-processes.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const key=vs=>vs.map(v=>v.map(x=>x.toFixed(8)).join(',')).sort().join('|');
test('unfolded pair preserves 350 distinct cells and connected seam, with all corner seeds',()=>{
 const p=doubleEsd7Process(7,0),all=[...p.retainedBodies,...p.emptyBodies];
 assert.equal(all.length,350);assert.equal(new Set(all.map(b=>key(b.vertices))).size,350);
 assert.equal(p.retainedBodies.length,8);
 assert.deepEqual(['proton','neutron','electron'].map(r=>p.retainedBodies.filter(b=>b.role===r).length),[2,4,2]);
 assert.deepEqual(p.presentationLabels.map(l=>l.text).sort(),['−P','+P','+N','+N','−N','−N','E','E'].sort());assert.equal(p.presentationWireframes.length,342);
 assert.equal(p.retainedBodies.filter(b=>b.front).length,2);
 const faces=new Map();for(const b of all)for(const f of b.faces){const k=key(f);if(!faces.has(k))faces.set(k,[]);faces.get(k).push(b.id);}
 assert.ok([...faces.values()].every(a=>a.length<=2));assert.ok([...faces.values()].some(a=>a.length===2&&a[0].split(':')[0]!==a[1].split(':')[0]));
 const ns=new Map(all.map(b=>[b.id,[]]));for(const a of faces.values())if(a.length===2){ns.get(a[0]).push(a[1]);ns.get(a[1]).push(a[0]);}
 const seen=new Set([all[0].id]);for(const id of seen)for(const n of ns.get(id))seen.add(n);assert.equal(seen.size,350);
 assert.equal(p.canAdvance,true);assert.throws(()=>doubleEsd7Process(7,8));
});
test('dual graph contains all cells and seam links without duplicate edges',()=>{
 const p=doubleEsd7Process(7,0),g=cellDualGraph([...p.retainedBodies,...p.emptyBodies]);
 assert.equal(g.nodes.length,350);assert.equal(g.nodes.filter(n=>n.body.role).length,8);
 assert.equal(new Set(g.links.map(e=>JSON.stringify([e.from,e.to]))).size,g.links.length);
 assert.ok(g.links.some(e=>e.from.split(':')[0]!==e.to.split(':')[0]));
 const seen=new Set([g.nodes[0].id]);let previous=-1;
 while(previous!==seen.size){previous=seen.size;for(const e of g.links){if(seen.has(e.from))seen.add(e.to);if(seen.has(e.to))seen.add(e.from);}}
 assert.equal(seen.size,350);
});
test('step one advances each opposing P front by one shared-face edge',()=>{
 const before=doubleEsd7Process(7,0),after=doubleEsd7Process(7,1),graph=cellDualGraph([...before.retainedBodies,...before.emptyBodies]);
 assert.equal(after.retainedBodies.length,10);assert.equal(after.emptyBodies.length,340);assert.equal(after.doubleEsd7Audit.seedCount,8);
 assert.equal(after.doubleEsd7Audit.growth.length,2);assert.equal(after.interfaceGuides.length,2);
 for(const g of after.doubleEsd7Audit.growth){
  assert.equal(g.word,'|P|');assert.ok(graph.links.some(e=>[e.from,e.to].includes(g.source)&&[e.from,e.to].includes(g.target)));
  const target=after.retainedBodies.find(b=>b.id===g.target);assert.equal(target.role,'proton');assert.equal(target.layer,1);assert.equal(target.front.label,g.front);
 }
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(c=>c.id===b.id),b);
 assert.equal(after.canAdvance,true);
});
test('both new P nodes branch to N N E and the inward P neighbor',()=>{
 const before=doubleEsd7Process(7,1),after=doubleEsd7Process(7,2),added=after.retainedBodies.filter(b=>b.layer===2);
 assert.equal(added.length,8);assert.equal(after.retainedBodies.length,18);assert.equal(after.emptyBodies.length,332);
 for(const source of before.retainedBodies.filter(b=>b.layer===1)){
  const branches=added.filter(b=>b.arrow.source===source.id);
  assert.deepEqual(branches.map(b=>[b.arrow.direction,b.role]),[['−N','neutron'],['+N','neutron'],['E','electron'],['P','proton']]);
  assert.equal(new Set(branches.map(b=>b.id)).size,4);
 }
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(c=>c.id===b.id),b);
 for(const half of ['original','clone'])assert.ok(added.some(b=>b.id===half+':tet-41'&&b.role==='proton'));
 assert.equal(after.interfaceGuides.length,10);assert.equal(after.canAdvance,true);
});
test('step three extends PPN to PPNP and PPE to PPEN',()=>{
 const before=doubleEsd7Process(7,2),after=doubleEsd7Process(7,3),added=after.retainedBodies.filter(b=>b.layer===3),graph=cellDualGraph([...before.retainedBodies,...before.emptyBodies]);
 assert.equal(added.length,6);assert.equal(new Set(added.map(b=>b.id)).size,6);
 assert.equal(after.retainedBodies.length,24);assert.equal(after.emptyBodies.length,326);
 for(const source of before.retainedBodies.filter(b=>b.layer===2&&b.role!=='proton')){
  const target=added.find(b=>b.arrow.source===source.id);assert.ok(target);assert.equal(target.role,source.role==='electron'?'neutron':'proton');assert.equal(target.arrow.word,source.role==='electron'?'|N|':'|P|');assert.deepEqual(target.front,source.front);
  assert.ok(graph.links.some(e=>[e.from,e.to].includes(source.id)&&[e.from,e.to].includes(target.id)));
 }
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(c=>c.id===b.id),b);
 assert.equal(after.interfaceGuides.length,16);assert.equal(after.canAdvance,true);
});
test('step four branches PPNP only and merges agreeing N arrivals',()=>{
 const before=doubleEsd7Process(7,3),after=doubleEsd7Process(7,4),added=after.retainedBodies.filter(b=>b.layer===4);
 assert.equal(added.length,14);assert.equal(after.retainedBodies.length,38);assert.equal(after.emptyBodies.length,312);
 const newArrows=after.doubleEsd7Audit.growth.slice(before.doubleEsd7Audit.growth.length);assert.equal(newArrows.length,16);
 for(const source of before.retainedBodies.filter(b=>b.layer===3)){
  const arrows=newArrows.filter(g=>g.source===source.id);
  if(source.role==='neutron'){assert.equal(arrows.length,0);continue;}
  assert.deepEqual(arrows.map(g=>[g.direction,g.role]),[['−N','neutron'],['+N','neutron'],['E','electron'],['P','proton']]);
 }
 const shared=added.filter(b=>b.arrivals.length===2);assert.equal(shared.length,2);assert.ok(shared.every(b=>b.role==='neutron'));
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(c=>c.id===b.id),b);
 assert.equal(after.interfaceGuides.length,32);assert.equal(after.canAdvance,true);
});
test('closure application matches preview exactly, persists provenance, and reverses as one step',()=>{
 const before=doubleEsd7Process(7,4),preview=before.doubleEsd7Audit.rulePreview,after=doubleEsd7Process(7,5),added=after.retainedBodies.filter(b=>b.layer===5);
 assert.equal(added.length,124);assert.equal(after.retainedBodies.length,162);assert.equal(after.emptyBodies.length,188);
 assert.deepEqual(added.map(b=>[b.id,b.role]),preview.candidates.map(b=>[b.id,b.role]));
 assert.ok(added.every(b=>b.ruleClosure.round>0&&b.arrivals.length));
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(c=>c.id===b.id),b);
 assert.equal(after.doubleEsd7Audit.rulePreview.candidates.length,164);assert.equal(after.doubleEsd7Audit.rulePreview.valid,true);
 assert.equal(after.canAdvance,true);assert.deepEqual(doubleEsd7Process(7,4),before);
});
test('extended rules preview and apply 164 additional cells without conflicts',()=>{
 const before=doubleEsd7Process(7,5),after=doubleEsd7Process(7,6),r=before.doubleEsd7Audit.rulePreview;
 assert.equal(r.valid,true);assert.equal(r.candidates.length,164);
 assert.deepEqual(after.retainedBodies.filter(b=>b.layer===6).map(b=>[b.id,b.role]),r.candidates.map(b=>[b.id,b.role]));
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(c=>c.id===b.id),b);
 assert.equal(after.retainedBodies.length,326);assert.equal(after.emptyBodies.length,24);assert.equal(after.canAdvance,true);
 assert.equal(after.doubleEsd7Audit.rulePreview.candidates.length,24);assert.equal(after.doubleEsd7Audit.rulePreview.valid,true);
});
test('3P+1N rule previews and fills precisely the last 24 cells',()=>{
 const before=doubleEsd7Process(7,6),after=doubleEsd7Process(7,7),preview=before.doubleEsd7Audit.rulePreview;
 assert.equal(preview.valid,true);assert.equal(preview.candidates.length,24);
 assert.deepEqual(after.retainedBodies.filter(b=>b.layer===7).map(b=>[b.id,b.role]),preview.candidates.map(b=>[b.id,b.role]));
 for(const b of before.retainedBodies)assert.deepEqual(after.retainedBodies.find(c=>c.id===b.id),b);
 assert.equal(after.retainedBodies.length,350);assert.equal(new Set(after.retainedBodies.map(b=>b.id)).size,350);assert.equal(after.emptyBodies.length,0);
 assert.equal(after.doubleEsd7Audit.rulePreview.candidates.length,0);assert.equal(after.doubleEsd7Audit.rulePreview.valid,true);assert.equal(after.canAdvance,false);
});
test('four independent rules reproduce every legacy cell colour without completion patches',()=>{
 const reference=doubleEsd7Process(7,7);
 for(let mask=0;mask<16;mask++){
  const ids=doubleEsd7Rules.filter((_,i)=>mask&(1<<i)).map(r=>r.id),p=doubleEsd7RuleProcess(7,ids);
  assert.deepEqual(p.doubleEsd7Audit.enabledRules,ids);assert.equal(p.doubleEsd7Audit.rulePreview.valid,true);
  for(const b of p.retainedBodies)assert.equal(b.role,reference.retainedBodies.find(c=>c.id===b.id).role);
  if(mask===15){assert.equal(p.retainedBodies.length,350);assert.equal(p.emptyBodies.length,0);}
 }
});
test('independent process registration and bounded persistence',()=>{
 assert.ok(processes.some(p=>p.id==='double-esd7'));assert.equal(processState('double-esd7',7,0).retainedBodies.length,8);
 const s=normalizeSceneSettings({process:{id:'double-esd7',k:2,step:99}});assert.equal(s.process.id,'double-esd7');assert.equal(s.process.k,7);assert.equal(s.process.step,7);
});
