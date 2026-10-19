import {localReferences} from './local-reference-data.mjs';
import {phaseUniverse} from './local-reference-universe.mjs';
import {itemKey} from './lattice-items.mjs';
const copy=x=>structuredClone(x),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b),cache=new Map();
const scope='Local contact/exit reference only; global field sewing and physical stability not established. Display prefixes are not certified synthesis steps.';
export const localReferenceIds=Object.freeze(Object.keys(localReferences));
function checked(id){
 if(cache.has(id))return cache.get(id);const data=localReferences[id];if(!data)throw Error('Unknown local reference');
 const {witness:w}=data,u=phaseUniverse({maxOrigin:data.maxOrigin,maxPackets:5000}),{rules}=u;if(!u.complete)throw Error('Incomplete viewer replay');
 const ids=w.packets.map(p=>p.id),selected=new Set(ids);
 if(!same([...ids].sort((a,b)=>a-b),w.selectedPackets)||!same(w.packets,ids.map(p=>rules.packets[p]))||!same(w.charts,[...new Set(ids.map(p=>rules.packets[p].chart))].map(c=>rules.charts[c])))throw Error('Saved packet/chart mismatch');
 const reached=new Set([rules.root]);for(const i of w.word){const op=rules.operations[i];if(!u.operations.includes(i)||!reached.has(op.source)||!selected.has(op.target)||reached.has(op.target))throw Error('Invalid reference construction');rules.validateTransfer(op);reached.add(op.target);if(!rules.describe([...reached]).valid)throw Error('Invalid reference prefix');}
 if(reached.size!==selected.size)throw Error('Unrooted reference');
 const audit=rules.inspect(ids);if(!audit.certifiedExit||!same(audit.counts,data.target))throw Error('Reference failed contact/exit inspection');
 const bodies=[...rules.describe(ids).bodies].map(([cell,species])=>({cell,species,key:rules.geometry.cells[cell].key,vertices:rules.geometry.cells[cell].vertices.map(v=>rules.geometry.points.get(v))}));if(!same(bodies,w.bodies))throw Error('Saved body mismatch');
 const items=bodies.map((b,i)=>({...copy(b),id:i,kind:'tetrahedron',components:[copy(b.vertices)],faces:[[0,2,1],[0,1,3],[0,3,2],[1,2,3]].map(f=>f.map(j=>copy(b.vertices[j]))),center:[0,1,2,3].map(j=>b.vertices.reduce((s,v)=>s+v[j],0)/4)}));
 for(const item of items)if(item.key!==itemKey(item.vertices))throw Error('Body coordinate mismatch');
 const roles=new Map();for(const c of w.charts)for(const [mark,vertex] of Object.entries(c.aliases)){if(roles.has(vertex)&&roles.get(vertex)!==mark[0])throw Error('Conflicting vertex role');roles.set(vertex,mark[0]);}
 const result={items,roles,audit};cache.set(id,result);return result;
}
// Same reversible-display interface as createAssemblyDisplay, but never
// masquerades as its stronger phase-first-whole-assembly certificate.
export function createLocalReferenceDisplay(id,{loop=true,initiallyAssembled=true}={}){
 const {items,roles,audit}=checked(id);let shown=initiallyAssembled?items.length:1;
 function snapshot(){
  const visible=copy(items.slice(0,shown)),points=new Map(visible.flatMap(i=>i.vertices.map(p=>[p.join(','),p]))),bindings=Object.fromEntries(points),displayBindings={};
  // Label only globally checked C/M roles; no invented absolute phase indices.
  const displayVertexLabels=[...points].map(([vertex,point])=>({vertex,point,text:roles.get(vertex)??'?',occurrences:visible.flatMap((item,itemIndex)=>item.vertices.some(p=>p.join(',')===vertex)?[{itemIndex}]:[])}));
  const counts=Object.fromEntries(['proton','neutron','electron'].map(s=>[s,visible.filter(i=>i.species===s).length]));
  return {atomTrial:id,status:shown===items.length?'complete':'ready',identity:'local-reference',items:visible,bindings,displayBindings,displayVertexLabels,history:[],events:[],candidates:[],added:shown-1,counts,construction:{kind:'local-reference-display',scope},phaseAudit:{status:'local-contact-exit-certified',completeReferenceOnly:true,globalSewingAsserted:false,counts:audit.counts,scope},assemblyDisplay:{shown,total:items.length,canPrevious:loop||shown>1,canNext:loop||shown<items.length,loop,phaseStatus:'local-contact-exit-certified',mode:'local-reference'},entry:{point:copy(items[0].center)},exit:{point:null,reached:false},tunnel:{position:shown-1,scope}};
 }
 function setShown(n){if(!Number.isInteger(n)||n<1||n>items.length)throw RangeError('Invalid displayed item count');shown=n;return snapshot();}
 return {snapshot,setShown,fullItems:()=>copy(items),next:()=>setShown(shown<items.length?shown+1:loop?1:shown),previous:()=>setShown(shown>1?shown-1:loop?items.length:shown)};
}
