import {readFileSync} from 'node:fs';
import {canonical,same,decodeWord,encodeWord} from './ramsey-native-word-trace.mjs';
import {project4} from './ramsey-native-region-family.mjs';
const copy=x=>structuredClone(x),need=(c,m)=>{if(!c)throw new RangeError(m);};
const raw=JSON.parse(readFileSync(new URL('./results/ramsey-native-region-family-input-v1.json',import.meta.url),'utf8'));
const sourceKeys=['schema','radius','rows','attemptedJointAssembly','canonicalPolicyUnchanged','preparedPolicyIsDifferent','wordToIndexConstructed'];
export const preparedInput=Object.fromEntries(sourceKeys.map(k=>[k,copy(raw[k])]));
export const labels=['s0','s1','s2'];
export const words=Array.from({length:27},(_,i)=>[Math.floor(i/9),Math.floor(i/3)%3,i%3]);
function keys(x,ks){need(x&&typeof x==='object'&&same(Object.keys(x).sort(),[...ks].sort()),'unexpected interface fields');}
export function compileWordProgram(input){
 keys(input,['prepared']);need(same(input.prepared,preparedInput),'not the admitted prepared input');
 const zero=input.prepared.rows.find(r=>same(r.point,[0,0,0]));
 const pattern=zero.frame.window.map(o=>project4(o.vertex));
 // This compiler runs on ALL words before any request or color function.
 const entries=words.map(word=>{
  const p=[0,1,2].map(j=>word.reduce((s,i)=>s+pattern[i][j],0));
  const regionIndex=input.prepared.rows.findIndex(r=>same(r.point,p));need(regionIndex>=0,'compiled query outside region');
  return {word:[...word],regionIndex};
 });
 return {schema:'marici.ramsey-native-word-query-program.v1',prepared:copy(input.prepared),pattern,entries};
}
export function verifyProgram(program){need(same(program,compileWordProgram({prepared:preparedInput})),'native program declaration changed');return true;}
function colorsInput(colors){need(Array.isArray(colors)&&colors.length===171&&colors.every(c=>Number.isSafeInteger(c)&&c>=0),'complete input color function required');}
export function queryWord(input){
 keys(input,['program','request','colors']);verifyProgram(input.program);colorsInput(input.colors);
 const requestWord=decodeWord(input.request);need(same(input.request.alphabet,labels)&&requestWord.length===3,'wrong request domain');
 need(same(input.request,encodeWord(labels,requestWord)),'request is not the fixed canonical native trace');
 const entry=input.program.entries.find(e=>same(e.word,requestWord));need(entry,'missing word premise');
 return {schema:'marici.ramsey-native-word-query-response.v1',request:copy(input.request),requestWord,
  regionIndex:entry.regionIndex,context:copy(input.program.prepared.rows[entry.regionIndex]),color:input.colors[entry.regionIndex]};
}
export function verifyResponse(program,expectedRequest,colors,response){
 verifyProgram(program);colorsInput(colors);keys(response,['schema','request','requestWord','regionIndex','context','color']);
 need(response.schema==='marici.ramsey-native-word-query-response.v1','response schema');
 need(same(response.request,expectedRequest),'a different request was substituted');
 const word=decodeWord(expectedRequest);need(same(response.requestWord,word),'native request word changed');
 const point=[0,1,2].map(j=>word.reduce((s,i)=>s+program.pattern[i][j],0));
 const expected=program.prepared.rows.findIndex(row=>same(row.point,point));
 need(response.regionIndex===expected&&same(response.context,program.prepared.rows[expected]),'wrong selected native context');
 need(same(project4(response.context.frame.window[0].vertex),point),'selected context does not realize word sum');
 need(response.color===colors[expected],'wrong supplied color');return true;
}
export {canonical,same,copy};
