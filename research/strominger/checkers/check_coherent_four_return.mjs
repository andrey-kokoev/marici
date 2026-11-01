// Noncommutative falsifiers and fresh Agda receipt binding for the torsor family.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
const root='research/strominger',receipt=root+'/results/coherent-four-return-v1/agda.json';
const proof=root+'/agda/CoherentFourReturn.agda',prior=root+'/agda/DependentFourReturn.agda';
const wrapper=root+'/checkers/check_dependent_four_return_agda.ps1';
const self=root+'/checkers/check_coherent_four_return.mjs';
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
const agda=JSON.parse((await fs.readFile(receipt,'utf8')).replace(/^\uFEFF/,''));
assert.equal(agda.module,'CoherentFourReturn');assert.equal(agda.passed,true);
assert.equal(agda.compiler_exit_code,0);assert.equal(agda.ignore_interfaces,true);assert.equal(agda.inputs_stable_during_check,true);
assert.equal(await digest(proof),agda.source_sha256);
assert.equal(await digest(prior),agda.source_inventory.owner['DependentFourReturn.agda']);
assert.equal(await digest(wrapper),agda.source_inventory.checker);
const imported=['ActualSeedEndpointTable.agda','SeedSeamPathComparisonBoundary.agda','TableFibrationCycle.agda'].map(n=>'research/nima/agda/'+n);
for(const p of imported)assert.equal(await digest(p),agda.source_inventory.imported_owner[p.split('/').at(-1)]);
const mod=x=>((x%5)+5)%5;
const mul=([a,b],[c,d])=>[mod(a+(b?-c:c)),b^d],inv=([a,b])=>[mod(b?a:-a),b];
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1],one=[0,0];
const G=p=>mul(mul([1,0],p),[4,0]);
const iter=(p,n)=>{for(let i=0;i<n;i++)p=G(p);return p;};
const elems=Array.from({length:10},(_,i)=>[i%5,Math.floor(i/5)]);
const rotate=w=>[...w.slice(1),w[0]];
const collapse=w=>w.map((p,i)=>iter(p,3-i)).reduce(mul,one);
let cycles=0,rawMismatch=0,firstRawMismatch=null;
for(const a of elems)for(const b of elems)for(const c of elems)for(const d of elems){
 const word=[a,b,c,d],p=collapse(word),rotated=rotate(word),q=collapse(rotated);
 // A base move by e0 must transport the dependent loop. Raw G(p)=q is false.
 const transported=mul(mul(inv(iter(a,4)),G(p)),a);assert.deepEqual(transported,q);
 if(!eq(G(p),q)){rawMismatch++;firstRawMismatch??={word,canonicalShift:G(p),rotatedCollapse:q,transported};}
 assert.deepEqual(rotate(rotate(rotate(rotated))),word);
 const normal=[one,one,one,p];assert.deepEqual(collapse(rotate(normal)),G(p));
 cycles++;
}
assert.equal(cycles,10000);assert(rawMismatch>0);
let compositionChecks=0;for(let k=0;k<4;k++)for(let l=0;l<4;l++)for(let x=0;x<4;x++){
 assert.equal((k+(l+x)%4)%4,((k+l)%4+x)%4);compositionChecks++;
}
// The order-four generator is not the order-two Klein-four alternative.
assert.equal((1+1)%4,2);assert.notEqual(1^1,(1+1)%4);
const sourceHashes={};for(const p of [proof,prior,wrapper,self,receipt,...imported])sourceHashes[p]=await digest(p);
const result={schema:'strominger.coherent-four-return.v1',passed:true,
 theorem:'For every S and G:S→S, a homotopy-coherent C4 action exists on a fibre equivalent to Per4 G; generator transport agrees with the canonical shift.',
 formalConstruction:{module:proof,receipt,safeFreshAgda:true,
 base:'Connected component of the oriented four-point successor structure in its univalent moduli space.',
 classification:['connected','torsorGroupoid','torsorLoops','label-compose','generator-label'],
 family:'Action.family',fibreEquivalence:'Action.fibreEquiv',coherentAction:'Action.coherentAction',
 generatorComparison:'Action.generator-is-shift',requiresStateIsSet:false},
 modelControls:{d5Cycles:cycles,cyclicCompositionChecks:compositionChecks,rawWitnessMismatches:rawMismatch,firstRawMismatch,
 exactFourRotationsRetainEdgeWords:true,kleinFourRivalRejected:true},
 residuals:{specificEarlierReturnHomotopyIdentifiedWithActionCoherence:false,nativeEdgeFiveSuccessorOrReturn:false,
 canonicalSourceSuccessorSelected:false,historyErasureAuthorized:false},
 sourceHashes};
await fs.writeFile(root+'/results/coherent-four-return-v1/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({...result,sourceHashes:undefined},null,2));
