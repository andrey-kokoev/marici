// Fixed-task forward query realization. Production packet rules are unchanged.
import {GenerativeAssemblyRules} from '../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {phaseFrame,phaseAdvanceWitness} from '../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {encodeWord,verifyWord,replayTrace,packetSnapshot,same} from './ramsey-native-word-trace.mjs';
const copy=x=>structuredClone(x),need=(c,m)=>{if(!c)throw new RangeError(m);};
const SCHEMA='marici.ramsey-native-query-selection.v1',PATH='marici.ramsey-native-query-path.v1';
export const labels=Object.freeze(['s0','s1','s2']);
export const suffixPrograms=Object.freeze({
 '0,0':[], '1,0':['reader-phase-advance','PN'], '0,1':[],
 '2,0':['PN','NN-phase-advance','NN-phase-advance','NN-phase-advance','inverse-PN'],
 '1,1':['PN','NN-phase-advance','NN-phase-advance','NN-phase-advance'],
 '0,2':['PN','NN-phase-advance','NN-phase-advance','inverse-PN'],
});
function keys(x,names){need(x&&typeof x==='object'&&!Array.isArray(x)&&same(Object.keys(x).sort(),[...names].sort()),'unexpected fields');}
export function latticePoint(vertex){
 const b=vertex.split(',').map(Number);need(b.length===4&&b.every(Number.isSafeInteger)&&b.reduce((a,x)=>a+x,0)===1,'invalid source point');
 return [b[1]+b[2],b[1]+b[3],b[2]+b[3]];
}
export function sourcePattern(){
 const r=new GenerativeAssemblyRules(),p=r.packets[r.root],f=phaseFrame(r.charts[p.chart],p.origin);
 return f.window.map(o=>latticePoint(o.vertex));
}
export function region(){const ps=[];for(let x=-2;x<=2;x++)for(let y=-2;y<=2;y++)for(let z=-2;z<=2;z++)if((x+y+z)%2===0)ps.push([x,y,z]);return ps;}
function field(task){
 keys(task,['alphabet','pattern','radius','colorCount','coloring']);
 need(same(task.alphabet,labels)&&same(task.pattern,sourcePattern())&&task.radius===2,'task not source-bound fixed pilot');
 need(Number.isSafeInteger(task.colorCount)&&task.colorCount>=1,'invalid palette');
 need(Array.isArray(task.coloring)&&task.coloring.length===63,'complete coloring required');
 const table=new Map();
 for(const row of task.coloring){keys(row,['point','color']);need(Array.isArray(row.point)&&row.point.length===3&&row.point.every(Number.isSafeInteger),'invalid color point');
  need(Number.isSafeInteger(row.color)&&row.color>=0&&row.color<task.colorCount,'invalid color');
  const k=row.point.join(',');need(!table.has(k),'duplicate coloring point');table.set(k,row.color);}
 need(region().every(p=>table.has(p.join(','))),'wrong coloring domain');return table;
}
function wordInput(word){need(Array.isArray(word)&&word.length===2&&word.every(i=>Number.isSafeInteger(i)&&i>=0&&i<3),'length-two word required');}
function take(r,current,kind,ordinal){
 need(['PN','inverse-PN','reader-phase-advance','NN-phase-advance'].includes(kind),'unadmitted query instruction');
 const ops=r.outgoing(current).map(i=>r.operations[i]).filter(o=>o.kind===kind);
 need(ops.length===1,'query operation is not uniquely available');const op=ops[0];need(r.validateTransfer(op)===true,'invalid native query transfer');
 const p=r.packets[op.source],q=r.packets[op.target],a=r.charts[p.chart],b=r.charts[q.chart];
 return {op,event:{ordinal,kind,source:packetSnapshot(r,op.source),target:packetSnapshot(r,op.target),face:copy(op.face),phaseDelta:op.phaseDelta,
  permutation:[...op.permutation],phaseFrames:{source:phaseFrame(a,p.origin),target:phaseFrame(b,q.origin)},
  phaseWitness:op.phaseDelta===1?phaseAdvanceWitness(a,b,p.origin):null}};
}
export function buildNativePath(prefix,kinds){
 const {rules:r,current:start}=replayTrace(prefix);let current=start;const events=[];
 for(const kind of kinds){const x=take(r,current,kind,prefix.events.length+events.length);events.push(x.event);current=x.op.target;}
 return {schema:PATH,prefix:copy(prefix),events,endpoint:packetSnapshot(r,current)};
}
export function replaySelectionPath(path){
 keys(path,['schema','prefix','events','endpoint']);need(path.schema===PATH&&Array.isArray(path.events)&&path.events.length<=8,'invalid query path');
 const {rules:r,current:start}=replayTrace(path.prefix);let current=start;
 for(let j=0;j<path.events.length;j++){
  const row=path.events[j],x=take(r,current,row.kind,path.prefix.events.length+j);
  need(same(row,x.event),'query packet/reference/phase witness changed');current=x.op.target;
 }
 need(same(path.endpoint,packetSnapshot(r,current)),'query endpoint changed');return {rules:r,current};
}
export function nativeMarker(path){
 const {rules:r,current}=replaySelectionPath(path),p=r.packets[current],frame=phaseFrame(r.charts[p.chart],p.origin);
 return {frame,occurrence:copy(frame.window[0]),latticePoint:latticePoint(frame.window[0].vertex)};
}
export function constructQuery(task,word){
 const table=field(task);wordInput(word);
 // Dispatch on supplied tokens, never on a computed target coordinate or color.
 const key=[word.filter(i=>i===1).length,word.filter(i=>i===2).length].join(',');
 const path=buildNativePath(encodeWord([...labels],word),suffixPrograms[key]),marker=nativeMarker(path);
 const color=table.get(marker.latticePoint.join(','));need(color!==undefined,'selected point outside supplied domain');
 return {schema:SCHEMA,path,marker,color};
}
export function verifyQuery(task,word,value){
 const table=field(task);wordInput(word);keys(value,['schema','path','marker','color']);need(value.schema===SCHEMA,'query schema');
 verifyWord(value.path.prefix,[...labels],word);
 const marker=nativeMarker(value.path);need(same(value.marker,marker),'not the terminal native first-window mark');
 // Task arithmetic is an independent check, not the forward construction.
 const expected=[0,1,2].map(j=>word.reduce((sum,i)=>sum+task.pattern[i][j],0));
 need(same(marker.latticePoint,expected),'native path selects the wrong requested word sum');
 need(value.color===table.get(expected.join(',')),'incorrect supplied-color observation');return true;
}
