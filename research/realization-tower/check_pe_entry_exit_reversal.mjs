import assert from 'node:assert/strict';
import {writeFile} from 'node:fs/promises';
import {slice,cells,seed,worldPoint} from './normal-ray-model.mjs';
import {nativePhaseFrame,auditPhaseFrame} from '../strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const key=p=>JSON.stringify(p),stop=slice(1),other=cells[stop.atStop.find(i=>i!==seed.id)];
const face=seed.vertices.filter(p=>other.vertices.some(q=>key(q)===key(p)));
const a=seed.vertices.find(p=>!face.some(q=>key(q)===key(p))),b=other.vertices.find(p=>!face.some(q=>key(q)===key(p)));
const swap=p=>key(p)===key(a)?b:key(p)===key(b)?a:p;
const sort=ps=>ps.map(key).sort();
assert.deepEqual(sort(seed.vertices.map(swap)),sort(other.vertices));
assert.deepEqual(sort(other.vertices.map(swap)),sort(seed.vertices));
for(const p of [...seed.vertices,...other.vertices])assert.deepEqual(swap(swap(p)),p);
// Choose the shared face's C,M,C order. All six orders are tested; none is
// claimed to be selected uniquely by bare geometric placement.
function perms(xs){return xs.length?xs.flatMap((x,i)=>perms(xs.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];}
const examples=[];
for(const [c1,m1,c2] of perms(face)){
 // P at origin 1 and E at origin 0 have the SAME actual shared occurrences:
 // P: C1 M1 C2 [M2]; E: M1 C1 C2 [M2]. Distinct outside vertices remain distinct.
 const p=nativePhaseFrame('p','proton',{C0:key(c1),M0:key(m1),C1:key(c2),M1:key(a)});
 for(const occurrence of [...p.window,p.context])occurrence.index++;
 const e=nativePhaseFrame('e','electron',{M1:key(m1),C1:key(c1),C2:key(c2),M2:key(b)});
 assert.equal(auditPhaseFrame(p).status,'native-template-compatible');assert.equal(auditPhaseFrame(e).status,'native-template-compatible');
 for(const o of p.window)assert(e.window.some(v=>key(v)===key(o)));
 function reverse(frame){return {id:frame.id==='p'?'e':'p',species:frame.species==='proton'?'electron':'proton',
  window:[frame.window[1],frame.window[0],frame.window[2]],
  context:{...frame.context,vertex:key(swap(JSON.parse(frame.context.vertex)))}};}
 assert.deepEqual(reverse(p),e);assert.deepEqual(reverse(e),p);
 assert.deepEqual(reverse(reverse(p)),p);
 examples.push({proton:p,electron:e});
}
const squaredEdges=vertices=>vertices.flatMap((p,i)=>vertices.slice(i+1).map(q=>{const x=worldPoint(p),y=worldPoint(q);return Number(x.reduce((s,v,j)=>s+(v-y[j])**2,0).toFixed(9));})).sort((a,b)=>a-b);
const pEdges=squaredEdges(seed.vertices),eEdges=squaredEdges(other.vertices);
assert.notDeepEqual(pEdges,eEdges);
const out={status:'pass-local-marked-entry-exit-involution',face,entryApex:a,exitApex:b,testedFaceOrders:examples.length,examples,
 reversal:{sharedFace:'fixed pointwise',windowOrder:[1,0,2],apices:'exchanged',twice:'exact identity on local marked presentation',
  origins:'P=1, E=0; actual face indices unchanged, not a forward realization advance'},
 limits:['Reversal is the simplicial exchange of the two tetrahedra, not a Euclidean reflection: their edge-length multisets differ.',
 'The ordered-window transposition is explicit and required; bare endpoint exchange alone does not reorder the reader.',
 'This compares native four-occurrence frames. No full five-coefficient transport or outside-reference-context law is proved.',
 'This local involution does not identify the two contexts as one occurrence or erase command history.',
 'No global lattice automorphism, unique initial C/M marking, neutron necessity or physical H-1 binding is derived.'],
 edgeSquaredLengths:{proton:pEdges,electron:eEdges}};
await writeFile(new URL('./results/pe-entry-exit-reversal-v1.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({status:out.status,testedFaceOrders:examples.length,sharedFaceFixed:true,nativeFramesExchanged:true,doubleReversalIdentity:true,euclideanReflection:false}));
