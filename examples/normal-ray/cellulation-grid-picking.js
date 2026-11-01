export function cellulationGridVertices(edges){
 const vertices=new Map();
 for(const edge of edges)for(const point of edge.vertices){
  const latticePoint=point.map(x=>Math.round(x*Math.SQRT2)),key=latticePoint.join(',');
  if(!vertices.has(key))vertices.set(key,{key,point,latticePoint});
 }
 return [...vertices.values()];
}
// Screen-space picking: fixed CSS-pixel radius, and frontmost vertex breaks ties.
export function pickCellulationGridVertex(vertices,{pointer,width,height,project,excluded=new Set(),radius=10}){
 if(!pointer)return null;let best=null,distance=radius*radius;
 for(const vertex of vertices){
  if(excluded.has(vertex.key))continue;
  const p=project(vertex.point);if(Math.abs(p.x)>1||Math.abs(p.y)>1||Math.abs(p.z)>1)continue;
  const x=(p.x+1)*width/2,y=(1-p.y)*height/2,d=(x-pointer.x)**2+(y-pointer.y)**2;
  if(d>distance+1e-8||best&&Math.abs(d-distance)<1e-8&&p.z>=best.depth)continue;
  distance=d;best={...vertex,x,y,depth:p.z};
 }
 return best;
}
