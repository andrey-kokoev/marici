import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {constructQuery,verifyQuery,nativeMarker,replaySelectionPath,region,sourcePattern,suffixPrograms,labels} from '../ramsey-native-query-selection.mjs';
import {same} from '../ramsey-native-word-trace.mjs';
const copy=x=>structuredClone(x);
const protocol=JSON.parse(readFileSync(new URL('../contracts/ramsey-native-query-selection-attempt.v1.json',import.meta.url),'utf8'));
assert(same(suffixPrograms,protocol.program.count_1_count_2_suffixes));
assert.deepEqual(sourcePattern(),[[0,0,0],[1,1,0],[1,0,1]]);
const task={alphabet:[...labels],pattern:sourcePattern(),radius:2,colorCount:2,
 coloring:region().map(point=>({point,color:(point[1]%2+2)%2}))};
const cases=[];let constructionCases=0,recoloringPathComparisons=0;
for(let a=0;a<3;a++)for(let b=0;b<3;b++){
 const word=[a,b],selection=constructQuery(task,word);assert.equal(verifyQuery(task,word,selection),true);constructionCases++;
 cases.push({word,selection});
 for(const variant of [task.coloring.map(row=>({...row,color:1-row.color})),task.coloring.map(row=>({...row,color:0}))]){
  const recolored={...task,coloring:variant},other=constructQuery(recolored,word);
  assert.equal(verifyQuery(recolored,word,other),true);assert(same(other.path,selection.path)&&same(other.marker,selection.marker));
  constructionCases++;recoloringPathComparisons++;
 }
}
const find=word=>cases.find(c=>same(c.word,word)).selection,A=find([0,2]),B=find([1,0]);
assert(same(A.path.prefix.endpoint,B.path.prefix.endpoint));
assert.deepEqual([A.marker.latticePoint,B.marker.latticePoint],[[1,0,1],[1,1,0]]);
assert.deepEqual([A.color,B.color],[0,1]);assert(!same(A.path.endpoint,B.path.endpoint));
const controls=[];function rejects(name,f){assert.throws(f,RangeError);controls.push(name);}
function mutation(word,alter){const x=copy(find(word));alter(x);return ()=>verifyQuery(task,word,x);}
rejects('erase selected-point witness',mutation([1,0],x=>{delete x.marker;}));
// These two adversarial objects remain SOURCE-VALID, including recomputed
// terminal markers and colors. Only the word-to-point square detects them.
function finish(x){x.marker=nativeMarker(x.path);x.color=task.coloring.find(r=>same(r.point,x.marker.latticePoint)).color;return x;}
const erased=copy(B);erased.path.events=[];erased.path.endpoint=copy(erased.path.prefix.endpoint);finish(erased);replaySelectionPath(erased.path);
rejects('source-valid erased suffix selects wrong requested point',()=>verifyQuery(task,[1,0],erased));
const swapped=copy(A);swapped.path.events=copy(B.path.events);swapped.path.endpoint=copy(B.path.endpoint);finish(swapped);replaySelectionPath(swapped.path);
rejects('source-valid swapped suffix selects wrong requested point',()=>verifyQuery(task,[0,2],swapped));
rejects('alter terminal outside native reference',mutation([1,0],x=>{x.path.endpoint.chart.aliases.C2=x.path.endpoint.chart.aliases.C0;}));
rejects('alter fifth coefficient coordinate',mutation([1,0],x=>{x.path.events[0].target.packet.permutation[4]=0;}));
rejects('drop actual phase witness',mutation([1,0],x=>{x.path.events[0].phaseWitness=null;}));
rejects('incorrect reported supplied color',mutation([1,0],x=>{x.color=1-x.color;}));
rejects('different requested word',()=>verifyQuery(task,[0,2],B));
rejects('inject target point as input',()=>constructQuery({...task,targetPoint:[1,1,0]},[1,0]));
rejects('partial input coloring',()=>constructQuery({...task,coloring:task.coloring.slice(1)},[1,0]));
const duplicate=copy(task);duplicate.coloring[1]=copy(duplicate.coloring[0]);
rejects('duplicate coloring row',()=>constructQuery(duplicate,[1,0]));
const foreign=copy(task);foreign.pattern[1]=[2,0,0];
rejects('pattern not bound to source window',()=>constructQuery(foreign,[1,0]));
rejects('length-three word outside this constructor',()=>constructQuery(task,[1,0,0]));
console.log(JSON.stringify({task,cases,constructionCases,recoloringPathComparisons,negativeControls:controls,
 sourceValidWrongQueryControls:2,primaryWords:[[0,2],[1,0]],primaryColors:[A.color,B.color],
 primarySuffixCounts:[A.path.events.length,B.path.events.length],
 primaryNativeEndpointsDistinguished:true,nativeWitnessEvents:cases.reduce((n,c)=>n+c.selection.path.prefix.events.length+c.selection.path.events.length,0),
 sourceSelectionUsesTargetPointOrColor:false,autonomousNativeControllerProved:false,uniformTaskPackageAdmitted:false,rootResolved:false}));
