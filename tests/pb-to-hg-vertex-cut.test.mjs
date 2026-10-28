import test from 'node:test';
import assert from 'node:assert/strict';
import {auditPbToHgVertexCuts} from '../research/strominger/pb-to-hg-vertex-cut-audit.mjs';
test('each pair of vertex caps removes two P-N-E chains while retaining the witness matching and connectivity',()=>{
 const audit=auditPbToHgVertexCuts();
 assert.equal(audit.caps.length,4);assert(audit.caps.every(c=>c.separable));
 assert.deepEqual(audit.caps.map(c=>c.chain),[74,28,7,1]);
 assert.equal(audit.pairs.length,6);
 for(const pair of audit.pairs){
  assert.equal(pair.removed.length,6);
  assert.deepEqual([pair.proton,pair.neutron,pair.electron],[80,124,80]);
  assert.equal(pair.retainedWitnesses,44);assert(pair.witnessMatchingIntact);
  assert.equal(pair.connectedComponents,1);
 }
});
