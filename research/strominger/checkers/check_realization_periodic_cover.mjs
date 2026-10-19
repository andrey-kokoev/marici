// Period-two coordinate chart with retained integer lift. Not packet quotienting.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
const file='research/strominger/results/hydrogen-edge-attachment/verification.json',bytes=await readFile(file),samples=JSON.parse(bytes).rows,rows=[];
const encode=n=>{assert.ok(Number.isSafeInteger(n)&&n>=0);return {phase:n%2,winding:Math.floor(n/2)};},decode=({phase,winding})=>{assert.ok([0,1].includes(phase)&&Number.isSafeInteger(winding)&&winding>=0);return 2*winding+phase;};
for(const sample of samples){
 const r=new GenerativeAssemblyRules({seedBindings:sample.seedBindings}),records=[],word=[];let current=r.root;
 for(let step=0;step<=10;step++){
  const p=r.packets[current],c=r.charts[p.chart],pn=r.outgoing(current).map(i=>r.operations[i]).find(o=>o.kind==='PN'),ne=r.outgoing(pn.target).map(i=>r.operations[i]).find(o=>o.kind==='NE'),reference=r.charts[r.packets[ne.target].chart],chartKey=JSON.stringify({aliases:reference.aliases,permutation:p.permutation}),coordinate=encode(p.origin);
  assert.equal(decode(coordinate),p.origin);if(step>=2)assert.equal(chartKey,records[step-2].chartKey);
  const occurrences=Object.fromEntries(Object.keys(reference.aliases).map(name=>[name,{vertex:reference.aliases[name],role:name[0],index:p.origin+Number(name.slice(1))}]));
  for(const [name,o] of Object.entries(occurrences))assert.equal(o.index,decode(coordinate)+Number(name.slice(1)));
  records.push({packet:current,origin:p.origin,...coordinate,chartKey,occurrences,history:[...word]});
  if(step<10){const op=r.outgoing(current).map(i=>r.operations[i]).find(o=>o.kind==='reader-phase-advance');assert.ok(op);r.validateTransfer(op);word.push(op.id);current=op.target;}
 }
 assert.equal(new Set(records.map(x=>x.chartKey)).size,2);assert.equal(new Set(records.map(x=>x.packet)).size,11);
 for(let i=0;i<10;i++){const a=records[i],b=records[i+1];assert.equal(b.phase,1-a.phase);assert.equal(b.winding,a.winding+(a.phase===1?1:0));assert.equal(b.history.length,a.history.length+1);}
 assert.equal(records[2].chartKey,records[0].chartKey);assert.notEqual(records[2].winding,records[0].winding);assert.notDeepEqual(records[2].occurrences,records[0].occurrences);
 rows.push({marking:sample.marking,records});
}
// A two-edge phase circle is subdivided into four edges for a simplicial model.
// Link circle has three vertices; their product triangulates the proposed base.
const triangles=[],vertex=(i,j)=>((i%4+4)%4)*3+(j%3+3)%3;
for(let i=0;i<4;i++)for(let j=0;j<3;j++)triangles.push([vertex(i,j),vertex(i+1,j),vertex(i+1,j+1)],[vertex(i,j),vertex(i+1,j+1),vertex(i,j+1)]);
const out='research/strominger/results/realization-periodic-cover';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'periodic-chart-with-lift-passed',rows,source:file,sourceSha256:createHash('sha256').update(bytes).digest('hex'),checkerSha256:createHash('sha256').update(await readFile(new URL('./check_realization_periodic_cover.mjs',import.meta.url))).digest('hex'),chartCoordinates:{encoding:'phase=r mod 2; winding=floor(r/2)',decoding:'r=2*winding+phase',advance:'phase 0->1 at same winding; phase 1->0 with winding+1'},proposedBaseTriangles:triangles,scope:'All 24 native P same-body reader orbits through origin 10. Geometry/reference permutation repeats every 2; lifted coordinates retain exact origin, all absolute occurrences and explicit operation word. Proposed torus is product of chosen periodic realization chart and co-moving transverse link circle, not an inferred M/C torus or quotient of complete assembly states. Physical/global field gluing not supplied. Native dynamics remains forward graded; production/viewer unchanged.'},null,2)+'\n');console.log(JSON.stringify({status:'passed',markings:rows.length,records:rows.reduce((s,r)=>s+r.records.length,0),originPreserved:true,historyPreserved:true}));
