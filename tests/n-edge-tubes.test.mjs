import test from 'node:test';import assert from 'node:assert/strict';
import {buildPESymmetricSector} from '../research/strominger/pe-symmetric-sector.mjs';
import {buildNEdgeTubes} from '../research/strominger/n-edge-tubes.mjs';
import {singleOctahedralProcess} from '../research/realization-tower/single-octahedral-process.mjs';
for(const radius of [0,1,2,3])test(`N edge fibres radius ${radius}: distinct reversible straight paths`,()=>{
 const s=buildPESymmetricSector(radius),t=buildNEdgeTubes(s),passes=new Map(t.passes.map(p=>[p.id,p])),used=t.paths.flatMap(p=>p.passIds),n=2*radius+1;
 assert.equal(t.audit.strandsPerCell,6);assert.equal(t.audit.localPasses,6*s.audit.wholeCells.neutron);assert.equal(t.paths.length,6*n*n);assert.equal(t.audit.sharedEdgeJoins+t.paths.length,t.passes.length);assert.equal(new Set(used).size,t.passes.length);assert.equal(used.length,t.passes.length);assert.equal(new Set(t.paths.flatMap(p=>[p.fromPort,p.toPort])).size,2*t.paths.length);
 for(const c of s.cells.filter(c=>c.role==='neutron'))assert.equal(new Set(t.passes.filter(p=>p.cell===c.id).map(p=>p.axis)).size,6);
 for(const p of t.paths){assert.ok(p.passIds.every(id=>passes.get(id).axis===p.axis));assert.equal(p.points.length,p.passIds.length+1);const delta=p.points[1].map((x,i)=>x-p.points[0][i]);for(let j=1;j<p.points.length;j++)assert.deepEqual(p.points[j].map((x,i)=>x-p.points[j-1][i]),delta);assert.equal(new Set(p.passIds.map(id=>passes.get(id).cell)).size,p.passIds.length);}
 const canonical=t=>t.paths.map(p=>[...p.passIds].sort().join('|')).sort();assert.deepEqual(canonical(t),canonical(buildNEdgeTubes({...s,cells:[...s.cells].reverse()})));
});
test('single viewer overlay is optional and does not merge or replace the cell graph',()=>{
 const off=singleOctahedralProcess(7,3),axis=singleOctahedralProcess(7,3,{nTubeAxis:'0'}),all=singleOctahedralProcess(7,3,{nTubeAxis:'all'});assert.equal(off.interfaceGuides.length,0);assert.equal(axis.interfaceGuides.length,49);assert.equal(all.interfaceGuides.length,294);assert.equal(all.nTubeAudit.localPasses,1386);assert.equal(all.nTubeAudit.sharedEdgeJoins,1092);assert.equal(all.nativeWiringGraph.nodes.length,679);assert.equal(all.emptyRegionAudit.enclosedRegions,85);assert.ok(all.interfaceGuides.every(g=>g.connector&&g.overlay));
});
