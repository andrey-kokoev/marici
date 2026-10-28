import {analyzeSeamLattice} from './seam-lattice.mjs';
import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {fibrationDisplayEnvelope} from './fibration12-process.mjs';
import {cellDualGraph} from './cell-dual-graph.mjs';
import {geometricCellLayer} from './cell-fibration-cut.mjs';
import {previewNeighbourRule} from './neighbour-rule-preview.mjs';
import {previewPathRules} from './path-rule-preview.mjs';
import {seed} from './normal-ray-model.mjs';
// The glued face contributes three shared vertices, not three extra anchors.
export const doubleEsd7Envelope=[...new Map(fibrationDisplayEnvelope.map(p=>[p.map(x=>x.toFixed(8)).join(','),p])).values()];
const model=buildFoldedFibration();
const seamLattice=analyzeSeamLattice(model.occurrences);
export const doubleEsd7VertexLabels=doubleEsd7Envelope.map(point=>{
 const binding=model.bindings.find(b=>b.point.every((x,i)=>Math.abs(x-point[i])<1e-8));
 if(!binding)throw Error('Missing double ESD7 vertex binding');
 return binding.text;
});
const kinds=new Map(model.geometry.map(g=>[g.id,g.kind]));
const geometry=model.occurrences.map(o=>({id:o.id,kind:kinds.get(o.sourceGeometry),vertices:o.vertices,faces:o.faces,components:[],role:null,layer:null,unfilled:true}));
const graph=cellDualGraph(geometry);
const localAddresses=new Map(model.geometry.map(b=>[b.id,[1,2,3,4].map(v=>geometricCellLayer(b,v))]));
const occurrences=new Map(model.occurrences.map(o=>[o.id,o]));
const portLabels=new Map();
for(const o of model.occurrences.filter(o=>o.boundary.length)){
 const address=localAddresses.get(o.sourceGeometry),axis=address.indexOf(0);
 if(axis>=0)portLabels.set(`${o.copy}:${axis}`,o.boundary[0].includes('P')?'P':o.boundary[0]);
}
const seamInterfaces=graph.links.flatMap(e=>occurrences.get(e.from).copy!==occurrences.get(e.to).copy?[{from:e.from,to:e.to},{from:e.to,to:e.from}]:[]);
const ruleWires=graph.links.flatMap(e=>[[e.from,e.to],[e.to,e.from]].flatMap(([from,to])=>{
 const a=occurrences.get(from),b=occurrences.get(to);
 if(a.copy!==b.copy)return []; // Interface identifications are not movement wires.
 const start=localAddresses.get(a.sourceGeometry),end=localAddresses.get(b.sourceGeometry),changed=start.flatMap((v,i)=>v!==end[i]?[i]:[]);
 if(changed.length!==1)return [];
 const axis=changed[0],direction=portLabels.get(`${a.copy}:${axis}`),delta=end[axis]-start[axis];
 return delta===(direction==='P'?1:-1)?[{from,to,direction}]:[];
}));
export const doubleEsd7Stages=['Seed ±P tips and E/+N/−N shared-bottom corners.','From each ±P tip, send |P| to the next face-adjacent node and assign P.','Each new P sends −N, +N and E to its three directional neighbours, plus |P| to the remaining inward neighbour.','Each step-2 output advances to its sole next unfilled face-neighbour: N sends |P|; E sends |N|.','From each PPNP node, send |−N|, |+N|, |P| and |E|; assign the arrow colour and merge agreeing arrivals.','Apply N + |P| → P and NP + |±N| → N to a fixed point as one reversible step.','Extend rule closure with E + |P| → N, N + |E| → E and N + |±N| → E, including zero-move +P/−P interface identifications.','Complete unfilled tetrahedra with exactly three P and one N face-neighbours as P.'];
const ends=[{id:model.entry,label:'−P',direction:'toward +P'},{id:model.exit,label:'+P',direction:'toward −P'}];
const centre=b=>b.vertices[0].map((_,i)=>b.vertices.reduce((s,p)=>s+p[i]/b.vertices.length,0));
export const doubleEsd7Rules=[
 {id:'P-branch',label:'P octahedron + |x| → x (including P-tip entry)'},
 {id:'N-P',label:'N + |P| → P'},
 {id:'E-P',label:'E + |P| → N'},
 {id:'N-nonP',label:'N + |E or ±N| → E'}
];
export function doubleEsd7RuleProcess(k,enabledRules=[],internalElectronSelf=false,seamBelts={enabled:false,a:0,b:1}){
 const seedState=doubleEsd7Process(k,0),seeds=seedState.retainedBodies;
 const states=seeds.map(b=>({node:b.id,front:b.front?.label??b.seedLabel,suffix:({proton:'P',neutron:'N',electron:'E'})[b.role]}));
 const options={wires:ruleWires,interfaces:seamInterfaces,extended:true,protonBranches:true,protonBranchNodes:new Set([...geometry.filter(b=>b.kind==='octahedron').map(b=>b.id),...ends.map(e=>e.id)])};
 const applied=previewPathRules({...options,bodies:seeds,states,enabledRules});
 const retainedBodies=[...seeds],growth=[],interfaceGuides=[];
 for(const proposal of applied.candidates){
  const target={...geometry.find(b=>b.id===proposal.id),role:proposal.role,unfilled:false,layer:null,arrivals:proposal.arrivals,ruleClosure:{round:proposal.round,rules:[...new Set(proposal.arrivals.map(a=>a.rule))]}};
  retainedBodies.push(target);states.push(...proposal.arrivals);
  for(const a of proposal.arrivals){
   if(a.kind==='interface-identification')continue;
   growth.push({source:a.source,target:a.target,front:a.front,word:`|${a.direction}|`,role:a.role,rule:a.rule});
   interfaceGuides.push({points:[centre(geometry.find(b=>b.id===a.source)),centre(target)],color:a.role==='electron'?0xa82664:a.role==='neutron'?0xe5eaf0:0x1265a8,inset:.11});
  }
 }
 const selected=new Set(retainedBodies.map(b=>b.id)),emptyBodies=geometry.filter(b=>!selected.has(b.id));
 let internalExperiment=null;
 if(internalElectronSelf){
  // Separate namespace and state: this is a test carrier, not a derived neutron refinement.
  const prefix=id=>`internal:${id}`,bodies=retainedBodies.map(b=>({id:prefix(b.id),role:b.role}));
  const states=retainedBodies.filter(b=>b.role==='electron').map(b=>({node:prefix(b.id),front:'internal',suffix:'E'}));
  const wires=ruleWires.map(w=>({...w,from:prefix(w.from),to:prefix(w.to)}));
  const result=previewPathRules({bodies,wires,states,enabledRules:[],sector:'internal',electronSelfRule:true});
  const current=new Map(retainedBodies.map(b=>[b.id,b.role]));
  const matches=ruleWires.filter(w=>w.direction==='E'&&current.get(w.from)==='electron');
  internalExperiment={rule:'E + |E| → P',carrier:'Isolated copy of current carrier; internal neutron geometry not yet defined.',matches:matches.length,agreeing:matches.filter(w=>current.get(w.to)==='proton').length,...result};
 }
 const preview=applied.valid?previewPathRules({...options,bodies:retainedBodies,states,enabledRules:doubleEsd7Rules.map(r=>r.id)}):applied;
 preview.rules=doubleEsd7Rules.map(r=>r.label);preview.scope='Candidates with all four rules enabled. Interface identification is not a movement.';
 const flows=[];
 if(seamBelts.enabled){
  for(const [side,index] of [[0,seamBelts.a],[1,seamBelts.b]]){
   const cycle=seamLattice.cycles[index];if(!cycle)throw Error('Unknown seam cycle');
   const cells=side===0?[...cycle.lifts[0]]:[...cycle.lifts[1]].reverse(),color=side===0?0x42bfb3:0xb785e8;
   flows.push({id:side===0?'A':'B',cycle:index,cells,pairs:cycle.pairs,direction:side===0?1:-1,color});
   for(let i=0;i<cells.length;i++)interfaceGuides.push({points:[centre(geometry.find(b=>b.id===cells[i])),centre(geometry.find(b=>b.id===cells[(i+1)%cells.length]))],color,inset:.03,seamFlow:true});
  }
 }
 return {...seedState,retainedBodies,emptyBodies,attachmentBodies:[],presentationWireframes:emptyBodies,interfaceGuides,
  presentationLabels:seeds.map(b=>({cell:b.id,role:b.role,text:b.seedLabel,point:centre(b)})),
  doubleEsd7Audit:{...seedState.doubleEsd7Audit,seamLattice:{pairCount:seamLattice.pairs.length,cellCount:seamLattice.cellIds.length,cycles:seamLattice.cycles,overlaps:seamLattice.overlaps,flows,sharedPairs:flows.length===2?flows[0].pairs.filter(id=>flows[1].pairs.includes(id)):[]},internalExperiment,rulePreview:preview,enabledRules:[...enabledRules],filledCount:retainedBodies.length,unfilledCount:emptyBodies.length,growth},
  summary:'Fixed point of enabled local rules.',history:[],canAdvance:false};
}
export function doubleEsd7Process(k,step){
 if(k!==7||!Number.isInteger(step)||step<0||step>=doubleEsd7Stages.length)throw Error('Invalid double ESD7 step');
 const retainedBodies=model.occurrences.filter(o=>o.boundary.length).map(o=>{
  const label=o.boundary[0],front=ends.find(e=>e.id===o.id);
  return {...geometry.find(g=>g.id===o.id),role:o.role,layer:0,unfilled:false,seedLabel:label,front:front?{...front}:null};
 });
 const seedCount=retainedBodies.length,growth=[],interfaceGuides=[],arrowLabels=[];
 if(step>=1)for(const front of ends){
  const source=retainedBodies.find(b=>b.id===front.id);
  const links=graph.links.filter(e=>e.from===source.id||e.to===source.id);
  if(links.length!==1)throw Error('P tip must have one inward face-neighbour');
  const targetId=links[0].from===source.id?links[0].to:links[0].from;
  if(retainedBodies.some(b=>b.id===targetId))throw Error('First P target must be unfilled');
  const target={...geometry.find(b=>b.id===targetId),role:'proton',layer:1,unfilled:false,front:{...front},arrow:{source:source.id,word:'|P|'}};
  retainedBodies.push(target);
  const from=centre(source),to=centre(target),mid=from.map((x,i)=>(x+to[i])/2);
  growth.push({source:source.id,target:target.id,front:front.label,word:'|P|',role:'proton'});
  interfaceGuides.push({points:[from,to],color:0x1265a8,inset:.11});
  arrowLabels.push({cell:`arrow:${front.id}`,role:'proton',text:'|P|',point:mid});
 }
 if(step>=2)for(const source of retainedBodies.filter(b=>b.layer===1)){
  const candidates=graph.links.filter(e=>e.from===source.id||e.to===source.id).map(e=>geometry.find(b=>b.id===(e.from===source.id?e.to:e.from))).filter(b=>!retainedBodies.some(p=>p.id===b.id));
  const targets=new Set();
  for(const label of ['−N','+N','E']){
   const binding=model.bindings.find(b=>b.text===label);
   const distance=b=>centre(b).reduce((s,x,i)=>s+(x-binding.point[i])**2,0);
   const ranked=[...candidates].sort((a,b)=>distance(a)-distance(b));
   if(!ranked[0]||Math.abs(distance(ranked[0])-distance(ranked[1]))<1e-8||targets.has(ranked[0].id))throw Error('Unique directional branch target required');
   targets.add(ranked[0].id);
   const role=binding.role,word=`|${label}|`,target={...ranked[0],role,layer:2,unfilled:false,seedLabel:label,front:{...source.front},arrow:{source:source.id,word,direction:label}};
   retainedBodies.push(target);
   const from=centre(source),to=centre(target),mid=from.map((x,i)=>(x+to[i])/2);
   growth.push({source:source.id,target:target.id,front:source.front.label,word,role,direction:label});
   interfaceGuides.push({points:[from,to],color:role==='electron'?0xa82664:0xe5eaf0,inset:.11});
   arrowLabels.push({cell:`arrow:${source.id}:${label}`,role,text:word,point:mid});
  }
  const remaining=candidates.filter(b=>!targets.has(b.id));
  if(remaining.length!==1)throw Error('Unique inward P branch required');
  const target={...remaining[0],role:'proton',layer:2,unfilled:false,seedLabel:'P',front:{...source.front},arrow:{source:source.id,word:'|P|',direction:'P'}};
  retainedBodies.push(target);
  const from=centre(source),to=centre(target),mid=from.map((x,i)=>(x+to[i])/2);
  growth.push({source:source.id,target:target.id,front:source.front.label,word:'|P|',role:'proton',direction:'P'});
  interfaceGuides.push({points:[from,to],color:0x1265a8,inset:.11});
  arrowLabels.push({cell:`arrow:${source.id}:P`,role:'proton',text:'|P|',point:mid});
 }
 if(step>=3){
  const assigned=new Set(retainedBodies.map(b=>b.id)),proposals=new Map();
  for(const source of retainedBodies.filter(b=>b.layer===2&&b.role!=='proton')){
   const candidates=graph.links.filter(e=>e.from===source.id||e.to===source.id).map(e=>e.from===source.id?e.to:e.from).filter(id=>!assigned.has(id));
   if(candidates.length!==1)throw Error('Step-2 output must have one next unfilled face-neighbour');
   const id=candidates[0],role=source.role==='electron'?'neutron':'proton',word=role==='neutron'?'|N|':'|P|';
   if(proposals.has(id))throw Error('Step-3 targets must be distinct');
   const target={...geometry.find(b=>b.id===id),role,layer:3,unfilled:false,front:{...source.front},arrow:{source:source.id,word}};
   proposals.set(id,target);
   const from=centre(source),to=centre(target),mid=from.map((x,i)=>(x+to[i])/2);
   growth.push({source:source.id,target:id,front:source.front.label,word,role});
   interfaceGuides.push({points:[from,to],color:role==='neutron'?0xe5eaf0:0x1265a8,inset:.11});
   arrowLabels.push({cell:`arrow:${source.id}:${word}`,role,text:word,point:mid});
  }
  retainedBodies.push(...proposals.values());
 }
 if(step>=4){
  const assigned=new Set(retainedBodies.map(b=>b.id)),proposals=new Map();
  for(const source of retainedBodies.filter(b=>b.layer===3&&b.role==='proton')){
   const candidates=graph.links.filter(e=>e.from===source.id||e.to===source.id).map(e=>geometry.find(b=>b.id===(e.from===source.id?e.to:e.from))).filter(b=>!assigned.has(b.id));
   const targets=new Set(),branches=[];
   for(const direction of ['−N','+N','E']){
    const binding=model.bindings.find(b=>b.text===direction),distance=b=>centre(b).reduce((sum,x,i)=>sum+(x-binding.point[i])**2,0);
    const ranked=[...candidates].sort((a,b)=>distance(a)-distance(b));
    if(ranked.length<2||Math.abs(distance(ranked[0])-distance(ranked[1]))<1e-8||targets.has(ranked[0].id))throw Error('Unique PPNP directional target required');
    targets.add(ranked[0].id);branches.push({cell:ranked[0],direction,role:binding.role});
   }
   const inward=candidates.filter(b=>!targets.has(b.id));
   if(inward.length!==1)throw Error('Unique PPNP inward P target required');
   branches.push({cell:inward[0],direction:'P',role:'proton'});
   for(const {cell,direction,role} of branches){
    const word=`|${direction}|`,arrival={source:source.id,word,direction,front:source.front.label};
    if(proposals.has(cell.id)){
     const existing=proposals.get(cell.id);if(existing.role!==role)throw Error('Conflicting PPNP arrivals');
     existing.arrivals.push(arrival);
    }else proposals.set(cell.id,{...cell,role,layer:4,unfilled:false,seedLabel:role==='neutron'?'N':direction,front:{...source.front},arrow:{source:source.id,word,direction},arrivals:[arrival]});
    const from=centre(source),to=centre(cell),mid=from.map((x,i)=>(x+to[i])/2);
    growth.push({source:source.id,target:cell.id,front:source.front.label,word,role,direction});
    interfaceGuides.push({points:[from,to],color:role==='electron'?0xa82664:role==='neutron'?0xe5eaf0:0x1265a8,inset:.11});
    arrowLabels.push({cell:`arrow:${source.id}:${direction}`,role,text:word,point:mid});
   }
  }
  retainedBodies.push(...proposals.values());
 }
 const pathStates=new Map(),stateKey=s=>JSON.stringify([s.node,s.front,s.suffix,s.pOrientation??(s.front==='−P'?-1:1)]);
 for(const b of retainedBodies.filter(b=>b.layer===0)){const s={node:b.id,front:b.front?.label??b.seedLabel,suffix:({proton:'P',neutron:'N',electron:'E'})[b.role]};pathStates.set(stateKey(s),s);}
 for(const edge of growth)for(const parent of [...pathStates.values()].filter(s=>s.node===edge.source)){
  const s={node:edge.target,front:parent.front,suffix:(parent.suffix+({proton:'P',neutron:'N',electron:'E'})[edge.role]).slice(-2)};pathStates.set(stateKey(s),s);
 }
 let rulePreview=previewPathRules({bodies:retainedBodies,wires:ruleWires,states:[...pathStates.values()]});
 let appliedClosure=null;
 if(step>=5){
  if(!rulePreview.valid)throw Error('Cannot apply conflicting rule closure');
  appliedClosure={count:rulePreview.candidates.length,rounds:rulePreview.rounds,rules:rulePreview.rules};
  for(const proposal of rulePreview.candidates){
   const target={...geometry.find(b=>b.id===proposal.id),role:proposal.role,layer:5,unfilled:false,arrivals:proposal.arrivals.map(a=>({...a})),ruleClosure:{round:proposal.round,rules:[...new Set(proposal.arrivals.map(a=>a.rule))]}};
   retainedBodies.push(target);
   for(const arrival of proposal.arrivals){
    pathStates.set(stateKey(arrival),arrival);
    const word=`|${arrival.direction}|`,source=geometry.find(b=>b.id===arrival.source),from=centre(source),to=centre(target);
    growth.push({source:source.id,target:target.id,front:arrival.front,word,role:proposal.role,rule:arrival.rule,round:proposal.round});
    interfaceGuides.push({points:[from,to],color:proposal.role==='neutron'?0xe5eaf0:0x1265a8,inset:.11});
   }
  }
  rulePreview=previewPathRules({bodies:retainedBodies,wires:ruleWires,interfaces:seamInterfaces,states:[...pathStates.values()],extended:true});
 }
 if(step>=6){
  if(!rulePreview.valid)throw Error('Cannot apply conflicting extended closure');
  appliedClosure={count:rulePreview.candidates.length,rounds:rulePreview.rounds,rules:rulePreview.rules};
  for(const proposal of rulePreview.candidates){
   const target={...geometry.find(b=>b.id===proposal.id),role:proposal.role,layer:6,unfilled:false,arrivals:proposal.arrivals.map(a=>({...a})),ruleClosure:{round:proposal.round,rules:[...new Set(proposal.arrivals.map(a=>a.rule))]}};
   retainedBodies.push(target);
   for(const arrival of proposal.arrivals){
    pathStates.set(stateKey(arrival),arrival);
    if(arrival.kind==='interface-identification')continue;
    const word=`|${arrival.direction}|`,source=geometry.find(b=>b.id===arrival.source),from=centre(source),to=centre(target);
    growth.push({source:source.id,target:target.id,front:arrival.front,word,role:proposal.role,rule:arrival.rule,round:proposal.round});
    interfaceGuides.push({points:[from,to],color:proposal.role==='electron'?0xa82664:proposal.role==='neutron'?0xe5eaf0:0x1265a8,inset:.11});
   }
  }
  rulePreview=previewPathRules({bodies:retainedBodies,wires:ruleWires,interfaces:seamInterfaces,states:[...pathStates.values()],extended:true});
 }
 if(step>=6)rulePreview=previewNeighbourRule(geometry,graph.links,retainedBodies);
 if(step>=7){
  if(!rulePreview.valid)throw Error('Cannot apply conflicting neighbourhood rule');
  appliedClosure={count:rulePreview.candidates.length,rounds:rulePreview.rounds,rules:rulePreview.rules};
  for(const proposal of rulePreview.candidates){
   const target={...geometry.find(b=>b.id===proposal.id),role:'proton',layer:7,unfilled:false,arrivals:proposal.arrivals.map(a=>({...a})),ruleClosure:{round:1,rules:rulePreview.rules}};
   retainedBodies.push(target);
   for(const arrival of proposal.arrivals){
    const source=geometry.find(b=>b.id===arrival.source);
    growth.push({source:source.id,target:target.id,front:'local',word:'3P+1N',role:'proton',rule:arrival.rule});
    interfaceGuides.push({points:[centre(source),centre(target)],color:0x1265a8,inset:.11});
   }
  }
  rulePreview=previewNeighbourRule(geometry,graph.links,retainedBodies);
 }
 rulePreview.scope=step>=6?'Whole tetrahedra, four shared-face neighbours; existing colours are checked and never overwritten.':step>=5?'Interface identification flips local P orientation without a movement or path letter.':'Within each half; apply this closure first to check continuation across the seam.';
 const selected=new Set(retainedBodies.map(b=>b.id)),emptyBodies=geometry.filter(g=>!selected.has(g.id));
 return {k:7,step,end:seed,assignments:[],firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],
 retainedBodies,emptyBodies,conflictBodies:[],presentationWireframes:emptyBodies,
 presentationLabels:[...retainedBodies.map(b=>({cell:b.id,role:b.role,text:b.seedLabel??(b.role==='neutron'?'N':b.role==='electron'?'E':'P'),point:centre(b)})),...arrowLabels],interfaceGuides,
 presentationAudit:{nativeGeometry:true,wholeCellColour:true},
 doubleEsd7Audit:{rulePreview,appliedClosure,bodyCount:geometry.length,seedCount,filledCount:retainedBodies.length,growth,unfilledCount:emptyBodies.length,ends,sharedInterface:true,frontPolicy:'Opposing fronts may pass through one another; P entry, directional branching, N→P / E→N continuation, and PPNP branching are currently defined.'},
 summary:doubleEsd7Stages[step],
 history:doubleEsd7Stages.slice(0,step+1).map((rule,layer)=>({layer,rule})),canAdvance:step<doubleEsd7Stages.length-1};
}
