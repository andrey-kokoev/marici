import test from 'node:test';import assert from 'node:assert/strict';
import {table,groupSource,restoreSource,unpackReversed,retainedKeyProjection,restoreKeyProjection,canonicalRows,runMarkedTableDiagram,verifyMarkedReference} from '../research/strominger/marked-table-diagram.mjs';
const sample=()=>table([{id:'a',label:0,source:0,target:1,payload:{values:[1,2],witness:'a'}},{id:'b',label:0,source:0,target:0,payload:{values:[3,4],witness:'b'}}],{label:[0,1],source:[0,1,2],target:[0,1]},['root-history']);
test('four-step cycle retains repeated labels, payloads, empty fibers and history',()=>{
 const input=sample(),result=runMarkedTableDiagram(input);assert.equal(result.tableDataRecovered,true);assert.equal(result.historyPreservedAndExtended,true);assert.equal(result.composition.status,'verified-conditionally');assert.equal(result.stages[1].groups.filter(g=>g.children.length===0).length,2);assert.equal(result.stages[4].history[0],'root-history');assert.equal(result.stages[4].history.length,5);assert.notDeepEqual(canonicalRows(result.stages[2].rows),canonicalRows(input.rows));
 assert.equal(runMarkedTableDiagram(table([],{label:[],source:[],target:[]})).tableDataRecovered,true);
});
test('key projection is noninvertible alone but the retained context reconstructs the full table',()=>{
 const a=sample(),b=sample();b.rows[0].payload.values[0]=99;const pa=retainedKeyProjection(a),pb=retainedKeyProjection(b);assert.deepEqual(pa.keys,pb.keys);assert.notDeepEqual(pa.retainedContext,pb.retainedContext);assert.deepEqual(canonicalRows(restoreKeyProjection(pa)),canonicalRows(a.rows));assert.throws(()=>restoreKeyProjection({keys:pa.keys}));
});
test('erased selector, false membership, wrong unpacking and row-label deduplication are detected',()=>{
 const t=sample(),f=groupSource(t);assert.throws(()=>restoreSource({...f,selector:null}));const hidden=structuredClone(f);hidden.groups[0].children[0].source=42;assert.throws(()=>restoreSource(hidden));
 const wrong=structuredClone(f);wrong.groups[0].key=17;assert.throws(()=>restoreSource(wrong));
 const dedup=structuredClone(f);dedup.groups[0].children.pop();assert.notDeepEqual(canonicalRows(restoreSource(dedup)),canonicalRows(t.rows));assert.notDeepEqual(canonicalRows(unpackReversed(f).rows),canonicalRows(t.rows));
});
test('finite adapter comparison rejects disagreement with a supplied reference case',()=>{
 const reference={source:'prior-checker',sha256:'test',scope:'test',cases:[{dimensions:[1,2,2],rows:[[0,0,1]],sourceFibers:[[0,[[0,1]]],[1,[]]],twice:[[0,1,0]],four:[[0,0,1]]}]};assert.equal(verifyMarkedReference(reference).status,'verified-finite-reference');reference.cases[0].twice=[[0,0,1]];assert.equal(verifyMarkedReference(reference).status,'rejected');
});
