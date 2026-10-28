import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {createRetainedContextMachine} from '../retained-context-spinor-packet.mjs';
const permutations=xs=>xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const cycles=p=>{const seen=new Set(),out=[];for(let i=0;i<p.length;i++)if(!seen.has(i)){const c=[];let j=i;while(!seen.has(j)){seen.add(j);c.push(j);j=p[j];}out.push(c);}return out;};
const words=[['reader-phase-advance','reader-phase-advance','reader-phase-advance'],['PN','reader-phase-advance','inverse-PN','reader-phase-advance','PN','reader-phase-advance','inverse-PN']];
const machine=createRetainedContextMachine([[1,0],[2,0],[3,0],[4,0],[5,0]]);
const packets=words.map(word=>word.reduce((p,kind)=>{const choices=machine.choices(p).filter(o=>o.kind===kind);assert.equal(choices.length,1);return machine.step(p,choices[0]);},machine.initial()));
const endpoint=p=>{const {permutation,...rest}=p.native;return rest;};assert.deepEqual(endpoint(packets[0]),endpoint(packets[1]));
const [a,b]=packets.map(p=>p.native.permutation),inverseA=a.map((_,i)=>a.indexOf(i)),H=b.map(i=>inverseA[i]);assert.equal(cycles(H).length,1);
// HE=ES, E a complex 5-by-4 matrix. Every equation is equality of two
// entries: E[H[i],j]=E[i,S[j]]. Union-find solves these EXACTLY, without
// floating ranks or a chosen encoding. Each component is one free complex value.
const rivals=permutations([0,1,2,3]).map(S=>{
 const parent=Array.from({length:20},(_,i)=>i),root=i=>{while(parent[i]!==i)i=parent[i];return i;},join=(i,j)=>{parent[root(i)]=root(j);};
 for(let i=0;i<5;i++)for(let j=0;j<4;j++)join(4*H[i]+j,4*i+S[j]);
 for(let i=1;i<5;i++)for(let j=0;j<4;j++)assert.equal(root(4*i+j),root(j));
 return {permutation:S,freeComplexParameters:new Set(parent.map((_,i)=>root(i))).size,allRowsEqual:true,maximumEncodingRank:1};
});
// Counter-control: the invariant zero-sum four-plane DOES exist. Its induced
// order-five action mixes amplitudes, rather than permuting four records.
const embedding=Array.from({length:5},(_,i)=>Array.from({length:4},(_,j)=>i===4?-1:Number(i===j)));
const multiply=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,x,k)=>s+x*B[k][j],0)));
const induced=H.slice(0,4).map(i=>embedding[i]),left=H.map(i=>embedding[i]);assert.deepEqual(left,multiply(embedding,induced));
let power=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>Number(i===j)));const I=structuredClone(power);
for(let i=1;i<=5;i++){power=multiply(power,induced);if(i<5)assert.notDeepEqual(power,I);}assert.deepEqual(power,I);
assert(induced.some(row=>row.some(x=>x===-1)));
// A history-dependent embedding can absorb every coefficient permutation.
// This is why the unrestricted existential statement is NOT falsified here.
const E0=[...I,[0,0,0,0]],dependent=packets.map(p=>p.native.permutation.map(i=>E0[i]));
assert.deepEqual(H.map(i=>dependent[0][i]),dependent[1]);
const paths=['research/strominger/checkers/falsify_fixed_signed_pair_codec.mjs','research/strominger/fixed-signed-pair-codec-falsification-v1.md','research/strominger/retained-context-spinor-packet.mjs','research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs','research/strominger/sulfur-32-reversible-channel-specification.md'];
const evidence=[];for(const path of paths)evidence.push({path,sha256:createHash('sha256').update(await fs.readFile(path)).digest('hex')});
const report={schema:'fixed-signed-pair-codec.falsification.v1',constructionAdmitted:false,
 verdict:'fixed endpoint-local complex-linear four-record relabelling codec falsified',
 broadExistentialConjectureFalsified:false,
 testedAssumptions:['four independent complex record values','source operations only permute those four records','one injective complex-linear encoding per geometric endpoint, independent of path/history','both freshly replayed native paths are in scope'],
 paths:packets.map((p,i)=>({word:words[i],native:p.native,history:p.history,historyCommitment:p.historyCommitment})),relativePermutation:H,relativeOrder:5,
 exactIntertwinerSolutions:rivals,maximumEncodingRank:1,requiredEncodingRank:4,
 controls:{zeroSumEncoding:embedding,inducedOrderFiveMatrix:induced,historyDependentEndpointEncodings:dependent},
 limits:['actual wire contents were not specified as four independent complex scalars','history/assembly-dependent encodings are allowed by the broader conjecture and evade this counterexample','the two paths share a geometric endpoint, not a proved identical whole-assembly state','no claim that these older-grammar paths have both been admitted in the intended five-side global realization','a dimension count alone does not reject invariant four-dimensional admissible state spaces'],evidence};
if(process.argv.includes('--record')){const dir='research/strominger/results/fixed-signed-pair-codec-falsification-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(`${dir}/verification.json`,JSON.stringify(report,null,2)+'\n');}
console.log(JSON.stringify({verdict:report.verdict,broadExistentialConjectureFalsified:false,relativePermutation:H,relativeOrder:5,fourRecordPermutationsExhausted:rivals.length,maximumEncodingRank:1,requiredEncodingRank:4,zeroSumAndHistoryDependentControlsPassed:true},null,2));
