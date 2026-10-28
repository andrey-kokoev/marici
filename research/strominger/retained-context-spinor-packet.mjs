// Experimental coordinate adapter over the existing native five-slot grammar.
// No new native operation, signed-pair binding, physical spin action or route.
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../nima/generative-phase-assembly.mjs';
import {activePhaseSlots,phaseFrame,phaseAdvanceWitness,applyPhasePermutation} from './demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const copy=x=>structuredClone(x),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const zero=x=>x===0?0:x;
const scale=(z,a)=>z.map(x=>zero(x*a)),add=(a,b)=>a.map((x,i)=>zero(x+b[i]));
const checkFive=value=>applyPhasePermutation(value,[0,1,2,3,4]).map(z=>z.map(zero));
export function splitCoordinates(species,value){
 value=checkFive(value);const slots=activePhaseSlots[species];if(!slots)throw Error('Unknown native species');
 const [a,b,c]=slots.map(i=>value[i]),outside=[0,1,2,3,4].filter(i=>!slots.includes(i));
 const contrast=[scale(add(a,scale(b,-1)),1/Math.sqrt(2)),scale(add(add(a,b),scale(c,-2)),1/Math.sqrt(6))];
 const mean=scale(add(add(a,b),c),1/Math.sqrt(3)),norm=contrast.flat().reduce((s,x)=>s+x*x,0);
 checkFive([...contrast,mean,...outside.map(i=>value[i])]);
 if(!Number.isFinite(norm)||(norm===0&&contrast.flat().some(x=>x!==0)))throw Error('Contrast norm outside numerical packet range');
 return {activeSlots:[...slots],contrast,context:{outside:outside.map(slot=>({slot,value:copy(value[slot])})),mean},contrastNormSquared:norm,
  // Columns z and Jz; unnormalized, no extra independent partner.
  pairedFrame:norm===0?null:[[contrast[0],[zero(-contrast[1][0]),contrast[1][1]]],[contrast[1],[contrast[0][0],zero(-contrast[0][1])]]],
  interpretation:'contrast coordinates; physical spinor identification remains conditional'};
}
export function joinCoordinates(species,packet){
 if(!packet?.context||packet.context.outside?.length!==2||packet.contrast?.length!==2)throw Error('Missing retained context or contrast');
 const slots=activePhaseSlots[species],outside=[0,1,2,3,4].filter(i=>!slots.includes(i));
 if(!same(packet.activeSlots,slots)||!same(packet.context.outside.map(x=>x.slot),outside))throw Error('Wrong coordinate occurrence slots');
 const [a,b]=packet.contrast,m=packet.context.mean,out=Array.from({length:5},()=>[0,0]);
 out[slots[0]]=add(add(scale(a,1/Math.sqrt(2)),scale(b,1/Math.sqrt(6))),scale(m,1/Math.sqrt(3)));
 out[slots[1]]=add(add(scale(a,-1/Math.sqrt(2)),scale(b,1/Math.sqrt(6))),scale(m,1/Math.sqrt(3)));
 out[slots[2]]=add(scale(b,-2/Math.sqrt(6)),scale(m,1/Math.sqrt(3)));
 for(const item of packet.context.outside)out[item.slot]=copy(item.value);return checkFive(out);
}
function occurrenceFrame(chart,origin){const {id,...frame}=phaseFrame(chart,origin);return frame;}
function cleanWitness(w){const {id:fromId,...from}=w.from,{id:toId,...to}=w.to;return {...w,from,to};}
export function createRetainedContextMachine(coefficients,{rules=new GenerativeAssemblyRules()}={}){
 const seed=checkFive(coefficients);
 const describe=id=>{const p=rules.packets[id],c=rules.charts[p.chart];return {species:c.species,origin:p.origin,permutation:[...p.permutation],aliases:copy(c.aliases),primitiveVertices:[...rules.geometry.cells[c.cell].vertices].sort(),occurrences:occurrenceFrame(c,p.origin)};};
 const root={coefficients:copy(seed),native:describe(rules.root)};
 const event=op=>{
  rules.validateTransfer(op);const a=rules.packets[op.source],b=rules.packets[op.target],ca=rules.charts[a.chart],cb=rules.charts[b.chart];
  return {kind:op.kind,permutation:[...op.permutation],face:op.face?[...op.face].sort():null,source:describe(op.source),target:describe(op.target),phaseWitness:op.phaseDelta?cleanWitness(phaseAdvanceWitness(ca,cb,a.origin)):null};
 };
 const pack=(id,value,history)=>{const native=describe(id),inverse=native.permutation.map((_,i)=>native.permutation.indexOf(i));return {schema:'native.retained-context-spinor-packet.v1',constructionAdmitted:false,root:copy(root),history:copy(history),historyCommitment:createHash('sha256').update(JSON.stringify({root,history})).digest('hex'),native,coordinates:splitCoordinates(native.species,value),movingFrame:{currentSlotsForRootCoordinates:inverse,rootCoordinates:applyPhasePermutation(value,inverse),anchor:copy(root.native)}};};
 const replay=packet=>{
  if(!same(packet?.root,root)||!Array.isArray(packet.history))throw Error('Wrong anchored source or missing native history');
  let id=rules.root,value=copy(seed);const history=[];
  for(const retained of packet.history){
   const matches=rules.outgoing(id).map(index=>rules.operations[index]).filter(op=>same(event(op),retained));
   if(matches.length!==1)throw Error('Unadmitted transfer or corrupted native occurrence/history witness');
   const op=matches[0];value=applyPhasePermutation(value,op.permutation);id=op.target;history.push(event(op));
  }
  const expected=pack(id,value,history);if(!same(packet,expected))throw Error('Packet coordinates, frame, context or provenance do not replay');
  return {id,value};
 };
 return {
  initial:()=>pack(rules.root,seed,[]),
  validate:packet=>{replay(packet);return true;},
  decode:packet=>copy(replay(packet).value),
  choices:packet=>rules.outgoing(replay(packet).id).map(index=>event(rules.operations[index])),
  step:(packet,selected)=>{const {id,value}=replay(packet),ops=rules.outgoing(id).map(index=>rules.operations[index]),matches=ops.filter(op=>same(event(op),selected));if(matches.length!==1)throw Error('Operation not admitted at this packet');const op=matches[0];return pack(op.target,applyPhasePermutation(value,op.permutation),[...packet.history,event(op)]);},
  serialize:packet=>{replay(packet);return JSON.stringify(packet);},
  restore:text=>{const packet=JSON.parse(text);replay(packet);return copy(packet);}
 };
}
