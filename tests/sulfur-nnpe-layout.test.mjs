import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildNNPEComposition} from '../research/realization-tower/sulfur-nnpe-composition.mjs';
import {layoutNNPEComposition} from '../research/realization-tower/sulfur-nnpe-layout.mjs';
test('each complex is three blue/red/white surfaces of a diagonally halved cube',()=>{
 const layout=layoutNNPEComposition(buildNNPEComposition());
 assert.equal(layout.groups.length,16);assert.equal(layout.audit.planes,48);assert.equal(layout.audit.centralGlyph,'none');assert.equal(layout.ports.length,48);
 for(const g of layout.groups){
  assert.deepEqual(g.planes.map(p=>p.colour),[0x168fff,0xff3030,0xffffff]);
  for(const p of g.planes)for(const point of p.corners){
   assert(Math.abs(point.reduce((s,x,i)=>s+(x-p.origin[i])*p.normal[i],0))<1e-12);
   const [x,y,z]=point.map((v,i)=>v-g.origin[i]);assert(y<=x+1e-12);assert([x,y,z].every(v=>Math.abs(Math.abs(v)-.85)<1e-12));
  }
  for(const p of g.ports){const plane=g.planes.find(f=>f.role===p.role);assert(Math.abs(p.point.reduce((s,x,i)=>s+(x-plane.origin[i])*plane.normal[i],0))<1e-12);}
  const diagonal=g.planes[2];assert(diagonal.corners.every(p=>Math.abs((p[0]-g.origin[0])-(p[1]-g.origin[1]))<1e-12));
 }
});
test('collapse retains inventory/history and distinct invisible attachment targets',()=>{
 const model=buildNNPEComposition(Array.from({length:15},(_,i)=>[`S${i+1}:E`,`S${i+2}:P`]));
 const full=layoutNNPEComposition(model),collapsed=layoutNNPEComposition(model,true);
 assert.equal(full.joins.length,15);assert.equal(collapsed.groups.length,1);assert.equal(collapsed.audit.planes,3);assert.equal(collapsed.ports.length,18);assert.equal(collapsed.joins.length,0);
 assert.deepEqual(collapsed.groups[0].inventory,{N:16,P:16});assert.deepEqual(collapsed.groups[0].history,model.components[0].history);
 assert.equal(new Set(collapsed.ports.map(p=>p.point.join(','))).size,18);
});
