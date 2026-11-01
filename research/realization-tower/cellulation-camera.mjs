// Vertex (0,0,0) points upward from the centroid of the FCC seed tetrahedron.
// Look perpendicular to that normal: it is screen-vertical without foreshortening.
export function cellulationResetPose(step=1,cellSize=1,frustum=[-2,2,2,-2]){
 const up=[-1,-1,-1].map(x=>x/Math.sqrt(3));
 const offset=[1,1,-2].map(x=>10*x/Math.sqrt(6));
 const target=step===0?[0,0,0]:[1,1,1].map(x=>x*cellSize/(2*Math.SQRT2));
 if(step!==0){
  // Put the seed centroid 28% across and 28% down the viewport, without
  // changing orientation or zoom. Growth proceeds screen-right and downward.
  const [left,right,top,bottom]=frustum,rightAxis=[1/Math.SQRT2,-1/Math.SQRT2,0];
  const dx=-(left+.28*(right-left)),dy=-(bottom+.72*(top-bottom));
  for(let i=0;i<3;i++)target[i]+=rightAxis[i]*dx+up[i]*dy;
 }
 return {up,offset,target,zoom:1};
}
