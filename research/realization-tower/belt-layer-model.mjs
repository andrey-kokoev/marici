import {instantiateBlockWiring,instantiateTriangleWiring,instantiateTriangleExchange,instantiateTriangleInterleave,outerPerimeter} from './belt-wiring.mjs';
import {fiberJunctionLaw} from './belt-fiber-junction.mjs';
// Physical order from the first ESD7 toward the second. P/E are transport
// directions, not particle roles. Only explicitly enabled symbolic wiring is built.
export const beltLayerDefinitions=Object.freeze([
 {kind:'tube-ports',rows:['EEEE','EPPE','EPPE','EEEE'],bundleLayout:'central-block-and-three-rim-bundles',rotationDegrees:0},
 {kind:'node-star',rows:['PE','EE'],starSlots:[3,2,1,0],supportRotationDegrees:0,rotationDegrees:0},
 {kind:'bundle-stars',groups:['EEE','EEE','EEE','PPP'],groupLayout:'three-stars',starRotationDegrees:0,bundleSlots:[3,2,1,0],rotationDegrees:0,groupRotationDegrees:180},
 {kind:'bundle-stars',groups:['PPP','PPP','PPP','EEE'],groupLayout:'three-stars',starRotationDegrees:180,bundleSlots:[0,1,2,3],rotationDegrees:0},
 {kind:'node-star',rows:['PP','PE'],starSlots:[0,1,2,3],supportRotationDegrees:180,rotationDegrees:0},
 {kind:'tube-ports',rows:['PPPP','PEEP','PEEP','PPPP'],bundleLayout:'central-block-and-three-rim-bundles',rotationDegrees:180},
].map(d=>Object.freeze({...d,...(d.rows?{rows:Object.freeze(d.rows)}:{}),...(d.groups?{groups:Object.freeze(d.groups)}:{}),...(d.bundleSlots?{bundleSlots:Object.freeze(d.bundleSlots)}:{}),...(d.starSlots?{starSlots:Object.freeze(d.starSlots)}:{})})));
export const beltLayerCount=beltLayerDefinitions.length;
export const transportColors=Object.freeze({P:0x1265a8,E:0xa82664});
const add=(a,b)=>a.map((v,i)=>v+b[i]),mul=(a,s)=>a.map(v=>v*s);

