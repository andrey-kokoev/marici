// Layer-only information audit. No native reference or routing model is imported.
import {buildBranchingSeed} from './branching-seed.mjs';
const require=(ok,message)=>{if(!ok)throw Error(message);};
const letter={red:'R',blue:'B'};
export function advanceHistoryMemory(memory,role){
 require(['white','red','blue'].includes(role),'Unknown edge colour');
 return role==='white'?{...memory}:{previous:memory.current,current:role};
}
export function encodeHistoryBit(colour,redSign='+'){
 require(['red','blue'].includes(colour)&&['+','-'].includes(redSign),'No historical branch bit available');
 return colour==='red'?redSign:redSign==='+'?'-':'+';
}
export function auditLayerHistory(layer){
 const edges=new Map(layer.edges.map(e=>[e.id,e])),white=new Map(),branches=new Map();
 function observe(map,edge,word,path,memory,arrival){
  if(!map.has(edge.id))map.set(edge.id,{edge,histories:new Map()});
  const records=map.get(edge.id).histories;
  if(!records.has(word))records.set(word,{word,path:[...path],memory:{...memory},arrival,completions:0});
  const old=records.get(word);require(old.path.join('|')===path.join('|'),'Colour word has multiple paths');old.completions++;
 }
 for(const route of layer.routes){
  let word='',memory={previous:null,current:null},path=[],last=null;
  for(const id of route.edges){
   const edge=edges.get(id);require(edge,'Route uses an unknown layer edge');
   if(last)require(last.to===edge.from,'Layer path is not directed and continuous');
   else require(edge.from===layer.root,'Layer path does not start at its root');
   path.push(id);memory=advanceHistoryMemory(memory,edge.role);
   if(edge.role==='white')observe(white,edge,word,path,memory,last?.id??null);
   else {word+=letter[edge.role];observe(branches,edge,word,path,memory,last?.id??null);}
   last=edge;
  }
 }
 const whiteRecords=[...white.values()].map(({edge,histories})=>{
  const records=[...histories.values()].sort((a,b)=>a.word.localeCompare(b.word)),depth=records[0].word.length;
  const incoming=[...new Set(records.map(r=>r.arrival).filter(Boolean))].map(id=>({edge:id,colour:edges.get(id).role,records:records.filter(r=>r.arrival===id)}));
  const outgoing=layer.edges.filter(e=>e.from===edge.to&&e.role!=='white');
  return {edge:edge.id,from:edge.from,to:edge.to,depth,records,incoming,outgoing:outgoing.map(e=>e.id),complete:incoming.length===2&&outgoing.length===2};
 });
 const collisions=whiteRecords.flatMap(w=>w.incoming.filter(p=>p.records.length>1).map(p=>({whiteEdge:w.edge,depth:w.depth,arrivalEdge:p.edge,colour:p.colour,words:p.records.map(r=>r.word),
  currentColourValues:[...new Set(p.records.map(r=>r.memory.current))],olderColourValues:[...new Set(p.records.map(r=>r.memory.previous))]}))).sort((a,b)=>a.depth-b.depth||a.words.join().localeCompare(b.words.join()));
 // This interface is selected entirely from layer geometry and causal prefix
 // multiplicity: the earliest white edge reached by two distinct prefixes.
 const candidates=whiteRecords.filter(w=>w.records.length===2&&w.complete),earliest=Math.min(...candidates.map(w=>w.depth));
 const interfaces=candidates.filter(w=>w.depth===earliest).map(w=>{
  const ports=w.outgoing.map(id=>{
   const branch=branches.get(id),records=[...branch.histories.values()].sort((a,b)=>a.word.localeCompare(b.word));
   return {edge:id,colour:branch.edge.role,from:branch.edge.from,to:branch.edge.to,
    records:records.map(r=>({...r,candidateB:encodeHistoryBit(r.memory.previous),oppositeConventionB:encodeHistoryBit(r.memory.previous,'-')}))};
  });
  return {whiteEdge:w.edge,depth:w.depth,incomingHistories:w.records,ports,
   independentPortAndHistory:ports.length===2&&ports.every(p=>p.records.length===2&&new Set(p.records.map(r=>r.candidateB)).size===2),
   flow:'two outgoing ports of a layer fork; not yet identified with native incoming ports'};
 });
 return {layer:layer.id,whiteRecords,collisions,interfaces,
  counts:{fullRoutes:layer.routes.length,whiteEdges:whiteRecords.length,distinctWhitePrefixes:whiteRecords.reduce((n,w)=>n+w.records.length,0),completeWhiteNeighbourhoods:whiteRecords.filter(w=>w.complete).length,
   completeIncomingTwoByTwo:whiteRecords.filter(w=>w.complete&&w.incoming.every(p=>p.records.length===2)).length}};
}
export function auditEightLayerHistory(seed=buildBranchingSeed()){
 const layers=seed.layers.map(auditLayerHistory);
 const signature=i=>i.ports.flatMap(p=>p.records.map(r=>[p.colour,r.word,r.candidateB,r.completions].join(':'))).sort().join('|');
 const signatures=layers.flatMap(l=>l.interfaces.map(signature));
 return {schema:'sulfur-layer-history.v1',layers,
  summary:{layers:layers.length,completeWhiteNeighbourhoods:layers.reduce((n,l)=>n+l.counts.completeWhiteNeighbourhoods,0),completeIncomingTwoByTwo:layers.reduce((n,l)=>n+l.counts.completeIncomingTwoByTwo,0),
   earliestTwoHistoryInterfaces:signatures.length,interfacesCarryIndependentBit:layers.every(l=>l.interfaces.length>0&&l.interfaces.every(i=>i.independentPortAndHistory)),reflectionInvariantHistoryCoding:new Set(signatures).size===1},
  convention:'candidate b: older red = +, older blue = -; global sign reversal is equally valid for the layer-only audit',
  scope:'causal path-prefix classes and their retained information, not a conserved particle population or an established layer-to-native correspondence'};
}
