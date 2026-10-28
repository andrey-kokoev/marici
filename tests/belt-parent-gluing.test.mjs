import test from 'node:test';import assert from 'node:assert/strict';
import {auditBeltParentGluing} from '../research/realization-tower/belt-parent-gluing-audit.mjs';
test('intact N-facing parents have no correctly oriented boundary faces for the axial patches',()=>{
 const a=auditBeltParentGluing();assert.equal(a.status,'blocked-intact-N-axis-face-gluing');
 for(const p of a.parents){assert.equal(p.boundaryFaces,196);assert.deepEqual(p.normalClasses,[-1,.333333333]);assert.equal(p.facingParallelFaces,0);assert.equal(p.oppositeFacingParallelFaces,49);assert.equal(p.capAlternative.applied,false);assert.equal(p.capAlternative.cells.filter(c=>c.kind==='tetrahedron').length,4);assert.equal(p.capAlternative.cells.filter(c=>c.kind==='octahedron').length,1);assert.equal(p.capAlternative.exposedFaces.length,4);}
});
