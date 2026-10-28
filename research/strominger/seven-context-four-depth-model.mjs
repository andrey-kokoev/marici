// Experimental 7 x 4 indexing of the single P/E interface. No layer-word input.
import {makeSinglePEPair} from './single-pe-pair-model.mjs';
import {windowProtocol} from './demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {activePhaseSlots} from './demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const copy=x=>structuredClone(x),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const key=vertices=>[...vertices].sort().join('|');
const subsets=vertices=>Array.from({length:2**vertices.length-1},(_,i)=>vertices.filter((_,j)=>(i+1)&(1<<j)));
export function makeSevenContextFourDepth({seedBindings=null}={}){
 const pair=makeSinglePEPair({seedBindings}),spec=s=>windowProtocol.find(p=>p.species===s);
 const faces={P:[...spec('proton').window],E:[...spec('electron').window]};
 const common=faces.P.filter(n=>faces.E.includes(n));
 if(common.length!==1)throw Error('Active endpoint faces must meet at exactly one marked vertex');
 const vertex=common[0],all=new Map(),star=new Map();
 for(const [owner,face]of Object.entries(faces))for(const vertices of subsets(face)){
  const id=key(vertices);if(!all.has(id))all.set(id,{id,vertices:[...vertices].sort(),owners:[]});all.get(id).owners.push(owner);
 }
 for(const [id,face]of all)if(face.vertices.includes(vertex))star.set(id,face);
 const contexts=[...star.values()].sort((a,b)=>a.vertices.length-b.vertices.length||a.id.localeCompare(b.id));
 const covers=[];
 for(const large of contexts)for(const small of contexts)if(large.vertices.length===small.vertices.length+1&&small.vertices.every(v=>large.vertices.includes(v)))covers.push({from:large.id,to:small.id});
 function localRead(state,context){
  const readings=context.owners.map(owner=>{
   const species=owner==='P'?'proton':'electron',slots=activePhaseSlots[species];
   return context.vertices.map(mark=>copy(state.endpoints[owner][slots[faces[owner].indexOf(mark)]]));
  });
  if(readings.some(r=>!same(r,readings[0])))throw Error('Shared active-face values disagree');
  return {context:context.id,vertices:[...context.vertices],values:readings[0]};
 }
 function bank(state){
  const ab=pair.reconstruct(state.endpoints.P,state.endpoints.E,state.orientation),ba=pair.reconstruct(state.endpoints.P,state.endpoints.E,-state.orientation);
  return {aa:{kind:'P-self-comparison',coefficients:copy(state.endpoints.P)},
   ab:{kind:'N-interface',cellKey:ab.cellKey,orientation:ab.orientation,readFrom:ab.readFrom,coefficients:ab.coefficients},
   ba:{kind:'N-interface',cellKey:ba.cellKey,orientation:ba.orientation,readFrom:ba.readFrom,coefficients:ba.coefficients},
   bb:{kind:'E-self-comparison',coefficients:copy(state.endpoints.E)}};
 }
 function advance(state){pair.reverseInPlace(state);pair.confirm(state);return state;}
 function run(value){
  const live=pair.prepare(value),states=[copy(live)],records=[];
  for(let depth=1;depth<=4;depth++){
   advance(live);states.push(copy(live));const retainedBank=bank(live);
   for(const context of contexts)records.push({position:records.length+1,depth,context:context.id,local:localRead(live,context),bankReference:`depth-${depth}`,orientation:live.orientation,confirmation:live.confirmation});
   states[depth].bank=retainedBank;
  }
  return {states,records,banks:states.slice(1).map(s=>s.bank),final:copy(live)};
 }
 // Each edge is the actual sequence of confirmed reversals between two
 // occurrence indices, not a parity quotient that erases intermediate history.
 function depthEdge(state,from,to){
  if(!Number.isInteger(from)||!Number.isInteger(to)||from<0||to>4||to<=from||state.history.length!==2*from)throw Error('Wrong typed depth edge');
  const target=copy(state);delete target.bank;
  for(let i=from;i<to;i++)advance(target);return target;
 }
 return {pair,faces,vertex,allFaces:[...all.values()],contexts,covers,localRead,bank,advance,run,depthEdge};
}
