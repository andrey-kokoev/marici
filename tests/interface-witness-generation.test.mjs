import test from 'node:test';
import assert from 'node:assert/strict';
import {generateInterfaceWitnesses} from '../research/realization-tower/interface-witness-generation.mjs';
import {centerInterfaceProcess} from '../research/realization-tower/center-interface-process.mjs';
const input=()=>centerInterfaceProcess(7,2).retainedBodies.map(b=>({id:b.id,role:b.role,vertices:b.components[0]}));
test('dual retains all incidence dimensions, including boundary blocks',()=>{
 const r=generateInterfaceWitnesses(input());
 assert.deepEqual(r.counts.before,[8,18,16,5]);
 assert.deepEqual(r.counts.dualBlocks,[5,16,18,8]);
 assert.equal(r.dualEdges.length,4);
 assert.equal(r.dualBlocks.filter(b=>b.dimension===1&&b.onBoundary).length,12);
 const byId=new Map(r.dualVertices.map(v=>[v.id,v]));
 for(const b of r.dualBlocks)for(const flag of b.maximalFlags){
  assert.equal(flag.length,b.dimension+1);
  for(let i=0;i<flag.length;i++){
   assert.ok(byId.has(flag[i]));
   if(i){const prev=flag[i-1].split('|'),next=flag[i].split('|');assert.equal(next.length,prev.length+1);assert.ok(prev.every(v=>next.includes(v)));}
  }
 }
});
test('witnesses and residuals partition the refinement without changing the boundary or parent volumes',()=>{
 const source=input(),snapshot=structuredClone(source),r=generateInterfaceWitnesses(source);
 assert.deepEqual(source,snapshot);
 assert.deepEqual(r.counts.after,[13,38,46,20]);
 assert.equal(r.counts.planesBefore,8);assert.equal(r.counts.planesAfter,32);
 assert.equal(r.witnesses.length,4);
 const all=[...r.witnesses.flatMap(w=>w.cells),...r.residualCells];
 assert.equal(new Set(all).size,all.length);
 assert.deepEqual(all.sort(),r.refinedCells.map(c=>c.id).sort());
 assert.deepEqual(r.sourceVolumes,r.refinedVolumes);
 assert.ok(r.boundaryPreserved);assert.equal(r.expandsOuterBody,false);
 for(const w of r.witnesses){
  assert.equal(w.cells.length,2);assert.equal(w.type,null);
  assert.deepEqual(w.cells.map(id=>r.refinedCells.find(c=>c.id===id).parent).sort(),[...w.parents].sort());
 }
});
test('reordering and integral translations preserve measured incidence',()=>{
 const source=input(),r=generateInterfaceWitnesses(source);
 const translated=source.toReversed().map(t=>({...t,vertices:t.vertices.toReversed().map(v=>v.map((x,i)=>x+[2,-1,-1,0][i]))}));
 assert.deepEqual(generateInterfaceWitnesses(translated).counts,r.counts);
});
