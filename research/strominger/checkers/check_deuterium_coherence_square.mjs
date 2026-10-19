// Endpoint square of decorated descriptions, with coefficients carried along
// vertex motion in a fixed reference basis. Not a derived geometric action
// on the five coefficient slots or an interior-isotopy certificate.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {phaseFrame} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseCombination} from '../demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const input='research/strominger/results/hydrogen-edge-attachment/verification.json',bytes=await readFile(input),samples=JSON.parse(bytes).rows;
const orders={proton:[2,3,1,0],neutron:[3,2,1,0],electron:[3,2,0,1]},swap={proton:'electron',electron:'proton',neutron:'neutron'},inverse=p=>p.map((_,i)=>p.indexOf(i)),copy=structuredClone;
const pairs=[['C0','M2'],['M0','C2'],['C1','M1']],rows=[];
for(const sample of samples){
 const aliases=sample.bodies[2].aliases,names=['C0','M0','C1','M1','C2','M2'],partner={};for(const [a,b] of pairs){partner[aliases[a]]=aliases[b];partner[aliases[b]]=aliases[a];}
 const position=Object.fromEntries(names.map(n=>[aliases[n],aliases[n].split(',').map(Number)]));
 const frames=sample.bodies.map((b,i)=>phaseFrame({id:String(sample.packets[i].id),species:b.species,aliases:b.aliases},0));
 const state={position,frames,edges:sample.operations.map((o,i)=>({source:frames[i].id,target:frames[i+1].id,kind:o.kind,face:o.face,permutation:o.permutation})),entry:frames[0].id,exit:frames[2].id};
 function G(s){return {...copy(s),position:Object.fromEntries(Object.keys(s.position).map(v=>[v,copy(s.position[partner[v]])]))};}
 function B(s){
  const transformed=s.frames.map(f=>{const all=[...f.window,f.context].map(o=>({...o,role:o.role==='M'?'C':'M',index:2-o.index})),v=orders[f.species].map(i=>all[i]);return {...f,species:swap[f.species],window:v.slice(0,3),context:v[3]};}).reverse();
  return {...copy(s),frames:transformed,edges:s.edges.map(e=>({...e,source:e.target,target:e.source,kind:e.kind==='PN'?'NE':'PN',permutation:inverse(e.permutation)})).reverse(),entry:s.exit,exit:s.entry};
 }
 function audit(s){
  assert.equal(s.frames[0].id,s.entry);assert.equal(s.frames.at(-1).id,s.exit);
  assert.equal(new Set(Object.values(s.position).map(p=>p.join(','))).size,6);
  const a=auditPhaseCombination(s.frames,s.edges.map(e=>({from:e.source,to:e.target,kind:e.kind,identification:'same-occurrence',vertices:e.face})));assert.equal(a.status,'native-phase-compatible');
  for(const e of s.edges){const fa=s.frames.find(f=>f.id===e.source),fb=s.frames.find(f=>f.id===e.target),va=[...fa.window,fa.context].map(o=>o.vertex),vb=[...fb.window,fb.context].map(o=>o.vertex);assert.deepEqual(va.filter(v=>vb.includes(v)).sort(),[...e.face].sort());assert.deepEqual([...e.permutation].sort(),[0,1,2,3,4]);}
  return {localFrameAudit:a.status,entry:s.entry,exit:s.exit,coefficientMap:s.edges.reduce((p,e)=>e.permutation.map(i=>p[i]),[0,1,2,3,4])};
 }
 const geometricThenReading=B(G(state)),readingThenGeometric=G(B(state));assert.deepEqual(geometricThenReading,readingThenGeometric);assert.deepEqual(G(G(state)),state);assert.deepEqual(B(B(state)),state);assert.deepEqual(B(G(B(G(state)))),state);
 const corners={original:audit(state),turned:audit(G(state)),reversed:audit(B(state)),turnedAndReversed:audit(geometricThenReading)};
 const bad=copy(readingThenGeometric);[bad.edges[0].permutation[0],bad.edges[0].permutation[1]]=[bad.edges[0].permutation[1],bad.edges[0].permutation[0]];assert.throws(()=>assert.deepEqual(geometricThenReading,bad));
 const badBoundary=copy(readingThenGeometric);badBoundary.entry=state.entry;assert.throws(()=>audit(badBoundary));
 rows.push({marking:sample.marking,commutesExactly:true,GsquaredIdentity:true,BsquaredIdentity:true,squareLoopIdentity:true,corners,combinedState:geometricThenReading,negativeControls:{changedCoefficientMapDetected:true,wrongEntryRejected:true}});
}
const out='research/strominger/results/deuterium-coherence-square';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'endpoint-description-square-commutes',markings:rows.length,source:input,sourceSha256:createHash('sha256').update(bytes).digest('hex'),checkerSha256:createHash('sha256').update(await readFile(new URL('./check_deuterium_coherence_square.mjs',import.meta.url))).digest('hex'),definitions:{G:'Move each labelled vertex to its paired endpoint, carrying reader/reference coefficient labels unchanged.',B:'Reverse entry/exit and edge order; invert coefficient maps; transform reader frames by M/C, i->2-i and context-aware P/E reversal.',coefficientConvention:'Fixed carried five-slot reference basis. No geometry-induced basis change is asserted.'},rows,scope:'Exact endpoint equality of decorated descriptions on 24 markings. Four corners pass local frame/face audits. Does not assert same-direction native shape eligibility, full solid isotopy, knot equivalence or a canonical geometric representation on coefficients. Clockwise and counterclockwise motion share G as endpoint action.'},null,2)+'\n');console.log(JSON.stringify({status:'endpoint-description-square-commutes',markings:rows.length,localCornerAudits:rows.length*4,negativeControls:rows.length*2}));
