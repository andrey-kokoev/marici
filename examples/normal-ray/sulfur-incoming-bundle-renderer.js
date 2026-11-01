import * as T from 'three';
import {worldPoint as nativeWorldPoint} from '../../research/realization-tower/normal-ray-model.mjs';
export function createSulfurIncomingBundle(model){
 const worldPoint=model.coordinateSpace==='world3'?(p=>p):nativeWorldPoint;
 const group=new T.Group();
 for(const strand of model.strands){
  const trunk=(strand.branchStemPoints??strand.points).map(p=>new T.Vector3(...worldPoint(p))),trunkLength=trunk.slice(1).reduce((s,p,i)=>s+p.distanceTo(trunk[i]),0);
  const paths=[{points:strand.points,offset:0},...(strand.branches??[]).map(b=>({...b,offset:trunkLength+(b.leadIn?new T.Vector3(...worldPoint(b.leadIn[0])).distanceTo(new T.Vector3(...worldPoint(b.leadIn.at(-1)))):0)}))];
  for(const path of paths){
  const points=path.points.map(p=>new T.Vector3(...worldPoint(p)));
  const curve=new T.CurvePath();
  for(let i=1;i<points.length;i++)curve.add(new T.LineCurve3(points[i-1],points[i]));
  const geometry=new T.TubeGeometry(curve,Math.max(192,Math.ceil(points.length*(model.tubeSegmentsPerPoint??3))),model.tubeRadius??.024,model.radialSegments??16,false);
  // Wiring overlay keeps all four edge guides visible on the unchanged shape.
  const material=new T.MeshBasicMaterial({color:strand.colors[0],depthTest:false,depthWrite:false});
  if(strand.colors.length===2){
   // Preserve equal-pitch spiral colour bands; the wire paths themselves are straight segments.
   const reference=model.stripeReferencePoints??strand.incomingPoints;
   const incomingCurve=new T.LineCurve3(new T.Vector3(...worldPoint(reference[0])),new T.Vector3(...worldPoint(reference.at(-1))));
   const pitch=incomingCurve.getLength()/6,turns=curve.getLength()/pitch,offset=path.offset/pitch;
   material.userData.spiral={turns,offset,incomingTurns:6,pitch,dutyCycle:.5,colors:[...strand.colors]};
   material.onBeforeCompile=shader=>{
    shader.uniforms.spiralA={value:new T.Color(strand.colors[0])};
    shader.uniforms.spiralB={value:new T.Color(strand.colors[1])};
    shader.uniforms.spiralTurns={value:turns};
    shader.uniforms.spiralOffset={value:offset};
    shader.vertexShader='varying vec2 vSpiralUv;\n'+shader.vertexShader.replace('#include <begin_vertex>','#include <begin_vertex>\nvSpiralUv = uv;');
    shader.fragmentShader='varying vec2 vSpiralUv;\nuniform vec3 spiralA;\nuniform vec3 spiralB;\nuniform float spiralTurns;\nuniform float spiralOffset;\n'+shader.fragmentShader.replace('#include <color_fragment>','#include <color_fragment>\nfloat spiralPhase = fract(vSpiralUv.x * spiralTurns + spiralOffset - vSpiralUv.y);\ndiffuseColor.rgb = mix(spiralA, spiralB, step(0.5, spiralPhase));');
   };
   material.customProgramCacheKey=()=> 'sulfur-incoming-equal-pitch-spiral-v2';
  }
  const mesh=new T.Mesh(geometry,material);
  mesh.userData.incomingStrand=strand.id;mesh.userData.polarities=strand.polarities;mesh.userData.branchCell=path.cell??null;mesh.userData.branchStage=path.stage??0;mesh.layers.set(1);mesh.renderOrder=15;group.add(mesh);
  }
 }
 return group;
}
