// Exhaust the translation quotient of source-generated local charts.
// A cap is a failure/open result, never evidence of closure.
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {makeLatticeItem} from '../../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
const names=['C0','M0','C1','M1','C2'],ID=[0,1,2,3,4];
const perms=a=>a.length?a.flatMap((v,i)=>perms(a.filter((_,j)=>i!==j)).map(p=>[v,...p])):[[]];
function view(r,id){const p=r.packets[id],c=r.charts[p.chart],cell=r.geometry.cells[c.cell],a=c.aliases.C0.split(',').map(Number),sub=v=>v.map((x,i)=>x-a[i]);
 const descriptor={species:c.species,ownerKind:cell.owner.kind,inverted:cell.owner.inverted,
 ownerOrigin:sub(cell.owner.origin),vertices:cell.vertices.map(v=>sub(v.split(',').map(Number))).sort((x,y)=>JSON.stringify(x).localeCompare(JSON.stringify(y))),
 aliases:Object.fromEntries(Object.entries(c.aliases).map(([n,v])=>[n,sub(v.split(',').map(Number))]))};
 return {key:JSON.stringify(descriptor),descriptor,anchor:a};}
const states=[],byKey=new Map(),queue=[],roots=[],edges=[],CAP=20000;
function add(r,id){const v=view(r,id);if(byKey.has(v.key))return byKey.get(v.key);
 assert(states.length<CAP,'Translation quotient cap reached: NOT a closure theorem');
 const index=states.length;byKey.set(v.key,index);states.push({index,...v});queue.push({r,id,index});return index;}
const seed=makeLatticeItem('tetrahedron',[0,0,0,0]);
for(const marking of perms([0,1,2,3])){const r=new GenerativeAssemblyRules({seedBindings:Object.fromEntries(names.slice(0,4).map((n,i)=>[n,seed.vertices[marking[i]].join(',')]))});roots.push({marking,index:add(r,r.root)});}
for(let q=0;q<queue.length;q++){
 const {r,id,index}=queue[q],chart=r.packets[id].chart;
 const canonical=r.packet(chart,0,ID),source=view(r,canonical);assert.equal(source.key,states[index].key);
 for(const oi of r.outgoing(canonical)){
  const op=r.operations[oi];assert(r.validateTransfer(op));const target=view(r,op.target),next=add(r,op.target);
  edges.push({source:index,target:next,kind:op.kind,permutation:op.permutation,
    displacement:target.anchor.map((x,i)=>x-source.anchor[i]),
    fieldParity:op.kind==='reader-phase-advance'&&source.descriptor.species==='proton'?1:0});
 }
}
assert.equal(queue.length,states.length);
// Independent representatives check translation/origin/permutation naturality.
// The all-parameter argument is structural (documented with the theorem);
// these are regressions, not its substitute.
const translations=[[0,0,0,0],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]],origins=[0,7],coefficientFrames=[ID,[1,0,2,3,4],[1,2,3,4,0]];
let naturalityCases=0,naturalityEdges=0;
for(const state of states)for(const t of translations){
 const d=state.descriptor,anchor=state.anchor.map((x,i)=>x+t[i]),point=v=>v.map((x,i)=>x+anchor[i]);
 const r=new GenerativeAssemblyRules(),owner=makeLatticeItem(d.ownerKind,point(d.ownerOrigin),d.inverted);
 const component=d.vertices.map(point),cell=r.geometry.register(owner,component);
 const aliases=Object.fromEntries(Object.entries(d.aliases).map(([n,v])=>[n,point(v).join(',')]));
 // These are translations of actual admitted reference vertices, not new modes.
 for(const v of Object.values(aliases))r.geometry.points.set(v,v.split(',').map(Number));
 const chart=r.chart(cell,d.species,aliases);
 const expected=edges.filter(e=>e.source===state.index);
 for(const origin of origins)for(const coefficients of coefficientFrames){
  const id=r.packet(chart,origin,coefficients),source=view(r,id);assert.equal(source.key,state.key);
  const ops=r.outgoing(id).map(i=>r.operations[i]);assert.equal(ops.length,expected.length);
  for(const op of ops){assert(r.validateTransfer(op));const target=view(r,op.target),e=expected.find(e=>e.kind===op.kind);assert(e);
   assert.equal(target.key,states[e.target].key);assert.deepEqual(target.anchor.map((x,i)=>x-source.anchor[i]),e.displacement);
   assert.deepEqual(op.permutation,e.permutation);assert.deepEqual(r.packets[op.target].permutation,e.permutation.map(i=>coefficients[i]));
   assert.equal(r.packets[op.target].origin,origin+op.phaseDelta);naturalityEdges++;
  }naturalityCases++;
 }
}
const sources=['research/voevodsky/checkers/check_ramsey_native_chart_quotient.mjs','research/nima/generative-phase-assembly.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs','research/strominger/demos/particle-overlap-tetrahedron/simplex-components.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/carrier.mjs'];
const result={schema:'marici.ramsey-native-chart-quotient.v1',node:'admitted-reversal-overlap-coherence',status:'closed_translation_quotient',
 states:states.map(({key,...s})=>s),edges,roots,cap:CAP,queueExhausted:true,
 naturalityRegressions:{cases:naturalityCases,edges:naturalityEdges,translations,origins,coefficientFrames},
 scope:'Finite exact quotient exploration. Unbounded completeness additionally requires the stated translation/origin/coefficient naturality argument for the source constructors; queue exhaustion is not a depth sample.',
 source_sha256:Object.fromEntries(sources.map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]))};
writeFileSync('research/voevodsky/results/ramsey-native-chart-quotient-v1.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,states:states.length,edges:edges.length,roots:roots.length,queueExhausted:true,naturalityCases,naturalityEdges}));
