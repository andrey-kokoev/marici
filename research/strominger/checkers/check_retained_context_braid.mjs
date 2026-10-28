import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {makeRetainedContextBraid,contextFrameActions,composeFrames,permuteReference} from '../retained-context-braid-model.mjs';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {applyPhasePermutation,spectralReadout} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex');
const priorPath='research/strominger/results/binary-simplex-native-binding-v1.json',prior=JSON.parse(fs.readFileSync(path.join(root,priorPath),'utf8'));
const checks=[];function check(name,f){f();checks.push(name);}
check('previous failed-binding receipt matches live sources',()=>{for(const [p,h]of Object.entries(prior.sourceSha256))assert.equal(hash(p),h);});
const model=makeRetainedContextBraid(),I=[0,1,2,3],q=[1,2,3,0],L=contextFrameActions.L,R=contextFrameActions.R;
const inverse=p=>p.map((_,i)=>p.indexOf(i));
const power=(p,n)=>{let out=I;for(let i=0;i<n;i++)out=composeFrames(p,out);return out;};
const frames=[I],frameKeys=new Set([I.join('')]);
for(let i=0;i<frames.length;i++)for(const p of [L,R]){const g=composeFrames(p,frames[i]),key=g.join('');if(!frameKeys.has(key)){frameKeys.add(key);frames.push(g);}}
check('closure grows five through six and seven to eight actual references',()=>{assert.equal(model.seedReferences.length,5);assert.equal(model.discovery.length,3);assert.equal(model.references.length,8);assert.equal(frames.length,8);});
check('every outside reference is the native P completion for one corner',()=>{assert.deepEqual(model.references,[...model.central,...model.outside]);assert.equal(new Set(model.outside).size,4);});
const distance=(a,b)=>a.split(',').map(Number).reduce((s,x,i)=>s+(x-Number(b.split(',')[i]))**2,0);
check('all frame actions preserve exact native geometry on the entire eight-reference support',()=>{
 for(const g of frames)for(const a of model.references)for(const b of model.references)assert.equal(distance(a,b),distance(permuteReference(a,g),permuteReference(b,g)));
});
const symbols=model.references.map((point,i)=>({symbol:i<5?`retained-${i}`:`unassigned-${i}`,reference:point}));
check('no new coefficient is invented or discarded in the parametric lift',()=>{
 for(const g of frames)assert.deepEqual(model.push(model.push(symbols,g),inverse(g)),symbols);
 assert.equal(symbols.filter(x=>x.symbol.startsWith('unassigned')).length,3);
});
check('passive reader change still depends on the additional context',()=>{
 const changed=structuredClone(symbols);changed[7]={symbol:'different-free-parameter'};
 assert.deepEqual(model.view(symbols,I),model.view(changed,I));
 assert.notDeepEqual(model.view(symbols,L),model.view(changed,L));
});
const canonical=new GenerativeAssemblyRules(),baseChart=canonical.charts[canonical.packets[canonical.root].chart];
const getWord=e=>{
 const pn=e.outgoing(e.root).map(i=>e.operations[i]).find(o=>o.kind==='PN');
 const ne=e.outgoing(pn.target).map(i=>e.operations[i]).find(o=>o.kind==='NE');
 for(const op of [pn,ne])assert.ok(e.validateTransfer(op));
 return {pn,ne,charts:[e.root,pn.target,ne.target].map(id=>e.charts[e.packets[id].chart])};
};
const base=getWord(canonical),families=[];
for(const g of frames){
 const seedBindings=Object.fromEntries(['C0','M0','C1','M1'].map(name=>[name,permuteReference(baseChart.aliases[name],g)]));
 const e=new GenerativeAssemblyRules({seedBindings}),word=getWord(e);
 for(let j=0;j<3;j++)for(const [name,point]of Object.entries(base.charts[j].aliases))assert.equal(word.charts[j].aliases[name],permuteReference(point,g));
 families.push({frame:g,PN:word.pn.permutation,NE:word.ne.permutation,charts:word.charts});
}
checks.push('all eight frame changes transport the actual native P/N/E charts and every outside mark');
const basis=Array.from({length:8},(_,i)=>Array.from({length:8},(_,j)=>[Number(i===j),0]));
check('context transport commutes with PN and NE on every full-bank basis vector',()=>{
 for(const g of frames)for(const values of basis)for(const op of [base.pn,base.ne]){
  assert.deepEqual(model.push(model.nativeOperation(values,I,op.permutation),g),model.nativeOperation(model.push(values,g),g,op.permutation));
 }
});
check('five-slot native readout and inverse recovery agree with the retained-bank execution',()=>{
 for(const g of frames)for(const values of basis){
  const moved=model.push(values,g),input=model.view(moved,g);
  const n=model.nativeOperation(moved,g,base.pn.permutation),e=model.nativeOperation(n,g,base.ne.permutation);
  assert.deepEqual(model.view(e,g),applyPhasePermutation(applyPhasePermutation(input,base.pn.permutation),base.ne.permutation));
  const restored=model.nativeOperation(model.nativeOperation(e,g,inverse(base.ne.permutation)),g,inverse(base.pn.permutation));assert.deepEqual(restored,moved);
 }
});
// Strict witness diagram on four lifted chart occurrences. Each edge is a
// derived context transport, not a new particle rule. The six edge maps obey
// all four face equations; both tetrahedral reductions are identical maps.
const edge=(i,j,values)=>model.push(values,power(q,j-i));
let faceTests=0;
for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)for(let k=j+1;k<4;k++)for(const values of basis){assert.deepEqual(edge(j,k,edge(i,j,values)),edge(i,k,values));faceTests++;}
check('four face comparisons and the tetrahedral coherence have a strict context-transport witness',()=>{
 assert.equal(faceTests,32);
 for(const values of basis){const long=edge(2,3,edge(1,2,edge(0,1,values)));assert.deepEqual(long,edge(0,3,values));assert.deepEqual(edge(2,3,edge(0,2,values)),edge(1,3,edge(0,1,values)));}
});
const block=state=>[...'LRRR'].reduce((s,a)=>model.reframe(s,a),state);
check('LRRR remains one q step on the complete retained support',()=>{
 const s=block(model.initial(symbols));assert.equal(s.t,1);assert.deepEqual(s.frame,q);assert.deepEqual(s.values,model.push(symbols,q));assert.equal(s.history.length,4);
});
check('four blocks return coefficients but retain the Sigma grade and sixteen action occurrences',()=>{
 let s=model.initial(symbols);for(let i=0;i<4;i++)s=block(s);
 assert.deepEqual(s.values,symbols);assert.deepEqual(s.frame,I);assert.equal(s.t,4);assert.equal(s.history.length,16);
});
check('opposite braid routes retain different grades even with the eight-reference lift',()=>{
 const run=word=>[...word].reduce((s,a)=>model.reframe(s,a),model.initial(symbols));
 const a=run('LRLR'),b=run('RLRL');assert.deepEqual(a.values,b.values);assert.deepEqual(a.frame,b.frame);assert.equal(a.t-b.t,4);
});
check('reader transport alone is not a PNE layer generator: all local spectral readouts are invariant',()=>{
 const values=Array.from({length:8},(_,i)=>[i+1,2*i-3]);
 for(const g of frames)for(const species of ['proton','neutron','electron'])assert.deepEqual(spectralReadout(species,model.view(model.push(values,g),g)),spectralReadout(species,model.view(values,I)));
});
const paths=[priorPath,'research/strominger/retained-context-braid-model.mjs','research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs'];
const result={status:'passed',checks,sourceSha256:Object.fromEntries(paths.map(p=>[p,hash(p)])),
 classification:'Eight-reference context-covariant extension with a strict transport witness; not an admitted new native evolution or derived PNE filler',
 support:model.references,discovery:model.discovery,sourceNativeFrameFamilies:families,
 witness:{vertices:[0,1,2,3],edges:'q^(j-i) on all eight references with grade change j-i',faces:'derived strict composition equalities',tetrahedron:'the two reductions are equal on all eight basis vectors',nativeIncidenceSpan:prior.witnessSpan,limitation:'This witness is for the context-transport diagram, not a derived analytic filler on the full retained native complex.'},
 parameterGate:'The initial five-slot packet leaves three context coefficients unspecified. They remain independent symbols. Active field+reader transport is invertible; passive reader change at fixed field depends on those symbols.',
 dynamicsGate:'Transporting field and reader together preserves the native spectral readout. PN and NE commute with the frame action, but this does not choose when or where to execute them, so the PNE surface words are not generated.',
 next:'Bind the split/leaf schedule to native attachment versus reader transport on the common context bank, retaining the separate clocks and supplying or deriving a boundary condition for newly exposed contexts.'};
const out=path.join(root,'research/strominger/results/retained-context-braid-v1.json');fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,checks:checks.length,supportSize:model.references.length,classification:result.classification},null,2));
