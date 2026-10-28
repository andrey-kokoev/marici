import * as T from 'three';
import {worldPoint} from '../../research/realization-tower/normal-ray-model.mjs';

// Cache CPU arrays, not disposable GPU resources. Rebuilding a scene makes
// fresh geometries/materials while reusing the immutable packed mesh data.
const cache=new WeakMap(),sides=6,pitch=.2;
function pack(tubes){
 const vertices=tubes.reduce((n,t)=>n+t.points.length*(sides+1),0),triangles=tubes.reduce((n,t)=>n+(t.points.length-1)*sides*2,0);
 const position=new Float32Array(vertices*3),normal=new Float32Array(vertices*3),uv=new Float32Array(vertices*2),index=new Uint32Array(triangles*3);
 let vertex=0,ix=0;
 for(const tube of tubes){
  const points=tube.points.map(p=>new T.Vector3(...worldPoint(p))),base=vertex,axis=points.at(-1).clone().sub(points[0]).normalize(),reference=Math.abs(axis.z)>.9?new T.Vector3(0,1,0):new T.Vector3(0,0,1);
  let distance=0;
  for(let r=0;r<points.length;r++){
   if(r)distance+=points[r].distanceTo(points[r-1]);
   const tangent=points[Math.min(r+1,points.length-1)].clone().sub(points[Math.max(0,r-1)]).normalize(),a=new T.Vector3().crossVectors(tangent,reference).normalize(),b=new T.Vector3().crossVectors(tangent,a);
   for(let j=0;j<=sides;j++,vertex++){
    const angle=j/sides*Math.PI*2,n=a.clone().multiplyScalar(Math.cos(angle)).addScaledVector(b,Math.sin(angle)),p=points[r].clone().addScaledVector(n,tube.radius);
    p.toArray(position,vertex*3);n.toArray(normal,vertex*3);uv[vertex*2]=distance/pitch;uv[vertex*2+1]=j/sides;
   }
   if(r)for(let j=0;j<sides;j++){
    const a=base+(r-1)*(sides+1)+j,b=a+sides+1;
    index.set([a,a+1,b,b,a+1,b+1],ix);ix+=6;
   }
  }
 }
 return {position,normal,uv,index,triangles};
}
function packedModel(model){
 let data=cache.get(model);if(data)return {data,cacheHit:true};
 const tubes=model.styles.map(()=>[]);
 if(model.renderPaths){for(const path of model.renderPaths)tubes[path.family].push(path);}else{
 for(const edge of model.edges)edge.families.forEach((family,index)=>{
  const lane=index-(edge.families.length-1)/2;
  // The lane centreline has only two bends. Sample the exact taper breakpoints
  // instead of subdividing each straight span into many redundant tube rings.
  const points=[0,.125,.875,1].map(t=>edge.guide[0].map((x,j)=>x+t*(edge.guide[1][j]-x)+.055*lane*Math.min(1,t*8,(1-t)*8)*edge.side[j]));
  tubes[family].push({points,radius:.014});
 });
 for(const strand of model.strands){tubes[strand.family].push({points:strand.incomingPoints,radius:.0075},{points:strand.outgoingPoints,radius:.0075});}
 }
 data=tubes.map(pack);cache.set(model,data);return {data,cacheHit:false};
}
// Four draw calls; each lane represents the same retained slot-wire bundle.
export function createDenseOctWiring(model){
 const group=new T.Group(),{data,cacheHit}=packedModel(model);
 for(let family=0;family<model.styles.length;family++){
  const style=model.styles[family],material=new T.MeshBasicMaterial({color:style.colors[0],depthTest:true,depthWrite:true});
  if(style.colors.length===2||style.dashed){
   material.onBeforeCompile=shader=>{
    shader.uniforms.stripeA={value:new T.Color(style.colors[0])};shader.uniforms.stripeB={value:new T.Color(style.colors[1]??style.colors[0])};
    shader.vertexShader='varying vec2 strandUv;\n'+shader.vertexShader.replace('#include <begin_vertex>','#include <begin_vertex>\nstrandUv=uv;');
    shader.fragmentShader='varying vec2 strandUv;\nuniform vec3 stripeA;\nuniform vec3 stripeB;\n'+shader.fragmentShader.replace('#include <color_fragment>','#include <color_fragment>\ndiffuseColor.rgb=mix(stripeA,stripeB,step(.5,fract(strandUv.x-strandUv.y)));');
   };
   if(style.dashed){const stripes=material.onBeforeCompile;material.onBeforeCompile=shader=>{stripes(shader);shader.fragmentShader=shader.fragmentShader.replace('#include <color_fragment>','#include <color_fragment>\nif(fract(strandUv.x)>.55) discard;');};}
   material.customProgramCacheKey=()=>style.dashed?'coherence-seam-dashes-v1':'dense-oct-family-stripes-v1';
  }
  const packed=data[family],geometry=new T.BufferGeometry();
  geometry.setAttribute('position',new T.BufferAttribute(packed.position,3));geometry.setAttribute('normal',new T.BufferAttribute(packed.normal,3));geometry.setAttribute('uv',new T.BufferAttribute(packed.uv,2));geometry.setIndex(new T.BufferAttribute(packed.index,1));
  const mesh=new T.Mesh(geometry,material);mesh.userData={denseWiring:true,family,label:style.label,edgeIds:model.renderPaths?model.renderPaths.filter(p=>p.family===family).map(p=>p.id):model.edges.filter(e=>e.families.includes(family)).map(e=>e.id),retainedStrandIds:model.renderPaths?[...new Set(model.renderPaths.filter(p=>p.family===family).flatMap(p=>p.wireIds))]:model.strands.filter(s=>s.family===family).map(s=>s.id)};mesh.layers.set(0);mesh.renderOrder=1;group.add(mesh);
 }
 group.userData.audit={nativeEdges:model.edges?.length,renderedColourLanes:model.renderPaths?.length??model.edges.reduce((n,e)=>n+e.families.length,0),internalChannels:model.renderPaths?.filter(p=>p.kind==='N-interior').length,retainedFibres:model.input.length,retainedSlotWires:model.strands.length,triangles:data.reduce((n,d)=>n+d.triangles,0),meshDataCacheHit:cacheHit};return group;
}
