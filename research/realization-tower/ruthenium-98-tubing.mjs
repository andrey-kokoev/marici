import {buildRuthenium98Wiring} from './ruthenium-98-wiring.mjs';
import {buildRuthenium98Carrier} from './ruthenium-98-model.mjs';
import {buildSulfurTubeNetwork} from './sulfur-32-tube-network.mjs';

// Reuse the continuity algorithm, not Sulfur's N identities or routing law.
export function analyzeRuthenium98Tubing(){
 const wiring=buildRuthenium98Wiring(),cells=buildRuthenium98Carrier();
 const model={...wiring,channelGroups:cells.filter(c=>c.role==='neutron').map((c,i)=>({id:c.id,label:`Ru native N${i+1}`,members:[c.id]}))};
 const nativeEdges=new Map(),faceOwners=new Map(),pointKey=p=>p.join(','),nativeEdgeKey=(a,b)=>[pointKey(a),pointKey(b)].sort().join('|');
 for(const cell of cells)for(const face of cell.faces){
  const fk=face.map(pointKey).sort().join('|');if(!faceOwners.has(fk))faceOwners.set(fk,{face,owners:[]});faceOwners.get(fk).owners.push(cell.id);
  for(let i=0;i<3;i++)for(let j=i+1;j<3;j++){
   const id=nativeEdgeKey(face[i],face[j]);if(!nativeEdges.has(id))nativeEdges.set(id,{id,points:[face[i],face[j]],owners:new Set(),surface:false});nativeEdges.get(id).owners.add(cell.id);
  }
 }
 for(const {face,owners} of faceOwners.values())if(owners.length===1)for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)nativeEdges.get(nativeEdgeKey(face[i],face[j])).surface=true;
 const allEdges=[...nativeEdges.values()],used=new Set(model.edges.map(e=>e.id)),vertices=[...new Map(allEdges.flatMap(e=>e.points.map(p=>[pointKey(p),p]))).values()],visited=new Set(model.strands.flatMap(s=>s.guide.map(pointKey))),vertexStrata={corner:0,edge:0,face:0,interior:0};
 for(const p of vertices)vertexStrata[['interior','face','edge','corner'][p.filter(x=>x===-1).length]]++;
 const height=p=>p[2]+p[3]+2,slices=Array.from({length:5},(_,i)=>({level:i+1,edges:allEdges.filter(e=>height(e.points[0])!==height(e.points[1])&&Math.max(...e.points.map(height))===i+1).length}));
 const NCellEdges=cells.filter(c=>c.role==='neutron').map(c=>{const owned=allEdges.filter(e=>e.owners.has(c.id));return {cell:c.id,total:owned.length,wired:owned.filter(e=>used.has(e.id)).length};});
 const coverage={vertices:{total:vertices.length,visited:visited.size,missing:vertices.filter(p=>!visited.has(pointKey(p))),strata:vertexStrata},edges:{total:allEdges.length,wired:used.size,unwired:allEdges.length-used.size,surface:allEdges.filter(e=>e.surface).length,surfaceWired:allEdges.filter(e=>e.surface&&used.has(e.id)).length,interior:allEdges.filter(e=>!e.surface).length,interiorWired:allEdges.filter(e=>!e.surface&&used.has(e.id)).length,horizontal:allEdges.filter(e=>height(e.points[0])===height(e.points[1])).length},NCellEdges,slices,minimumMonotoneStrandsForFullEdgeCoverage:Math.max(...slices.map(s=>s.edges)),scope:'Full native edge coverage is a proposed completeness criterion, not implied by the sixteen polarity labels.'};
 const network=buildSulfurTubeNetwork(model),histogram={};
 for(const segment of network.segments)histogram[segment.edgeIds.length]=(histogram[segment.edgeIds.length]??0)+1;
 const nSegments=network.segments.filter(s=>s.nGroups.length),domains=network.identities.map(g=>({id:g.id,slots:g.segmentIds.map(id=>nSegments.findIndex(s=>s.id===id))})).sort((a,b)=>a.slots.length-b.slots.length||a.id.localeCompare(b.id));
 if(nSegments.length>30)throw Error('Incidence matching exceeds the exact bitset bound');
 // Equal-size bipartite perfect matchings; a used mask fixes the recursion depth.
 const memo=new Map();
 function count(i,used){
  if(i===domains.length)return 1n;
  if(memo.has(used))return memo.get(used);
  let total=0n;for(const slot of domains[i].slots)if(!(used&(1<<slot)))total+=count(i+1,used|(1<<slot));
  memo.set(used,total);return total;
 }
 const matchingCount=nSegments.length===domains.length?count(0,0):0n;
 // Test the already verified coordinate-pair exchange / path-reversal symmetry.
 const reversePoint=p=>[p[2],p[3],p[0],p[1]],shape=ps=>ps.map(p=>p.join(',')).sort().join('|'),flip=x=>x==='+'?'-':'+';
 const dualCells=new Map(network.identities.map(g=>{const source=cells.find(c=>c.id===g.id),target=cells.find(c=>shape(c.vertices)===shape(source.vertices.map(reversePoint)));return [g.id,target.id];}));
 const edgeKey=(a,b)=>[a.join(','),b.join(',')].sort().join('|');
 const signature=(edges,wires)=>JSON.stringify([[...edges].sort(),[...wires].sort()]);
 const segmentBySignature=new Map(nSegments.map(s=>[signature(s.edgeIds,s.strandIds),s]));
 const dualSegments=new Map(nSegments.map(s=>{
  const reversedEdges=s.points.slice(1).map((p,i)=>edgeKey(reversePoint(p),reversePoint(s.points[i])));
  const reversedWires=s.strandIds.map(id=>{const q=model.strands.find(w=>w.id===id).polarities;return `ru:wire:${q.a}${q.b}${flip(q.e)}${flip(q.p)}`;});
  const target=segmentBySignature.get(signature(reversedEdges,reversedWires));if(!target)throw Error('Tube reversal does not close');return [s.id,target.id];
 }));
 const fixedNCells=[...dualCells].filter(([a,b])=>a===b).map(([a])=>a),fixedNSegments=[...dualSegments].filter(([a,b])=>a===b).map(([a])=>a);
 const reversal={fixedNCells,fixedNSegments,equivariantMatchingCount:fixedNCells.length!==fixedNSegments.length?'0':null,obstruction:fixedNCells.length!==fixedNSegments.length?'Different fixed-point counts forbid a reversal-equivariant bijection':null};
 const sharedEdges=model.edges.filter(e=>e.strandIds.length>1).map(e=>({edgeId:e.id,points:e.guide,strands:e.strandIds.map(id=>{const s=model.strands.find(s=>s.id===id);return {id,polarities:s.polarities,label:s.label};}),NCells:e.carrierCells}));
 return {model,network,sharedEdges,reversal,coverage,audit:{strands:model.strands.length,nativeEdges:model.edges.length,continuousSegments:network.segments.length,edgeStepHistogram:histogram,longestSteps:Math.max(...network.segments.map(s=>s.edgeIds.length)),junctions:network.junctions.length,closedSegments:network.audit.closedSegments,
  nativeNCells:model.channelGroups.length,NIncidentSegments:nSegments.length,segmentsWithoutN:network.segments.filter(s=>!s.nGroups.length).length,segmentsIncidentToMultipleN:network.segments.filter(s=>s.nGroups.length>1).length,
  disconnectedNIncidence:network.identities.filter(g=>g.components.length>1).map(g=>({cell:g.id,components:g.components.length})),incidencePerfectMatchings:matchingCount.toString(),matchingStates:memo.size,reversalFixedNCells:fixedNCells.length,reversalFixedNSegments:fixedNSegments.length,reversalEquivariantMatchings:reversal.equivariantMatchingCount,
  NChannelCount:null,scope:'Native-edge continuity and incidence only. 64 possible N-cell/segment matchings do not select a canonical identification or establish equivalence to the 54 retained N records.'}};
}
