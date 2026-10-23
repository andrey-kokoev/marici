import assert from 'node:assert/strict';
import {writeFileSync,mkdirSync} from 'node:fs';
import {GenerativeAssemblyRules} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {makeLatticeItem} from '../../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {packetSnapshot} from '../ramsey-native-word-trace.mjs';
import {phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {prepareExact,exactContext,bindLegacy} from '../ramsey-exact-source.mjs';
const rules=new GenerativeAssemblyRules(),id=rules.root,p=rules.packets[id],op=rules.outgoing(id).map(i=>rules.operations[i]).find(o=>o.kind==='PN'),n=rules.packets[op.target];
assert.equal(rules.validateTransfer(op),true);
const canonical={index:0,point:[0,0,0],shift:[0,0,0,0],packet:packetSnapshot(rules,id),frame:phaseFrame(rules.charts[p.chart],0),
 PN:{operation:structuredClone(op),target:packetSnapshot(rules,op.target),targetFrame:phaseFrame(rules.charts[n.chart],0)}};
const binding=bindLegacy(exactContext(['0','0','0']),canonical);
function chart(context,color,slot){return {kind:'native-E-chart-description',index:context.shift.slice(1),canonical,color,slot,
 premiseGenerator:'constant canonical input certificate',indexDomain:'all exact integer shifts; not a finite enumerated tree'};}
function reference(c,name){const [a,b,d]=c.index.map(BigInt),delta=[-(a+b+d),a,b,d];return canonical.packet.chart.aliases[name].split(',').map((x,j)=>String(BigInt(x)+delta[j])).join(',');}
function point(c){const b=reference(c,'C0').split(',').map(BigInt);return [b[1]+b[2],b[1]+b[3],b[2]+b[3]].map(String);}
let inputCases=0,referenceComparisons=0;
for(let radius=0;radius<=4;radius++)for(const [i,context] of prepareExact(String(radius)).rows.entries()){
 const c=chart(context,i%3,i);inputCases++;
 for(const name of ['C0','M0','C1','M1','C2']){assert.equal(reference(c,name),context.references[name]);referenceComparisons++;}
 assert.deepEqual(point(c),context.point);assert.equal(c.color,i%3);assert.equal(c.canonical,canonical);
}
const region=prepareExact('1'),colors=region.rows.map((_,i)=>i%2);
const I=i=>({op:'input',i}),P=F=>({op:'P',F}),E=(F,j)=>({op:'E',F,j});
function source(expr){if(expr.op==='input')return {context:region.rows[expr.i],color:colors[expr.i]};if(expr.op==='P')return expr.F.map(source);return {index:expr.j,value:source(expr.F[expr.j])};}
function target(expr){if(expr.op==='input')return chart(region.rows[expr.i],colors[expr.i],expr.i);if(expr.op==='P')return expr.F.map(target);return {index:expr.j,value:target(expr.F[expr.j])};}
function restore(expr,value){if(expr.op==='input')return {context:exactContext(point(value)),color:value.color};if(expr.op==='P')return expr.F.map((p,i)=>restore(p,value[i]));return {index:value.index,value:restore(expr.F[value.index],value.value)};}
const inputs=region.rows.map((_,i)=>I(i)),expressions=[...inputs,P(inputs),...inputs.map((_,i)=>E(inputs,i))];
const program=P(inputs.map((_,i)=>E(inputs,i))),request=E(program.F,2),bundle=P([P(inputs),program,request]);expressions.push(program,request,bundle);
for(const expr of expressions)assert.deepEqual(restore(expr,target(expr)),source(expr));
const controls=[];function reject(n,f){assert.throws(f);controls.push(n);}
const c=chart(exactContext(['1','1','0']),0,0);const noTag=structuredClone(c);noTag.index=['0','0','0'];reject('erase native chart index',()=>assert.deepEqual(point(noTag),['1','1','0']));
const badColor=structuredClone(c);badColor.color=1;reject('change input color',()=>assert.equal(badColor.color,c.color));
const badC2=reference(c,'C0');reject('drop outside reference',()=>assert.equal(badC2,reference(c,'C2')));
const moved=target(bundle);moved[2].index=3;reject('swap request selector',()=>assert.deepEqual(restore(bundle,moved),source(bundle)));
// Direct absolute Number port: origin is exactly representable, but +e1 is not.
const u=2**53,owner=makeLatticeItem('tetrahedron',[-u,u,0,0]);
const actualM0=owner.components[0][1].map(x=>String(BigInt(x))),expectedM0=[-BigInt(u),BigInt(u)+1n,0n,0n].map(String);
assert.notDeepEqual(actualM0,expectedM0);assert.equal(u+1,u);
const large=chart(exactContext([String(BigInt(u)),String(BigInt(u)),'0']),0,0);assert.deepEqual(point(large),[String(BigInt(u)),String(BigInt(u)),'0']);
const dir=new URL('../fixtures/ramsey-chart-interpretation/',import.meta.url);mkdirSync(dir,{recursive:true});
const header=name=>`{-# OPTIONS --safe --cubical --guardedness #-}\nmodule ${name} where\nopen import Cubical.Foundations.Prelude\nopen import Cubical.Data.Nat.Base using (zero; suc)\nopen import Cubical.Data.Int.Base using (pos)\nopen import Cubical.Data.Unit.Base using (tt)\nopen import RamseyUniformRelative using (Slot; first; next; nil; cons)\nopen import RamseyUniformSigned using (zero3)\nopen import RamseyExactSource using (Region; Shift; Member)\nopen import RamseyChartInterpretation\n`;
writeFileSync(new URL('RamseyChartInstances.agda',dir),header('RamseyChartInstances')+`color : Region 0 → Slot 1
color _ = first
module M = Interpretation 0 1 color
letters : Slot 1 → Shift
letters first = pos 1 , (pos 0 , pos 0)
module Q = M.Queries 1 1 letters
native : M.T.Resolve (M.target (Q.result-program (cons first nil)))
native = Q.interpreted-result (cons first nil)
`);
writeFileSync(new URL('RamseyChartBadReference.agda',dir),header('RamseyChartBadReference')+`import RamseyExactSource as X
bad : chart-reference (pos 1 , (pos 0 , pos 0)) root-context X.C2 ≡ canonical-reference root-context X.C2
bad = refl
`);
writeFileSync(new URL('RamseyChartBadSourceSeed.agda',dir),header('RamseyChartBadSourceSeed')+`color : Region 0 → Slot 1
color _ = first
module M = Interpretation 0 1 color
bad : M.T.Resolve (M.source-fiber (zero3 , tt))
bad = M.T.seed ((zero3 , tt) , refl)
`);
writeFileSync(new URL('RamseyChartBadSelector.agda',dir),header('RamseyChartBadSelector')+`color : Region 0 → Slot 1
color _ = first
module M = Interpretation 0 1 color
F : Slot 2 → M.Program
F _ = M.input (zero3 , tt)
bad : fst (M.N.value (M.target (M.pick (Slot 2) F first))) ≡ next first
bad = refl
`.replace('M.N.value','N.value'));
writeFileSync(new URL('../results/ramsey-chart-interpretation-input-v1.json',import.meta.url),JSON.stringify({canonical,binding,inputCases,referenceComparisons,programCases:expressions.length,controls,
 numberPort:{shift:[String(-BigInt(u)),String(BigInt(u)),'0','0'],actualM0,expectedM0,referenceMismatch:true},
 chartLargePoint:point(large),targetSeedsOnlyCanonicalContextAndInputColors:true,exactContextAtomsAssumedAsTargetSeeds:false,
 infiniteIndexDomainExplicit:true,finiteFullShiftUnfoldingClaimed:false,physicalTrajectoryClaimed:false,wholeCacheEquivalenceClaimed:false},null,2)+'\n');
console.log(JSON.stringify({inputCases,referenceComparisons,programCases:expressions.length,controls:controls.length,numberPortRefuted:true}));
