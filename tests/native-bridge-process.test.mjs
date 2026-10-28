import test from 'node:test';import assert from 'node:assert/strict';
import {processState} from '../research/realization-tower/normal-ray-processes.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
const get=(r=2,v={})=>processState('native-octahedral-bridge',7,r,1,{complexVisibility:v});
for(const [r,n,links,faces]of [[0,51,104,72],[1,151,312,200],[2,539,1224,456]])test(`native bridge viewer radius ${r}`,()=>{
 const p=get(r);for(const role of ['proton','neutron','electron','total'])assert.equal(p.inventory.cellLocationRows.reduce((s,row)=>s+row[role],0),p.inventory.rows.at(-1)[role]);assert.equal(p.nativeWiringGraph.nodes.length,n);assert.equal(p.nativeWiringGraph.links.length,links);assert.ok(p.nativeWiringGraph.links.every(e=>e.kind==='native-face'&&e.directed===false));assert.equal(p.retainedBodies.reduce((s,c)=>s+c.faces.length,0),faces);assert.ok(p.retainedBodies.every(c=>c.insideNSector));assert.equal(p.presentationLabels.length,12);assert.equal(p.inventory.faceRows.at(-1).total,faces);assert.equal(p.inventory.faceRows.at(-1).proton,faces/2);assert.equal(p.inventory.faceRows.at(-1).electron,faces/2);assert.equal(p.inventory.faceRows.at(-1).neutron,null);assert.equal(p.inventory.faceRows[0].total+p.inventory.faceRows[1].total,faces);assert.equal(new Set(p.retainedBodies.map(c=>c.id)).size,n);assert.equal(p.nativeBridgeAudit.visibleSharedTerminals,2);
 for(const body of p.retainedBodies)for(const face of body.faces)assert.ok(body.faceRoles[face.map(p=>p.join(',')).sort().join('|')]);
});
test('shared terminals have union visibility; interior faces exposed when parts hidden',()=>{
 assert.equal(get(2,{original:false}).retainedBodies.length,295);assert.deepEqual(get(2,{original:false}).inventory.faceRows,get().inventory.faceRows);assert.deepEqual(get(2,{original:false}).inventory.cellLocationRows,get().inventory.cellLocationRows);const bridge=get(2,{original:false,clone:false});assert.equal(bridge.retainedBodies.length,51);assert.equal(bridge.nativeWiringGraph.links.length,104);assert.equal(bridge.retainedBodies.reduce((s,c)=>s+c.faces.length,0),72);
 assert.equal(get(2,{belt:false}).retainedBodies.length,490);assert.equal(get(2,{original:false,clone:false,belt:false}).retainedBodies.length,0);
 const full=get();assert.deepEqual(full.inventory.rows.at(-1),{id:'combined',label:'Combined total',proton:176,neutron:187,electron:176,total:539});assert.equal(normalizeSceneSettings({process:{id:'native-octahedral-bridge',step:2}}).process.id,'native-octahedral-bridge');
});
