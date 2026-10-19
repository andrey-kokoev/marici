import {createWindowConstruction,windowProtocol} from './window-construction-model.mjs';
import {windowPrefixGraph,auditStateCoverage} from './fiber-coverage-model.mjs';
const clone=x=>structuredClone(x),flip=b=>b==='common'?b:b==='positive'?'negative':'positive';
const mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i],0)/ps.length);
export const referenceCarrierMarks=Object.freeze([...new Set(windowProtocol.flatMap(p=>p.window))]);
function validateCoefficients(c,n){if(!Array.isArray(c)||c.length!==n||c.some(z=>!Array.isArray(z)||z.length!==2||z.some(x=>!Number.isFinite(x))))throw Error(`${n} finite complex coefficients are required`);}
function transfer(event){
 const stage=windowProtocol.findIndex((p,i)=>p.species===event.from&&windowProtocol[i+1]?.species===event.to);
 if(stage<0)throw Error('No admitted transfer for this species pair');
 const source=windowProtocol[stage].window,target=windowProtocol[stage+1].window;
 const outgoing=source.find(n=>!target.includes(n)),entering=target.find(n=>!source.includes(n));
 if(JSON.stringify(event.frameExchange)!==JSON.stringify([outgoing,entering])||JSON.stringify(event.orderedFace)!==JSON.stringify(target)||event.targetCycle!==(stage===0?'forward':'inverse'))throw Error('Incompatible ordered-window adapter');
 return {stage,permutation:target.map(n=>source.indexOf(n===entering?outgoing:n))};
}
// A conditional reference-frame map on C^3, not a native particle operator.
// The inverse is computed algebraically, never loaded from a saved payload.
export function transportWindowCoefficients(coefficients,event,direction=1){
 if(![1,-1].includes(direction))throw RangeError('Direction must be +1 or -1');
 validateCoefficients(coefficients,3);
 const {permutation}=transfer(event);
 if(direction===1)return permutation.map(i=>[...coefficients[i]]);
 const result=[];permutation.forEach((i,j)=>result[i]=[...coefficients[j]]);return result;
}
// Keep the full five-slot reference carrier, including the complement of the
// active window. M2 is geometric context, not an invented sixth native mode.
export function transportCarrierCoefficients(coefficients,event,direction=1){
 if(![1,-1].includes(direction))throw RangeError('Direction must be +1 or -1');
 validateCoefficients(coefficients,referenceCarrierMarks.length);transfer(event);
 const [a,b]=event.frameExchange.map(n=>referenceCarrierMarks.indexOf(n)),result=clone(coefficients);
 [result[a],result[b]]=[result[b],result[a]];return result; // each full-frame exchange is an involution
}
export function transportWindowMode(mode,event,direction=1){
 if(![1,-1].includes(direction)||!['common','positive','negative'].includes(mode.branch)||!Number.isInteger(mode.phaseExponent)||mode.phaseExponent<0||mode.phaseExponent>2)throw Error('Invalid mode or direction');
 const {stage}=transfer(event),sourceBranch=direction===-1&&stage===1?flip(mode.branch):mode.branch;
 const increment=sourceBranch==='common'?0:stage===0?(sourceBranch==='positive'?1:2):(sourceBranch==='positive'?2:1);
 return {branch:direction===1?(stage===1?flip(sourceBranch):sourceBranch):sourceBranch,phaseExponent:(mode.phaseExponent+direction*increment+3)%3};
}
export function windowModeCoefficients(mode){
 if(!mode||!['common','positive','negative'].includes(mode.branch)||!Number.isInteger(mode.phaseExponent)||mode.phaseExponent<0||mode.phaseExponent>2)throw Error('Invalid window mode');
 const sign=mode.branch==='common'?0:mode.branch==='positive'?1:-1;
 return [0,1,2].map(k=>{const angle=2*Math.PI*((mode.phaseExponent+sign*k+3)%3)/3;return [Math.cos(angle)/Math.sqrt(3),Math.sin(angle)/Math.sqrt(3)];});
}
export const identityBoundaryHypothesis='canonical-identity-hypothesis';
function boundarySteps(events,direction){
 if(![1,-1].includes(direction)||!Array.isArray(events)||events.length!==2||events.some((e,i)=>transfer(e).stage!==i))throw Error('Boundary requires the complete ordered P/N/E frame ledger');
 return direction===1?[...events].reverse().map(event=>({event,direction:-1})):events.map(event=>({event,direction:1}));
}
// Hypothesis, not a derived boundary law: with T the within-cycle frame map,
// choose canonical identity gluing, so B = T^-1 and B^-1 = T.
export function transportCycleBoundaryCoefficients(coefficients,events,direction){
 validateCoefficients(coefficients,5);
 return boundarySteps(events,direction).reduce((c,s)=>transportCarrierCoefficients(c,s.event,s.direction),clone(coefficients));
}
export function transportCycleBoundaryMode(mode,events,direction){return boundarySteps(events,direction).reduce((m,s)=>transportWindowMode(m,s.event,s.direction),{...mode});}
// Necessary typed-order check only; not a substitute for geometric admission.
export function isTypedWindowOrder(species,events,direction){
 if(![1,-1].includes(direction))throw RangeError('Direction must be +1 or -1');
 for(const event of events){transfer(event);if(species!==(direction===1?event.from:event.to))return false;species=direction===1?event.to:event.from;}return true;
}
export function createDeuteriumTunnel(options={}){
 const {complementCoefficients=[[0,0],[0,0]],realizationCycles=1,boundaryIdentification=null,...constructionOptions}=options;validateCoefficients(complementCoefficients,2);
 if(![1,2].includes(realizationCycles)||boundaryIdentification!==null&&boundaryIdentification!==identityBoundaryHypothesis||realizationCycles>1&&boundaryIdentification!==identityBoundaryHypothesis)throw Error('Two-cycle trials require explicit canonical-identity gluing');
 const construction=createWindowConstruction(constructionOptions);let position=0,cycle=0,mode={...construction.snapshot().mode};const passages=[],boundaryPassages=[],observed=new Set(['0:0']);
 const active=windowProtocol[0].window,initial=windowModeCoefficients(mode),complement=referenceCarrierMarks.filter(n=>!active.includes(n));
 const inputCarrier=referenceCarrierMarks.map(n=>[...(active.includes(n)?initial[active.indexOf(n)]:complementCoefficients[complement.indexOf(n)])]);
 let carrierCoefficients=clone(inputCarrier);
 function snapshot(){
  const state=construction.snapshot(),graph=windowPrefixGraph(state),keys=state.items.map(s=>s.key);
  let fiber=clone(inputCarrier);
  graph.states=graph.states.map((s,i)=>{if(i)fiber=transportCarrierCoefficients(fiber,state.events[i-1]);return {...s,referenceCarrier:clone(fiber)};});
  if(JSON.stringify(carrierCoefficients)!==JSON.stringify(graph.states[position].referenceCarrier)||JSON.stringify(mode)!==JSON.stringify(graph.states[position].mode))throw Error('Transported carrier disagrees with the retained fiber state');
  if(new Set(keys).size!==keys.length||graph.transitions.some(([a,b],i)=>a!==graph.states[i].id||b!==graph.states[i+1].id))throw Error('Construction is not a simple uninterrupted tunnel');
  const prefixCoverage=auditStateCoverage({...graph,exitStates:[graph.states.at(-1).id],requiredCells:keys});
  const current=state.items[position],frontier=state.items.at(-1),terminal=state.status==='complete';
  const guideEdges=state.events.flatMap((event,i)=>{const port=mean(event.face);return [[state.items[i].center,port],[port,state.items[i+1].center]];});
  return {...state,atomTrial:'deuterium',counts:Object.fromEntries(['proton','neutron','electron'].map(s=>[s,state.items.filter(i=>i.species===s).length])),
   tunnel:{position,window:[...current.window],species:current.species,mode:{...mode},coefficients:current.window.map(n=>[...carrierCoefficients[referenceCarrierMarks.indexOf(n)]]),referenceCarrier:{marks:[...referenceCarrierMarks],coefficients:clone(carrierCoefficients)},identity:state.identity,
    realizations:{cycle,count:realizationCycles,boundaryIdentification,assumed:boundaryIdentification!==null,observedStates:[...observed],requiredStates:3*realizationCycles,canNextCycle:terminal&&position===2&&cycle+1<realizationCycles,canPreviousCycle:terminal&&position===0&&cycle>0,boundaryPassages:clone(boundaryPassages)},
    frontier:{item:state.items.length-1,center:[...frontier.center],window:[...(state.candidates[0]?.window??frontier.window)],terminal},
    coverage:{required:3,built:state.items.length,covered:prefixCoverage.coveredCells,complete:terminal&&prefixCoverage.coveredCells===3,boundaryKind:terminal?'terminal-electron':'provisional-frontier'},
    interfaces:state.events.map((e,i)=>({from:state.items[i].key,to:state.items[i+1].key,face:clone(e.face),window:[...e.orderedFace]})),
    canTowardEntry:terminal&&position>0,canTowardExit:terminal&&position<state.items.length-1,fiberStates:graph.states.map(s=>({...clone(s),identity:state.identity})),guideEdges:clone(guideEdges),passages:clone(passages),
    scope:'One deuterium geometry, optionally viewed in two realization charts with explicitly assumed canonical-identity gluing. No physical boundary law or branching network is derived.'}};
 }
 function step(){
  const result=construction.step();
  if(result.committed){const event=result.events.at(-1);carrierCoefficients=transportCarrierCoefficients(carrierCoefficients,event);mode=transportWindowMode(mode,event);position=result.items.length-1;observed.add(cycle+':'+position);}
  return {...snapshot(),committed:result.committed};
 }
 function pass(direction){
  if(![1,-1].includes(direction))throw RangeError('Direction must be +1 or -1');
  const state=construction.snapshot(),next=position+direction;
  if(state.status!=='complete'||next<0||next>=state.items.length)return {...snapshot(),moved:false};
  const event=state.events[direction===1?position:next],before={...mode};
  carrierCoefficients=transportCarrierCoefficients(carrierCoefficients,event,direction);mode=transportWindowMode(mode,event,direction);
  passages.push({cycle,from:position,to:next,direction,face:clone(event.face),modeBefore:before,modeAfter:{...mode}});position=next;observed.add(cycle+':'+position);
  return {...snapshot(),moved:true};
 }
 function crossCycle(direction){
  if(![1,-1].includes(direction))throw RangeError('Direction must be +1 or -1');
  const state=construction.snapshot(),allowed=state.status==='complete'&&boundaryIdentification===identityBoundaryHypothesis&&(direction===1?position===2&&cycle+1<realizationCycles:position===0&&cycle>0);
  if(!allowed)return {...snapshot(),crossed:false};
  const from={cycle,position},before={...mode};
  carrierCoefficients=transportCycleBoundaryCoefficients(carrierCoefficients,state.events,direction);mode=transportCycleBoundaryMode(mode,state.events,direction);
  cycle+=direction;position=direction===1?0:2;observed.add(cycle+':'+position);
  boundaryPassages.push({kind:'assumed-realization-gluing',hypothesis:boundaryIdentification,direction,from,to:{cycle,position},modeBefore:before,modeAfter:{...mode},ordinarySpatialEdge:false});
  return {...snapshot(),crossed:true};
 }
 return {snapshot,step,pass,crossCycle};
}
