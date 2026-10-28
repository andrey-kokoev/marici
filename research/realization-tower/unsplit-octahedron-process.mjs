import {seed} from './normal-ray-model.mjs';
export const octahedronStages=Object.freeze(['One unsplit octahedron: 6 vertices, 12 edges, 8 faces. No subdivision diagonal.','Mark both sides of each face: teal outward, amber inward. These are interface directions, not extra cells.']);
const center=[.25,.25,.25,.25];
const pairs=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
const vertices=pairs.map(pair=>center.map((x,i)=>x+(pair.includes(i)?.5:-.5)));
const d2=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);
const edges=vertices.flatMap((a,i)=>vertices.slice(i+1).flatMap((b,j)=>d2(a,b)===2?[[i,i+j+1]]:[]));
const faceIndices=[];
for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)if(d2(vertices[i],vertices[j])===2&&d2(vertices[j],vertices[k])===2&&d2(vertices[k],vertices[i])===2)faceIndices.push([i,j,k]);
const faces=faceIndices.map(f=>f.map(i=>vertices[i]));
export function unsplitOctahedronProcess(k,step){
 if(!Number.isInteger(k)||k<1||k>7||!Number.isInteger(step)||step<0||step>=octahedronStages.length)throw Error('Invalid octahedron step');
 const guides=[];
 const sides=faces.map((face,i)=>{
  const point=center.map((_,j)=>face.reduce((s,v)=>s+v[j]/3,0)),direction=point.map((x,j)=>x-center[j]);
  const norm=Math.hypot(...direction),offset=direction.map(x=>x*.22/norm);
  const outward=point.map((x,j)=>x+offset[j]),inward=point.map((x,j)=>x-offset[j]);
  if(step===1){guides.push({id:`face${i}-outside`,points:[point,outward],color:0x67c9c2});guides.push({id:`face${i}-inside`,points:[point,inward],color:0xe5ae55});}
  return {face:i+1,vertices:faceIndices[i],point,outward,inward};
 });
 return {k:7,step,end:seed,assignments:[],firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],
 retainedBodies:[{id:'unsplit-octahedron',kind:'octahedron',faces,components:[],color:0x9dbbd6,opacity:.18,round:0}],
 presentationLabels:[],interfaceGuides:guides,
 presentationAudit:{nativeRealization:false,fixedCellSize:true},
 octahedronAudit:{vertices,edges,faceIndices,sides,vertexCount:6,edgeCount:12,faceCount:8,bodyCount:1,internalEdges:0,subdivided:false},
 summary:`Step ${step+1} — ${octahedronStages[step]}`,canAdvance:step===0,history:octahedronStages.slice(0,step+1).map((rule,round)=>({round,rule}))};
}
