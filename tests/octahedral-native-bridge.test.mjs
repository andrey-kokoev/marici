import test from 'node:test';import assert from 'node:assert/strict';
import {probeOctahedralNativeBridge} from '../research/strominger/octahedral-native-bridge.mjs';
import {buildPESymmetricSector} from '../research/strominger/pe-symmetric-sector.mjs';
const key=ps=>ps.map(p=>p.join(',')).sort().join('|');
for(const radius of [0,1,2])test(`native growth radius ${radius}: shared faces, balanced fronts and no imported belt`,()=>{
 const p=probeOctahedralNativeBridge(radius),a=p.audit;assert.equal(a.bridgeCells,49);assert.deepEqual(a.bridgeRoles,{proton:16,neutron:17,electron:16});assert.equal(a.shortestFaceSteps,8);assert.equal(a.shortestPaths,'576');assert.equal(a.dualClosed,true);assert.equal(a.attachmentFaces,8);assert.equal(a.pointOnlyLinks,0);assert.equal(a.nonmanifoldBoundaryEdges,0);
 for(const layer of a.distanceLayers)assert.equal(layer.proton,layer.electron);
 // The whole corridor is precisely a native edge-three octahedron, with its
 // two polar N cells already present in the parent complexes (not duplicated).
 assert.deepEqual(p.corridorCells.map(c=>key(c.vertices)).sort(),buildPESymmetricSector(1).cells.map(c=>key(c.vertices)).sort());
 for(const id of p.terminals){assert.equal(p.corridorCells.find(c=>c.id===id).role,'neutron');assert.equal(p.assemblyCells.filter(c=>c.id===id).length,1);const fs=p.attachmentFaces.filter(f=>f.owners.includes(id));assert.equal(fs.length,4);assert.equal(fs.filter(f=>f.role==='proton').length,2);assert.equal(fs.filter(f=>f.role==='electron').length,2);}
 const cells=new Map(p.assemblyCells.map(c=>[c.id,c])),seen=new Set([p.terminals[0]]);for(const f of p.connections){assert.equal(f.owners.length,2);for(const id of f.owners)assert.ok(cells.get(id).faces.some(face=>key(face)===key(f.vertices)));}
 for(let change=true;change;){change=false;for(const f of p.connections)if(f.owners.some(id=>seen.has(id)))for(const id of f.owners)if(!seen.has(id)){seen.add(id);change=true;}}assert.equal(seen.size,cells.size);
 const vs=new Set(),es=new Set();for(const f of p.boundary){for(const v of f.vertices)vs.add(v.join(','));for(let i=0;i<3;i++)es.add(key([f.vertices[i],f.vertices[(i+1)%3]]));}assert.equal(vs.size-es.size+p.boundary.length,2);
});
test('corridor does not depend on the artificial search boundary',()=>{
 for(const r of [0,1,2]){const a=probeOctahedralNativeBridge(r),b=probeOctahedralNativeBridge(r,1);assert.deepEqual(a.bridgeCells.map(c=>c.id).sort(),b.bridgeCells.map(c=>c.id).sort());assert.deepEqual(a.audit,b.audit);}
});
