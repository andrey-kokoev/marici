import assert from 'node:assert/strict';
import {makeAtom,atomDefinitions} from '../demos/particle-overlap-tetrahedron/atom-model.mjs';
import {lattice,cellNeighbors,layerReferenceCellId} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
for(const kind of Object.keys(atomDefinitions)){
 const atom=makeAtom(kind),definition=atomDefinitions[kind];
 for(const species of ['proton','neutron','electron'])assert.equal(atom.bodies.filter(b=>b.species===species).length,definition[species]);
 assert.equal(atom.counts.proton,atom.counts.electron);
 assert.equal(new Set(atom.bodies.map(b=>b.cellId)).size,atom.bodies.length);
 assert.equal(atom.nucleus[0],layerReferenceCellId);
 for(let i=1;i<atom.nucleus.length;i++)assert.ok(atom.nucleus.slice(0,i).some(n=>cellNeighbors(n).includes(atom.nucleus[i])));
 for(const e of atom.electrons){
  assert.ok(!atom.nucleus.includes(e));assert.equal(lattice.cells[e].length,4);
  assert.ok(atom.nucleus.some(n=>cellNeighbors(n).includes(e)));
  const attachment=atom.electronAttachments.find(a=>a.cellId===e);
  assert.ok(atom.nucleus.includes(attachment.nuclearCellId));assert.equal(attachment.faceNodeIds.length,3);
  assert.deepEqual(attachment.faceNodeIds,lattice.cells[e].filter(id=>lattice.cells[attachment.nuclearCellId].includes(id)));
 }
 for(const body of atom.bodies){assert.deepEqual(body.nodeIds,lattice.cells[body.cellId]);body.names.forEach((name,i)=>{
  assert.equal(atom.points[name],lattice.nodes[body.nodeIds[i]].point);
  assert.equal(atom.coordinates[name],lattice.nodes[body.nodeIds[i]].coordinate);
 });}
 assert.deepEqual(makeAtom(kind),atom);
}
assert.throws(()=>makeAtom('unknown'));assert.throws(()=>makeAtom('hydrogen',-1));
console.log('PASS neutral H-1 / H-2 / He-4 occupancies, connected nuclei, distinct lattice cells and tetrahedral electrons sharing nuclear faces');
