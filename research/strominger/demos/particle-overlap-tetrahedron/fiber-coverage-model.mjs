import {createWindowConstruction,windowProtocol} from './window-construction-model.mjs';
const canonical=value=>JSON.stringify(normalize(value));
function normalize(value){return Array.isArray(value)?value.map(normalize):value&&typeof value==='object'?Object.fromEntries(Object.keys(value).sort().map(k=>[k,normalize(value[k])])):value;}

// Graph kernel only: its caller must supply admitted state transitions.
// Intersect at STATE level before projecting onto cells. Equal cell locations
// do not identify different windows, histories, modes or frames.
export function auditStateCoverage({states,transitions,entryStates,exitStates,requiredCells}){
 if(![states,transitions,entryStates,exitStates,requiredCells].every(Array.isArray))throw Error('State graph and boundary lists must be arrays');
 const byId=new Map(states.map(s=>[s.id,s]));
 if(byId.size!==states.length||states.some(s=>typeof s.id!=='string'||typeof s.cell!=='string'))throw Error('State IDs must be unique and states must name their cells');
 const required=new Set(requiredCells);if(required.size!==requiredCells.length||requiredCells.some(c=>typeof c!=='string'||!c))throw Error('Required cells must have unique nonempty string keys');
 const forward=new Map(states.map(s=>[s.id,[]])),backward=new Map(states.map(s=>[s.id,[]]));
 for(const edge of transitions){if(!Array.isArray(edge)||edge.length!==2||!byId.has(edge[0])||!byId.has(edge[1]))throw Error('Transition refers to an unknown state');forward.get(edge[0]).push(edge[1]);backward.get(edge[1]).push(edge[0]);}
 for(const id of [...entryStates,...exitStates])if(!byId.has(id))throw Error('Unknown boundary state');
 for(const id of exitStates)if(forward.get(id).length)throw Error('Terminal exit state cannot have a forward continuation');
 function reachable(roots,edges){const seen=new Set(roots),queue=[...roots];for(let i=0;i<queue.length;i++)for(const next of edges.get(queue[i]))if(!seen.has(next)){seen.add(next);queue.push(next);}return seen;}
 const from=reachable(entryStates,forward),to=reachable(exitStates,backward),through=new Set([...from].filter(id=>to.has(id)));
 const project=set=>new Set([...set].map(id=>byId.get(id).cell));
 const fromCells=project(from),toCells=project(to),covered=project(through),modeled=new Set(states.map(s=>s.cell));
 const rows=[...required].map(cell=>({cell,modeled:modeled.has(cell),fromEntry:fromCells.has(cell),toExit:toCells.has(cell),covered:covered.has(cell)}));
 return {status:!entryStates.length||!exitStates.length?'pending-boundary':rows.every(r=>r.covered)?'covered':'incomplete',requiredCells:required.size,stateCount:states.length,
  entryExitRouteExists:exitStates.some(id=>from.has(id)),fromEntryCells:rows.filter(r=>r.fromEntry).length,toExitCells:rows.filter(r=>r.toExit).length,coveredCells:rows.filter(r=>r.covered).length,
  unmodeledCells:rows.filter(r=>!r.modeled).map(r=>r.cell),unreachableCells:rows.filter(r=>r.modeled&&!r.fromEntry).map(r=>r.cell),deadEndCells:exitStates.length?rows.filter(r=>r.fromEntry&&!r.toExit).map(r=>r.cell):[],
  incompatibleStateCells:rows.filter(r=>r.fromEntry&&r.toExit&&!r.covered).map(r=>r.cell),uncoveredCells:rows.filter(r=>!r.covered).map(r=>r.cell),coveredCellKeys:[...required].filter(cell=>covered.has(cell)),
  fromEntryStateIds:[...from],toExitStateIds:[...to],throughStateIds:[...through],deadEndStateIds:exitStates.length?[...from].filter(id=>!to.has(id)):[],allEnteredStatesReachExit:exitStates.length?[...from].every(id=>to.has(id)):null,rows};
}

// Admission adapter for the currently implemented protocol. Replay ONLY the
// supplied committed prefix and verify its full ledger against the constructor.
// Never add a seed at another proton or invent an electron-to-proton edge.
export function windowPrefixGraph(snapshot,namespace='window'){
 if(!snapshot.seed||snapshot.added!==snapshot.events?.length||snapshot.items?.length!==snapshot.added+1||snapshot.added<0||snapshot.added>=windowProtocol.length)throw Error('Invalid committed window prefix');
 const bindings=Object.fromEntries(windowProtocol[0].nodes.map(n=>[n,snapshot.bindings[n]]));
 const engine=createWindowConstruction({seed:snapshot.seed,bindings,identity:snapshot.identity,branch:snapshot.events[0]?.modeBefore.branch??snapshot.mode.branch,phaseExponent:snapshot.events[0]?.modeBefore.phaseExponent??snapshot.mode.phaseExponent});
 const prefixes=[engine.snapshot()];
 for(let i=0;i<snapshot.added;i++){const next=engine.step();if(!next.committed)throw Error('Unadmitted window transition');prefixes.push(next);}
 const expected=prefixes.at(-1);
 for(const field of ['seed','status','identity','entry','exit','items','bindings','history','mode','events','added'])if(canonical(snapshot[field])!==canonical(expected[field]))throw Error('Window admission mismatch: '+field);
 const states=prefixes.map((s,i)=>({id:namespace+':'+i,cell:s.items.at(-1).key,species:s.items.at(-1).species,window:[...s.items.at(-1).window],bindings:s.bindings,history:s.history,mode:s.mode,identity:s.identity}));
 return {states,transitions:states.slice(1).map((s,i)=>[states[i].id,s.id]),entryStates:[states[0].id],exitStates:expected.status==='complete'?[states.at(-1).id]:[],admission:'replayed-retained-window-prefix'};
}
export function auditWindowCoverage(snapshot,requiredCells){return auditStateCoverage({...windowPrefixGraph(snapshot),requiredCells});}
