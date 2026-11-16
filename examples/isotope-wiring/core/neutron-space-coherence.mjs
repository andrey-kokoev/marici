// Neutral space may branch. The tested condition is agreement of transport
// between paths, not uniqueness of a successor arrow.
import {auditFrameReturn} from './frame-return.mjs';
import {auditLayeredTransfers} from './layered-transfer-audit.mjs';
const transpose=a=>a[0].map((_,i)=>a.map(r=>r[i]));
const multiply=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,x,k)=>s+x*b[k][j],0)));
const rotation=(t,axis)=>{const c=Math.cos(t),s=Math.sin(t);return axis==='x'?[[1,0,0],[0,c,-s],[0,s,c]]:[[c,-s,0],[s,c,0],[0,0,1]];};
export function buildNeutronCoherence(model,{maxPathsPerPair=256,localCoverage='terminal-transfers'}={}){
 if(!Number.isSafeInteger(maxPathsPerPair)||maxPathsPerPair<2)throw Error('Path enumeration limit must be an integer >= 2');
 if(model.topology.turns!==undefined)throw Error('Restricted turns need a state-space cycle audit; cannot discard routing restrictions');
 if(!['terminal-transfers','actual-interface-ports'].includes(localCoverage))throw Error('Unknown local coverage policy');
 // The new coverage mode reads actual attachments, not nominal span endpoints.
 const transfers=localCoverage==='terminal-transfers'?auditLayeredTransfers(model):null;
 if(transfers&&transfers.status!=='verified-for-declared-interfaces')throw Error('Cannot claim complete coherence coverage with blocked transfers');
 const allVertices=new Map(model.topology.vertices.map(v=>[v.id,v])),allEdges=new Map(model.topology.edges.map(e=>[e.id,e]));
 if(allVertices.size!==model.topology.vertices.length||allEdges.size!==model.topology.edges.length)throw Error('Duplicate topology IDs');
 for(const e of allEdges.values()){const r=allEdges.get(e.reverse);if(!allVertices.has(e.from)||!allVertices.has(e.to)||!r||r.reverse!==e.id||r.from!==e.to||r.to!==e.from||r.support!==e.support||r.kind!==e.kind)throw Error('Invalid reverse interface');}
 const neutralLayers=new Set(['neutron-space','wrapper','neutron-interface']);
 // N here is an audit-base role, not an additional inventory particle.
 const vertices=model.topology.vertices.filter(v=>neutralLayers.has(v.layer)).map(v=>({...structuredClone(v),role:'N'})),vertexMap=new Map(vertices.map(v=>[v.id,v]));
 const edges=model.topology.edges.filter(e=>vertexMap.has(e.from)&&vertexMap.has(e.to)).map(e=>structuredClone(e)),edgeMap=new Map(edges.map(e=>[e.id,e])),adj=new Map(vertices.map(v=>[v.id,[]]));
 for(const e of edges)adj.get(e.from).push(e);
 for(const a of adj.values())a.sort((a,b)=>a.id.localeCompare(b.id));
 const reverse=ids=>[...ids].reverse().map(id=>edgeMap.get(id).reverse),supports=new Map();
 for(const e of edges){const old=supports.get(e.support);if(old&&old.id!==e.reverse&&old.id!==e.id)throw Error('More than two arrows on a support');if(!old)supports.set(e.support,e);}
 const seen=new Set(),tree=new Set(),components=[],basis=[],walks=[];
 for(const start of [...vertexMap.keys()].sort())if(!seen.has(start)){
  const routes=new Map([[start,[]]]),q=[start];seen.add(start);
  for(let i=0;i<q.length;i++)for(const e of adj.get(q[i]))if(!routes.has(e.to)){routes.set(e.to,[...routes.get(q[i]),e.id]);tree.add(e.support);seen.add(e.to);q.push(e.to);}
  components.push({root:start,vertices:q});
  for(const e of [...supports.values()].sort((a,b)=>a.support.localeCompare(b.support)))if(routes.has(e.from)&&!tree.has(e.support)){
   const w={id:`neutral-basis:${basis.length}`,kind:'N',base:start,edges:[...routes.get(e.from),e.id,...reverse(routes.get(e.to))],chord:e.support};basis.push(w);walks.push(w);
  }
 }
 // Retain BOTH sides of each wrapper as an explicit path comparison.
 const wrapperComparisons=model.wrappers.map(w=>{
  const first=w.boundary.slice(0,2),second=reverse(w.boundary.slice(2)),id=`wrapper-comparison:${w.id}`;
  walks.push({id,kind:'N',base:w.ports.T,edges:[...first,...reverse(second)]});
  return {id,from:w.ports.T,to:w.ports.B,paths:[first,second]};
 });
 const spaceShell=new Map(model.spaces.map(s=>[s.id,s.shell]));
 function shortestPaths(from,to){
  const shell=spaceShell.get(vertexMap.get(from).owner),local=id=>vertexMap.get(id)?.layer==='neutron-space'&&spaceShell.get(vertexMap.get(id).owner)===shell;
  const distance=new Map([[from,0]]),parents=new Map([[from,[]]]),q=[from];
  for(let i=0;i<q.length;i++)for(const e of adj.get(q[i]))if(local(e.to)){
   const d=distance.get(e.from)+1;
   if(!distance.has(e.to)){distance.set(e.to,d);parents.set(e.to,[e]);q.push(e.to);}
   else if(distance.get(e.to)===d)parents.get(e.to).push(e);
  }
  if(!distance.has(to))throw Error('Missing local route');
  const paths=[];
  function visit(at,suffix){if(at===from){if(paths.length>=maxPathsPerPair)throw Error('Path enumeration limit exceeded; no truncated completeness claim');paths.push(suffix);return;}for(const e of parents.get(at))visit(e.from,[e.id,...suffix]);}
  visit(to,[]);return paths;
 }
 const compared=new Set(),localComparisons=[],candidates=[];
 if(transfers){for(const t of transfers.transfers)if(!t.uniqueShortestLocalRoute)candidates.push({from:t.forwardVertices[1],to:t.forwardVertices[1+t.localLength],expected:t.shortestLocalAlternatives});}
 else{
  const targets=new Set(edges.filter(e=>['space-to-wrapper','stacked-interface'].includes(e.kind)).flatMap(e=>[e.from,e.to]).filter(id=>vertexMap.get(id).layer==='neutron-space'));
  for(const pe of model.PEComplexes){const attachment=allEdges.get(pe.attachment);if(!attachment||attachment.kind!=='PE-to-neutron-space'||attachment.from!==pe.base)throw Error('Missing PE interface');
   const from=attachment.to,shell=spaceShell.get(vertexMap.get(from)?.owner);if(!shell)throw Error('PE interface misses neutron space');
   const localTargets=[...targets].filter(to=>spaceShell.get(vertexMap.get(to).owner)===shell);
   if(!localTargets.length)throw Error('Missing same-shell interface port');
   for(const to of localTargets)candidates.push({from,to});
  }
 }
 for(const {from,to,expected} of candidates){
  const key=JSON.stringify([from,to]);if(compared.has(key))continue;compared.add(key);
  const paths=shortestPaths(from,to);if(expected!==undefined&&BigInt(paths.length)!==BigInt(expected))throw Error('Path count disagrees with transfer audit');
  if(paths.length===1)continue;
  const ids=[];
  for(let i=1;i<paths.length;i++){const id=`local-comparison:${localComparisons.length}:${i}`;ids.push(id);walks.push({id,kind:'N',base:from,edges:[...paths[0],...reverse(paths[i])]});}
  localComparisons.push({from,to,paths,walks:ids});
 }
 const cycleRank=supports.size-vertices.length+components.length;if(basis.length!==cycleRank)throw Error('Incomplete neutral cycle basis');
 return {definitionId:model.definitionId,localCoverage,localAccessPairsChecked:compared.size,topology:{vertices,edges,walks},basis,components,localComparisons,wrapperComparisons,
  counts:{vertices:vertices.length,supports:supports.size,components:components.length,cycleRank,basisCycles:basis.length,localPathPairs:localComparisons.length,wrapperPathPairs:wrapperComparisons.length,comparisonWalks:walks.length-basis.length},
  criterion:'For paths p and q with common endpoints, compare transport around p followed by inverse(q). Identity holonomy means equal endpoint frame transport; path uniqueness is not required.',
  scope:'All composable neutral-space and wrapper turns are candidate-admissible. The cycle basis tests flatness of this declared graph connection, not a physical law or a proof of simple connectivity. No filled faces or homotopy relations are inferred from the drawing.',
  limits:[localCoverage==='terminal-transfers'?'Local comparisons retain all shortest alternatives reported by the transfer audit; the basis additionally covers longer cycles algebraically.':'Local comparisons cover PE access to actual same-shell interface ports, including the stacked contact. Wrapper side comparisons are internal loops, not assertions of two transport terminals.','N audit-base roles do not change particle inventory.','Frame agreement is a proposed coherence criterion; nontrivial holonomy may instead require explicit physical interpretation.','PE circulation is not included in the neutral coherence audit.']};
}
export function studyNeutronCoherence(model,options={}){
 const comparison=buildNeutronCoherence(model,options),actual=auditFrameReturn(comparison.topology),flat=structuredClone(comparison.topology);
 // Synthetic, noncommuting vertex gauges: a positive implementation control.
 const frames=new Map(flat.vertices.map((v,i)=>[v.id,multiply(rotation(i*Math.PI/7,'x'),rotation(i*Math.PI/11,'z'))]));
 for(const e of flat.edges)e.transport=multiply(frames.get(e.to),transpose(frames.get(e.from)));
 const flatControl=auditFrameReturn(flat),twisted=structuredClone(flat),target=comparison.localComparisons[0]?.paths[0][0]??comparison.basis[0]?.edges.find(id=>comparison.topology.edges.find(e=>e.id===id)?.support===comparison.basis[0].chord);
 if(!target)throw Error('No comparison cycle for hostile control');
 const edge=twisted.edges.find(e=>e.id===target),back=twisted.edges.find(e=>e.id===edge.reverse);edge.transport=multiply(rotation(Math.PI/2,'x'),edge.transport);back.transport=transpose(edge.transport);
 const twistedControl=auditFrameReturn(twisted);
 return {comparison,actual,flatControl,twistedControl,twistedSupport:edge.support,status:actual.status,
  conclusion:'Multiple neutral paths are retained, not rejected. Missing transport leaves coherence unknown. Flat and inverse-consistently twisted controls test the checker, not the physical diagram.'};
}
