import test from 'node:test';
import assert from 'node:assert/strict';
import {analyzeRuthenium98Tubing} from '../research/realization-tower/ruthenium-98-tubing.mjs';
test('Ru tubing continuity, sharing and N incidence are counted separately',()=>{
 const {model,network,sharedEdges,audit}=analyzeRuthenium98Tubing();
 assert.equal(audit.strands,16);assert.equal(audit.nativeEdges,78);assert.equal(audit.continuousSegments,22);
 assert.deepEqual(audit.edgeStepHistogram,{'1':2,'2':8,'5':12});assert.equal(audit.junctions,4);assert.equal(audit.closedSegments,0);
 assert.equal(network.segments.flatMap(s=>s.edgeIds).length,78);assert.equal(new Set(network.segments.flatMap(s=>s.edgeIds)).size,78);
 assert(network.junctions.every(j=>j.ports.length===3));assert.equal(sharedEdges.length,2);
 for(const edge of sharedEdges){
  assert.deepEqual(edge.NCells,[]);assert.equal(edge.strands.length,2);
  const [a,b]=edge.strands.map(s=>s.polarities);assert.equal(a.a,b.a);assert.equal(a.p,b.p);assert.equal(a.e,b.e);assert.notEqual(a.b,b.b);
 }
 assert.equal(audit.nativeNCells,20);assert.equal(audit.NIncidentSegments,20);assert.equal(audit.segmentsWithoutN,2);assert.equal(audit.segmentsIncidentToMultipleN,16);
 assert.deepEqual(audit.disconnectedNIncidence.map(g=>g.cell).sort(),['ru:base:50','ru:base:56','ru:base:58','ru:base:59']);
 assert.equal(audit.NChannelCount,null);assert.equal(model.strands.length,16);
});
test('coverage exposes the omitted honeycomb edges and distinguishes 56 vertices from N tubes',()=>{
 const {coverage:c}=analyzeRuthenium98Tubing();
 assert.equal(c.vertices.total,56);assert.equal(c.vertices.visited,52);assert.equal(c.vertices.missing.length,4);
 assert(c.vertices.missing.every(p=>p.filter(x=>x===-1).length===3));
 assert.deepEqual(c.vertices.strata,{corner:4,edge:24,face:24,interior:4});
 assert.deepEqual(c.edges,{total:210,wired:78,unwired:132,surface:150,surfaceWired:70,interior:60,interiorWired:8,horizontal:70});
 assert(c.NCellEdges.every(c=>c.total===12&&c.wired>=3&&c.wired<=5));
 assert.deepEqual(c.slices.map(s=>s.edges),[20,32,36,32,20]);assert.equal(c.minimumMonotoneStrandsForFullEdgeCoverage,36);
});
test('the 64 incidence bijections cannot respect the existing reversal involution',()=>{
 const {network,audit,reversal}=analyzeRuthenium98Tubing();
 // Independent explicit enumeration, rather than the implementation's memoized count.
 const domains=[...network.identities].sort((a,b)=>a.segmentIds.length-b.segmentIds.length),used=new Set();let count=0;
 function visit(i){if(i===domains.length){count++;return;}for(const id of domains[i].segmentIds)if(!used.has(id)){used.add(id);visit(i+1);used.delete(id);}}
 visit(0);assert.equal(count,64);assert.equal(audit.incidencePerfectMatchings,'64');
 assert.equal(reversal.fixedNCells.length,0);assert.equal(reversal.fixedNSegments.length,4);
 assert.equal(audit.reversalEquivariantMatchings,'0');assert.match(reversal.obstruction,/fixed-point/);
});
