import assert from 'node:assert/strict';
import {writeFileSync,mkdirSync} from 'node:fs';
import {exactContext,verifyContext,prepareExact,verifyRegion,queryExact,bindLegacy,observedPoint} from '../ramsey-exact-source.mjs';
import {extendPrepared} from '../ramsey-family-refinement.mjs';
const copy=x=>structuredClone(x),regions=[],controls=[];
for(let n=0;n<=5;n++){const g=prepareExact(String(n));assert.equal(verifyRegion(g),true);regions.push(g);for(const c of g.rows)assert.equal(verifyContext(c),true);}
let inclusions=0;
for(let n=0;n<5;n++)for(const c of regions[n].rows){assert.deepEqual(regions[n+1].rows.find(d=>d.namespace===c.namespace),c);inclusions++;}
const legacy=extendPrepared(),witnesses=legacy.newRows.map(row=>bindLegacy(exactContext(row.point.map(String)),row));assert.equal(witnesses.length,365);
const large=[];for(const p of [['1000000000000000000000000000000','-1000000000000000000000000000000','0'],['-1000000000000000000000000000001','3','2']]){const c=exactContext(p);assert.equal(verifyContext(c),true);assert.deepEqual(observedPoint(c),p);large.push(c);}
function words(k,n){return n===0?[[]]:words(k,n-1).flatMap(w=>Array.from({length:k},(_,i)=>[...w,i]));}
let queries=0,selected=0,refused=0;
const letters=[['0','0','0'],['1','1','0'],['-1','0','-1']];
for(const g of regions.slice(0,4))for(let n=0;n<=3;n++)for(const word of words(3,n))for(const palette of [1,3]){
 const colors=g.rows.map((_,i)=>i%palette),q=queryExact({letters,region:g,word,colors,palette});queries++;
 if(q.kind==='selected'){selected++;assert.deepEqual(observedPoint(q.context),q.point);assert.equal(q.color,colors[q.index]);}
 else{refused++;assert(q.absence.every(Boolean));}
}
function rejects(n,f){assert.throws(f,RangeError);controls.push(n);}
const c=copy(regions[1].rows[0]);c.references.C2=c.references.C0;rejects('changed outside reference',()=>verifyContext(c));
const missing=copy(regions[1]);missing.rows.pop();rejects('incomplete region',()=>verifyRegion(missing));
const perm=copy(regions[1].rows[0]);perm.target.permutation=[0,1,2,3,4];rejects('wrong complete PN permutation',()=>verifyContext(perm));
const old=copy(legacy.newRows[0]);old.PN.operation.source=old.PN.operation.target;rejects('wrong scoped legacy pointer',()=>bindLegacy(exactContext(old.point.map(String)),old));
const wrong=copy(legacy.newRows[0]);wrong.packet.chart.aliases.C2=wrong.packet.chart.aliases.C0;rejects('legacy outside reference changed',()=>bindLegacy(exactContext(wrong.point.map(String)),wrong));
const namespace=copy(regions[1].rows[0]);namespace.namespace='unwitnessed';rejects('unwitnessed namespace',()=>verifyContext(namespace));
const args={letters,region:regions[0],word:[],colors:[0],palette:1};rejects('free target index',()=>queryExact({...args,targetIndex:0}));
rejects('not D3',()=>exactContext(['1','0','0']));
const dir=new URL('../fixtures/ramsey-exact-source/',import.meta.url);mkdirSync(dir,{recursive:true});
const header=name=>`{-# OPTIONS --safe --cubical --guardedness #-}\nmodule ${name} where\nopen import Cubical.Foundations.Prelude\nopen import Cubical.Data.Nat.Base using (zero; suc)\nopen import Cubical.Data.Int.Base using (pos)\nopen import Cubical.Data.Unit.Base using (tt)\nopen import RamseyUniformRelative using (Slot; first; next; nil; cons)\nopen import RamseyUniformSigned using (zero3)\nopen import RamseyExactSource\n`;
writeFileSync(new URL('RamseyExactInstances.agda',dir),header('RamseyExactInstances')+`letters : Slot 1 → Shift
letters first = pos 1 , (pos 0 , pos 0)
module E = Query 0 1 0 1 letters (λ _ → first)
empty-word : E.R.Resolve (E.result-package nil)
empty-word = E.result nil
module O = Query 0 1 1 1 letters (λ _ → first)
outside-word : O.R.Resolve (O.result-package (cons first nil))
outside-word = O.result (cons first nil)
`);
writeFileSync(new URL('RamseyExactBadBinding.agda',dir),header('RamseyExactBadBinding')+`bad : observed-point (prepared zero3) ≡ project (pos 1 , (pos 0 , pos 0))
bad = refl
`);
writeFileSync(new URL('RamseyExactBadReference.agda',dir),header('RamseyExactBadReference')+`bad : reference (prepared zero3) C2 ≡ reference (prepared zero3) C0
bad = refl
`);
writeFileSync(new URL('RamseyExactBadMember.agda',dir),header('RamseyExactBadMember')+`bad : Member 0 (pos 1 , (pos 0 , pos 0))
bad = tt
`);
writeFileSync(new URL('RamseyExactBadPermutation.agda',dir),header('RamseyExactBadPermutation')+`bad : permutation first ≡ first
bad = refl
`);
writeFileSync(new URL('../results/ramsey-exact-source-input-v1.json',import.meta.url),JSON.stringify({regions,inclusions,legacyBindings:witnesses.length,
 witnesses,large,queries,selected,refused,controls,exactSourceInterpretationOnly:true,legacyWholeCacheEquivalenceClaimed:false,unboundedNumberAPIClaimed:false,physicalAdmissionProved:false},null,2)+'\n');
console.log(JSON.stringify({contexts:regions.reduce((n,g)=>n+g.rows.length,0),inclusions,legacyBindings:365,queries,selected,refused,controls:controls.length}));
