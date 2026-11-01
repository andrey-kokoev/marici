export const blueCloneColour=0x3080ff;
export const blueCloneDuration=1800;
export function buildBlueClone(previous){
 let source=previous;while(source.step>10)source=source.previous;
 let seed=source;while(!seed.markedVertex)seed=seed.previous;
 const sourceStart=[...seed.markedVertex],sourceEnd=[...source.extensions.at(-1).cycle.first.at(-1).proposedVertex];
 const attachment=[...previous.whiteRepeats.at(-1).stages[0].directedArrow.to];
 const a=sourceEnd.map((x,i)=>x-sourceStart[i]);
 const normal=[1,0,0],axisSigns=[-1,1,1],direction=a.map((x,i)=>x*axisSigns[i]),axisLength=Math.hypot(...direction);
 if(axisLength<1e-10)throw Error('The blue assembly needs a nonzero longitudinal axis');
 const axialNormal=direction.map(x=>x/axisLength);
 // Roll the mirrored copy 180° around its attached longitudinal axis.
 const linearTransform=axialNormal.map((u,i)=>axialNormal.map((v,j)=>{
  const x=(2*u*v-(i===j?1:0))*axisSigns[j];return Math.abs(x-Math.round(x))<1e-12?(Math.round(x)||0):x;
 }));
 const point=p=>attachment.map((x,i)=>x+linearTransform[i].reduce((sum,v,j)=>sum+v*(p[j]-sourceStart[j]),0));
 const rotationDegrees=180;
 const cells=source.cells.map(c=>({...c,id:`blue:${c.id}`,vertices:c.vertices.map(point),faces:c.faces.map(f=>f.map(point))}));
 const arrows=source.cells.filter(c=>c.kind==='tetrahedron').map(c=>({from:point(c.vertices[0]),to:point(c.vertices[2]),colour:blueCloneColour}));
 const lattice=p=>p.map(x=>Math.round(x*Math.SQRT2/source.cellSize));
 const key=c=>c.vertices.map(p=>lattice(p).join(',')).sort().join('|'),existing=new Set(previous.cells.map(key));
 const sharedCells=cells.filter(c=>existing.has(key(c))),newCells=cells.filter(c=>!existing.has(key(c)));
 return {source,sourceStart,sourceEnd,attachment,normal,cells,arrows,end:point(sourceEnd),attachmentLattice:lattice(attachment),endLattice:lattice(point(sourceEnd)),axisSigns,axialNormal,linearTransform,newCells,sharedCells,rotationDegrees,colour:blueCloneColour};
}
export function blueCloneVector(clone,vector){return clone.linearTransform.map(row=>row.reduce((sum,x,i)=>sum+x*vector[i],0));}
export function blueClonePoint(clone,point){return blueCloneVector(clone,point.map((x,i)=>x-clone.sourceStart[i])).map((x,i)=>x+clone.attachment[i]);}
