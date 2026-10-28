// Fresh retained assembly reversal, including both histories and all interfaces.
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const source='research/strominger/results/window-combination-coherence/verification.json';
const prior=JSON.parse(readFileSync(source)),w=prior.coefficientFrameHolonomyExamples.find(w=>w.paths[0].word.length===3&&w.paths.every(p=>p.retainedCombinationAudit.allContactsWitnessed));
assert(w);const r=new GenerativeAssemblyRules(),retained=new Set([r.root]),histories=[];
for(const path of w.paths){let active=r.root;const packets=[active],edges=[];
 for(const kind of [...path.word,'PN','NE']){const op=r.outgoing(active).map(i=>r.operations[i]).find(o=>o.kind===kind);assert(op&&r.validateTransfer(op));edges.push(op.id);active=op.target;retained.add(active);packets.push(active);}
 histories.push({word:[...path.word,'PN','NE'],packets,edges});}
const ids=[...retained],audit=r.inspect(ids),desc=r.describe(ids);assert(audit.valid&&audit.certifiedExit&&audit.allContactsWitnessed&&audit.allPacketsCanReachExit&&audit.allCellsOnEntryExitPaths);assert.equal(audit.pendingContacts.length,0);
const incoming=['C0','M0','C1','M1','C2'],outgoing=['M0','C1','M1','C2','M2'],Q=[4,3,2,1,0];
const apply=(p,x)=>p.map(i=>x[i]),inv=p=>p.map((_,i)=>p.indexOf(i)),mul=(a,b)=>a.map(i=>b[i]);
const swap=s=>({proton:'electron',electron:'proton',neutron:'neutron'})[s],orders={proton:[2,3,1,0],neutron:[3,2,1,0],electron:[3,2,0,1]};
const packets=ids.map(id=>{const p=r.packets[id],c=r.charts[p.chart];return {id,chart:p.chart,origin:p.origin,frame:phaseFrame(c,p.origin),permutation:p.permutation,
 reference:incoming.map(n=>({role:n[0],index:p.origin+Number(n.slice(1)),vertex:c.aliases[n]})),coefficients:apply(p.permutation,['x0','x1','x2','x3','x4'])};});
const K=Math.max(...packets.flatMap(p=>[...p.frame.window,p.frame.context,...p.reference].map(o=>o.index)));
const forward={direction:1,K,packets,edges:audit.links.map(i=>r.operations[i]),entries:[r.root],exits:[...audit.exitPackets],histories,
 bodies:[...desc.bodies].map(([cell,species])=>({cell,species,geometry:r.geometry.cells[cell].geometry,vertices:r.geometry.cells[cell].vertices})),roles:[...desc.roles],contacts:desc.contacts};
function reverse(a){const J=o=>({...o,role:o.role==='M'?'C':'M',index:a.K-o.index});return {...a,direction:-a.direction,
 packets:a.packets.map(p=>{const all=[...p.frame.window,p.frame.context].map(J),v=orders[p.frame.species].map(i=>all[i]);return {...p,origin:a.K-p.origin-2,
 frame:{...p.frame,species:swap(p.frame.species),window:v.slice(0,3),context:v[3]},reference:p.reference.map(J).reverse(),coefficients:[...p.coefficients].reverse(),permutation:mul(Q,p.permutation)};}),
 // Keep kind as forward provenance; direction and species define its reverse interpretation.
 edges:a.edges.map(e=>({...e,source:e.target,target:e.source,permutation:mul(Q,mul(inv(e.permutation),Q))})),
 entries:[...a.exits],exits:[...a.entries],histories:a.histories.map(h=>({...h,word:[...h.word].reverse(),packets:[...h.packets].reverse(),edges:[...h.edges].reverse()})),
 bodies:a.bodies.map(b=>({...b,species:swap(b.species)})),roles:a.roles.map(([v,role])=>[v,role==='C'?'M':'C'])};}
function reachable(roots,edges){const s=new Set(roots),q=[...roots];for(let i=0;i<q.length;i++)for(const e of edges)if(e.source===q[i]&&!s.has(e.target)){s.add(e.target);q.push(e.target);}return s;}
function validate(a){assert.deepEqual(reverse(a),forward);const p=new Map(a.packets.map(p=>[p.id,p]));
 for(const packet of a.packets){assert.equal(auditPhaseFrame(packet.frame).status,'native-template-compatible');assert(packet.origin>=0);assert.deepEqual(packet.reference.map(o=>o.role+(o.index-packet.origin)),outgoing);}
 for(const edge of a.edges)assert.deepEqual(apply(edge.permutation,p.get(edge.source).coefficients),p.get(edge.target).coefficients);
 assert.equal(reachable(a.entries,a.edges).size,a.packets.length);assert.equal(reachable(a.exits,a.edges.map(e=>({source:e.target,target:e.source}))).size,a.packets.length);
 const roles=new Map(a.roles),species=new Map(a.bodies.map(b=>[b.cell,b.species]));
 for(const b of a.bodies){if(b.species==='electron')assert.equal(b.geometry,'proton');if(b.species==='neutron')assert.equal(b.geometry,'split');}
 for(const c of a.contacts){const pair=c.cells.map(x=>species.get(x)),kind=pair.includes('electron')?'NE':pair[0]===pair[1]?'NN':'PN';assert.equal(c.face.filter(v=>roles.get(v)==='M').length,kind==='NE'?1:2);}
}
const dual=reverse(forward);validate(dual);assert.equal(ids.length,14);assert.equal(dual.edges.length,18);assert.equal(dual.entries.length,2);
const controls=[];for(const [name,change] of [
 ['drop one entry',a=>a.entries.pop()],['drop incidental interface',a=>a.edges.pop()],
 ['erase one history',a=>a.histories.pop()],['unrebased inverse edge',a=>a.edges[0].permutation=inv(forward.edges[0].permutation)],
 ['erase complementary coefficient',a=>a.packets[0].coefficients.pop()]]){const bad=structuredClone(dual);change(bad);assert.throws(()=>validate(bad));controls.push(name);}
const provenance=['research/voevodsky/checkers/check_ramsey_reversed_assembly.mjs',source,'research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs','research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/carrier.mjs'];
const result={schema:'marici.ramsey-reversed-assembly.v1',checkerStatus:'passed',node:'admitted-reversal-overlap-coherence',forward,dual,controls,
 summary:{packets:14,interfaces:18,bodies:dual.bodies.length,dualEntries:2,dualExits:1,retainedHistories:2},
 scope:'One fresh contact-certified complete retained assembly under explicit negative-direction pullback policy. Edge kinds are retained forward provenance, not new forward commands. No claim of arbitrary assemblies or forward native admission.',
 source_sha256:Object.fromEntries(provenance.map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]))};
writeFileSync('research/voevodsky/results/ramsey-reversed-assembly-v1.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({status:result.checkerStatus,...result.summary,controls:controls.length}));
