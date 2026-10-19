import {GenerativeAssemblyRules,phaseFrame,applyPhasePermutation} from './generative-phase-assembly.mjs';
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b),sorted=a=>[...a].sort((a,b)=>a-b);

// The bound is on absolute realization origin, NOT operation count, reader
// visits, final C index, coefficient order or concurrent scheduling rounds.
export function phaseUniverse({maxOrigin,seedBindings=null,maxPackets=100000}={}){
 if(!Number.isInteger(maxOrigin)||maxOrigin<0||maxOrigin>10)throw Error('Explicit maxOrigin integer in [0,10] required');
 const rules=new GenerativeAssemblyRules({seedBindings}),queue=[rules.root],seen=new Set(queue),operations=[];
 let complete=true,stop=null;
 for(let i=0;i<queue.length;i++){
  const id=queue[i],packet=rules.packets[id];
  for(const index of rules.outgoing(id)){
   const op=rules.operations[index],target=rules.packets[op.target];
   rules.validateTransfer(op);
   if(op.phaseDelta===0){
    if(op.kind==='NE'){if(rules.outgoing(op.target).length)throw Error('Terminal NE has a zero-grade continuation');}
    else {
     const inverseKind=op.kind==='PN'?'inverse-PN':'PN';
     if(!rules.outgoing(op.target).some(j=>rules.operations[j].kind===inverseKind&&rules.operations[j].target===id))throw Error('Zero-grade PN closure no longer returns its exact packet');
    }
   }else if(op.phaseDelta!==1||target.origin!==packet.origin+1)throw Error('Unsupported phase grading');
   if(target.origin>maxOrigin)continue;
   operations.push(index);
   if(!seen.has(op.target)){
    if(queue.length>=maxPackets){complete=false;stop={reason:'packet-resource-limit',maxPackets};break;}
    seen.add(op.target);queue.push(op.target);
   }
  }
  if(!complete)break;
 }
 return {rules,maxOrigin,packets:queue,operations,complete,stop,
  finiteness:'Each zero-grade component is a native PN pair with terminal NE exit (at most three packets); each component has at most three +1 successors. Finite branching and the origin cap bound reachable packets. Repeated zero-grade words remain labelled cycles, not a finite list of histories.'};
}

export function enumerateOriginAssemblies({maxOrigin,maxConfigurations=250000,inspect=true,seedBindings=null}={}){
 if(!Number.isSafeInteger(maxConfigurations)||maxConfigurations<1)throw Error('Positive configuration resource bound required');
 const universe=phaseUniverse({maxOrigin,seedBindings}),{rules}=universe;
 const allowed=new Set(universe.operations),nodes=[{id:0,grade:0,packets:[rules.root],parent:null,operation:null,minOperations:0}],byKey=new Map([[String(rules.root),0]]),edges=[];
 // Current guards are unary/binary occupancy, vertex-role and face-contact
 // predicates. Compile their exact pair table; the checker independently
 // validates every retained whole configuration with describe/inspect.
 const incompatible=new Map(universe.packets.map(p=>[p,new Set()]));
 for(let a=0;a<universe.packets.length;a++)for(let b=a+1;b<universe.packets.length;b++){
  const p=universe.packets[a],q=universe.packets[b];if(!rules.describe([p,q]).valid){incompatible.get(p).add(q);incompatible.get(q).add(p);}
 }
 let complete=universe.complete,stop=universe.stop;
 for(let cursor=0;complete&&cursor<nodes.length;cursor++){
  const node=nodes[cursor],selected=new Set(node.packets);
  candidates:for(const id of node.packets)for(const index of rules.outgoing(id)){
   if(!allowed.has(index))continue;const op=rules.operations[index];
   if(selected.has(op.target)){edges.push({from:node.id,to:node.id,operation:index});continue;}
   if(node.packets.some(p=>incompatible.get(op.target).has(p)))continue;
   const ids=sorted([...node.packets,op.target]),key=ids.join(',');let next=byKey.get(key);
   if(next===undefined){
    if(nodes.length>=maxConfigurations){complete=false;stop={reason:'configuration-resource-limit',maxConfigurations,cursor};break candidates;}
    next=nodes.length;byKey.set(key,next);nodes.push({id:next,grade:Math.max(node.grade,rules.packets[op.target].origin),packets:ids,parent:node.id,operation:index,minOperations:node.minOperations+1});
   }
   edges.push({from:node.id,to:next,operation:index});
  }
 }
 const profiles=new Map();let exitCertified=0,maxBodies=0;
 const maxMinimumOperations=nodes.reduce((m,n)=>Math.max(m,n.minOperations),0);
 if(inspect)for(const n of nodes){
  n.inspection=rules.inspect(n.packets);if(!n.inspection.valid)throw Error('Incompatible retained configuration');
  const i=n.inspection,c=i.counts,key=[c.proton,c.neutron,c.electron].join('/');
  if(!profiles.has(key))profiles.set(key,{counts:c,configurations:0,selectedRecordExitCertificates:0});
  const p=profiles.get(key);p.configurations++;if(i.certifiedExit){p.selectedRecordExitCertificates++;exitCertified++;}
  maxBodies=Math.max(maxBodies,c.proton+c.neutron+c.electron);
 }
 return {schema:'marici.nima.origin-bounded-assemblies.v1',complete,stop,
  contract:{budgetKind:'realization-advances',seedOrigin:0,maxOrigin,grade:'maximum absolute origin among the configuration selected packets',
   operationCountBound:null,readerVisitBound:null,finalCIndexBound:null,contextPolicy:'Bind and validate all native contexts, including C_(D+2)/M_(D+2); lookahead labels do not consume extra realization advances.',
   branching:'Explore all compatible alternatives at each origin, including dependent zero-grade operations. Do not eagerly union all enabled NE/NN alternatives. Sibling depths combine by maximum, not sum.',
   histories:'All operation histories remain labelled paths/cycles. minOperations is representative metadata only, never an admission bound.',
   sewing:'Local transport consistency and selected-record exit certificate only. No unasserted occurrence identification, global cross-branch state merge, or physical binding claim.'},
  summary:{universePackets:universe.packets.length,universeOperations:universe.operations.length,configurations:nodes.length,constructionEdges:edges.length,
   selectedRecordExitCertificates:inspect?exitCertified:null,profiles:inspect?profiles.size:null,maxOccupiedBodies:inspect?maxBodies:null,maxRepresentativeOperations:maxMinimumOperations},
  finiteness:universe.finiteness,profiles:[...profiles.values()],nodes,edges,universe,rules};
}

