// A declared layered attachment trial, not inferred from enclosure or screen crossings.
import {bindCalciumLocalPaths} from './diagram-path-trial.mjs';
export function buildLayeredCalcium(definition,svg){
 const local=bindCalciumLocalPaths(definition,svg),vertices=[],edges=[],spaces=[],complexes=[],wrappers=[],attachments=[],walks=[];
 const vertexMap=new Map(),edgeMap=new Map();
 function vertex(id,layer,owner,port,position,role='junction'){
  if(vertexMap.has(id))throw Error('Duplicate layered port');const v={id,layer,owner,port,position,role};vertices.push(v);vertexMap.set(id,v);return id;
 }
 function connect(id,from,to,kind,provenance){
  if(!vertexMap.has(from)||!vertexMap.has(to)||edgeMap.has(id)||edgeMap.has(id+':reverse'))throw Error('Invalid layered incidence');
  const f={id,from,to,kind,support:id,reverse:id+':reverse',provenance},r={...f,id:f.reverse,from:to,to:from,reverse:id};edges.push(f,r);edgeMap.set(f.id,f);edgeMap.set(r.id,r);return f.id;
 }
 function cycle(id,ports,kind){return ports.map((p,i)=>connect(`${id}:edge:${i}`,p,ports[(i+1)%ports.length],kind,{owner:id}));}
 const cells=new Map();
 for(const m of svg.matchAll(/<g class="cell-hit" data-cell="([^"]+)"[^>]*><path fill="transparent" d="([^"]+)"/g)){
  const n=m[2].match(/-?\d+(?:\.\d+)?/g).map(Number);if(n.length!==8)throw Error('Expected four cell corners');
  const cell=definition.graph.cells.find(c=>c.id===m[1]);if(!cell)throw Error('Unknown cell');
  const points=Object.fromEntries(['T','R','B','L'].map((p,i)=>[p,n.slice(2*i,2*i+2)])),owner=`space:${cell.id}`,ports={};
  for(const p of ['T','R','B','L'])ports[p]=vertex(`${owner}:${p}`,'neutron-space',owner,p,points[p]);
  const boundary=cycle(owner,Object.values(ports),'neutron-space-boundary');
  const neutronLegs=[connect(`${owner}:leg:TB`,ports.T,ports.B,'tetrahedral-neutron-leg',{cell:cell.id,oppositeLeg:'LR',projectedCrossingIsJunction:false}),connect(`${owner}:leg:LR`,ports.L,ports.R,'tetrahedral-neutron-leg',{cell:cell.id,oppositeLeg:'TB',projectedCrossingIsJunction:false})];
  const space={id:owner,cell:cell.id,shell:cell.shell,ports,boundary,neutronLegs,tetrahedralTopology:{vertices:4,edges:6,centralJunction:false},inventoryMeaning:'Shared neutron-space presentation of this two-PE cell; not an additional N count.'};spaces.push(space);cells.set(cell.id,{cell,points,space});
 }
 for(const b of local.bindings.filter(b=>b.source.pair)){
  const pair=definition.graph.pairs.find(p=>p.id===b.source.pair),cell=cells.get(pair.cell),owner=`PE:${pair.id}`;
  const ports=b.positions.map((position,i)=>vertex(`${owner}:v${i}`,'PE',owner,i,position,i===0?'PE':'junction'));
  const boundary=cycle(owner,ports,'PE-cycle');walks.push({id:owner,kind:'PE',base:ports[0],edges:boundary});
  const attachment=connect(`attach:${owner}`,ports[0],cell.space.ports[b.source.mainPort],'PE-to-neutron-space',{rule:'PE main port attaches to the same named port of its own cell space',pair:pair.id,cell:pair.cell});
  attachments.push({id:attachment,kind:'local-PE',from:ports[0],to:cell.space.ports[b.source.mainPort]});complexes.push({id:pair.cell,pair:pair.id,PE:owner,base:ports[0],space:cell.space.id,mainPort:b.source.mainPort,attachment});
 }
 // Candidate local assembly rule: identify no vertices; explicitly connect
 // coincident named ports of DIFFERENT neutron spaces in the SAME shell.
 for(let i=0;i<spaces.length;i++)for(let j=i+1;j<spaces.length;j++)if(spaces[i].shell===spaces[j].shell){
  for(const a of Object.values(spaces[i].ports))for(const b of Object.values(spaces[j].ports))if(JSON.stringify(vertexMap.get(a).position)===JSON.stringify(vertexMap.get(b).position)){
   const id=connect(`space-contact:${attachments.length}`,a,b,'neutron-space-contact',{rule:'Declared same-shell coincident-boundary-port contact',cells:[spaces[i].cell,spaces[j].cell]});attachments.push({id,kind:'same-shell',from:a,to:b});
  }
 }
 // Wrappers have their OWN square ports. A terminal attachment is a typed
 // interface, not a claim that the displayed perimeter touches the gateway.
 for(const b of local.bindings.filter(b=>b.source.wrapper)){
  const owner=`wrapper:${b.source.wrapper}`,ports={};
  ['T','R','B','L'].forEach((p,i)=>{ports[p]=vertex(`${owner}:${p}`,'wrapper',owner,p,b.positions[i]);});
  const boundary=cycle(owner,Object.values(ports),'neutron-wrapper-boundary'),spans=b.source.spans;
  const gateways=[];
  for(const [shell,side,wrapperPort] of [[spans[0],'B','T'],[spans.at(-1),'T','B']]){
   const candidates=spaces.filter(s=>s.shell===shell).map(s=>({space:s,vertex:vertexMap.get(s.ports[side])})).filter(c=>c.vertex.position[0]===0);
   candidates.sort((a,b)=>side==='B'?b.vertex.position[1]-a.vertex.position[1]:a.vertex.position[1]-b.vertex.position[1]);
   if(!candidates.length||candidates[1]?.vertex.position[1]===candidates[0].vertex.position[1])throw Error('Missing or ambiguous axial gateway');
   const gateway=candidates[0],id=connect(`attach:${owner}:${wrapperPort}`,gateway.vertex.id,ports[wrapperPort],'space-to-wrapper',{rule:'Trial axial terminal policy: upper-shell bottom to T, lower-shell top to B',span:spans});
   gateways.push({shell,space:gateway.space.id,spacePort:side,wrapperPort,attachment:id});attachments.push({id,kind:'wrapper-terminal',from:gateway.vertex.id,to:ports[wrapperPort]});
  }
  wrappers.push({id:owner,ports,boundary,spans,gateways,intermediateShells:spans.slice(1,-1),intermediateAttachments:[]});
 }
 const containment=[];
 for(const outer of wrappers)for(const inner of wrappers)if(outer.spans.length>inner.spans.length&&inner.spans.every(s=>outer.spans.includes(s)))containment.push({outer:outer.id,inner:inner.id,kind:'span-containment',createsAttachment:false});
 const adj=new Map(vertices.map(v=>[v.id,[]]));for(const e of edges)adj.get(e.from).push(e);
 const seen=new Set(),components=[];
 for(const v of vertices)if(!seen.has(v.id)){const q=[v.id];seen.add(v.id);for(let i=0;i<q.length;i++)for(const e of adj.get(q[i]))if(!seen.has(e.to)){seen.add(e.to);q.push(e.to);}components.push(q);}
 // Concrete PE -> local space -> wrapper right side -> local space -> PE trace.
 const wrapper=wrappers[0],upper=complexes.find(c=>c.space===wrapper.gateways[0].space&&c.mainPort==='B'),lower=complexes.find(c=>c.space===wrapper.gateways[1].space&&c.mainPort==='T');
 if(!upper||!lower)throw Error('No PE at declared demonstration gateways');
 const outward=[upper.attachment,wrapper.gateways[0].attachment,wrapper.boundary[0],wrapper.boundary[1],edgeMap.get(wrapper.gateways[1].attachment).reverse,edgeMap.get(lower.attachment).reverse];
 const returning=[...outward].reverse().map(id=>edgeMap.get(id).reverse),trace=(start,ids)=>{const visited=[start];let at=start;for(const id of ids){const e=edgeMap.get(id);if(!e||e.from!==at)throw Error('Noncomposable layered trace');at=e.to;visited.push(at);}return visited;};
 const forwardVertices=trace(upper.base,outward),reverseVertices=trace(lower.base,returning);
 if(forwardVertices.at(-1)!==lower.base||reverseVertices.at(-1)!==upper.base)throw Error('Transfer endpoint mismatch');
 const excursions=[...walks.find(w=>w.base===upper.base).edges,...outward,...walks.find(w=>w.base===lower.base).edges,...returning];
 trace(upper.base,excursions);
 return {definitionId:definition.id,status:'candidate',topology:{vertices,edges,walks},spaces,PEComplexes:complexes,wrappers,attachments,containment,
  counts:{PEOccurrences:complexes.length,neutronSpaces:spaces.length,wrappers:wrappers.length,localPEAttachments:attachments.filter(a=>a.kind==='local-PE').length,wrapperAttachments:attachments.filter(a=>a.kind==='wrapper-terminal').length,sameShellContacts:attachments.filter(a=>a.kind==='same-shell').length,components:components.length},
  inventory:{PE:definition.Z,N:definition.N,localAssignedN:definition.Z,wrapperN:wrappers.length,neutronSpacesAddInventory:false},
  transfer:{from:upper.pair,to:lower.pair,wrapper:wrapper.id,edges:outward,reverseEdges:returning,forwardVertices,reverseVertices,PEExcursion:excursions},
  components,policy:'Explicit candidate interfaces; no cross-layer vertex merging, no incidence from projected crossings, no transport arrow from containment alone.',
  residuals:['Axial wrapper gateways and same-shell boundary contacts are trial attachment choices.','Wrapper T-to-B has two perimeter routes; the demonstration chooses the right side, not a uniqueness claim.','Neutron-space transport and SO(3) frame law remain unspecified.','Local spaces retain tetrahedral boundary and opposite neutron legs; cross-layer attachments are additional declared interfaces, not an isomorphism with the earlier flattened graph.']};
}
