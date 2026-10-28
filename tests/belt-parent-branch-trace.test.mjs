import test from 'node:test';import assert from 'node:assert/strict';
import {traceBeltParentBranches} from '../research/realization-tower/belt-parent-branch-trace.mjs';
import {buildFoldedFibration} from '../research/realization-tower/fibration-folded-process.mjs';
const audit=traceBeltParentBranches(),model=buildFoldedFibration(),owners=new Map(model.occurrences.map(o=>[o.id,o]));
const key=f=>f.map(p=>p.map(x=>x.toFixed(7)).join(',')).sort().join('|');
test('the candidate four roots are witnessed by actual parent faces, not inferred from four-star geometry',()=>{
 for(const p of audit.parents){assert.equal(p.firstMediator.length,1);assert.deepEqual(p.candidateRoots.map(r=>r.sourceParticleRole),['electron','proton','proton','proton']);assert.equal(p.candidateRoots.length,4);
  for(const a of p.earlyWitnesses)for(const w of a.witnesses)for(const id of [a.body,w.parent])assert.ok(owners.get(id).faces.some(f=>key(f)===key(w.face)));
  const merge=p.earlyWitnesses.filter(a=>a.round===3);assert.equal(merge.length,3);for(const a of merge){assert.equal(a.roots.length,2);assert.ok(a.roots.includes(0));}
 }
 assert.deepEqual(audit.parents[0].candidateRoots.map(r=>r.sourceGeometry),audit.parents[1].candidateRoots.map(r=>r.sourceGeometry));
});
test('root ancestry overlaps at every exposed seam face and cannot define a four-way partition',()=>{
 for(const p of audit.parents){assert.equal(p.boundary.length,49);assert.equal(p.disjointBoundaryPartition,false);assert.deepEqual(p.rootMultiplicityHistogram,{'2':6,'3':27,'4':16});assert.deepEqual(p.candidateRoots.map(r=>r.reachableSeamFaces),[49,36,36,36]);for(const b of p.boundary){assert.ok(b.rootIndices.includes(0));assert.ok(b.rootIndices.length>=2);}}
 assert.equal(audit.attachment,null);
});
test('all 49 existing seam crossings have a witnessed reverse traversal',()=>{
 assert.equal(audit.crossings.outward.length,49);assert.equal(audit.crossings.return.length,49);
 for(const edge of audit.crossings.outward){assert.equal(owners.get(edge.from).copy,'clone');assert.equal(owners.get(edge.to).copy,'original');const back=audit.crossings.return.find(e=>e.seamPair===edge.seamPair);assert.equal(back.from,edge.to);assert.equal(back.to,edge.from);assert.equal(key(back.face),key(edge.face));}
});
