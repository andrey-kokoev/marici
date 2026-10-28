import {worldPoint} from './normal-ray-model.mjs';
import {cellDualGraph} from './cell-dual-graph.mjs';
const pointKey=p=>p.map(x=>x.toFixed(8)).join(',');
const faceKey=f=>f.map(pointKey).sort().join('|');
// Quotient only for interface incidence: retain both native cell representatives.
export function analyzeSeamLattice(occurrences){
 const graph=cellDualGraph(occurrences),byId=new Map(occurrences.map(b=>[b.id,b]));
 const pairs=graph.links.filter(e=>byId.get(e.from).copy!==byId.get(e.to).copy).map((e,i)=>{
  const a=byId.get(e.from),b=byId.get(e.to),keys=new Set(b.faces.map(faceKey)),face=a.faces.find(f=>keys.has(faceKey(f)));
  if(!face)throw Error('Missing shared seam face');
  return {id:i,cells:[e.from,e.to],face};
 });
 const pairOf=new Map(pairs.flatMap(p=>p.cells.map(id=>[id,p.id]))),adj=new Map(pairs.map(p=>[p.id,new Set()]));
 for(const e of graph.links){const a=pairOf.get(e.from),b=pairOf.get(e.to);if(a!==undefined&&b!==undefined&&a!==b){adj.get(a).add(b);adj.get(b).add(a);}}
 const stars=new Map();for(const p of pairs)for(const v of p.face){const k=pointKey(v);if(!stars.has(k))stars.set(k,{point:v,pairs:[]});stars.get(k).pairs.push(p.id);}
 const cycles=[];
 for(const star of stars.values()){
  if(star.pairs.length!==6)continue;
  const ids=new Set(star.pairs),start=Math.min(...ids),order=[start];let previous=null,current=start;
  while(order.length<6){const next=[...adj.get(current)].filter(id=>ids.has(id)&&id!==previous&&!order.includes(id)).sort((a,b)=>a-b)[0];if(next===undefined)break;order.push(next);previous=current;current=next;}
  if(order.length!==6||!adj.get(order[5]).has(start))throw Error('Interior seam vertex must have a six-cycle');
  const sub=(a,b)=>a.map((v,i)=>v-b[i]),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0);
  const ref=pairs[0].face.map(worldPoint),normal=cross(sub(ref[1],ref[0]),sub(ref[2],ref[0])),center=worldPoint(star.point);
  const centers=order.map(id=>worldPoint(pairs[id].face[0].map((_,i)=>pairs[id].face.reduce((s,v)=>s+v[i]/3,0))));
  const orientation=centers.reduce((s,p,i)=>s+dot(normal,cross(sub(p,center),sub(centers[(i+1)%6],center))),0);
  if(orientation<0)order.reverse();
  const lifts=['original','clone'].map(copy=>order.map(id=>pairs[id].cells.find(cell=>byId.get(cell).copy===copy)));
  cycles.push({id:cycles.length,point:star.point,pairs:order,lifts});
 }
 const overlaps=[];for(let i=0;i<cycles.length;i++)for(let j=i+1;j<cycles.length;j++){
  const common=cycles[i].pairs.filter(id=>cycles[j].pairs.includes(id));if(common.length)overlaps.push({cycles:[i,j],sharedPairs:common});
 }
 return {pairs,cycles,overlaps,cellIds:[...pairOf.keys()],linkCount:[...adj.values()].reduce((n,s)=>n+s.size,0)/2};
}
