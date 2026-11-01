// Vertex normals are the outward centroid-to-vertex normals of the regular seed.
export function cellulationDotAnchors(model,turnMarkers=[]){
 if(!model.markedVertex)return [];
 const vertices=model.cells[0].vertices,center=[0,1,2].map(i=>vertices.reduce((sum,p)=>sum+p[i]/4,0));
 const entries=[{id:'seed',name:'top dot',point:model.markedVertex}];
 if(model.proposedVertex)entries.push({id:'witness',name:'witness dot',point:model.proposedVertex});
 for(const marker of turnMarkers)if(marker.outlineVisible||marker.solidVisible)entries.push({id:marker.id,name:marker.name,point:marker.point});
 return entries.map(a=>{const n=a.point.map((x,i)=>x-center[i]),length=Math.hypot(...n);return {...a,point:[...a.point],normal:n.map(x=>x/length)};});
}
