// Pure screen-space layout. Inputs are projected anchors and projected owner
// centres in CSS pixels; this module knows nothing about vertex indices or poses.
export const vertexLabelMetrics=Object.freeze({clearance:36,height:40,minWidth:40,margin:6,gap:4});
export function layoutVertexLabels(anchors,{width,height}){
 const m=vertexLabelMetrics,placed=[],clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
 return anchors.map(anchor=>{
  if(!anchor.visible)return {...anchor,x:anchor.anchorX,y:anchor.anchorY};
  const boxWidth=Math.max(m.minWidth,(anchor.text?.length??2)*10+14),boxHeight=m.height;
  const dx=anchor.anchorX-anchor.centerX,dy=anchor.anchorY-anchor.centerY,angle=Math.hypot(dx,dy)>1e-6?Math.atan2(dy,dx):-Math.PI/2;
  let best;
  for(const radius of [m.clearance,60,84,108])for(const turn of [0,-Math.PI/6,Math.PI/6,-Math.PI/3,Math.PI/3,-Math.PI/2,Math.PI/2,Math.PI]){
   const x=clamp(anchor.anchorX+radius*Math.cos(angle+turn),boxWidth/2+m.margin,width-boxWidth/2-m.margin),y=clamp(anchor.anchorY+radius*Math.sin(angle+turn),boxHeight/2+m.margin,height-boxHeight/2-m.margin);
   const overlap=placed.reduce((s,p)=>s+Math.max(0,(boxWidth+p.boxWidth)/2+m.gap-Math.abs(x-p.x))*Math.max(0,(boxHeight+p.boxHeight)/2+m.gap-Math.abs(y-p.y)),0);
   const score=overlap*1e6+(radius-m.clearance)**2+turn**2*300;
   if(!best||score<best.score)best={x,y,boxWidth,boxHeight,score};
  }
  placed.push(best);
  const distance=Math.hypot(best.x-anchor.anchorX,best.y-anchor.anchorY),stop=Math.min(20,distance);
  return {...anchor,x:best.x,y:best.y,leaderX:best.x-(best.x-anchor.anchorX)*stop/(distance||1),leaderY:best.y-(best.y-anchor.anchorY)*stop/(distance||1)};
 });
}
