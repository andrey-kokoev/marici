import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {makeLatticeItem,itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {createSequentialConstruction,resumeFaceContinuation,sequentialRule} from '../demos/particle-overlap-tetrahedron/sequential-space-model.mjs';
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const symmetries=permutations([0,1,2,3]),permute=(q,p)=>p.map(i=>q[i]);
const seed=makeLatticeItem('tetrahedron',[0,0,0,0]),pending=createSequentialConstruction(),initial=pending.snapshot();
assert.deepEqual(initial.entry,{kind:'inner-center',source:'inner-dimension',point:[.25,.25,.25,.25]});
assert.equal(initial.incomingFace,null);assert.equal(initial.exit,null);assert.equal(initial.status,'needs-exit');
for(let i=0;i<3;i++){const s=pending.step();assert.equal(s.committed,false);assert.deepEqual(s.items,initial.items);assert.equal(s.identity,initial.identity);}
// Explicit test boundary, not a default endpoint or a particle-count target.
const exitCell=makeLatticeItem('tetrahedron',[2,1,-1,-2]);
const sequence=createSequentialConstruction({exitCell}),first=sequence.snapshot();
assert.equal(first.status,'ready');assert.deepEqual(first.exit.point,exitCell.center);assert.equal(first.exit.reached,false);
const prefixes=[first];
while(sequence.snapshot().status==='ready'){
 const before=sequence.snapshot(),after=sequence.step();
 assert.equal(after.committed,true);assert.equal(after.items.length,before.items.length+1);assert.equal(after.added,before.added+1);
 assert.deepEqual(after.items.slice(0,-1),before.items);assert.equal(after.identity,first.identity);
 assert.ok(after.parameter>before.parameter);assert.deepEqual(after.exit.point,first.exit.point);
 const event=after.events.at(-1);assert.equal(event.priorItemCount,before.items.length);
 assert.ok(after.items.slice(-2).every(s=>s.faces.some(f=>itemKey(f)===itemKey(event.face))));prefixes.push(after);
 assert.ok(after.added<100,'Test safety bound, not a construction parameter');
}
const final=sequence.snapshot();assert.equal(final.status,'complete');assert.equal(final.items.at(-1).key,exitCell.key);assert.equal(final.exit.reached,true);assert.equal(final.exit.identity,first.identity);assert.equal(final.parameter,1);
assert.equal(sequence.step().committed,false);assert.deepEqual(sequence.snapshot().items,final.items);
for(const p of symmetries){
 const engine=createSequentialConstruction({exitCell:makeLatticeItem(exitCell.kind,permute(exitCell.origin,p),exitCell.inverted)});
 for(let i=0;i<final.added;i++)assert.equal(engine.step().committed,true);
 const s=engine.snapshot();assert.equal(s.status,'complete');assert.deepEqual(s.items.map(i=>i.key),final.items.map(i=>itemKey(i.vertices.map(q=>permute(q,p)))));
}
const singular=createSequentialConstruction({exitCell:makeLatticeItem('tetrahedron',[1,1,-1,-1])});assert.equal(singular.snapshot().status,'ambiguous');assert.equal(singular.step().committed,false);assert.equal(singular.snapshot().added,0);
const coincident=createSequentialConstruction({exitCell:seed});assert.equal(coincident.snapshot().status,'complete');assert.equal(coincident.snapshot().added,0);
assert.throws(()=>createSequentialConstruction({incomingFace:seed.faces[0]}));
assert.throws(()=>createSequentialConstruction({exitCell:{kind:'tetrahedron',origin:[1,1,1,1]}}));
// A later spatial face admission is still a separate operation from seed entry.
const oct=makeLatticeItem('octahedron',[-1,0,0,0]),resume=resumeFaceContinuation({item:oct,incomingFace:oct.faces[0]});assert.equal(resume.snapshot().entry.kind,'spatial-face');assert.equal(resume.step().committed,true);
// Exact integer-coordinate SAT on every admitted prefix: positive primitives,
// no duplicates, no positive-volume overlap. No final assembly is imported.
const faces=[[0,2,1],[0,1,3],[0,3,2],[1,2,3]],edges=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]],sub=(a,b)=>a.map((x,i)=>x-b[i]),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],dot=(a,b)=>a.reduce((n,x,i)=>n+x*b[i],0);
for(const prefix of prefixes){
 const components=prefix.items.flatMap(s=>s.components);assert.equal(new Set(components.map(itemKey)).size,components.length);
 assert.ok(components.flat().every(p=>p.every(Number.isInteger)&&p.reduce((a,b)=>a+b,0)===1));
 const tets=components.map(c=>c.map(p=>p.slice(0,3)));
 for(let i=0;i<tets.length;i++){
  const [a,b,c,d]=tets[i];assert.equal(Math.abs(dot(sub(b,a),cross(sub(c,a),sub(d,a)))),1);
  for(let j=i+1;j<tets.length;j++){
   const axes=[];for(const t of [tets[i],tets[j]])for(const [a,b,c] of faces)axes.push(cross(sub(t[b],t[a]),sub(t[c],t[a])));
   for(const [a,b] of edges)for(const [c,d] of edges)axes.push(cross(sub(tets[i][b],tets[i][a]),sub(tets[j][d],tets[j][c])));
   assert.ok(axes.some(axis=>{if(axis.every(x=>x===0))return false;const a=tets[i].map(p=>dot(p,axis)),b=tets[j].map(p=>dot(p,axis));return Math.max(...a)<=Math.min(...b)||Math.max(...b)<=Math.min(...a);}));
  }
 }
}
const report={status:'verified-boundary-transition',rule:sequentialRule,entry:initial.entry,unspecifiedExit:'needs-exit, not a construction obstruction',testExit:{kind:exitCell.kind,origin:exitCell.origin},committedItems:final.added,prefixesChecked:prefixes.length,coordinatePermutationChecks:24,positiveDisjointPrefixes:true,sharedIdentityAtExit:true,singularSegment:'explicit ambiguity; no arbitrary tie-break',scope:'Sequential realization between supplied endpoints under a straight-segment proposal; not a Pb-208 derivation or whole-structure witnessing proof.'};
const out='research/strominger/results/sequential-space';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log('PASS endpoint-conditioned sequential construction, one-item commits, shared identity at exit, 24 symmetry checks, positive/disjoint prefixes; unspecified exit is pending boundary data');
