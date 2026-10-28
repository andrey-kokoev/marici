import test from 'node:test';import assert from 'node:assert/strict';
import {doubleEsd7RuleProcess,doubleEsd7Rules} from '../research/realization-tower/double-esd7-process.mjs';
import {presentNeutronOccurrenceRefinements} from '../research/realization-tower/neutron-occurrence-refinements.mjs';
import {cellDualGraph} from '../research/realization-tower/cell-dual-graph.mjs';
test('four reflected N occurrences own independent six-cell carriers and retain their face ports',()=>{
 const source=doubleEsd7RuleProcess(7,doubleEsd7Rules.map(r=>r.id)),p=presentNeutronOccurrenceRefinements(source),a=p.neutronRefinementAudit;
 assert.equal(a.complexCount,4);assert.equal(a.internalCellCount,24);assert.equal(a.extraParticleAssignments,0);
 assert.deepEqual(a.complexes.map(c=>c.parentId).sort(),['clone:tet-134','clone:tet-67','original:tet-134','original:tet-61']);
 assert.deepEqual(p.retainedBodies,source.retainedBodies);assert.equal(p.interfaceGuides.filter(g=>g.rimPort||g.connector).length,0);
 const graph=cellDualGraph([...p.retainedBodies,...p.attachmentBodies]);assert.equal(graph.nodes.length,374);
 for(const c of a.complexes){
  assert.equal(c.parentPorts.length,4);assert.ok(c.parentPorts.every(port=>port.childPort===null));
  assert.deepEqual(c.parentPorts.map(port=>port.face),source.retainedBodies.find(b=>b.id===c.parentId).faces);
  const ids=new Set(c.cellIds);assert.equal(ids.size,6);
  for(const id of ids){const links=graph.links.filter(e=>e.from===id||e.to===id);assert.equal(links.length,2);assert.ok(links.every(e=>ids.has(e.from)&&ids.has(e.to)));}
 }
});
