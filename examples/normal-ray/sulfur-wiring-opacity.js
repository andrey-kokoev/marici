// Update existing materials without rebuilding geometry or changing wire records.
export function setSulfurWiringOpacity(root,{wireOpacity=1,tubeOpacity=.14}={}){
 const wire=Math.max(0,Math.min(1,wireOpacity)),tube=Math.max(0,Math.min(1,tubeOpacity));
 root.traverse(o=>{
  if(!o.material)return;
  const scale=o.userData.nTubeOpacityScale;
  const opacity=o.userData.incomingStrand||o.userData.blueCompletion||o.userData.denseWiring?wire:scale!==undefined?Math.min(1,tube*scale):null;
  if(opacity===null)return;
  if(o.userData.denseWiring)o.visible=opacity>0;
  for(const material of Array.isArray(o.material)?o.material:[o.material]){
   material.opacity=opacity;
   if(o.userData.carvedWire||o.userData.denseWiring)material.depthWrite=opacity===1;
   const transparent=o.userData.denseWiring?opacity<1:true;
   if(material.transparent!==transparent){material.transparent=transparent;material.needsUpdate=true;}
  }
 });
 return {wireOpacity:wire,tubeOpacity:tube};
}
