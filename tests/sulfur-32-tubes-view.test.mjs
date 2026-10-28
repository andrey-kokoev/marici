import test from 'node:test';
import assert from 'node:assert/strict';
import {sulfur32Process} from '../research/realization-tower/sulfur-32-process.mjs';
import {singleOctahedralEnvelope} from '../research/realization-tower/single-octahedral-process.mjs';
import {removeSulfurTubesTips} from '../research/realization-tower/sulfur-32-tubes-view.mjs';
import {junctionOverlapVolumes,junctionPlaneDistance,polygonArea,subtractTubesJunction} from '../research/realization-tower/sulfur-32-junction-cut.mjs';
for(const step of [0,1])test(`Tubes removes exactly six N tip cells without modifying Geometry, stage ${step}`,()=>{
 const source=sulfur32Process(7,step),before=JSON.stringify(source),view=removeSulfurTubesTips(source),tips=new Set(singleOctahedralEnvelope(1).map(p=>p.join(',')));
 assert.equal(view.retainedBodies.length,13);assert.equal(view.retainedBodies.filter(c=>c.role==='neutron').length,13);
 assert.equal(view.retainedBodies.filter(c=>c.role==='proton').length,0);assert.equal(view.retainedBodies.filter(c=>c.role==='electron').length,0);
 assert.equal(view.tubesViewAudit.removedPECells.length,32);
 const removedPE=new Set(view.tubesViewAudit.removedPECells);
 assert(view.presentationLabels.every(l=>!removedPE.has(l.cell)));
 assert(view.nativeWiringGraph.nodes.every(n=>!removedPE.has(n.id)));
 assert(view.nativeWiringGraph.links.every(l=>!removedPE.has(l.from)&&!removedPE.has(l.to)));
 assert(view.retainedBodies.every(c=>c.vertices.every(v=>!tips.has(v.join(',')))));
 const removed=new Set(view.tubesViewAudit.removedTipCells);assert.equal(removed.size,6);
 assert(view.presentationLabels.every(l=>!removed.has(l.cell)&&!tips.has(l.point.join(','))));
 assert(view.nativeWiringGraph.links.every(l=>!removed.has(l.from)&&!removed.has(l.to)));
 assert.equal(view.tubesCutPrisms.length,12);
 const faceKey=w=>w.map(v=>v.join(',')).sort().join('|');
 for(const pair of view.tubesCutPrisms){
  assert.equal(pair.color,0xffffff);assert.equal(pair.rectangle.length,4);
  assert.equal(pair.prisms.length,2);assert.equal(pair.uncutWalls.length,5);
  const origin=pair.rectangle[0].map((_,i)=>pair.rectangle.reduce((s,p)=>s+p[i]/4,0));
  const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),depth2=dot(pair.inward,pair.inward);
  const layers=source.retainedBodies.flatMap(c=>c.vertices.map(v=>dot(v.map((x,i)=>x-origin[i]),pair.inward)/depth2)).filter(x=>x>1e-9);
  assert.equal(Math.min(...layers),1);
  for(const prism of pair.prisms){
   assert.equal(prism.front.length,3);assert(prism.front.every(p=>pair.rectangle.includes(p)));
   assert.deepEqual(prism.back,prism.front.map(p=>p.map((x,i)=>x+pair.inward[i])));
   assert.equal(prism.walls.length,3);assert(prism.walls.every(w=>w.length===4));
   assert(prism.walls.every(w=>!w.every(v=>prism.front.includes(v))&&!w.every(v=>prism.back.includes(v))));
  }
  const shared=pair.prisms[0].walls.filter(w=>pair.prisms[1].walls.some(other=>faceKey(w)===faceKey(other)));
  assert.equal(shared.length,1);
  const width2=w=>w[0].reduce((s,x,i)=>s+(x-w[1][i])**2,0);
  assert.equal(width2(shared[0]),Math.max(...pair.prisms[0].walls.map(width2)));
 }
 const ordered=view.tubesCutPrisms.filter(p=>p.layer===0).toSorted((a,b)=>a.tipIndex-b.tipIndex);
 assert.deepEqual(ordered.map(p=>p.alternate),[false,true,false,true,false,true]);
 for(const pair of ordered){
  const divider=pair.prisms[0].front.filter(p=>pair.prisms[1].front.includes(p));
  assert.equal(divider.length,2);
  assert.equal(divider.includes(pair.rectangle[0]),!pair.alternate);
 }
 for(const outer of ordered){
  const inner=view.tubesCutPrisms.find(p=>p.tipIndex===outer.tipIndex&&p.layer===1);
  assert(inner);assert.equal(inner.alternate,!outer.alternate);
  assert.deepEqual(inner.rectangle,outer.rectangle.map(p=>p.map((x,i)=>x+outer.inward[i])));
  const backVertices=new Set(outer.prisms.flatMap(p=>p.back.map(v=>v.join(','))));
  assert.deepEqual(new Set(inner.rectangle.map(v=>v.join(','))),backVertices);
  const oldDivider=outer.prisms[0].back.filter(p=>outer.prisms[1].back.some(q=>q.join(',')===p.join(','))).map(v=>v.join(','));
  const newDivider=inner.prisms[0].front.filter(p=>inner.prisms[1].front.includes(p)).map(v=>v.join(','));
  assert(newDivider.every(v=>!oldDivider.includes(v)));
 }
 assert.equal(view.tubesViewAudit.prisms,24);
 assert.equal(view.tubesViewAudit.depthLayers,2);
 assert.equal(view.tubesViewAudit.endCaps,0);
 assert.equal(view.tubesViewAudit.junctionCut,'pairwise-and-triple-overlaps');
 const walls=view.tubesCutPrisms.flatMap(p=>p.walls).concat(view.retainedBodies.flatMap(c=>c.faces));
 for(const wall of walls){
  assert(polygonArea(wall)>1e-9);
  // Every surviving patch lies outside at least one cutter half-space.
  for(const planes of junctionOverlapVolumes)assert(planes.some(plane=>wall.every(p=>junctionPlaneDistance(p,plane)>=-1e-9)&&wall.some(p=>junctionPlaneDistance(p,plane)>1e-9)));
  assert(Math.abs(subtractTubesJunction(wall).reduce((s,p)=>s+polygonArea(p),0)-polygonArea(wall))<1e-8);
 }
 for(const pair of view.tubesCutPrisms){
  const oldArea=pair.uncutWalls.reduce((s,p)=>s+polygonArea(p),0),newArea=pair.walls.reduce((s,p)=>s+polygonArea(p),0);
  if(pair.layer===0)assert(Math.abs(oldArea-newArea)<1e-8);
  else {
   // Only the four exterior triangular patches survive. The entire inner
   // divider and all walls blocking two-way overlaps must be gone.
   assert(Math.abs(newArea-Math.SQRT2)<1e-8);
   assert(newArea<oldArea);
  }
 }
 assert.equal(JSON.stringify(source),before);assert.equal(source.retainedBodies.length,51);
 assert.equal(source.tubesCutPrisms,undefined);
});
