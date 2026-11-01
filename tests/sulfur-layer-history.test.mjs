import {test} from 'node:test';
import assert from 'node:assert/strict';
import {buildBranchingSeed} from '../research/realization-tower/branching-seed.mjs';
import {auditEightLayerHistory,auditLayerHistory,advanceHistoryMemory,encodeHistoryBit} from '../research/realization-tower/sulfur-layer-history.mjs';
const seed=buildBranchingSeed(),before=JSON.stringify(seed),audit=auditEightLayerHistory(seed);
const signature=i=>i.ports.flatMap(p=>p.records.map(r=>[p.colour,r.word,r.candidateB].join(':'))).sort();
test('audit counts causal prefixes, not distinct future completions as current records',()=>{
 assert.equal(audit.summary.completeWhiteNeighbourhoods,168);
 for(const layer of audit.layers){
  assert.deepEqual(layer.counts,{fullRoutes:256,whiteEdges:36,distinctWhitePrefixes:255,completeWhiteNeighbourhoods:21,completeIncomingTwoByTwo:0});
  for(const white of layer.whiteRecords)for(const record of white.records)assert.equal(record.completions,2**(8-white.depth));
 }
});
test('current edge colour cannot distinguish co-arriving histories, whereas an older branch bit can',()=>{
 for(const layer of audit.layers){
  const first=layer.collisions[0];assert.equal(first.depth,3);assert.equal(first.words.length,2);
  assert.equal(first.currentColourValues.length,1);assert.equal(first.olderColourValues.length,2);
  assert(layer.collisions.some(c=>c.words.length>2&&c.olderColourValues.length===2));
 }
});
test('first merge plus its outgoing fork supplies four independent port/history states in every layer',()=>{
 assert.equal(audit.summary.earliestTwoHistoryInterfaces,8);assert.equal(audit.summary.interfacesCarryIndependentBit,true);
 for(const layer of audit.layers){
  assert.equal(layer.interfaces.length,1);const i=layer.interfaces[0];assert.equal(i.depth,2);
  assert.deepEqual(i.incomingHistories.map(r=>r.word).sort(),['BR','RB']);
  assert.deepEqual(signature(i),['blue:BRB:+','blue:RBB:-','red:BRR:+','red:RBR:-']);
  const states=i.ports.flatMap(p=>p.records.map(r=>p.colour+':'+r.candidateB));assert.equal(new Set(states).size,4);
  assert.equal(i.incomingHistories.reduce((s,r)=>s+r.completions,0),128);
  assert.equal(i.ports.flatMap(p=>p.records).reduce((s,r)=>s+r.completions,0),128);
 }
});
test('history memory is causal and needs no suffix, route ID or native assignment',()=>{
 const layer=seed.layers[0],edges=new Map(layer.edges.map(e=>[e.id,e]));
 const truncated=[...new Map(layer.routes.map(r=>{const path=r.edges.slice(0,6);return [JSON.stringify(path),{id:'opaque',edges:path}];})).values()];
 const short=auditLayerHistory({...layer,routes:truncated});
 assert.deepEqual(signature(short.interfaces[0]),signature(audit.layers[0].interfaces[0]));
 for(const p of short.interfaces[0].ports)for(const r of p.records){
  let memory={previous:null,current:null};for(const id of r.path)memory=advanceHistoryMemory(memory,edges.get(id).role);
  assert.equal(memory.current,p.colour);assert.equal(encodeHistoryBit(memory.previous),r.candidateB);assert.equal(r.completions,1);
 }
});
test('one colour convention survives all reflections and does not depend on geometric left/right',()=>{
 assert.equal(audit.summary.reflectionInvariantHistoryCoding,true);
 const redSides=new Set(),arrowDirections=new Set();
 for(const [index,l]of audit.layers.entries()){
  const i=l.interfaces[0],source=seed.layers[index],white=source.edges.find(e=>e.id===i.whiteEdge),red=source.edges.find(e=>e.id===i.ports.find(p=>p.colour==='red').edge);
  redSides.add(Math.sign(red.points[1][0]-red.points[0][0]));arrowDirections.add(Math.sign(white.points[1][1]-white.points[0][1]));
  for(const p of i.ports)for(const r of p.records)assert.notEqual(r.candidateB,r.oppositeConventionB);
 }
 assert.equal(redSides.size,2);assert.equal(arrowDirections.size,2);
 const gap=auditEightLayerHistory(buildBranchingSeed({seedLayerGap:6}));assert.deepEqual(gap.summary,audit.summary);
});
test('a complete single white-edge incoming neighbourhood is not silently reduced to four paths',()=>{
 assert.equal(audit.summary.completeIncomingTwoByTwo,0);
 for(const layer of audit.layers)for(const w of layer.whiteRecords.filter(w=>w.complete))assert(!w.incoming.every(p=>p.records.length===2));
 assert.equal(JSON.stringify(seed),before);
});
