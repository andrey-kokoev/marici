import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {heliumCandidate,heliumCarriers} from '../examples/realization-lattice/helium.js';
import {makeLattice,key} from '../examples/realization-lattice/geometry.js';
test('six retained constituent tetrahedra map exactly onto FCC sites',()=>{
  const items=heliumCarriers(.67),l=makeLattice(2,.67);
  assert.deepEqual(items.map(i=>i.label),['P1','N1','E1','P2','E2','N2']);
  for(const species of ['proton','neutron','electron'])assert.equal(items.filter(i=>i.species===species).length,2);
  for(const item of items){assert.equal(item.positions.length,4);item.indices.forEach((m,i)=>assert.deepEqual(item.positions[i],l.vertices[l.lookup.get(key(m))].position));}
  // P1-N1-E1 and P2-N1-E2 retain their complete shared faces.
  const shared=(a,b)=>a.indices.filter(p=>b.indices.some(q=>key(p)===key(q))).length;
  for(const [a,b] of [[0,1],[1,2],[3,1],[1,4],[0,5],[3,5]])assert.equal(shared(items[a],items[b]),3);
});
test('viewer candidate is the tested helium ring, on actual lattice vertices',()=>{
  const receipt=JSON.parse(readFileSync(new URL('../research/realization-tower/results/helium-role-test-v1.json',import.meta.url)));
  for(const d of [.2,.67,1.5]){
    const h=heliumCandidate(d),l=makeLattice(2,d);
    assert.deepEqual(h.wedges.map(w=>w.map(i=>h.indices[i])),receipt.tetrahedral_wedges);
    for(let i=0;i<h.indices.length;i++)assert.deepEqual(h.positions[i],l.vertices[l.lookup.get(key(h.indices[i]))].position);
    const latticeEdges=new Set(l.edges.map(([a,b])=>[a,b].sort((x,y)=>x-y).join(',')));
    const edgeKey=([a,b])=>[l.lookup.get(key(h.indices[a])),l.lookup.get(key(h.indices[b]))].sort((x,y)=>x-y).join(',');
    assert.equal(new Set(h.edges.map(edgeKey)).size,12);
    h.edges.forEach(e=>assert(latticeEdges.has(edgeKey(e))));assert(!latticeEdges.has(edgeKey(h.axis)));
  }
});
