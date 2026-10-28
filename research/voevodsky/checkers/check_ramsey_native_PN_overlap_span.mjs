import assert from 'node:assert/strict';
import {writeFileSync,mkdirSync} from 'node:fs';
import {GenerativeAssemblyRules} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {packetSnapshot} from '../ramsey-native-word-trace.mjs';
import {canonical} from '../ramsey-word-family-selection.mjs';
const copy=x=>structuredClone(x),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b),names=['C0','M0','C1','M1'];
function permutations(a){return a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];}
const r=new GenerativeAssemblyRules(),cell=r.charts[r.packets[r.root].chart].cell,vertices=r.geometry.cells[cell].vertices,frames=[],ports=new Map();let validatedTransfers=0;
for(const p of permutations([0,1,2,3])){
 const c=frames.length,aliases=Object.fromEntries(names.map((n,i)=>[n,vertices[p[i]]])),chart=r.completeP(cell,aliases),base=r.packet(chart,0,[0,1,2,3,4]);
 const ops=r.outgoing(base).map(i=>r.operations[i]),pn=ops.find(o=>o.kind==='PN'),reader=ops.find(o=>o.kind==='reader-phase-advance');
 const readerPN=r.outgoing(reader.target).map(i=>r.operations[i]).find(o=>o.kind==='PN');
 for(const op of [pn,reader,readerPN]){assert.equal(r.validateTransfer(op),true);validatedTransfers++;}
 const role=Object.fromEntries(names.map(n=>[aliases[n],n[0]]));
 for(const [op,history] of [[pn,[]],[readerPN,[reader]]]){
  const face=vertices.findIndex(v=>!op.face.includes(v));assert(face>=0);assert.equal(role[vertices[face]],'C');
  const src=r.packets[op.source],dst=r.packets[op.target];
  const record={chart:c,face,faceVertices:[...op.face],role,permitMCount:op.face.filter(v=>role[v]==='M').length,
   base:packetSnapshot(r,base),baseFrame:phaseFrame(r.charts[chart],0),prefix:copy(history),
   source:packetSnapshot(r,op.source),sourceFrame:phaseFrame(r.charts[src.chart],src.origin),
   operation:copy(op),target:packetSnapshot(r,op.target),targetFrame:phaseFrame(r.charts[dst.chart],dst.origin)};
  assert.equal(record.permitMCount,2);ports.set(c+':'+face,record);
 }
 frames.push({chart:c,p,roles:role,eligible:[p[0],p[2]].sort()});
}
assert.equal(ports.size,48);
const domain=(a,b)=>frames[a].eligible.filter(f=>frames[b].eligible.includes(f));
function select(a,b,f){assert(domain(a,b).includes(f),'not a certified common port');return {face:f,permits:[{chart:a,MCount:2},{chart:b,MCount:2}],source:ports.get(a+':'+f),target:ports.get(b+':'+f)};}
function compose(a,b,c,f){assert(frames[a].eligible.includes(f)&&frames[b].eligible.includes(f)&&frames[c].eligible.includes(f),'empty or non-common triple');
 return {face:f,charts:[a,b,c],AB:select(a,b,f),BC:select(b,c,f),AC:select(a,c,f),fullSource:[ports.get(a+':'+f),ports.get(b+':'+f),ports.get(c+':'+f)]};}
function verifyComposite(v){const [a,b,c]=v.charts,expected=compose(a,b,c,v.face);assert(same(v,expected),'composition/history changed');
 assert(same(v.AB.target,v.BC.source));assert(same(v.fullSource[1],v.AB.target));return true;}
