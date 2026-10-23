import assert from 'node:assert/strict';
import {writeFileSync,mkdirSync} from 'node:fs';
import {GenerativeAssemblyRules} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {makeLatticeItem} from '../../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {packetSnapshot} from '../ramsey-native-word-trace.mjs';
const fk=f=>[...f].sort().join('|'),copy=x=>structuredClone(x),ID=[0,1,2,3,4];
function perms(a){if(!a.length)return [[]];return a.flatMap((x,i)=>perms(a.filter((_,j)=>i!==j)).map(p=>[x,...p]));}
const cases=[];let transfers=0,neighbors=0;const controls=[];
for(const [origin,inverted] of [[[0,0,0,0],false],[[-1,1,0,0],false],[[2,0,0,0],true],[[1,1,0,0],true]]){
 const r=new GenerativeAssemblyRules(),owner=makeLatticeItem('tetrahedron',origin,inverted),cell=r.geometry.register(owner,owner.components[0]),vertices=r.geometry.cells[cell].vertices;
 const faces=r.geometry.cells[cell].faces.map(f=>[...f]);
 for(const f of faces){const neighbor=r.geometry.neighbor(cell,f);assert.equal(r.geometry.cells[neighbor].geometry,'split');neighbors++;}
 const groups=new Map(),frames=[];
 for(const p of perms([0,1,2,3])){
  const aliases=Object.fromEntries(['C0','M0','C1','M1'].map((n,i)=>[n,vertices[p[i]]]));
  const chart=r.completeP(cell,aliases);assert.notEqual(chart,null);const packet=r.packet(chart,0,ID);
  const outgoing=r.outgoing(packet).map(i=>r.operations[i]),pn=outgoing.find(o=>o.kind==='PN'),reader=outgoing.find(o=>o.kind==='reader-phase-advance');
  assert(pn&&reader);assert.equal(r.validateTransfer(pn),true);assert.equal(r.validateTransfer(reader),true);transfers+=2;
  const readerP=r.packets[reader.target],readerChart=r.charts[readerP.chart];
  const roles=Object.fromEntries(['C0','M0','C1','M1'].map(n=>[aliases[n],n[0]]));
  for(const name of ['C0','M0','C1','M1'])assert.equal(roles[readerChart.aliases[name]],name[0]);
  const second=r.outgoing(reader.target).map(i=>r.operations[i]).find(o=>o.kind==='PN');assert(second);assert.equal(r.validateTransfer(second),true);transfers++;
  const counts=faces.map(face=>face.filter(v=>roles[v]==='M').length);assert.deepEqual([...counts].sort(),[1,1,2,2]);
  assert.equal(pn.face.filter(v=>roles[v]==='M').length,2);assert.equal(second.face.filter(v=>roles[v]==='M').length,2);
  const groupKey=fk(Object.keys(roles).filter(v=>roles[v]==='M'));
  if(!groups.has(groupKey))groups.set(groupKey,{roles,faces:new Set(),frameCount:0});
  const g=groups.get(groupKey);g.faces.add(fk(pn.face));g.faces.add(fk(second.face));g.frameCount++;
  frames.push({aliases:r.charts[chart].aliases,packet,pn:copy(pn),reader:copy(reader),readerPN:copy(second),counts,groupKey});
 }
 assert.equal(groups.size,6);for(const g of groups.values()){assert.equal(g.frameCount,4);assert.equal(g.faces.size,2);}
 const union=new Set(frames.map(f=>fk(f.pn.face)));assert.equal(union.size,4);
 const fixed=frames[0],blocked=faces.find(f=>!new Set([fk(fixed.pn.face),fk(fixed.readerPN.face)]).has(fk(f)));
 assert(blocked);const alternate=frames.find(f=>fk(f.pn.face)===fk(blocked));assert(alternate);
 assert.equal(r.validateTransfer(alternate.pn),true);
 const joint=r.describe([fixed.packet,alternate.pn.target]);assert.equal(joint.valid,false);assert.equal(joint.reason,'global-CM-role-conflict');
 const corrupt=copy(fixed.pn);corrupt.face=[...blocked];assert.throws(()=>r.validateTransfer(corrupt));controls.push('wrong PN face rejected');
 assert.notEqual(fixed.groupKey,alternate.groupKey);controls.push('source-valid per-face map rejected by global-role sewing');
 assert.throws(()=>assert.equal(groups.get(fixed.groupKey).faces.size,4));controls.push('coherent two-face coverage not promoted to four');
 cases.push({origin,inverted,vertices,faces,groups:[...groups].map(([key,g])=>({key,roles:g.roles,faces:[...g.faces],frameCount:g.frameCount})),frames,
  counterexample:{source:packetSnapshot(r,fixed.packet),sourceOperation:fixed.pn,blockedFace:blocked,
   alternativeSource:packetSnapshot(r,alternate.packet),alternativeOperation:alternate.pn,alternativeTarget:packetSnapshot(r,alternate.pn.target),joint}});
}
const dir=new URL('../fixtures/ramsey-single-frame-faces/',import.meta.url);mkdirSync(dir,{recursive:true});
const header=name=>`{-# OPTIONS --safe --cubical --guardedness #-}\nmodule ${name} where\nopen import Cubical.Foundations.Prelude\nopen import RamseySingleFrameFaces\n`;
writeFileSync(new URL('RamseySingleFrameBadAllFaces.agda',dir),header('RamseySingleFrameBadAllFaces')+`bad : (v : Vertex) → Eligible v
bad c0 = refl
bad c1 = refl
bad m0 = refl
bad m1 = refl
`);
writeFileSync(new URL('RamseySingleFrameBadRoleChange.agda',dir),header('RamseySingleFrameBadRoleChange')+`swap : Vertex → Vertex
swap c0 = m0
swap m0 = c0
swap c1 = c1
swap m1 = m1
bad : M-role (swap c0) ≡ M-role c0
bad = refl
`);
writeFileSync(new URL('../results/ramsey-single-frame-faces-input-v1.json',import.meta.url),JSON.stringify({cases,transfers,neighbors,controls,
 singleRoleFrameAllFourFacesRefuted:true,allPerFaceChartsUnavailable:false,spaceAdmissionRefuted:false,WGChartTaskPackageRefuted:false,rootResolved:false},null,2)+'\n');
console.log(JSON.stringify({cases:cases.length,frames:cases.reduce((n,c)=>n+c.frames.length,0),coherentGroups:24,transfers,neighbors,controls:controls.length}));
