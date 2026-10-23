import assert from 'node:assert/strict';
import {writeFileSync,mkdirSync} from 'node:fs';
import {GenerativeAssemblyRules} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {packetSnapshot} from '../ramsey-native-word-trace.mjs';
const fk=f=>[...f].sort().join('|'),copy=x=>structuredClone(x),names=['C0','M0','C1','M1'];
function permutations(a){if(!a.length)return [[]];return a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p]));}
const r=new GenerativeAssemblyRules(),cell=r.charts[r.packets[r.root].chart].cell,body=r.geometry.cells[cell].vertices,faces=r.geometry.cells[cell].faces,frames=[];let validatedTransfers=0;
for(const p of permutations([0,1,2,3])){
 const aliases=Object.fromEntries(names.map((n,i)=>[n,body[p[i]]]));const chart=r.completeP(cell,aliases);assert.notEqual(chart,null);
 const packet=r.packet(chart,0,[0,1,2,3,4]),ops=r.outgoing(packet).map(i=>r.operations[i]),pn=ops.find(o=>o.kind==='PN'),reader=ops.find(o=>o.kind==='reader-phase-advance');
 const readerPN=r.outgoing(reader.target).map(i=>r.operations[i]).find(o=>o.kind==='PN');
 for(const op of [pn,reader,readerPN]){assert.equal(r.validateTransfer(op),true);validatedTransfers++;}
 const role=Object.fromEntries(names.map(n=>[aliases[n],n[0]])),eligible=faces.filter(f=>f.filter(v=>role[v]==='M').length===2).map(fk);
 assert.deepEqual([...new Set([fk(pn.face),fk(readerPN.face)])].sort(),[...eligible].sort());
 frames.push({p,aliases:r.charts[chart].aliases,role,eligible,packet,pn:copy(pn),readerPN:copy(readerPN)});
}
const inv=p=>p.map((_,i)=>p.indexOf(i)),change=(f,g)=>f.p.map(v=>inv(g.p)[v]);
let pairCells=0,changedRolePairs=0,oneLost=0,twoLost=0,sameFaceFiveReferenceChangedPairs=0;
for(const f of frames)for(const g of frames){
 const sigma=change(f,g);for(let i=0;i<4;i++)assert.equal(f.p[i],g.p[sigma[i]]);pairCells++;
 const lost=f.eligible.filter(s=>!g.eligible.includes(s));
 const rolesDiffer=body.some(v=>f.role[v]!==g.role[v]);
 if(rolesDiffer){changedRolePairs++;assert(lost.length>0);if(lost.length===1)oneLost++;else{assert.equal(lost.length,2);twoLost++;}}
 else assert.equal(lost.length,0);
 if(fk(f.pn.face)===fk(g.pn.face)){
  assert.deepEqual(Object.values(f.aliases).sort(),Object.values(g.aliases).sort());
  if(rolesDiffer)sameFaceFiveReferenceChangedPairs++;
 }
}
let cocycles=0,fullCocycles=0;
for(const f of frames)for(const g of frames)for(const h of frames){
 const fg=change(f,g),gh=change(g,h),fh=change(f,h);assert.deepEqual(fg.map(i=>gh[i]),fh);cocycles++;
 if(f.aliases.C0===g.aliases.C0&&g.aliases.C0===h.aliases.C0){assert.equal(f.aliases.C2,g.aliases.C2);assert.equal(g.aliases.C2,h.aliases.C2);fullCocycles++;}
}
const source=frames.find(f=>f.p.join(',')==='0,1,2,3'),target=frames.find(f=>f.p.join(',')==='0,2,1,3');assert(source&&target);
assert.equal(fk(source.pn.face),fk(target.pn.face));assert.deepEqual(Object.values(source.aliases).sort(),Object.values(target.aliases).sort());
const lost=source.eligible.find(f=>!target.eligible.includes(f)),shared=source.eligible.filter(f=>target.eligible.includes(f));assert(lost&&shared.length===1);
const lostFace=lost.split('|');assert.equal(lostFace.filter(v=>source.role[v]==='M').length,2);assert.equal(lostFace.filter(v=>target.role[v]==='M').length,1);
const controls=[];function rejected(n,f){assert.throws(f);controls.push(n);}
rejected('total domain transition over fixed faces',()=>source.eligible.forEach(f=>assert(target.eligible.includes(f))));
const bad=change(source,target);bad[0]=bad[1];rejected('wrong geometric permutation',()=>bad.forEach((j,i)=>assert.equal(source.p[i],target.p[j])));
rejected('body-only map treated as full reference map',()=>assert.equal(change(source,target).length,5));
rejected('role swap called role preserving',()=>body.forEach(v=>assert.equal(source.role[v],target.role[v])));
rejected('partial overlap adapter extended to lost face',()=>assert(shared.includes(lost)));
const dir=new URL('../fixtures/ramsey-role-domain-transport/',import.meta.url);mkdirSync(dir,{recursive:true});
const header=name=>`{-# OPTIONS --safe --cubical --guardedness #-}\nmodule ${name} where\nopen import Cubical.Foundations.Prelude\nopen import RamseySingleFrameFaces\nopen import RamseyRoleDomainTransport\n`;
writeFileSync(new URL('RamseyRoleDomainBadTotal.agda',dir),header('RamseyRoleDomainBadTotal')+`bad : TargetEligible c1
bad = refl
`);
writeFileSync(new URL('RamseyRoleDomainBadGauge.agda',dir),header('RamseyRoleDomainBadGauge')+`bad : M-role (swap-role m0) ≡ M-role m0
bad = refl
`);
const payload={frames,pairCells,changedRolePairs,oneLost,twoLost,sameFaceFiveReferenceChangedPairs,cocycles,fullCocycles,validatedTransfers,controls,
 counterexample:{source:packetSnapshot(r,source.packet),sourcePN:source.pn,sourceReaderPN:source.readerPN,
 target:packetSnapshot(r,target.packet),targetPN:target.pn,targetReaderPN:target.readerPN,
 sigma:change(source,target),lostFace,sharedFaces:shared.map(s=>s.split('|'))},
 totalFixedFacePNDomainTransportRefuted:true,geometricCocycleFailed:false,allPartialTransitionsRefuted:false,faceChartDescentRefuted:false,WGTaskPackageRefuted:false,rootResolved:false};
writeFileSync(new URL('../results/ramsey-role-domain-transport-input-v1.json',import.meta.url),JSON.stringify(payload,null,2)+'\n');
console.log(JSON.stringify({pairCells,changedRolePairs,oneLost,twoLost,sameFaceFiveReferenceChangedPairs,cocycles,fullCocycles,validatedTransfers,controls:controls.length}));
