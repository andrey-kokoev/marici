// Import the retained words/context marks, NOT their reflected display coordinates.
import {trial} from './carrier.mjs';
import {makeLatticeItem,acrossFace,itemKey} from './lattice-items.mjs';
const faces=[[0,2,1],[0,1,3],[0,3,2],[1,2,3]];
const mean=points=>points.reduce((a,p)=>a.map((x,i)=>x+p[i]/points.length),[0,0,0,0]);
export const windowProtocol=Object.freeze(trial.bodies.map(b=>Object.freeze({species:b.id,nodes:Object.freeze([...b.nodes]),window:Object.freeze([...b.window]),continuation:b.continuation})));
const pointKey=p=>p.join(',');
function primitiveAcross(owner,current,face){
 const fk=itemKey(face),matches=c=>faces.some(f=>itemKey(f.map(i=>c[i]))===fk);
 let nextOwner=owner,candidates=owner.components.filter(c=>itemKey(c)!==itemKey(current)&&matches(c));
 if(!candidates.length){
  if(!owner.faces.some(f=>itemKey(f)===fk))return null;
  nextOwner=acrossFace(owner,face);candidates=nextOwner.components.filter(matches);
 }
 return candidates.length===1?{owner:nextOwner,component:candidates[0]}:null;
}
function carrier(stage,bindings){
 const p=windowProtocol[stage],vertices=p.nodes.map(n=>bindings[n]);
 return {kind:'tetrahedron',species:p.species,nodes:[...p.nodes],window:[...p.window],continuation:p.continuation,vertices,components:[vertices],faces:faces.map(f=>f.map(i=>vertices[i])),center:mean(vertices),key:itemKey(vertices)};
}
export const windowRule=Object.freeze({
 name:'retained ordered-window transfer',
 source:'carrier.mjs#trial; cmc-mcm-identity-attachment.md',
 principle:'P: C0 M0 C1 [M1] → N: M0 C1 M1 [C2] → E: M1 C1 C2 [M2]. Match the ordered target window to a complete face, retain global vertex identities, and admit the unique neighboring primitive cell.',
 scope:'Binding of the supplied marked-carrier protocol to the existing primitive lattice. The seed frame and octahedral subdivision are retained geometric inputs, not a derived physical C/M marking or a Pb-208 derivation. Window phases use the declared historical adapter; M2 has geometric context provenance only.',
});
export function createWindowConstruction({seed=makeLatticeItem('tetrahedron',[0,0,0,0]),bindings:initialBindings=null,identity={id:'id'},branch='positive',phaseExponent=0}={}){
 if(seed.kind!=='tetrahedron')throw RangeError('A four-vertex marked proton seed is required; octahedral proton roles need a separate binding');
 if(!['common','positive','negative'].includes(branch)||!Number.isInteger(phaseExponent)||phaseExponent<0||phaseExponent>2)throw RangeError('Unknown retained window mode or phase');
 const root=makeLatticeItem(seed.kind,seed.origin,seed.inverted),initial=initialBindings??Object.fromEntries(windowProtocol[0].nodes.map((n,i)=>[n,root.vertices[i]]));
 if(Object.keys(initial).length!==4||!windowProtocol[0].nodes.every(n=>Array.isArray(initial[n])&&initial[n].length===4&&initial[n].every(Number.isInteger)))throw RangeError('Seed must bind exactly C0,M0,C1,M1');
 if(itemKey(Object.values(initial))!==root.key)throw RangeError('Seed marks must bijectively bind its actual four vertices');
 const bindings=structuredClone(initial),carriedIdentity=Object.freeze({...identity}),placed=[carrier(0,bindings)],owners=[root],occupied=new Set([placed[0].key]),events=[];
 const history=[...windowProtocol[0].window],entry={kind:'inner-center',source:'inner-dimension',point:[...placed[0].center]};
 let mode={branch,phaseExponent};
 function inspect(){
  const stage=placed.length-1;if(stage===windowProtocol.length-1)return {status:'complete',reason:'The retained electron window is constructed; identity exits at its center',candidates:[]};
  const current=placed.at(-1),target=windowProtocol[stage+1],orderedFace=target.window.map(n=>bindings[n]);
  if(orderedFace.some(p=>!p)||!current.faces.some(f=>itemKey(f)===itemKey(orderedFace)))return {status:'incompatible-interface',reason:'Transported window is not a full face of the current carrier',candidates:[]};
  const next=primitiveAcross(owners.at(-1),current.vertices,orderedFace);
  if(!next||occupied.has(itemKey(next.component)))return {status:'incompatible-interface',reason:'No unique unoccupied lattice primitive across the transported face',candidates:[]};
  const faceKeys=new Set(orderedFace.map(pointKey)),apex=next.component.filter(p=>!faceKeys.has(pointKey(p)));
  if(apex.length!==1||Object.values(bindings).some(p=>pointKey(p)===pointKey(apex[0])))return {status:'incompatible-interface',reason:'Continuation must introduce a distinct context identity, not rename an old vertex',candidates:[]};
  return {status:'ready',reason:'Unique neighboring primitive across the retained ordered window',candidates:[{window:[...target.window],face:structuredClone(orderedFace),newMark:target.continuation}],next,apex:apex[0]};
 }
 function snapshot(){
  const {next,apex,...decision}=inspect(),current=placed.at(-1),complete=decision.status==='complete';
  return {identity:carriedIdentity,seed:{kind:root.kind,origin:[...root.origin],inverted:root.inverted},entry:structuredClone(entry),exit:{kind:'next-center',target:'next-realization',role:'electron',point:complete?[...current.center]:null,reached:complete,identity:complete?carriedIdentity:null},rule:windowRule,...structuredClone(decision),items:structuredClone(placed),bindings:structuredClone(bindings),history:[...history],mode:{...mode},events:structuredClone(events),added:events.length};
 }
 function step(){
  const decision=inspect();if(decision.status!=='ready')return {...snapshot(),committed:false};
  const stage=placed.length-1,source=windowProtocol[stage],target=windowProtocol[stage+1],before={...mode};
  const shared=source.window.filter(n=>target.window.includes(n)),outgoing=source.window.find(n=>!target.window.includes(n)),entering=target.window.find(n=>!source.window.includes(n));
  // Historical overlap-fixing adapter: PN preserves branch; NE reverses it.
  const increment=mode.branch==='common'?0:stage===0?(mode.branch==='positive'?1:2):(mode.branch==='positive'?2:1);
  mode={branch:stage===1&&mode.branch!=='common'?(mode.branch==='positive'?'negative':'positive'):mode.branch,phaseExponent:(mode.phaseExponent+increment)%3};
  bindings[target.continuation]=[...decision.apex];
  let overlap=Math.min(history.length,target.window.length);while(overlap>0&&history.slice(-overlap).join('|')!==target.window.slice(0,overlap).join('|'))overlap--;
  history.push(...target.window.slice(overlap));
  const body=carrier(stage+1,bindings);
  events.push({number:events.length+1,from:source.species,to:target.species,priorItemCount:placed.length,identityId:carriedIdentity.id,orderedFace:[...target.window],face:structuredClone(decision.candidates[0].face),fixedWindowMarks:shared,frameExchange:[outgoing,entering],targetCycle:stage===0?'forward':'inverse',modeBefore:before,modeAfter:{...mode},phaseIncrement:increment,newContext:{mark:target.continuation,coordinate:[...decision.apex]}});
  placed.push(body);owners.push(decision.next.owner);occupied.add(body.key);
  return {...snapshot(),committed:true};
 }
 return {snapshot,step};
}
