// Structural mode test; no Pb-208 target counts are generator inputs.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {buildFoldedFibration} from '../../realization-tower/fibration-folded-process.mjs';
import {pairedPolarityProbe} from '../paired-polarity-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
function rank(rows){
 if(!rows.length)return 0;const a=rows.map(r=>r.map(BigInt)),n=a[0].length;let at=0;
 for(let col=0;col<n&&at<a.length;col++){
  let pivot=at;while(pivot<a.length&&a[pivot][col]===0n)pivot++;if(pivot===a.length)continue;
  [a[at],a[pivot]]=[a[pivot],a[at]];
  for(let i=at+1;i<a.length;i++)if(a[i][col]!==0n){
   const p=a[at][col],q=a[i][col];for(let j=col;j<n;j++)a[i][j]=p*a[i][j]-q*a[at][j];
   const d=a[i].slice(col).reduce(gcd,0n);if(d>1n)for(let j=col;j<n;j++)a[i][j]/=d;
  }
  at++;
 }
 return at;
}
const checks=[];function check(name,f){f();checks.push(name);}
check('exact rank handles dependence and a non-unit pivot',()=>{assert.equal(rank([[2,4],[3,6]]),1);assert.equal(rank([[2,1],[1,2]]),2);assert.equal(rank([[0,0]]),0);});
const tiling=buildFoldedFibration(),faces=new Map(),key=vs=>vs.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
const adjacency=new Map(tiling.geometry.map(g=>[g.id,new Set()]));
for(const g of tiling.geometry)for(const f of g.faces){const k=key(f);if(!faces.has(k))faces.set(k,[]);faces.get(k).push(g.id);}
for(const owners of faces.values())if(owners.length===2){adjacency.get(owners[0]).add(owners[1]);adjacency.get(owners[1]).add(owners[0]);}
const P=tiling.geometry.filter(g=>g.role==='proton'),N=tiling.geometry.filter(g=>g.role==='neutron'),E=tiling.geometry.filter(g=>g.role==='electron');
// Compare two minority sites when they meet the same actual neutral cell.
// Equality along these links is a candidate coherence law, not an installed
// native dynamics. Its kernel is independent of positive edge-weight choices.
const links=new Map(),majorityLinks=new Map();let mediatedPaths=0;const mediators=[];
for(const n of N){
 const es=E.filter(e=>adjacency.get(n.id).has(e.id)),ps=P.filter(p=>adjacency.get(n.id).has(p.id));
 if(es.length&&ps.length)mediators.push(n.id);mediatedPaths+=es.length*ps.length;
 for(let i=0;i<ps.length;i++)for(let j=i+1;j<ps.length;j++){const endpoints=[ps[i].id,ps[j].id].sort();majorityLinks.set(endpoints.join('|'),endpoints);}
 for(let i=0;i<es.length;i++)for(let j=i+1;j<es.length;j++){
  const endpoints=[es[i].id,es[j].id].sort(),k=endpoints.join('|');if(!links.has(k))links.set(k,{endpoints,witnesses:[]});links.get(k).witnesses.push(n.id);
 }
}
const graph=new Map(E.map(e=>[e.id,new Set()]));for(const {endpoints:[a,b]}of links.values()){graph.get(a).add(b);graph.get(b).add(a);}
const seen=new Set(),components=[];
for(const e of E)if(!seen.has(e.id)){const q=[e.id];seen.add(e.id);for(let i=0;i<q.length;i++)for(const v of graph.get(q[i]))if(!seen.has(v)){seen.add(v);q.push(v);}components.push(q);}
const index=new Map(E.map((e,i)=>[e.id,i]));
const D=[...links.values()].map(({endpoints:[a,b]})=>E.map((_,i)=>Number(i===index.get(a))-Number(i===index.get(b))));
const L=E.map((_,i)=>E.map((_,j)=>D.reduce((s,r)=>s+r[i]*r[j],0)));
const differenceRank=rank(D),laplacianRank=rank(L);
check('actual neutral-mediated minority graph has one collective zero mode',()=>{
 assert.equal(components.length,1);assert.equal(differenceRank,E.length-1);assert.equal(laplacianRank,differenceRank);
 for(const row of D)assert.equal(row.reduce((a,b)=>a+b,0),0);
 for(const row of L)assert.equal(row.reduce((a,b)=>a+b,0),0);
});
check('positive reweighting of the link comparisons does not change the collective kernel',()=>{
 assert.equal(rank(D.map((row,i)=>row.map(x=>x*(i+1)))),differenceRank);
});
check('collective observation plus retained contrasts recovers every original site exactly',()=>{
 // Integer representation avoids rational roundoff: retain sum and xi-x0.
 for(let basis=0;basis<E.length;basis++){
  const x=E.map((_,i)=>Number(i===basis)),sum=x.reduce((a,b)=>a+b,0),contrasts=x.slice(1).map(v=>v-x[0]);
  const x0=(sum-contrasts.reduce((a,b)=>a+b,0))/E.length;
  assert.deepEqual([x0,...contrasts.map(d=>x0+d)],x);
 }
});
check('generic minority states do not already obey the consensus law',()=>{
 const x=E.map((_,i)=>i);assert.ok(D.some(row=>row.reduce((s,v,i)=>s+v*x[i],0)!==0));
 const a=E.map(()=>0),b=E.map((_,i)=>i===0?1:i===1?-1:0);
 assert.equal(a.reduce((s,x)=>s+x,0),b.reduce((s,x)=>s+x,0));assert.notDeepEqual(a,b);
});
// A concrete, declared comparison update, not merely a zero-mode count:
// T = I - L/q, q > 2*maximum degree. It conserves the mean and contracts
// contrasts, while remaining invertible at every finite number of steps.
const maxDegree=Math.max(...L.map((row,i)=>row[i])),denominator=2*maxDegree+1;
const numerator=L.map((row,i)=>row.map((x,j)=>Number(i===j)*denominator-x));
const stepRank=rank(numerator),mean=x=>x.reduce((s,v)=>s+v,0)/x.length;
const variance=x=>{const m=mean(x);return x.reduce((s,v)=>s+(v-m)**2,0);};
let probe=E.map((_,i)=>i),varianceTrace=[variance(probe)];
check('candidate local comparison update conserves the mean, contracts contrasts and has full finite-step rank',()=>{
 assert.equal(stepRank,E.length);
 for(let i=0;i<E.length;i++){
  assert.ok(numerator[i].every(x=>x>=0));assert.equal(numerator[i].reduce((s,x)=>s+x,0),denominator);
  assert.equal(numerator.reduce((s,row)=>s+row[i],0),denominator);
 }
 const originalMean=mean(probe);
 for(let k=0;k<28;k++){
  probe=numerator.map(row=>row.reduce((s,v,i)=>s+v*probe[i],0)/denominator);
  assert.ok(Math.abs(mean(probe)-originalMean)<1e-10);
  const v=variance(probe);assert.ok(v<varianceTrace.at(-1));varianceTrace.push(v);
 }
 assert.ok(varianceTrace.at(-1)>0);
});
const A_P=P.map(p=>N.map(n=>Number(adjacency.get(p.id).has(n.id)))),A_E=E.map(e=>N.map(n=>Number(adjacency.get(e.id).has(n.id))));
const B=P.map((_,i)=>E.map((_,j)=>N.reduce((s,__,k)=>s+A_P[i][k]*A_E[j][k],0)));
const ranks={P_from_N:rank(A_P),E_from_N:rank(A_E),joint_charged_from_N:rank([...A_P,...A_E]),P_E_mediation:rank(B)};
const I=N.map((_,i)=>N.map((__,j)=>Number(i===j))),stackedRank=rank([...I,...I]);
check('retained N polarity copies add no independent scalar site coordinates',()=>{
 assert.equal(stackedRank,N.length);
 const probe=pairedPolarityProbe();assert.deepEqual(probe.ab.positive.coefficients,probe.ab.negative.coefficients);
 assert.equal(probe.ab.positive.interfaceFlow,-probe.ab.negative.interfaceFlow);
});
check('minus-sheet minority P sites are the same geometric carrier as plus-sheet minority E sites',()=>{
 assert.deepEqual(tiling.geometry.filter(g=>g.polarityRoles.negative==='proton').map(g=>g.id),E.map(g=>g.id));
});
const exposed=new Set(tiling.outer.flatMap(f=>f.owners));
const pInterior=P.map((p,i)=>exposed.has(p.id)?null:i).filter(i=>i!==null),eInterior=E.map((e,i)=>exposed.has(e.id)?null:i).filter(i=>i!==null);
const pIndex=new Map(P.map((p,i)=>[p.id,i]));
const D_P=[...majorityLinks.values()].map(([a,b])=>P.map((_,i)=>Number(i===pIndex.get(a))-Number(i===pIndex.get(b))));
const L_P=P.map((_,i)=>P.map((_,j)=>D_P.reduce((s,r)=>s+r[i]*r[j],0)));
const majorityConsensusRank=rank(D_P),eDirichletRank=rank(eInterior.map(i=>eInterior.map(j=>L[i][j]))),pDirichletRank=rank(pInterior.map(i=>pInterior.map(j=>L_P[i][j])));
check('boundary geometry independently singles out one minority port and ten interior majority sites',()=>{
 assert.equal(E.length-eInterior.length,1);assert.equal(pInterior.length,10);
 assert.equal(eDirichletRank,eInterior.length);assert.equal(pDirichletRank,pInterior.length);
 // Constant extension solves the unforced interior equations, so the one
 // minority boundary value uniquely fixes its harmonic extension.
 for(const i of eInterior)assert.equal(L[i].reduce((s,x)=>s+x,0),0);
});
check('the same unconstrained consensus rule would collapse the majority sector too',()=>assert.equal(majorityConsensusRank,P.length-1));
const sourcePaths=['research/realization-tower/fibration-folded-process.mjs','research/strominger/paired-polarity-model.mjs','research/strominger/checkers/check_collective_pair_modes.mjs'];
const result={status:'passed',checks,scope:'Exact scalar site-incidence probe of the existing geometry, not a derived Hamiltonian or full native particle-state space.',
 sourceSha256:Object.fromEntries(sourcePaths.map(p=>[p,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex')])),
 siteCounts:{P:P.length,N:N.length,E:E.length},minorityCollective:{sites:E.map(e=>e.id),links:[...links.values()],componentSizes:components.map(c=>c.length),differenceRank,laplacianRank,kernelDimension:E.length-laplacianRank,
  observation:'mean = sum(x)/siteCount; one collective observable',retainedInternalCoordinates:E.length-1,
  proposedConstraint:'Equality of minority-site values across every shared-N comparison link, D x = 0',
  established:'One constant zero mode exists. Generic input retains all site coordinates; consensus is not yet a source-derived evolution.'},
 neutronIndependence:{displayedOccurrences:2*N.length,independentSiteCoordinates:stackedRank,extraIndependentCoordinates:stackedRank-N.length,reason:'Opposite N sheet reverses flow but retains the same coefficient state.'},
 interfaceProbe:{distinctNeutralMediators:mediators.length,mediatedTwoLegPaths:mediatedPaths,ranks,
  neutralInvisibleToP:N.length-ranks.P_from_N,neutralInvisibleToE:N.length-ranks.E_from_N,neutralInvisibleToJoint:N.length-ranks.joint_charged_from_N,
  scope:'Unweighted whole-face incidence and its P-N-E composition. Other physically supplied operators could have different spectra; these are not universal particle-mode counts.'},
 candidateDynamics:{rule:'T = I - L/(2*maximumDegree+1)',maximumDegree:maxDegree,denominator,finiteStepRank:stepRank,probeVarianceByStep:varianceTrace,
  scope:'Declared positive-weight local comparison law. Its constant limit follows from graph connectivity, but no native dynamics selects this law. Full finite-step rank means 14 or 28 repetitions do not exactly collapse the minority sector.'},
 boundaryProbe:{minority:{boundary:E.length-eInterior.length,interior:eInterior.length,interiorDirichletRank:eDirichletRank},majority:{boundary:P.length-pInterior.length,interior:pInterior.length,interiorDirichletRank:pDirichletRank},
  tenInteriorSites:pInterior.map(i=>P[i].id),
  interpretation:'Ten is the kernel dimension of majority boundary restriction, not ten additional N modes. Those sites already belong to the 81 charged readings. With a declared unforced harmonic comparison law, the minority sector has a unique extension from its single boundary value.',
  selectivityControl:{majorityConsensusKernel:P.length-majorityConsensusRank,note:'Uniform consensus also leaves only one majority mode. Keeping all 81 while collapsing only 36 requires a selective boundary/dynamics justification.'}},
 conditionalObservableDimension:P.length+(E.length-laplacianRank),retainedChargedSiteCoordinates:P.length+E.length,
 conclusion:'A natural candidate supports one collective mode for the minority sector, with contrasts retained. Ten interior majority P/E sites are geometrically present, but neither independent doubling of N nor their promotion to ten additional independent N modes has been established. The effective carrier is reused by the opposite sheet, not doubled into independent P/E particles.'};
const out=path.join(root,'research/strominger/results/collective-pair-modes-v1.json');fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,checks:checks.length,sites:result.siteCounts,minority:{links:links.size,components:components.map(c=>c.length),rank:differenceRank,zeroModes:E.length-laplacianRank},neutron:result.neutronIndependence,interface:result.interfaceProbe,boundary:result.boundaryProbe,conditionalObservableDimension:result.conditionalObservableDimension,retainedChargedSiteCoordinates:result.retainedChargedSiteCoordinates,candidateDynamics:{denominator,finiteStepRank:stepRank,varianceAfter28:varianceTrace.at(-1)}},null,2));
