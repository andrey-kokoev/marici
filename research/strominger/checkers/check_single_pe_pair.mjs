import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {makeSinglePEPair} from '../single-pe-pair-model.mjs';
import {applyPhasePermutation,activePhaseSlots} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {contextFrameActions,composeFrames,permuteReference} from '../retained-context-braid-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const checks=[];function check(name,f){f();checks.push(name);}
const model=makeSinglePEPair(),value=[[2,1],[3,-2],[5,3],[7,-4],[11,5]],state=model.prepare(value);
const initial=structuredClone(state),ab=model.reconstruct(state.endpoints.P,state.endpoints.E,1),ba=model.reconstruct(state.endpoints.P,state.endpoints.E,-1);
check('actual marked P/E endpoints have a unique common face-neighbor neutron',()=>{
 assert.equal(ab.witness.commonFaceNeighbors.length,1);assert.equal(ab.chart.species,'neutron');
 assert.equal(ab.cell,model.rules.charts[model.rules.packets[model.pn.target].chart].cell);
 const a=model.rules.geometry.cells[model.pChart.cell].vertices,b=model.rules.geometry.cells[model.eChart.cell].vertices;
 assert.equal(a.filter(v=>b.includes(v)).length,2); // P/E meet on an edge, not a face.
 assert.equal(model.rules.inspect([model.pn.source,model.pn.target,model.ne.target]).certifiedExit,true);
});
check('ab and ba reconstruct the same full N with opposite endpoint readings',()=>{
 assert.deepEqual(ab.coefficients,ba.coefficients);assert.equal(ab.cellKey,ba.cellKey);
 assert.equal(ab.readFrom,'P');assert.equal(ba.readFrom,'E');assert.equal(ab.orientation,-ba.orientation);
 assert.deepEqual(ab.coefficients,applyPhasePermutation(value,model.pn.permutation));
});
check('reversal is in place and requires a separate positive confirmation',()=>{
 assert.equal(model.reverseInPlace(state),state);assert.equal(state.confirmation,'pending');assert.equal(state.history.length,1);
 assert.equal(model.confirm(state),state);assert.equal(state.confirmation,'confirmed');assert.equal(state.orientation,-1);
 assert.deepEqual(state.endpoints,initial.endpoints);assert.deepEqual(state.neutron.coefficients,initial.neutron.coefficients);
 assert.deepEqual(state.history.map(h=>h.action),['reverse-flow-in-place','positive-confirmation']);
 assert.throws(()=>model.confirm(state),/pending reversal/);
});
check('two confirmed reversals return the state while retaining all four action records',()=>{
 model.confirm(model.reverseInPlace(state));assert.equal(state.orientation,1);assert.deepEqual(state.neutron,initial.neutron);assert.equal(state.history.length,4);
});
check('an inconsistent endpoint cannot receive positive confirmation',()=>{
 const bad=model.prepare(value);model.reverseInPlace(bad);bad.endpoints.E[0][0]+=1;
 assert.throws(()=>model.confirm(bad),/endpoints disagree/);assert.equal(bad.confirmation,'pending');
 assert.equal(bad.history.filter(h=>h.action==='positive-confirmation').length,0);
});
check('visible P/E faces alone do not determine the full neutron state',()=>{
 const other=structuredClone(value);other[3]=[23,29];other[4]=[31,37];
 const s=model.prepare(other),face=(species,v)=>activePhaseSlots[species].map(i=>v[i]);
 assert.deepEqual(face('proton',initial.endpoints.P),face('proton',s.endpoints.P));
 assert.deepEqual(face('electron',initial.endpoints.E),face('electron',s.endpoints.E));
 assert.notDeepEqual(initial.neutron.coefficients,s.neutron.coefficients);
});
check('all five basis coordinates reconstruct independently from each endpoint',()=>{
 for(let i=0;i<5;i++){const v=Array.from({length:5},(_,j)=>[Number(i===j),0]),s=model.prepare(v);
  assert.deepEqual(model.reconstruct(s.endpoints.P,s.endpoints.E,-1).coefficients,applyPhasePermutation(v,model.pn.permutation));}
});
const frames=[[0,1,2,3]],seen=new Set(['0123']);
for(let i=0;i<frames.length;i++)for(const g of Object.values(contextFrameActions)){const p=composeFrames(g,frames[i]);if(!seen.has(p.join(''))){seen.add(p.join(''));frames.push(p);}}
check('the marked single-pair reconstruction holds in all eight retained context frames',()=>{
 for(const frame of frames){
  const seedBindings=Object.fromEntries(['C0','M0','C1','M1'].map(n=>[n,permuteReference(model.pChart.aliases[n],frame)]));
  const m=makeSinglePEPair({seedBindings}),s=m.prepare(value);m.confirm(m.reverseInPlace(s));
  assert.deepEqual(s.neutron.coefficients,ab.coefficients);
  for(const [mark,point]of Object.entries(ab.chart.aliases))assert.equal(s.neutron.chart.aliases[mark],permuteReference(point,frame));
 }
});
check('ba is an interface reading, not an invented native E-to-N propagation',()=>{
 assert.deepEqual(model.rules.outgoing(model.ne.target),[]);assert.equal(ba.nativeReverseGrowth,false);
});
const paths=['research/strominger/single-pe-pair-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs','research/nima/generative-phase-assembly.mjs'];
const receipt={status:'passed',checks,classification:'Fixture-local N reconstructed as a compatible marked P/E interface; reversed reading positively confirmed',
 sourceSha256:Object.fromEntries(paths.map(p=>[p,crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex')])),
 hypothesis:{a:'proton endpoint',b:'electron endpoint',ab:'compatible P-to-E interface mediated by one native neutron',ba:'the same neutron interface read from E toward P',aa:'P self-comparison, no new species',bb:'E self-comparison, no new species'},
 ab,ba,confirmedExecution:state,
 boundary:'This uses the native PN/NE marked-boundary laws. It is not a literal product of amplitudes, proof of a physical P+E=N reaction, native reverse growth, or an Artin braid crossing. Polarity means flow orientation here, not electric charge conjugation. No missing stage rule or fourteen-step extrapolation is assumed.'};
fs.writeFileSync(path.join(root,'research/strominger/results/single-pe-pair-v1.json'),JSON.stringify(receipt,null,2)+'\n');
console.log(JSON.stringify({status:receipt.status,checks:checks.length,classification:receipt.classification},null,2));
