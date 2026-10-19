import {assembleComponents} from './simplex-components.mjs';
// Component assembly is authoritative; the grid is its deduplicated boundary graph.
export const resolution=7;
export const primitiveEdgeLength=6/7;
export const spaceScale=resolution/7;
export const vertices=[[0,0,0],[6,0,0],[3,3*Math.sqrt(3),0],[3,Math.sqrt(3),2*Math.sqrt(6)]].map(p=>p.map(x=>x/resolution));
const center=vertices.reduce((s,p)=>s.map((x,i)=>x+p[i]/4),[0,0,0]);
export const edges=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
export const faces=[[0,2,1],[0,1,3],[0,3,2],[1,2,3]];
export function validateCoordinate(q) {
  if(!Array.isArray(q)||q.length!==4||q.some(x=>!Number.isFinite(x))||Math.abs(q.reduce((a,b)=>a+b,0)-1)>1e-9)throw RangeError('Use four finite structural coordinates whose sum is 1.');
  return q;
}
export function worldPoint(q) {
  validateCoordinate(q);
  return center.map((c,i)=>vertices.reduce((s,v,j)=>s+q[j]*v[i],0)-c);
}
export const corners=vertices.map((_,i)=>vertices.map((__,j)=>Number(i===j)));
// Labels for the total space only; not a typing of lattice nodes or particles.
export const outerSpaceRoles=['codimension-one₀','main₀','codimension-one₁','main₁'];
export const envelopeCoordinates=corners.map(p=>p.map(x=>2-resolution*x));
export const outerSpaceEdges=edges.map(([from,to])=>({from,to,
  label:outerSpaceRoles[from]+' → '+outerSpaceRoles[to],
  start:worldPoint(envelopeCoordinates[from]),end:worldPoint(envelopeCoordinates[to])}));
