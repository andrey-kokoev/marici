// Geometry-only projection of the existing folded 12×12 carrier.
// No flow, polarity, particle roles, or additional subdivisions are displayed.
import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {worldPoint} from './normal-ray-model.mjs';
import {buildPESymmetricSector} from '../strominger/pe-symmetric-sector.mjs';
const key=points=>points.map(p=>p.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
export function buildCellulationGeometry(source='fibration-12x12'){
 if(!['fibration-12x12','sulfur-32'].includes(source))throw Error('Unknown cellulation source');
 const geometry=source==='sulfur-32'?buildPESymmetricSector(1).cells:buildFoldedFibration().geometry;
 const cells=geometry.map(({id,kind,vertices,faces})=>({id,kind,vertices:vertices.map(worldPoint),faces:faces.map(f=>f.map(worldPoint))}));
 return packCellulation(cells,source);
}
export function packCellulation(cells,source){
 const faces=new Map(),edges=new Map();
 for(const cell of cells)for(const face of cell.faces){
  const k=key(face);if(!faces.has(k))faces.set(k,{vertices:face,owners:[]});faces.get(k).owners.push(cell.id);
  for(let i=0;i<3;i++){const edge=[face[i],face[(i+1)%3]],e=key(edge);if(!edges.has(e))edges.set(e,{vertices:edge,owners:new Set()});edges.get(e).owners.add(cell.id);}
 }
 if([...faces.values()].some(f=>f.owners.length>2))throw Error('Nonmanifold cellulation');
 return {source,cells,faces:[...faces.values()],edges:[...edges.values()].map(e=>({...e,owners:[...e.owners]}))};
}
