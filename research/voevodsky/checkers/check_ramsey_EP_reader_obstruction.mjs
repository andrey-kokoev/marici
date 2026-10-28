// Falsification target: naturality of the moving U(2) E/P adapter on the
// actual P reader-prefixed PN port and the proved whole-reference dual reader.
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {phaseFrame,phaseAdvancePermutations} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
import {packetSnapshot} from '../ramsey-native-word-trace.mjs';
const sha=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
const input='research/voevodsky/results/ramsey-moving-EP-preparation-v1.json',prior=JSON.parse(readFileSync(input));
for(const [p,h] of Object.entries(prior.source_sha256))assert.equal(sha(p),h,p);
const compose=(a,b)=>a.map(i=>b[i]),Q=[4,3,2,1,0],PP=[...phaseAdvancePermutations.proton];
const inverse=p=>p.map((_,i)=>p.indexOf(i)),PE=compose(compose(Q,inverse(PP)),Q);
assert.deepEqual(PP,[2,3,0,1,4]);assert.deepEqual(PE,[0,3,4,1,2]);
const T=[3,4,2,0,1],viaP=compose(PP,T),viaE=compose(T,PE);
assert.equal(viaP[0],2);assert.equal(viaE[0],1);
// Countercontrol: the earlier body-carrying convention IS reader-natural,
// but was already found to change the named native coefficient projectors.
const candidateAudit=prior.retainedPairPermutationCandidates.map(c=>({...c,
 readerNatural:JSON.stringify(compose(PP,c.coefficientOrder))===JSON.stringify(compose(c.coefficientOrder,PE))}));
