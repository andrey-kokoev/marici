import test from 'node:test';
import assert from 'node:assert/strict';
import {buildRuthenium98,ruthenium98Envelope} from '../research/realization-tower/ruthenium-98-model.mjs';
import {processState,processes} from '../research/realization-tower/normal-ray-processes.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
import {useViewerModel} from '../examples/normal-ray/useViewerModel.js';
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
test('edge-five carrier and retained matching yield 44 P sites and ten N witnesses',()=>{
 const m=buildRuthenium98();assert.equal(m.base.length,65);assert.equal(m.carrier.length,54);assert.equal(m.context.length,11);assert.equal(m.witnessPairs.length,10);
 assert.equal(new Set(m.witnessPairs.map(p=>p.outer)).size,10);assert.equal(new Set(m.witnessPairs.map(p=>p.inner)).size,10);
 for(const p of m.witnessPairs){const a=m.base.find(c=>c.id===p.inner),b=m.base.find(c=>c.id===p.outer);assert(a.faces.some(f=>b.faces.some(g=>key(f)===key(g))));}
 assert(ruthenium98Envelope.every(p=>m.base.some(c=>c.vertices.some(v=>String(v)===String(p)))));
});
test('44 outward chains have native face contacts, no reused lattice cells, and tetrahedral E endpoints',()=>{
 const m=buildRuthenium98(),occupied=new Set(m.base.map(c=>c.key)),all=[...m.base];
 for(const c of m.chains){
  assert.equal(c.electron.kind,'tetrahedron');assert.equal(c.electron.vertices.length,4);
  assert(c.proton.faces.some(f=>key(f)===key(c.protonNeutronFace)));
  assert(c.neutron.faces.some(f=>key(f)===key(c.protonNeutronFace)));
  assert(c.neutron.faces.some(f=>key(f)===key(c.neutronElectronFace)));
  assert(c.electron.faces.some(f=>key(f)===key(c.neutronElectronFace)));
  for(const p of [...c.neutron.parts,c.electron]){assert(!occupied.has(p.key));occupied.add(p.key);all.push(p);assert(p.vertices.every(v=>v.reduce((s,x)=>s+x,0)===1));}
 }
 assert.equal(m.chains.length,44);assert.equal(all.length,163);assert.equal(m.audit.compositeNeutrons,10);
 const byFace=new Map();all.forEach((c,i)=>c.faces.forEach(f=>{const k=key(f);if(!byFace.has(k))byFace.set(k,[]);byFace.get(k).push(i);}));
 assert([...byFace.values()].every(ids=>ids.length<=2));
 const adj=all.map(()=>[]);for(const ids of byFace.values())if(ids.length===2){adj[ids[0]].push(ids[1]);adj[ids[1]].push(ids[0]);}
 const seen=new Set([0]),queue=[0];for(let i=0;i<queue.length;i++)for(const j of adj[queue[i]])if(!seen.has(j)){seen.add(j);queue.push(j);}assert.equal(seen.size,all.length);
});
test('legacy viewer item is now a genuine five-edge octahedron',()=>{
 assert.equal(processes.find(p=>p.id==='ruthenium-98').name,'5-side oct');
 const p=processState('ruthenium-98',7,0);
 assert.equal(p.retainedBodies.length,245);assert.equal(p.contextBodies,undefined);assert(!p.canAdvance);
 assert.deepEqual(['proton','neutron','electron'].map(r=>p.retainedBodies.filter(c=>c.role===r).length),[80,85,80]);
 assert.equal(p.retainedBodies.reduce((n,c)=>n+c.faces.length,0),200);
 assert(p.retainedBodies.every(c=>c.insideNSector&&c.components.length===0));
 assert.equal(p.nativeWiringGraph.nodes.length,245);assert.equal(p.nativeWiringGraph.links.length,560);
 assert.deepEqual(['proton','neutron','electron','total'].map(r=>p.inventory.rows[0][r]),[80,85,80,245]);
 assert.equal(p.inventory.records.length,245);assert.equal(new Set(p.inventory.records.map(r=>r.id)).size,245);
 for(const role of ['proton','neutron','electron'])assert.equal(p.inventory.rows[0][role],p.inventory.records.filter(r=>r.role===role).length);
 assert.equal(p.inventory.rows[0].label,'5-side oct cells');
 assert.equal(p.ruthenium98Audit.template,'five-side-octahedron');assert.equal(p.ruthenium98Audit.outwardChains,false);
 assert.throws(()=>processState('ruthenium-98',7,1),/stage/);
 const s=normalizeSceneSettings({process:{id:'ruthenium-98',k:1,step:1},appearance:{rutheniumView:'wiring'}});assert.equal(s.process.k,7);assert.equal(s.process.step,0);assert.equal(s.appearance.rutheniumView,'lattice');
 assert.equal(s.appearance.rutheniumViewVersion,2);
 const fresh=normalizeSceneSettings({appearance:{rutheniumView:'wiring',rutheniumViewVersion:2}});assert.equal(fresh.appearance.rutheniumView,'wiring');
 assert.equal(normalizeSceneSettings(fresh).appearance.rutheniumView,'wiring');
 const m=useViewerModel();m.selectProcess('ruthenium-98');assert.equal(m.process.step,0);assert.equal(m.pneInventory.value.rows[0].total,245);m.move(1);assert.equal(m.process.step,0);assert.match(m.summary.value,/245 cells/);m.selectProcess('sulfur-32');m.selectProcess('ruthenium-98');assert.equal(m.process.step,0);m.disposeSettings();
});
