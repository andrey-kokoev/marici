import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {createWindowConstruction,windowProtocol,windowRule} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {makeLatticeItem,itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {trial} from '../demos/particle-overlap-tetrahedron/carrier.mjs';
import {walk} from '../demos/particle-overlap-tetrahedron/model.mjs';
const cellIds=new Map(lattice.cells.map((c,id)=>[itemKey(c.map(n=>lattice.nodes[n].address)),id]));
assert.deepEqual(windowProtocol,trial.bodies.map(b=>({species:b.id,nodes:b.nodes,window:b.window,continuation:b.continuation})));
const perms=a=>a.length?a.flatMap((x,i)=>perms(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const root=makeLatticeItem('tetrahedron',[0,0,0,0]);
const sub=(a,b)=>a.map((x,i)=>x-b[i]),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
function signed(face,p){const [a,b,c]=face.map(q=>q.slice(0,3));return dot(cross(sub(b,a),sub(c,a)),sub(p.slice(0,3),a));}
function verify(options={}){
 const engine=createWindowConstruction(options),initial=engine.snapshot();
 assert.equal(initial.status,'ready');assert.equal(initial.items.length,1);assert.equal(initial.exit.point,null);assert.equal(initial.entry.kind,'inner-center');
 assert.deepEqual(Object.keys(initial.bindings).sort(),['C0','C1','M0','M1']);assert.equal(initial.candidates[0].newMark,'C2');
 const prefixes=[initial];
 for(let i=0;i<2;i++){
  const before=engine.snapshot(),after=engine.step(),event=after.events.at(-1);
  assert.equal(after.committed,true);assert.equal(after.items.length,before.items.length+1);assert.deepEqual(after.items.slice(0,-1),before.items);assert.equal(after.identity,initial.identity);
  assert.equal(event.priorItemCount,before.items.length);assert.deepEqual(event.orderedFace,windowProtocol[i+1].window);
  for(const [name,p] of Object.entries(before.bindings))assert.deepEqual(after.bindings[name],p,'No shared or archived identity moves');
  const left=after.items.at(-2),right=after.items.at(-1),face=event.face;
  assert.ok(left.faces.some(f=>itemKey(f)===itemKey(face)));assert.ok(right.faces.some(f=>itemKey(f)===itemKey(face)));
  const apices=[left,right].map(b=>b.vertices.find(p=>!face.some(q=>itemKey([p])===itemKey([q]))));assert.ok(signed(face,apices[0])*signed(face,apices[1])<0);
  prefixes.push(after);
 }
 const end=engine.snapshot();assert.equal(end.status,'complete');assert.equal(end.items.length,3);assert.equal(end.events.length,2);assert.equal(end.exit.identity,initial.identity);assert.deepEqual(end.exit.point,end.items[2].center);
 assert.deepEqual(end.history,walk);assert.equal(end.history.filter(n=>n==='C1').length,2);assert.equal(Object.keys(end.bindings).length,6);assert.equal(new Set(Object.values(end.bindings).map(p=>p.join(','))).size,6);
 assert.deepEqual(end.events.map(e=>e.frameExchange),[['C0','M1'],['M0','C2']]);assert.deepEqual(end.events.map(e=>e.targetCycle),['forward','inverse']);
 const incoming=end.events[0].face.map(p=>p.join(',')),outgoing=end.events[1].face.map(p=>p.join(','));
 assert.deepEqual(new Set(incoming.filter(p=>outgoing.includes(p))),new Set(['C1','M1'].map(n=>end.bindings[n].join(','))));
 assert.deepEqual(end.items[1].window.slice(-2),end.items[2].window.slice(0,2).reverse());
 const omitted=end.items[1].nodes.filter(n=>!end.items[2].window.includes(n));assert.deepEqual(omitted,['M0']);
 assert.equal(new Set(end.items.map(s=>s.key)).size,3);
 for(const prefix of prefixes)for(const body of prefix.items){
  const [a,b,c,d]=body.vertices.map(p=>p.slice(0,3));assert.equal(Math.abs(dot(sub(b,a),cross(sub(c,a),sub(d,a)))),1);
  assert.ok(body.vertices.every(p=>p.every(Number.isInteger)&&p.reduce((a,b)=>a+b,0)===1));
 }
 assert.equal(engine.step().committed,false);assert.deepEqual(engine.snapshot().items,end.items);
 return end;
}
const result=verify();assert.deepEqual(result.mode,{branch:'negative',phaseExponent:0});assert.deepEqual(result.events[0].modeAfter,{branch:'positive',phaseExponent:1});
for(const branch of ['common','negative']){const end=verify({branch});assert.deepEqual(end.mode,{branch:branch==='common'?'common':'positive',phaseExponent:0});}
// Check every supplied initial marking on the fixed ambient subdivision.
// This is not a claim that the subdivision is invariant under every rotation.
for(const p of perms([0,1,2,3])){
 const bindings=Object.fromEntries(windowProtocol[0].nodes.map((n,i)=>[n,root.vertices[p[i]]]));const end=verify({bindings});
 assert.ok(end.items.every(s=>cellIds.has(s.key)),'All three bodies are actual existing lattice cells');
}
const shift=[1,-1,0,0],translated=verify({seed:makeLatticeItem('tetrahedron',shift)});
for(const [name,p] of Object.entries(result.bindings))assert.deepEqual(translated.bindings[name],p.map((x,i)=>x+shift[i]));
assert.throws(()=>createWindowConstruction({seed:makeLatticeItem('octahedron',[-1,0,0,0])}));
assert.throws(()=>createWindowConstruction({bindings:{C0:root.vertices[0],M0:root.vertices[0],C1:root.vertices[2],M1:root.vertices[3]}}));
assert.throws(()=>createWindowConstruction({branch:'unknown'}));
const protectedState=createWindowConstruction(),copy=protectedState.snapshot();copy.bindings.C1[0]=999;assert.equal(protectedState.step().status,'ready');
const out='research/strominger/results/window-construction';await mkdir(out,{recursive:true});
await writeFile(out+'/verification.json',JSON.stringify({status:'pass',rule:windowRule,sourceWindows:windowProtocol,steps:result.events,defaultCellIds:result.items.map(s=>cellIds.get(s.key)),bindings:result.bindings,retainedHistory:result.history,terminalMode:result.mode,seedMarkingsChecked:24,allThreeModesChecked:true,existingLatticeCells:true,positiveUnitVolumes:true,requiredNeutronElectronFace:['M1','C1','C2'],preservedEdge:['C1','M1'],legacyPbRebound:false},null,2)+'\n');
console.log('PASS retained-window construction: P → N → E, one actual lattice cell per step; exact MCC face, reversed C1/M1 edge, full mark/history retention and symbolic branch/phase transfer');
