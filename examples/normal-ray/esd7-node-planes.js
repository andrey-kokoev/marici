import {buildFoldedFibration} from '../../research/realization-tower/fibration-folded-process.mjs';
const model=buildFoldedFibration(),byGeometry=new Map(model.geometry.map(b=>[b.id,b]));
// Actual centroid planes, not the three-family grouped vertex layers.
// The native opposite-tip axis is q[1]; the common face is q[1]=2.
const height=b=>Math.round(4*b.vertices.reduce((s,p)=>s+p[1]/b.vertices.length,0))/4;
const heights=[...new Set(model.geometry.map(height))].sort((a,b)=>b-a);
export const esd7NodePlanes=heights.map((h,index)=>({index,height:h,count:model.geometry.filter(b=>height(b)===h).length,label:index===0?'Face-side':index===1?'Immediately behind':`Plane ${index+1}`}));
export const esd7PlaneOf=new Map(model.occurrences.map(b=>[b.id,{copy:b.copy,index:heights.indexOf(height(byGeometry.get(b.sourceGeometry)))}]));
