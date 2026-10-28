// Trial fibre routing: opposite edge ports in each N octahedron. Shared edges
// connect fibres, NOT positive-area empty volumes. Crossing strands never merge.
const key=ps=>ps.map(p=>p.join(',')).sort().join('|'),mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i],0)/ps.length),d2=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);
export const nTubeAxes=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
export function buildNEdgeTubes(sector){
 const cells=sector.cells.filter(c=>c.role==='neutron'),passes=[],ports=new Map(),boundaryEdges=new Set();
 for(const f of sector.boundary)for(let i=0;i<3;i++)boundaryEdges.add(key([f.vertices[i],f.vertices[(i+1)%3]]));
 for(const cell of cells){const centre=mean(cell.vertices),edges=cell.vertices.flatMap((a,i)=>cell.vertices.slice(i+1).filter(b=>d2(a,b)===2).map(b=>[a,b])),edgeMap=new Map(edges.map(e=>[key(e),e])),used=new Set();
  for(const edge of edges){const a=key(edge);if(used.has(a))continue;const b=key(edge.map(p=>p.map((x,i)=>2*centre[i]-x))),other=edgeMap.get(b);if(!other)throw Error('Missing opposite N edge');used.add(a);used.add(b);const points=[mean(edge),mean(other)],direction=points[1].map((x,i)=>x-points[0][i]),active=direction.flatMap((x,i)=>x===0?[]:[i]),axis=nTubeAxes.findIndex(pair=>pair.every((x,i)=>x===active[i]));if(axis<0)throw Error('Non-native tube direction');
   const pass={id:`${cell.id}:axis:${axis}`,cell:cell.id,axis,portKeys:[a,b],points};passes.push(pass);for(const port of [a,b]){if(!ports.has(port))ports.set(port,[]);ports.get(port).push(pass);}
  }
 }
 for(const [port,ps]of ports){if(ps.length>2)throw Error('Ambiguous N edge junction');if(ps.length===1&&!boundaryEdges.has(port))throw Error('Unmatched N port is not on the boundary');if(ps.length===2&&ps[0].axis!==ps[1].axis)throw Error('Directions disagree at N edge');}
 const paths=[],seen=new Set();for(const start of passes)for(const startPort of start.portKeys){if(seen.has(start.id)||ports.get(startPort).length!==1)continue;let pass=start,entry=startPort;const steps=[],points=[start.points[start.portKeys.indexOf(entry)]];
  while(true){if(seen.has(pass.id))throw Error('Routing merged or cycled');seen.add(pass.id);steps.push(pass.id);const exitIndex=1-pass.portKeys.indexOf(entry),exit=pass.portKeys[exitIndex];points.push(pass.points[exitIndex]);const next=ports.get(exit).find(p=>p.id!==pass.id);if(!next)break;entry=exit;pass=next;}
  paths.push({id:`N-tube:${paths.length}`,axis:start.axis,passIds:steps,points,fromPort:startPort,toPort:pass.portKeys[1-pass.portKeys.indexOf(entry)]});
 }
 if(seen.size!==passes.length)throw Error('Untraced closed strand');
 const joins=[...ports.values()].filter(ps=>ps.length===2).length,axisCounts=nTubeAxes.map((axes,axis)=>({axis,axes,label:`q${axes[0]} − q${axes[1]}`,paths:paths.filter(p=>p.axis===axis).length}));
 return {passes,paths,axisCounts,audit:{rule:'opposite-edge N fibres',carrierCells:cells.length,strandsPerCell:6,localPasses:passes.length,sharedEdgeJoins:joins,compressedPaths:paths.length,boundaryEnds:2*paths.length,branchingJunctions:0,closedPaths:0,axisCounts,scope:'Explicit reversible edge-port routing assumption. Six independent N fibres per octahedron; no merging at cell centres. Zero-area contacts are not open voids, and channel counts are not neutron particle counts.'}};
}
