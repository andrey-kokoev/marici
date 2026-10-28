import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {extendPrepared,freshRebuild4,verifyExtension,region4} from '../ramsey-family-refinement.mjs';
import {preparedInput,words,labels,queryWord,compileWordProgram} from '../ramsey-word-family-selection.mjs';
import {canonical,same,encodeWord} from '../ramsey-native-word-trace.mjs';
const copy=x=>structuredClone(x),data=extendPrepared();
assert.equal(verifyExtension(data),true);assert(same(data.oldRows,preparedInput.rows));
assert.equal(data.oldRows.length,171);assert.equal(data.newRows.length,365);assert.equal(region4().length,365);
assert.equal(data.joint3.valid,false);assert.equal(data.joint4.valid,false);
const fresh=freshRebuild4(),freshIndex=new Map(fresh.map((r,i)=>[r.point.join(','),i]));
const newIndex=new Map(data.newRows.map((r,i)=>[r.point.join(','),i]));
const freshMismatch=data.oldRows.filter(r=>!same(r,fresh[freshIndex.get(r.point.join(','))])).length;
assert.equal(freshMismatch,171);
const controls=[];const rejects=(n,f)=>{assert.throws(f,RangeError);controls.push(n);};
function bad(name,change){const v=copy(data);change(v);rejects(name,()=>verifyExtension(v));}
bad('changed old outside reference',v=>{v.newRows[0].packet.chart.aliases.C2=v.newRows[0].packet.chart.aliases.C0;});
bad('old source context deleted',v=>{v.newRows.splice(0,1);});
bad('new boundary context changed',v=>{v.newRows[364].PN.operation.face=[];});
bad('wrong old index embedding',v=>{v.embedding[1]=0;});
bad('fresh rebuild without reference transport',v=>{v.newRows=fresh;v.embedding=v.oldRows.map(r=>freshIndex.get(r.point.join(',')));});
rejects('word/answer injection into source extension',()=>extendPrepared({word:[1,1,1],point:[3,3,0]}));
const program=compileWordProgram({prepared:preparedInput});
const colorFunctions=[r=>(r.point[1]%3+3)%3,r=>(r.point[0]-r.point[2]+20)%4,r=>0],cases=[];
let comparisons=0,freshReadoutComparisons=0;
for(const f of colorFunctions){
 const bigColors=data.newRows.map(f),oldColors=data.embedding.map(i=>bigColors[i]);
 for(const word of words){
  const request=encodeWord(labels,word),old=queryWord({program,request,colors:oldColors});
  const point=[0,1,2].map(j=>word.reduce((n,i)=>n+program.pattern[i][j],0)),j=newIndex.get(point.join(','));
  assert.equal(data.embedding[old.regionIndex],j);assert(same(old.context,data.newRows[j]));assert.equal(old.color,bigColors[j]);comparisons++;
  const k=freshIndex.get(point.join(','));assert(same(fresh[k].point,point)&&f(fresh[k])===old.color);freshReadoutComparisons++;
  if(cases.length<27)cases.push({word,oldIndex:old.regionIndex,newIndex:j,point,color:old.color,request});
 }
}
const ri=i=>'r'+String(i).padStart(3,'0'),ni=i=>'n'+String(i).padStart(3,'0'),wp=w=>'(W.word '+w.map(x=>'W.l'+x).join(' ')+')',pt=p=>'('+p[0]+' , ('+p[1]+' , '+p[2]+'))';
const template=readFileSync(new URL('../agda/RamseyFamilyRefinement.agda.in',import.meta.url),'utf8');
function generate(rows,embedding,moduleName){
 const map=new Map(rows.map((r,i)=>[r.point.join(','),i]));
 return template.replace('module RamseyFamilyRefinement where','module '+moduleName+' where')
 .replace('@@NEWINDICES@@',rows.map((_,i)=>'  '+ni(i)+' : NewIndex').join('\n'))
 .replace('@@EMBED@@',embedding.map((e,i)=>'embed Old.'+ri(i)+' = '+ni(e)).join('\n'))
 .replace('@@CONTEXTS@@',rows.map((r,i)=>'new-context '+ni(i)+' = '+JSON.stringify(JSON.stringify(canonical(r)))).join('\n'))
 .replace('@@POINTS@@',rows.map((r,i)=>'new-point '+ni(i)+' = '+pt(r.point.map(x=>x+4))).join('\n'))
 .replace('@@COMPILE@@',cases.map(c=>'compile-new '+wp(c.word)+' = '+ni(map.get(c.point.join(',')))).join('\n'))
 .replace('@@CONTEXT-PROOFS@@',data.oldRows.map((_,i)=>'  context-preserved Old.'+ri(i)+' = refl').join('\n'))
 .replace('@@INDEX-PROOFS@@',cases.map(c=>'  index-square '+wp(c.word)+' = refl').join('\n'))
 .replace('@@POINT-PROOFS@@',cases.map(c=>'  point-square '+wp(c.word)+' = refl').join('\n'));
}
const text=generate(data.newRows,data.embedding,'RamseyFamilyRefinement');
writeFileSync(new URL('../agda/RamseyFamilyRefinement.agda',import.meta.url),text);
const dir=new URL('../fixtures/ramsey-family-refinement/',import.meta.url);mkdirSync(dir,{recursive:true});
const freshCode=generate(fresh,data.oldRows.map(r=>freshIndex.get(r.point.join(','))),'RamseyFamilyFreshRebuild');
writeFileSync(new URL('RamseyFamilyFreshNativeOnly.agda',dir),freshCode.split('  -- BEGIN SOURCE TRANSPORT')[0].replace('module RamseyFamilyFreshRebuild where','module RamseyFamilyFreshNativeOnly where'));
writeFileSync(new URL('RamseyFamilyFreshRebuild.agda',dir),freshCode);
const origin=newIndex.get('0,0,0'),target=newIndex.get('3,3,0');
const wrong=text.replace('compile-new '+wp([1,1,1])+' = '+ni(target),'compile-new '+wp([1,1,1])+' = '+ni(origin));assert(wrong!==text);
writeFileSync(new URL('RamseyFamilyWrongQuery.agda',dir),wrong.replace('module RamseyFamilyRefinement where','module RamseyFamilyWrongQuery where'));
writeFileSync(new URL('RamseyFamilyWrongSeed.agda',dir),`{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyFamilyWrongSeed where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero)
open import RamseyFamilyRefinement
import RamseyRegionFamily as Old
module X = Refine (λ _ → zero)
bad : (i : Old.RegionIndex) → X.Big.Resolve (X.Small.B.fiber i)
bad i = X.Big.seed (n000 , refl)
`);
writeFileSync(new URL('../results/ramsey-family-refinement-input-v1.json',import.meta.url),JSON.stringify({data,cases,comparisons,
 freshReadoutComparisons,freshLiteralMismatches:freshMismatch,sourceControls:controls,
 freshRebuildRows:fresh,wholeFamilyEquivalenceClaimed:false,physicalPolicyAdmissionProved:false,rootResolved:false},null,2)+'\n');
console.log(JSON.stringify({old:171,new:365,added:194,comparisons,freshReadoutComparisons,freshLiteralMismatches:freshMismatch,controls:controls.length}));
