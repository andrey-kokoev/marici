import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';
import {buildBeltLayers} from '../research/realization-tower/belt-layer-model.mjs';
import {sectorRows,bindSourceFibers,restoreSourceFibers,auditSourceFiberRouting} from '../research/realization-tower/belt-source-fiber-binding.mjs';
const m=buildBeltLayers({origin:[0,0,0],x:[1,0,0],y:[0,1,0],normal:[0,0,1]});
const permutations=xs=>xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
test('candidate consumes the actual prior sector table and binds both outer layers bijectively',()=>{
 const prior=JSON.parse(fs.readFileSync(new URL('../research/strominger/results/two-ended-sector-trace.json',import.meta.url),'utf8'));
 assert.deepEqual(sectorRows().map(r=>[r.label,r.source,r.target]),prior.forward[0].rows);
 for(const index of [0,5]){const rows=sectorRows().map(r=>({...r,packet:{coefficients:[r.label,2,3,4,5],witness:'retained'}})),history=['open','operation-a'],binding=bindSourceFibers(rows,m.layers[index],{history});assert.equal(new Set(binding.satellites.map(s=>s.node)).size,12);assert.deepEqual(restoreSourceFibers(binding),rows);assert.deepEqual(binding.history,history);
  for(const c of binding.centres){assert.equal(c.sourceRows.length,3);assert.equal(c.targetRows.length,3);assert.equal(c.sourceRows.filter(x=>c.targetRows.includes(x)).length,0,'source and target fibers are not the same three rows');}
 }
});
test('all 24 relabelings commute when the endpoint marking travels with the rows',()=>{
 const base=bindSourceFibers(sectorRows(),m.layers[0]);for(const p of permutations([0,1,2,3])){const rows=sectorRows().map(r=>({...r,source:p[r.source],target:p[r.target]})),bound=bindSourceFibers(rows,m.layers[0],{marking:p});assert.deepEqual(bound.satellites.map(r=>r.node),base.satellites.map(r=>r.node));assert.deepEqual(restoreSourceFibers(bound),rows);}
 const swapped=sectorRows().map(r=>({...r,source:r.target,target:r.source}));assert.notDeepEqual(bindSourceFibers(swapped,m.layers[0]).satellites.map(s=>s.node),base.satellites.map(s=>s.node));
 assert.throws(()=>restoreSourceFibers({...base,selector:null}));assert.throws(()=>bindSourceFibers([...sectorRows().slice(1),sectorRows()[1]],m.layers[0]));
});
test('current equal-split belt distributes each marked row to all four destinations, not its target',()=>{
 for(const [a,b] of [[0,5],[5,0]]){const audit=auditSourceFiberRouting(m,a,b);assert.equal(audit.allIntendedTargetsReachable,true);assert.equal(audit.equalSplittingRespectsTargets,false);
  for(const row of audit.rows)assert.deepEqual(row.equalSplitShares,[.25,.25,.25,.25]);assert.deepEqual(audit.addressedSinkFlux,[3,3,3,3]);for(let i=0;i<4;i++)assert.equal(audit.addressedTargetTransfer[i].filter(x=>x===1).length,3);
 }
});
test('fiber sums cannot replace retained row packets',()=>{
 const rows=sectorRows(),values=Object.fromEntries(rows.map(r=>[r.label,0])),group=rows.filter(r=>r.target===0);values[group[0].label]=1;values[group[1].label]=-1;
 assert.ok(Object.values(values).some(v=>v!==0));assert.deepEqual([0,1,2,3].map(t=>rows.filter(r=>r.target===t).reduce((s,r)=>s+values[r.label],0)),[0,0,0,0]);
});
