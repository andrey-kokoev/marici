import {buildFoldedFibration,foldedFibrationEnvelope} from './fibration-folded-process.mjs';
import {geometricCellLayer} from './cell-fibration-cut.mjs';

export const simplexVertexLabels=['N₁','P','E','N₂'];
const geometry=buildFoldedFibration().geometry;
const pointKey=p=>p.join(','),faceKey=f=>f.map(pointKey).sort().join('|');
const address=body=>[1,2,3,4].map(v=>geometricCellLayer(body,v));
const byId=new Map(geometry.map(body=>[body.id,body]));
const facetCells=new Map();
for(const body of geometry)for(const face of body.faces){
 const key=faceKey(face);if(!facetCells.has(key))facetCells.set(key,[]);facetCells.get(key).push(body.id);
}
const neighbors=new Map(geometry.map(body=>[body.id,[]]));
for(const ids of facetCells.values())if(ids.length===2){neighbors.get(ids[0]).push(ids[1]);neighbors.get(ids[1]).push(ids[0]);}
const roots=foldedFibrationEnvelope.map(point=>{
 const found=geometry.filter(body=>body.kind==='tetrahedron'&&body.vertices.some(v=>pointKey(v)===pointKey(point)));
 if(found.length!==1)throw Error('Expected one corner tetrahedron per simplex vertex');return found[0].id;
});
const routes=roots.map(root=>{
 const previous=new Map([[root,null]]),queue=[root];
 for(let i=0;i<queue.length;i++)for(const next of neighbors.get(queue[i]))if(!previous.has(next)){previous.set(next,queue[i]);queue.push(next);}
 return previous;
});
function trace(previous,target,startVertex){
 if(!previous.has(target))throw Error(`Cell ${target} is disconnected from simplex vertex ${startVertex}`);
 const cells=[];for(let id=target;id!==null;id=previous.get(id))cells.push(id);cells.reverse();
 const steps=[];
 for(let i=1;i<cells.length;i++){
  const from=address(byId.get(cells[i-1])),to=address(byId.get(cells[i]));
  const changed=from.map((x,j)=>to[j]-x).map((d,j)=>({d,j})).filter(x=>x.d!==0);
  if(changed.length!==1||Math.abs(changed[0].d)!==1)throw Error('A facet crossing must change exactly one simplex coordinate by one unit');
  const {d,j}=changed[0];steps.push({vertex:j+1,direction:simplexVertexLabels[j],sign:d>0?'+':'−',from:from.join(''),to:to.join('')});
 }
 return {startVertex,label:simplexVertexLabels[startVertex-1],root:roots[startVertex-1],target,cells,steps,code:steps.map(s=>s.direction+s.sign)};
}
export function simplexMovementPaths(cellId){
 if(!byId.has(cellId))throw Error(`Unknown simplex cell ${cellId}`);
 return routes.map((previous,i)=>trace(previous,cellId,i+1));
}
export function simplexCellPath(fromId,toId){
 if(!byId.has(fromId)||!byId.has(toId))return null;
 const previous=new Map([[fromId,null]]),queue=[fromId];
 for(let i=0;i<queue.length&&!previous.has(toId);i++)for(const next of neighbors.get(queue[i]))if(!previous.has(next)){previous.set(next,queue[i]);queue.push(next);}
 return previous.has(toId)?trace(previous,toId,null):null;
}
export function simplexMovementCellIds(){return geometry.map(body=>body.id);}
