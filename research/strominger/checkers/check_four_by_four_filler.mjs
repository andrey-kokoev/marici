import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {makeFourByFourFiller,decomposeFillerSlots,fillerEndpointReadout,fillerChannels} from '../four-by-four-filler-model.mjs';
import {makeSevenContextFourDepth} from '../seven-context-four-depth-model.mjs';
import {buildFoldedFibration} from '../../realization-tower/fibration-folded-process.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;};
function rank(rows){
 if(!rows.length)return 0;const a=rows.map(r=>r.map(BigInt));let at=0;
 for(let col=0;col<a[0].length&&at<a.length;col++){
  let pivot=at;while(pivot<a.length&&!a[pivot][col])pivot++;if(pivot===a.length)continue;[a[at],a[pivot]]=[a[pivot],a[at]];
  for(let i=at+1;i<a.length;i++)if(a[i][col]){const p=a[at][col],q=a[i][col];for(let j=col;j<a[0].length;j++)a[i][j]=p*a[i][j]-q*a[at][j];const d=a[i].slice(col).reduce(gcd,0n);if(d>1n)for(let j=col;j<a[0].length;j++)a[i][j]/=d;}
  at++;
 }
 return at;
}
const checks=[];function check(name,f){f();checks.push(name);}
const filler=makeFourByFourFiller(),B=filler.boundaryRows;
const zero={P:0,E:0};
check('the free 4x4 slot bank has two independent endpoint readings and fourteen residual directions',()=>{
 assert.equal(filler.slots.length,16);assert.equal(rank(B),2);assert.equal(filler.residualBasis.length,14);
 assert.equal(rank(filler.residualBasis.map(b=>b.vector)),14);
 for(const b of filler.residualBasis)assert.deepEqual(fillerEndpointReadout(b.vector),zero);
 assert.equal(rank([filler.collective.P,filler.collective.E,...filler.residualBasis.map(b=>b.vector)]),16);
});
check('collective plus residual decomposition exactly recovers every free slot basis vector',()=>{
 for(let i=0;i<16;i++){
  const v=Array.from({length:16},(_,j)=>Number(i===j)),d=decomposeFillerSlots(v);
  assert.deepEqual(d.collective.map((x,j)=>x+d.residual[j]),v);
  assert.deepEqual(fillerEndpointReadout(d.residual),zero);
  assert.deepEqual(decomposeFillerSlots(d.collective).collective,d.collective);
 }
});
const existingN=filler.slots.filter(s=>s.role==='neutron'),chargedRows=filler.slots.filter(s=>s.role!=='neutron').map(s=>filler.slots.map(t=>Number(s.index===t.index)));
const alreadyNeutralDimension=16-rank([...B,...chargedRows]);
check('fourteen boundary-invisible directions are not all supported on the native N-labelled channels',()=>{
 assert.equal(existingN.length,8);assert.equal(alreadyNeutralDimension,8);
 assert.equal(filler.residualBasis.filter(b=>b.kind==='P-history-contrast').length,3);
 assert.equal(filler.residualBasis.filter(b=>b.kind==='E-history-contrast').length,3);
 const counterexample=filler.residualBasis.find(b=>b.kind==='P-history-contrast');
 assert.deepEqual(fillerEndpointReadout(counterexample.vector),zero);
 assert.ok(counterexample.vector.some((x,i)=>x!==0&&filler.slots[i].role==='proton'));
});
check('role polarity preserves the residual space but exchanges rather than neutralizes charged contrasts',()=>{
 const flip=v=>filler.slots.map(s=>v[(s.depth-1)*4+(3-fillerChannels.indexOf(s.channel))]);
 assert.deepEqual(flip(filler.collective.P),filler.collective.E);
 for(const b of filler.residualBasis){assert.deepEqual(fillerEndpointReadout(flip(b.vector)),zero);assert.deepEqual(flip(flip(b.vector)),b.vector);}
 const p=filler.residualBasis.find(b=>b.kind==='P-history-contrast'),e=flip(p.vector);
 assert.ok(e.every((x,i)=>x===0||filler.slots[i].role==='electron'));
});
const Q4=filler.collectiveChargeNumerator,apply=(matrix,v)=>matrix.map(row=>row.reduce((s,x,i)=>s+x*v[i],0));
check('a declared boundary-only charge operator realizes the full 1P + 1E + 14 neutral decomposition',()=>{
 assert.equal(rank(Q4),2);assert.deepEqual(apply(Q4,filler.collective.P),filler.collective.P.map(x=>4*x));
 assert.deepEqual(apply(Q4,filler.collective.E),filler.collective.E.map(x=>x===0?0:-4*x));
 for(const v of filler.residualBasis)assert.deepEqual(apply(Q4,v.vector),Array(16).fill(0));
 for(let i=0;i<16;i++)for(let j=0;j<16;j++)assert.equal(Q4[i][j],Q4[j][i]);
 const flip=v=>filler.slots.map(s=>v[(s.depth-1)*4+(3-fillerChannels.indexOf(s.channel))]);
 for(let i=0;i<16;i++){
  const v=Array.from({length:16},(_,j)=>Number(i===j));
  assert.deepEqual(apply(Q4,flip(v)),flip(apply(Q4,v)).map(x=>x===0?0:-x));
 }
});
// Actual source realization: one five-coefficient packet, replayed across the
// four retained depths. All full packets are used; no scalar readout is fitted.
const native=makeSevenContextFourDepth(),columns=[];
for(let i=0;i<5;i++){
 const value=Array.from({length:5},(_,j)=>[Number(i===j),0]),run=native.run(value);
 columns.push(run.banks.flatMap(bank=>fillerChannels.flatMap(channel=>bank[channel].coefficients.map(z=>z[0]))));
}
const realized=Array.from({length:80},(_,i)=>columns.map(c=>c[i]));
// Endpoint *sums*, scaled by 4 relative to means, keep this rank calculation integer-exact.
const endpoints=[0,3].flatMap(column=>Array.from({length:5},(_,coefficient)=>Array.from({length:5},(_,input)=>[0,1,2,3].reduce((s,depth)=>s+realized[(depth*4+column)*5+coefficient][input],0))));
const nativeRank=rank(realized),nativeBoundaryRank=rank(endpoints);
const chargedNative=Array.from({length:80},(_,row)=>Array.from({length:5},(_,input)=>Q4[Math.floor(row/5)].reduce((s,q,j)=>s+q*realized[j*5+row%5][input],0)));
const nativeChargeClosureRank=rank(realized.map((row,i)=>[...row,...chargedNative[i]]));
check('the proposed boundary charge does not preserve the old native replay subspace without extension',()=>{
 assert.ok(nativeChargeClosureRank>nativeRank);assert.equal(nativeChargeClosureRank,10);
});
check('native sixteen packet occurrences retain only the original five independent complex coefficients',()=>{
 assert.equal(realized.length,80);assert.equal(nativeRank,5);assert.equal(nativeBoundaryRank,5);
 assert.equal(nativeRank-nativeBoundaryRank,0);
 for(let depth=1;depth<4;depth++)for(const column of [0,3])for(let c=0;c<5;c++)assert.deepEqual(realized[(depth*4+column)*5+c],realized[column*5+c]);
});
check('all eight N packet slots share the same native coefficient state despite distinct depth/direction provenance',()=>{
 const n=realized.slice(5,10);
 for(let depth=0;depth<4;depth++)for(const column of [1,2])assert.deepEqual(realized.slice((depth*4+column)*5,(depth*4+column+1)*5),n);
 const run=native.run([[2,1],[3,-2],[5,3],[7,-4],[11,5]]);
 assert.deepEqual(run.states.map(s=>s.history.length),[0,2,4,6,8]);
 assert.equal(run.banks[0].ab.orientation,-run.banks[0].ba.orientation);
});
const tiling=buildFoldedFibration(),octahedra=tiling.geometry.filter(g=>g.kind==='octahedron'),I=octahedra.map((_,i)=>octahedra.map((__,j)=>Number(i===j)));
check('the two 56-site N sheets are still an identity-linked pair, not independent summands',()=>{
 assert.equal(octahedra.length,56);assert.ok(octahedra.every(g=>g.polarityRoles.positive==='neutron'&&g.polarityRoles.negative==='neutron'));
 assert.equal(rank([...I,...I]),56);
});
const sources=['research/strominger/four-by-four-filler-model.mjs','research/strominger/checkers/check_four_by_four_filler.mjs','research/strominger/seven-context-four-depth-model.mjs','research/strominger/single-pe-pair-model.mjs','research/strominger/paired-polarity-model.mjs','research/realization-tower/fibration-folded-process.mjs'];
const result={status:'passed',candidateStatus:'Free 1P+1E+14 boundary-neutral decomposition constructed under an explicit new charge law; independent native N filler modes remain unconstructed',checks,
 sourceSha256:Object.fromEntries(sources.map(p=>[p,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex')])),
 slotDefinition:'Four retained reversal depths times aa, ab, ba, bb. Not an arbitrary 16-particle initialization.',freeSlotSpace:{dimension:16,boundaryRank:rank(B),residualDimension:14,slots:filler.slots,boundaryRows:B,residualBasis:filler.residualBasis,
  decomposition:{collectiveP:1,collectiveE:1,NChannelDirections:8,PHistoryContrasts:3,EHistoryContrasts:3}},
 boundaryChargeCandidate:{numerator:Q4,denominator:4,rank:rank(Q4),neutralKernelDimension:16-rank(Q4),spectrum:{positive:1,negative:1,zero:14},polarityOdd:true,
  assumption:'Only the two collective boundary lines carry charge; all boundary-invisible contrasts are neutral. This changes the existing local role interpretation and does not create independent amplitudes.'},
 interpretation:'All fourteen residual directions are neutral under the declared boundary-only charge operator. Only eight already lie in the existing N-labelled channel subspace; the other six are reclassified by the new law, not by the old native transport.',
 nativeRealization:{packetOccurrences:16,complexCoefficientsPerPacket:5,storedComplexCoordinates:80,independentComplexCoefficients:nativeRank,endpointReadoutRank:nativeBoundaryRank,freeResidualCoordinatesWithEndpointsFixed:nativeRank-nativeBoundaryRank,spanWithBoundaryChargeImage:nativeChargeClosureRank,boundaryChargePreservesNativeSubspace:false},
 octahedralSheets:{geometricSites:56,displayedSheetOccurrences:112,independentScalarSiteCoordinates:rank([...I,...I])},
 next:'Supply an actual new filler state and typed boundary/transport maps if it is intended to add independent modes. Demonstrate neutrality of the six charged contrasts and independence from the existing N carrier; a count alone does not supply those maps.'};
fs.writeFileSync(path.join(root,'research/strominger/results/four-by-four-filler-v1.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,checks:checks.length,candidateStatus:result.candidateStatus,freeDecomposition:result.freeSlotSpace.decomposition,boundaryChargeSpectrum:result.boundaryChargeCandidate.spectrum,native:result.nativeRealization,octahedralSheets:result.octahedralSheets},null,2));
