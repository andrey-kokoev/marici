import assert from 'node:assert/strict';
import {writeFileSync} from 'node:fs';
import {GenerativeAssemblyRules} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {makeLatticeItem} from '../../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const mod2=x=>(x%2+2)%2,chi=v=>{const p=v.split(',').map(Number);return mod2(p[0]+p[2]);};
const failures=c=>Object.entries(c.aliases).filter(([name,v])=>chi(v)!==(name[0]==='C'?1:0));
const normalize=(v,shift)=>v.split(',').map((x,i)=>Number(x)-shift[i]).join(',');
const canonical=x=>Array.isArray(x)?x.map(canonical):x&&typeof x==='object'?Object.fromEntries(Object.keys(x).sort().map(k=>[k,canonical(x[k])])):x;
const key=x=>JSON.stringify(canonical(x));
const shapes=[{kind:'tetrahedron',inverted:false,component:0,sum:0},{kind:'tetrahedron',inverted:true,component:0,sum:2},...Array.from({length:4},(_,component)=>({kind:'octahedron',inverted:false,component,sum:-1}))];
function run(shape,origin,perm,shift=[0,0,0,0],phase=0){
 const r=new GenerativeAssemblyRules(),owner=makeLatticeItem(shape.kind,origin.map((x,i)=>x+shift[i]),shape.inverted);
 const cell=r.geometry.register(owner,owner.components[shape.component]);
 const vertices=r.geometry.cells[cell].vertices;
 const names=shape.kind==='tetrahedron'?['C0','M0','C1','M1']:['M0','C1','M1','C2'];
 const aliases=Object.fromEntries(names.map((n,i)=>[n,vertices[perm[i]]]));
 if(failures({aliases}).length)return {status:'active-invariant-absent'};
 const chart=shape.kind==='tetrahedron'?r.completeP(cell,aliases):r.completeN(cell,aliases);
 if(chart===null)return {status:'not-native-completable'};
 const source=r.charts[chart];if(failures(source).length)return {status:'full-invariant-absent'};
 const id=r.packet(chart,phase,[0,1,2,3,4]);const targets=[];
 for(const n of r.outgoing(id)){
  const op=r.operations[n];assert.equal(r.validateTransfer(op),true);
  const target=r.charts[r.packets[op.target].chart],bad=failures(target);
  assert.equal(bad.length,0,key({shape,origin,perm,shift,phase,op,source,target,bad}));
  targets.push({kind:op.kind,phaseDelta:op.phaseDelta,species:target.species,
   aliases:Object.fromEntries(Object.entries(target.aliases).map(([n,v])=>[n,normalize(v,shift)])),
   face:op.face?.map(v=>normalize(v,shift))??null});
 }
 return {status:'checked',sourceSpecies:source.species,targets};
}
const records=[],totals={},kinds={};let geometricParityForms=0,markings=0,translationControls=0,phaseControls=0;
for(const shape of shapes)for(let mask=0;mask<16;mask++){
 const bits=Array.from({length:4},(_,i)=>(mask>>i)&1);if(mod2(bits.reduce((a,b)=>a+b,0))!==mod2(shape.sum))continue;
 geometricParityForms++;const origin=[...bits];origin[3]+=shape.sum-origin.reduce((a,b)=>a+b,0);
 for(const perm of permutations([0,1,2,3])){
  markings++;const result=run(shape,origin,perm);totals[result.status]=(totals[result.status]??0)+1;
  if(result.status!=='checked')continue;
  for(const target of result.targets)kinds[target.kind]=(kinds[target.kind]??0)+1;
  for(let i=0;i<3;i++){const shift=[0,0,0,0];shift[i]=2;shift[3]=-2;assert.equal(key(run(shape,origin,perm,shift)),key(result));translationControls++;}
  for(const phase of [1,5]){assert.equal(key(run(shape,origin,perm,[0,0,0,0],phase)),key(result));phaseControls++;}
  records.push({shape,origin,permutation:perm,...result});
 }
}
assert.equal(geometricParityForms,48);assert.equal(markings,1152);assert(records.length>0);
for(const kind of ['PN','inverse-PN','NE','reader-phase-advance','NN-phase-advance'])assert(kinds[kind]>0,'uncovered rule '+kind);
const base=new GenerativeAssemblyRules();assert.equal(failures(base.charts[base.packets[base.root].chart]).length,0);
const a=base.charts[base.packets[base.root].chart].aliases;
const complement=new GenerativeAssemblyRules({seedBindings:{C0:a.M0,M0:a.C0,C1:a.M1,M1:a.C1}});
const bad=failures(complement.charts[complement.packets[complement.root].chart]);assert(bad.length>=4);
const out={status:'passed',geometricParityForms,markings,totals,ruleKindCoverage:kinds,translationControls,phaseControls,
 defaultSeedSatisfiesInvariant:true,complementarySeedViolations:bad,records,
 finiteDepthSearchUsedAsProof:false,allOriginConclusionRequiresTranslationAndPhaseIndependenceArgument:true,
 javascriptSemanticsKernelVerified:false,parentDescentResolved:false};
writeFileSync(new URL('../results/ramsey-role-parity-invariant-runtime-v1.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({...out,records:undefined},null,2));
