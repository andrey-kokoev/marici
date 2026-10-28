// Fresh whole-certificate direction reversal with Q-rebased references.
// Experimental pullback comparison; no native outgoing E rule is installed.
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {makeLatticeItem} from '../../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const incoming=['C0','M0','C1','M1','C2'],outgoing=['M0','C1','M1','C2','M2'],Q=[4,3,2,1,0];
const swap=s=>({proton:'electron',electron:'proton',neutron:'neutron'})[s];
const orders={proton:[2,3,1,0],neutron:[3,2,1,0],electron:[3,2,0,1]};
const inverse=p=>p.map((_,i)=>p.indexOf(i));
const multiply=(a,b)=>a.map(i=>b[i]); // matrix permutation a after b
const conjugate=p=>multiply(Q,multiply(p,Q));
const apply=(p,x)=>p.map(i=>x[i]);
function reverse(a){
 const J=o=>({...o,role:o.role==='C'?'M':'C',index:a.K-o.index});
 return {...a,direction:-a.direction,
   packets:a.packets.map(p=>{const all=[...p.frame.window,p.frame.context].map(J),v=orders[p.frame.species].map(i=>all[i]);return {...p,
     origin:a.K-p.origin-2,
     frame:{...p.frame,species:swap(p.frame.species),window:v.slice(0,3),context:v[3]},
     reference:p.reference.map(J).reverse(),coefficients:[...p.coefficients].reverse()};}),
   bodies:a.bodies.map(b=>({...b,species:swap(b.species)})),
   roles:a.roles.map(([v,r])=>[v,r==='C'?'M':'C']),
   edges:a.edges.map(e=>({...e,source:e.target,target:e.source,kind:({PN:'NE',NE:'PN'})[e.kind],permutation:conjugate(inverse(e.permutation))})),
   entries:[...a.exits],exits:[...a.entries]};
}
function reachable(roots,edges){const found=new Set(roots),q=[...roots];for(let i=0;i<q.length;i++)for(const e of edges)if(e.source===q[i]&&!found.has(e.target)){found.add(e.target);q.push(e.target);}return found;}
function validate(dual,forward){
 assert.equal(dual.direction,-1);assert.deepEqual(reverse(dual),forward);
 const packets=new Map(dual.packets.map(p=>[p.id,p]));
 for(const p of dual.packets){
   assert.equal(auditPhaseFrame(p.frame).status,'native-template-compatible');
   assert.deepEqual(p.reference.map(o=>o.role+(o.index-p.origin)),outgoing);
   assert.equal(new Set(p.reference.map(o=>o.vertex)).size,5);
 }
 for(const e of dual.edges){assert.deepEqual(apply(e.permutation,packets.get(e.source).coefficients),packets.get(e.target).coefficients);}
 for(const b of dual.bodies){if(b.species==='electron')assert.equal(b.geometry,'proton');if(b.species==='neutron')assert.equal(b.geometry,'split');}
 assert.equal(reachable(dual.entries,dual.edges).size,dual.packets.length);
 assert.equal(reachable(dual.exits,dual.edges.map(e=>({source:e.target,target:e.source}))).size,dual.packets.length);
 return true;
}
const permutations=a=>a.length?a.flatMap((v,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[v,...p])):[[]];
const seed=makeLatticeItem('tetrahedron',[0,0,0,0]),rows=[];
for(const marking of permutations([0,1,2,3])){
 const rules=new GenerativeAssemblyRules({seedBindings:Object.fromEntries(incoming.slice(0,4).map((n,i)=>[n,seed.vertices[marking[i]].join(',')]))});
 const find=(id,k)=>rules.outgoing(id).map(i=>rules.operations[i]).find(e=>e.kind===k);
 const pn=find(rules.root,'PN'),ne=find(pn.target,'NE');assert(rules.validateTransfer(pn)&&rules.validateTransfer(ne));
 const ids=[rules.root,pn.target,ne.target],desc=rules.describe(ids);assert.equal(desc.valid,true);
 const packets=ids.map(id=>{const p=rules.packets[id],c=rules.charts[p.chart];return {id,origin:p.origin,
   frame:phaseFrame(c,p.origin),reference:incoming.map(n=>({role:n[0],index:p.origin+Number(n.slice(1)),vertex:c.aliases[n]})),
   coefficients:apply(p.permutation,['x0','x1','x2','x3','x4']),
   // Physical field carrier is retained, not identified by the new species name.
   retainedFieldType:c.species==='proton'?'P36-plus-E8':'N36-plus-E8'};});
 const forward={direction:1,K:2,packets,
   bodies:[...desc.bodies].map(([cell,species])=>({cell,species,geometry:rules.geometry.cells[cell].geometry,vertices:rules.geometry.cells[cell].vertices})),
   roles:[...desc.roles],contacts:desc.contacts,
   edges:[pn,ne].map(e=>({source:e.source,target:e.target,kind:e.kind,permutation:e.permutation,face:e.face})),entries:[rules.root],exits:[ne.target]};
 const dual=reverse(forward);assert(validate(dual,forward));assert.deepEqual(reverse(dual),forward);
 // Context provenance: dual M2 is old C0 at the same vertex, not old M2.
 for(let i=0;i<3;i++)assert.equal(dual.packets[i].reference[4].vertex,forward.packets[i].reference[0].vertex);
 const echart=rules.charts[rules.packets[ne.target].chart];assert.notEqual(echart.aliases.C0,echart.aliases.M2);
 const dualOldP=dual.packets[0];assert.equal(dualOldP.frame.species,'electron');
 const indices=dualOldP.frame.window.map(o=>dualOldP.reference.findIndex(r=>r.role===o.role&&r.index===o.index&&r.vertex===o.vertex));
 assert.deepEqual(indices,[2,1,3]);assert.equal(dualOldP.frame.context.vertex,dualOldP.reference[4].vertex);
 // Audit transported contacts without keeping the old operation name as authority.
 const roles=new Map(dual.roles),species=new Map(dual.bodies.map(b=>[b.cell,b.species]));
 for(const c of dual.contacts){const pair=c.cells.map(x=>species.get(x)),kind=pair.includes('electron')?'NE':'PN';assert.equal(c.face.filter(v=>roles.get(v)==='M').length,kind==='NE'?1:2);}
 const bads=[];
 const reject=(name,mutate)=>{const bad=structuredClone(dual);mutate(bad);assert.throws(()=>validate(bad,forward));bads.push(name);};
 reject('missing entry',a=>a.entries=[]);
 reject('missing exit',a=>a.exits=[]);
 reject('unrebased inverse edge',a=>a.edges[0].permutation=inverse(forward.edges[0].permutation));
 reject('old M2 substituted for dual M2',a=>a.packets[2].reference[4].vertex=echart.aliases.M2);
 reject('dropped reference coefficient',a=>a.packets[0].coefficients.pop());
 reject('frozen boundary direction',a=>a.entries=[...forward.entries]);
 rows.push({marking,forward,dual,dualEWindowReferenceSlots:indices,controls:bads,originalElectronOutgoingCount:rules.outgoing(ne.target).length});
}
assert.equal(rows.length,24);assert(rows.every(r=>r.originalElectronOutgoingCount===0));
const sources=['research/voevodsky/checkers/check_ramsey_complete_reversed_reference.mjs','research/nima/generative-phase-assembly.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/carrier.mjs'];
const result={schema:'marici.ramsey-complete-reversed-reference.v1',checkerStatus:'passed',node:'T-seam-based-port-readout-binding',
 scientificStatus:'complete_direction_reversed_PNE_certificates_pass',freshMarkings:24,referenceBasis:outgoing,basisMap:Q,rows,
 scope:'Fresh complete three-packet PNE certificates with all contacts and boundaries. Experimental pullback comparison, not an added forward generator rule or universal assembly theorem. Physical field carrier types are retained, not inferred from dual species names.',
 source_sha256:Object.fromEntries(sources.map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]))};
writeFileSync('research/voevodsky/results/ramsey-complete-reversed-reference-v1.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.checkerStatus,markings:24,wholeCertificateDoubleReversal:true,dualEWindowSlots:[2,1,3],controlsPerCase:6}));
