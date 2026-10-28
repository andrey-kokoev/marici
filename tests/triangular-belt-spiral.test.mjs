import test from 'node:test';import assert from 'node:assert/strict';
import {triangularBeltSpiral} from '../research/realization-tower/triangular-belt-spiral.mjs';
test('side-four colour order has four runs and ten unique positions',()=>{
 const {points,runs}=triangularBeltSpiral(4);assert.deepEqual(runs.map(r=>[r.length,r.role]),[[4,'proton'],[3,'electron'],[2,'proton'],[1,'electron']]);assert.equal(new Set(points.map(p=>p.coordinates.join(','))).size,10);
});
test('side-five colour order has five alternating runs and fifteen unique positions',()=>{
 const {points,runs}=triangularBeltSpiral(5);assert.deepEqual(runs.map(r=>r.length),[5,4,3,2,1]);assert.equal(new Set(points.map(p=>p.coordinates.join(','))).size,15);assert.equal(points.filter(p=>p.role==='proton').length,9);assert.equal(points.filter(p=>p.role==='electron').length,6);
});
test('six turning runs cover the native side-six triangle exactly once',()=>{
 const {points,runs}=triangularBeltSpiral();assert.deepEqual(runs.map(r=>r.length),[6,5,4,3,2,1]);
 assert.equal(points.length,21);assert.equal(new Set(points.map(p=>p.coordinates.join(','))).size,21);
 for(const p of points){assert.equal(p.coordinates.reduce((a,b)=>a+b,0),5);assert.ok(p.coordinates.every(x=>Number.isInteger(x)&&x>=0));}
 for(let i=1;i<points.length;i++){const delta=points[i].coordinates.map((x,j)=>x-points[i-1].coordinates[j]);assert.deepEqual(delta.sort((a,b)=>a-b),[-1,0,1]);}
 for(const r of runs){const ps=r.steps.map(i=>points[i]);assert.ok(ps.every(p=>p.role===r.role));if(ps.length>2){const d=ps[1].coordinates.map((x,i)=>x-ps[0].coordinates[i]);for(let j=2;j<ps.length;j++)assert.deepEqual(ps[j].coordinates.map((x,i)=>x-ps[j-1].coordinates[i]),d);}}
 assert.equal(points.filter(p=>p.role==='proton').length,12);assert.equal(points.filter(p=>p.role==='electron').length,9);
});
