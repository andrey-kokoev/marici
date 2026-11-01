// A separate height-aligned reference pair, not a replacement for simplex paths.
export function buildSeedSidePair(layer,index,pairIndex=0){
 const sub=(a,b)=>a.map((x,i)=>x-b[i]),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
 const root=layer.nodes.find(n=>n.id===layer.root).point;
 const first=layer.edges.find(e=>e.role==='white'&&e.from===layer.root);
 const raw=sub(first.points[1],first.points[0]),direction=raw.map(x=>x/Math.hypot(...raw));
 const height=p=>dot(sub(p,root),direction),bands=new Map();
 for(const edge of layer.edges){
  const [start,end]=edge.points.map(height).sort((a,b)=>a-b),role=edge.role==='white'?'white':'exposed';
  const id=`${role}:${start.toFixed(9)}:${end.toFixed(9)}`;
  if(!bands.has(id))bands.set(id,{role,start,end,sourceEdges:[]});
  bands.get(id).sourceEdges.push(edge.id);
 }
 const intervals=[...bands.values()].sort((a,b)=>a.start-b.start);
 const maxX=Math.max(...layer.nodes.map(n=>n.point[0])),axisStart=[maxX+.8+.45*pairIndex,root[1],root[2]];
 const at=t=>axisStart.map((x,i)=>x+t*direction[i]);
 const firstBlue=layer.edges.find(e=>e.from===first.to&&e.role==='blue');
 const blueSide=Math.sign(firstBlue.points[1][0]-firstBlue.points[0][0]);
 const conductors=['blue','red'].map(colour=>({id:`${layer.id}:side-pair:${pairIndex+1}:${colour}`,colour,points:[]}));
 let halfTurns=0;
 for(const band of intervals){
  band.axisPoints=[at(band.start),at(band.end)];
  // One half-turn inside the sleeve, then one in the exposed band:
  // every exposed blue/red displacement keeps its source branch direction.
  const steps=32;
  for(let k=0;k<=steps;k++){
   if(k===0&&conductors[0].points.length)continue;
   const t=k/steps,axis=at(band.start+(band.end-band.start)*t),phase=Math.PI*(halfTurns+t);
   for(const conductor of conductors){
    const offset=(conductor.colour==='blue'?1:-1)*blueSide*.07*Math.cos(phase);
    conductor.points.push([axis[0]+offset,axis[1],axis[2]]);
   }
  }
  halfTurns++;
 }
 const totalHeight=Math.max(...layer.nodes.map(n=>height(n.point)));
 return {id:`${layer.id}:side-pair:${pairIndex+1}`,layerIndex:index,pairIndex,axis:[at(0),at(totalHeight)],direction,totalHeight,bands:intervals,conductors,
  bounds:[at(0).map((x,i)=>i===0?x-.14:x),at(totalHeight).map((x,i)=>i===0?x+.14:x)],
  clearanceFromSimplex:axisStart[0]-.14-maxX,
  representation:'planar drawing of one twisted pair; crossings are distinct conductors, not joins'};
}
