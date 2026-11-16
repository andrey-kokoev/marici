// Exhaustive wrapper/terminal/perimeter coverage, with counted shortest local
// space paths. A representative path is evidence of reachability, not a rule.
export function auditLayeredTransfers(model){
 if(model.wrappers.some(w=>w.gateways.length!==2))throw Error('Two-terminal transfer audit does not apply to single-anchor coherence wrappers');
 const vertices=new Map(model.topology.vertices.map(v=>[v.id,v])),edges=new Map(model.topology.edges.map(e=>[e.id,e])),spaces=new Map(model.spaces.map(s=>[s.id,s]));
 if(vertices.size!==model.topology.vertices.length||edges.size!==model.topology.edges.length)throw Error('Duplicate graph IDs');
 for(const e of edges.values()){const r=edges.get(e.reverse);if(!vertices.has(e.from)||!vertices.has(e.to)||!r||r.from!==e.to||r.to!==e.from||r.reverse!==e.id||r.kind!==e.kind||r.support!==e.support)throw Error('Invalid reverse interface');}
 const neutralKinds=new Set(['neutron-space-boundary','tetrahedral-neutron-leg','neutron-space-contact']);
 const reverse=ids=>[...ids].reverse().map(id=>edges.get(id).reverse);
 function trace(start,ids){let at=start;const visited=[at];for(const id of ids){const e=edges.get(id);if(!e||e.from!==at)throw Error('Noncomposable transfer');at=e.to;visited.push(at);}return visited;}
 function shortest(shell,start,target){
  const allowed=new Set([...vertices.values()].filter(v=>v.layer==='neutron-space'&&spaces.get(v.owner)?.shell===shell).map(v=>v.id)),adj=new Map([...allowed].map(v=>[v,[]]));
  if(!allowed.has(start)||!allowed.has(target))throw Error('Gateway leaves source shell');
  for(const e of edges.values())if(neutralKinds.has(e.kind)&&allowed.has(e.from)&&allowed.has(e.to))adj.get(e.from).push(e);
  // Sorting only makes the displayed witness reproducible, never resolves the
  // alternatives: every shortest route contributes to the exact count.
  for(const a of adj.values())a.sort((a,b)=>a.id.localeCompare(b.id));
  const distance=new Map([[start,0]]),counts=new Map([[start,1n]]),witness=new Map([[start,[]]]),q=[start];
  for(let i=0;i<q.length;i++){const v=q[i];for(const e of adj.get(v)){
   const d=distance.get(v)+1;
   if(!distance.has(e.to)){distance.set(e.to,d);counts.set(e.to,counts.get(v));witness.set(e.to,[...witness.get(v),e.id]);q.push(e.to);}
   else if(distance.get(e.to)===d)counts.set(e.to,counts.get(e.to)+counts.get(v));
  }}
  return distance.has(target)?{length:distance.get(target),count:counts.get(target),edges:witness.get(target)}:null;
 }
 const transfers=[],blocked=[];
 for(const wrapper of model.wrappers)for(let endpoint=0;endpoint<2;endpoint++){
  const entry=wrapper.gateways[endpoint],exit=wrapper.gateways[1-endpoint],entryEdge=edges.get(entry.attachment),exitEdge=edges.get(exit.attachment);
  if(!entryEdge||!exitEdge||entryEdge.kind!=='space-to-wrapper'||exitEdge.kind!=='space-to-wrapper')throw Error('Missing wrapper terminal');
  const targets=model.PEComplexes.filter(p=>p.space===exit.space&&p.mainPort===exit.spacePort);
  if(targets.length!==1)throw Error('Expected a unique PE occurrence at the exit port');
  const target=targets[0],targetEdge=edges.get(target.attachment);
  for(const source of model.PEComplexes.filter(p=>spaces.get(p.space)?.shell===entry.shell)){
   const sourceEdge=edges.get(source.attachment);if(!sourceEdge||!targetEdge)throw Error('Missing PE interface');
   const local=shortest(entry.shell,sourceEdge.to,entryEdge.from);
   if(!local){blocked.push({source:source.pair,wrapper:wrapper.id,endpoint,reason:'No local neutron-space route'});continue;}
   const backwards=shortest(entry.shell,entryEdge.from,sourceEdge.to);if(backwards.count!==local.count||backwards.length!==local.length)throw Error('Local reversal count mismatch');
   // T-R-B versus T-L-B, reversed when entering through B.
   const right=wrapper.boundary.slice(0,2),left=reverse(wrapper.boundary.slice(2));
   for(const [side,forward] of [['R',right],['L',left]]){
    const perimeter=endpoint===0?forward:reverse(forward),ids=[source.attachment,...local.edges,entry.attachment,...perimeter,exitEdge.reverse,targetEdge.reverse],rev=reverse(ids);
    const forwardVertices=trace(source.base,ids),reverseVertices=trace(target.base,rev);
    if(forwardVertices.at(-1)!==target.base||JSON.stringify(reverseVertices)!==JSON.stringify([...forwardVertices].reverse()))throw Error('Transfer reversal mismatch');
    const sourceLoop=model.topology.walks.find(w=>w.base===source.base),targetLoop=model.topology.walks.find(w=>w.base===target.base);
    const excursion=[...sourceLoop.edges,...ids,...targetLoop.edges,...rev];if(trace(source.base,excursion).at(-1)!==source.base)throw Error('Excursion does not close');
    transfers.push({source:source.pair,target:target.pair,wrapper:wrapper.id,entry:entry.wrapperPort,side,localLength:local.length,shortestLocalAlternatives:local.count.toString(),uniqueShortestLocalRoute:local.count===1n,edges:ids,reverseEdges:rev,forwardVertices,reverseVertices,excursion});
   }
  }
 }
 const byPE=model.PEComplexes.map(p=>{const rows=transfers.filter(t=>t.source===p.pair);return {pair:p.pair,wrappers:[...new Set(rows.map(r=>r.wrapper))],representatives:rows.length,shortestTransferChoices:rows.reduce((sum,r)=>sum+BigInt(r.shortestLocalAlternatives),0n).toString(),ambiguousEvenWithWrapperAndSide:rows.some(r=>!r.uniqueShortestLocalRoute)};});
 return {definitionId:model.definitionId,status:blocked.length||byPE.some(p=>!p.representatives)?'refuted':'verified-for-declared-interfaces',
  counts:{PEOccurrences:byPE.length,wrappers:model.wrappers.length,representativeTransfers:transfers.length,representativesWithMultipleLocalRoutes:transfers.filter(t=>!t.uniqueShortestLocalRoute).length,shortestTransferChoices:byPE.reduce((sum,p)=>sum+BigInt(p.shortestTransferChoices),0n).toString(),blocked:blocked.length},
  transfers,byPE,blocked,checks:{reverseInterfaces:true,localShortestCountsReversalInvariant:true,representativeTransfersReverseExactly:true,basedExcursionsClose:true},
  frameReturn:'unknown',
  limits:['Coverage is every source PE to the opposite terminal PE of each wrapper incident on its shell, not all PE-to-PE destination pairs.','Completeness covers both perimeter sides, with one witness and exact count for shortest local-space routes measured by graph steps, not metric length.','Longer routes and repeated-wrapper tours are not enumerated.','Lexicographic witness choice is not a routing law; route multiplicities remain explicit.','Frame transports are absent. Vertex closure and reverse incidence do not prove SO(3) frame return.']};
}
