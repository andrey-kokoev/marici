import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {buildStackedFullInterface} from '../examples/isotope-wiring/core/stacked-full-interface.mjs';
import {solveTetrahedralDepths} from '../examples/isotope-wiring/core/tetrahedral-depth-constraints.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),b=buildLayeredCalcium(d,c.IsotopeWiring.renderSVG(d,{interactive:true})),full=buildStackedFullInterface(b);
const solve=()=>solveTetrahedralDepths(full,{allowContactTranslation:true}),near=(a,b)=>Math.abs(a-b)<1e-8;
test('fixed display projection cannot realize the declared cell contact',()=>{
 assert.throws(()=>solveTetrahedralDepths(full),/required relative translation \[0,-20\]/);const r=solve();for(const s of r.solutions)for(const [cell,offset] of Object.entries(s.projectedTranslations))assert.deepEqual(offset,cell.startsWith('s2-')?[0,-20]:[0,0]);
});
test('all 1024 binary lifts are checked and sixteen satisfy the stated incidence constraints',()=>{
 const before=JSON.stringify(full),r=solve();assert.equal(JSON.stringify(full),before);assert.deepEqual(r.counts,{cells:10,contactConstraints:21,signAssignments:1024,admissibleSignAssignments:16,geometricComponents:3,relativeComponentDepthOffsets:2});assert.equal(new Set(r.solutions.map(s=>s.mask)).size,16);assert.equal(r.allPositiveControl.admissible,false);assert(r.allPositiveControl.violations.length>0);assert.equal(r.relations.length,12);
});
test('every retained solution independently realizes all vertex contacts and six equal tetrahedral edges',()=>{
 const r=solve();for(const s of r.solutions){for(const contact of r.constraints){const a=s.coordinates[r.cells[contact.a].id][contact.fromPort],b=s.coordinates[r.cells[contact.b].id][contact.toPort];assert(a.every((x,i)=>near(x,b[i])));}
  for(const cell of r.cells){const points=Object.values(s.coordinates[cell.id]);for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)assert(near(Math.hypot(...points[i].map((x,k)=>x-points[j][k])),2*cell.radius));}
 }
});
test('shell assembly constrains internal sign relations without selecting shell-1 relative handedness',()=>{
 const r=solve();for(const relation of r.relations)assert(r.solutions.every(s=>(s.signs[relation.cells[0]]===s.signs[relation.cells[1]])===(relation.relation==='same-depth-sign')));
 assert.deepEqual([...new Set(r.solutions.map(s=>s.signs['s1-00']*s.signs['s2-01']))].sort(),[-1,1]);assert(!r.relations.some(relation=>relation.cells.some(id=>id.startsWith('s1-'))));
});
test('rejects unprovided mediator geometry and oversized or malformed enumeration inputs',()=>{
 assert.throws(()=>solveTetrahedralDepths(buildStackedFullInterface(b,{mode:'neutron-mediated'})),/mediator extent/);assert.throws(()=>solveTetrahedralDepths(full,{maxCells:9}),/bound/);
 const bad=structuredClone(full);bad.model.topology.vertices.find(v=>v.id==='space:s1-00:T').position[0]+=1;assert.throws(()=>solveTetrahedralDepths(bad,{allowContactTranslation:true}),/square projection/);
});
