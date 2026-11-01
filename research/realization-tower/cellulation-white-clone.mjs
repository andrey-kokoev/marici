import {packCellulation} from './cellulation-geometry.mjs';
export const whiteCloneDuration=1800;
export function buildClosingWhiteClone(previous){
 const white=previous.previous,red=previous.blueClone.source,redIds=new Set(red.cells.map(c=>c.id)),lineage=[];
 let cursor=white;while(cursor.step>10){lineage.unshift(cursor);cursor=cursor.previous;}
 // Copy only the white additions, not the red bar underneath their history.
 let source={...packCellulation([],'cellulation-step'),step:10,cellSize:white.cellSize,retained:true};
 for(const model of lineage)source={...model,...packCellulation(model.cells.filter(c=>!redIds.has(c.id)),'cellulation-step'),previous:source};
 const sourceStart=[...previous.blueClone.sourceEnd],sourceEnd=[...previous.blueClone.attachment],attachment=[...previous.blueClone.end],targetEnd=[...previous.blueClone.sourceStart];
 // Point reflection through midpoint(sourceStart, attachment), then +90° about X at attachment.
 const linearTransform=[[-1,0,0],[0,0,1],[0,-1,0]],point=p=>attachment.map((x,i)=>x+linearTransform[i].reduce((sum,v,j)=>sum+v*(p[j]-sourceStart[j]),0));
 const end=point(sourceEnd);if(end.some((x,i)=>Math.abs(x-targetEnd[i])>1e-9))throw Error('The closing white copy does not reach the red start');
 const cells=source.cells.map(c=>({...c,id:`closing-white:${c.id}`,vertices:c.vertices.map(point),faces:c.faces.map(f=>f.map(point))}));
 const lattice=p=>p.map(x=>Math.round(x*Math.SQRT2/white.cellSize)),key=c=>c.vertices.map(p=>lattice(p).join(',')).sort().join('|'),existing=new Set(previous.cells.map(key));
 const sharedCells=cells.filter(c=>existing.has(key(c))),newCells=cells.filter(c=>!existing.has(key(c)));
 const arrows=lineage.flatMap(m=>m.directedArrow?[m.directedArrow]:m.whiteRepeats?m.whiteRepeats.map(c=>c.stages[0].directedArrow):[]).map(a=>({...a,from:point(a.from),to:point(a.to),colour:0xffffff}));
 return {source,sourceStart,sourceEnd,attachment,end,cells,newCells,sharedCells,arrows,linearTransform,reflectionPoint:sourceStart.map((x,i)=>(x+attachment[i])/2),rotationAxis:[1,0,0],rotationDegrees:90,attachmentLattice:lattice(attachment),endLattice:lattice(end)};
}
export function closingWhiteVector(clone,p){return clone.linearTransform.map(row=>row.reduce((sum,x,i)=>sum+x*p[i],0));}
export function closingWhitePoint(clone,p){return closingWhiteVector(clone,p.map((x,i)=>x-clone.sourceStart[i])).map((x,i)=>x+clone.attachment[i]);}
