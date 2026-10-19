// Boundary reversal on fixed deuterium geometry; no moving vertices.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {phaseFrame} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseCombination} from '../demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const input='research/strominger/results/hydrogen-edge-attachment/verification.json',bytes=await readFile(input),samples=JSON.parse(bytes).rows,inv=p=>p.map((_,i)=>p.indexOf(i)),apply=(p,x)=>p.map(i=>x[i]),compose=(a,b)=>b.map(i=>a[i]),rows=[];
const orders={proton:[2,3,1,0],neutron:[3,2,1,0],electron:[3,2,0,1]},swapped={proton:'electron',neutron:'neutron',electron:'proton'};
function reversedFrame(f){const v=[...f.window,f.context].map(o=>({...o,role:o.role==='M'?'C':'M',index:2-o.index})),q=orders[f.species].map(i=>v[i]);return {...f,species:swapped[f.species],window:q.slice(0,3),context:q[3]};}
for(const sample of samples){
 const [p,n,e]=sample.packets,[pn,ne]=sample.operations,charts=sample.bodies.map((b,i)=>({id:String(sample.packets[i].chart),species:b.species,aliases:b.aliases})),frames=charts.map((c,i)=>phaseFrame(c,sample.packets[i].origin)),geometryBefore=JSON.stringify(sample.bodies);
 const value=[11,23,37,41,59],afterPN=apply(pn.permutation,value),afterNE=apply(ne.permutation,afterPN),backToN=apply(inv(ne.permutation),afterNE),backToP=apply(inv(pn.permutation),backToN);
 assert.deepEqual(afterNE,apply(e.permutation,value));assert.deepEqual(backToN,afterPN);assert.deepEqual(backToP,value);
 const total=compose(pn.permutation,ne.permutation),backTotal=compose(inv(ne.permutation),inv(pn.permutation));assert.deepEqual(backTotal,inv(total));assert.deepEqual(total,backTotal);
 const reverseEdges=[{source:e.id,target:n.id,permutation:inv(ne.permutation),face:ne.face},{source:n.id,target:p.id,permutation:inv(pn.permutation),face:pn.face}];
 let current=e.id;const seen=[current];for(const edge of reverseEdges){assert.equal(edge.source,current);current=edge.target;seen.push(current);}assert.equal(current,p.id);assert.equal(new Set(seen).size,3);
 const [rp,rn,re]=[frames[2],frames[1],frames[0]].map(reversedFrame);
 const audit=auditPhaseCombination([rp,rn,re],[{from:rp.id,to:rn.id,kind:'PN',identification:'same-occurrence',vertices:ne.face},{from:rn.id,to:re.id,kind:'NE',identification:'same-occurrence',vertices:pn.face}]);assert.equal(audit.status,'native-phase-compatible');
 for(const f of frames)assert.deepEqual(reversedFrame(reversedFrame(f)),f);
 assert.equal(JSON.stringify(sample.bodies),geometryBefore);
 rows.push({marking:sample.marking,forwardBoundary:{entry:p.id,exit:e.id},reverseBoundary:{entry:e.id,exit:p.id},fixedBodyCoordinates:sample.bodies.map(b=>({species:b.species,vertices:b.vertices})),forwardReaderOrder:['P','N','E'],reverseReaderOrder:['old E','old N','old P'],reverseEdges,coefficientTrace:{forward:[value,afterPN,afterNE],backward:[afterNE,backToN,backToP]},totalPermutation:total,inverseTotalPermutation:backTotal,selfInverseTotal:true,relabelledReverseFrames:[rp,rn,re],reverseFrameAudit:audit.status});
}
const out='research/strominger/results/deuterium-reverse-reading';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'fixed-geometry-reverse-reading-passed',markings:rows.length,source:input,sourceSha256:createHash('sha256').update(bytes).digest('hex'),checkerSha256:createHash('sha256').update(await readFile(new URL('./probe_deuterium_reverse_reading.mjs',import.meta.url))).digest('hex'),rows,scope:'Swap entry/exit and reverse the two face maps on unchanged deuterium coordinates. Inverse coefficient maps plus context-aware M/C/index/P-E relabelling pass native local frame audit. Original generator does not thereby acquire electron-outgoing operations; this is the reversed reader convention, not a new forward production rule. Total map is involutive, so direction must be retained by ordered path/boundary labels.'},null,2)+'\n');console.log(JSON.stringify({status:'passed',markings:rows.length,totalPermutation:rows[0].totalPermutation,trace:rows[0].coefficientTrace,reverseFrameAudit:rows[0].reverseFrameAudit}));
