import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
const c=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],c);
const trace=(...args)=>JSON.parse(JSON.stringify(c.IsotopeWiring.traceAlternatingEdges(...args)));
const edge=(id,a,b,directed=true)=>({id,a,b,directed});
const T=[0,34],L=[-50,84],R=[50,84],C=[0,134],D=[50,184],E=[-50,184];
const lithium=[edge('red-top',T,L),edge('green-top',L,R),edge('red-in',R,C),edge('red-bottom',C,D),edge('green-bottom',D,E),edge('blue-bottom',E,C),edge('blue-out',C,L),edge('blue-top',R,T)];
test('reflected Li6 follows arrows and both branches with actual-turn fallback',()=>{
 const r=trace(lithium,'green-top');assert.equal(r.status,'closed');assert.deepEqual(r.steps.map(s=>s.id),['green-top','blue-top','red-top','green-top','red-in','red-bottom','green-bottom','blue-bottom','blue-out']);assert(r.steps.some(s=>s.fallback&&s.turn==='right'));assert(r.steps.some(s=>s.fallback&&s.turn==='left'));
 for(const start of lithium){const result=trace(lithium,start.id);assert.equal(result.status,'closed');assert.equal(new Set(result.steps.map(s=>s.id)).size,8);}
});
test('same-color straight continuation beats a preferred turn and retains turn preference',()=>{
 for(const color of ['red','blue','green']){const edges=[{...edge('in',[0,0],[1,0]),color},{...edge('left',[1,0],[1,-1]),color},{...edge('straight',[1,0],[2,0]),color},{...edge('next-left',[2,0],[2,-1]),color}];const r=trace(edges,'in');assert.deepEqual(r.steps.map(s=>s.id),['in','straight','next-left']);assert.equal(r.steps[0].turn,'straight');assert.equal(r.steps[0].sameColorStraight,true);assert.equal(r.steps[0].fallback,false);assert.equal(r.steps[1].preferred,'left');}
});
test('different-color straight edges do not outrank a turn and reverse arrows remain forbidden',()=>{
 const r=trace([{...edge('in',[0,0],[1,0]),color:'red'},{...edge('straight',[1,0],[2,0]),color:'blue'},{...edge('reverse',[2,0],[1,0]),color:'red'},{...edge('left',[1,0],[1,-1]),color:'blue'}],'in');assert.equal(r.steps[1].id,'left');assert.equal(r.steps[0].sameColorStraight,false);
});
test('same-side forks select the first eligible edge in drawing order',()=>{
 for(const sign of [1,-1]){const incoming=edge('in',[0,0],[0,1]),a=edge('a',[0,1],[sign,2]),b=edge('b',[0,1],[sign,1]);for(const order of [[a,b],[b,a]]){const r=trace([incoming,...order],'in');assert.equal(r.status,'dead-end');assert.equal(r.steps[1].id,order[0].id);assert.equal(r.steps[0].turn,sign===1?'left':'right');}}
});
test('undirected edges allow either start; directed arrows cannot be reversed',()=>{
 assert.equal(trace([edge('bar',[0,0],[0,1],false)],'bar',true).steps[0].from[1],1);assert.throws(()=>trace([edge('arrow',[0,0],[0,1])],'arrow',true),/Cannot reverse/);
 const r=trace([edge('in',[0,0],[1,0]),edge('back',[2,0],[1,0])],'in');assert.equal(r.status,'dead-end');
});
test('unmarked crossings are not vertices; straight continuation is a last resort',()=>{
 assert.equal(trace([edge('across',[-1,0],[1,0]),edge('cross',[0,-1],[0,1])],'across').steps.length,1);
 const r=trace([edge('a',[0,0],[1,0]),edge('b',[1,0],[2,0])],'a');assert.equal(r.steps[0].turn,'straight');assert.equal(r.steps[1].preferred,'left');
});
