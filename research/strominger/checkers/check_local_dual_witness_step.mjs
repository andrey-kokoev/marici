import assert from 'node:assert/strict';
import {generateInterfaceWitnesses} from '../../realization-tower/interface-witness-generation.mjs';
import {centerInterfaceProcess} from '../../realization-tower/center-interface-process.mjs';
const p=centerInterfaceProcess(7,2);
const input=p.retainedBodies.map(b=>({id:b.id,role:b.role,vertices:b.components[0]}));
const result=generateInterfaceWitnesses(input);
assert.equal(result.dualEdges.length,4);
assert.ok(result.witnesses.every(w=>w.cells.length===2&&w.parents.includes('central-P')));
assert.deepEqual(result.source.map(t=>t.role),['proton','proton','electron','neutron','neutron']);
assert.deepEqual(result.sourceVolumes,result.refinedVolumes);
const before=structuredClone(input);generateInterfaceWitnesses(input);assert.deepEqual(input,before);
const reversed=generateInterfaceWitnesses(input.toReversed().map(t=>({...t,vertices:t.vertices.toReversed()})));
assert.deepEqual(result.counts,reversed.counts);
assert.deepEqual(result.refinedCells.map(c=>c.id).sort(),reversed.refinedCells.map(c=>c.id).sort());
for(const block of result.dualBlocks)for(const flag of block.maximalFlags){
 assert.equal(flag[0],block.primalFace);
 assert.equal(flag.length,block.dimension+1);
}
assert.equal(result.counts.before.reduce((s,n,i)=>s+(i%2?-n:n),0),1);
assert.equal(result.counts.after.reduce((s,n,i)=>s+(i%2?-n:n),0),1);
assert.throws(()=>generateInterfaceWitnesses([...input,input[0]]));
console.log(JSON.stringify({checksPassed:true,...result},null,2));
