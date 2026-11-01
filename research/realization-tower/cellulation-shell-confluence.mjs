import {buildShellFace} from './cellulation-shell.mjs';
import {packCellulation} from './cellulation-geometry.mjs';
import {buildShellWitnessPlan,validateShellWitnessPlan} from './cellulation-shell-witness.mjs';

const rounded=v=>v.map(x=>Math.round(x*1e9)/1e9);
const pointKey=(p,size)=>p.map(x=>Math.round(x*Math.SQRT2/size)).join(',');
const geometryKey=(ps,size)=>ps.map(p=>pointKey(p,size)).sort().join('|');
const sorted=map=>[...map].sort(([a],[b])=>a.localeCompare(b));
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
export function advanceShellWitnessState(initial,plan){
 validateShellWitnessPlan(plan);if(!plan.complete)throw Error('Cannot advance an incomplete witness plan');
 const owners=new Map(plan.events.map(e=>[e.id,e.cell]));
 return {arrows:[...initial.arrows,...plan.arrows],anchors:[...initial.anchors,...plan.dots.map(d=>({id:d.id,point:d.point,normal:d.normal,colour:d.colour,solid:true,writer:owners.get(d.event)}))],faces:[...(initial.faces??[]),...plan.faces],cells:[...initial.cells,...plan.cells.map(c=>c.cell)]};
}
export function shellSemanticOutcome(state,size=1){
 const arrows=new Map(),dots=new Map(),faces=new Map(),cells=new Map(),ownership=new Map();
 for(const a of state.arrows){const key=`${pointKey(a.from,size)}>${pointKey(a.to,size)}:${a.colour??a.color}`;arrows.set(key,true);}
 for(const a of state.anchors)if(a.solid)dots.set(pointKey(a.point,size),{id:a.id,colour:a.colour,normal:rounded(a.normal)});
 for(const f of state.faces??[])faces.set(geometryKey(f.vertices,size),{colour:f.colour,source:f.source});
 for(const c of state.cells){cells.set(geometryKey(c.vertices,size),{id:c.id,kind:c.kind});for(const f of c.faces){const key=geometryKey(f,size);if(!ownership.has(key))ownership.set(key,[]);ownership.get(key).push(c.id);}}
 return {arrows:sorted(arrows),dots:sorted(dots),faces:sorted(faces),cells:sorted(cells),faceOwnership:sorted(new Map([...ownership].map(([k,v])=>[k,v.sort()])))};
}
export function compareShellOutcomes(a,b){
 const differences=[];
 for(const field of ['arrows','faces','cells','faceOwnership']){
  const left=new Map(a[field]),right=new Map(b[field]);
  for(const key of new Set([...left.keys(),...right.keys()]))if(!equal(left.get(key),right.get(key)))differences.push({field,key,left:left.get(key)??null,right:right.get(key)??null});
 }
 const left=new Map(a.dots),right=new Map(b.dots);
 for(const key of new Set([...left.keys(),...right.keys()]))for(const property of ['id','colour','normal'])if(!equal(left.get(key)?.[property],right.get(key)?.[property]))differences.push({field:`dots.${property}`,key,left:left.get(key)?.[property]??null,right:right.get(key)?.[property]??null});
 return differences;
}
export function permutations(values){return values.length?values.flatMap((value,i)=>permutations(values.filter((_,j)=>i!==j)).map(rest=>[value,...rest])):[[]];}
export function auditShellFaceOrders(baseModel,initial){
 let baseline=null;const differingTrialsByField={},examples=[],incomplete=[],affected={};
 for(const order of permutations([0,1,2,3])){
  let model=baseModel,state=initial,blocked=false;
  for(const index of order){
   const shellFace=buildShellFace(model,index);model={...packCellulation([...model.cells,...shellFace.newCells],'cellulation-step'),step:model.step+1,cellSize:model.cellSize,previous:model,shellFace};
   const plan=buildShellWitnessPlan(model,state);
   if(!plan.complete){incomplete.push({order,index,blockers:plan.blockers});blocked=true;break;}
   state=advanceShellWitnessState(state,plan);
  }
  if(blocked)continue;
  const outcome=shellSemanticOutcome(state,model.cellSize);if(!baseline)baseline=outcome;
  const differences=compareShellOutcomes(baseline,outcome);
  for(const field of new Set(differences.map(d=>d.field)))differingTrialsByField[field]=(differingTrialsByField[field]??0)+1;
  for(const d of differences){affected[d.field]??=new Set();affected[d.field].add(d.key);}
  if(differences.length&&examples.length<4)examples.push({order,differences:differences.slice(0,8)});
 }
 return {status:Object.keys(differingTrialsByField).length?'order-dependent':'no-counterexample-in-tested-orders',tested:24,completed:24-incomplete.length,incomplete,differingTrialsByField,affectedKeysByField:Object.fromEntries(Object.entries(affected).map(([k,v])=>[k,[...v].sort()])),examples,scope:'All 24 macro-face orders, using the canonical eligible-cell order within each face. Not all combinations of macro, cell and arrow interleavings.'};
}
function shuffle(values,seed){const result=[...values];let state=seed>>>0;for(let i=result.length-1;i>0;i--){state=(Math.imul(state,1664525)+1013904223)>>>0;const j=state%(i+1);[result[i],result[j]]=[result[j],result[i]];}return result;}
export function auditShellCellOrders(model,initial,{randomTrials=32,seed=20260721}={}){
 const baseline=buildShellWitnessPlan(model,initial);if(!baseline.complete)throw Error('Baseline construction is blocked');
 const before=shellSemanticOutcome(advanceShellWitnessState(initial,baseline),model.cellSize),baseOrder=baseline.cells.map(c=>c.cell.id),byId=new Map(model.shellFace.newCells.map(c=>[c.id,c]));
 const counts={},affected={},outcomes=new Set(),orders=new Set(),examples=[];let trials=0,incomplete=0,adjacentWitness=null,arrivalTrials=0,arrivalConflicts=0;
 function check(order,octahedronOrder,label,adjacent=null){
  const reordered={...model,shellFace:{...model.shellFace,newCells:order.map(id=>byId.get(id))}},plan=buildShellWitnessPlan(reordered,initial,{octahedronOrder});trials++;
  if(!plan.complete){incomplete++;examples.push({label,blockers:plan.blockers});return;}
  const actualOrder=plan.cells.map(c=>c.cell.id);orders.add(JSON.stringify(actualOrder));
  const after=shellSemanticOutcome(advanceShellWitnessState(initial,plan),model.cellSize),differences=compareShellOutcomes(before,after);outcomes.add(JSON.stringify(after));
  for(const field of new Set(differences.map(d=>d.field)))counts[field]=(counts[field]??0)+1;
  for(const d of differences){affected[d.field]??=new Set();affected[d.field].add(d.key);}
  if(label.startsWith('arrivals:')){arrivalTrials++;if(differences.length)arrivalConflicts++;}
  if(differences.length&&examples.length<4)examples.push({label,order:actualOrder,octahedronOrder,differences:differences.slice(0,8)});
  if(adjacent&&!adjacentWitness&&equal(actualOrder,order)&&differences.length){
   const first=differences.find(d=>d.field.startsWith('dots.'))??differences[0],writers=plan=>plan.dots.filter(d=>pointKey(d.point,model.cellSize)===first.key).map(d=>({cell:plan.events.find(e=>e.id===d.event).cell,colour:d.colour,normal:rounded(d.normal)}));
   adjacentWitness={kind:'two-adjacent-cell counterexample',prefix:baseOrder.slice(0,adjacent.index),leftOrder:baseOrder,rightOrder:actualOrder,cells:adjacent.cells,firstDifference:first,leftWriter:writers(baseline),rightWriter:writers(plan),differences};
  }
 }
 check(baseOrder,[0,1,2,3],'baseline');check([...baseOrder].reverse(),[0,1,2,3],'reverse-priority');
 for(let i=0;i<baseOrder.length-1;i++){const order=[...baseOrder];[order[i],order[i+1]]=[order[i+1],order[i]];check(order,[0,1,2,3],`adjacent:${i}`,{index:i,cells:baseOrder.slice(i,i+2)});}
 for(let i=0;i<randomTrials;i++)check(shuffle(baseOrder,seed+i),[0,1,2,3],`shuffle:${seed+i}`);
 for(const order of permutations([0,1,2,3]))check(baseOrder,order,`arrivals:${order.join(',')}`);
 return {step:model.step,status:Object.keys(counts).length?'order-dependent':'no-counterexample-in-tested-orders',trials,uniqueCellSchedules:orders.size,distinctSemanticOutcomes:outcomes.size,incompleteSchedules:incomplete,differingTrialsByField:counts,affectedKeysByField:Object.fromEntries(Object.entries(affected).map(([k,v])=>[k,[...v].sort()])),octahedralArrivalOrders:{tested:arrivalTrials,conflicting:arrivalConflicts,scope:'Each permutation is applied uniformly to all octahedra; arbitrary independent per-cell combinations are not exhausted.'},adjacentWitness,examples,scope:'Actual planner reruns from identical retained input. Whole-cell transactions remain atomic; tetrahedral internal witness order is fixed. Cell-order search is bounded, not an all-schedules confluence proof. Timings, first-writer provenance and neutral scaffold draw order are excluded from semantic equality.'};
}
