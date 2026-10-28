// Symbolic 2×2 block aggregation. A bundle address PLUS its branch address
// recovers the fine address exactly; aggregation never erases the branch.
export function encodeBlockAddress({row,column}){
 if(![row,column].every(n=>Number.isInteger(n)&&n>=0&&n<4))throw Error('Expected a 4×4 grid address');
 return {bundle:{row:Math.floor(row/2),column:Math.floor(column/2)},branch:{row:row%2,column:column%2}};
}
export function decodeBlockAddress({bundle,branch}){
 if(![bundle.row,bundle.column,branch.row,branch.column].every(n=>n===0||n===1))throw Error('Expected binary bundle and branch addresses');
 return {row:2*bundle.row+branch.row,column:2*bundle.column+branch.column};
}
function orientedAddress(node,layer){
 let {row,column}=node,turns=((layer.rotationDegrees%360)+360)%360/90;
 if(!Number.isInteger(turns))throw Error('Grid wiring requires quarter-turn orientations');
 const size=layer.rows.length;
 while(turns-->0)[row,column]=[size-1-column,row];
 return {row,column};
}
const key=a=>`${a.row}:${a.column}`;
export const outerPerimeter=Object.freeze([[0,0],[0,1],[0,2],[0,3],[1,3],[2,3],[3,3],[3,2],[3,1],[3,0],[2,0],[1,0]].map(Object.freeze));
export function instantiateBlockWiring(outer,inner){
 if(!['grid','star-array','tube-ports'].includes(outer.kind)||!['grid','node-star'].includes(inner.kind)||outer.rows.length!==4||outer.rows.some(r=>r.length!==4)||inner.rows.length!==2||inner.rows.some(r=>r.length!==2))throw Error('Block wiring requires 4×4 and 2×2 address sets');
 const coarse=new Map(inner.nodes.map(n=>[key(orientedAddress(n,inner)),n]));
 const perimeter=outerPerimeter;
 const centred=outer.bundleLayout==='central-block-and-three-rim-bundles';
 const branches=outer.nodes.map(node=>{
  // Star arms already carry the geometric rotation. Do not rotate their
  // legacy grid addresses a second time when assigning transport bundles.
  const oriented=['star-array','tube-ports'].includes(outer.kind)?{row:node.row,column:node.column}:orientedAddress(node,outer);let address;
  if(centred){
   if(!inner.starSlots)throw Error('Centred outer bundles require a star destination');
   const central=[1,2].includes(oriented.row)&&[1,2].includes(oriented.column),rimIndex=perimeter.findIndex(([r,c])=>r===oriented.row&&c===oriented.column);
   const bundleSlot=inner.starSlots[central?3:Math.floor(rimIndex/4)],branchSlot=central?2*(oriented.row-1)+oriented.column-1:rimIndex%4;
   address={bundle:{row:Math.floor(bundleSlot/2),column:bundleSlot%2},branch:{row:Math.floor(branchSlot/2),column:branchSlot%2},fineAddress:oriented,region:central?'centre':'perimeter'};
  }else address=encodeBlockAddress(oriented);
  const target=coarse.get(key(address.bundle));
  if(node.direction!==target.direction)throw Error('Incompatible transport directions within a bundle');
  // P travels toward increasing plane coordinate; E toward decreasing.
  const outerToInner=node.direction==='P'?inner.plane>outer.plane:inner.plane<outer.plane;
  return {id:`belt:wire:${outer.layer}:${inner.layer}:${node.slot}`,kind:'belt-transport',from:outerToInner?node.id:target.id,to:outerToInner?target.id:node.id,direction:node.direction,outer:node.id,inner:target.id,...address};
 });
 return {rule:centred?'central-block-and-three-rim-bundles':'2×2-block-with-retained-branch',outerLayer:outer.layer,innerLayer:inner.layer,branches};
}
// Each uniform triangle retains an explicit square-bundle address, independent
// of its current centre placement.
// Retain each triangle vertex as a distinct symbolic branch.
export function instantiateTriangleWiring(square,triangles,direction){
 if(!['grid','node-star'].includes(square.kind)||triangles.kind!=='bundle-stars')throw Error('Expected four-bundle and central bundle-star layers');
 const targets=new Map(square.nodes.map(n=>[key(orientedAddress(n,square)),n])),groups=triangles.groups.map((pattern,i)=>pattern===direction.repeat(3)?i:-1).filter(i=>i>=0);
 if(!triangles.bundleSlots||new Set(triangles.bundleSlots).size!==4)throw Error('Expected four retained bundle slots');
 const branches=groups.flatMap(group=>{
  const slot=triangles.bundleSlots[group],quadrant={row:Math.floor(slot/2),column:slot%2},target=targets.get(key(quadrant));
  if(!target||target.direction!==direction)throw Error('Triangle direction does not match its retained square bundle');
  return triangles.nodes.filter(n=>n.group===group).map(node=>{
   const towardSquare=direction==='P'?square.plane>triangles.plane:square.plane<triangles.plane;
   return {id:`belt:triangle-wire:${triangles.layer}:${square.layer}:${node.slot}`,kind:'belt-transport',from:towardSquare?node.id:target.id,to:towardSquare?target.id:node.id,direction,outer:target.id,inner:node.id,group,branch:{vertex:node.vertex}};
  });
 });
 return {rule:'uniform-triangle-to-matching-square',outerLayer:square.layer,innerLayer:triangles.layer,branches};
}

