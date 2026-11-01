import {readFile} from 'node:fs/promises';
import {buildSulfurIncomingBundle} from '../../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {buildRouteBlindGeometry} from '../../research/realization-tower/sulfur-route-blind.mjs';
import {generateUpperNeighbourhood} from '../../research/realization-tower/sulfur-neighbourhood-generator.mjs';
export async function loadUpperCalibration(){
 return JSON.parse(await readFile(new URL('../../research/realization-tower/sulfur-upper-local-calibration.v1.json',import.meta.url),'utf8'));
}
export function queriesFromIncomingPrefixes(prefixes){
 const groups=new Map();
 for(const {prefix,record} of prefixes){
  if(prefix.length<2)throw Error('Need an actual arrival edge');
  const at=prefix.at(-1),id=at.join(',');
  if(!groups.has(id))groups.set(id,{at:[...at],arrivals:[]});
  groups.get(id).arrivals.push({previous:[...prefix.at(-2)],record:structuredClone(record)});
 }
 return [...groups.values()];
}
export async function runNeighbourhoodProbe(){
 const calibration=await loadUpperCalibration(),geometry=buildRouteBlindGeometry(1),reference=buildSulfurIncomingBundle(),before=JSON.stringify(reference);
 // Cut BEFORE either carrier or its head. No supplied pair grouping, joinCell,
 // carrier list, next ports, or native future route is present in these inputs.
 const prefixes=reference.strands.map((s,i)=>({prefix:s.guide.slice(0,3),record:{id:s.id,polarities:{...s.polarities},colour:s.label,payload:{ordinal:i,nested:[null,{phase:-2}]}}}));
 const queries=queriesFromIncomingPrefixes(prefixes);
 const predicted=queries.map(query=>({query,result:generateUpperNeighbourhood(geometry,query,calibration)}));
 // Compare only after every neighbourhood has been generated.
 const comparisons=predicted.flatMap(({result})=>result.generated.map(g=>{
  const s=reference.strands.find(s=>s.id===g.record.id),expected=s.guide.slice(1,5),input=prefixes.find(p=>p.record.id===g.record.id).record;
  return {id:g.record.id,expected,actual:g.points,routeMatch:JSON.stringify(expected)===JSON.stringify(g.points),recordPreserved:JSON.stringify(input)===JSON.stringify(g.record)};
 }));
 const flipped=queries.map(query=>{
  const changed=structuredClone(query);for(const a of changed.arrivals)a.record.polarities.b=a.record.polarities.b==='+'?'-':'+';
  return generateUpperNeighbourhood(geometry,changed,calibration);
 });
 const originalPaths=new Map(predicted.flatMap(p=>p.result.generated.map(g=>[g.record.id,g.points])));
 const changedCarriers=flipped.flatMap(r=>r.generated).filter(g=>JSON.stringify(g.points[2])!==JSON.stringify(originalPaths.get(g.record.id)[2])).length;
 const withoutB=new Map();
 for(const query of queries)for(const arrival of query.arrivals){
  const {a,p,e}=arrival.record.polarities;
  const observable={at:query.at,previous:arrival.previous,polarities:{a,p,e},colour:arrival.record.colour},id=JSON.stringify(observable);
  if(!withoutB.has(id))withoutB.set(id,{observable,records:[]});
  withoutB.get(id).records.push({id:arrival.record.id,b:arrival.record.polarities.b,generatedHead:originalPaths.get(arrival.record.id)[2]});
 }
 if(JSON.stringify(reference)!==before)throw Error('Reference was changed');
 return {schema:'sulfur-neighbourhood-probe.v1',calibration,geometry:geometry.audit,referenceScope:reference.audit.routingStatus,
  calibrationScope:'Frozen previously calibrated rule; this is not a new leave-one-junction-out fit or independent validation of rule discovery.',
  sourceRoutesUnchanged:true,predicted,comparisons,bAblation:[...withoutB.values()],
  counts:{junctions:queries.length,carriers:predicted.reduce((n,p)=>n+p.result.groups.filter(g=>g.status==='unique').length,0),records:comparisons.length,exactNeighbourhoods:comparisons.filter(c=>c.routeMatch).length,preservedRecords:comparisons.filter(c=>c.recordPreserved).length,changedCarriersWhenBFlipped:changedCarriers}};
}