assert(!candidateAudit.some(c=>c.allPass&&c.readerNatural));
assert.deepEqual(candidateAudit.filter(c=>c.readerNatural).map(c=>c.coefficientOrder),[[3,4,1,2,0]]);
const permutations=a=>a.length?a.flatMap((v,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[v,...p])):[[]];
const r=new GenerativeAssemblyRules(),cell=r.charts[r.packets[r.root].chart].cell,vertices=r.geometry.cells[cell].vertices;
const names=['C0','M0','C1','M1'],six=['C0','M0','C1','M1','C2','M2'];
const J={C0:'M2',M0:'C2',C1:'M1',M1:'C1',C2:'M0',M2:'C0'};
const rows=[];let validated=0;
function step(packet,kind){const op=r.outgoing(packet).map(i=>r.operations[i]).find(o=>o.kind===kind);assert(op&&r.validateTransfer(op));validated++;return op;}
function fullE(packet){return r.charts[r.packets[step(step(packet,'PN').target,'NE').target].chart];}
function dualAliases(chart){return Object.fromEntries(six.map(n=>[n,chart.aliases[J[n]]]));}
function reread(e){return r.completeP(cell,{C0:e.C2,M0:e.M2,C1:e.C1,M1:e.M1});}
for(const marking of permutations([0,1,2,3])){
 const original=r.completeP(cell,Object.fromEntries(names.map((n,i)=>[n,vertices[marking[i]]])));
 const before=r.packet(original,0,[0,1,2,3,4]),oldReader=step(before,'reader-phase-advance'),after=oldReader.target;
 assert.equal(r.packets[after].origin,1);assert.deepEqual(oldReader.permutation,PP);
 const beforeFull=fullE(before),afterFull=fullE(after);
 // K=3 reverses the original r=0->1 edge into dual r=0->1,
 // with old 'after' as the dual source. No forward E operation is invented.
 const es=dualAliases(afterFull),et=dualAliases(beforeFull);
 const esChart=r.chart(cell,'electron',es),etChart=r.chart(cell,'electron',et);
 const ef0=phaseFrame(r.charts[esChart],0),ef1=phaseFrame(r.charts[etChart],1);
 assert.equal(auditPhaseFrame(ef0).status,'native-template-compatible');assert.equal(auditPhaseFrame(ef1).status,'native-template-compatible');
 assert.deepEqual(ef0.window[2],ef1.window[1]);assert.deepEqual(ef0.context,ef1.window[0]);
 const ps=reread(es),pt=reread(et);assert.notEqual(ps,null);assert.notEqual(pt,null);
 const start=r.packet(ps,2,T),pReader=step(start,'reader-phase-advance'),end=pReader.target;
 assert.equal(r.packets[end].origin,3);assert.equal(r.packets[end].chart,pt);
 assert.deepEqual(r.packets[end].permutation,viaP);
 const expectedEnd=r.packet(pt,3,viaE);
 const pf0=phaseFrame(r.charts[ps],2),pf1=phaseFrame(r.charts[pt],3);
 // Both proposed routes concern literally the SAME final retained occurrence.
 assert.deepEqual(pf1.window[0],pf0.window[2]);assert.deepEqual(pf1.window[0],ef1.window[2]);
 const pnA=step(end,'PN'),pnB=step(expectedEnd,'PN');
 assert.deepEqual(pnA.face,pnB.face);assert.deepEqual(pnA.permutation,pnB.permutation);
 const outA=r.packets[pnA.target],outB=r.packets[pnB.target];assert.equal(outA.chart,outB.chart);assert.equal(outA.origin,outB.origin);
 assert.equal(outA.permutation[3],2);assert.equal(outB.permutation[3],1);
 // Choose source dual E coefficient e1. No context U can affect the
 // first target row of either route (it reads x2 versus x1).
 const unit=[0,1,0,0,0];assert.equal(unit[r.packets[end].permutation[0]],0);assert.equal(unit[viaE[0]],1);
 rows.push({marking,oldReader,dualReader:{reflectionCenter:3,sourceFrame:ef0,targetFrame:ef1,permutation:PE,policy:'whole-reference reverse of the actual P reader; not an emitted forward E edge'},
   sourceP:packetSnapshot(r,start),nativePReader:pReader,finalViaP:packetSnapshot(r,end),finalViaE:packetSnapshot(r,expectedEnd),
   conflictingSameOccurrence:pf1.window[0],sourceUnitCoefficient:1,viaPValue:0,viaEValue:1,
   readerPrefixedPN:{face:pnA.face,operation:pnA,otherOperation:pnB,viaPPermutation:outA.permutation,viaEPermutation:outB.permutation,
     differingActiveNeutronSlot:3,viaPValue:0,viaEValue:1}});
}
assert.equal(rows.length,24);
const files=[input,'research/voevodsky/checkers/check_ramsey_EP_reader_obstruction.mjs',
 'research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs','research/voevodsky/ramsey-native-word-trace.mjs'];
const result={status:'passed',scientificResult:'claimed_U2_adapter_extension_fails_reader_naturality',
 node:'face-chart-transition-descent',coefficientConvention:'output[i]=input[permutation[i]]',
 positivePReader:PP,negativeEReader:PE,referenceAdapter:T,viaP,viaE,candidateAudit,rows,validatedTransfers:validated,
 universalObstruction:'For any source U and target V, row0(P_P T_U)=e2^t but row0(T_V P_E)=e1^t. Even an arbitrary target adapter retaining C2 has the latter row.',
 scope:'Refutes extension of the specified locally L/G/N-compatible moving U(2) family with the unchanged reader laws and exact retained-value interpretation. Does not refute the structural four-facet construction or all other semantic comparisons.',
 source_sha256:Object.fromEntries([...new Set([...files,...Object.keys(prior.source_sha256)])].map(p=>[p,sha(p)]))};
writeFileSync('research/voevodsky/results/ramsey-EP-reader-obstruction-input-v1.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:'passed',markings:24,validatedTransfers:validated,viaP,viaE,
 sameFinalOccurrenceValues:[0,1],alsoVisibleInNativePNWindow:true}));
