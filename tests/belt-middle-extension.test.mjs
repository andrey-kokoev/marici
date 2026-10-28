import test from 'node:test';import assert from 'node:assert/strict';
import {buildCentralTerminalWiring,buildCentralBeltLayout} from '../research/realization-tower/central-belt-layout.mjs';
import {beltViewerPoint} from '../research/realization-tower/neutron-belt-process.mjs';
import {geometryBeltSurface} from '../examples/normal-ray/belt-geometry-layout.js';
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
test('staggered extension has 32P/32E exposed faces, whole native cells and a connected closed boundary',()=>{
 const source=buildCentralTerminalWiring().surface,layout=buildCentralBeltLayout(),snapshot=JSON.stringify(source),s=geometryBeltSurface(source,{...layout,origin:beltViewerPoint(layout.origin)}),c=s.cellulation;
 assert.deepEqual(s.counts,{vertices:34,edges:96,faces:64,euler:2});assert.deepEqual([s.extension.P,s.extension.E],[32,32]);assert.deepEqual([c.counts.tetrahedra,c.counts.octahedra],[20,14]);assert.equal(c.counts.internalFaces,64);
 const seen=new Set();for(const cell of c.cells){const vs=cell.indices.map(i=>c.nativeVertices[i]);assert.ok(!seen.has(key(vs)));seen.add(key(vs));for(const v of vs){assert.ok(v.every(Number.isInteger));assert.equal(v.reduce((a,b)=>a+b,0),1);}
  for(const w of cell.witnesses){const template=source.cellulation.cells.find(t=>t.sourceGeometry===w.sourceGeometry);assert.equal(key(vs),key(template.indices.map(i=>source.cellulation.nativeVertices[i].map((v,j)=>v+w.translation[j]))));}
 }
 for(const f of c.faces)assert.ok(f.owners.length===1||f.owners.length===2);
 const reached=new Set([c.cells[0].id]);let changed=true;while(changed){changed=false;for(const f of c.faces)if(f.owners.some(id=>reached.has(id)))for(const id of f.owners)if(!reached.has(id)){reached.add(id);changed=true;}}assert.equal(reached.size,34);
 for(const edge of s.edges){assert.equal(edge.faces.length,2);const signs=edge.faces.map(id=>{const face=s.faces.find(f=>f.id===id),i=face.indices.indexOf(edge.indices[0]);return face.indices[(i+1)%3]===edge.indices[1]?1:-1;});assert.equal(signs[0]+signs[1],0);}
 for(const i of s.extension.poleIndices){const neighbors=s.edges.filter(e=>e.indices.includes(i));assert.equal(neighbors.length,4);}
 assert.equal(JSON.stringify(source),snapshot);
});
