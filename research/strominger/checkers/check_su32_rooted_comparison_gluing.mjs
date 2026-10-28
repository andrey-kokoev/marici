import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,channelOperand,compareAt,reconcileAt,reconcileBothOrders} from '../su32-layer4-comparison.mjs';
import {comparisonPort,decomposeRootedComparison,glueRootedComparison} from '../su32-rooted-comparison-gluing.mjs';
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h);
const atlas=buildSu32SignedReferenceAtlas(fixture),reading=fixture.readings.find(r=>r.id==='reading:0:-1');
const chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);assert(chart);
let boundaryAssignments=0,accepted=0,rootReconstructions=0,stagedGluings=0;const refusalsByRoute={E:{comparison:0,reconciliation:0},P:{comparison:0,reconciliation:0}};
let example,conflict;
function evaluate(layout,channels,role){
 const specs=layout.template.comparisons.filter(c=>c.sharedRole===role);let local;
 try{local=specs.map(c=>compareAt(layout,c.cell,...c.inputs.map(id=>channels[id])));}catch(error){
  assert.match(error.message,/Shared record disagrees/);return {accepted:false,stage:'comparison'};
 }
 try{return {accepted:true,node:reconcileAt(layout,...local)};}catch(error){
  assert.match(error.message,/Shared record disagrees/);return {accepted:false,stage:'reconciliation',locallyValid:local};
 }
}
function inspectTree(layout,root){
 for(const expansion of [[0],[1],[0,1]]){
  const diagram=decomposeRootedComparison(layout,root,expansion),before=structuredClone(diagram);
  assert.equal(diagram.vertices.length,1+expansion.length);
  // Internal port descriptors do not smuggle the entire prior tree as data.
  for(const v of diagram.vertices){assert(!Object.hasOwn(v.output,'children'));for(const p of v.inputs)assert(!Object.hasOwn(p.expected,'children'));}
  assert.deepEqual(glueRootedComparison(layout,diagram),root);assert.deepEqual(diagram,before);rootReconstructions++;
 }
 // Contract either child operation first, then perform the remaining two-node
 // graft. This tests staged gluing on the same fixed source operation tree.
 const full=decomposeRootedComparison(layout,root,[0,1]);
 for(const i of [0,1]){
  const small=structuredClone(full),id='root/'+i;
  small.vertices=small.vertices.filter(v=>v.id!==id);
  small.boundary=small.boundary.filter(b=>!b.id.startsWith(id+'/'));
  small.boundary.push({id,operand:structuredClone(root.children[i])});
  small.vertices.find(v=>v.id==='root').inputs[i].source={kind:'boundary',id};
  assert.deepEqual(glueRootedComparison(layout,small),glueRootedComparison(layout,full));stagedGluings++;
 }
}
for(const p of [0,1])for(const e of [0,1]){
 const layout=comparisonLayout(atlas,fixture,chart.id,[p,e]);
 // Four channels have TWO appearances each: enumerate all 2^8 assignments,
 // not just the sixteen pre-consistent four-record registries.
 for(let bits=0;bits<256;bits++){
  let position=0;const channels={},appearances={};
  for(const c of layout.template.channels){
   const records={};for(const label of [c.P.record,c.E.record]){
    const value=(bits>>position++)&1;records[label]=value;(appearances[label]??=[]).push(value);
   }
   channels[c.cell]=channelOperand(layout,c.cell,records);
  }
  const consistent=Object.values(appearances).every(xs=>xs.length===2&&xs[0]===xs[1]);
  const routes=Object.fromEntries(['E','P'].map(r=>[r,evaluate(layout,channels,r)]));
  for(const role of ['E','P']){
   assert.equal(routes[role].accepted,consistent);
   if(!routes[role].accepted)refusalsByRoute[role][routes[role].stage]++;
  }
  boundaryAssignments++;
  if(!consistent){if(!conflict&&routes.E.stage==='reconciliation')conflict={bits,channels,comparisons:routes.E.locallyValid};continue;}
  accepted++;assert.deepEqual(routes.E.node.records,routes.P.node.records);assert.notDeepEqual(routes.E.node.children,routes.P.node.children);
  inspectTree(layout,routes.E.node);inspectTree(layout,routes.P.node);
 }
}
const layout=comparisonLayout(atlas,fixture,chart.id,[0,0]);
const registry=Object.fromEntries(['P+','P-','E+','E-'].map((k,i)=>[k,{id:'input:'+k,value:i,provenance:{entry:reading.incomingN}}]));
const built=reconcileBothOrders(layout,registry);inspectTree(layout,built.byE);inspectTree(layout,built.byP);
example=decomposeRootedComparison(layout,built.byE,[0,1]);
// All required shared-interface incidences are inherited from the source layout.
const adjacent=(a,b)=>fixture.interfaces.some(f=>{const cs=f.ports.map(p=>p.split('@')[0]);return cs.includes(a)&&cs.includes(b);});
for(const v of example.vertices)for(const port of v.inputs)assert(adjacent(port.expected.at,v.at));
let negativeControls=0;
const corrupt=fn=>{const d=structuredClone(example);fn(d);assert.throws(()=>glueRootedComparison(layout,d));negativeControls++;};
corrupt(d=>{d.vertices[0].inputs[0].expected.records['P+'].payload={wrong:true};});
corrupt(d=>{d.vertices[0].inputs[0].source.id='missing';});
corrupt(d=>{d.vertices[0].inputs[0].source.id='root';});
corrupt(d=>{d.vertices[0].inputs[1].source=d.vertices[0].inputs[0].source;});
corrupt(d=>{d.vertices[0].at='absent';});
corrupt(d=>{d.vertices[1].output.records['P+'].payload={invented:true};});
corrupt(d=>{d.boundary.pop();});
corrupt(d=>{d.vertices.push({...structuredClone(d.vertices[1]),id:'unused'});});
corrupt(d=>{d.anchor.binding=[1,1];});
corrupt(d=>{d.vertices[0].kind='comparison';});
// Attempting to treat a reconciliation result as a channel operand is a typed
// refusal by the current grammar, not proof that no cyclic extension can exist.
const spec=layout.template.comparisons[0];
assert.throws(()=>compareAt(layout,spec.cell,built.byE,built.channels[spec.inputs[1]]));negativeControls++;
assert.equal(accepted,64);assert(conflict);
// Verify that the conflict really consists of valid local comparison outputs,
// and its record overlap (not merely its support or geometric shape) disagrees.
const [a,b]=conflict.comparisons;
const conflicting=Object.keys(a.records).filter(k=>Object.hasOwn(b.records,k)&&JSON.stringify(a.records[k])!==JSON.stringify(b.records[k]));
assert(conflicting.length>0);
const sources=[fixturePath,'research/strominger/su32-layer4-comparison.mjs','research/strominger/su32-signed-reference-encoder.mjs',
 'research/strominger/su32-rooted-comparison-gluing.mjs','research/strominger/checkers/check_su32_rooted_comparison_gluing.mjs'];
