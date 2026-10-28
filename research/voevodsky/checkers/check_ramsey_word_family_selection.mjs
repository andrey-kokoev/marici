import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {preparedInput,words,labels,compileWordProgram,queryWord,verifyResponse,same,canonical,copy} from '../ramsey-word-family-selection.mjs';
import {verifyPrepared} from '../ramsey-native-region-family.mjs';
import {encodeWord} from '../ramsey-native-word-trace.mjs';
assert.equal(verifyPrepared(preparedInput),true);
const program=compileWordProgram({prepared:preparedInput});
assert.deepEqual(program.pattern,[[0,0,0],[1,1,0],[1,0,1]]);
const colors=preparedInput.rows.map(r=>(r.point[1]%3+3)%3),cases=[];
let queryCases=0,recoloringIndexComparisons=0;
for(const word of words){
 const request=encodeWord(labels,word),response=queryWord({program,request,colors});
 assert.equal(verifyResponse(program,request,colors,response),true);queryCases++;cases.push({word,response});
 for(const other of [colors.map(c=>2-c),colors.map(()=>0)]){
  const v=queryWord({program,request,colors:other});assert.equal(verifyResponse(program,request,other,v),true);
  assert.equal(v.regionIndex,response.regionIndex);assert(same(v.context,response.context));queryCases++;recoloringIndexComparisons++;
 }
}
const find=w=>cases.find(c=>same(c.word,w)).response,controls=[];
function rejects(name,f){assert.throws(f,RangeError);controls.push(name);}
const request=encodeWord(labels,[1,1,1]),response=find([1,1,1]),origin=program.prepared.rows.findIndex(r=>same(r.point,[0,0,0]));
assert.deepEqual(response.context.point,[3,3,0]);
rejects('free target-index query parameter',()=>queryWord({program,request,colors,targetIndex:origin}));
rejects('free point-answer query parameter',()=>queryWord({program,request,colors,targetPoint:[3,3,0]}));
const badProgram=copy(program);badProgram.entries.find(e=>same(e.word,[1,1,1])).regionIndex=origin;
rejects('changed native program index declaration',()=>queryWord({program:badProgram,request,colors}));
const wrong=copy(response);wrong.regionIndex=origin;wrong.context=copy(program.prepared.rows[origin]);wrong.color=colors[origin];
rejects('native-valid wrong-index response fails task square',()=>verifyResponse(program,request,colors,wrong));
const badColor=copy(response);badColor.color=(badColor.color+1)%3;
rejects('incorrect supplied color',()=>verifyResponse(program,request,colors,badColor));
const badRef=copy(response);badRef.context.packet.chart.aliases.C2=badRef.context.packet.chart.aliases.C0;
rejects('altered selected native context reference',()=>verifyResponse(program,request,colors,badRef));
const changedTrace=copy(response);changedTrace.request.events[0].permutation[4]=0;
rejects('changed retained request trace',()=>verifyResponse(program,request,colors,changedTrace));
rejects('swapped equal-sum requests',()=>verifyResponse(program,find([1,1,2]).request,colors,find([1,2,1])));
rejects('incomplete input colors',()=>queryWord({program,request,colors:colors.slice(1)}));
const incomplete=copy(preparedInput);incomplete.rows.pop();
rejects('missing unselected region premise',()=>compileWordProgram({prepared:incomplete}));
const missingWord=copy(program);missingWord.entries.pop();
rejects('missing unselected word premise',()=>queryWord({program:missingWord,request,colors}));
rejects('unsupported word length',()=>queryWord({program,request:encodeWord(labels,[1,1]),colors}));
const wp=w=>'(word '+w.map(x=>'l'+x).join(' ')+')',ri=i=>'r'+String(i).padStart(3,'0'),pt=p=>'('+p[0]+' , ('+p[1]+' , '+p[2]+'))';
const template=readFileSync(new URL('../agda/RamseyWordFamilySelection.agda.in',import.meta.url),'utf8');
const text=template
 .replace('@@LETTERS@@',program.pattern.map((p,i)=>'letter-point l'+i+' = '+pt(p)).join('\n'))
 .replace('@@TRACES@@',cases.map(c=>'canonical-trace '+wp(c.word)+' = '+JSON.stringify(JSON.stringify(canonical(c.response.request)))).join('\n'))
 .replace('@@REGION@@',program.prepared.rows.map((r,i)=>'region-point '+ri(i)+' = '+pt(r.point.map(x=>x+3))).join('\n'))
 .replace('@@INDICES@@',program.entries.map(e=>'compile-index '+wp(e.word)+' = '+ri(e.regionIndex)).join('\n'))
 .replace('@@SQUARES@@',words.map(w=>'  point-square '+wp(w)+' = refl').join('\n'));
writeFileSync(new URL('../agda/RamseyWordFamilySelection.agda',import.meta.url),text);
const fixture=new URL('../fixtures/ramsey-word-family-selection/',import.meta.url);mkdirSync(fixture,{recursive:true});
const oldLine='compile-index '+wp([1,1,1])+' = '+ri(response.regionIndex),newLine='compile-index '+wp([1,1,1])+' = '+ri(origin);
assert(text.includes(oldLine)&&oldLine!==newLine);
const wrongText=text.replace(oldLine,newLine);
writeFileSync(new URL('RamseyWordFamilyWrongIndexNative.agda',fixture),wrongText.split('  -- BEGIN TASK SQUARE')[0].replace('module RamseyWordFamilySelection where','module RamseyWordFamilyWrongIndexNative where'));
writeFileSync(new URL('RamseyWordFamilyWrongIndex.agda',fixture),wrongText.replace('module RamseyWordFamilySelection where','module RamseyWordFamilyWrongIndex where'));
writeFileSync(new URL('RamseyWordFamilyWrongPremise.agda',fixture),`{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyWordFamilyWrongPremise where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero)
open import RamseyWordFamilySelection
import NativeTableRules as Rules
module Native = Rules.Native ℓ-zero
module X = Query (λ _ → zero)
bad : X.R.Resolve (Native.Pi-package Word X.point-package)
bad = X.R.apply (Native.P-kind , Word , X.point-package) (λ { (lift w) → X.point-derivation (word l0 l0 l0) })
`);
const output={program,colors,cases,queryCases,recoloringIndexComparisons,sourceControls:controls,
 nativeWordPremises:27,nativeRegionPremisesPerWord:171,retainedFieldPremiseSlots:27*171,
 tableCompiledWithoutColors:true,freeTargetIndexInput:false,newSeedPolicyIntroduced:false,
 hostTraceDecoderRetained:true,hostTableCompilerRetained:true,autonomousNativeControllerProved:false,rootResolved:false};
writeFileSync(new URL('../results/ramsey-word-family-selection-input-v1.json',import.meta.url),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({requests:27,queryCases,recoloringIndexComparisons,controls:controls.length,retainedFieldPremiseSlots:4617}));
