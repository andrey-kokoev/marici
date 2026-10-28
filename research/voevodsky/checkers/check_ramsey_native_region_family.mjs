import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {prepareRegion,verifyPrepared,region3,project4,shift4} from '../ramsey-native-region-family.mjs';
import {canonical,same} from '../ramsey-native-word-trace.mjs';
const copy=x=>structuredClone(x),data=prepareRegion();
assert.equal(verifyPrepared(data),true);assert.equal(data.rows.length,171);
assert.equal(data.attemptedJointAssembly.valid,false);assert.equal(data.attemptedJointAssembly.reason,'global-CM-role-conflict');
assert(data.rows.some(r=>same(r.point,[3,3,0])&&same(project4(r.frame.window[0].vertex),[3,3,0])));
const planes=new Set(data.rows.map(row=>project4(row.packet.chart.aliases.M0)[1]));assert.equal(planes.size,7);
const controls=[];const rejects=(name,f)=>{assert.throws(f,RangeError);controls.push(name);};
function corrupt(name,f){const b=copy(data);f(b);rejects(name,()=>verifyPrepared(b));}
corrupt('delete unselected input row',b=>b.rows.pop());
corrupt('duplicate region row',b=>b.rows[1]=copy(b.rows[0]));
corrupt('alter native outside reference',b=>b.rows[0].packet.chart.aliases.C2=b.rows[0].packet.chart.aliases.C0);
corrupt('alter five-slot input packet',b=>b.rows[0].packet.packet.permutation[4]=0);
corrupt('alter PN boundary',b=>b.rows[0].PN.operation.face=[]);
rejects('inject word argument',()=>prepareRegion({word:[1,1,1]}));
rejects('inject selected answer argument',()=>prepareRegion({target:[3,3,0],color:0}));
// Formal input is the COMPLETE retained context, not a hash or point label.
const names=data.rows.map((_,i)=>'r'+String(i).padStart(3,'0'));
const template=readFileSync(new URL('../agda/RamseyRegionFamily.agda.in',import.meta.url),'utf8');
const text=template.replace('@@INDICES@@',names.map(n=>'  '+n+' : RegionIndex').join('\n'))
 .replace('@@CONTEXTS@@',data.rows.map((row,i)=>'context '+names[i]+' = '+JSON.stringify(JSON.stringify(canonical(row)))).join('\n'));
writeFileSync(new URL('../agda/RamseyRegionFamily.agda',import.meta.url),text);
mkdirSync(new URL('../fixtures/ramsey-native-region-family',import.meta.url),{recursive:true});
writeFileSync(new URL('../fixtures/ramsey-native-region-family/RamseyRegionFamilyWrongPremise.agda',import.meta.url),`{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyRegionFamilyWrongPremise where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero)
open import RamseyRegionFamily
module X = UnderInput (λ _ → zero)
bad : X.R.Resolve (N.Pi-package RegionIndex X.fiber)
bad = X.R.apply (N.P-kind , RegionIndex , X.fiber) (λ { (lift i) → X.seed-at r000 })
`);
mkdirSync(new URL('../results',import.meta.url),{recursive:true});
const output={...data,sourceControls:controls,nativeLiteralContextStrings:171,preparedMPlanes:[...planes].sort((a,b)=>a-b),
 sourceRuleBinding:'NativeTableRules P-kind and E-kind, NativeTableResolution.Full',
 suppliedIndexOnly:true,wordDerivedIndexConstructed:false,simultaneousAssemblyAdmitted:false,
 physicalPreparedPolicyDerived:false,rootResolved:false};
writeFileSync(new URL('../results/ramsey-native-region-family-input-v1.json',import.meta.url),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({preparedContexts:171,planes:7,sourceControls:controls.length,nativeModuleGenerated:true,jointAssemblyReason:data.attemptedJointAssembly.reason}));
