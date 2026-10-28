// Whole cells are nodes; a shared complete facet is one undirected link.
export function cellDualGraph(bodies){
 const nodes=bodies.map(body=>({id:body.id,body,position:body.vertices[0].map((_,i)=>body.vertices.reduce((s,p)=>s+p[i]/body.vertices.length,0))}));
 const facets=new Map();
 for(const b of bodies)for(const face of b.faces){
  const key=face.map(p=>p.map(x=>x.toFixed(8)).join(',')).sort().join('|');
  if(!facets.has(key))facets.set(key,[]);facets.get(key).push(b.id);
 }
 const links=[],seen=new Set();
 for(const ids of facets.values()){
  if(ids.length>2)throw Error('Nonmanifold cell graph facet');
  if(ids.length!==2)continue;
  const pair=[...ids].sort(),key=JSON.stringify(pair);if(seen.has(key))continue;seen.add(key);
  links.push({from:pair[0],to:pair[1]});
 }
 return {nodes,links};
}
