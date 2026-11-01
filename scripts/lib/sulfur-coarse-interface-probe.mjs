import {buildBranchingSeed} from '../../research/realization-tower/branching-seed.mjs';
import {auditReturnInterface,planeSimilarity} from '../../research/realization-tower/sulfur-coarse-interface.mjs';
import {runNeighbourhoodProbe} from './sulfur-neighbourhood-probe.mjs';
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const equal=(a,b)=>a.every((x,i)=>Math.abs(x-b[i])<1e-9);
const unique=ps=>[...new Map(ps.map(p=>[p.join(','),p])).values()];
function planeDistanceSquared(at,ports,point){
 const [a,b]=ports.map(p=>sub(p,at)),v=sub(point,at),aa=dot(a,a),ab=dot(a,b),bb=dot(b,b),det=aa*bb-ab*ab;
 const u=(bb*dot(v,a)-ab*dot(v,b))/det,w=(aa*dot(v,b)-ab*dot(v,a))/det;
 return v.reduce((s,x,i)=>s+(x-u*a[i]-w*b[i])**2,0);
}
export async function runCoarseInterfaceProbe(){
 const layers=buildBranchingSeed().layers.map(auditReturnInterface),native=await runNeighbourhoodProbe(),alignments=[];
 for(const layer of layers)for(const [index,{query,result}]of native.predicted.entries())for(const swapped of [false,true]){
  const targetPorts=unique(query.arrivals.map(a=>a.previous));if(swapped)targetPorts.reverse();
  const transform=planeSimilarity(layer.target.point,layer.target.incoming.map(e=>e.points[0]),query.at,targetPorts);
  const mappedHeads=layer.target.outgoing.map(e=>transform.map(e.points[1])),expected=result.groups.map(g=>g.head);
  alignments.push({layer:layer.layer,nativeJunction:index,swapped,scaleSquared:transform.scaleSquared,
   targetPorts,mappedHeads,carrierHeadsMatch:mappedHeads.length===expected.length&&mappedHeads.every(p=>expected.some(q=>equal(p,q)))});
 }
 const departures=native.predicted.flatMap(({query,result})=>{
  const ports=unique(query.arrivals.map(a=>a.previous));
  return result.generated.map(g=>({id:g.record.id,distanceSquaredFromInputPlane:planeDistanceSquared(query.at,ports,g.points.at(-1))}));
 });
 return {schema:'sulfur-coarse-interface-probe.v1',layers,alignments,departures,
  summary:{layers:layers.length,unlabelledMetricAlignments:alignments.filter(a=>a.carrierHeadsMatch).length,nativeDepartures:departures.length,
   nativeDeparturesOutsideInputPlane:departures.filter(d=>d.distanceSquaredFromInputPlane>1e-10).length,
   closedLayerChannels:layers.filter(l=>l.closedChannel).length},
  scope:'Coarse directed join/carrier metric compatibility only. Neither port labels nor a full chart transition nor a conserved strand population is inferred.'};
}
