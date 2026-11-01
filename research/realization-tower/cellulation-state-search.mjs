const sort=xs=>[...xs].map(value=>({key:JSON.stringify(value),value})).sort((a,b)=>a.key.localeCompare(b.key)).map(x=>x.value);
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function freeze(value){if(value&&typeof value==='object'&&!Object.isFrozen(value)){Object.values(value).forEach(freeze);Object.freeze(value);}return value;}
export function compileStateSpecification(spec){
 spec=freeze(structuredClone(spec));
 if(spec.schema!=='cellulation-event-state-v1')throw Error('Unknown frozen state schema');
 for(const [items,key] of [[spec.programs,'id'],[spec.cells,'id'],[spec.initial.dots,'key'],[spec.initial.faces,'key']])if(new Set(items.map(x=>x[key])).size!==items.length)throw Error('Ambiguous specification identity');
 const operations=spec.programs.flatMap(p=>p.operations.map(o=>({...o,program:p.id,cell:p.cell}))),byId=new Map();
 for(const [i,o] of operations.entries()){if(byId.has(o.id))throw Error('Duplicate operation');o.bit=1n<<BigInt(i);byId.set(o.id,o);}
 const cells=new Map(spec.cells.map(c=>[c.id,c]));
 if(new Set(spec.initial.cells).size!==spec.initial.cells.length||spec.initial.cells.some(id=>!cells.has(id)))throw Error('Unknown or duplicate retained cell');
 if(new Set(spec.targets).size!==spec.targets.length||spec.targets.some(id=>!cells.has(id)||spec.initial.cells.includes(id)))throw Error('Invalid target cells');
 for(const o of operations){
  if(!spec.targets.includes(o.cell))throw Error('Operation outside target');
  o.dependencies=(o.requires??[]).map(id=>{const dep=byId.get(id);if(!dep)throw Error(`Unknown prerequisite ${id}`);return dep;});
  for(const effect of o.effects)if(!['propose','solidify','arrow','face','commit'].includes(effect.type))throw Error('Unknown operation effect');
 }
 const visiting=new Set(),done=new Set();function visit(o){if(done.has(o.id))return;if(visiting.has(o.id))throw Error('Cyclic prerequisites');visiting.add(o.id);for(const d of o.dependencies)visit(d);visiting.delete(o.id);done.add(o.id);}operations.forEach(visit);
 operations.forEach(freeze);Object.freeze(operations);
 return {spec,operations,byId,cells};
}
export function initialEventState(compiled){
 const input=compiled.spec.initial;
 return {done:0n,owners:new Map(),dots:new Map(input.dots.map(d=>[d.key,{...d,retained:true,claims:d.claims??[],witnesses:d.witnesses??[]}])) ,arrows:new Set(input.arrows),faces:new Map(input.faces.map(f=>[f.key,{...f,retained:true,claims:f.claims??[]}])),cells:new Set(input.cells)};
}
export function operationEnabled(state,o){
 return !(state.done&o.bit)&&!state.cells.has(o.cell)&&(!state.owners.has(o.cell)||state.owners.get(o.cell)===o.program)&&o.dependencies.every(d=>state.done&d.bit)&&(o.requiresDots??[]).every(k=>state.dots.has(k))&&(o.requiresSolid??[]).every(k=>state.dots.get(k)?.solid)&&(o.requiresCells??[]).every(k=>state.cells.has(k))&&(o.requiresFaces??[]).every(k=>state.faces.has(k));
}
export function applyEventOperation(compiled,state,id){
 const o=compiled.byId.get(id);if(!o||!operationEnabled(state,o))throw Error(`Disabled operation: ${id}`);
 const next={...state,done:state.done|o.bit,owners:new Map(state.owners)};next.owners.set(o.cell,o.program);
 for(const effect of o.effects){
  if(effect.type==='propose'){
   next.dots=new Map(next.dots);const old=next.dots.get(effect.key),claim={operation:o.id,colour:effect.colour,normal:effect.normal};
   next.dots.set(effect.key,old?{...old,claims:sort([...old.claims,claim])}:{key:effect.key,id:`shell:${effect.key}`,colour:effect.colour,normal:effect.normal,solid:false,retained:false,first:o.id,claims:[claim],witnesses:[]});
  }else if(effect.type==='solidify'){
   const old=next.dots.get(effect.key);if(!old)throw Error('Solidification without a candidate');
   next.dots=new Map(next.dots);next.dots.set(effect.key,{...old,solid:true,witnesses:sort([...old.witnesses,o.id])});
  }else if(effect.type==='arrow'){next.arrows=new Set(next.arrows);next.arrows.add(effect.key);}
  else if(effect.type==='face'){
   next.faces=new Map(next.faces);const old=next.faces.get(effect.key);
   next.faces.set(effect.key,old?{...old,claims:sort([...old.claims,{operation:o.id,colour:effect.colour}])}:{key:effect.key,colour:effect.colour,source:effect.source,retained:false,claims:[{operation:o.id,colour:effect.colour}]});
  }else{
   const cell=compiled.cells.get(o.cell);if(cell.faces.some(k=>!next.faces.has(k))||cell.vertices.some(k=>!next.dots.get(k)?.solid))throw Error('Cell commitment without witnessed vertices and faces');
   next.cells=new Set(next.cells);next.cells.add(o.cell);
  }
 }
 return next;
}
export function eventStateOutcome(compiled,state){
 const ownership=new Map();for(const id of state.cells)for(const face of compiled.cells.get(id).faces){if(!ownership.has(face))ownership.set(face,[]);ownership.get(face).push(id);}
 return {arrows:sort(state.arrows),dots:sort([...state.dots].map(([key,d])=>[key,{id:d.id,colour:d.colour,normal:d.normal,solid:d.solid}])),faces:sort([...state.faces].map(([key,f])=>[key,{colour:f.colour,source:f.source}])),cells:sort(state.cells),faceOwnership:sort([...ownership].map(([k,v])=>[k,sort(v)]))};
}
export function eventOutcomeDifferences(left,right){
 const differences=[];
 for(const field of ['arrows','cells']){const a=new Set(left[field]),b=new Set(right[field]);for(const key of new Set([...a,...b]))if(a.has(key)!==b.has(key))differences.push({field,key,left:a.has(key),right:b.has(key)});}
 for(const field of ['dots','faces','faceOwnership']){const a=new Map(left[field]),b=new Map(right[field]);for(const key of new Set([...a.keys(),...b.keys()]))if(!same(a.get(key),b.get(key)))differences.push({field,key,left:a.get(key)??null,right:b.get(key)??null});}
 return differences;
}
function stateKey(state){
 // Exact key, not a hash: no collision assumption. Against one fixed spec,
 // completed operation bits determine owners, arrows, cells, solid flags and
 // ALL claim/witness multisets by monotone union of their immutable effects.
 // Only new dot/face selections depend on order and must be stored separately.
 // Retained selections and initial claim histories are fixed by the boundary.
 return JSON.stringify([state.done.toString(16),sort([...state.dots].filter(([,d])=>!d.retained).map(([k,d])=>[k,{first:d.first,colour:d.colour,normal:d.normal}])),sort([...state.faces].filter(([,f])=>!f.retained).map(([k,f])=>[k,{colour:f.colour,source:f.source}]))]);
}
export function replayEventTrace(compiled,trace,{requireComplete=true}={}){
 let state=initialEventState(compiled);for(const id of trace)state=applyEventOperation(compiled,state,id);
 if(requireComplete&&!compiled.spec.targets.every(id=>state.cells.has(id)))throw Error('Trace does not complete the target');return state;
}
export function freezeEventPrefix(compiled,state,programIds){
 if([...state.owners.keys()].some(id=>!state.cells.has(id)))throw Error('Only completed-cell prefixes can be frozen');
 const programs=compiled.spec.programs.filter(p=>programIds.includes(p.id));
 if(!programs.length||programs.length!==new Set(programIds).size)throw Error('Unknown prefix continuation program');
 return {...compiled.spec,prefix:{completedOperations:compiled.operations.filter(o=>state.done&o.bit).map(o=>o.id),selectedModes:sort(state.owners)},initial:{dots:[...state.dots.values()].map(d=>({...d})),arrows:sort(state.arrows),faces:[...state.faces.values()].map(f=>({...f})),cells:sort(state.cells)},targets:[...new Set(programs.map(p=>p.cell))],programs};
}
export function searchEventStates(compiled,{maxStates=2000,maxMilliseconds=15000,guideTraces=[]}={}){
 if(!Number.isInteger(maxStates)||maxStates<1||!Number.isFinite(maxMilliseconds)||maxMilliseconds<=0)throw Error('Positive explicit resource limits required');
 const start=Date.now(),visited=new Set(),completedPaths=new Map(),terminalOutcomes=new Map(),counterexamples=[],deadlocks=[],trace=[];let transitions=0,duplicateStates=0,searchTerminalStates=0,stopReason=null,first=null;
 function terminal(state,path,origin){
  const outcome=eventStateOutcome(compiled,state),key=JSON.stringify(outcome);if(terminalOutcomes.has(key))return;
  terminalOutcomes.set(key,true);if(!first)first={outcome,trace:[...path],origin};else{const differences=eventOutcomeDifferences(first.outcome,outcome);if(differences.length&&counterexamples.length<3)counterexamples.push({leftOrigin:first.origin,rightOrigin:origin,leftTrace:first.trace,rightTrace:[...path],differences});}
 }
 // Guide traces are independently replayed under this frozen event semantics;
 // they supply counterexamples, never search-coverage credit or pruning.
 for(const guide of guideTraces)terminal(replayEventTrace(compiled,guide.trace),guide.trace,guide.name);
 const root=initialEventState(compiled),rootKey=stateKey(root);visited.add(rootKey);const stack=[{state:root,key:rootKey,enabled:null,index:0,paths:0n}];
 function finish(frame,paths){completedPaths.set(frame.key,paths);stack.pop();if(stack.length)stack.at(-1).paths+=paths;if(trace.length)trace.pop();}
 while(stack.length){
  if(Date.now()-start>=maxMilliseconds){stopReason='time-limit';break;}
  const frame=stack.at(-1);
  if(frame.enabled===null){
   if(compiled.spec.targets.every(id=>frame.state.cells.has(id))){searchTerminalStates++;terminal(frame.state,trace,'state-search');finish(frame,1n);continue;}
   frame.enabled=compiled.operations.filter(o=>operationEnabled(frame.state,o));
   if(!frame.enabled.length){if(deadlocks.length<3)deadlocks.push({trace:[...trace],missingCells:compiled.spec.targets.filter(id=>!frame.state.cells.has(id))});finish(frame,0n);continue;}
  }
  if(frame.index===frame.enabled.length){finish(frame,frame.paths);continue;}
  const o=frame.enabled[frame.index++],next=applyEventOperation(compiled,frame.state,o.id);transitions++;
  const key=stateKey(next);if(visited.has(key)){duplicateStates++;const paths=completedPaths.get(key);if(paths===undefined)throw Error('Non-monotone state cycle');frame.paths+=paths;continue;}
  if(visited.size>=maxStates){frame.index--;stopReason='state-limit';break;}
  visited.add(key);trace.push(o.id);stack.push({state:next,key,enabled:null,index:0,paths:0n});
 }
 const complete=!stack.length;
 return {result:counterexamples.length||deadlocks.length?'counterexample-found':complete?'verified-for-frozen-model':'incomplete',coverage:complete?'complete':'incomplete',stopReason,visitedStates:visited.size,exploredTransitions:transitions,duplicateStates,distinctTerminalOutcomes:terminalOutcomes.size,searchTerminalStates,guideTraceCount:guideTraces.length,completeScheduleCount:complete?completedPaths.get(rootKey).toString():null,unprocessedFrontierEdges:stack.reduce((sum,f)=>sum+(f.enabled?f.enabled.length-f.index:1),0),elapsedMilliseconds:Date.now()-start,limits:{maxStates,maxMilliseconds},counterexamples,deadlocks,firstTerminalTrace:first?.trace??null,reduction:'None. All enabled completion events are explored; only exact canonical state deduplication is used.',scope:'Finite event-completion model. Continuous animation time is abstracted; every prerequisite and retained claim remains represented. Guide traces are excluded from coverage counts.'};
}
