// Necessary conditions for a fixed identity bijection preserving shared
// segments, even after subdividing or contracting existing segments.
export function bundleInventory(edges){
 const bundles=new Map();
 for(const edge of edges){
  const members=[...new Set(edge.strands)].sort(),key=JSON.stringify(members);
  if(!members.length)continue;
  if(!bundles.has(key))bundles.set(key,{members,size:members.length,edges:[]});
  bundles.get(key).edges.push(edge.id);
 }
 const groups=[...bundles.values()],bySize={};
 for(const g of groups)bySize[g.size]=(bySize[g.size]??0)+1;
 return {groups,bySize};
}
export function checkRouteBundleCapacity(sourceEdges,targetEdges){
 const source=bundleInventory(sourceEdges),target=bundleInventory(targetEdges);
 const obstructions=Object.entries(target.bySize).filter(([size,count])=>count>(source.bySize[size]??0)).map(([size,count])=>({size:Number(size),availableSourceGroups:source.bySize[size]??0,requiredTargetGroups:count}));
 return {source,target,obstructions,necessaryConditionsSatisfied:obstructions.length===0,
  scope:'One fixed bijection of source conductors to target identities, preserving the exact identities sharing each represented segment. Subdivision repeats a bundle; contraction removes it. New inter-layer sewing, new overlaps, or partial chart occupancy are not covered.'};
}
