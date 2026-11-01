import {foldBeryllium9Faces} from './beryllium-9-face-fold.mjs';
import {growSimplex,calculateSeedStrands} from './hex-edge-grid-model.generated.mjs';
import {buildSeedSidePair} from './branching-seed-side-pair.mjs';
// Same depth convention as the hex experiment: one white edge followed by
// one branching layer. Integer coordinates deduplicate the actual honeycomb.
export function buildBranchingSeed({seedLayerGap=2,seedPairsByLayer=true,processId,be9View,be9AssemblyFold=false,be9AssemblySides=false,seedDepth=processId==='beryllium-9'&&be9View==='3d-assembly'?8:['beryllium-8','beryllium-9'].includes(processId)?4:8}={}){
 if(![4,8].includes(seedDepth))throw Error('Supported seed depths are 4 and 8');
 if(!Number.isFinite(seedLayerGap)||seedLayerGap<0||seedLayerGap>6)throw Error('Layer gap must be between 0 and 6');
 be9AssemblyFold=be9AssemblyFold||be9AssemblySides;
 const depth=seedDepth,seed=growSimplex(2,0,depth,0);
 // Rotate the honeycomb so its root points down and its white edges are vertical.
 // Colour directions are unoriented edge families, measured clockwise from up:
 // white 0°, blue 120°, red 240°.
 const assembly=processId==='beryllium-9'&&be9View==='3d-assembly';
 const hinge=[-7*Math.sqrt(3)/16,-5.75,21/16],hingeAxis=[Math.sqrt(3)/2,0,.5];
 const fold=p=>{
  const v=p.map((x,i)=>x-hinge[i]),[a,b,c]=hingeAxis,[x,y,z]=v,dot=a*x+b*y+c*z,cross=[b*z-c*y,c*x-a*z,a*y-b*x];
  return v.map((value,i)=>hinge[i]+.5*value+Math.sqrt(3)/2*cross[i]+.5*dot*hingeAxis[i]);
 };
 const project=(v,applyFold=true)=>{
  if(!assembly)return [Math.sqrt(3)*v.y/2,-(v.x-2)/2,0];
  // Retained branch counts give a consistent embedding even at merged nodes.
  // Keep the white/red plane fixed; turn the blue half-plane 60° from flat,
  // giving a 120° opening about the common white direction.
  const branches=Math.floor((v.x-2)/3),red=(branches-v.y)/2,blue=(branches+v.y)/2;
  const point=[Math.sqrt(3)/2*(-red+blue/2),-(v.x-2)/2,3*blue/4];
  return applyFold&&be9AssemblyFold&&v.x>13.5?fold(point):point;
 };
 let nodes=[...seed.vertices.values()].map(v=>({id:v.id,point:project(v),lattice:[v.x,v.y]}));
 let edges=[...seed.edges.values()].map(e=>{
  let a=seed.vertices.get(e.a),b=seed.vertices.get(e.b);
  if(a.x>b.x)[a,b]=[b,a];
  const role=a.y===b.y?'white':b.y>a.y?'blue':'red';
  const points=[project(a),project(b)];
  if(assembly&&be9AssemblyFold&&role!=='white'&&a.x===13){
   const start=project(a,false),end=project(b,false);
   points.splice(1,0,start.map((x,i)=>(x+end[i])/2));
  }
  return {id:e.id,from:a.id,to:b.id,role,points};
 });
 const routes=calculateSeedStrands(seed).map(s=>({id:s.id,edges:s.seedEdges,output:s.seedVertices.at(-1).id}));
 const root='v(2,0)';
 if(assembly){
  const sideFold=be9AssemblySides?foldBeryllium9Faces(nodes,edges,fold):null;
  if(sideFold){nodes=sideFold.nodes;edges=sideFold.edges;}
  const displayPoints=edges.flatMap(e=>e.points);
  const bounds=[0,1,2].map(i=>[Math.min(...displayPoints.map(p=>p[i]))-.3,Math.max(...displayPoints.map(p=>p[i]))+.3]);
  const envelope=bounds[0].flatMap(x=>bounds[1].flatMap(y=>bounds[2].map(z=>[x,y,z]))),count=role=>edges.filter(e=>e.role===role).length;
  return {nodes,edges,routes,faces:sideFold?.faces??[],root,roots:[root],layers:[{id:'original',nodes,edges,routes,root}],sidePairs:[],centerMarkers:[],reflectionCenters:[],envelope,
   audit:{...sideFold?.audit,assemblyStep:be9AssemblySides?2:be9AssemblyFold?1:0,foldAngle:be9AssemblyFold?60:0,foldBeforeWhiteLayer:5,foldEdgeRoles:['red','blue'],foldLatticeX:13.5,hinge,hingeAxis,depth,edgeLayers:2*depth,paths:routes.length,pathsPerLayer:routes.length,exits:new Set(routes.map(r=>r.output)).size,
    edges:edges.length,nodes:nodes.length,whiteEdges:count('white'),redEdges:count('red'),blueEdges:count('blue'),layers:1,
    dihedralDegrees:120,planar:false,eachLayerPlanar:false,rootRole:edges.find(e=>e.from===root).role,lattice:'honeycomb-connectivity'}};
 }
 const boxCenter=[0,1].map(i=>(Math.min(...nodes.map(n=>n.point[i]))+Math.max(...nodes.map(n=>n.point[i])))/2);
 const centerVertex=nodes.find(n=>n.point[0]===boxCenter[0]&&n.point[1]===boxCenter[1]);
 const centerEdge=edges.find(e=>e.role==='white'&&e.from===centerVertex?.id);
 if(!centerEdge)throw Error('Expected a white edge below the central vertex');
 const center=[0,1].map(i=>(centerEdge.points[0][i]+centerEdge.points[1][i])/2);

 const reflectionCenter=[...center,-seedLayerGap/2];
 const reflect=p=>p.map((x,i)=>2*reflectionCenter[i]-x),cloneId=id=>'clone:'+id;
 const cloneNodes=nodes.map(n=>({...n,id:cloneId(n.id),source:n.id,point:reflect(n.point)}));
 const cloneEdges=edges.map(e=>({...e,id:cloneId(e.id),source:e.id,from:cloneId(e.from),to:cloneId(e.to),points:e.points.map(reflect)}));
 const cloneRoutes=routes.map(r=>({...r,id:cloneId(r.id),source:r.id,edges:r.edges.map(cloneId),output:cloneId(r.output)}));
 const layers=[{id:'original',nodes,edges,routes,root},{id:'reflected',nodes:cloneNodes,edges:cloneEdges,routes:cloneRoutes,root:cloneId(root)}];
 // Reflect the complete pair through the plane perpendicular to the central
 // white arrow at its midpoint, then translate it down by one pair-height.
 const arrow=centerEdge.points[1].map((x,i)=>x-centerEdge.points[0][i]);
 const normal=arrow.map(x=>x/Math.hypot(...arrow)),planePoint=[...center,0];
 const reflectLower=p=>{
  const distance=p.reduce((s,x,i)=>s+(x-planePoint[i])*normal[i],0);
  return p.map((x,i)=>x-2*distance*normal[i]-(i===2?2*seedLayerGap:0));
 };
 const mirroredId=id=>'mirror:'+id;
 layers.push(...layers.map(layer=>({
  id:'mirrored-'+layer.id,source:layer.id,root:mirroredId(layer.root),
  nodes:layer.nodes.map(n=>({...n,id:mirroredId(n.id),source:n.id,point:reflectLower(n.point)})),
  edges:layer.edges.map(e=>({...e,id:mirroredId(e.id),source:e.id,from:mirroredId(e.from),to:mirroredId(e.to),points:e.points.map(reflectLower)})),
  routes:layer.routes.map(r=>({...r,id:mirroredId(r.id),source:r.id,edges:r.edges.map(mirroredId),output:mirroredId(r.output)}))
 })));
 // Clone all four existing layers lower without reversing their Z order.
 // Each new layer is inverted about its own center in its own plane.
 const reflectBlockLower=p=>[2*center[0]-p[0],2*center[1]-p[1],p[2]-4*seedLayerGap];
 const centralId=id=>'central:'+id;
 layers.push(...layers.map(layer=>({
  id:'central-'+layer.id,source:layer.id,root:centralId(layer.root),
  nodes:layer.nodes.map(n=>({...n,id:centralId(n.id),source:n.id,point:reflectBlockLower(n.point)})),
  edges:layer.edges.map(e=>({...e,id:centralId(e.id),source:e.id,from:centralId(e.from),to:centralId(e.to),points:e.points.map(reflectBlockLower)})),
  routes:layer.routes.map(r=>({...r,id:centralId(r.id),source:r.id,edges:r.edges.map(centralId),output:centralId(r.output)}))
 })));
 const centerMarkers=[{point:reflectionCenter,layers:[0,1]},{point:reflectLower(reflectionCenter),layers:[2,3]},
  ...layers.slice(4).map((layer,i)=>({point:[...center,layer.nodes[0].point[2]],layers:[i+4]}))];
 const reflectionCenters=centerMarkers.map(m=>m.point);
 const allNodes=layers.flatMap(l=>l.nodes),allEdges=layers.flatMap(l=>l.edges),allRoutes=layers.flatMap(l=>l.routes);
 const sidePairs=layers.flatMap((layer,index)=>Array.from({length:depth},(_,pairIndex)=>buildSeedSidePair(layer,index,pairIndex)));
 const displayPoints=[...allNodes.map(n=>n.point),...(seedPairsByLayer?sidePairs.flatMap(p=>p.bounds):[])];
 const bounds=[0,1,2].map(i=>[Math.min(...displayPoints.map(p=>p[i]))-.3,Math.max(...displayPoints.map(p=>p[i]))+.3]);
 const envelope=bounds[0].flatMap(x=>bounds[1].flatMap(y=>bounds[2].map(z=>[x,y,z])));
 const count=role=>allEdges.filter(e=>e.role===role).length;
 return {nodes:allNodes,edges:allEdges,routes:allRoutes,root,roots:layers.map(l=>l.root),layers,sidePairs,reflectionCenter,reflectionCenters,centerMarkers,reflect,reflectLower,reflectBlockLower,envelope,audit:{depth,edgeLayers:2*depth,paths:allRoutes.length,pathsPerLayer:routes.length,exits:layers.length*new Set(routes.map(r=>r.output)).size,
  edges:allEdges.length,nodes:allNodes.length,whiteEdges:count('white'),redEdges:count('red'),blueEdges:count('blue'),
  layers:8,blockOperation:'per-layer point reflection',blockDrop:4*seedLayerGap,gap:seedLayerGap,reflectionCenter,reflectionCenters,reflectionCenterEdge:centerEdge.id,pairOperation:'perpendicular reflection',pairReflectionNormal:normal,pairReflectionPoint:planePoint,pairDrop:2*seedLayerGap,layerPlanes:layers.map(l=>l.nodes[0].point[2]),planar:seedLayerGap===0,eachLayerPlanar:true,rootRole:edges.find(e=>e.from===root).role,colourDirections:{white:0,blue:120,red:240},lattice:'honeycomb'}};
}
