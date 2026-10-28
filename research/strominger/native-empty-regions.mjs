// Occupancy hypothesis: P/E cells occupied, N octahedra empty. A positive-area
// shared face connects open 3D voids; edge/point-only touching does not.
export function nativeEmptyRegions(sector){
 const empty=sector.cells.filter(c=>c.role==='neutron'),ids=new Set(empty.map(c=>c.id)),surface=new Set(sector.boundary.flatMap(f=>f.owners)),adj=new Map(empty.map(c=>[c.id,new Set()]));let sharedFaces=0;
 for(const f of sector.faces)if(f.owners.length===2&&f.owners.every(id=>ids.has(id))){sharedFaces++;const[a,b]=f.owners;adj.get(a).add(b);adj.get(b).add(a);}
 function components(graph){const unseen=new Set(graph.keys()),result=[];while(unseen.size){const queue=[unseen.values().next().value];unseen.delete(queue[0]);for(let i=0;i<queue.length;i++)for(const next of graph.get(queue[i]))if(unseen.delete(next))queue.push(next);result.push(queue);}return result;}
 const regions=components(adj).map((cellIds,i)=>({id:`empty-region:${i}`,cellIds,opensToExterior:cellIds.some(id=>surface.has(id))}));
 const vertexOwners=new Map();for(const c of empty)for(const p of c.vertices){const k=p.join(',');if(!vertexOwners.has(k))vertexOwners.set(k,[]);vertexOwners.get(k).push(c.id);}
 const contacts=new Map();for(const owners of vertexOwners.values())for(let i=0;i<owners.length;i++)for(let j=i+1;j<owners.length;j++){const pair=[owners[i],owners[j]].sort(),k=pair.join('|');if(!contacts.has(k))contacts.set(k,{pair,sharedVertices:0});contacts.get(k).sharedVertices++;}
 const closedContactComponents=threshold=>{const graph=new Map(empty.map(c=>[c.id,new Set()]));for(const c of contacts.values())if(c.sharedVertices>=threshold){const[a,b]=c.pair;graph.get(a).add(b);graph.get(b).add(a);}return components(graph).length;};
 const interior=regions.filter(r=>!r.opensToExterior),open=regions.filter(r=>r.opensToExterior);
 return {regions,emptyCells:empty.length,sharedEmptyFaces:sharedFaces,enclosedRegions:interior.length,surfaceOpeningRegions:open.length,regionsWithinCarrier:regions.length,regionsIncludingExterior:interior.length+1,exteriorComponentCount:1,edgeTouchComponents:closedContactComponents(2),vertexTouchComponents:closedContactComponents(1),scope:'P/E occupied, N empty is a trial occupancy model. Enclosed filler voids use shared-face connectivity. Boundary openings merge through one unbounded exterior, which is not a neutron cavity. Lower-dimensional contacts are diagnostics only.'};
}
