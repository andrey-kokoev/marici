import test from 'node:test';import assert from 'node:assert/strict';
import {buildPneInventory,exposedParentFaces} from '../examples/normal-ray/pne-inventory.js';
import {buildParentCellulations} from '../examples/normal-ray/parent-cellulation.js';
import {presentCentralBelt} from '../research/realization-tower/central-belt-layout.mjs';
import {doubleEsd7RuleProcess,doubleEsd7Rules} from '../research/realization-tower/double-esd7-process.mjs';
const values=r=>[r.proton,r.neutron,r.electron,r.total];
test('parents and belt share native face counting and whole-octahedron filler counting',()=>{
 const p=presentCentralBelt(doubleEsd7RuleProcess(7,doubleEsd7Rules.map(r=>r.id))),snapshot=JSON.stringify(p),inventory=buildPneInventory(p),rows=Object.fromEntries(inventory.rows.map(r=>[r.id,r]));
 assert.deepEqual(values(rows.original),[109,56,87,252]);assert.deepEqual(values(rows.clone),[109,56,87,252]);assert.deepEqual(values(rows['parents-exposed']),[218,112,174,504]);assert.deepEqual(values(rows['belt-faces']),[32,14,32,78]);assert.deepEqual(values(rows.combined),[250,126,206,582]);assert.equal(inventory.unassigned,0);assert.equal(inventory.exposedParentFaceCount,392);assert.equal(inventory.neutronFillerCells,112);
 assert.deepEqual(inventory.displayRows.map(r=>r.id),['parents-exposed','belt-faces','combined']);
 const faces=exposedParentFaces(p);for(const id of p.parentTipReplacementAudit.cellIds){const tips=faces.filter(f=>f.owner===id);assert.equal(tips.length,3);assert.ok(tips.every(f=>f.role==='electron'));}
 for(const parent of buildParentCellulations(p)){assert.deepEqual(parent.counts,{tetrahedra:119,octahedra:56,exposedFaces:196});for(const e of parent.edges){const [a,b]=e.indices.map(i=>parent.vertices[i]);assert.ok(Math.abs(Math.hypot(...a.map((v,i)=>v-b[i]))-p.beltSurface.cellulation.unitEdge)<1e-10);}assert.ok(parent.faces.every(f=>['proton','electron'].includes(f.colorRole)));}
 assert.equal(JSON.stringify(p),snapshot);
});
test('native structural counts are independent of growth-rule assignment colors',()=>{
 const partial=buildPneInventory(presentCentralBelt(doubleEsd7RuleProcess(7,['P-branch']))),full=buildPneInventory(presentCentralBelt(doubleEsd7RuleProcess(7,doubleEsd7Rules.map(r=>r.id))));assert.deepEqual(partial,full);
});
