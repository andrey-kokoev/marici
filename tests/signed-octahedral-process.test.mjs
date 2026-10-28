import test from 'node:test';import assert from 'node:assert/strict';
import {processState,processes} from '../research/realization-tower/normal-ray-processes.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
const state=(r,options={})=>processState('signed-octahedral-belt',7,r,1,options);
for(const r of [0,1,2,3])test(`signed octahedral assembly radius ${r}: whole cells, six ports each, two contacts and connected dual`,()=>{
 const p=state(r),a=p.signedOctahedralAudit,g=p.nativeWiringGraph;assert.equal(a.ports.length,12);for(const copy of ['original','clone'])assert.deepEqual(a.ports.filter(x=>x.copy===copy).map(x=>x.text),['+P','−P','+N','−N','+E','−E']);
 assert.ok(p.retainedBodies.every(b=>b.insideNSector===true));
 const contacts=g.links.filter(e=>e.kind==='native-tip-contact');assert.equal(contacts.length,2);const ns=new Map(g.nodes.map(n=>[n.id,n]));for(const e of contacts)for(const id of[e.from,e.to])assert.ok(ns.get(id).body.vertices.some(v=>Math.hypot(...worldPoint(v).map((x,i)=>x-e.point[i]))<1e-8));
 const reached=new Set([g.nodes[0].id]);for(let changed=true;changed;){changed=false;for(const e of g.links){assert.equal(e.directed,false);if(reached.has(e.from)||reached.has(e.to))for(const id of[e.from,e.to])if(!reached.has(id)){reached.add(id);changed=true;}}}assert.equal(reached.size,g.nodes.length);
 assert.equal(p.inventory.rows[0].proton,p.inventory.rows[0].electron);assert.equal(p.inventory.rows[1].total,34);for(const role of ['proton','neutron','electron','total'])assert.equal(p.inventory.cellLocationRows.reduce((s,row)=>s+row[role],0),p.inventory.rows.at(-1)[role]);assert.equal(p.inventory.faceRows[0].total+p.inventory.faceRows[1].total,p.inventory.faceRows[2].total);
 // Every rendered native triangle retains the belt's same physical unit edge.
 let edge;for(const b of p.retainedBodies)for(const f of b.faces){const ps=f.map(worldPoint);for(let i=0;i<3;i++){const d=Math.hypot(...ps[i].map((x,j)=>x-ps[(i+1)%3][j]));edge??=d;assert.ok(Math.abs(d-edge)<1e-8);assert.ok(b.faceRoles[f.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|')]);}}
});
test('independent registry, inventory, visibility and persisted size',()=>{
 assert.ok(processes.some(p=>p.id==='signed-octahedral-belt'));const p=state(2);assert.deepEqual(p.inventory.rows.at(-1),{id:'combined',label:'Combined total',proton:170,neutron:184,electron:170,total:524});assert.equal(p.nativeWiringGraph.links.length,1186);
 assert.equal(state(2,{complexVisibility:{original:false}}).nativeWiringGraph.nodes.length,279);assert.equal(state(2,{complexVisibility:{belt:false}}).nativeWiringGraph.nodes.length,490);
 const saved=normalizeSceneSettings({process:{id:'signed-octahedral-belt',k:7,step:2}});assert.equal(saved.process.id,'signed-octahedral-belt');assert.equal(saved.process.step,2);
});
