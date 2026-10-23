import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {preparedInput,canonical} from '../ramsey-word-family-selection.mjs';
import {relativeQuery,assertSectorBinding,phi,substitute} from '../ramsey-uniform-relative.mjs';
const rows=preparedInput.rows.map(context=>({declaredPoint:context.point.map(String),context}));
assert.equal(assertSectorBinding(rows),true);
const lettersSets=[[[0,0,0]],[[1,1,0]],[[-1,-1,0]],[[0,0,0],[1,1,0],[1,0,1]],[[10n**30n,10n**30n,0n]]].map(s=>s.map(p=>p.map(String)));
function words(k,n){if(!n)return [[]];return words(k,n-1).flatMap(w=>Array.from({length:k},(_,i)=>[...w,i]));}
let hits=0,misses=0,queryCases=0,substitutionCases=0;const samples=[];
for(const letters of lettersSets)for(let n=0;n<=4;n++)for(const word of words(letters.length,n))for(const palette of [1,2,4]){
 const colors=rows.map((_,i)=>i%palette),q=relativeQuery({letters,rows,word,colors,palette});queryCases++;
 const p=phi(letters,word);assert.deepEqual(q.point,p);assert.deepEqual(q.word,word);assert.equal(q.retainedRows,rows);
 if(q.kind==='selected'){hits++;assert.deepEqual(rows[q.index].declaredPoint,p);assert.equal(q.color,colors[q.index]);assert.deepEqual(q.context,rows[q.index].context);}
 else{misses++;assert.equal(q.absence.length,171);assert(q.absence.every(Boolean));assert(!rows.some(r=>r.declaredPoint.join(',')===p.join(',')));}
 if(palette===2)samples.push({letters,word,point:p,kind:q.kind,...(q.kind==='selected'?{index:q.index,color:q.color}:{})});
}
const codebook=lettersSets[3];
for(let n=0;n<=4;n++)for(const raw of words(4,n)){
 const template=raw.map(i=>i===3?null:i);
 for(let a=0;a<3;a++){const s=substitute(codebook,template,a);assert.deepEqual(phi(codebook,s.word),s.point);if(template.includes(null))assert(s.multiplicity>0);substitutionCases++;}
}
const origin=rows.find(r=>r.declaredPoint.join(',')==='0,0,0');
const zeroTask=relativeQuery({letters:[['-1','-1','0']],rows:[origin],word:[],colors:[1],palette:2});
assert.equal(zeroTask.kind,'selected');assert.deepEqual(zeroTask.point,['0','0','0']);
assert.equal(relativeQuery({letters:[['-1','-1','0']],rows:[origin],word:[0],colors:[1],palette:2}).kind,'refused');
assert.equal(relativeQuery({letters:codebook,rows:[],word:[],colors:[],palette:1}).kind,'refused');
const bad=[{declaredPoint:['1','1','0'],context:origin.context}];
const misbound=relativeQuery({letters:[['1','1','0']],rows:bad,word:[0],colors:[0],palette:1});
assert.equal(misbound.kind,'selected');assert.throws(()=>assertSectorBinding(bad),RangeError);
const controls=[];function rejects(n,f){assert.throws(f,RangeError);controls.push(n);}
const args={letters:codebook,rows,word:[0],colors:rows.map(()=>0),palette:1};
rejects('free target index',()=>relativeQuery({...args,targetIndex:0}));
rejects('out-of-range supplied palette color',()=>relativeQuery({...args,colors:rows.map(()=>1)}));
rejects('missing input color',()=>relativeQuery({...args,colors:[]}));
rejects('source point/context mismatch',()=>assertSectorBinding(bad));
const dir=new URL('../fixtures/ramsey-uniform-relative/',import.meta.url);mkdirSync(dir,{recursive:true});
const header=name=>`{-# OPTIONS --safe --cubical --guardedness #-}\nmodule ${name} where\nopen import Cubical.Foundations.Prelude\nopen import Cubical.Data.Nat.Base using (zero; suc)\nopen import Cubical.Data.Int.Base using (pos; negsuc)\nopen import Agda.Builtin.String using (String)\nopen import RamseyUniformRelative\nopen import RamseyUniformSigned\n`;
const base=header('RamseyUniformMisbound')+`at110 : Slot 1 → Point3
at110 first = pos 1 , (pos 1 , pos 0)
ctx : Slot 1 → String
ctx first = ${JSON.stringify(JSON.stringify(canonical(origin.context)))}
c : Slot 1 → Slot 1
c first = first
module U = Compiler signed-geometry 1 1 1 1 at110 at110 ctx c
w : U.Request
w = cons first nil
native-valid : U.R.Resolve (U.result-package w)
native-valid = U.result w
relative-certificate : U.Certified (U.A.phi w)
relative-certificate = U.certified-query w
`;
writeFileSync(new URL('RamseyUniformMisbound.agda',dir),base);
writeFileSync(new URL('RamseyUniformBadBinding.agda',dir),base.replaceAll('RamseyUniformMisbound','RamseyUniformBadBinding')+'\nclaimed-sector-binding : zero3 ≡ at110 first\nclaimed-sector-binding = refl\n');
writeFileSync(new URL('RamseyUniformBadLookup.agda',dir),header('RamseyUniformBadLookup')+`module L = Lookup signed-geometry
bad : L.Located origin-list (negative-letter first)
bad = L.hit first refl
`);
writeFileSync(new URL('RamseyUniformBadRefusal.agda',dir),header('RamseyUniformBadRefusal')+`bad : NegativeWord.L.Missing origin-list zero3
bad = negative-refusal
`);
writeFileSync(new URL('RamseyUniformBadSubstitution.agda',dir),header('RamseyUniformBadSubstitution')+`module A = Arithmetic signed-geometry (Slot 1) negative-letter
bad : A.phi (A.instantiate (cons A.hole-token nil) first) ≡ A.base (cons A.hole-token nil)
bad = refl
`);
writeFileSync(new URL('../results/ramsey-uniform-relative-input-v1.json',import.meta.url),JSON.stringify({queryCases,hits,misses,substitutionCases,samples,controls,
misboundNativeRelativeInterfaceAccepts:true,misboundSectorBindingRejected:true,allRegionContextConstructionProved:false,fullUniformTaskPackageProved:false},null,2)+'\n');
console.log(JSON.stringify({queryCases,hits,misses,substitutionCases,controls:controls.length}));
