import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {makeSevenContextFourDepth} from '../seven-context-four-depth-model.mjs';
import {windowProtocol} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const checks=[];function check(name,f){f();checks.push(name);}
const model=makeSevenContextFourDepth(),input=[[2,1],[3,-2],[5,3],[7,-4],[11,5]],run=model.run(input);
const plain=s=>{const out=structuredClone(s);delete out.bank;return out;};
check('the actual active P/E triangles meet at C1 and have seven incident face contexts',()=>{
 assert.equal(model.vertex,'C1');assert.equal(model.contexts.length,7);
 assert.deepEqual([1,2,3].map(n=>model.contexts.filter(c=>c.vertices.length===n).length),[1,4,2]);
 assert.equal(model.allFaces.length,13);assert.equal(model.covers.length,8);
 for(const [species,marks]of Object.entries(model.faces)){
  const chart=species==='P'?model.pair.pChart:model.pair.eChart;
  assert.ok(model.pair.rules.geometry.cells[chart.cell].faces.some(face=>marks.every(m=>face.includes(chart.aliases[m]))));
 }
});
check('the seven-context star is not misreported as a closed simplicial complex',()=>{
 const ids=new Set(model.contexts.map(c=>c.id));assert.ok(model.allFaces.some(f=>!ids.has(f.id)));
 assert.equal(model.allFaces.filter(f=>f.vertices.length===1).length,5);
});
check('the native N active triangle is a separate mixed face in the abstract reference 4-simplex',()=>{
 const n=windowProtocol.find(p=>p.species==='neutron').window;
 assert.deepEqual(new Set([...model.faces.P,...model.faces.E]),new Set(['C0','M0','C1','M1','C2']));
 assert.ok(n.includes(model.vertex));assert.ok(!model.allFaces.some(f=>f.id===[...n].sort().join('|')));
 const starWithN=new Set([...model.contexts.map(c=>c.id),[...n].sort().join('|')]);assert.equal(starWithN.size,8);
 // All actual coordinates lie in one affine three-dimensional hyperplane:
 // the abstract reference simplex is not a nondegenerate physical 4-cell.
 for(const point of Object.values(model.pair.pChart.aliases))assert.equal(point.split(',').map(Number).reduce((a,b)=>a+b,0),1);
});
check('four retained depths give twenty-eight positions carrying one 2x2 bank each',()=>{
 assert.equal(run.records.length,28);assert.equal(run.banks.length,4);
 assert.equal(new Set(run.records.map(r=>`${r.depth}:${r.context}`)).size,28);
 for(let d=1;d<=4;d++){
  assert.equal(run.records.filter(r=>r.depth===d).length,7);
  assert.deepEqual(Object.keys(run.banks[d-1]),['aa','ab','ba','bb']);
  assert.ok(run.records.filter(r=>r.depth===d).every(r=>r.bankReference===`depth-${d}`));
 }
});
check('depth is retained occurrence history, not four distinct parity states or a third bank axis',()=>{
 assert.deepEqual(run.states.map(s=>s.orientation),[1,-1,1,-1,1]);
 assert.deepEqual(run.states.map(s=>s.history.length),[0,2,4,6,8]);
 assert.deepEqual(run.final.endpoints,run.states[0].endpoints);
 assert.equal(run.final.history.filter(h=>h.action==='positive-confirmation').length,4);
 assert.equal(run.final.neutron.origin,0);
});
check('off-diagonal readings reverse while native N coefficients and diagonal self-comparisons remain intact',()=>{
 for(let i=1;i<run.banks.length;i++){
  const a=run.banks[i-1],b=run.banks[i];assert.deepEqual(a.aa,b.aa);assert.deepEqual(a.bb,b.bb);
  assert.deepEqual(a.ab,b.ba);assert.deepEqual(a.ba,b.ab);assert.deepEqual(a.ab.coefficients,b.ab.coefficients);
 }
});
const restrict=(reading,vertices)=>vertices.map(v=>reading.values[reading.vertices.indexOf(v)]);
check('native local restrictions commute on all eight face incidences and both triangle diamonds at every depth',()=>{
 for(const state of run.states.slice(1)){
  for(const edge of model.covers){
   const from=model.contexts.find(c=>c.id===edge.from),to=model.contexts.find(c=>c.id===edge.to);
   assert.deepEqual(restrict(model.localRead(state,from),to.vertices),model.localRead(state,to).values);
  }
  for(const triangle of model.contexts.filter(c=>c.vertices.length===3)){
   const edges=model.contexts.filter(c=>c.vertices.length===2&&c.vertices.every(v=>triangle.vertices.includes(v)));
   const point=model.contexts.find(c=>c.vertices.length===1);
   const via=edges.map(edge=>restrict({vertices:edge.vertices,values:restrict(model.localRead(state,triangle),edge.vertices)},point.vertices));
   assert.deepEqual(via[0],via[1]);
  }
 }
});
check('context restriction and confirmed flow reversal commute on the retained interface',()=>{
 for(let d=1;d<=4;d++)for(const c of model.contexts)assert.deepEqual(model.localRead(run.states[d],c),model.localRead(run.states[d-1],c));
});
check('the five occurrence vertices have ten typed edges and ten commuting triangular faces',()=>{
 let edges=0,triangles=0;
 for(let i=0;i<5;i++)for(let j=i+1;j<5;j++){
  edges++;assert.deepEqual(model.depthEdge(run.states[i],i,j),plain(run.states[j]));
  for(let k=j+1;k<5;k++){triangles++;assert.deepEqual(model.depthEdge(model.depthEdge(run.states[i],i,j),j,k),model.depthEdge(run.states[i],i,k));}
 }
 assert.equal(edges,10);assert.equal(triangles,10);
 assert.throws(()=>model.depthEdge(run.states[0],1,2),/typed depth/);
});
check('all five tetrahedral faces and all eight factorizations across the depth 4-simplex preserve the complete history',()=>{
 let tetrahedra=0;
 for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)for(let k=j+1;k<5;k++)for(let l=k+1;l<5;l++){
  tetrahedra++;
  assert.deepEqual(model.depthEdge(model.depthEdge(run.states[i],i,k),k,l),model.depthEdge(model.depthEdge(run.states[i],i,j),j,l));
 }
 assert.equal(tetrahedra,5);
 for(let mask=0;mask<8;mask++){
  const vertices=[0,...[1,2,3].filter((_,i)=>mask&(1<<i)),4];let state=plain(run.states[0]);
  for(let i=1;i<vertices.length;i++)state=model.depthEdge(state,vertices[i-1],vertices[i]);
  assert.deepEqual(state,run.final);
 }
});
check('twenty-eight local face readings do not recover two hidden coefficients without the retained bank',()=>{
 const changed=structuredClone(input);changed[3]=[17,19];changed[4]=[23,29];const other=model.run(changed);
 assert.deepEqual(run.records.map(r=>r.local),other.records.map(r=>r.local));
 assert.notDeepEqual(run.final.neutron.coefficients,other.final.neutron.coefficients);
 for(let i=0;i<5;i++){
  const basis=Array.from({length:5},(_,j)=>[Number(i===j),0]),r=model.run(basis);assert.deepEqual(r.final.endpoints.P,basis);
 }
});
check('positive confirmation and shared-face agreement reject incompatible states',()=>{
 const bad=model.pair.prepare(input);bad.endpoints.E[2][0]+=1;
 assert.throws(()=>model.localRead(bad,model.contexts.find(c=>c.vertices.length===1)),/disagree/);
 assert.throws(()=>model.advance(bad),/endpoints disagree/);assert.equal(bad.confirmation,'pending');
});
const paths=['research/strominger/seven-context-four-depth-model.mjs','research/strominger/single-pe-pair-model.mjs','research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs','research/strominger/demos/particle-overlap-tetrahedron/carrier.mjs'];
const receipt={status:'passed',checks,sourceSha256:Object.fromEntries(paths.map(p=>[p,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex')])),
 classification:'Native active-face seven-context star times four confirmed reversal depths; strict occurrence 4-simplex diagram',
 faces:model.faces,sharedVertex:model.vertex,contexts:model.contexts,restrictionEdges:model.covers,execution:run,
 counts:{contexts:7,depths:4,positions:28,bankEntriesPerPosition:4,indexedBankEntries:112,independentNativeCoefficients:5,physicalFixtureBodies:3},
 distinction:{referenceSimplex:'Abstract simplex on C0,M0,C1,M1,C2; its points are physically affinely dependent.',depthSimplex:'Nerve of four composable confirmed reversals, with five occurrence vertices 0..4. Not identified with the five reference vertices.'},
 limitations:['The seven contexts omit the mixed neutron face; including it gives eight incident contexts. N is retained as the cross-interface witness, not counted as an endpoint-face context.',
 'The four depths are explicit retained repetitions. Native incidence alone does not select a cutoff of four or a chronological ordering of the seven contexts.',
 'Reversal changes orientation but not local face values. The 28 positions do not generate new particles or recover the missing two coefficients from face readouts alone.',
 'No identification with the former matching clock, LRRR clock, Sigma grade, or fourteen-step forward/return word has been derived.']};
fs.writeFileSync(path.join(root,'research/strominger/results/seven-context-four-depth-v1.json'),JSON.stringify(receipt,null,2)+'\n');
console.log(JSON.stringify({status:receipt.status,checks:checks.length,counts:receipt.counts,faces:receipt.faces},null,2));