let pairCells=0,emptyPairs=0,pairPorts=0,tripleCells=0,emptyTriples=0,triplePorts=0,pairwiseButTripleEmpty=0;
for(let a=0;a<24;a++)for(let b=0;b<24;b++){
 pairCells++;const common=domain(a,b);if(!common.length)emptyPairs++;for(const f of common){const v=select(a,b,f);assert.equal(v.source.permitMCount,2);assert.equal(v.target.permitMCount,2);pairPorts++;}
 for(let c=0;c<24;c++){tripleCells++;const common3=common.filter(f=>frames[c].eligible.includes(f));if(!common3.length){emptyTriples++;if(common.length&&domain(b,c).length&&domain(a,c).length)pairwiseButTripleEmpty++;}
  for(const f of common3){const v=compose(a,b,c,f);assert.equal(verifyComposite(v),true);triplePorts++;}
 }
}
const idx=p=>frames.findIndex(f=>same(f.p,p));const A=idx([0,1,2,3]),B=idx([0,2,1,3]),C=idx([1,0,2,3]),D=idx([0,1,3,2]);assert([A,B,C,D].every(i=>i>=0));
assert(domain(A,B).length&&domain(B,C).length&&domain(A,C).length);assert.equal(domain(C,D).length,0);
const example=compose(A,B,D,0),controls=[];function rejects(n,f){assert.throws(f);controls.push(n);}
const missing=copy(example);delete missing.AB.source.source.chart.aliases.C2;rejects('erase outside reference',()=>verifyComposite(missing));
const lost=frames[A].eligible.find(f=>!frames[B].eligible.includes(f));rejects('extend partial span to lost port',()=>select(A,B,lost));
rejects('select empty pair',()=>select(C,D,0));rejects('pairwise nonempty used as triple witness',()=>compose(A,B,C,0));
const seam=copy(example);seam.BC.source.face=1;rejects('change shared middle source',()=>verifyComposite(seam));
const coefficient=copy(example);coefficient.fullSource[1].target.packet.permutation.pop();rejects('drop fifth coefficient slot',()=>verifyComposite(coefficient));
const dir=new URL('../fixtures/ramsey-native-PN-overlap-span/',import.meta.url);mkdirSync(dir,{recursive:true});
const header=`{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPNOverlapExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; _+_)
open import Cubical.Data.Empty.Base using (⊥)
import Cubical.Data.Empty as Empty
open import Agda.Builtin.String using (String)
open import RamseySingleFrameFaces
open import RamseyNativePNOverlapSpan
`;
const cs=[['A',A],['B',B],['C',C],['D',D]],vs=['c0','m0','c1','m1'];
let code=header+`data Chart : Type where
  A B C D : Chart
role : Chart → Vertex → ℕ
`;
for(const [name,i] of cs)for(let v=0;v<4;v++)code+='role '+name+' '+vs[v]+' = '+(frames[i].roles[vertices[v]]==='M'?1:0)+'\n';
code+=`Permit : Chart → Vertex → Type
Permit c f = count (λ i → role c (face f i)) ≡ 2
packet : (c : Chart) (f : Vertex) → Permit c f → String
`;
for(const [name,i] of cs)for(let f=0;f<4;f++)code+='packet '+name+' '+vs[f]+' p = '+(ports.has(i+':'+f)?JSON.stringify(JSON.stringify(canonical(ports.get(i+':'+f)))):'Empty.rec (one-not-two p)')+'\n';
code+=`module S = Spans Chart Vertex Permit packet
example : S.Triple A B D
example = c0 , (refl , (refl , refl))
native-example : S.R.Resolve (S.composition-package A B D example)
native-example = S.composition-proof A B D example
pair-AB : S.Common A B
pair-AB = c0 , (refl , refl)
pair-BC : S.Common B C
pair-BC = m0 , (refl , refl)
pair-AC : S.Common A C
pair-AC = c1 , (refl , refl)
no-empty-pair : S.Common C D → ⊥
no-empty-pair (c0 , (p , q)) = one-not-two p
no-empty-pair (m0 , (p , q)) = one-not-two q
no-empty-pair (c1 , (p , q)) = one-not-two q
no-empty-pair (m1 , (p , q)) = one-not-two p
no-empty-triple : S.Triple A B C → ⊥
no-empty-triple (c0 , (p , (q , s))) = one-not-two s
no-empty-triple (m0 , (p , (q , s))) = one-not-two p
no-empty-triple (c1 , (p , (q , s))) = one-not-two q
no-empty-triple (m1 , (p , (q , s))) = one-not-two p
empty-family : S.R.Resolve (S.span-package C D)
empty-family = S.span-proof C D
`;
writeFileSync(new URL('RamseyPNOverlapExamples.agda',dir),code);
const badHeader=n=>`{-# OPTIONS --safe --cubical --guardedness #-}\nmodule ${n} where\nopen import Cubical.Foundations.Prelude\nopen import RamseySingleFrameFaces\nopen import RamseyPNOverlapExamples\n`;
writeFileSync(new URL('RamseyPNOverlapBadEmptyPair.agda',dir),badHeader('RamseyPNOverlapBadEmptyPair')+'bad : S.Common C D\nbad = c0 , (refl , refl)\n');
writeFileSync(new URL('RamseyPNOverlapBadTriple.agda',dir),badHeader('RamseyPNOverlapBadTriple')+'bad : S.Triple A B C\nbad = c0 , (refl , (refl , refl))\n');
writeFileSync(new URL('RamseyPNOverlapBadLostPort.agda',dir),badHeader('RamseyPNOverlapBadLostPort')+'bad : S.Common A B\nbad = c1 , (refl , refl)\n');
writeFileSync(new URL('../results/ramsey-native-PN-overlap-span-input-v1.json',import.meta.url),JSON.stringify({frames,ports:[...ports.values()],validatedTransfers,pairCells,emptyPairs,pairPorts,tripleCells,emptyTriples,triplePorts,pairwiseButTripleEmpty,
 demoCharts:{A,B,C,D},example,controls,policyBeforeOverlapSelection:true,compositionResultSeeded:false,totalGaugeClaimed:false,physicalRoleChangeClaimed:false,globalAssemblyClaimed:false},null,2)+'\n');
console.log(JSON.stringify({inputs:ports.size,validatedTransfers,pairCells,emptyPairs,pairPorts,tripleCells,emptyTriples,triplePorts,pairwiseButTripleEmpty,controls:controls.length}));
