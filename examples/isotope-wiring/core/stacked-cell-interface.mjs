// Isolated experiment: one reversible channel between two stacked cells.
// This is not a claim that the unchanged full-isotope graph has no bypasses.
export function buildStackedCellInterface(model,{mode='direct'}={}){
 if(!['direct','neutron-mediated'].includes(mode))throw Error('Unknown interface mode');
 const wrapper=model.wrappers.find(w=>JSON.stringify(w.spans)===JSON.stringify(['s1','s2']));
 if(!wrapper)throw Error('Missing shell 1/2 wrapper provenance');
 const [upperGateway,lowerGateway]=wrapper.gateways;
 if(upperGateway.shell!=='s1'||lowerGateway.shell!=='s2'||upperGateway.spacePort!=='B'||lowerGateway.spacePort!=='T')throw Error('Unexpected stacked ports');
 const spaces=[upperGateway.space,lowerGateway.space].map(id=>model.spaces.find(s=>s.id===id));
 if(spaces.some(s=>!s))throw Error('Missing stacked neutron space');
 const complexes=model.PEComplexes.filter(p=>spaces.some(s=>s.id===p.space));
 if(complexes.length!==4)throw Error('Expected two PE pairs in each of two cells');
 const owners=new Set([...spaces.map(s=>s.id),...complexes.map(p=>p.PE)]);
 const vertices=model.topology.vertices.filter(v=>owners.has(v.owner)).map(v=>structuredClone(v)),vertexIds=new Set(vertices.map(v=>v.id));
 const edges=model.topology.edges.filter(e=>vertexIds.has(e.from)&&vertexIds.has(e.to)).map(e=>structuredClone(e));
 const walks=model.topology.walks.filter(w=>complexes.some(p=>p.base===w.base)).map(w=>structuredClone(w));
 const from=spaces[0].ports.B,to=spaces[1].ports.T,channelSupports=[];
 function segment(id,a,b){channelSupports.push(id);edges.push({id,from:a,to:b,support:id,reverse:id+':reverse',kind:'stacked-interface'},{id:id+':reverse',from:b,to:a,support:id,reverse:id,kind:'stacked-interface'});}
 if(mode==='direct')segment('stack:s1-s2',from,to);
 else{
  // No invented 3D position or additional particle count. The intermediate
  // state is a candidate interface representation of the existing 1+2 wrapper.
  const id='interface:s1-s2';vertices.push({id,owner:id,layer:'neutron-interface',role:'N',port:'intermediate',provenance:wrapper.id});
  segment('stack:s1-interface',from,id);segment('stack:interface-s2',id,to);
 }
 const channelEdges=channelSupports,edgeMap=new Map(edges.map(e=>[e.id,e])),reverse=ids=>[...ids].reverse().map(id=>edgeMap.get(id).reverse);
 const source=complexes.find(p=>p.space===spaces[0].id&&p.mainPort==='B'),target=complexes.find(p=>p.space===spaces[1].id&&p.mainPort==='T');
 if(!source||!target)throw Error('Missing PE at contact');
 const transfer=[source.attachment,...channelEdges,edgeMap.get(target.attachment).reverse],back=reverse(transfer);
 function trace(start,ids){let at=start;const visited=[at];for(const id of ids){const e=edgeMap.get(id);if(!e||e.from!==at)throw Error('Noncomposable interface trace');at=e.to;visited.push(at);}return visited;}
 const forwardVertices=trace(source.base,transfer),reverseVertices=trace(target.base,back);
 if(JSON.stringify(reverseVertices)!==JSON.stringify([...forwardVertices].reverse()))throw Error('Transfer does not reverse');
 const excursion=[...walks.find(w=>w.base===source.base).edges,...transfer,...walks.find(w=>w.base===target.base).edges,...back];
 if(trace(source.base,excursion).at(-1)!==source.base)throw Error('Excursion did not close');
 function reachable(a,b,removed=new Set(),rows=edges){const adj=new Map();for(const e of rows)if(!removed.has(e.support)){if(!adj.has(e.from))adj.set(e.from,[]);adj.get(e.from).push(e.to);}const seen=new Set([a]),q=[a];for(let i=0;i<q.length;i++)for(const v of adj.get(q[i])||[])if(!seen.has(v)){seen.add(v);q.push(v);}return seen.has(b);}
 const bridgeChecks=channelSupports.map(support=>({support,disconnectedWhenRemoved:!reachable(from,to,new Set([support]))}));
 if(!reachable(from,to)||bridgeChecks.some(c=>!c.disconnectedWhenRemoved))throw Error('Interface has a bypass');
 // Explicitly expose the isolation boundary, including old wrapper terminals.
 const excludedInterfaces=model.topology.edges.filter(e=>vertexIds.has(e.from)!==vertexIds.has(e.to)).map(e=>({id:e.id,kind:e.kind,from:e.from,to:e.to}));
 const bypassInOriginalModel=reachable(from,to,new Set(),model.topology.edges);
 const supports=new Set(edges.map(e=>e.support)),neutralVertices=vertices.filter(v=>v.layer!=='PE'),neutralIds=new Set(neutralVertices.map(v=>v.id)),neutralSupports=new Set(edges.filter(e=>neutralIds.has(e.from)&&neutralIds.has(e.to)).map(e=>e.support));
 return {definitionId:model.definitionId,mode,status:'verified-for-isolated-interface',topology:{vertices,edges,walks},spaces:structuredClone(spaces),PEComplexes:structuredClone(complexes),
  interface:{from,to,channelSupports,forward:channelEdges,reverse:reverse(channelEdges),reversibleChannels:1,bridgeChecks,wrapperProvenance:wrapper.id},
  counts:{cells:2,PEOccurrences:4,vertices:vertices.length,supports:supports.size,cycleRank:supports.size-vertices.length+1,neutralCycleRank:neutralSupports.size-neutralVertices.length+1},
  transfer:{from:source.pair,to:target.pair,edges:transfer,reverseEdges:back,forwardVertices,reverseVertices,excursion},
  excludedInterfaces,bypassInOriginalModel,frameReturn:'unknown',
  inventory:{fullIsotope:structuredClone(model.inventory),addedNeutrons:0,interpretation:mode==='direct'?'No mediator added.':'Intermediate interface state is a subdivision candidate associated with the existing 1+2 wrapper, not an extra neutron claim.'},
  limits:['Only shell 1 and the top cell of shell 2 are isolated here. Other shell-2 cells and all wrapper-perimeter transport are outside this trial.','Internal neutral paths may branch. The channel is unique as an interface, not as a walk allowing arbitrary loops.','The original full model retains bypass routes; its attachments require a separate decision before this bottleneck can be asserted globally.','Stacking supplies incidence only; no 3D metric, depth coordinates, or SO(3) transport is inferred.']};
}
