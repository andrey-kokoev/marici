import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
const source='research/nima/agda/ActualSeedEndpointTable.agda';
const free='research/nima/agda/SeedSeamPathComparisonBoundary.agda';
const candidate='research/strominger/agda/DependentFourReturn.agda';
const text=await fs.readFile(source,'utf8');
const from=Object.fromEntries([...text.matchAll(/^source (\w+) = (\w+)\r?$/gm)].map(m=>[m[1],m[2]]));
const to=Object.fromEntries([...text.matchAll(/^target (\w+) = (\w+)\r?$/gm)].map(m=>[m[1],m[2]]));
assert.deepEqual(Object.keys(from).sort(),['AB','AD','BA','BC','CA','DB']);
const vertices=[...new Set(Object.values(from))].sort();assert.deepEqual(vertices,['A','B','C','D']);
function run(start,word){let at=start;for(const e of word){assert.equal(from[e],at);at=to[e];}return at;}
const closed=[];
function enumerate(start,at,word){if(word.length===4){if(at===start)closed.push({start,word});return;}
 for(const e of Object.keys(from))if(from[e]===at)enumerate(start,to[e],[...word,e]);}
for(const v of vertices)enumerate(v,v,[]);
assert.equal(closed.length,6);
const rotations=w=>w.map((_,i)=>[...w.slice(i),...w.slice(0,i)]);
const orbitKey=w=>rotations(w).map(x=>x.join(',')).sort()[0];
const orbitSizes=Object.values(Object.groupBy(closed,h=>orbitKey(h.word))).map(g=>g.length).sort();assert.deepEqual(orbitSizes,[2,4]);
const word=['AD','DB','BC','CA'];assert.equal(run('A',word),'A');
const shifts=rotations(word).map(w=>({start:from[w[0]],word:w,end:run(from[w[0]],w)}));
assert(shifts.every(x=>x.start===x.end));
// Executing the selected source occurrences appends; comparing the active
// endpoint does not identify or erase any executed occurrence.
const prefix=['AB','BA'],retained=[...prefix,...word];assert.equal(run('A',prefix),'A');assert.equal(run('A',retained),'A');
assert.deepEqual(retained.slice(0,prefix.length),prefix);assert.equal(retained.length,prefix.length+4);assert.notDeepEqual(retained,prefix);
const circle=[];for(let k=-9;k<=9;k++){const raw=16*k,transported=-16*k+raw+k;assert.equal(transported,k);circle.push({initial:k,raw,transported});}
assert.equal(circle.filter(x=>x.initial!==x.raw).length,18);
const mod=x=>((x%5)+5)%5;
const mul=([a,b],[c,d])=>[mod(a+(b?-c:c)),b^d],inv=([a,b])=>[mod(b?a:-a),b];
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
const G=p=>mul(mul([1,0],p),[4,0]);
const d5=[];for(let b=0;b<2;b++)for(let a=0;a<5;a++){
 const p=[a,b];let raw=p;for(let i=0;i<4;i++)raw=G(raw);
 const transported=mul(mul(inv(raw),raw),p);assert.deepEqual(transported,p);d5.push({initial:p,raw,transported});
}
assert.equal(d5.filter(x=>!eq(x.initial,x.raw)).length,5);
assert(!eq(mul([1,0],[0,1]),mul([0,1],[1,0])));
assert.equal((3+1+2+2)%5,3);assert.notEqual((1+2+2+3)%5,1);
assert.throws(()=>run('A',['AD','BC','DB','CA']));
const agdaReceipt='research/strominger/results/dependent-four-return-v1/agda.json';
const wrapper='research/strominger/checkers/check_dependent_four_return_agda.ps1';
const agda=JSON.parse((await fs.readFile(agdaReceipt,'utf8')).replace(/^\uFEFF/,''));
const digest=async p=>createHash('sha256').update(await fs.readFile(p)).digest('hex');
assert.equal(agda.passed,true);assert.equal(agda.compiler_exit_code,0);
assert.equal(agda.ignore_interfaces,true);assert.equal(agda.inputs_stable_during_check,true);
assert.equal(await digest(candidate),agda.source_sha256);
assert.equal(await digest(wrapper),agda.source_inventory.checker);
for(const p of [source,free])assert.equal(await digest(p),agda.source_inventory.imported_owner[p.split('/').at(-1)]);
const self='research/strominger/checkers/check_dependent_four_return.mjs',sourceHashes={};
for(const p of [source,free,candidate,self,wrapper,agdaReceipt])sourceHashes[p]=await digest(p);
const result={schema:'strominger.dependent-four-return.v1',passed:true,
 obligation:'route/coherencer compatibility: dependent identity-path return, kept separate from free directed histories',
 rootedFourArrowHistories:closed,cyclicOrbitSizes:orbitSizes,selectedCycle:{word,shifts,selectionIsAdditionalData:true},
 retainedHistory:{prefix,result:retained,activeReferenceReturned:true,fullRecordReturned:false},circle,d5,
 independentProductCounterexample:{factors:[3,1,2,2],sumMod5:3,rotatedFirst:1},
 agda:{candidate,typechecked:true,receipt:agdaReceipt,compiler:agda.compiler_version,
 verification:'Fresh safe Cubical closure via operator-authorized adapted PowerShell wrapper; stable included-source inventories.',
 theorem:'For every type S and G:S→S, shift^4 on Σ a, G^4(a)≡a is homotopic to identity, without isSet.',
 proofMethod:'Explicit cubical dependent square and its first shift-equivariance law via relative hcomp naturality, with source-selected four-arrow seed fixture and non-erasure lemma.',
 firstHigherEquivariance:'cong shift (shift-four x) ≡ shift-four (shift x)' },
 residuals:['Full higher-coherent C4 action not established beyond the first equivariance square','No source-canonical successor selection','No directed-occurrence-to-identity-path conversion','No edge-five payload return operator or period-four closure supplied'],sourceHashes};
await fs.mkdir('research/strominger/results/dependent-four-return-v1',{recursive:true});
await fs.writeFile('research/strominger/results/dependent-four-return-v1/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,histories:closed.length,orbitSizes,circleChecks:circle.length,d5Checks:d5.length,agda:result.agda,residuals:result.residuals},null,2));
