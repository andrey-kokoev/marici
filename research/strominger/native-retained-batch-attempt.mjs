// Owner-local attempt to assemble simultaneous retained native operations.
// Native laws are imported unchanged. No isotope layout, quota or ambient grid.
import {GenerativeAssemblyRules} from '../nima/generative-phase-assembly.mjs';
export {GenerativeAssemblyRules};
const sorted=xs=>[...new Set(xs)].sort((a,b)=>a-b);

export function frontier(rules,packets){
 if(!rules.describe(packets).valid)throw Error('Invalid source assembly');
 const selected=new Set(packets),groups=new Map();
 for(const id of packets)for(const index of rules.outgoing(id)){
  const op=rules.operations[index];rules.validateTransfer(op);
  // Exclude progress-free rereads from the batching search, not from the grammar.
  if(selected.has(op.target))continue;
  if(!groups.has(op.target))groups.set(op.target,{target:op.target,operations:[]});
  groups.get(op.target).operations.push(index);
 }
 return [...groups.values()].sort((a,b)=>a.target-b.target);
}

export function applyBatch(rules,packets,operationIds){
 const source=new Set(packets);
 for(const index of operationIds){
  const op=rules.operations[index];
  if(!op||!source.has(op.source))throw Error('Batch operation source is not in the prior snapshot');
  rules.validateTransfer(op);
 }
 const next=sorted([...packets,...operationIds.map(i=>rules.operations[i].target)]);
 const description=rules.describe(next);
 if(!description.valid)return {valid:false,reason:description.reason,packets:next};
 return {valid:true,packets:next,inspection:rules.inspect(next,description),operations:[...operationIds]};
}

export function compatibleBatches(rules,packets,{maxCandidates=14}={}){
 if(!Number.isInteger(maxCandidates)||maxCandidates<0||maxCandidates>20)throw Error('Explicit candidate budget required');
 const candidates=frontier(rules,packets);
 if(candidates.length>maxCandidates)return {complete:false,reason:'candidate-resource-bound',candidateCount:candidates.length,maxCandidates};
 const accepted=[],rejections={};
 // Complete nonempty subset enumeration for this one frozen source state.
 for(let mask=1;mask<2**candidates.length;mask++){
  const selected=candidates.filter((_,i)=>mask&(2**i));
  const ids=sorted([...packets,...selected.map(c=>c.target)]),d=rules.describe(ids);
  if(!d.valid){rejections[d.reason]=(rejections[d.reason]??0)+1;continue;}
  accepted.push({mask,packets:ids,operations:selected.flatMap(c=>c.operations)});
 }
 const masks=new Set(accepted.map(a=>a.mask));
 // All constraints in describe are persistent role/species/contact conflicts.
 // We also check maximality against ALL supersets in the checker.
 const maximal=accepted.filter(a=>candidates.every((_,i)=>(a.mask&(2**i))||!masks.has(a.mask|(2**i))));
 return {complete:true,candidates,subsetsExamined:2**candidates.length-1,accepted,rejections,maximal};
}

export function serializeRules(rules){
 return {packets:rules.packets,charts:rules.charts,operations:rules.operations,
 cells:rules.geometry.cells.map(({owner,...cell})=>({...cell,owner:{kind:owner.kind,origin:owner.origin,inverted:owner.inverted}})),
 points:Object.fromEntries(rules.geometry.points)};
}
