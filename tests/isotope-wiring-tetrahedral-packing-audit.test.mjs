import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {classifyTetrahedronPair,auditTetrahedralPacking} from '../examples/isotope-wiring/core/tetrahedral-packing-audit.mjs';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedFullInterface} from '../examples/isotope-wiring/core/stacked-full-interface.mjs';
import {solveTetrahedralDepths} from '../examples/isotope-wiring/core/tetrahedral-depth-constraints.mjs';
const tetra=[[0,0,0],[1,0,0],[0,1,0],[0,0,1]],shift=(p,d)=>p.map(v=>v.map((x,i)=>x+d[i]));
test('separates disjoint tetrahedra, boundary contacts, and positive-volume overlap',()=>{
 assert.equal(classifyTetrahedronPair(tetra,shift(tetra,[2,0,0])).status,'disjoint');assert.equal(classifyTetrahedronPair(tetra,shift(tetra,[1,0,0])).status,'boundary-contact');assert.equal(classifyTetrahedronPair(tetra,tetra.map(([x,y,z])=>[x,-y,-z])).status,'boundary-contact');assert.equal(classifyTetrahedronPair(tetra,tetra.map(([x,y,z])=>[x,y,-z])).status,'boundary-contact');assert.equal(classifyTetrahedronPair(tetra,shift(tetra,[0.1,0.1,0.1])).status,'volume-overlap');assert.equal(classifyTetrahedronPair(tetra,tetra).status,'volume-overlap');assert.equal(classifyTetrahedronPair(tetra,shift(tetra.map(p=>p.map(x=>x*0.2)),[0.1,0.1,0.1])).status,'volume-overlap');
});
test('classification is symmetric and invariant under a shared rigid coordinate change',()=>{
 const transform=points=>points.map(([x,y,z])=>[z+10,x-20,y+30]);for(const delta of [[2,0,0],[1,0,0],[0.1,0.1,0.1]]){const second=shift(tetra,delta),status=classifyTetrahedronPair(tetra,second).status;assert.equal(classifyTetrahedronPair(second,tetra).status,status);assert.equal(classifyTetrahedronPair(transform(tetra),transform(second)).status,status);}
});
test('degenerate cells and invalid tolerances cannot pass the packing check',()=>{
 assert.throws(()=>classifyTetrahedronPair(tetra,[[0,0,0],[1,0,0],[0,1,0],[1,1,0]]),/Degenerate/);assert.throws(()=>classifyTetrahedronPair(tetra,[[NaN,0,0],...tetra.slice(1)]),/finite/);assert.throws(()=>classifyTetrahedronPair(tetra,tetra,{tolerance:0}),/Tolerance/);
});
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),model=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true})),depths=solveTetrahedralDepths(buildStackedFullInterface(model),{allowContactTranslation:true});
test('all sixteen candidate embeddings have thirteen declared contact pairs and no volume overlaps',()=>{
 const before=JSON.stringify(depths),r=auditTetrahedralPacking(depths);assert.equal(JSON.stringify(depths),before);assert.equal(r.status,'verified-for-cell-geometry');assert.equal(r.embeddings,16);for(const result of r.results){assert.deepEqual(result.counts,{pairs:45,disjoint:32,boundaryContacts:13,volumeOverlaps:0,unexpectedContacts:0,missingContacts:0,violatedVertexConstraints:0});assert.equal(result.pairs.filter(p=>p.sharedVertices.length===2).length,8);assert.equal(result.pairs.filter(p=>p.sharedVertices.length===1).length,5);}
});
test('overlap, undeclared contact, and wrong vertex correspondence are independently rejected',()=>{
 const overlap=structuredClone(depths);overlap.solutions=overlap.solutions.slice(0,1);overlap.solutions[0].coordinates['s4-00']=structuredClone(overlap.solutions[0].coordinates['s1-00']);const a=auditTetrahedralPacking(overlap);assert.equal(a.status,'refuted');assert(a.results[0].counts.volumeOverlaps>0);
 const undeclared=structuredClone(depths);undeclared.solutions=undeclared.solutions.slice(0,1);undeclared.constraints=undeclared.constraints.filter(c=>c.support!=='stack:s1-s2');assert(auditTetrahedralPacking(undeclared).results[0].counts.unexpectedContacts>0);
 const mislabeled=structuredClone(depths);mislabeled.solutions=mislabeled.solutions.slice(0,1);const p=mislabeled.solutions[0].coordinates['s1-00'];[p.T,p.B]=[p.B,p.T];const bad=auditTetrahedralPacking(mislabeled);assert.equal(bad.status,'refuted');assert(bad.results[0].counts.violatedVertexConstraints>0);
});
