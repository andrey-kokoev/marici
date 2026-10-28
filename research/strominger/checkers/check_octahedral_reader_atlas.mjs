import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const specPath='research/strominger/contracts/pb208-octahedral-reader-atlas-attempt.v1.json';
const prePath='research/strominger/contracts/persistent-seam-pe-conjecture-net.snapshot.rev28.json';
const output='research/strominger/results/octahedral-reader-atlas';
const checks=[];function check(n,f){f();checks.push(n);}
const key=points=>points.map(p=>Array.isArray(p)?p.join(','):p).sort().join('|');
const r=new GenerativeAssemblyRules();
const pn=r.outgoing(r.root).map(i=>r.operations[i]).find(o=>o.kind==='PN');
const p0=r.packets[pn.target],c0=r.charts[p0.chart],owner=r.geometry.cells[c0.cell].owner;
const diagonal=[c0.aliases.C1,c0.aliases.C2].sort();
const components=new Set(owner.components.map(key)),boundary=new Set(owner.faces.map(key));
const pre=JSON.parse(await fs.readFile(path.join(root,prePath),'utf8'));
check('atlas question registered before execution',()=>{
 const n=pre.conjectures.find(n=>n.id==='pb208-octahedral-reader-atlas-attempt');assert.equal(n.status,'open');assert.equal(n.registration_before_execution,true);assert.ok(n.evidence.includes(specPath));
});
check('canonical PN target belongs to the actual four-component octahedron',()=>{
 assert.equal(owner.kind,'octahedron');assert.equal(components.size,4);assert.equal(boundary.size,8);
});
const vertices=[...new Map(owner.components.flat().map(v=>[v.join(','),v])).values()];
const center=vertices[0].map((_,i)=>vertices.reduce((n,v)=>n+v[i],0)/vertices.length);
check('fixed-root C pair is an antipodal diagonal, not an octahedron boundary edge',()=>{
 const [a,b]=diagonal.map(v=>v.split(',').map(Number));assert.equal(vertices.length,6);
 assert.deepEqual(a.map((x,i)=>(x+b[i])/2),center);
 for(const f of owner.faces)assert.ok(!diagonal.every(v=>f.some(p=>p.join(',')===v)));
 for(const c of owner.components)assert.ok(diagonal.every(v=>c.some(p=>p.join(',')===v)));
});
const stateKey=p=>p.chart+':'+p.permutation.join(',');
const nodes=[{packet:pn.target,path:[r.root,pn.target],operations:[pn.id]}],seen=new Map([[stateKey(p0),0]]),edges=[],exits=[];
for(let cursor=0;cursor<nodes.length;cursor++){
 if(nodes.length>64)throw Error('Explicit atlas resource limit; no completeness claim');
 const node=nodes[cursor],p=r.packets[node.packet],c=r.charts[p.chart],ops=r.outgoing(p.id).map(i=>r.operations[i]);
 assert.equal(c.species,'neutron');assert.equal(r.describe(node.path).valid,true);
 const exit=ops.find(o=>o.kind==='NE');assert.ok(exit);r.validateTransfer(exit);
 const ec=r.geometry.cells[r.charts[r.packets[exit.target].chart].cell];
 exits.push({source:cursor,operation:exit.id,face:exit.face,external:boundary.has(key(exit.face)),targetInsideSupport:components.has(ec.key),
 selectedPathAdmission:r.describe([...new Set([...node.path,exit.target])]).valid});
 for(const op of ops.filter(o=>['NN-phase-advance','reader-phase-advance'].includes(o.kind))){
  r.validateTransfer(op);const q=r.packets[op.target],d=r.charts[q.chart];
  assert.deepEqual([d.aliases.C1,d.aliases.C2].sort(),diagonal);
  assert.equal(d.aliases.C1,c.aliases.C2);assert.equal(d.aliases.C2,c.aliases.C1);
  assert.ok(components.has(r.geometry.cells[d.cell].key));
  const k=stateKey(q);if(!seen.has(k)){seen.set(k,nodes.length);nodes.push({packet:q.id,path:[...node.path,q.id],operations:[...node.operations,op.id]});}
  const target=seen.get(k),representative=r.packets[nodes[target].packet];
  edges.push({from:cursor,to:target,operation:op.id,kind:op.kind,actualTargetPacket:q.id,actualTargetOrigin:q.origin,representativeOrigin:representative.origin,originOffset:q.origin-representative.origin});
 }
 // The native source uses origin only through translated occurrence indices.
 // Replay at an offset as a control; the all-origin argument is recorded in note.
 const shifted=r.packet(p.chart,p.origin+7,p.permutation),shiftOps=r.outgoing(shifted).map(i=>r.operations[i]);
 for(const op of ops){const t=shiftOps.find(o=>o.kind===op.kind);assert.ok(t);r.validateTransfer(t);
  const a=r.packets[op.target],b=r.packets[t.target];assert.equal(a.chart,b.chart);assert.deepEqual(a.permutation,b.permutation);assert.equal(b.origin,a.origin+7);}
}
check('finite chart/full-map quotient closes under both unchanged N-only rules',()=>{
 assert.ok(nodes.length>1&&nodes.length<64);assert.equal(edges.length,2*nodes.length);
 for(const e of edges)assert.ok(nodes[e.to]);
});
check('all representative paths retain valid occupation and all five coefficients',()=>{
 for(const n of nodes){assert.equal(r.describe(n.path).valid,true);assert.deepEqual([...r.packets[n.packet].permutation].sort(),[0,1,2,3,4]);}
});
check('every NE face contains the invariant diagonal and lies inside the support',()=>{
 for(const e of exits){assert.ok(diagonal.every(v=>e.face.includes(v)));assert.equal(e.external,false);assert.equal(e.targetInsideSupport,true);}
});
check('quotient cycles retain origin offsets rather than identifying histories',()=>{
 assert.ok(edges.some(e=>e.originOffset>0));for(const e of edges)assert.ok(e.actualTargetOrigin>=e.representativeOrigin);
});
const references=nodes.map(n=>{const p=r.packets[n.packet],c=r.charts[p.chart],face=[c.aliases.M0,c.aliases.C1,c.aliases.M1],reference=r.geometry.neighbor(c.cell,face);
 return {packet:p.id,referenceCell:reference,occupied:r.describe(n.path).bodies.has(reference)};});
