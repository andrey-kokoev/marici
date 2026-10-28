import test from 'node:test';import assert from 'node:assert/strict';
import {buildCentralTerminalWiring} from '../research/realization-tower/central-belt-layout.mjs';
import {restoreTerminalFiber} from '../research/realization-tower/belt-terminal-wiring.mjs';
test('four directional tubes per N terminal retain every link and all four star identities',()=>{
 const w=buildCentralTerminalWiring(),seen=new Set();
 for(const [i,b] of w.bundles.entries()){
  const t=b.body.beltTerminal;assert.deepEqual(t.tubes.map(t=>t.label),i===0?['E1','E2','E3','P']:['P1','P2','P3','E']);assert.deepEqual(t.tubes.map(t=>t.flux),[4,4,4,12]);
  for(const tube of t.tubes){assert.equal(tube.faceBinding.status,'declared-geometric-role');assert.ok(w.surface.faces.some(f=>f.id===tube.faceBinding.face));assert.equal(tube.nativeFieldMap,null);assert.deepEqual(tube.lanes.map(l=>l.star),[0,1,2,3]);
   for(const lane of tube.lanes){assert.ok(!seen.has(lane.linkId));seen.add(lane.linkId);const e=w.links.find(e=>e.id===lane.linkId);assert.equal(e.tube,tube.id);assert.equal(e.direction,tube.direction);assert.equal(e.lane,lane.star);assert.equal(e.arm,tube.slot<3?tube.slot:null);assert.equal(e.from,lane.from);assert.equal(e.to,lane.to);assert.equal(e.flux,lane.flux);assert.equal(e.from===b.body.id,tube.flow==='parent-to-belt');}
  }
  assert.equal(restoreTerminalFiber(b).length,175);
 }
 assert.equal(seen.size,32);assert.ok(w.links.every(e=>seen.has(e.id)));
});