// Transpose the 3×3 branch table: source bundle k, branch j goes to
// destination triangle j, vertex k. Source bundle order is inherited from
// the retained bundle-slot correspondence, so changing geometry preserves wiring.
export function instantiateTriangleInterleave(square,triangles,direction){
 const direct=instantiateTriangleWiring(square,triangles,direction),groups=[...new Set(direct.branches.map(e=>e.group))];
 if(groups.length!==3)throw Error('Interleaving requires three source bundles and three triangles');
 if((triangles.plane-square.plane)*(direction==='P'?1:-1)<=0)throw Error('Interleave conflicts with transport heading');
 const sources=groups.map(group=>direct.branches.find(e=>e.group===group).outer);
 const branches=direct.branches.map(edge=>{
  const bundle=edge.branch.vertex,lane=groups.indexOf(edge.group),source=sources[bundle];
  return {...edge,from:source,to:edge.inner,outer:source,branch:{bundle,lane},sourceAddress:{bundle,lane},destinationAddress:{triangle:lane,vertex:bundle}};
 });
 return {rule:'three-bundle-transpose',outerLayer:square.layer,innerLayer:triangles.layer,branches};
}

// Complete directed 3×3 star exchange: one satellite per opposite centre.
// Arm k feeds opposite star k in both directions, preserving threefold symmetry.
// Keep symbolic source (group,vertex) records alongside explicit star addresses.
export function instantiateTriangleExchange(source,target,direction){
 if(source.kind!=='bundle-stars'||target.kind!=='bundle-stars')throw Error('Central exchange requires two bundle-star layers');
 const sourceGroups=source.groups.map((p,i)=>p===direction.repeat(3)?i:-1).filter(i=>i>=0),targetGroups=target.groups.map((p,i)=>p===direction.repeat(3)?i:-1).filter(i=>i>=0);
 if(sourceGroups.length!==3||targetGroups.length!==1)throw Error('Expected three source triangles and one destination triangle');
 if((target.plane-source.plane)*(direction==='P'?1:-1)<=0)throw Error('Exchange conflicts with transport heading');
 const destinations=new Map(target.nodes.filter(n=>n.group===targetGroups[0]).map(n=>[n.star,n]));
 const branches=source.nodes.filter(n=>sourceGroups.includes(n.group)).map(node=>{
  const targetStar=node.arm;
  return {id:`belt:exchange:${source.layer}:${target.layer}:${node.slot}`,kind:'belt-transport',from:node.id,to:destinations.get(targetStar).id,direction,branch:{group:node.group,vertex:node.vertex},sourceAddress:{star:node.star,arm:node.arm},destinationAddress:{star:targetStar,centre:true}};
 });
 return {rule:'three-star-complete-exchange-with-retained-branch',outerLayer:source.layer,innerLayer:target.layer,branches};
}

// Reverse the directed relation without deleting the bundle/branch witness.
// P/E here are transport headings: reversing a directed edge exchanges them.
export function reverseBlockWiring(wiring){
 return {...wiring,branches:wiring.branches.map(edge=>({...edge,from:edge.to,to:edge.from,direction:edge.direction==='P'?'E':'P'}))};
}
