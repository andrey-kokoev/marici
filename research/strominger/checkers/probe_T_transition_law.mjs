// Test direct coordinate-cycle and chart-dependent lifts against native maps.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const file='research/strominger/results/T-metric-gluing/verification.json',bytes=await readFile(file),metricData=JSON.parse(bytes),labels=['a','b','u','v','c'],I=[0,1,2,3,4],PN=[3,1,2,0,4],NE=[0,4,2,3,1],compose=(a,b)=>b.map(i=>a[i]),inv=p=>p.map((_,i)=>p.indexOf(i)),eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const cycle={a:'b',b:'c',c:'a',u:'u',v:'v'},facets={P:['u','v','a','b'],N:['u','v','b','c'],E:['u','v','c','a']};
// Push point coordinates with the vertex cycle. Pullback permutation uses
// inverse vertex image because target coordinate at v comes from cycle^-1(v).
const Q=labels.map(x=>labels.findIndex(y=>cycle[y]===x));assert.deepEqual(compose(compose(Q,Q),Q),I);assert.ok(!eq(Q,I));
assert.ok(!eq(Q,PN));assert.ok(!eq(Q,NE));
const EP=inv(compose(PN,NE)),F={P:I,N:PN,E:compose(PN,NE)},native={PN,NE,EP};
const arrow=(from,to)=>compose(inv(F[from]),F[to]);assert.deepEqual(arrow('P','N'),PN);assert.deepEqual(arrow('N','E'),NE);assert.deepEqual(arrow('E','P'),EP);
let triangles=0;for(const a of ['P','N','E'])for(const b of ['P','N','E'])for(const c of ['P','N','E']){assert.deepEqual(compose(arrow(a,b),arrow(b,c)),arrow(a,c));triangles++;}
// Can one common change of five-slot basis turn a 3-cycle into either native
// map? Their orders differ (3 vs 2), an invariant under conjugation.
function order(p){let x=I;for(let n=1;n<=120;n++){x=compose(x,p);if(eq(x,I))return n;}throw Error('No finite order');}
assert.equal(order(Q),3);assert.equal(order(PN),2);assert.equal(order(NE),2);
const transitionMetricTests=metricData.rows.map(row=>{assert.ok(row.metricCompatible);const d=(a,b)=>a===b?0:row.metric[[a,b].sort().join('|')],perFacet={};for(const [s,vs] of Object.entries(facets)){const changes=[];for(let i=0;i<vs.length;i++)for(let j=i+1;j<vs.length;j++){const a=vs[i],b=vs[j],old=d(a,b),next=d(cycle[a],cycle[b]);if(old!==next)changes.push({edge:[a,b],before:old,after:next});}perFacet[s]={isometric:changes.length===0,changedEdges:changes};}return {marking:row.marking,perFacet};});
const role={a:['C0','M2'],b:['M0'],c:['C2'],u:['C1'],v:['M1']};assert.equal(role.a.length,2);
const source='research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',sourceBytes=await readFile(source);
const out='research/strominger/results/T-transition-law';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'coordinate-cycle-and-native-transport-separated',coefficientSlotOrder:labels,coordinateCycle:Q,orders:{coordinateCycle:order(Q),PN:order(PN),NE:order(NE),EP:order(EP)},oneCommonBasisConjugationPossible:false,chartFrames:F,chartDependentTransitions:native,coherenceTrianglesPassed:triangles,transitionMetricTests,seamOccurrenceLabels:role.a,sourceHashes:{[file]:createHash('sha256').update(bytes).digest('hex'),[source]:createHash('sha256').update(sourceBytes).digest('hex')},checkerSha256:createHash('sha256').update(await readFile(new URL('./probe_T_transition_law.mjs',import.meta.url))).digest('hex'),scope:'Tested direct action of a->b->c->a on the five geometric labels versus native five-coefficient permutations. The two are different representations. A flat chart-dependent coefficient transport is constructed from existing PN/NE plus inferred inverse-composite EP; its coherence follows from that choice. This does not derive coordinate naming a=R,b=M,c=C, an occurrence-period identification C0~M2 or a physical E-outgoing law. Metrics retained and tested rather than symmetrized. Production/viewer unchanged.'},null,2)+'\n');console.log(JSON.stringify({coordinateCycle:Q,orders:{coordinate:order(Q),PN:order(PN),NE:order(NE)},chartFrames:F,triangles,metricIsometries:Object.fromEntries(['P','N','E'].map(s=>[s,transitionMetricTests.filter(r=>r.perFacet[s].isometric).length]))},null,2));
