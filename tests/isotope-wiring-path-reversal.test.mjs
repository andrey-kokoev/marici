import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {auditPathReversal,auditDefinitionPathReversal} from '../examples/isotope-wiring/core/path-reversal.mjs';

// Synthetic contract examples, NOT an extraction of the isotope drawings or
// an assertion that these chains are the native NNPE/NNNN generators.
function example(){
 const vertices=[],edges=[],paths=[];
 for(const word of ['NNPE','NNNN']){
  const ids=[...word].map((role,i)=>{const id=`${word}:${i}`;vertices.push({id,role});return id;});
  const steps=[];
  for(let i=0;i<3;i++){
   const id=`${word}:e${i}`,reverse=id+'^-1',support=`${word}:support${i}`,kind='incidence';
   edges.push({id,from:ids[i],to:ids[i+1],reverse,support,kind},{id:reverse,from:ids[i+1],to:ids[i],reverse:id,support,kind});steps.push(id);
  }
  paths.push({id:word,generator:word,edges:steps});
 }
 return {vertices,edges,paths};
}
const codes=r=>r.paths.flatMap(p=>p.issues.map(i=>i.code));
test('explicit reverse topology exists, composes, preserves roles/supports and is involutive',()=>{
 const t=example(),before=structuredClone(t),r=auditPathReversal(t);assert.equal(r.status,'verified');assert.deepEqual(t,before);
 for(const p of r.paths)assert.deepEqual(p.reverseVertices,[...p.forwardVertices].reverse());
 const reversed=structuredClone(t);reversed.paths.forEach((p,i)=>{p.edges=r.paths[i].reverseEdges;});
 const rr=auditPathReversal(reversed);assert.equal(rr.status,'verified');rr.paths.forEach((p,i)=>assert.deepEqual(p.reverseEdges,t.paths[i].edges));
});
test('removing an inverse fails even though the undirected outline is unchanged',()=>{
 const t=example();t.edges=t.edges.filter(e=>e.id!=='NNPE:e1^-1');const r=auditPathReversal(t);assert.equal(r.status,'refuted');assert(codes(r).includes('missing-explicit-reverse'));
});
test('a return connection on a different support does not substitute for the reverse',()=>{
 const t=example();t.edges.find(e=>e.id==='NNPE:e0^-1').support='another-support';assert(codes(auditPathReversal(t)).includes('reverse-role-or-support-mismatch'));
});
test('wrong endpoints, changed roles and non-involutive declarations are rejected',()=>{
 for(const patch of [{from:'NNPE:3'},{kind:'different'},{reverse:'NNPE:e2'}]){
  const t=example();Object.assign(t.edges.find(e=>e.id==='NNPE:e0^-1'),patch);assert.equal(auditPathReversal(t).status,'refuted');
 }
});
test('reverse edges alone do not suffice when reverse turns are forbidden',()=>{
 const t=example();t.turns=t.paths.flatMap(p=>p.edges.slice(1).map((e,i)=>[p.edges[i],e]));
 let r=auditPathReversal(t);assert.equal(r.status,'refuted');assert(codes(r).includes('forbidden-turn'));
 t.turns.push(...t.paths.flatMap(p=>{const ids=[...p.edges].reverse().map(id=>id+'^-1');return ids.slice(1).map((e,i)=>[ids[i],e]);}));assert.equal(auditPathReversal(t).status,'verified');
});
test('noncomposable paths and malformed graph incidence fail closed',()=>{
 let t=example();t.paths[0].edges.reverse();assert.equal(auditPathReversal(t).status,'refuted');
 t=example();t.vertices.pop();assert.equal(auditPathReversal(t).status,'refuted');
 t=example();t.edges.push(t.edges[0]);assert.equal(auditPathReversal(t).status,'refuted');
});
test('missing declarations and missing generator coverage are unknown, not vacuous success',()=>{
 assert.equal(auditPathReversal().status,'unknown');assert.equal(auditPathReversal({vertices:[],edges:[],paths:[]}).status,'unknown');
 const t=example();t.paths.pop();assert.equal(auditPathReversal(t).status,'unknown');
});
test('Ca46 remains unknown: rendered wrapper spans do not supply native path topology',()=>{
 const html=readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8'),context=vm.createContext({});
 vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],context);
 const definition=JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures().Ca46)),r=auditDefinitionPathReversal(definition);
 assert.equal(r.definitionId,'Ca46');assert.equal(r.status,'unknown');assert.deepEqual(r.issues,[{code:'missing-path-topology'}]);
});