export function makeSimplexLattice(n=resolution) {
  const assembly=assembleComponents(n),nodes=[],lookup=new Map(),edgeMap=new Map();
  // Shared coordinates identify one node, not overlapping copies of vertices.
  const cells=assembly.components.map(component=>component.addresses.map(address=>{
    const key=address.join(',');
    if(!lookup.has(key)){
      const coordinate=[...address];lookup.set(key,nodes.length);
      nodes.push({address:[...address],coordinate,point:worldPoint(coordinate)});
    }
    return lookup.get(key);
  }));
  for(const cell of cells)for(const [i,j] of edges){const pair=[cell[i],cell[j]].sort((a,b)=>a-b);edgeMap.set(pair.join(','),pair);}
  return {resolution:n,nodes,cells,edges:[...edgeMap.values()],assembly};
}
export const lattice=makeSimplexLattice();
export const coordinateBounds=[0,1,2,3].map(i=>({min:Math.min(...lattice.nodes.map(n=>n.address[i])),max:Math.max(...lattice.nodes.map(n=>n.address[i]))}));
// Depth of the assembled space: each regular tetrahedron or whole octahedral
// group is one element. Internal octahedron triangulation faces are not layers.
export function measureSurfaceLayers(space=lattice){
  const groupOf=space.assembly.components.map(c=>c.parent===null?'tetrahedron:'+c.id:'octahedron:'+c.parent);
  const adjacency=new Map(groupOf.map(g=>[g,new Set()])),incidence=new Map();
  space.cells.forEach((cell,id)=>{
    for(const face of faces){const key=face.map(i=>cell[i]).sort((a,b)=>a-b).join(',');
      if(!incidence.has(key))incidence.set(key,[]);incidence.get(key).push(groupOf[id]);}
  });
  const boundary=new Set();
  for(const groups of incidence.values()){
    if(groups.length===1)boundary.add(groups[0]);
    else if(groups.length===2){const [a,b]=groups;if(a!==b){adjacency.get(a).add(b);adjacency.get(b).add(a);}}
    else throw Error('Non-manifold assembly boundary');
  }
  const depth=new Map([...boundary].map(g=>[g,1])),queue=[...boundary];
  for(let i=0;i<queue.length;i++)for(const next of adjacency.get(queue[i]))if(!depth.has(next)){
    depth.set(next,depth.get(queue[i])+1);queue.push(next);
  }
  if(depth.size!==adjacency.size)throw Error('Disconnected surface-depth calculation');
  const counts={};for(const layer of depth.values())counts[layer]=(counts[layer]||0)+1;
  const cellLayers=groupOf.map(g=>depth.get(g)),maxLayer=Math.max(...cellLayers);
  return {groupOf,groupLayers:Object.fromEntries(depth),cellLayers,counts,maxLayer,
    deepestCellIds:cellLayers.flatMap((layer,id)=>layer===maxLayer?[id]:[])};
}
export const surfaceLayers=measureSurfaceLayers();
if(surfaceLayers.maxLayer!==4||surfaceLayers.deepestCellIds.length!==1)throw Error('Expected one element in the fourth surface layer');
// Local barycentric weights distinguish containment from proximity.
export function cellWeights(coordinate,cell) {
  validateCoordinate(coordinate);
  const [a,...rest]=cell.map(id=>lattice.nodes[id].coordinate.slice(0,3));
  const [u,v,w]=rest.map(p=>p.map((x,i)=>x-a[i]));
  const r=coordinate.slice(0,3).map((x,i)=>x-a[i]);
  const det=(u,v,w)=>u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0]);
  const d=det(u,v,w),weights=[det(r,v,w)/d,det(u,r,w)/d,det(u,v,r)/d];
  return [1-weights.reduce((s,x)=>s+x,0),...weights];
}
export const barycenter=[.25,.25,.25,.25];
const containing=lattice.cells.map((cell,id)=>({cell,id,weights:cellWeights(barycenter,cell)})).filter(c=>c.weights.every(w=>w>=-1e-10));
if(containing.length!==1||!containing[0].weights.every(w=>w>1e-10))throw Error('Barycenter has no unique strict-interior cell; an explicit boundary anchoring rule is needed.');
// Upright seed, not the old reflected T184 cell.
export const centralCellAddresses=corners;
const addressSet=cell=>cell.map(id=>lattice.nodes[id].address.join(',')).sort().join('|');
const centralKey=centralCellAddresses.map(a=>a.join(',')).sort().join('|');
const centralMatches=lattice.cells.map((cell,id)=>({cell,id})).filter(({cell})=>addressSet(cell)===centralKey);
if(centralMatches.length!==1||centralMatches[0].id!==containing[0].id)throw Error('Upright seed and barycenter containment disagree');
export const centralCellId=surfaceLayers.deepestCellIds[0];
if(centralCellId!==centralMatches[0].id)throw Error('Deepest assembled element is not the upright seed');
export const protonAnchor={cellId:centralCellId,coordinate:barycenter,weights:[.25,.25,.25,.25],location:'strict-interior'};
// Coordinate slabs only, NOT surface depth. Use surfaceLayers for depth.
export function cellFaceLayers(cellId){
  return [0,1,2,3].map(i=>{
    const values=lattice.cells[cellId].map(id=>lattice.nodes[id].address[i]);
    return {min:Math.min(...values),max:Math.max(...values),layer:Math.min(...values)-coordinateBounds[i].min+1};
  });
}
// Placement begins at the first constructed item, never an old numeric ID.
export const layerReferenceCellId=lattice.assembly.layers[0].items[0].children[0];
if(layerReferenceCellId!==centralCellId)throw Error('Layer-zero seed must match the central cell');
// Select actual incident cells, never independently embed or reflect carriers.
const neighbor=(face,exclude)=>lattice.cells.findIndex((cell,i)=>!exclude.includes(i)&&face.every(v=>cell.includes(v)));
const candidates=containing;
let placement;
for(const {cell:p,id:pi} of candidates) {
  const ni=neighbor(p.slice(1),[pi]);if(ni<0)continue;
  const c2=lattice.cells[ni].find(v=>!p.includes(v));
  const face=[p[3],p[2],c2],ei=neighbor(face,[pi,ni]);if(ei<0)continue;
  const m2=lattice.cells[ei].find(v=>!face.includes(v));if(p.includes(m2))continue;
  placement={nodeIds:{C0:p[0],M0:p[1],C1:p[2],M1:p[3],C2:c2,M2:m2},cellIds:[pi,ni,ei]};break;
}
if(!placement)throw Error('No three-cell carrier chain in lattice');
export const nodeIds=placement.nodeIds;
export const coordinates=Object.fromEntries(Object.entries(nodeIds).map(([name,id])=>[name,lattice.nodes[id].coordinate]));
Object.values(coordinates).forEach(validateCoordinate);
export const bodies=[
  {id:'proton',symbol:'P',signature:'C₀ M₀ C₁ [M₁]',names:['C0','M0','C1','M1'],color:0x6baec8,construction:'Proton: the selected center cell C₀ M₀ C₁ [M₁].'},
  {id:'neutron',symbol:'N',signature:'M₀ C₁ M₁ [C₂]',names:['M0','C1','M1','C2'],color:0xd7ae77,construction:'Neutron: the adjacent lattice cell across the M₀ C₁ M₁ face.'},
  {id:'electron',symbol:'E',signature:'M₁ C₁ C₂ [M₂]',names:['M1','C1','C2','M2'],color:0xf19ad0,construction:'Trial electron: the adjacent lattice cell across the M₁ C₁ C₂ face.'},
];
bodies.forEach((body,i)=>{body.cellId=placement.cellIds[i];body.nodeIds=body.names.map(n=>nodeIds[n]);});
export function cellNeighbors(cellId) {
  const cell=lattice.cells[cellId];if(!cell)throw RangeError('Unknown cell');
  return cell.map((_,i)=>neighbor(cell.filter((__,j)=>j!==i),[cellId]));
}
export function placementAtCell(cellId=protonAnchor.cellId) {
  const cell=lattice.cells[cellId];if(!cell)throw RangeError('Unknown cell');
  // Keep the chosen P cell fixed; find a valid two-face N/E continuation.
  for(const c0 of cell)for(const m0 of cell.filter(v=>v!==c0))for(const c1 of cell.filter(v=>v!==c0&&v!==m0)){
    const m1=cell.find(v=>v!==c0&&v!==m0&&v!==c1);
    const ni=neighbor([m0,c1,m1],[cellId]);if(ni<0)continue;
    const c2=lattice.cells[ni].find(v=>!cell.includes(v));
    const ei=neighbor([m1,c1,c2],[cellId,ni]);if(ei<0)continue;
    const m2=lattice.cells[ei].find(v=>![m1,c1,c2].includes(v));if(cell.includes(m2))continue;
    const bindings={C0:c0,M0:m0,C1:c1,M1:m1,C2:c2,M2:m2};
    const coordinate=cell.reduce((s,id)=>s.map((x,i)=>x+lattice.nodes[id].address[i]),[0,0,0,0]).map(x=>x/4);
    return {nodeIds:bindings,bodies:bodies.map((b,i)=>({...b,cellId:[cellId,ni,ei][i],nodeIds:b.names.map(n=>bindings[n])})),anchor:{cellId,coordinate,weights:[.25,.25,.25,.25],location:'strict-interior'}};
  }
  throw RangeError('No three-cell continuation at this cell');
}
// Move one coordinate slab while minimizing lateral displacement. The
// simplex sum is preserved by distributing the compensating displacement
// equally across the other three coordinates; choose an actual existing cell.
export function nextLayerCell(cellId,axis,step){
  if(!lattice.cells[cellId]||!Number.isInteger(axis)||axis<0||axis>3||![1,-1].includes(step))throw RangeError('Invalid layer move');
  const targetLayer=cellFaceLayers(cellId)[axis].layer+step;
  const extent=coordinateBounds[axis].max-coordinateBounds[axis].min;
  if(targetLayer<1||targetLayer>extent)return null;
  const centroid=id=>lattice.cells[id].reduce((s,v)=>s.map((x,i)=>x+lattice.nodes[v].address[i]/4),[0,0,0,0]);
  const target=centroid(cellId).map((x,i)=>x+(i===axis?step:-step/3));
  const candidates=lattice.cells.flatMap((_,id)=>cellFaceLayers(id)[axis].layer===targetLayer?[{id,score:centroid(id).reduce((s,x,i)=>s+(x-target[i])**2,0)}]:[]).sort((a,b)=>a.score-b.score||a.id-b.id);
  for(const {id} of candidates){try{placementAtCell(id);return id;}catch{}}
  return null;
}
export function selectCarriers(mode='none',cellId=protonAnchor.cellId) {
  const ids=Array.isArray(mode)?mode:mode==='all'?bodies.map(b=>b.id):mode==='none'?[]:[mode];
  if(ids.some(id=>!bodies.some(b=>b.id===id)))throw RangeError('Unknown carrier selection');
  const placement=placementAtCell(cellId),selected=placement.bodies.filter(b=>ids.includes(b.id));
  const names=[...new Set(selected.flatMap(b=>b.names))],bindings=placement.nodeIds;
  return {anchor:placement.anchor,bodies:selected,coordinates:Object.fromEntries(names.map(n=>[n,lattice.nodes[bindings[n]].coordinate])),nodeIds:Object.fromEntries(names.map(n=>[n,bindings[n]])),points:Object.fromEntries(names.map(n=>[n,lattice.nodes[bindings[n]].point]))};
}
