import {buildSulfurIncomingBundle} from './sulfur-32-incoming-bundle.mjs';
import {buildBranchingSeed} from './branching-seed.mjs';
const key=p=>p.join(',');
const compare=(a,b)=>{for(let i=0;i<a.length;i++)if(a[i]!==b[i])return a[i]-b[i];return 0;};
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const require=(ok,message)=>{if(!ok)throw Error(message);};
const uniquePoints=ps=>[...new Map(ps.map(p=>[key(p),p])).values()].sort(compare);
function starGeometry(arms){
 const gram=arms.map(a=>arms.map(b=>dot(a,b)/Math.sqrt(dot(a,a)*dot(b,b))));
 const cosines=[gram[0][1],gram[0][2],gram[1][2]].sort((a,b)=>a-b);
 const determinant=gram[0][0]*(gram[1][1]*gram[2][2]-gram[1][2]*gram[2][1])-gram[0][1]*(gram[1][0]*gram[2][2]-gram[1][2]*gram[2][0])+gram[0][2]*(gram[1][0]*gram[2][1]-gram[1][1]*gram[2][0]);
 return {cosines,anglesDegrees:cosines.map(c=>Math.acos(Math.max(-1,Math.min(1,c)))*180/Math.PI),gramDeterminant:determinant,hexStar:cosines.every(c=>Math.abs(c+.5)<1e-10)};
}
function extractMotif(reference,edge){
 const rows=[];
 for(const strand of reference.strands)for(let i=0;i<strand.edgeIds.length;i++)if(strand.edgeIds[i]===edge.id){
  if(i===0||i+2>=strand.guide.length)return null;
  rows.push({strandId:strand.id,colour:strand.label,polarities:{...strand.polarities},index:i,
   incomingEdge:strand.edgeIds[i-1],outgoingEdge:strand.edgeIds[i+1],
   previous:strand.guide[i-1],tail:strand.guide[i],head:strand.guide[i+1],next:strand.guide[i+2]});
 }
 if(rows.length!==2||new Set(rows.map(r=>key(r.tail))).size!==1||new Set(rows.map(r=>key(r.head))).size!==1)return null;
 const inputs=uniquePoints(rows.map(r=>r.previous)),outputs=uniquePoints(rows.map(r=>r.next));
 if(inputs.length!==2||outputs.length!==2)return null;
 const tail=rows[0].tail,head=rows[0].head;
 const ports=(points,field,edgeField)=>points.map((point,index)=>({index,point,edge:rows.find(r=>key(r[field])===key(point))[edgeField]}));
 return {id:edge.id,tail,head,inputs:ports(inputs,'previous','incomingEdge'),outputs:ports(outputs,'next','outgoingEdge'),
  rows:rows.map(r=>({...r,input:inputs.findIndex(p=>key(p)===key(r.previous)),output:outputs.findIndex(p=>key(p)===key(r.next))})),
  geometry:{tail:starGeometry([sub(head,tail),...inputs.map(p=>sub(p,tail))]),head:starGeometry([sub(tail,head),...outputs.map(p=>sub(p,head))])}};
}
export function buildSulfurLocalTransitions(reference=buildSulfurIncomingBundle()){
 const candidates=reference.edges.map(e=>extractMotif(reference,e)).filter(Boolean);
 const motifs=reference.layer3Mixes.map((edge,index)=>{
  const motif=candidates.find(m=>m.id===edge.id);require(motif,'Expected a two-input, two-output upper mixing edge');
  const varying=['a','b','p','e'].filter(bit=>new Set(motif.rows.map(r=>r.polarities[bit])).size===2);
  require(varying.length===1&&['p','e'].includes(varying[0]),'Upper motif must carry exactly one varying p/e bit');
  const selector=varying[0],heldBit=selector==='p'?'e':'p',heldSign=motif.rows[0].polarities[heldBit];
  const context=Object.fromEntries(['a','b','p','e'].filter(bit=>bit!==selector).map(bit=>[bit,motif.rows[0].polarities[bit]]));
  return {...motif,number:index+1,selector,heldBit,heldSign,context,
   observedPermutation:[0,1].map(i=>motif.rows.find(r=>r.input===i).output)};
 });
 // Local observations, not a new global path generator. Canonical port numbering
 // is lexicographic in the reference's native four-coordinate frame.
 return {schema:'sulfur-local-transition.v1',sourceScope:reference.audit.routingStatus,
  portConvention:'numeric lexicographic native coordinates, independently at each endpoint',motifs,candidates,
  coverage:{motifs:motifs.length,passages:motifs.reduce((n,m)=>n+m.rows.length,0),strandIds:[...new Set(motifs.flatMap(m=>m.rows.map(r=>r.strandId)))]}};
}
// Fit only the switch parity by held-sign; require every observation in a class
// to agree. This supports leave-one-motif-out tests instead of fitting IDs.
export function learnLocalRule(motifs){
 const parityByHeldSign={},selectorByA={};
 for(const m of motifs){
  require(selectorByA[m.context.a]===undefined||selectorByA[m.context.a]===m.selector,'No uniform selector rule');
  selectorByA[m.context.a]=m.selector;
 }
 for(const m of motifs)for(const row of m.rows){
  require(row.input===Number(row.polarities[m.selector]==='-'),'Input slot does not encode the observed selector');
  const parity=row.input^row.output;
  require(parityByHeldSign[m.heldSign]===undefined||parityByHeldSign[m.heldSign]===parity,'No uniform local rule in this port convention');
  parityByHeldSign[m.heldSign]=parity;
 }
 require(parityByHeldSign['+']!==undefined&&parityByHeldSign['-']!==undefined,'Training misses a held-sign class');
 return {parityByHeldSign,selectorByA,scope:'observed upper reference motifs only; coordinate-dependent port convention'};
}
function parityFor(motif,rule){const parity=rule.parityByHeldSign[motif.heldSign];require(parity===0||parity===1,'Missing switch parity');return parity;}
export function enterLocalCarrier(motif,packet,rule,direction='forward'){
 require(['forward','reverse'].includes(direction),'Unknown direction');
 const ports=direction==='forward'?motif.inputs:motif.outputs,index=ports.findIndex(p=>p.edge===packet.port);
 require(index>=0,'Packet is not on an incoming port for this direction');
 for(const [bit,value] of Object.entries(motif.context))require(packet.polarities?.[bit]===value,'Packet context does not match this carrier');
 const parity=parityFor(motif,rule),slot=direction==='forward'?index:index^parity;
 require(packet.polarities[motif.selector]===(slot===0?'+':'-'),'Packet selector disagrees with its port');
 const {port,...payload}=packet;
 return {motif:motif.id,direction,selector:motif.selector,slot,payload:structuredClone(payload)};
}
export function leaveLocalCarrier(motif,carrier,rule){
 require(carrier.motif===motif.id&&carrier.selector===motif.selector,'Wrong carrier');
 require(carrier.slot===0||carrier.slot===1,'The shared edge requires its one-bit lane state');
 require(['forward','reverse'].includes(carrier.direction),'Unknown direction');
 const parity=parityFor(motif,rule),index=carrier.direction==='forward'?carrier.slot^parity:carrier.slot;
 const ports=carrier.direction==='forward'?motif.outputs:motif.inputs;
 return {...structuredClone(carrier.payload),port:ports[index].edge};
}
export function compareHexLocalStars(transitions,seed=buildBranchingSeed()){
 const charts=[];
 for(const [layerIndex,layer] of seed.layers.entries())for(const edge of layer.edges.filter(e=>e.role==='white')){
  const at=id=>layer.edges.filter(e=>e.id!==edge.id&&(e.from===id||e.to===id));
  const incoming=at(edge.from),outgoing=at(edge.to);if(incoming.length!==2||outgoing.length!==2)continue;
  const neighbor=(e,id)=>e.from===id?e.points[1]:e.points[0],tail=edge.points[0],head=edge.points[1];
  const geometry={tail:starGeometry([sub(head,tail),...incoming.map(e=>sub(neighbor(e,edge.from),tail))]),head:starGeometry([sub(tail,head),...outgoing.map(e=>sub(neighbor(e,edge.to),head))])};
  const red=incoming.find(e=>e.role==='red'),direction=sub(head,tail),redDirection=sub(neighbor(red,edge.from),tail);
  charts.push({layer:layerIndex+1,edge:edge.id,arrowY:Math.sign(direction[1]),redSide:Math.sign(direction[0]*redDirection[1]-direction[1]*redDirection[0]),geometry});
 }
 const patterns=new Map();for(const chart of charts){const id=chart.arrowY+','+chart.redSide;if(!patterns.has(id))patterns.set(id,{arrowY:chart.arrowY,redSide:chart.redSide,layers:[],instances:0,example:chart});const p=patterns.get(id);p.instances++;if(!p.layers.includes(chart.layer))p.layers.push(chart.layer);}
 return {hexMotifs:charts.length,patterns:[...patterns.values()],allHexStars120:charts.every(c=>c.geometry.tail.hexStar&&c.geometry.head.hexStar),
  referenceCandidates:transitions.candidates.length,
  rigidStarMatches:transitions.candidates.filter(m=>m.geometry.tail.hexStar&&m.geometry.head.hexStar).map(m=>m.id),
  scope:'Angle invariants test a direct rigid local-edge identification, not every possible folding or multi-edge coarse-graining.'};
}
