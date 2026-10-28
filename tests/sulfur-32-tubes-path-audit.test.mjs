import test from 'node:test';
import assert from 'node:assert/strict';
import {auditSulfur32TubesPaths,segmentHitsWall} from '../research/realization-tower/sulfur-32-tubes-path-audit.mjs';
import {sulfur32Process} from '../research/realization-tower/sulfur-32-process.mjs';
import {removeSulfurTubesTips} from '../research/realization-tower/sulfur-32-tubes-view.mjs';
for(const step of [0,1])test(`actual Tubes walls allow four endpoint connections for each opposite pair, stage ${step}`,()=>{
 const a=auditSulfur32TubesPaths(step);
 assert.equal(a.ports.length,12);assert.deepEqual(a.innerDividerAreas,[0,0,0,0,0,0]);
 assert(a.allPortCentrePathsClear);
 assert.deepEqual(a.oppositePairs.map(p=>p.clearEndpointConnections),[4,4,4]);
 assert(a.oppositePairs.every(p=>p.entryOpenings===2&&p.exitOpenings===2));
});
test('segment checker detects real transverse and coplanar wall contact',()=>{
 const pair=removeSulfurTubesTips(sulfur32Process(7,0)).tubesCutPrisms[0],wall=pair.uncutWalls[0];
 const mid=wall[0].map((_,i)=>wall.reduce((s,v)=>s+v[i]/4,0));
 // Coplanar segment across the wall, and a crossing along an independent edge direction.
 assert(segmentHitsWall(wall[0],wall[2],wall));
 const other=pair.rectangle.find(p=>!wall.some(v=>String(v)===String(p))),edge=other.map((x,i)=>x-wall[0][i]);
 assert(segmentHitsWall(mid.map((x,i)=>x-edge[i]),mid.map((x,i)=>x+edge[i]),wall));
 const offset=pair.inward.map(x=>10*x);
 assert(!segmentHitsWall(wall[0].map((x,i)=>x+offset[i]),wall[2].map((x,i)=>x+offset[i]),wall));
});
