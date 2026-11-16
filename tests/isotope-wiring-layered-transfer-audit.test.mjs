import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {buildLayeredCalcium} from '../examples/isotope-wiring/core/layered-neutron-transport.mjs';
import {auditLayeredTransfers} from '../examples/isotope-wiring/core/layered-transfer-audit.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),svg=c.IsotopeWiring.renderSVG(d,{interactive:true});
const build=()=>buildLayeredCalcium(d,svg);
test('covers every PE, its three terminal wrappers, both directions and both sides',()=>{
 const b=build(),before=JSON.stringify(b),a=auditLayeredTransfers(b);assert.equal(JSON.stringify(b),before);assert.equal(a.status,'verified-for-declared-interfaces');assert.equal(a.counts.representativeTransfers,120);assert.equal(a.counts.blocked,0);
 assert(a.byPE.every(p=>p.wrappers.length===3&&p.representatives===6));for(const w of b.wrappers)assert.deepEqual([...new Set(a.transfers.filter(t=>t.wrapper===w.id).map(t=>t.entry+t.side))].sort(),['BL','BR','TL','TR']);
});
test('all transfers reverse exactly and every PE excursion closes',()=>{
 const b=build(),a=auditLayeredTransfers(b),edges=new Map(b.topology.edges.map(e=>[e.id,e])),pe=new Map(b.PEComplexes.map(p=>[p.pair,p]));
 for(const t of a.transfers){assert.deepEqual(t.reverseEdges,[...t.edges].reverse().map(id=>edges.get(id).reverse));assert.deepEqual(t.reverseVertices,[...t.forwardVertices].reverse());let at=pe.get(t.source).base;for(const id of t.excursion){const e=edges.get(id);assert.equal(e.from,at);at=e.to;}assert.equal(at,pe.get(t.source).base);}
 assert(b.topology.edges.every(e=>e.transport===undefined));
});
test('explicit ambiguity survives representative selection',()=>{
 const a=auditLayeredTransfers(build());assert.equal(a.counts.representativesWithMultipleLocalRoutes,24);assert.equal(a.byPE.filter(p=>p.ambiguousEvenWithWrapperAndSide).length,8);assert.deepEqual([...new Set(a.byPE.map(p=>p.shortestTransferChoices))].sort(),['10','6','8']);assert.equal(a.byPE.reduce((n,p)=>n+Number(p.shortestTransferChoices),0),144);
});
test('independent bounded path enumeration confirms shortest local multiplicities',()=>{
 const b=build(),a=auditLayeredTransfers(b),edges=new Map(b.topology.edges.map(e=>[e.id,e])),allowed=new Set(['neutron-space-boundary','tetrahedral-neutron-leg','neutron-space-contact']);
 const adjacency=new Map(b.topology.vertices.map(v=>[v.id,[]]));for(const e of b.topology.edges)if(allowed.has(e.kind))adjacency.get(e.from).push(e.to);
 for(const t of a.transfers){const start=edges.get(t.edges[0]).to,target=edges.get(t.edges[t.localLength+1]).from;
  function count(at,left,seen){if(left===0)return at===target?1:0;let total=0;for(const next of adjacency.get(at))if(!seen.has(next)){const s=new Set(seen);s.add(next);total+=count(next,left-1,s);}return total;}
  for(let length=0;length<t.localLength;length++)assert.equal(count(start,length,new Set([start])),0);
  assert.equal(String(count(start,t.localLength,new Set([start]))),t.shortestLocalAlternatives);
 }
});
test('removing same-shell contacts exposes blocked transfers rather than silently skipping PEs',()=>{
 const b=build();b.topology.edges=b.topology.edges.filter(e=>e.kind!=='neutron-space-contact');const a=auditLayeredTransfers(b);assert.equal(a.status,'refuted');assert(a.blocked.length>0);assert.equal(a.byPE.length,20);assert(a.byPE.some(p=>p.representatives===0));
});
test('broken inverse interfaces fail and edge storage order does not select routes',()=>{
 const b=build(),a=auditLayeredTransfers(b);b.topology.edges.reverse();assert.deepEqual(auditLayeredTransfers(b),a);b.topology.edges.pop();assert.throws(()=>auditLayeredTransfers(b),/Invalid reverse interface/);
});