// One centering/spacing rule for every layer; no hidden historical geometry.
// Frame vectors are orthonormal world-space vectors supplied by the parent pair.
export function buildBeltLayers({origin,x,y,normal,spacing=1.05,pitch=.8}){
 if(!(spacing>0&&pitch>0))throw Error('Belt spacing and pitch must be positive');
 const layers=beltLayerDefinitions.map((definition,index)=>{
  const layer=index+1,plane=((beltLayerCount-1)/2-index)*spacing,center=add(origin,mul(normal,plane));
  const angle=definition.rotationDegrees*Math.PI/180,c=Math.cos(angle),s=Math.sin(angle),nodes=[],directionCounts={P:0,E:0};
  function node(direction,u,v,location){
   const local=[c*u-s*v,s*u+c*v],position=add(center,add(mul(x,local[0]),mul(y,local[1]))),slot=nodes.length;
   directionCounts[direction]++;
   nodes.push({id:`belt:layer:${layer}:node:${slot}`,layer,slot,direction,local,position,...location});
  }
  if(definition.kind==='grid'){
   const height=definition.rows.length,width=definition.rows[0].length;
   definition.rows.forEach((row,r)=>[...row].forEach((direction,col)=>node(direction,(col-(width-1)/2)*pitch,((height-1)/2-r)*pitch,{row:r,column:col})));
  }else if(definition.kind==='tube-ports'){
   // Tube-first attachment ports: three majority groups around one return group.
   // Original grid, star and arm addresses remain provenance, not geometry.
   definition.rows.forEach((row,r)=>[...row].forEach((direction,col)=>{
    const central=[1,2].includes(r)&&[1,2].includes(col),rimIndex=outerPerimeter.findIndex(([rr,cc])=>r===rr&&col===cc),group=central?2*(r-1)+col-1:rimIndex%4,arm=central?null:Math.floor(rimIndex/4);
    const tubeSlot=central?3:arm,theta=Math.PI/2+(arm??0)*2*Math.PI/3,radius=central?0:1.25*pitch,cu=radius*Math.cos(theta),cv=radius*Math.sin(theta);
    const du=(group%2-.5)*.35*pitch,dv=(.5-Math.floor(group/2))*.35*pitch;
    const roll=(arm??0)*2*Math.PI/3;
    node(direction,cu+du*Math.cos(roll)-dv*Math.sin(roll),cv+du*Math.sin(roll)+dv*Math.cos(roll),{row:r,column:col,group,arm,starCentre:central,tubeSlot,tubeLane:group});
   }));
  }else if(definition.kind==='node-star'){
   // Keep row/column addresses for symbolic wiring; only presentation moves.
   const minoritySlot=definition.starSlots[3],directions=definition.rows.join('');
   if([...directions].filter(d=>d===directions[minoritySlot]).length!==1)throw Error('Node-star centre must be the minority direction');
   definition.rows.forEach((row,r)=>[...row].forEach((direction,col)=>{
    const slot=r*2+col,arm=definition.starSlots.indexOf(slot),theta=Math.PI/2+arm*2*Math.PI/3+definition.supportRotationDegrees*Math.PI/180,radius=slot===minoritySlot?0:.4*pitch;
    node(direction,radius*Math.cos(theta),radius*Math.sin(theta),{row:r,column:col});
   }));
  }else if(definition.kind==='bundle-stars'){
   // Retain symbolic (group,vertex) identities while regrouping by vertex:
   // each star receives one minority centre and one node from each majority group.
   const minority=definition.groups.findIndex(p=>definition.groups.filter(q=>q===p).length===1),majority=definition.groups.map((_,i)=>i).filter(i=>i!==minority);
   if(minority<0||majority.length!==3)throw Error('Expected one minority and three majority bundles');
   definition.groups.forEach((pattern,group)=>[...pattern].forEach((direction,vertex)=>{
    const theta=Math.PI/2+vertex*2*Math.PI/3+(definition.groupRotationDegrees??0)*Math.PI/180,cu=1.5*pitch*Math.cos(theta),cv=1.5*pitch*Math.sin(theta),central=group===minority,arm=central?null:majority.indexOf(group);
    const satelliteAngle=Math.PI/2+(arm??0)*2*Math.PI/3+definition.starRotationDegrees*Math.PI/180,radius=central?0:.4*pitch;
    node(direction,cu+radius*Math.cos(satelliteAngle),cv+radius*Math.sin(satelliteAngle),{group,vertex,star:vertex,arm,starCentre:central});
   }));
  }else throw Error(`Unsupported belt geometry: ${definition.kind}`);
  const depth=Math.min(index,beltLayerCount-1-index)+1,primed=index>=beltLayerCount/2;
  return {...definition,layer,label:`L${depth}${primed?'′':''}`,depth,side:primed?'second':'first',displayOrder:2*(depth-1)+(primed?1:0),plane,center,directionCounts,nodes,nodeCount:nodes.length,wiring:null};
 });
 const wiring=[instantiateBlockWiring(layers[0],layers[1]),instantiateBlockWiring(layers[5],layers[4]),instantiateTriangleWiring(layers[1],layers[2],'P'),instantiateTriangleWiring(layers[4],layers[3],'E'),instantiateTriangleInterleave(layers[1],layers[2],'E'),instantiateTriangleInterleave(layers[4],layers[3],'P'),instantiateTriangleExchange(layers[2],layers[3],'E'),instantiateTriangleExchange(layers[3],layers[2],'P')];
 for(const layer of layers)layer.wiring=[...new Set(wiring.filter(w=>w.outerLayer===layer.layer||w.innerLayer===layer.layer).map(w=>w.rule))];
 const fiberJunctions=wiring.filter(w=>w.rule==='three-star-complete-exchange-with-retained-branch').flatMap(w=>[...new Set(w.branches.map(e=>e.to))].map(target=>({id:`belt:junction:${target}`,target,inputs:w.branches.filter(e=>e.to===target).sort((a,b)=>a.sourceAddress.star-b.sourceAddress.star).map(e=>e.from),law:fiberJunctionLaw.id,status:'trial',retainedModes:['common','contrast-1','contrast-2']})));
 return {version:2,spacing,pitch,origin:[...origin],x:[...x],y:[...y],normal:[...normal],layers,nodeCount:layers.reduce((n,l)=>n+l.nodeCount,0),wiring,fiberJunctions,links:wiring.flatMap(w=>w.branches)};
}
