import * as T from 'three';
import {createSeedSidePair} from './branching-seed-side-pair-renderer.js';
const colors={white:0xf3f6ff,red:0xff4545,blue:0x438bff};
export function createBranchingSeed(model,state={}){
 const visibleLayers=model.layers.map((layer,index)=>({layer,index})).filter(({index})=>(state.processId==='beryllium-9'&&state.be9View==='3d-assembly')||model.layers.length===1||state.seedVisibleLayers?.[index]!==false);
 const group=new T.Group(),up=new T.Vector3(0,1,0);
 const arrowGeometry=new T.ConeGeometry(.13,.24,12);
 const materials=Object.fromEntries(Object.entries(colors).map(([role,color])=>[role,new T.MeshBasicMaterial({color})]));
 for(const edge of visibleLayers.flatMap(({layer})=>layer.edges)){
  for(let i=1;i<edge.points.length;i++){
   const a=new T.Vector3(...edge.points[i-1]),b=new T.Vector3(...edge.points[i]),delta=b.clone().sub(a);
   const mesh=new T.Mesh(new T.CylinderGeometry(.035,.035,delta.length(),10),materials[edge.role]);
   mesh.position.copy(a).add(b).multiplyScalar(.5);mesh.quaternion.setFromUnitVectors(up,delta.normalize());mesh.userData.seedEdge=edge.id;group.add(mesh);
   if(edge.role==='white'&&i===edge.points.length-1){
    const arrow=new T.Mesh(arrowGeometry,materials.white);
    arrow.position.copy(edge.points.length===3?a:mesh.position);arrow.quaternion.copy(mesh.quaternion);
    arrow.userData.whiteDirection={edge:edge.id,from:edge.from,to:edge.to};group.add(arrow);
   }
  }
 }
 const joints=new T.SphereGeometry(.04,10,6);
 for(const node of visibleLayers.flatMap(({layer})=>layer.nodes)){
  const sphere=new T.Mesh(joints,materials.white);sphere.position.fromArray(node.point);
  if(model.roots.includes(node.id))sphere.scale.setScalar(2);
  group.add(sphere);
 }
 for(const {point,layers} of model.centerMarkers){
  if(!visibleLayers.some(v=>layers.includes(v.index)))continue;
  const center=new T.Mesh(new T.SphereGeometry(.11,12,8),new T.MeshBasicMaterial({color:0xffc866}));
  center.position.fromArray(point);center.userData.reflectionCenter=true;group.add(center);
 }
 const visibleIndices=new Set(visibleLayers.map(v=>v.index));
 const visiblePairs=state.seedPairsByLayer===false?[]:model.sidePairs.filter(p=>visibleIndices.has(p.layerIndex));
 for(const pair of visiblePairs)group.add(createSeedSidePair(pair));
 group.userData.audit={...model.audit,sidePairs:visiblePairs.length,sidePairsPerLayer:model.sidePairs.length?model.audit.depth:0,combinedDisplay:'separate route-comparison panel',sidePairHeight:model.sidePairs[0]?.totalHeight??0,sidePairSleevesPerLayer:model.sidePairs[0]?.bands.filter(b=>b.role==='white').length??0,visibleLayers:visibleLayers.map(v=>v.index+1),whiteArrows:group.children.filter(o=>o.userData.whiteDirection).length,whiteDirection:model.layers.length===1?'away from the original root':'away from each layer root; reflected arrows reversed; copied pair mirrored perpendicular to the central white arrow; lower four inverted in their own planes'};return group;
}
