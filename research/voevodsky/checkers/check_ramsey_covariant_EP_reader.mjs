// Positive challenge on the exact geometry used by the failed U(2) adapter.
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {packetSnapshot} from '../ramsey-native-word-trace.mjs';
const sha=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
const input='research/voevodsky/results/ramsey-EP-reader-obstruction-input-v1.json',prior=JSON.parse(readFileSync(input));
for(const [p,h] of Object.entries(prior.source_sha256))assert.equal(sha(p),h,p);
const compose=(a,b)=>a.map(i=>b[i]),T=[3,4,1,2,0],PP=prior.positivePReader,PE=prior.negativeEReader;
assert.deepEqual(compose(PP,T),compose(T,PE));
const r=new GenerativeAssemblyRules(),cell=r.charts[r.packets[r.root].chart].cell;
let validated=0;const rows=[];
function step(p,kind){const op=r.outgoing(p).map(i=>r.operations[i]).find(o=>o.kind===kind);assert(op&&r.validateTransfer(op));validated++;return op;}
for(const old of prior.rows){
 const ps=r.completeP(cell,old.sourceP.chart.aliases),pt=r.completeP(cell,old.finalViaP.chart.aliases);
 assert.deepEqual(r.charts[ps].aliases,old.sourceP.chart.aliases);assert.deepEqual(r.charts[pt].aliases,old.finalViaP.chart.aliases);
 const p0=r.packet(ps,2,T),pn0=step(p0,'PN'),back=step(pn0.target,'inverse-PN');assert.equal(back.target,p0);
 const reader=step(back.target,'reader-phase-advance'),p1=reader.target;
 const other=r.packet(pt,3,compose(T,PE));assert.equal(other,p1);
 const pn1=step(p1,'PN'),pnOther=step(other,'PN');assert.equal(pn1.target,pnOther.target);
 assert.deepEqual(r.packets[p1].permutation,compose(PP,T));
 assert.deepEqual(r.packets[pn1.target].permutation,compose(pn1.permutation,compose(T,PE)));
 assert.deepEqual(pn1.face,old.readerPrefixedPN.face);
 assert.deepEqual(phaseFrame(r.charts[pt],3).window[0],old.conflictingSameOccurrence);
 for(const [chart,origin,ef] of [[ps,2,old.dualReader.sourceFrame],[pt,3,old.dualReader.targetFrame]]){
  const p=phaseFrame(r.charts[chart],origin);
  assert.deepEqual(p.window[0],ef.window[2]);assert.deepEqual(p.window[1],ef.context);
 }
 rows.push({marking:old.marking,dualReader:old.dualReader,
   packets:{P0:packetSnapshot(r,p0),N0:packetSnapshot(r,pn0.target),P1:packetSnapshot(r,p1),N1:packetSnapshot(r,pn1.target)},
   operations:{PN0:pn0,inversePN0:back,PReader:reader,PN1:pn1},
   sameFinalPPacket:true,sameFinalPNPacket:true,allFiveCoefficientMapsAgree:true,
   retainedFinalOccurrence:old.conflictingSameOccurrence});
}
assert.equal(rows.length,24);
const files=[input,'research/voevodsky/checkers/check_ramsey_covariant_EP_reader.mjs','research/nima/generative-phase-assembly.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs','research/voevodsky/ramsey-native-word-trace.mjs'];
const result={status:'passed',node:'face-chart-transition-descent',adapter:T,PReader:PP,negativeEReader:PE,
 rows,validatedTransfers:validated,scope:'reader square plus direct and reader-prefixed PN ports, under the retained negative-direction comparison policy; no forward E operation installed',
 source_sha256:Object.fromEntries([...new Set([...files,...Object.keys(prior.source_sha256)])].map(p=>[p,sha(p)]))};
writeFileSync('research/voevodsky/results/ramsey-covariant-EP-reader-input-v1.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:'passed',markings:24,validatedTransfers:validated,allFiveSlotsAgree:true,sameFullPNPackets:true}));
