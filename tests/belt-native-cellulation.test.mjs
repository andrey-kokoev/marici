import test from 'node:test';import assert from 'node:assert/strict';
import {buildCentralTerminalWiring,centralParentPoint} from '../research/realization-tower/central-belt-layout.mjs';
import {buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
const distance=(a,b)=>Math.hypot(...a.map((v,i)=>v-b[i])),key=vs=>vs.map(v=>v.join(',')).sort().join('|');
test('belt uses 8 tetrahedra and 6 whole octahedra drawn exactly from ESD7 source cells',()=>{
 const s=buildCentralTerminalWiring().surface,c=s.cellulation,source=buildFoldedFibration().geometry;
 assert.deepEqual(c.counts,{vertices:19,edges:60,faces:56,cells:14,tetrahedra:8,octahedra:6,internalFaces:24});assert.equal(c.vertices.length-c.edges.length+c.faces.length-c.cells.length,1);
 for(const cell of c.cells){const original=source.find(o=>o.id===cell.sourceGeometry);assert.ok(original);assert.equal(cell.kind,original.kind);assert.equal(key(cell.indices.map(i=>c.nativeVertices[i])),key(original.vertices));assert.equal(cell.faces.length,cell.kind==='octahedron'?8:4);assert.deepEqual(cell.faces.map(id=>key(c.faces.find(f=>f.id===id).indices.map(i=>c.nativeVertices[i]))).sort(),original.faces.map(key).sort());}
 assert.equal(c.faces.filter(f=>f.owners.length===1).length,32);assert.equal(c.faces.filter(f=>f.owners.length===2).length,24);
 const reached=new Set([c.cells[0].sourceGeometry]);let prior=-1;while(prior!==reached.size){prior=reached.size;for(const f of c.faces)if(f.owners.some(id=>reached.has(id)))f.owners.forEach(id=>reached.add(id));}assert.equal(reached.size,14);
});
test('rigid belt placement preserves all native distances and the displayed parents unit edge',()=>{
 const c=buildCentralTerminalWiring().surface.cellulation,parent=buildFoldedFibration().occurrences.find(o=>o.copy==='original'),face=parent.faces[0],unit=distance(worldPoint(centralParentPoint(face[0],'original')),worldPoint(centralParentPoint(face[1],'original')));
 assert.ok(Math.abs(unit-c.unitEdge)<1e-12);for(const e of c.edges)assert.ok(Math.abs(distance(...e.indices.map(i=>c.vertices[i]))-unit)<1e-12);
 for(let i=0;i<c.vertices.length;i++)for(let j=0;j<i;j++)assert.ok(Math.abs(distance(c.vertices[i],c.vertices[j])-distance(worldPoint(c.nativeVertices[i]),worldPoint(c.nativeVertices[j])))<1e-12);
 assert.equal(c.parentLatticeAttachment.status,'central-unit-face-docked');assert.ok(c.parentLatticeAttachment.caps.every(c=>c.faceError<1e-12));
});
