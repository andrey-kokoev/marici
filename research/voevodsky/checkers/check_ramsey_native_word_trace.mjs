import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {encodeWord,decodeWord,verifyWord,appendWord,replayTrace,packetSnapshot,canonical,same,NativeTraceResourceError} from '../ramsey-native-word-trace.mjs';
const ROOT=new URL('../../../',import.meta.url),OUT=new URL('../results/',import.meta.url),hash=x=>createHash('sha256').update(x).digest('hex');
const labels=k=>Array.from({length:k},(_,i)=>'symbol-'+i);
function words(k,n){if(n===0)return [[]];return words(k,n-1).flatMap(w=>Array.from({length:k},(_,i)=>[...w,i]));}
function width(k){let d=1;while(2**d<k)d++;return d;}
const I=[0,1,2,3,4],R=[2,3,0,1,4],cases=[];let selectedEvents=0,maxVisitedCells=0;
function positive(k,word){
 const alphabet=labels(k),trace=encodeWord(alphabet,word);
 assert(verifyWord(trace,alphabet,word));
 const ones=word.flatMap(s=>[...s.toString(2).padStart(width(k),'0')]).filter(b=>b==='1').length;
 assert.equal(trace.endpoint.packet.origin,ones);
 assert.deepEqual(trace.endpoint.packet.permutation,ones%2?R:I);
 const cells=new Set([trace.seed.cell.key,...trace.events.flatMap(e=>[e.source.cell.key,e.target.cell.key])]);
 assert(cells.size<=3);maxVisitedCells=Math.max(maxVisitedCells,cells.size);
 selectedEvents+=trace.events.length;cases.push({alphabetSize:k,wordLength:word.length,events:trace.events.length,origin:ones,visitedPrimitiveCells:cells.size});
}
for(const [k,max] of [[1,6],[2,5],[3,3],[4,2]])for(let n=0;n<=max;n++)for(const word of words(k,n))positive(k,word);
positive(5,[0,4,1,3,2]);positive(8,[7,0,4,2,1]);assert.equal(cases.length,133);
const binary=[...words(2,0),...words(2,1),...words(2,2)],alphabet=labels(2);let appendCases=0;
for(const u of binary)for(const v of binary){
 const prefix=encodeWord(alphabet,u),before=structuredClone(prefix),combined=appendWord(prefix,v),direct=encodeWord(alphabet,[...u,...v]);
 assert(same(combined,direct));assert(same(prefix,before));assert(same(combined.events.slice(0,prefix.events.length),prefix.events));
 assert(verifyWord(combined,alphabet,[...u,...v]));appendCases++;
}
assert.equal(appendCases,49);
for(const [a,b,c] of [[[],[0],[1]],[[0],[1],[0,1]],[[1,0],[0,0],[1]]]){
 assert(same(appendWord(appendWord(encodeWord(alphabet,a),b),c),appendWord(encodeWord(alphabet,a),[...b,...c])));
}
const zero=encodeWord(alphabet,[0]),twice=encodeWord(alphabet,[0,0]),left=encodeWord(alphabet,[0,1]),right=encodeWord(alphabet,[1,0]);
assert(same(zero.endpoint,twice.endpoint));assert(same(left.endpoint,right.endpoint));
assert(!same(zero.events,twice.events));assert(!same(left.events,right.events));
const withoutOrdinal=event=>{const result=structuredClone(event);delete result.ordinal;return JSON.stringify(canonical(result));};
assert.deepEqual([...new Set(zero.events.map(withoutOrdinal))].sort(),[...new Set(twice.events.map(withoutOrdinal))].sort());
const reduced=structuredClone(twice),seen=new Set();reduced.events=reduced.events.filter(e=>{const k=withoutOrdinal(e);if(seen.has(k))return false;seen.add(k);return true;}).map((e,i)=>({...e,ordinal:i}));
assert.deepEqual(decodeWord(reduced),[0]);
const {rules,current:root}=replayTrace(zero),beforeCache=JSON.stringify(canonical(rules));let current=root;
for(const kind of ['PN','inverse-PN']){
 const candidates=rules.outgoing(current).map(i=>rules.operations[i]).filter(op=>op.kind===kind);assert.equal(candidates.length,1);
 assert(rules.validateTransfer(candidates[0]));current=candidates[0].target;
}
assert(same(packetSnapshot(rules,current),zero.endpoint));assert.equal(JSON.stringify(canonical(rules)),beforeCache);
const rejected=[];
function reject(name,fn,expected=RangeError){assert.throws(fn,expected);rejected.push(name);}
reject('deduplicated support is a different valid word',()=>verifyWord(reduced,alphabet,[0,0]));
reject('replaced task codebook',()=>verifyWord({...zero,alphabet:['other-0','other-1']},alphabet,[0]));
const one=encodeWord(alphabet,[1]);
function altered(name,trace,edit){const bad=structuredClone(trace);edit(bad);reject(name,()=>decodeWord(bad));}
altered('native source packet changed',zero,t=>t.events[0].source.packet.origin=1);
altered('native target chart reference changed',zero,t=>t.events[0].target.chart.aliases.C2='0,0,0,1');
altered('fifth slot dropped',zero,t=>t.events[0].target.packet.permutation.pop());
altered('native permutation changed',zero,t=>t.events[0].permutation=[4,1,2,0,3]);
altered('phase frames erased',one,t=>t.events[0].phaseFrames=null);
altered('outside reference witness erased',one,t=>delete t.events[0].phaseWitness.referenceContext);
altered('supplied reference law relabeled physical derivation',one,t=>t.events[0].phaseWitness.referenceContext.physicalLawDerived=true);
altered('origin folded away',encodeWord(alphabet,[1,1]),t=>t.endpoint.packet.origin=0);
altered('occurrence order lost',zero,t=>t.events.reverse());
altered('partial zero macro',zero,t=>t.events.pop());
altered('unknown native operation',zero,t=>t.events[0].kind='fabricated');
altered('face mark changed',zero,t=>t.events[0].face[0]='99,0,0,0');
const unused=encodeWord(labels(4),[3]);unused.alphabet=labels(3);
assert(replayTrace(unused));reject('unused binary symbol code',()=>decodeWord(unused));
reject('duplicate alphabet labels',()=>encodeWord(['same','same'],[0]));
reject('invalid input symbol',()=>encodeWord(alphabet,[2]));
reject('word resource refusal is not a Ramsey counterexample',()=>encodeWord(alphabet,Array(129).fill(0)),NativeTraceResourceError);
reject('alphabet resource refusal',()=>encodeWord(labels(257),[]),NativeTraceResourceError);
const fixture={trace:encodeWord(labels(3),[2,0,1,2]),expectedWord:[2,0,1,2],expectedAlphabet:labels(3)};
const sourceHashes={};async function pin(path){if(path in sourceHashes)return;const bytes=await readFile(new URL(path,ROOT));sourceHashes[path]=hash(bytes);
 if(path.endsWith('.mjs'))for(const match of bytes.toString('utf8').matchAll(/(?:from\s*|import\s*)['"]([^'"]+\.mjs)['"]/g))if(match[1].startsWith('.')){
  const target=new URL(match[1],new URL(path,ROOT)),relative=decodeURIComponent(target.href.slice(ROOT.href.length));assert(!relative.startsWith('../'));await pin(relative);
 }
}
await pin('research/voevodsky/checkers/check_ramsey_native_word_trace.mjs');
const result={schema:'marici.ramsey-native-word-trace.replay.v1',status:'passed',cases,appendCases,associativityCases:3,
 selectedEventsInPositiveCases:selectedEvents,maxVisitedPrimitiveCells:maxVisitedCells,rejectedControls:rejected,sourceHashes,
 endpointCollisionVerified:true,cacheStateCollisionVerified:true,supportMultiplicityCollisionVerified:true,
 sourceOperations:'PN; inverse-PN; P reader-phase-advance, through actual outgoing/validateTransfer',
 simultaneousAssemblyAdmissionProved:false,codebookNativeSeedAdmissionProved:false,nativeForcingControlProved:false,rootResolved:false};
await writeFile(new URL('ramsey-native-word-trace-replay-v1.json',OUT),JSON.stringify(result,null,2)+'\n');
await writeFile(new URL('ramsey-native-word-trace-fixture-v1.json',OUT),JSON.stringify(fixture,null,2)+'\n');
console.log(JSON.stringify({status:'passed',wordCases:cases.length,appendCases,selectedEventsInPositiveCases:selectedEvents,negativeControls:rejected.length}));
