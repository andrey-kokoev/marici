import test from 'node:test';import assert from 'node:assert/strict';
import {processState} from '../research/realization-tower/normal-ray-processes.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('edge-seven single shape: no hidden second parent, belt or duplicate terminals',()=>{
 const p=processState('single-octahedral',7,3,1,{complexVisibility:{original:false,clone:false,belt:false}}),g=p.nativeWiringGraph;
 assert.equal(g.nodes.length,679);assert.equal(g.links.length,1624);assert.equal(p.singleOctahedralAudit.shapeCount,1);assert.equal(p.singleOctahedralAudit.bridgeCells,0);assert.equal(p.presentationLabels.length,6);assert.equal(p.retainedBodies.reduce((s,c)=>s+c.faces.length,0),392);assert.ok(p.retainedBodies.every(c=>c.insideNSector&&c.nativeWiring.shape==='single'));
 assert.deepEqual(p.inventory.rows[0],{id:'combined',label:'Single shape',proton:224,neutron:231,electron:224,total:679});assert.deepEqual(p.inventory.cellLocationRows.map(r=>[r.proton,r.neutron,r.electron,r.total]),[[84,146,84,314],[140,85,140,365]]);assert.deepEqual(p.inventory.faceRows.map(r=>[r.proton,r.neutron,r.electron,r.total]),[[196,null,196,392],[84,224,84,392]]);assert.equal(p.emptyRegionAudit.enclosedRegions,85);assert.equal(p.emptyRegionAudit.sharedEmptyFaces,0);assert.equal(p.emptyRegionAudit.edgeTouchComponents,1);assert.ok(p.retainedBodies.filter(c=>c.role==='neutron'&&c.faces.length).every(c=>Object.values(c.faceRoles).every(r=>r==='neutron')));
 const seen=new Set([g.nodes[0].id]);for(let changed=true;changed;){changed=false;for(const e of g.links){assert.equal(e.kind,'native-face');if(seen.has(e.from)||seen.has(e.to))for(const id of[e.from,e.to])if(!seen.has(id)){seen.add(id);changed=true;}}}assert.equal(seen.size,679);
 assert.equal(normalizeSceneSettings({process:{id:'single-octahedral',step:3}}).process.step,3);
});
test('orientation reference can be restored without changing the void inventory',()=>{
 const p=processState('single-octahedral',7,3,1,{singleFaceColoring:'orientation'});assert.ok(p.retainedBodies.every(c=>Object.values(c.faceRoles).every(r=>r!=='neutron')));assert.equal(p.emptyRegionAudit.enclosedRegions,85);
});
test('single shape size options retain whole-cell and face counts',()=>{
 for(const [r,n]of [[0,1],[1,51],[2,245],[3,679]]){const p=processState('single-octahedral',7,r);assert.equal(p.retainedBodies.length,n);assert.equal(p.inventory.cellLocationRows.reduce((s,row)=>s+row.total,0),n);assert.equal(p.inventory.faceRows[0].total,8*(2*r+1)**2);}
});
