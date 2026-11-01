import {packCellulation} from './cellulation-geometry.mjs';
import {blueClonePoint} from './cellulation-blue-clone.mjs';
export const crossEdgeDuration=6000;
export function crossEdgePoint(c,p){return c.attachment.map((x,i)=>x+c.linearTransform[i].reduce((sum,v,j)=>sum+v*(p[j]-c.sourceStart[j]),0));}
export function crossEdgeVector(c,p){return c.linearTransform.map(row=>row.reduce((sum,v,j)=>sum+v*p[j],0));}
export function buildCrossEdge(previous,remaining=false){
 let cursor=previous;while(!cursor.blueClone)cursor=cursor.previous;
 const blue=cursor.blueClone,terminal=blue.source.extensions.at(-1).cycle.first.at(-1);
 let seed=blue.source;while(seed.step!==6)seed=seed.previous;
 const from=remaining?[...seed.witness.turnMarker.point]:[...terminal.witness.priorTurnMarkers[0].point];
 const to=blueClonePoint(blue,remaining?seed.witness.priorTurnMarkers[0].point:terminal.witness.turnMarker.point),size=previous.cellSize;
 const prefix=remaining?'remaining-complex:':'cross-complex:',axisPrefix=remaining?'remaining-edge:':'cross-edge:';
 const length=Math.hypot(...to.map((x,i)=>x-from[i])),count=Math.round(length/size);
 if(count!==6||Math.abs(length-count*size)>size*1e-7)throw Error('Expected a six-unit cross edge between the existing terminal turns');
 const points=Array.from({length:count+1},(_,i)=>from.map((x,j)=>x+(to[j]-x)*i/count));
 // Reuse the completed whole-cell red-bar construction, shortened to six units.
 const extensions=blue.source.extensions.slice(0,3),source={...blue.source,...packCellulation([...blue.source.previous.cells,...extensions.flatMap(e=>e.cells)],'cellulation-step'),extensions};
 const sourceStart=blue.sourceStart,linearTransform=remaining?[[1,0,0],[0,0,1],[0,1,0]]:[[-1,0,0],[0,0,1],[0,-1,0]];
 const map=p=>from.map((x,i)=>x+linearTransform[i].reduce((sum,v,j)=>sum+v*(p[j]-sourceStart[j]),0));
 const cells=source.cells.map(c=>({...c,id:`${prefix}${c.id}`,vertices:c.vertices.map(map),faces:c.faces.map(f=>f.map(map))}));
 const key=c=>c.vertices.map(p=>p.map(x=>Math.round(x*Math.SQRT2/size)).join(',')).sort().join('|'),existing=new Set(previous.cells.map(key));
 const newCells=cells.filter(c=>!existing.has(key(c)));
 return {prefix,axisPrefix,source,sourceStart,attachment:from,linearTransform,cells,newCells,points,latticePoints:points.map(p=>p.map(x=>Math.round(x*Math.SQRT2/size))),arrows:points.slice(1).map((to,i)=>({from:points[i],to,colour:0xffffff}))};
}
