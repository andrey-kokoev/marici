import test from 'node:test';
import assert from 'node:assert/strict';
import {auditFrameReturn} from '../examples/isotope-wiring/core/frame-return.mjs';
const I=[[1,0,0],[0,1,0],[0,0,1]],X=[[1,0,0],[0,0,-1],[0,1,0]],Y=[[0,0,1],[0,1,0],[-1,0,0]];
const transpose=a=>a[0].map((_,i)=>a.map(r=>r[i]));
const multiply=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,x,k)=>s+x*b[k][j],0)));
function example(rotations=[X,Y,transpose(multiply(Y,X))]){
 const vertices=[{id:'pe',role:'PE'},{id:'a',role:'junction'},{id:'b',role:'junction'}],edges=[];
 for(let i=0;i<3;i++){const from=vertices[i].id,to=vertices[(i+1)%3].id,id='e'+i,reverse='r'+i,support='s'+i;edges.push({id,from,to,support,reverse,transport:rotations[i]},{id:reverse,from:to,to:from,support,reverse:id,transport:transpose(rotations[i])});}
 return {vertices,edges,walks:[{id:'pe-loop',base:'pe',edges:['e0','e1','e2']}]};
}
test('noncommuting rotations return the PE vertex and whole frame in both directions',()=>{
 const t=example(),before=structuredClone(t),r=auditFrameReturn(t);assert.equal(r.status,'verified');assert.deepEqual(r.walks[0].forwardHolonomy,I);assert.deepEqual(r.walks[0].reverseHolonomy,I);assert.deepEqual(t,before);
});
test('closed triangle with residual rotation fails frame return',()=>{
 const r=auditFrameReturn(example([X,Y,I]));assert.equal(r.status,'refuted');assert(r.walks[0].issues.some(i=>i.code==='frame-does-not-return'));
});
test('returning one axis is not return of the whole frame',()=>{
 const r=auditFrameReturn(example([X,I,I]));assert.equal(r.status,'refuted');assert.deepEqual(r.walks[0].forwardHolonomy.map(row=>row[0]),[1,0,0]);
});
test('frame identity alone cannot repair an open path',()=>{
 const t=example([I,I,I]);t.walks[0].edges.pop();assert.equal(auditFrameReturn(t).status,'refuted');
});
test('reflection and malformed transports are not SO(3)',()=>{
 for(const transport of [[[-1,0,0],[0,1,0],[0,0,1]],[[1]],[[NaN,0,0],[0,1,0],[0,0,1]],[[2,0,0],[0,1,0],[0,0,1]]]){const t=example();t.edges[0].transport=transport;assert.equal(auditFrameReturn(t).status,'refuted');}
});
test('reverse transport must invert its own edge, not merely close some other loop',()=>{
 const t=example();t.edges.find(e=>e.id==='r0').transport=I;assert(auditFrameReturn(t).walks[0].issues.some(i=>i.code==='reverse-transport-not-inverse'));
});
test('missing frame data is unknown rather than default identity',()=>{
 const t=example();delete t.edges[0].transport;assert.equal(auditFrameReturn(t).status,'unknown');assert.equal(auditFrameReturn().status,'unknown');
});
test('cyclic turn restrictions include the closing turn and reversed traversal',()=>{
 const t=example();t.turns=[['e0','e1'],['e1','e2'],['e2','e0'],['r2','r1'],['r1','r0'],['r0','r2']];assert.equal(auditFrameReturn(t).status,'verified');t.turns.pop();assert.equal(auditFrameReturn(t).status,'refuted');
});
test('each PE base needs a declared walk; invalid bases and duplicate IDs fail',()=>{
 const t=example();t.vertices.push({id:'other',role:'PE'});assert.equal(auditFrameReturn(t).status,'unknown');t.walks[0].base='a';assert.equal(auditFrameReturn(t).status,'refuted');
 const duplicate=example();duplicate.vertices.push(duplicate.vertices[0]);assert.equal(auditFrameReturn(duplicate).status,'refuted');
});
