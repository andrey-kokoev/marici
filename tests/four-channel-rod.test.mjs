import test from 'node:test';
import assert from 'node:assert/strict';
import {fourChannelRod} from '../research/realization-tower/four-channel-rod.mjs';
const distance=(a,b)=>Math.hypot(...a.map((x,i)=>x-b[i]));
test('four labelled channels survive every size and reference-frame change',()=>{
 for(let k=1;k<=7;k++){
  const p=fourChannelRod(k),e=fourChannelRod(k,'electron');
  assert.deepEqual(p.assignments,[]);assert.deepEqual(p.centerPoint,[0,0,0]);assert.deepEqual(e.vertexPoints[0],[0,0,0]);
  assert.deepEqual(p.channels.map(c=>c.id),['fiber-1','fiber-2','fiber-3','fiber-4']);
  assert.equal(p.channels.filter(c=>c.marked).length,1);
  const radius=distance(p.centerPoint,p.vertexPoints[0]);
  for(let i=0;i<4;i++){
   assert.deepEqual(p.channels[i].to,e.channels[i].to);assert.deepEqual(p.channels[i].from,e.channels[i].from);
   assert(Math.abs(distance(p.centerPoint,p.vertexPoints[i])-radius)<1e-9);
   assert(Math.abs(distance(e.centerPoint,e.vertexPoints[i])-radius)<1e-9);
   assert.equal(p.channels[i].status,'schematic-not-a-lattice-path');
  }
  assert.equal(p.centerStatus,k===1?'shared-seed-cell':k%2?'unique-center-cell':'multiple-center-pieces');
 }
 assert.equal(fourChannelRod(5).centralCell,26);assert.equal(fourChannelRod(7).centralCell,0);
 assert.throws(()=>fourChannelRod(0));assert.throws(()=>fourChannelRod(8));assert.throws(()=>fourChannelRod(3,'other'));
});
