// Explicit reference-seam candidate: reflected occurrence charts and dual
// five-slot bases. No identification of distinct occurrences or origin reset.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {auditPhaseFrame} from '../demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const input='research/strominger/results/hydrogen-edge-attachment/verification.json',bytes=await readFile(input),samples=JSON.parse(bytes).rows;
const incoming=['C0','M0','C1','M1','C2'],outgoing=['M0','C1','M1','C2','M2'],six=['C0','M0','C1','M1','C2','M2'],Q=[4,3,2,1,0],PN=[3,1,2,0,4],NE=[0,4,2,3,1],compose=(a,b)=>b.map(i=>a[i]),inv=p=>p.map((_,i)=>p.indexOf(i)),apply=(p,x)=>p.map(i=>x[i]),swap={proton:'electron',neutron:'neutron',electron:'proton'},orders={proton:[2,3,1,0],neutron:[3,2,1,0],electron:[3,2,0,1]};
function occurrence(name,r){return {role:name[0],index:r+Number(name.slice(1))};}
function J(o,r){return {role:o.role==='C'?'M':'C',index:2*r+2-o.index};}
const localName=(o,r)=>o.role+(o.index-r),shift=(o,k)=>({...o,index:o.index+k}),conjugate=p=>compose(compose(Q,p),Q),rows=[];
assert.deepEqual(compose(Q,Q),[0,1,2,3,4]);assert.deepEqual(conjugate(inv(NE)),PN);assert.deepEqual(conjugate(inv(PN)),NE);
for(const sample of samples)for(let r=0;r<=10;r++){
 for(const name of six){const o=occurrence(name,r);assert.deepEqual(J(J(o,r),r),o);assert.deepEqual(J(shift(o,3),r+3),shift(J(o,r),3));assert.deepEqual(J(J(o,r),r+1),shift(o,2));}
 const a=sample.bodies[2].aliases;
 for(const b of sample.bodies){const ns=({proton:['C0','M0','C1','M1'],neutron:['M0','C1','M1','C2'],electron:['M1','C1','C2','M2']})[b.species],v=ns.map(n=>({...J(occurrence(n,r),r),vertex:a[n]})),t=orders[b.species].map(i=>v[i]);assert.equal(auditPhaseFrame({id:'dual',species:swap[b.species],window:t.slice(0,3),context:t[3]}).status,'native-template-compatible');}
 const induced=outgoing.map(target=>incoming.findIndex(source=>localName(J(occurrence(source,r),r),r)===target));assert.deepEqual(induced,Q);
 // Distinct symbols distinguish transported coordinates from a fabricated
 // sixth physical amplitude. No missing slot is assigned zero.
 const x=['x_C0','x_M0','x_C1','x_M1','x_C2'],y=apply(Q,x);assert.deepEqual(apply(Q,y),x);
 // Reverse traversal: E-out in the dual basis -> N -> P. The edge maps are
 // inverted first, then changed from incoming to outgoing coordinates.
 const sourceE=apply(NE,apply(PN,x)),dualStart=apply(Q,sourceE),dualN=apply(PN,dualStart),dualEnd=apply(NE,dualN);assert.deepEqual(dualN,apply(Q,apply(PN,x)));assert.deepEqual(dualEnd,apply(Q,x));
 rows.push({marking:sample.marking,origin:r,seamFrom:occurrence('C0',r),seamTo:J(occurrence('C0',r),r),dualCoefficients:Object.fromEntries(outgoing.map((n,i)=>[n,y[i]])),nativeDualPNNERecovered:true});
}
// Wrong one-period formula and fixed incoming-basis assumption must fail.
assert.notDeepEqual({role:'M',index:1},J(occurrence('C0',0),0));assert.ok(!incoming.includes(localName(J(occurrence('C0',0),0),0)));
const out='research/strominger/results/T-seam-transition';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'explicit-seam-reference-transition-passed',cases:rows.length,originBounds:[0,10],formula:'J_r(role,i)=(opposite(role),2r+2-i)',incomingReference:incoming,outgoingReference:outgoing,basisMap:Q,dualNativeMaps:{reverseNE_inDualBasis:conjugate(inv(NE)),reversePN_inDualBasis:conjugate(inv(PN))},rows,sourceSha256:createHash('sha256').update(bytes).digest('hex'),checkerSha256:createHash('sha256').update(await readFile(new URL('./check_T_seam_transition.mjs',import.meta.url))).digest('hex'),scope:'Candidate reference/chart law, not physical equality C_r=M_(r+2). Five coordinates transport bijectively between different five-slot references within the six labels; no sixth amplitude invented. Reflections are involutive at fixed r; successive centers translate indices by 2 and are not origin reset or periodic identification. All 24 markings and origins 0..10 tested; global gluing across assemblies, channel ranks and derivation of occupancy contraction remain separate. Production/viewer unchanged.'},null,2)+'\n');console.log(JSON.stringify({cases:rows.length,basisMap:Q,reverseNE:conjugate(inv(NE)),reversePN:conjugate(inv(PN))}));
