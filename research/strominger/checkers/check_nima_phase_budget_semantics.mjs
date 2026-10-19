// Read-only audit of Nima's local rules; no changes to his generator or budget.
import assert from 'node:assert/strict';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules,phaseFrame} from '../../nima/generative-phase-assembly.mjs';
const files=['research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs','research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs'];
const hash=b=>createHash('sha256').update(b).digest('hex'),sourceHashes={};for(const f of files)sourceHashes[f]=hash(await readFile(f));
const r=new GenerativeAssemblyRules(),edge=(p,kind)=>{const op=r.outgoing(p).map(i=>r.operations[i]).find(o=>o.kind===kind);assert.ok(op,kind);return op;};
const pn=edge(r.root,'PN'),inverse=edge(pn.target,'inverse-PN');assert.equal(inverse.target,r.root);assert.equal(pn.phaseDelta+inverse.phaseDelta,0);
const p1=edge(r.root,'reader-phase-advance'),p2=edge(p1.target,'reader-phase-advance');
assert.equal(r.packets[p2.target].chart,r.packets[r.root].chart);assert.deepEqual(r.packets[p2.target].permutation,r.packets[r.root].permutation);assert.equal(r.packets[p2.target].origin,2);assert.notEqual(p2.target,r.root);
const n1=edge(pn.target,'reader-phase-advance'),siblings=[r.root,pn.target,p1.target,n1.target];assert.equal(r.describe(siblings).valid,true);assert.equal(Math.max(...siblings.map(i=>r.packets[i].origin)),1);assert.equal(p1.phaseDelta+n1.phaseDelta,2);
const ne=edge(pn.target,'NE'),nn=edge(pn.target,'NN-phase-advance');assert.equal(r.charts[r.packets[ne.target].chart].cell,r.charts[r.packets[nn.target].chart].cell);assert.equal(r.describe([r.root,pn.target,ne.target,nn.target]).reason,'occupied-cell-species-conflict');
assert.equal(r.outgoing(ne.target).length,0);assert.ok(r.outgoing(r.root).length>0);
const words=[];
for(let origin=0;origin<=2;origin++){
 let p=pn.target;const path=[r.root,p];for(let i=0;i<origin;i++){p=edge(p,'reader-phase-advance').target;path.push(p);}p=edge(p,'NE').target;path.push(p);
 const visits=[];for(const id of path){const packet=r.packets[id],f=phaseFrame(r.charts[packet.chart],packet.origin),w=f.window.map(o=>({label:o.role+o.index,vertex:o.vertex}));let overlap=Math.min(visits.length,w.length);while(overlap&&JSON.stringify(visits.slice(-overlap))!==JSON.stringify(w.slice(0,overlap)))overlap--;visits.push(...w.slice(overlap));}
 assert.equal(r.packets[p].origin,origin);assert.equal(visits.length,6+2*origin);words.push({origin,visits:visits.length,word:visits.map(o=>o.label).join(' ')});
}
assert.deepEqual(words.map(w=>w.word),['C0 M0 C1 M1 C1 C2','C0 M0 C1 M1 C2 M2 C2 C3','C0 M0 C1 M1 C2 M2 C3 M3 C3 C4']);
assert.ok(r.packets.length>3);assert.equal(r.inspect([r.root,pn.target,ne.target]).certifiedExit,true);
assert.throws(()=>r.validateTransfer({...pn,permutation:[0,1,2,3,4]}),/Lost a full coefficient/);
for(const f of files)assert.equal(hash(await readFile(f)),sourceHashes[f],'Source changed during audit: '+f);
await mkdir('research/strominger/results/nima-phase-budget-audit',{recursive:true});
await writeFile('research/strominger/results/nima-phase-budget-audit/verification.json',JSON.stringify({status:'pass-local-semantics-falsifiers',sourceHashes,words,zeroCostPNCycle:true,coefficientClosureDoesNotResetOrigin:true,siblingDepthNotSum:true,eagerNEUnionConflictsWithNN:true,unselectedCachedPacketsDoNotBlockExit:true,forgedCoefficientMapRejected:true,scope:'Tests of the existing local rules, not a completed phase-bounded generator, global branch sewing theorem, or source-derived choice of depth 8 versus 10.'},null,2)+'\n');
console.log('PASS phase-budget audit: visit counts 6/8/10 mean origins 0/1/2 on these paths; PN cycle is zero-grade; P+ squared does not reset origin; eager NE closure conflicts with NN; selected PNE certifies despite cached alternatives.');