// Only explicit record identifications are audited. Coordinates alone never
// assert that distinct histories are one occurrence or one physical state.
export function auditRecordSewing(rules,{from,to,coefficientIdentification,occurrences=[],identifiedSlots=null,scope='packet'}={}){
 if(scope!=='packet')return {status:'ancestry-key-required',generic:false};
 const a=rules.packets[from],b=rules.packets[to];
 if(!a||!b||!Array.isArray(coefficientIdentification)||!same([...coefficientIdentification].sort((x,y)=>x-y),[0,1,2,3,4]))throw Error('Explicit source, target and full five-slot identification required');
 const ca=rules.charts[a.chart],cb=rules.charts[b.chart],failures=[];
 for(const {fromMark,toMark} of occurrences){
  const x={vertex:ca.aliases[fromMark],role:fromMark[0],index:Number(fromMark.slice(1))+a.origin},y={vertex:cb.aliases[toMark],role:toMark[0],index:Number(toMark.slice(1))+b.origin};
  if(typeof x.vertex!=='string'||typeof y.vertex!=='string'||!same(x,y))failures.push({fromMark,toMark,from:x,to:y});
 }
 if(failures.length)return {status:'occurrence-identification-rejected',generic:false,failures};
 const slots=identifiedSlots??[0,1,2,3,4];
 if(!Array.isArray(slots)||!slots.length||new Set(slots).size!==slots.length||slots.some(i=>!Number.isInteger(i)||i<0||i>4))throw Error('Explicit identified coefficient rows required');
 const transported=coefficientIdentification.map(i=>a.permutation[i]),equalities=[];
 for(const slot of slots)if(transported[slot]!==b.permutation[slot])equalities.push({slot,rootCoordinates:[transported[slot],b.permutation[slot]],condition:`root[${transported[slot]}] = root[${b.permutation[slot]}]`});
 const basis=[...Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>[Number(i===j),0])),...Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>[0,Number(i===j)]))];
 let allBasisEqual=true;
 for(const x of basis){const left=applyPhasePermutation(applyPhasePermutation(x,a.permutation),coefficientIdentification),right=applyPhasePermutation(x,b.permutation);if(!same(slots.map(i=>left[i]),slots.map(i=>right[i])))allBasisEqual=false;}
 if(allBasisEqual!==!equalities.length)throw Error('Symbolic and basis sewing checks disagree');
 return {status:allBasisEqual?(identifiedSlots===null?'generic-full-map-sewing-pass':'identified-slot-sewing-pass'):'explicit-input-subspace-required',generic:allBasisEqual,basisInputs:10,identifiedSlots:[...slots],mapScope:identifiedSlots===null?'full-five-carrier':'listed-rows-only; other coordinates remain unmerged',rootEqualities:equalities,
  identifiedOccurrencePairs:occurrences.length,assertsPhysicalStateIdentity:false,
  scope:'Only the declared coefficient transport and listed occurrence pairs were audited. No inference about unlisted occurrences, resetting origin, global branch sewing or physical-state identity.'};
}
export {GenerativeAssemblyRules,phaseFrame};
