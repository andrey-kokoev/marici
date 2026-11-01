import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildCellulationStep,terminalLatticeFrame} from '../research/realization-tower/cellulation-steps.mjs';
const near=(a,b)=>a.forEach((x,i)=>assert(Math.abs(x-b[i])<1e-12));
test('all later construction follows the shortened red chain instead of the old absolute origin',()=>{
 for(const size of [.5,1,2]){
  const models=new Map(Array.from({length:9},(_,i)=>[10+i,buildCellulationStep(10+i,size)])),get=s=>models.get(s);
  const red=get(10),terminal=red.extensions.at(-1).cycle.first.at(-1);
  assert.equal(red.extensions.length,5);assert.equal(red.cells.filter(c=>c.kind==='tetrahedron').length,8);
  near(get(11).directedArrow.from,terminal.witness.turnMarker.point);assert.deepEqual(get(11).directedArrow.fromLattice,[8,1,7]);
  near(get(12).faceClosure.arrow.from,get(11).directedArrow.to);
  near(get(13).directedArrow.from,get(11).directedArrow.to);
  for(const step of [14,15]){near(get(step).triangleClosure.arrows[0].from,get(13).directedArrow.to);near(get(step).triangleClosure.arrows[1].to,get(13).directedArrow.from);}
  near(get(16).sequentialFaces[0].arrow.from,get(12).faceClosure.arrow.to);near(get(16).sequentialFaces[0].arrow.to,get(14).triangleClosure.arrows[0].to);
  near(get(16).sequentialFaces[1].arrow.from,get(15).triangleClosure.arrows[0].to);near(get(16).sequentialFaces[1].arrow.to,get(12).faceClosure.finish.arrow.to);
  near(get(17).solidClosure.arrow.from,get(14).triangleClosure.arrows[0].to);near(get(17).solidClosure.arrow.to,get(15).triangleClosure.arrows[0].to);
  near(get(18).whiteRepeats[0].stages[0].directedArrow.from,get(13).directedArrow.to);
  assert.deepEqual(get(18).whiteRepeats.at(-1).stages[0].directedArrow.toLattice,[8,8,0]);
 }
});
test('the lattice frame reads the actual terminal marker, not a hard-coded coordinate',()=>{
 const m=buildCellulationStep(10),offset=[-1,2,-1],before=terminalLatticeFrame(m)(offset),marker=m.extensions.at(-1).cycle.first.at(-1).witness.turnMarker;
 const shift=[2,-2,0];marker.point=marker.point.map((x,i)=>x+shift[i]/Math.SQRT2);
 assert.deepEqual(terminalLatticeFrame(m)(offset),before.map((x,i)=>x+shift[i]));
});