check('reference-only P geometry is used without creating extra protons',()=>{
 assert.ok(references.some(x=>!x.occupied));
 for(const n of nodes)assert.equal([...r.describe(n.path).bodies.values()].filter(s=>s==='proton').length,1);
});
check('changing C-pair to a true boundary edge is outside the invariant',()=>{
 const edge=owner.faces[0].slice(0,2).map(p=>p.join(','));assert.ok(owner.faces.some(f=>edge.every(v=>f.some(p=>p.join(',')===v))));assert.notEqual(key(edge),key(diagonal));
});
const result={registration:specPath,preExecutionSnapshot:prePath,disposition:'no-external-port-under-fixed-root-N-only-rules',
 nodes,edges,exits,references,diagonal,owner:{kind:owner.kind,vertices,components:owner.components,faces:owner.faces},
 packets:r.packets,charts:r.charts,operations:r.operations,
 externalPortEstablished:false,sourceInvariantEstablished:true,absoluteHistoriesIdentified:false,
 wholeNeutronAdmissionEstablished:false,allNativeRoutesExcluded:false,
 scope:'Canonical root and its first owner octahedron; only NN and N-reader phase advances. Inverse-PN, alternate marks/subdivisions and support changes are excluded, not ruled out.'};
await fs.mkdir(path.join(root,output),{recursive:true});await fs.writeFile(path.join(root,output,'atlas.json'),JSON.stringify(result,null,2)+'\n');
const spec=JSON.parse(await fs.readFile(path.join(root,specPath),'utf8'));
const prior=JSON.parse(await fs.readFile(path.join(root,'research/strominger/results/native-reader-comparison/verification.json'),'utf8'));
for(const [p,d] of Object.entries(prior.sourceHashes))assert.equal(crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex'),d,'stale input '+p);
const inputs=[specPath,prePath,...spec.priorClues,'research/strominger/subdivision-dependence-v1.md','research/strominger/mixed-subdivision-n14-v1.md','research/strominger/native-screw-patch-v1.md',...Object.keys(prior.sourceHashes),'research/strominger/checkers/check_octahedral_reader_atlas.mjs','research/strominger/octahedral-reader-atlas-result-v1.md',output+'/atlas.json'];
const sourceHashes={};for(const p of inputs)sourceHashes[p]=crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex');
const report={status:'passed',check_count:checks.length,checks,criterionDisposition:result.disposition,readerStates:nodes.length,nativeTransitions:edges.length,exitPorts:exits.length,
 externalPorts:exits.filter(e=>e.external).length,referenceOnlyReaders:references.filter(r=>!r.occupied).length,
 externalPortEstablished:false,sourceInvariantEstablished:true,absoluteHistoriesIdentified:false,wholeNeutronAdmissionEstablished:false,allNativeRoutesExcluded:false,sourceHashes};
await fs.writeFile(path.join(root,output,'verification.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,checks:undefined,sourceHashes:undefined}));
