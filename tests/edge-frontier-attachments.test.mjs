import test from 'node:test';
import assert from 'node:assert/strict';
import {auditFrontierAttachments} from '../research/realization-tower/edge-frontier-attachments.mjs';
test('k4 missing face supports belong to one octahedron attached through opposite N edges',()=>{
 for(const branch of [1,3]){
  const a=auditFrontierAttachments(4,branch);
  assert.deepEqual(a.newAssignments,[]);assert.deepEqual(a.eligibleInteriorCells,[]);
  assert.deepEqual(a.frontier.map(f=>f.cell),[132,127]);
  assert.deepEqual(a.frontier.map(f=>f.assignedFaceNeighbors.length),[1,1]);
  assert.deepEqual(a.frontier.map(f=>f.missingSupports.map(s=>s.cell)),[[333],[331]]);
  assert(a.frontier.every(f=>f.missingSupports.every(s=>s.assignedFaceNeighbors.length===0)));
  assert.equal(a.dependencyGroups.length,1);
  const group=a.dependencyGroups[0];assert(group.unassigned);
  assert.deepEqual(group.cells.map(c=>c.cell),[331,332,333,334]);
  assert.deepEqual(group.assignedExternalFaceContacts,[]);
  assert(group.pairedOppositeEdges);
  assert.deepEqual(group.assignedEdgeContacts.map(c=>c.cell).sort((x,y)=>x-y),[313,339]);
  assert(group.assignedEdgeContacts.every(c=>c.role==='neutron'&&c.edge.length===2));
 }
});
