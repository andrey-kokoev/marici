// Coherence of the explicit PE rewrite with carried-coordinate G and boundary
// reversal B. Compare full decorated states on all faces of the rewrite cube.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const copy=structuredClone,inv=p=>p.map((_,i)=>p.indexOf(i)),product=(a,b)=>b.map(i=>a[i]),hash=b=>createHash('sha256').update(b).digest('hex');
const out='research/strominger/results/contraction-coherence-cube',sourceHashes={},load=async f=>{const b=await readFile(f);sourceHashes[f]=hash(b);return JSON.parse(b);};
const independent=await load('research/strominger/results/terminal-pe-independent/verification.json');assert.equal(independent.status,'independent-python-check-passed');for(const [f,h] of Object.entries(independent.sourceHashes))assert.equal(hash(await readFile(f)),h);
const probe=await load('research/strominger/results/terminal-pe-probe/verification.json'),hydrogen=await load('research/strominger/results/hydrogen-edge-attachment/verification.json');
const swap={proton:'electron',electron:'proton',neutron:'neutron'},orders={proton:[2,3,1,0],neutron:[3,2,1,0],electron:[3,2,0,1]},names={proton:['C0','M0','C1','M1'],neutron:['M0','C1','M1','C2'],electron:['M1','C1','C2','M2']},results=[];
function check(label,packets,charts,selected,shortcut,factors){
 const ps=new Map(packets.map(p=>[p.id,p])),cs=new Map(charts.map(c=>[Number(String(c.id).replace('chart-','')),c])),chart=p=>cs.get(ps.get(p).chart),cell=p=>chart(p).cell;
 const [pn,ne]=factors;assert.equal(pn.target,ne.source);const p=pn.source,n=pn.target,e=ne.target;assert.equal(p,shortcut.source);assert.equal(e,shortcut.target);
 const occupied=[...new Set(selected.map(cell))].sort((a,b)=>a-b);assert.ok(!occupied.includes(cell(n)));
 const a=chart(e).aliases,partner={};for(const [x,y] of [['C0','M2'],['M0','C2'],['C1','M1']]){partner[a[x]]=a[y];partner[a[y]]=a[x];}
 const allVertices=[...new Set(charts.flatMap(c=>Object.values(c.aliases)))].sort(),position=Object.fromEntries(allVertices.map(v=>[v,v.split(',').map(Number)]));
 const K=Math.max(...[p,n,e].flatMap(i=>names[chart(i).species].map(k=>Number(k.slice(1))+ps.get(i).origin)));
 const frames=[p,n,e].map(i=>{const c=chart(i),v=names[c.species].map(k=>({vertex:c.aliases[k],role:k[0],index:Number(k.slice(1))+ps.get(i).origin}));return {id:i,species:c.species,window:v.slice(0,3),context:v[3]};});
 // Native edges in the selected diagram are recorded independently of the
 // experimental path. Boundary guards use these exact arrows, not display order.
 const env=selected.map(i=>({id:i,species:chart(i).species,body:cell(i)}));
 const originalNative=check.native.filter(o=>selected.includes(o.source)&&selected.includes(o.target)).map(o=>({source:o.source,target:o.target}));
 const initial={direction:1,K,position,frames,word:[pn,ne].map(o=>({source:o.source,target:o.target,kind:o.kind,permutation:o.permutation})),support:[cell(p),cell(n),cell(e)].sort((a,b)=>a-b),referenceSupport:[cell(p),cell(n),cell(e)].sort((a,b)=>a-b),boundary:{entry:p,exit:e},context:{occupied,native:originalNative,readers:env},contracted:false};
 function G(s){const t=copy(s);t.position=Object.fromEntries(allVertices.map(v=>[v,copy(s.position[partner[v]??v])]));return t;}
 function B(s){const t=copy(s);t.direction=-s.direction;t.frames=s.frames.map(f=>{const v=[...f.window,f.context].map(o=>({...o,role:o.role==='M'?'C':'M',index:s.K-o.index})),q=orders[f.species].map(i=>v[i]);return {...f,species:swap[f.species],window:q.slice(0,3),context:q[3]};}).reverse();t.word=s.word.map(o=>({...o,source:o.target,target:o.source,kind:o.kind==='PN'?'NE':o.kind==='NE'?'PN':o.kind,permutation:inv(o.permutation)})).reverse();t.boundary={entry:s.boundary.exit,exit:s.boundary.entry};t.context.native=s.context.native.map(o=>({source:o.target,target:o.source}));t.context.readers=s.context.readers.map(r=>({...r,species:swap[r.species]}));return t;}
 function C(s){
  assert.equal(s.contracted,false);assert.equal(s.word.length,2);assert.equal(s.word[0].target,s.word[1].source);assert.equal(s.word[0].target,n);assert.ok(!s.context.occupied.includes(cell(n)));
  const port=s.direction===1?'source':'target';for(const end of [s.boundary.entry,s.boundary.exit])assert.ok(!s.context.native.some(o=>o[port]===end),'Transported boundary guard failed');
  assert.equal(ps.get(p).origin,ps.get(n).origin);assert.equal(ps.get(n).origin,ps.get(e).origin);
  const f=s.frames[0],l=s.frames.at(-1),left=[...f.window,f.context].map(o=>o.vertex),right=[...l.window,l.context].map(o=>o.vertex),edge=left.filter(v=>right.includes(v));assert.equal(edge.length,2);
  assert.ok(edge.every(v=>Object.hasOwn(s.position,v)));assert.equal(new Set(Object.values(s.position).map(v=>v.join(','))).size,allVertices.length);
  const t=copy(s);t.word=[{source:s.boundary.entry,target:s.boundary.exit,kind:'PE-contraction',permutation:product(s.word[0].permutation,s.word[1].permutation)}];t.support=s.support.filter(c=>c!==cell(n));t.contracted=true;return t;
 }
 const lower=C(initial);assert.deepEqual(lower.word[0].permutation,shortcut.permutation);
 assert.deepEqual(C(G(initial)),G(lower));assert.deepEqual(C(B(initial)),B(lower));assert.deepEqual(C(G(B(initial))),G(C(B(initial))));assert.deepEqual(C(B(G(initial))),B(C(G(initial))));assert.deepEqual(C(B(G(initial))),B(G(lower)));assert.deepEqual(B(G(initial)),G(B(initial)));assert.deepEqual(B(G(lower)),G(B(lower)));
 assert.deepEqual(B(B(initial)),initial);assert.deepEqual(G(G(initial)),initial);assert.deepEqual(B(B(lower)),lower);assert.deepEqual(G(G(lower)),lower);
 const badVacancy=copy(initial);badVacancy.context.occupied.push(cell(n));assert.throws(()=>C(badVacancy));
 const badBoundary=copy(B(initial));badBoundary.context.native.push({source:n,target:badBoundary.boundary.entry});assert.throws(()=>C(badBoundary));
 const badMap=copy(G(lower));[badMap.word[0].permutation[0],badMap.word[0].permutation[1]]=[badMap.word[0].permutation[1],badMap.word[0].permutation[0]];assert.throws(()=>assert.deepEqual(C(G(initial)),badMap));
 results.push({label,source:p,target:e,referenceNeutronCell:cell(n),allSixCubeFacesCommute:true,bothInvolutionsBeforeAndAfter:true,grade:0,permutation:lower.word[0].permutation,occupiedSupportBefore:initial.support,occupiedSupportAfter:lower.support,referenceSupport:lower.referenceSupport,negativeControls:3});
}
for(const h of hydrogen.rows){const charts=h.bodies.map((b,i)=>({id:'chart-'+h.packets[i].chart,cell:b.cell,species:b.species,aliases:b.aliases})),[p,n,e]=h.packets;check.native=h.operations;check('H1-'+h.marking.join(''),h.packets,charts,[p.id,e.id],{source:p.id,target:e.id,permutation:h.compositePermutation},h.operations);}
for(const isotope of ['n15','ne22']){
 const base=`research/strominger/results/reference-${isotope}-search`,summary=await load(base+'/verification.json'),row=summary.rows.find(r=>r.witnessFile),w=(await load(base+'/'+row.witnessFile)).witness;check.native=w.operations;
 for(const d of probe.deletions.filter(d=>d.sourceIsotope===isotope&&d.variants['electron-and-proton-record-terminal'].passesHypotheticalChecks))for(const s of d.shortcuts.filter(s=>s.recordTerminal))check(isotope+'-delete-'+d.deletedNeutron.cell,w.packets,w.charts,d.selectedPackets,s,s.nativeFactors.map(i=>w.operations.find(o=>o.id===i)));
}
sourceHashes['research/strominger/checkers/check_contraction_coherence_cube.mjs']=hash(await readFile(new URL('./check_contraction_coherence_cube.mjs',import.meta.url)));
await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'carried-reference-contraction-cubes-pass',cases:results.length,commutingFaces:results.length*6,negativeControls:results.length*3,results,sourceHashes,scope:'G is a fixed labelled coordinate permutation carrying coefficient bases unchanged. B is the context-aware reader involution with inverted maps and reversed selected native arrows. C removes only occupied N support, retaining reference data. Backward guards are incoming-arrow counterparts of forward outgoing-arrow guards. Finite endpoint rewrite consistency, not path isotopy, field sewing, canonical geometric coefficient action or production admission.'},null,2)+'\n');console.log(JSON.stringify({status:'pass',cases:results.length,commutingFaces:results.length*6,negativeControls:results.length*3}));