const hashes={};for(const p of sources)hashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const report={schema:'su32.rooted-comparison-gluing-candidate.v1',passed:true,reading:reading.id,
 boundaryAssignments,accepted,refused:boundaryAssignments-accepted,refusalsByRoute,rootReconstructions,stagedGluings,negativeControls,
 portContract:'A wire carries a typed operand: node kind, occurrence anchor, cell attachment, reference identities, and payload values. Consumer/producer polarity is distinct from P/E direction signs.',
 shapeContract:'Rooted, input-slot-indexed two- or three-operation trees from existing compareAt/reconcileAt. Slot indexing is not a native planar cyclic order.',
 example,conflict:{...conflict,conflictingSharedRecords:conflicting},
 interpretation:{fixedTreeGluing:'Exact reconstruction of preexisting validated candidate trees from local operation headers and boundary operands; original child histories survive.',
  uniqueness:'For these fixed shapes, slots, boundary operands and deterministic existing operations, recursive evaluation fixes the resulting tree. No uniqueness across different trees/histories is claimed.',
  routeComparison:'E-first and P-first trees agree on complete records but retain distinct syntax; no new higher witness is supplied.'},
 limits:['This is a bounded Segal-style gluing test, not a cyclic operad or all-tree Segal theorem.',
  'Bad pairs of locally valid comparisons violate the root compatibility condition; they are not counterexamples consisting of fully compatible Segal-core data.',
  'A record can appear in several operand packets, but equal reference identities must have equal payloads. The 2^8 census tests this requirement explicitly.',
  'No units, root-changing actions, color involution, unrooted composition, global middle routing, or physical implementation were derived.',
  'The original joins are candidate information operations; native comparison maps remain unbound.'],sourceHashes:hashes};
const dir='research/strominger/results/su32-rooted-comparison-gluing-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,example:undefined,conflict:undefined,sourceHashes:undefined},null,2));
