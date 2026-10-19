import {auditNamedConstruction} from './phase-discipline-model.mjs';
import {auditPhaseAssembly} from './phase-assembly-model.mjs';
import {itemKey} from './lattice-items.mjs';
const copy=x=>structuredClone(x);
// Reversible assembly DISPLAY, never a transport or between-element law.
export function createAssemblyDisplay(factory,{loop=false,initiallyAssembled=false}={}){
 const model=factory(),initial=model.snapshot(),whole=initial.construction?.kind==='phase-first-whole-assembly';
 let prefixes=[initial],referenceAudit=null;
 if(whole){
  const reference=model.reference();referenceAudit=auditPhaseAssembly(reference);
  if(JSON.stringify(initial.items.map(i=>i.key).sort())!==JSON.stringify([...reference.certificate.requiredCells].sort()))throw Error('Display does not contain the phase-certified assembly');
  initial.items.forEach((item,i)=>{const view=initial.phaseViews[i];
   if(item.key!==itemKey(item.vertices)||item.species!==view.frame.species||!reference.certificate.states.some(s=>s.cell===item.key&&s.chart===view.chart&&s.origin===view.origin&&JSON.stringify(s.history)===JSON.stringify(view.history)&&JSON.stringify(s.frame)===JSON.stringify(view.frame)))throw Error('Display frame lacks an actual phase-history witness');
  });
  prefixes=initial.items.map((_,i)=>{const state=copy(initial);state.items=state.items.slice(0,i+1);state.phaseViews=state.phaseViews.slice(0,i+1);state.counts=Object.fromEntries(['proton','neutron','electron'].map(s=>[s,state.items.filter(x=>x.species===s).length]));state.status=i===initial.items.length-1?'complete':'ready';state.added=i;return state;});
 }
 while(prefixes.at(-1).status==='ready'){
  const next=model.step(),before=prefixes.at(-1);
  if(!next.committed||next.items.length!==before.items.length+1||JSON.stringify(next.items.slice(0,-1))!==JSON.stringify(before.items))throw Error('Expected one retained carrier per display prefix');
  prefixes.push(next);if(prefixes.length>1000)throw Error('Unbounded assembly display');
 }
 const complete=prefixes.at(-1),audit=referenceAudit??auditNamedConstruction(complete),native=audit.status==='native-phase-compatible';
 const vertices=[...new Set(complete.items.flatMap(i=>i.vertices.map(p=>JSON.stringify(p))))].sort(),neutral=new Map(vertices.map((p,i)=>[p,'vertex-'+i]));let cursor=initiallyAssembled?prefixes.length-1:0;
 function snapshot(){
  const state=copy(prefixes[cursor]),visible=new Set(state.items.flatMap(i=>i.vertices.map(p=>JSON.stringify(p))));
  const view=whole?state.phaseViews.at(-1):null;
  state.displayVertexLabels=[];
  if(whole){
   const grouped=new Map(),counts={proton:0,neutron:0,electron:0};
   state.phaseViews.forEach((v,itemIndex)=>{
    const species=state.items[itemIndex].species,owner=({proton:'P',neutron:'N',electron:'E'})[species]+(++counts[species]);
    [...v.frame.window,v.frame.context].forEach((o,slot)=>{
     if(!grouped.has(o.vertex))grouped.set(o.vertex,{vertex:o.vertex,point:copy(state.bindings[o.vertex]),occurrences:[]});
     grouped.get(o.vertex).occurrences.push({itemIndex,itemKey:state.items[itemIndex].key,owner,origin:v.origin,role:o.role,index:o.index,context:slot===3});
    });
   });
   state.displayVertexLabels=[...grouped.values()].map(label=>{
    const names=[...new Set(label.occurrences.map(o=>o.role+o.index))].sort((a,b)=>a[0].localeCompare(b[0])||Number(a.slice(1))-Number(b.slice(1)));
    return {...label,text:names.join(' / ')};
   });
   state.displayBindings=Object.fromEntries(state.displayVertexLabels.map(label=>[label.vertex,copy(label.point)]));
  }else state.displayBindings=native?copy(state.bindings):Object.fromEntries([...visible].map(p=>[neutral.get(p),JSON.parse(p)]));
  state.displayPhase=view?{origin:view.origin,frame:copy(view.frame),word:view.frame.window.map(o=>o.role+o.index).join(' ')+' ['+view.frame.context.role+view.frame.context.index+']',scope:'Current item’s witnessed reader, not permanent vertex names'}:null;
  state.phaseAudit=copy(audit);state.assemblyDisplay={shown:state.items.length,total:complete.items.length,canPrevious:loop||cursor>0,canNext:loop||cursor<prefixes.length-1,loop,phaseStatus:audit.status,mode:whole?'phase-reference':native?'native-template':'geometry-only'};
  state.tunnel.position=state.items.length-1;return state;
 }
 function next(){if(cursor<prefixes.length-1)cursor++;else if(loop)cursor=0;return snapshot();}
 function previous(){if(cursor>0)cursor--;else if(loop)cursor=prefixes.length-1;return snapshot();}
 function setShown(count){if(!Number.isInteger(count)||count<1||count>prefixes.length)throw RangeError('Invalid displayed item count');cursor=count-1;return snapshot();}
 return {snapshot,next,previous,setShown,fullItems:()=>copy(complete.items)};
}
