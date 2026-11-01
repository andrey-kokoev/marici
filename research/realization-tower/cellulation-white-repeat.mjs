import {packCellulation} from './cellulation-geometry.mjs';
export const whiteRepeatCount=5;
export const whiteRepeatStages=Object.freeze([{step:13,duration:1000},{step:14,duration:2650},{step:15,duration:2650},{step:16,duration:3300},{step:17,duration:2000}]);
export const whiteRepeatDuration=whiteRepeatStages.reduce((sum,s)=>sum+s.duration,0);
export function whiteRepeatAt(elapsed){
 const total=whiteRepeatCount*whiteRepeatDuration,t=Math.max(0,Math.min(total,elapsed)),index=Math.min(whiteRepeatCount-1,Math.floor(t/whiteRepeatDuration));
 let local=t-index*whiteRepeatDuration,stage=0;
 while(stage<whiteRepeatStages.length-1&&local>=whiteRepeatStages[stage].duration){local-=whiteRepeatStages[stage].duration;stage++;}
 return {index,stage,step:whiteRepeatStages[stage].step,localElapsed:t===total?Infinity:local,completed:Math.min(whiteRepeatCount,Math.floor(t/whiteRepeatDuration)),active:t<total,reusedStep12:true};
}
export function buildWhiteRepeat(templates,index,cellSize){
 const delta=[0,index+1,-index-1],prefix=`white-repeat:${index+1}:`,lattice=p=>p.map((x,i)=>x+delta[i]),point=p=>p.map((x,i)=>x+delta[i]*cellSize/Math.SQRT2),face=f=>f.map(point);
 const arrow=a=>({...a,from:point(a.from),to:point(a.to),...(a.fromLattice?{fromLattice:lattice(a.fromLattice),toLattice:lattice(a.toLattice)}:{})});
 let previous={...packCellulation([],'cellulation-step'),step:12,cellSize,retained:true};const stages=[];
 for(const template of templates){
  const cells=template.step===17?[template.cells.at(-1)].map(c=>({...c,id:prefix+c.id,vertices:face(c.vertices),faces:c.faces.map(face)})):[];
  const model={...packCellulation(cells,'cellulation-step'),step:template.step,cellSize,anchorPrefix:prefix,previous};
  if(template.directedArrow)model.directedArrow=arrow(template.directedArrow);
  if(template.triangleClosure){const c=template.triangleClosure;model.triangleClosure={...c,latticeFace:c.latticeFace.map(lattice),face:face(c.face),arrows:c.arrows.map(arrow)};}
  if(template.sequentialFaces)model.sequentialFaces=template.sequentialFaces.map(c=>({...c,latticeFace:c.latticeFace.map(lattice),arrow:arrow(c.arrow),faces:c.faces.map(face)}));
  if(template.solidClosure){const c=template.solidClosure;model.solidClosure={...c,arrow:arrow(c.arrow),faces:c.faces.map(face),filledVertices:c.filledVertices.map(point),latticeFaces:c.latticeFaces.map(f=>f.map(lattice)),filledLatticeVertices:c.filledLatticeVertices.map(lattice),latticeRectangle:c.latticeRectangle.map(lattice)};}
  stages.push(model);previous=model;
 }
 return {delta,stages};
}
