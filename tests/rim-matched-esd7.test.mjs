import test from 'node:test';import assert from 'node:assert/strict';
import {buildRimMatchedEsd7} from '../research/realization-tower/rim-matched-esd7.mjs';
import {presentRimAssembly} from '../research/realization-tower/rim-assembly-presentation.mjs';
import {doubleEsd7RuleProcess,doubleEsd7Rules} from '../research/realization-tower/double-esd7-process.mjs';
import {buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
import {worldPoint} from '../research/realization-tower/normal-ray-model.mjs';
import {cellDualGraph} from '../research/realization-tower/cell-dual-graph.mjs';
const distance=(a,b)=>Math.hypot(...a.map((x,i)=>x-b[i]));
test('source rim placement preserves parent metrics and separates interiors',()=>{
 const a=buildRimMatchedEsd7(),original=new Map(buildFoldedFibration().occurrences.map(b=>[b.id,b]));
 assert.equal(a.parents.length,350);assert.equal(a.bodies.length,6);assert.equal(a.audit.capConesAdded,0);
 const graph=cellDualGraph(a.bodies);assert.equal(graph.nodes.length,6);assert.equal(graph.links.length,6);
 for(const b of a.bodies)assert.equal(graph.links.filter(e=>e.from===b.id||e.to===b.id).length,2);
 assert.equal(cellDualGraph([...a.parents,...a.bodies]).nodes.length,356);
 for(const p of a.ports){assert.ok(p.maxVertexGap<1e-12);const y=worldPoint(p.target[0])[1];for(const b of a.parents.filter(b=>b.copy===p.copy))for(const v of b.vertices)assert.ok(p.copy==='original'?worldPoint(v)[1]<=y+1e-10:worldPoint(v)[1]>=y-1e-10);}
 for(const b of a.parents){const old=original.get(b.id);for(let i=0;i<b.vertices.length;i++)for(let j=i+1;j<b.vertices.length;j++)assert.ok(Math.abs(distance(worldPoint(b.vertices[i]),worldPoint(b.vertices[j]))-distance(worldPoint(old.vertices[i]),worldPoint(old.vertices[j])))<1e-10);}
 const lo=worldPoint(a.ports[0].target[0])[1],hi=worldPoint(a.ports[1].target[0])[1];assert.ok(lo<hi);
 for(const b of a.bodies)for(const v of b.vertices)assert.ok(worldPoint(v)[1]>=lo-1e-10&&worldPoint(v)[1]<=hi+1e-10);
});
test('presentation retains all parent assignments and makes 42 actual rim-edge contacts',()=>{
 const source=doubleEsd7RuleProcess(7,doubleEsd7Rules.map(r=>r.id)),p=presentRimAssembly(source);
 assert.equal(p.rimAssemblyAudit.rimEdgeLinks,42);assert.equal(p.interfaceGuides.filter(g=>g.rimPort).length,42);
 assert.deepEqual(p.retainedBodies.map(b=>[b.id,b.role]),source.retainedBodies.map(b=>[b.id,b.role]));assert.ok(p.attachmentBodies.every(b=>b.role===null));assert.equal(p.doubleEsd7Audit.sharedInterface,false);
});
