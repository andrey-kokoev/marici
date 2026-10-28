import test from 'node:test';import assert from 'node:assert/strict';
import {buildPESymmetricSector} from '../research/strominger/pe-symmetric-sector.mjs';
import {nativeEmptyRegions} from '../research/strominger/native-empty-regions.mjs';
test('native N voids are not joined by their edge-only contacts',()=>{
 const a=nativeEmptyRegions(buildPESymmetricSector(3));assert.equal(a.emptyCells,231);assert.equal(a.regionsWithinCarrier,231);assert.equal(a.enclosedRegions,85);assert.equal(a.surfaceOpeningRegions,146);assert.equal(a.sharedEmptyFaces,0);assert.equal(a.edgeTouchComponents,1);assert.equal(a.vertexTouchComponents,1);assert.equal(a.regionsIncludingExterior,86);assert.equal(new Set(a.regions.flatMap(r=>r.cellIds)).size,231);
});
test('positive-area passages really merge volumes when the occupied separators are removed',()=>{
 const s=buildPESymmetricSector(1),a=nativeEmptyRegions({...s,cells:s.cells.map(c=>({...c,role:'neutron'}))});assert.equal(a.emptyCells,51);assert.ok(a.sharedEmptyFaces>0);assert.equal(a.regionsWithinCarrier,1);assert.equal(a.enclosedRegions,0);assert.equal(a.surfaceOpeningRegions,1);
});
