import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import {bindCa46ConnectedPaths,studyConnectedCa46,studyConnectedCalcium} from '../examples/isotope-wiring/core/connected-path-trial.mjs';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const d=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca46)),svg=c.IsotopeWiring.renderSVG(d,{interactive:true});
test('Ca44 maps ten tetrahedra and four coherence spans and traces PE walks both ways',()=>{
 const definition=JSON.parse(JSON.stringify(c.IsotopeWiring.fixtures().Ca44)),svg44=c.IsotopeWiring.renderSVG(definition,{interactive:true}),result=studyConnectedCalcium(definition,svg44),b=result.binding;
 assert.equal(b.tetrahedra.length,10);assert.equal(b.peBindings.length,20);assert.equal(b.counts.verticalDiagonals,10);assert.equal(b.counts.components,5);assert.equal(b.counts.cycleRank,34);assert.equal(b.cycles.length,34);
 assert.equal(b.crossings.filter(x=>x.reason==='opposite-neutron-legs-in-tetrahedron').length,10);assert.equal(b.crossings.filter(x=>!x.reason).length,6);
 assert.equal(b.topology.walks.filter(w=>w.id.startsWith('wrapper:')).length,4);
 assert.equal(result.gaugeControl.status,'verified');assert.equal(result.twistedControl.status,'refuted');assert.equal(result.status,'unknown');
 const edges=new Map(b.topology.edges.map(e=>[e.id,e]));
 for(const pair of definition.graph.pairs){const w=b.topology.walks.find(w=>w.id===pair.id);assert(w);let at=w.base;for(const id of [...w.edges].reverse().map(id=>edges.get(id).reverse)){const e=edges.get(id);assert.equal(e.from,at);at=e.to;}assert.equal(at,w.base);}
});

test('endpoint-only gluing retains twenty PE occurrences and binds all diagonals',()=>{
 const b=bindCa46ConnectedPaths(d,svg);assert.equal(b.peBindings.length,20);assert.deepEqual(b.peBindings.map(p=>p.pair).sort(),d.graph.pairs.map(p=>p.id).sort());
 assert.equal(b.counts.verticalDiagonals,10);assert.equal(b.supports.flatMap(s=>s.sources).filter(s=>s.startsWith('vertical:')).length,10);
 assert.equal(new Set(b.topology.vertices.map(v=>v.position.join(','))).size,b.topology.vertices.length);
 assert.equal(b.counts.components,7);assert.equal(b.counts.vertices,47);assert.equal(b.counts.supports,76);
});
test('two-PE cells are tetrahedra with disjoint opposite neutron legs, not five-vertex planar crosses',()=>{
 const b=bindCa46ConnectedPaths(d,svg),supports=new Map(b.supports.map(s=>[s.id,s]));assert.equal(b.tetrahedra.length,10);
 for(const t of b.tetrahedra){assert.equal(t.vertices.length,4);assert.equal(t.supports.length,6);assert.equal(t.PEOccurrences.length,2);assert.equal(t.centralJunction,false);
  const legs=t.oppositeNeutronLegs.map(id=>supports.get(id));assert.equal(new Set(legs.flatMap(s=>[s.from,s.to])).size,4);assert(legs.every(s=>s.role==='neutron-leg'));
  for(const v of t.vertices)assert.equal(t.supports.filter(id=>{const s=supports.get(id);return s.from===v||s.to===v;}).length,3);
  const crossing=b.crossings.find(c=>c.cell===t.cell);assert.equal(crossing.joined,false);assert.equal(crossing.reason,'opposite-neutron-legs-in-tetrahedron');
  assert(!t.vertices.some(id=>b.topology.vertices.find(v=>v.id===id).position.join(',')===crossing.position.join(',')));
 }
 assert.equal(b.counts.tetrahedralProjectionCrossings,10);
});
test('forest supplies complete cycle rank with composable return paths',()=>{
 const b=bindCa46ConnectedPaths(d,svg),edges=new Map(b.topology.edges.map(e=>[e.id,e]));
 assert.equal(b.cycles.length,b.counts.supports-b.counts.vertices+b.components.length);assert.equal(b.cycles.length,36);
 assert.equal(new Set(b.cycles.map(w=>w.chord)).size,b.cycles.length);
 for(const w of b.topology.walks){let at=w.base;for(const id of w.edges){const e=edges.get(id);assert.equal(e.from,at);at=e.to;}assert.equal(at,w.base);}
});
test('branching and interior crossings remain explicit unresolved choices',()=>{
 const b=bindCa46ConnectedPaths(d,svg);assert.equal(b.branches.length,27);assert(b.branches.every(v=>v.nonBacktrackingChoicesPerArrival>1));assert.equal(b.crossings.length,20);assert(b.crossings.every(x=>x.joined===false));
 assert.equal(b.topology.turns,undefined);assert(b.residuals.some(r=>r.includes('Routing')));
});
test('global flatness is a transport assumption, not selected by the drawing',()=>{
 const before=JSON.stringify(d),r=studyConnectedCa46(d,svg);assert.equal(r.status,'unknown');assert.equal(r.gaugeControl.status,'verified');assert.equal(r.twistedControl.status,'refuted');assert(r.twistedControl.walks.some(w=>w.issues.some(i=>i.code==='frame-does-not-return')));assert.equal(JSON.stringify(d),before);
});
test('removing a displayed vertical diagonal cannot silently pass coverage',()=>{
 const damaged=svg.replace(/<path class="neutron sketch-cross" data-cell="s1-00" d="M0 34 L0 134">[\s\S]*?<\/path>/,'');assert.notEqual(damaged,svg);assert.throws(()=>bindCa46ConnectedPaths(d,damaged),/coverage mismatch/);
});
