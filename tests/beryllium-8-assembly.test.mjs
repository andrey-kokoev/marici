import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildBeryllium8Reference} from '../research/realization-tower/beryllium-8-reference.mjs';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {buildSulfurRouteComparison} from '../research/realization-tower/sulfur-route-comparison.mjs';
import {buildBerylliumDirectionComponents} from '../research/realization-tower/beryllium-8-direction-components.mjs';
import {buildBeryllium8Assembly} from '../research/realization-tower/beryllium-8-assembly.mjs';
const reference=buildBeryllium8Reference(),columns=buildSulfurRouteComparison(buildBranchingSeed({processId:'beryllium-8'}),{reference}).reference,assembly=buildBeryllium8Assembly(columns,reference);
const key=p=>p.join(','),distance=(a,b)=>Math.hypot(...a.map((x,i)=>x-b[i]));
test('isometric carrier is an octahedron: six vertices, twelve native edges, degree four and eight faces',()=>{
 assert.deepEqual(assembly.audit,{vertices:6,edges:12,strands:8,polarityArrows:12,routeArrows:12,displayLaneOffset:.04});
 const adjacency=new Map(assembly.vertices.map(p=>[key(p),new Set()]));
 for(const edge of assembly.edges){const [a,b]=edge.guide;assert(Math.abs(distance(a,b)-Math.sqrt(2))<1e-12);adjacency.get(key(a)).add(key(b));adjacency.get(key(b)).add(key(a));assert.equal(edge.strandIds.length,2);}
 assert([...adjacency.values()].every(n=>n.size===4));
 let faces=0;const vertices=[...adjacency.keys()];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)if(adjacency.get(vertices[i]).has(vertices[j])&&adjacency.get(vertices[j]).has(vertices[k])&&adjacency.get(vertices[k]).has(vertices[i]))faces++;
 assert.equal(faces,8);
});
test('all eight complete strand routes retain identity, exact endpoints and three native edge memberships',()=>{
 for(const s of assembly.strands){
  const source=columns.find(c=>c.id===s.id);assert.equal(s.inputSlot,source.inputSlot);assert.equal(s.outputSlot,source.outputSlot);assert.deepEqual(s.colours,source.colours);
  assert.deepEqual(s.guide[0],assembly.inputPole);assert.deepEqual(s.guide.at(-1),assembly.outputPole);assert.equal(s.runs.length,3);
  for(const [i,run] of s.runs.entries()){
   assert.equal(run.edgeId,source.edgeIds[i]);assert.deepEqual(run.points[0],s.guide[i]);assert.deepEqual(run.points.at(-1),s.guide[i+1]);
   assert(run.points.flat().every(Number.isFinite));
  }
  assert.equal(s.arrows.length,3);
  for(const arrow of s.arrows){assert.equal(arrow.kind,source.polarityDirection?'polarity':'route');const delta=s.guide[arrow.segment+1].map((x,i)=>x-s.guide[arrow.segment][i]);assert(Math.sign(delta.reduce((sum,x,i)=>sum+x*arrow.direction[i],0))===(source.polarityDirection||1));}
  for(const arrow of s.arrows)assert.deepEqual(arrow.point,s.runs[arrow.segment].points[8]);
 }
 for(const edge of assembly.edges){
  const midpoints=edge.strandIds.map(id=>assembly.strands.find(s=>s.id===id).runs.find(r=>r.edgeId===edge.id).points[8]);
  assert(Math.abs(distance(...midpoints)-.08)<1e-12);
 }
});
test('component assemblies change only colours; native reference and display lanes are not rewired',()=>{
 const before=JSON.stringify(reference);
 for(const row of buildBerylliumDirectionComponents(columns)){
  const model=buildBeryllium8Assembly(row.columns,reference);assert.deepEqual(model.edges,assembly.edges);
  for(const s of model.strands){const original=assembly.strands.find(c=>c.id===s.id);for(const k of ['guide','runs','points','arrows','inputSlot','outputSlot'])assert.deepEqual(s[k],original[k]);assert.deepEqual(s.colours,row.columns.find(c=>c.id===s.id).colours);}
 }
 assert.equal(JSON.stringify(reference),before);assert.throws(()=>buildBeryllium8Assembly(columns.slice(1),reference));
});
