import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {bindCa46ConnectedPaths} from '../examples/isotope-wiring/core/connected-path-trial.mjs';
import {buildDeterministicRouting} from '../examples/isotope-wiring/core/deterministic-routing.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),b=bindCa46ConnectedPaths(d,c.IsotopeWiring.renderSVG(d,{interactive:true}));
const key=s=>JSON.stringify([s.edge,s.hand]);
test('one successor and predecessor at every directed arrival state, without backtracking',()=>{
 const before=JSON.stringify(b),r=buildDeterministicRouting(b);assert.equal(JSON.stringify(b),before);assert.equal(r.counts.routingStates,304);assert.equal(r.counts.cycles,46);assert.equal(r.counts.immediateBacktracks,0);
 const edges=new Map(b.topology.edges.map(e=>[e.id,e]));assert.equal(new Set(r.transitions.map(t=>key(t.from))).size,304);assert.equal(new Set(r.transitions.map(t=>key(t.to))).size,304);
 for(const t of r.transitions){assert.equal(edges.get(t.from.edge).to,edges.get(t.to.edge).from);assert.notEqual(edges.get(t.from.edge).reverse,t.to.edge);}
});
test('every allowed turn has precisely its handedness-reversed turn',()=>{
 const r=buildDeterministicRouting(b),edges=new Map(b.topology.edges.map(e=>[e.id,e])),next=new Map(r.transitions.map(t=>[key(t.from),t.to]));
 for(const {from,to} of r.transitions)assert.deepEqual(next.get(key({edge:edges.get(to.edge).reverse,hand:-to.hand})),{edge:edges.get(from.edge).reverse,hand:-from.hand});
});
test('all twenty PE departures return their full routing state in eight steps and reverse exactly',()=>{
 const r=buildDeterministicRouting(b);assert.equal(r.PEroutes.length,40);assert.equal(new Set(r.PEroutes.map(p=>p.pair)).size,20);assert(r.PEroutes.every(p=>p.fullStateReturn===8));assert.deepEqual([...new Set(r.PEroutes.map(p=>p.firstVertexReturn))].sort((a,b)=>a-b),[3,4,8]);
 const edges=new Map(b.topology.edges.map(e=>[e.id,e]));for(const p of r.PEroutes)assert.deepEqual(p.reverseEdges,[...p.edges].reverse().map(id=>edges.get(id).reverse));
 for(const pair of b.peBindings){const [a,z]=r.PEroutes.filter(p=>p.pair===pair.pair);assert.notDeepEqual(a.edges,z.edges,'Handedness is real input, not uniqueness from vertex alone');}
 assert.match(r.frameReturn,/unknown/);
});
test('routing does not join tetrahedral projection crossings or change incidence',()=>{
 const r=buildDeterministicRouting(b);assert.equal(r.order.length,b.topology.vertices.length);for(const t of b.tetrahedra)assert.equal(t.centralJunction,false);assert.equal(b.counts.components,7);
});
test('reordering stored edges cannot change geometric cyclic routing',()=>{
 const altered=structuredClone(b);altered.topology.edges.reverse();
 const summarize=r=>r.transitions.map(t=>JSON.stringify(t)).sort();assert.deepEqual(summarize(buildDeterministicRouting(altered)),summarize(buildDeterministicRouting(b)));
});
test('missing inverses and coincident port rays are rejected rather than tie-broken by ID',()=>{
 const bad=structuredClone(b);bad.topology.edges.pop();assert.throws(()=>buildDeterministicRouting(bad),/reverse incidence/);
 const tie=structuredClone(b),e=tie.topology.edges[0],v=tie.topology.vertices.find(v=>v.id===e.to);tie.topology.vertices.push({...v,id:'duplicate-position'});tie.topology.edges.push({id:'tie+',from:e.from,to:'duplicate-position',reverse:'tie-',support:'tie'},{id:'tie-',from:'duplicate-position',to:e.from,reverse:'tie+',support:'tie'});assert.throws(()=>buildDeterministicRouting(tie),/Ambiguous cyclic order/);
});
