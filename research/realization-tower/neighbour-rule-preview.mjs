// Completion rule for whole tetrahedra; neighbours are shared-facet cells.
export function previewNeighbourRule(geometry,links,assigned){
 const roles=new Map(assigned.map(b=>[b.id,b.role])),neighbors=new Map(geometry.map(b=>[b.id,new Set()]));
 for(const {from,to} of links){neighbors.get(from).add(to);neighbors.get(to).add(from);}
 const rule='Tetrahedron with 3P + 1N face-neighbours → P',candidates=[],conflicts=[];
 for(const cell of geometry){
  if(cell.kind!=='tetrahedron')continue;
  const ids=[...neighbors.get(cell.id)],ns=ids.map(id=>({cell:id,role:roles.get(id)??null}));
  if(ns.length!==4||ns.filter(n=>n.role==='proton').length!==3||ns.filter(n=>n.role==='neutron').length!==1)continue;
  const arrivals=ns.map(n=>({source:n.cell,target:cell.id,role:'proton',neighborRole:n.role,rule,front:'local',direction:'coherence'}));
  if(roles.has(cell.id)){if(roles.get(cell.id)!=='proton')conflicts.push({id:cell.id,existingRole:roles.get(cell.id),arrivals});}
  else candidates.push({id:cell.id,role:'proton',round:1,arrivals});
 }
 const valid=!conflicts.length;
 return {valid,candidates:valid?candidates:[],rounds:valid&&candidates.length?[{round:1,ids:candidates.map(c=>c.id)}]:[],conflicts,rules:[rule],seamTransfers:[]};
}
