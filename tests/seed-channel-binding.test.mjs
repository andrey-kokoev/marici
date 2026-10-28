import test from 'node:test';
import assert from 'node:assert/strict';
import {loadSeed,seedChannelStudy,forward,reversePath,endpoints,reducePath,comparePaths} from '../research/realization-tower/seed-channel-binding.mjs';
test('actual source yields four endpoint indices but not four outgoing primitive ports',async()=>{
 const s=await seedChannelStudy();assert.deepEqual(s.seed.vertices,['A','B','C','D']);assert.equal(s.seed.rows.length,6);
 assert.deepEqual(Object.values(s.rawSourceFibres).map(f=>f.length),[2,2,1,1]);
 assert.deepEqual(Object.values(s.rawTargetFibres).map(f=>f.length),[2,2,1,1]);
 assert.deepEqual(Object.values(s.directChannels).map(f=>f.length),[0,1,0,1]);
 assert(Object.values(s.endpointFamilies).every(f=>f.length>0));
 assert.deepEqual(s.endpointUniqueness,{seed:true,pathTable:false});
 assert(s.endpointFamilies.B.some(p=>p.word.map(e=>e.label).join(',')==='AB'));
 assert(s.endpointFamilies.B.some(p=>p.word.map(e=>e.label).join(',')==='AD,DB'));
 for(const paths of Object.values(s.endpointFamilies))for(const p of paths)assert.deepEqual(endpoints(s.seed,p.from,p.word),{from:p.from,to:p.to});
});
test('formal reversal retains occurrence labels and is not the independent BA edge',async()=>{
 const seed=await loadSeed(),ab=[forward('AB')],ba=[forward('BA')];
 assert.deepEqual(reversePath(reversePath(ab)),ab);assert.deepEqual(endpoints(seed,'B',reversePath(ab)),endpoints(seed,'B',ba));
 assert.notDeepEqual(reversePath(ab),ba);assert.deepEqual(reducePath([...ab,...reversePath(ab)]),[]);
 assert.equal(reducePath([...ab,...ba]).length,2);assert.throws(()=>endpoints(seed,'A',ba));
});
test('parallel-route comparison constructs a retained defect, not a fabricated face equality',async()=>{
 const s=await seedChannelStudy(),c=s.comparison;
 assert.equal(c.reducedLoop.length,3);assert.deepEqual(endpoints(s.seed,'A',c.loop),{from:'A',to:'A'});
 const swapped=comparePaths(s.seed,'A',c.right,c.left);assert.deepEqual(swapped.loop,reversePath(c.loop));
 assert.deepEqual(reducePath([...c.loop,...swapped.loop]),[]);
 assert.throws(()=>comparePaths(s.seed,'A',[forward('AB')],[forward('AD')]));
 assert.equal(s.probeResults.direct,1);assert.equal(s.probeResults.via,0);assert.equal(s.probeResults.loopDefect,1);
 assert.equal(s.probeResults.correctedVia,1);assert(!s.disposition.correctionIsNativeFiller);
 assert.notEqual(s.probeResults.primitiveBA,s.probeResults.formalInverseAB);
 assert.deepEqual(s.assignmentCounts,{all:64,forwardEquation:32,triangleEquation:32,both:16});
});
