import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {buildPESymmetricSector} from '../research/strominger/pe-symmetric-sector.mjs';
import {buildFiveSideOctRoutingObligations} from '../research/realization-tower/five-side-oct-routing-obligations.mjs';

test('obligation contract preserves provenance and leaves all construction gates open',async()=>{
 const c=JSON.parse(await fs.readFile('research/strominger/contracts/five-side-oct-routing-obligations-v1.json','utf8')),sources=new Map(c.sources.map(s=>[s.id,s]));
 assert.equal(c.constructionAdmitted,false);assert.equal(c.status,'specification-and-obligations-only');
 for(const s of sources.values())if(s.path)await fs.access(s.path);
 const ids=[...c.requirements,...c.bindings,...c.completionGates].map(x=>x.id);assert.equal(new Set(ids).size,ids.length);
 for(const r of c.requirements){assert(r.witness.length>0);assert(r.sources.every(id=>sources.has(id)));assert(r.sources.some(id=>['operator-instruction','operator-directed-document'].includes(sources.get(id).kind)));}
 for(const g of c.completionGates){assert.equal(g.status,'open');assert(g.requires.every(id=>ids.includes(id)));}
 assert(c.bindings.every(b=>b.status==='open'));assert(c.unvalidatedConventions.some(c=>c.id==='posthoc-coherence-groups'));
});
test('whole carrier sites are retained without selecting any wires, seams or groups',()=>{
 const m=buildFiveSideOctRoutingObligations();
 assert.deepEqual(m.inventory,{cells:245,P:80,N:85,E:80,faceOccurrences:1320,nativeFaces:760,nativeEdges:660,sharedInterfaces:560,boundaryOccurrences:200,oppositeFaceSites:340});
 assert.equal(m.constructionAdmitted,false);assert.deepEqual(m.selectedRoutes,[]);assert.deepEqual(m.selectedGroups,[]);assert.deepEqual(m.selectedEndpointMatches,[]);
 const ports=new Map(m.ports.map(p=>[p.id,p]));assert.equal(ports.size,1320);
 for(const f of m.interfaces){assert.equal(f.witness,null);assert.equal(f.ports.length,2);assert.equal(ports.get(f.ports[0]).face,ports.get(f.ports[1]).face);assert.notEqual(ports.get(f.ports[0]).cell,ports.get(f.ports[1]).cell);}
 for(const b of m.boundaries){assert.equal(b.continuation,null);assert.equal(b.witness,null);assert(ports.has(b.port));}
 for(const n of m.oppositeFaceSites){assert.equal(n.channelWitness,null);assert(n.ports.every(p=>ports.get(p).cell===n.cell&&ports.get(p).axis===n.axis));}
});
test('source-specified entry comparisons have actual shared references in all six readings',()=>{
 for(const radius of [1,2]){
  const sector=buildPESymmetricSector(radius),m=buildFiveSideOctRoutingObligations(sector);
  const adjacent=(a,b)=>sector.faces.some(f=>f.owners.includes(a)&&f.owners.includes(b));
  assert.equal(m.readings.length,6);
  for(const r of m.readings){
   assert.equal(r.comparisons.length,4);assert.equal(r.outer.length,8);assert.equal(r.contexts.length,4);
   assert.equal(r.comparisons.filter(c=>c.kind==='compare-P-at-shared-E').length,2);
   assert.equal(r.comparisons.filter(c=>c.kind==='compare-E-at-shared-P').length,2);
   for(const c of r.comparisons){assert(c.inputs.every(id=>adjacent(id,c.cell)&&adjacent(id,c.sharedReference)));assert.equal(c.comparisonWitness,null);assert.equal(c.outputPairing,null);}
   for(const context of r.contexts){assert(adjacent(context.channelOccurrence,context.P));assert(adjacent(context.channelOccurrence,context.E));assert.equal(context.signBinding,null);}
   assert.equal(r.layerProfile.length,radius===1?9:17);
  }
  assert.deepEqual(m.readings[0].layerProfile,m.readings[5].layerProfile);
 }
});
test('enumeration order and arbitrary cell labels cannot select different obligations',()=>{
 const s=buildPESymmetricSector(2),a=buildFiveSideOctRoutingObligations(s);
 const reversed={...s,cells:[...s.cells].reverse().map(c=>({...c,faces:[...c.faces].reverse()})),faces:[...s.faces].reverse().map(f=>({...f,owners:[...f.owners].reverse()}))};
 assert.deepEqual(buildFiveSideOctRoutingObligations(reversed),a);
 const rename=new Map(s.cells.map((c,i)=>[c.id,`renamed-cell:${String(s.cells.length-i).padStart(4,'0')}`])),restore=new Map([...rename].map(([a,b])=>[b,a]));
 const b=buildFiveSideOctRoutingObligations({...s,cells:s.cells.map(c=>({...c,id:rename.get(c.id)})),faces:s.faces.map(f=>({...f,owners:f.owners.map(id=>rename.get(id))}))});
 assert.deepEqual(b.inventory,a.inventory);
 const comparisons=(m,restore=id=>id)=>new Set(m.readings.flatMap(r=>r.comparisons.map(c=>[r.axis.join(','),r.sign,c.kind,restore(c.cell),restore(c.sharedReference),...c.inputs.map(restore).sort()].join('|'))));
 assert.deepEqual(comparisons(b,id=>restore.get(id)),comparisons(a));
 assert.deepEqual(new Set(b.ports.map(p=>`${restore.get(p.cell)}|${p.face}|${p.axis}`)),new Set(a.ports.map(p=>`${p.cell}|${p.face}|${p.axis}`)));
});
