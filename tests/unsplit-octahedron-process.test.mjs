import test from 'node:test';
import assert from 'node:assert/strict';
import {unsplitOctahedronProcess} from '../research/realization-tower/unsplit-octahedron-process.mjs';
import {normalizeSceneSettings} from '../examples/normal-ray/settings.js';
test('one unsplit regular octahedron has only its twelve boundary edges',()=>{
 const p=unsplitOctahedronProcess(7,0),a=p.octahedronAudit;
 assert.equal(a.vertices.length,6);assert.equal(a.edges.length,12);assert.equal(a.faceIndices.length,8);
 assert.equal(p.retainedBodies.length,1);assert.deepEqual(p.retainedBodies[0].components,[]);
 assert.equal(p.retainedBodies[0].faces.length,8);assert.equal(a.internalEdges,0);
 for(const [i,j] of a.edges){assert.equal(a.vertices[i].reduce((s,x,k)=>s+(x-a.vertices[j][k])**2,0),2);assert.equal(a.faceIndices.filter(f=>f.includes(i)&&f.includes(j)).length,2);}
 assert.equal(p.interfaceGuides.length,0);
});
test('two sides retain each face without creating extra solids',()=>{
 const p=unsplitOctahedronProcess(7,1);
 assert.equal(p.interfaceGuides.length,16);assert.equal(p.retainedBodies.length,1);assert.equal(p.canAdvance,false);
 for(const side of p.octahedronAudit.sides)side.point.forEach((x,i)=>assert.ok(Math.abs(side.outward[i]+side.inward[i]-2*x)<1e-12));
 assert.throws(()=>unsplitOctahedronProcess(7,2));
 const s=normalizeSceneSettings({process:{id:'unsplit-octahedron',step:55,k:3}});
 assert.equal(s.process.step,1);assert.equal(s.process.k,7);
});
