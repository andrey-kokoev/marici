// Experimental reader-transport extension, not a change to native generators.
import {GenerativeAssemblyRules} from '../nima/generative-phase-assembly.mjs';
const marks=['C0','M0','C1','M1'];
const key=p=>p.join(',');
export function composeFrames(p,q){return q.map(i=>p[i]);}
export function permuteReference(point,p){const out=Array(4);point.split(',').map(Number).forEach((x,i)=>out[p[i]]=x);return key(out);}
export const contextFrameActions=Object.freeze({L:Object.freeze([3,2,1,0]),R:Object.freeze([0,3,2,1])});
export function makeRetainedContextBraid(){
 const engine=new GenerativeAssemblyRules(),packet=engine.packets[engine.root],chart=engine.charts[packet.chart];
 const seed=Object.values(chart.aliases),support=new Set(seed),discovery=[];
 const queue=[...seed];
 for(let i=0;i<queue.length;i++)for(const [action,p] of Object.entries(contextFrameActions)){
  const point=permuteReference(queue[i],p);
  if(!support.has(point)){support.add(point);queue.push(point);discovery.push({action,from:queue[i],added:point});}
 }
 const central=marks.map(m=>chart.aliases[m]);
 // Identify each outside context using native P completion, not fitted points.
 const outside=central.map((_,i)=>{
  const p=[0,1,2,3].map(j=>(j+i)%4),bindings=Object.fromEntries(marks.map(m=>[m,permuteReference(chart.aliases[m],p)]));
  const e=new GenerativeAssemblyRules({seedBindings:bindings});return e.charts[e.packets[e.root].chart].aliases.C2;
 });
 const references=[...central,...outside];
 if(references.length!==new Set(references).size||references.some(v=>!support.has(v))||support.size!==references.length)throw Error('Native context completion does not match action closure');
 const slot=new Map(references.map((v,i)=>[v,i]));
 const permutation=p=>references.map(v=>{const i=slot.get(permuteReference(v,p));if(i===undefined)throw Error('Context bank is not closed');return i;});
 const push=(values,p)=>{if(values.length!==references.length)throw Error('Full retained context bank required');const out=Array(values.length);permutation(p).forEach((to,from)=>{out[to]=structuredClone(values[from]);});return out;};
 function reframe(state,action){
  const p=contextFrameActions[action];if(!p)throw Error('Unknown context action');
  const t=action==='L'?3-state.t:4-state.t;
  return {t,frame:composeFrames(p,state.frame),values:push(state.values,p),history:[...state.history,{action,before:state.t,after:t}]};
 }
 function view(values,frame){
  const base=[...central,outside[0]];
  return base.map(v=>structuredClone(values[slot.get(permuteReference(v,frame))]));
 }
 // Each native five-slot permutation is embedded as a swap of the matching
 // retained reference positions. Outside-bank values are never discarded.
 function nativeOperation(values,frame,permutation5){
  const indices=[...central,outside[0]].map(v=>slot.get(permuteReference(v,frame)));
  const out=structuredClone(values),input=indices.map(i=>structuredClone(values[i]));
  indices.forEach((to,i)=>{out[to]=input[permutation5[i]];});return out;
 }
 return {references,central,outside,discovery,seedReferences:seed,permutation,push,reframe,view,nativeOperation,
  initial(values){if(values.length!==references.length)throw Error('Full retained context bank required');return {t:0,frame:[0,1,2,3],values:structuredClone(values),history:[]};}};
}
