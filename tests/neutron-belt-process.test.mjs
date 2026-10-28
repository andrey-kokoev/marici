import test from 'node:test';
import {doubleEsd7RuleProcess,doubleEsd7Rules} from '../research/realization-tower/double-esd7-process.mjs';
import assert from 'node:assert/strict';
import {neutronBeltProcess,beltViewerPoint} from '../research/realization-tower/neutron-belt-process.mjs';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import {cellDualGraph} from '../research/realization-tower/cell-dual-graph.mjs';
import source from '../research/voevodsky/results/four_six_center_cones.json' with {type:'json'};
test('native seam cycles replace external attachments without changing cell assignments',()=>{
 const p=doubleEsd7RuleProcess(7,doubleEsd7Rules.map(r=>r.id),false,{enabled:true,a:0,b:1}),s=p.doubleEsd7Audit.seamLattice;
 assert.equal(p.retainedBodies.length,350);assert.equal(p.attachmentBodies.length,0);assert.equal(s.pairCount,49);assert.equal(s.cellCount,98);assert.equal(s.cycles.length,15);assert.equal(s.overlaps.length,30);
 assert.equal(s.flows.length,2);assert.deepEqual(s.flows.map(f=>f.direction),[1,-1]);
 const g=cellDualGraph(p.retainedBodies),edges=new Set(g.links.flatMap(e=>[e.from+'|'+e.to,e.to+'|'+e.from]));
 for(const c of s.cycles)for(const lift of c.lifts){assert.equal(new Set(lift).size,6);for(let i=0;i<6;i++)assert.ok(edges.has(lift[i]+'|'+lift[(i+1)%6]));}
 assert.equal(p.interfaceGuides.filter(g=>g.seamFlow).length,12);assert.equal(p.interfaceGuides.filter(g=>g.connector).length,0);
 assert.deepEqual(p.retainedBodies,doubleEsd7RuleProcess(7,doubleEsd7Rules.map(r=>r.id)).retainedBodies);
});
test('adapter preserves physical coordinates',()=>{for(const p of [[0,0,0],[1,2,3],[-.5,.35,1]])assert.ok(worldPoint(beltViewerPoint(p)).every((x,i)=>Math.abs(x-p[i])<1e-12));});
test('source six cones preserve annular link, C6 incidence and opposite paired signs',()=>{
 const p=neutronBeltProcess(7,0),g=cellDualGraph(p.retainedBodies);assert.equal(g.nodes.length,6);assert.equal(g.links.length,6);
 assert.deepEqual(p.retainedBodies.map(b=>b.internalSector.vertices),source.belt_tetrahedra);
 for(const b of p.retainedBodies){assert.equal(b.role,null);assert.equal(g.links.filter(e=>e.from===b.id||e.to===b.id).length,2);}
 for(const [a,b] of p.neutronBeltAudit.sectors)assert.equal(p.retainedBodies[a].internalSector.circulation+p.retainedBodies[b].internalSector.circulation,0);
 for(const e of g.links)assert.notEqual(g.nodes.find(n=>n.id===e.from).body.internalSector.circulation,g.nodes.find(n=>n.id===e.to).body.internalSector.circulation);
 assert.deepEqual(p.neutronBeltAudit.centerLink,[1,1,0,0]);assert.equal(p.neutronBeltAudit.excludedCaps.length,2);assert.equal(p.interfaceGuides.length,18);assert.equal(p.neutronBeltAudit.transfers.total,1836);
});
