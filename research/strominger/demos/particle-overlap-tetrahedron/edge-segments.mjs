// Thin adapter around the unmodified, version-matched Three.js line addons.
// Opaque edges write depth BEFORE transparent faces are composited over them.
export function createEdgeSegments(THREE,{color=0x000000,width=2,dashed=false}={}){
 if(THREE.REVISION!=='128')throw Error('The vendored r128 line addons require Three.js r128');
 if(!THREE.LineSegments2||!THREE.LineSegmentsGeometry||!THREE.LineMaterial)throw Error('Three.js line addons must be loaded first');
 const geometry=new THREE.LineSegmentsGeometry();geometry.instanceCount=0;
 const material=new THREE.LineMaterial({color,linewidth:width,dashed,dashSize:.016,gapSize:.04,transparent:false,opacity:1,depthTest:true,depthWrite:true,alphaToCoverage:true});
 // r128's dashed flag is not a shader define setter.
 if(dashed)material.defines.USE_DASH='';
 const line=new THREE.LineSegments2(geometry,material);
 line.frustumCulled=false;line.userData.edgeStroke=true;line.userData.dashed=dashed;line.userData.segmentCount=0;
 line.setPairs=pairs=>{
  const next=new THREE.LineSegmentsGeometry();next.instanceCount=pairs.length;
  if(pairs.length)next.setPositions(pairs.flatMap(([a,b])=>[...a,...b]));
  line.geometry.dispose();line.geometry=next;line.userData.segmentCount=pairs.length;
  if(dashed&&pairs.length)line.computeLineDistances();
 };
 line.setResolution=(width,height)=>material.resolution.set(Math.max(1,width),Math.max(1,height));
 return line;
}
