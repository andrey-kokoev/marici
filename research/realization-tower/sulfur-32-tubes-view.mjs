import {singleOctahedralEnvelope} from './single-octahedral-process.mjs';
import {subtractTubesJunction} from './sulfur-32-junction-cut.mjs';
const key=p=>p.map(x=>x.toFixed(9)).join(',');
const centre=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i]/vs.length,0));
const distance2=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);

// Presentation-only removal of the six N cells owning the carrier's tips.
export function removeSulfurTubesTips(process){
 const orderedTips=singleOctahedralEnvelope(1).map(key),tips=new Set(orderedTips);
 const removed=process.retainedBodies.filter(c=>c.role==='neutron'&&c.vertices.some(v=>tips.has(key(v))));
 if(removed.length!==6)throw Error('Expected six N tip cells');
 const removedPE=process.retainedBodies.filter(c=>['proton','electron'].includes(c.role));
 const hidden=[...removed,...removedPE],ids=new Set(hidden.map(c=>c.id)),faceCentres=new Set(hidden.flatMap(c=>c.faces.map(f=>key(centre(f)))));
 const tubesCutPrisms=removed.flatMap(cell=>{
  const tip=cell.vertices.find(v=>tips.has(key(v)));
  const opposite=cell.vertices.reduce((a,b)=>distance2(tip,a)>distance2(tip,b)?a:b);
  const opening=cell.vertices.filter(v=>v!==tip&&v!==opposite).sort((a,b)=>key(a).localeCompare(key(b)));
  // Each pair spans one native vertex layer, stacked inward without end caps.
  const origin=centre(opening),inward=opposite.map((x,i)=>x-origin[i]);
  return [0,1].map(layer=>{
  const rectangle=opening.map(p=>p.map((x,i)=>x+layer*inward[i]));
  const first=rectangle[0],across=rectangle.reduce((a,b)=>distance2(first,a)>distance2(first,b)?a:b);
  const alternate=(orderedTips.indexOf(key(tip))+layer)%2===1;
  const [start,end]=alternate?rectangle.filter(v=>v!==first&&v!==across):[first,across];
  const other=rectangle.filter(v=>v!==start&&v!==end),fronts=[[start,other[0],end],[end,other[1],start]];
  const prisms=fronts.map(front=>{
   const back=front.map(p=>p.map((x,i)=>x+inward[i]));
   return {front,back,walls:front.map((p,i)=>[p,front[(i+1)%3],back[(i+1)%3],back[i]])};
  });
  // The wide rectangular divider is shared, not drawn twice. Neither end is capped.
  const walls=[...new Map(prisms.flatMap(p=>p.walls).map(w=>[w.map(key).sort().join('|'),w])).values()];
  return {cell:cell.id,layer,rectangle,inward,prisms,uncutWalls:walls,walls:walls.flatMap(subtractTubesJunction),alternate,tipIndex:orderedTips.indexOf(key(tip)),color:0xffffff};
  });
 });
 return {...process,tubesCutPrisms,
  retainedBodies:process.retainedBodies.filter(c=>!ids.has(c.id)).map(c=>({...c,faces:c.faces.flatMap(subtractTubesJunction)})),
  presentationLabels:(process.presentationLabels??[]).filter(l=>!ids.has(l.cell)&&!tips.has(key(l.point))),
  interfaceGuides:(process.interfaceGuides??[]).filter(g=>!g.points.some(p=>faceCentres.has(key(p)))),
  nativeWiringGraph:{...process.nativeWiringGraph,nodes:process.nativeWiringGraph.nodes.filter(n=>!ids.has(n.id)),links:process.nativeWiringGraph.links.filter(l=>!ids.has(l.from)&&!ids.has(l.to))},
  tubesViewAudit:{removedTipCells:removed.map(c=>c.id),removedPECells:removedPE.map(c=>c.id),remainingCells:process.retainedBodies.length-ids.size,prismPairs:tubesCutPrisms.length,prisms:tubesCutPrisms.length*2,sideWalls:tubesCutPrisms.reduce((n,p)=>n+p.walls.length,0),endCaps:0,depthLayers:2,junctionCut:'pairwise-and-triple-overlaps',junctionCutPlanes:12,junctionCutVolumes:3}
 };
}
