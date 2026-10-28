// A retained trace of ACTUAL native packet operations, not geometry-only moves.
import {GenerativeAssemblyRules} from '../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {phaseFrame,phaseAdvanceWitness} from '../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
export class NativeTraceResourceError extends Error {}
const SCHEMA='marici.ramsey-native-word-trace.v1',MAX_ALPHABET=256,MAX_WORD=128,MAX_EVENTS=2048;
const copy=x=>structuredClone(x);
export function canonical(x){
 if(x instanceof Map)return {map:[...x].map(([k,v])=>[canonical(k),canonical(v)]).sort((a,b)=>{const x=JSON.stringify(a[0]),y=JSON.stringify(b[0]);return x<y?-1:x>y?1:0;})};
 if(Array.isArray(x))return x.map(canonical);
 if(x&&typeof x==='object')return Object.fromEntries(Object.keys(x).sort().map(k=>[k,canonical(x[k])]));
 return x;
}
export const same=(a,b)=>JSON.stringify(canonical(a))===JSON.stringify(canonical(b));
function require(c,message){if(!c)throw new RangeError(message);}
function keys(x,expected){require(x&&typeof x==='object'&&!Array.isArray(x)&&same(Object.keys(x).sort(),[...expected].sort()),'invalid trace fields');}
function alphabet(xs){
 require(Array.isArray(xs)&&xs.length>0&&xs.every(x=>typeof x==='string'&&x.length)&&new Set(xs).size===xs.length,'distinct nonempty alphabet labels required');
 if(xs.length>MAX_ALPHABET)throw new NativeTraceResourceError('alphabet execution limit');
 let width=1;while(2**width<xs.length)width++;return width;
}
function symbols(xs,k){
 require(Array.isArray(xs)&&xs.every(x=>Number.isSafeInteger(x)&&x>=0&&x<k),'invalid input symbol');
 if(xs.length>MAX_WORD)throw new NativeTraceResourceError('word execution limit');
}
export function packetSnapshot(rules,id){
 const p=rules.packets[id],c=rules.charts[p.chart],cell=rules.geometry.cells[c.cell];
 return {packet:copy(p),chart:copy(c),cell:{id:cell.id,key:cell.key,vertices:[...cell.vertices],
  owner:{kind:cell.owner.kind,origin:[...cell.owner.origin],inverted:cell.owner.inverted,key:cell.owner.key}}};
}
function choose(rules,current,kind){
 require(['PN','inverse-PN','reader-phase-advance'].includes(kind),'not a word-trace operation');
 const choices=rules.outgoing(current).map(i=>rules.operations[i]).filter(op=>op.kind===kind);
 require(choices.length===1,'required native operation is not uniquely available');
 const op=choices[0];require(rules.validateTransfer(op)===true,'native transfer validation failed');return op;
}
function event(rules,op,ordinal){
 const p=rules.packets[op.source],t=rules.packets[op.target],a=rules.charts[p.chart],b=rules.charts[t.chart];
 return {ordinal,kind:op.kind,source:packetSnapshot(rules,op.source),target:packetSnapshot(rules,op.target),
  face:copy(op.face),phaseDelta:op.phaseDelta,permutation:[...op.permutation],
  phaseFrames:{source:phaseFrame(a,p.origin),target:phaseFrame(b,t.origin)},
  phaseWitness:op.phaseDelta===1?phaseAdvanceWitness(a,b,p.origin):null};
}
export function replayTrace(trace){
 keys(trace,['schema','alphabet','seed','events','endpoint']);require(trace.schema===SCHEMA,'wrong trace schema');alphabet(trace.alphabet);
 require(Array.isArray(trace.events),'events must be an ordered list');
 if(trace.events.length>MAX_EVENTS)throw new NativeTraceResourceError('trace execution limit');
 const rules=new GenerativeAssemblyRules();let current=rules.root;
 require(same(trace.seed,packetSnapshot(rules,current)),'trace has no canonical admitted seed');
 for(let i=0;i<trace.events.length;i++){
  const row=trace.events[i];keys(row,['ordinal','kind','source','target','face','phaseDelta','permutation','phaseFrames','phaseWitness']);
  require(row.ordinal===i,'lost occurrence order');
  const op=choose(rules,current,row.kind),expected=event(rules,op,i);
  require(same(row,expected),'native packet, coefficient, face or phase witness changed');current=op.target;
 }
 require(same(trace.endpoint,packetSnapshot(rules,current)),'native endpoint changed');
 return {rules,current};
}
function decodeChecked(trace){
 const bits=[];
 for(let i=0;i<trace.events.length;){
  const first=trace.events[i];
  if(first.kind==='reader-phase-advance'){
   require(first.source.chart.species==='proton'&&first.target.chart.species==='proton','word reader step must be P to P');bits.push(1);i++;
  }else{
   const second=trace.events[i+1];
   require(first.kind==='PN'&&second?.kind==='inverse-PN','zero bit needs PN followed by inverse-PN');
   require(same(first.source,second.target),'zero-bit loop did not restore the whole packet');bits.push(0);i+=2;
  }
 }
 const width=alphabet(trace.alphabet);require(bits.length%width===0,'incomplete symbol code');
 const result=[];
 for(let i=0;i<bits.length;i+=width){const symbol=bits.slice(i,i+width).reduce((n,b)=>2*n+b,0);require(symbol<trace.alphabet.length,'unused binary code');result.push(symbol);}
 symbols(result,trace.alphabet.length);return result;
}
export function decodeWord(trace){replayTrace(trace);return decodeChecked(trace);}
export function verifyWord(trace,expectedAlphabet,expected){alphabet(expectedAlphabet);require(same(trace.alphabet,expectedAlphabet),'task codebook changed');symbols(expected,expectedAlphabet.length);require(same(decodeWord(trace),expected),'trace is a different word');return true;}
export function appendWord(prefix,word){
 const old=decodeWord(prefix),width=alphabet(prefix.alphabet);symbols(word,prefix.alphabet.length);symbols([...old,...word],prefix.alphabet.length);
 const {rules,current:start}=replayTrace(prefix),result=copy(prefix);let current=start;
 const take=kind=>{const op=choose(rules,current,kind);result.events.push(event(rules,op,result.events.length));current=op.target;};
 for(const symbol of word)for(const bit of symbol.toString(2).padStart(width,'0')){
  require(rules.charts[rules.packets[current].chart].species==='proton','code boundary must be P');
  if(bit==='0'){const before=packetSnapshot(rules,current);take('PN');take('inverse-PN');require(same(before,packetSnapshot(rules,current)),'PN inverse lost complete packet');}
  else take('reader-phase-advance');
 }
 if(result.events.length>MAX_EVENTS)throw new NativeTraceResourceError('trace execution limit');
 result.endpoint=packetSnapshot(rules,current);return result;
}
export function encodeWord(labels,word){
 alphabet(labels);symbols(word,labels.length);
 const rules=new GenerativeAssemblyRules(),seed=packetSnapshot(rules,rules.root);
 return appendWord({schema:SCHEMA,alphabet:[...labels],seed,events:[],endpoint:copy(seed)},word);
}
