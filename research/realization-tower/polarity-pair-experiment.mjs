import {oppositeComparisonRole} from '../strominger/paired-polarity-model.mjs';
const key=vs=>vs.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
const center=g=>g.vertices[0].map((_,i)=>g.vertices.reduce((s,v)=>s+v[i],0)/g.vertices.length);
// Trial assumption: PE and EP are the same unordered pair. Other rules remain open.
export function trialPairRole(a,b){
 if(!['proton','neutron','electron'].includes(a)||!['proton','neutron','electron'].includes(b))throw Error('Two known input roles required');
 if(a==='proton'&&b==='proton')return 'neutron';
 if([a,b].includes('proton')&&[a,b].includes('electron'))return 'proton';
 return null;
}
function summarizePairs(pairs){
 const summary={pairs:pairs.length,PP:0,PE:0,unspecified:0};
 for(const p of pairs){if(p.result==='neutron')summary.PP++;else if(p.result==='proton')summary.PE++;else summary.unspecified++;}
 return summary;
}
function assess(pairs){
 const roles=[...new Set(pairs.map(p=>p.result).filter(Boolean))],unspecified=pairs.filter(p=>p.result===null).length;
 return {roles,unspecified,status:roles.length>1?'conflict':roles.length===0?'unspecified':unspecified?'partial':'covered'};
}
export function runPolarityPairExperiment(geometry,assigned){
 const occupied=new Map(assigned.map(g=>[g.id,g])),byShape=new Map(geometry.map(g=>[key(g.vertices),g]));
 if(occupied.size!==84||assigned.some(g=>g.kind!=='tetrahedron'))throw Error('Complete 84-cell source sector required');
 const sameCell=assigned.map(g=>{const mirrored=oppositeComparisonRole(g.role);return {source:g.id,roles:[g.role,mirrored],result:trialPairRole(g.role,mirrored)};});
 const reflectedTargets=new Map(geometry.filter(g=>g.kind==='tetrahedron'&&!occupied.has(g.id)).map(g=>[g.id,{target:g.id,proposals:[]}]));
 const octahedra=[],reflectionPairs=[];let boundaryDirections=0;
 for(const oct of geometry.filter(g=>g.kind==='octahedron')){
  const faceKeys=new Set(oct.faces.map(key));
  const neighbors=assigned.filter(g=>g.faces.some(f=>faceKeys.has(key(f))));
  if(neighbors.length!==4)throw Error('Each octahedron must have four source-sector face neighbors');
  const c=center(oct),localReflections=[];
  for(const source of neighbors){
   const reflected=source.vertices.map(v=>v.map((x,i)=>2*c[i]-x)),target=byShape.get(key(reflected));
   if(!target){boundaryDirections++;continue;}
   if(!reflectedTargets.has(target.id)||!target.faces.some(f=>faceKeys.has(key(f))))throw Error('Reflection must reach an opposite-sector face neighbor');
   const reverse=target.vertices.map(v=>v.map((x,i)=>2*c[i]-x));
   if(key(reverse)!==key(source.vertices))throw Error('Geometric reflection is not an involution');
   const role=oppositeComparisonRole(source.role),proposal={source:source.id,via:oct.id,target:target.id,role};
   reflectedTargets.get(target.id).proposals.push(proposal);
   const pair={source:source.id,target:target.id,via:oct.id,roles:[source.role,role],result:trialPairRole(source.role,role)};
   reflectionPairs.push(pair);localReflections.push(pair);
  }
  // Alternative: independently coloured source neighbors around the same octahedron.
  // These faces are NOT opposite faces; no polarity involution is claimed here.
  const neighborPairs=[];
  for(let i=0;i<neighbors.length;i++)for(let j=i+1;j<neighbors.length;j++){
   const a=neighbors[i],b=neighbors[j];neighborPairs.push({sources:[a.id,b.id],roles:[a.role,b.role],result:trialPairRole(a.role,b.role)});
  }
  octahedra.push({id:oct.id,sourceNeighbors:neighbors.map(g=>g.id),reflections:localReflections,neighborPairs,neighborAssessment:assess(neighborPairs)});
 }
 const targets=[...reflectedTargets.values()].map(t=>{
  if(t.proposals.length!==4)throw Error('Opposite tetrahedron must have four mirror witnesses');
  const roles=[...new Set(t.proposals.map(p=>p.role))];return {...t,roles,status:roles.length===1?'consistent':'conflict',suggestedRole:roles.length===1?roles[0]:null};
 });
 const agreed={proton:0,neutron:0,electron:0};for(const t of targets)if(t.suggestedRole)agreed[t.suggestedRole]++;
 const octahedralStatuses={covered:0,partial:0,conflict:0,unspecified:0};for(const o of octahedra)octahedralStatuses[o.neighborAssessment.status]++;
 return {assumptions:{PEisUnordered:true,allNeighborPairsMustAgreeForWholeCell:true,unlistedPairsRemainUnspecified:true,priorityApplied:false,mutatesConstruction:false},
  sameCell:{summary:summarizePairs(sameCell),pairs:sameCell,carrierMismatch:true,scope:'The original carrier is tetrahedral; a pair label does not turn it into an octahedron.'},
  oppositeFace:{summary:summarizePairs(reflectionPairs),boundaryDirections,targets,consistent:targets.filter(t=>t.status==='consistent').length,conflicts:targets.filter(t=>t.status==='conflict').length,agreedRoles:agreed,scope:'Counterfactual local mirror readings; conflicting target readings are not assigned.'},
  neighboringSources:{summary:summarizePairs(octahedra.flatMap(o=>o.neighborPairs)),octahedralStatuses,octahedra,scope:'Six unordered pairs of four independent source neighbors per octahedron. This is a different pairing, not an exact polarity mirror.'},
  conclusion:'Pure P/E polarity mirroring cannot produce PP. PP fusion requires independently coloured inputs. No unlisted pair rule, conflict resolution, or occupancy is inferred.'};
}
