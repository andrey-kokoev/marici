import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildBeryllium9Wiring as build} from '../research/realization-tower/beryllium-9-wiring-procedure.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('one flat layer of eight strand pairs, then straight halves through one central knot',()=>{
 const start=build(),twisted=build({be9WiringStep:1});
 assert.equal(start.wires.length,16);assert.equal(new Set(start.wires.map(w=>w.strandId)).size,8);
 assert.deepEqual(twisted.audit.wireIds,start.audit.wireIds);
 for(const [i,w]of twisted.wires.entries()){
  assert.equal(w.points.length,3);assert.deepEqual(w.points[1],[0,0,0]);
  assert.deepEqual(w.points[0],start.wires[i].points[0]);
  assert.deepEqual(w.points[2],[-w.lane,4,0]);
  assert(w.points.every(p=>p[2]===0));assert.equal(w.colour,start.wires[i].colour);
  // A straight segment on each side, with no extra samples or control curves.
  const a=w.points[0],b=w.points[2];assert(a.every((x,j)=>Math.abs(x+b[j])<1e-12));
 }
 assert.equal(twisted.subbundles.length,0);
});
test('removed step 2 cannot be restored from saved settings',()=>{
 assert.equal(normalizeSceneSettings({appearance:{be9WiringStep:2}}).appearance.be9WiringStep,1);
 assert.deepEqual(build({be9WiringStep:2}),build({be9WiringStep:1}));
});
